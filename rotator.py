"""meraki-ssid-psk-rotator — v0.1

Early iteration: everything hardcoded, rotation simulated.
This project is intentionally built in visible stages (v0.1 → v1.0),
refactoring toward production practices one step at a time.
See README for the roadmap. Do not use before v1.0.
"""


network_all = ["branch1", "branch2", "branch3", "branch4", "mainoffice"]

network_selected = ["branch1", "branch3"]

network_rotated = 0
network_skipped = 0

for network in network_all:
    if network in network_selected:
        print(f"Rotating PSK for {network}")
        network_rotated += 1
    else:
        print(f"{network} skipped.")
        network_skipped += 1

print(f"{network_rotated} rotated, {network_skipped} skipped")