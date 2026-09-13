"""meraki-ssid-psk-rotator — v0.1

This project is intentionally built in visible stages (v0.1 → v1.0),
refactoring toward production practices one step at a time.
See README for the roadmap. Do not use before v1.0.
"""

from pathlib import Path

network_all = ["branch1", "branch2", "branch3", "branch4", "mainoffice"]

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

def rotate_network(networks):
    """Simulate PSK rotation for each network in the selected list; write results.txt and print a summary."""
    network_rotated = 0
    network_skipped = 0
    result = []

    for network in network_all:
        if network in networks:
            print(f"Rotating PSK for {network}")
            network_rotated += 1
            result.append(f"{network} rotated")
        else:
            print(f"{network} skipped.")
            network_skipped += 1
            result.append(f"{network} skipped")

    print(f"{network_rotated} rotated, {network_skipped} skipped")
    Path("result.txt").write_text("\n".join(result))

def main():
    """Run one rotation: load selected networks and rotate them."""

    networks = selected_networks("selected_networks.txt")

    rotate_network(networks)

if  __name__ ==  "__main__":
    main()