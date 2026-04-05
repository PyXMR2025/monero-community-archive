---
title: Project roadmap for 2025
source_url: https://github.com/Cuprate/cuprate/issues/376
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2025-01-28T17:53:01+00:00'
updated_at: '2025-02-09T21:09:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue documents Cuprate's roadmap for 2025.

> [!NOTE]  
> 1. This roadmap is conservative
> 1. This roadmap can always be changed in the future
> 1. This roadmap is made under the assumption that current developer resources will stay the same

## Beneficiaries

<details>

<summary>TODO: this section is not yet finished.</summary>

It is worth identifying the stakeholders/beneficiaries before laying out any value hierarchy for Cuprate as it is the aim of any project to bring value to those groups and set the roadmap accordingly. Being a public node project, Cuprate benefits a large portion of Monero, particularly:

1. Organizations (wallets, exchanges, services, businesses)
1. Operators (individual users)
1. Developers

`cuprated`'s RPC interface is planned to be practically no different than `monerod`, as such, current services utilizing daemon RPC should be able to swap `monerod` for `cuprated` with no trouble for a faster experience. This is a large incentive for any user of `monerod`, particularly any organization operating at scale.

Individual users benefit from the organization-level benefits as well as other 'smaller' practical benefits, mostly stemming from being a modern implementation of Monero, e.g. sync speeds, documentation, etc.

Regarding developers, the libraries that make up Cuprate's node implementation are all re-usable, open-source, and increasingly more importantly, in Rust. For all practical purposes, this is a non-trivial detail that is important for future development.

</details>

## Project roadmap

### Q1
These goals will be focused on throughout January-March 2025.

| Goal | Details |
|------|---------|
| Alpha `cuprated` release cycle | Cuprate has begun working on finalizing an alpha release cycle here: [1](https://github.com/Cuprate/cuprate/issues/371) [2](https://github.com/Cuprate/cuprate/issues/374) [3](https://github.com/monero-project/meta/issues/1140). There are a few other details that must be decided, where after, the first release is expected in 2025 Q1. Alpha releases are set to occur every 4 weeks from there after. |
| Fast-sync | https://github.com/Cuprate/cuprate/tree/fast-sync |
| Transaction pool relay rules | https://github.com/Cuprate/cuprate/issues/319
| Logging | https://github.com/Cuprate/cuprate/issues/163
| STDIN commands | TODO

### Q2/Q3/Q4
These goals will be focused on throughout April-December 2025.

| Goal | Details |
|------|---------|
| FCMP++ | FCMP++ in `monerod` is still be worked on, thus work on this has not yet started, although it must eventually be implemented in `cuprated` in order to continue to stay compatible with the network. |
| RPC | Much of the core functionality of `monerod` has already been implemented: transaction/block {sync, verification, propagation}. One of the remaining core functionality is a wallet-compatible RPC system. As mentioned earlier, there are large incentives for this to be done for organizations operating at scale. |
| Tor (arti) integration | One of the aspects of Monero's privacy that could be further worked on is the P2P network. As `arti` can be embedded within `cuprated`, the barrier of entry for Tor usage can be lowered significantly, as such, a more anonymous P2P network can be achieved. Due to these reasons, this has remained a high priority for Cuprate since the beginning of the project [1](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/370) [2](https://github.com/Cuprate/cuprate/blob/2c7cb27548c727550ce4684cb31d0eafcf852c8e/readme.md?plain=1#L41).

### Non-likely goals for 2025
There is a long bucket list for Cuprate, yet the project is limited in time and resources. Some items must take precedence over others. This is an incomplete list of items that Cuprate will likely not implement (in 2025) in order to focus on the core goals laid out above:

- Other interfaces (e.g. ZMQ, WebSockets)
- Non-node related efforts (e.g. wallet, GUI)
- Optimizations for certain hardware
- Novel architecture/implementations
- Stability guarantees for crates and binary interfaces
- Reproducible builds
- Expanded build targets
- ...

# Discussion History
# Action History
- Created by: hinto-janai | 2025-01-28T17:53:01+00:00
