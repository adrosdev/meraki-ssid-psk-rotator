"""meraki-ssid-psk-rotator — v0.4

This project is intentionally built in visible stages (v0.1 → v1.0),
refactoring toward production practices one step at a time.
See README for the roadmap. Do not use before v1.0.
"""

from pathlib import Path
import random
BASE_DIR = Path(__file__).parent

network_all = ["branch1", "branch2", "branch3", "branch4", "mainoffice"]

class Network:

    def __init__(self, name):
        self.name = name
        self.status = "pending"

    def rotate(self):
        if random.random() < 0.3:
            raise ConnectionError(f"Simulated timeout for {self.name}")
        print(f"Rotating PSK for {self.name}")
        self.status = "rotated"


def selected_networks(path):
    """Read selected network names from a file, one per line. Return a clean list"""
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

def main():
    """Run one rotation: load selected networks and rotate them."""

    networks = selected_networks(BASE_DIR / "selected_networks.txt")
    fleet = []

    for name in network_all:
        fleet.append(Network(name))


    for network in fleet:
        if network.name in networks:
            try:
                network.rotate()
            except ConnectionError as e:
                print(f"{network.name} FAILD {e}")
                network.status =  "skipped"
        else:
            print(f"{network.name} skipped")
            network.status =  "skipped"

    rotated = [n.name for n in fleet if n.status == "rotated"]
    skipped = [n.name for n in fleet if n.status ==  "skipped"]
    failed  = [n.name for n in fleet if n.status == "failed"]

    result = [f"{n.name}: {n.status}" for n in fleet]
    print(f"{len(rotated)} rotated. {len(skipped)} skipped. {len(failed)} FAILD")
    (BASE_DIR / "result.txt").write_text("\n".join(result))


if  __name__ ==  "__main__":
    main()