# meraki-ssid-psk-rotator

Rotates the pre-shared key of a chosen SSID across selected networks in a Meraki organization. Under active development — Built by [Adris](https://adros.dev).

## Project roadmap

Built deliberately in public iterations, each tagged:

- **v0.1** — crude simulated rotation ✅
- **v0.2** — config moves to files, logic into functions ✅
- **v0.3** — error handling and per-network failure isolation
- **v0.4** — class-based structure
- **v0.5** — real Meraki API (env-var credentials, dry-run mode)
- **v0.6** — pytest test suite
- **v0.7** — CLI flags, packaging, CI

Not production-ready before v1.0.