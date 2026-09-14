"""meraki-ssid-psk-rotator — v0.6

This project is intentionally built in visible stages (v0.1 → v1.0),
refactoring toward production practices one step at a time.
See README for the roadmap. Do not use before v1.0.
"""

from pathlib import Path
import os
import requests
from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")
API_KEY = os.environ.get("MERAKI_API_KEY")
BASE_URL = "https://api.meraki.com/api/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
TARGET_SSID = "guest-wifi"
NEW_PSK = os.environ.get("NEW_PSK")
DRY_RUN = True

class Network:

    def __init__(self, name, network_id):
        self.name = name
        self.network_id = network_id
        self.status = "pending"

    def rotate(self):
        """Rotate this network's PSK for TARGET_SSID. Honors DRY_RUN."""

        url = f"{BASE_URL}/networks/{self.network_id}/wireless/ssids"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        ssids = response.json()

        target = None

        for ssid in ssids:
            if ssid["name"] == TARGET_SSID:
                target = ssid
                break

        if target is None:
            raise ValueError(f"SSID '{TARGET_SSID}' is not found on {self.name}")

        if DRY_RUN:
            print(f"[DRY RUN] {self.name}: would set new PSK on SSID {target['number']} ('{TARGET_SSID}')")
            self.status = "rotated"
            return
        
        put_url = f"{url}/{target['number']}"
        response = requests.put(put_url, headers=HEADERS, json={"psk": NEW_PSK})
        response.raise_for_status()
        print(f"{self.name}: PSK rotated on SSID {target['number']}")
        self.status = "rotated"       


def selected_networks(path):
    try:
        lines = Path(path).read_text().splitlines()
    except FileNotFoundError:
        print(f"{path} file not found.")
        return []
    networks =  []
    for line in lines:
        name = line.strip()
        if name == "":
            continue
        networks.append(name)
    return networks

def get_org_id():
    response = requests.get(f"{BASE_URL}/organizations", headers=HEADERS)
    response.raise_for_status()
    orgs  = response.json()
    return orgs[0]["id"]

def get_networks(orgs_id):
    response  = requests.get(f"{BASE_URL}/organizations/{orgs_id}/networks", headers=HEADERS)
    response.raise_for_status()
    return response.json()



def main():

    networks = selected_networks(BASE_DIR / "selected_networks.txt")

    org_id = get_org_id()
    network_data = get_networks(org_id)

    fleet = []

    for net in network_data:
        fleet.append(Network(net["name"], net["id"]))


    for network in fleet:
        if network.name in networks:
            try:
                network.rotate()
            except (requests.RequestException, ValueError) as e:
                print(f"{network.name} FAILED {e}")
                network.status =  "failed"
        else:
            print(f"{network.name} skipped")
            network.status =  "skipped"

    rotated = [n.name for n in fleet if n.status == "rotated"]
    skipped = [n.name for n in fleet if n.status ==  "skipped"]
    failed  = [n.name for n in fleet if n.status == "failed"]

    result = [f"{n.name}: {n.status}" for n in fleet]
    print(f"{len(rotated)} rotated. {len(skipped)} skipped. {len(failed)} FAILED")
    (BASE_DIR / "result.txt").write_text("\n".join(result))


if  __name__ ==  "__main__":
    main()