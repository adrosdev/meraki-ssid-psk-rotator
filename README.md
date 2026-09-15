<div align="center">

# meraki-ssid-psk-rotator

**One command. Every guest network. New password.**

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Tests](https://github.com/adrosdev/meraki-ssid-psk-rotator/actions/workflows/tests.yaml/badge.svg)](https://github.com/adrosdev/meraki-ssid-psk-rotator/actions)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Rotates the pre-shared key of a chosen SSID across selected networks in a
Meraki organization — built for recurring guest WiFi password changes.

Built by [**Adris Sahray**](https://www.linkedin.com/in/mohammad-adris-s-51ab33221/)

</div>

---

## Why

Guest WiFi passwords should rotate regularly. Doing it by hand across an
organization means logging into the dashboard and editing the same SSID on
every network — slow, error-prone, and easy to postpone. This tool does it
in one run: pick the networks, set the new PSK once, every selected network
gets it. One network failing doesn't stop the rest.

## How it looks

```text
$ python rotator.py
[INFO]    Networks found: 4
[DRY RUN] branch3: SSID 0 ('GuestWiFi')
[DRY RUN] branch4: SSID 1 ('GuestWiFi')
[DRY RUN] branch1: SSID 0 ('GuestWiFi')
[FAILED]  branch2: 'GuestWiFi' SSID is not found
----
3 rotated, 0 skipped, 1 failed
```

Dry run is the default. Add `--execute` to perform the rotation.

## Quick start

1. Clone and install:

```text
   git clone https://github.com/adrosdev/meraki-ssid-psk-rotator.git
   cd meraki-ssid-psk-rotator
   python -m venv .venv && .venv\Scripts\activate
   pip install -r requirements.txt
```

2. Create a `.env` (never committed — see Security):

```text
   MERAKI_API_KEY=your-40-char-dashboard-api-key
   NEW_PSK=the-new-guest-password
```

3. List the networks to rotate in `selected_networks.txt`, one name per line.

4. Set `TARGET_SSID` in `rotator.py` to your SSID's name, then run:

```text
   python rotator.py             # dry run — reports what would change
   python rotator.py --execute   # performs the rotation
   python rotator.py --help      # all options
```

## Security posture

- No secret ever appears in the code, at any stage of this project's history
- API key and PSK enter via environment variables only (`.env` is gitignored)
- The new PSK is never printed or written to any log or results file
- Dry-run is the default; writes are opt-in

## Roadmap

Built deliberately in public iterations, each tagged:

| Version | Focus | |
|---------|-------|---|
| v0.1 | Crude simulated rotation, everything hardcoded | ✅ |
| v0.2 | Network selection from file, results log | ✅ |
| v0.3 | Per-network failure isolation | ✅ |
| v0.4 | `Network` class carries rotation state | ✅ |
| v0.5 | Real Meraki API, dry-run rotation, secrets via `.env` | ✅ |
| v0.6 | pytest test suite | ✅ |
| v0.7 | CLI flags, output polish, CI | 🔨 |

Not production-ready before v1.0. The git tags are the story — diff any two
versions to watch the refactors happen.

## Support & contribute

If this tool is useful to you:

- ⭐ **Star the repo** — it helps others find it
- 🐛 **Open an issue** — bugs, ideas, or questions about the approach are warmly welcome
- 🔀 **Contribute** — PRs are open; the roadmap above shows where the project is heading

---