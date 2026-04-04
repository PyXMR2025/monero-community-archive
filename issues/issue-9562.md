---
title: 'Feature request: Tor controlport for a good management of Tor'
source_url: https://github.com/monero-project/monero/issues/9562
author: XMRZombie
assignees: []
labels:
- discussion
- request
created_at: '2024-11-10T17:46:47+00:00'
updated_at: '2024-11-11T09:25:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It's always difficult to get people running Tor based nodes because they haves multiple args to add in their configuration.

By creating an arg like _--TorControlPort_ in monerod (or even on monero-cli), the software could control Tor to use a Tor proxy or deploying a hidden-service.

# Discussion History
## vtnerd | 2024-11-10T23:05:24+00:00
I have this on my to todo list, but I'm not sure its worth the effort. You typically have to manually setup the control port with password protection, and then configure both on the `monerod` side too. Its arguably less friction than setting up the hidden service manually, but not by much.

# Action History
- Created by: XMRZombie | 2024-11-10T17:46:47+00:00
