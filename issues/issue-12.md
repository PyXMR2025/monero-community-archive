---
title: Becoming stable
source_url: https://github.com/MrCyjaneK/monero_c/issues/12
author: MrCyjaneK
assignees: []
labels: []
created_at: '2024-07-23T08:32:41+00:00'
updated_at: '2026-03-12T11:31:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monero_c started as a rewrite to be used in only one wallet, but times have changed and now monero_c is also being used in xmruw, cake and stack, and with large amount of users and widespread adoption comes great responsibility, for this reason monero_c is becoming stable. What does that mean? Mostly turning branch protections on, all changes will come in separate PRs and adding other wallets into the CI to ensure compatibility across new revisions and to speed up testing of changes


# TODO

- [x] Rebase against v0.18.3.4 tag (once released) #14 
- [x] Add cake into the CI #15 
- [x] Cleanup patches (just a little bit)
- [ ] Create upstream version of monero_c (one without custom patches)
- [x] merge monero.dart into monero_c repo #16
- [x] throw errors when wrong wrapper is being used (embed git hash at build time)
- [x] Pin iOS dependencies
- [x] Cache sources on release builds (we sha256 them anyway)
- [ ] you tell me

# Discussion History
# Action History
- Created by: MrCyjaneK | 2024-07-23T08:32:41+00:00
