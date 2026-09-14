<div align="center">

# meraki-ssid-psk-rotator

**One command. Every guest network. New password.**

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-pre--release-orange)](#roadmap)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Rotates the pre-shared key of a chosen SSID across selected networks in a
Meraki organization — built for recurring guest WiFi password changes.

[**adros.dev**](https://adros.dev)

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
[DRY RUN] branch_office: would set new PSK on SSID 2 ('guest-wifi')
branch_office2 skipped
1 rotated, 0 failed, 1 skipped
```

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

4. Set `TARGET_SSID` in `rotator.py` to your SSID's name, then run. The tool
   is **dry-run by default** — it reports what it would change. Set
   `DRY_RUN = False` to execute.

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
| v0.6 | pytest test suite | 🔨 |
| v0.7 | CLI flags, CI | — |

Not production-ready before v1.0. The git tags are the story — diff any two
versions to watch the refactors happen.

## Support & contribute

If this tool is useful to you:

- ⭐ **Star the repo** — it helps others find it
- 🐛 **Open an issue** — bugs, ideas, or questions about the approach are  warmly welcomed
- 🔀 **Contribute** — PRs are open; the roadmap above shows where the project is heading

---