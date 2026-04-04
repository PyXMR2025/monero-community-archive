---
title: Option to use Socks proxy/Tor/I2P for everything
source_url: https://github.com/monero-project/monero-gui/issues/3239
author: throoweway387
assignees: []
labels: []
created_at: '2020-11-15T18:26:02+00:00'
updated_at: '2025-03-18T13:18:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In Monero-gui there's Socks proxy option for only remote node connection, updates, fetching price sources.

In Bitcoin-qt you can configure it to use Socks proxy, for example Tor, for everything.

It would be great to have similar option in Monero-gui too!

# Discussion History
## xiphon | 2020-11-15T20:26:23+00:00
> you can configure it to use Socks proxy, for example Tor, for everything.

Monero daemon doesn't support this.

## Antiwh0re | 2025-03-18T13:18:03+00:00
This request delivers a related question - does the app or daemon produce any other traffic besides the one with remote node when remote node is selected in settings? Cause if it does, than this proxy option (for remote node connection only) won't save us from leaks.

# Action History
- Created by: throoweway387 | 2020-11-15T18:26:02+00:00
