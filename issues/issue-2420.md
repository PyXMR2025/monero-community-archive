---
title: cannot use custom monero remote node / monero-gui does not respect Remote Node
  Setting / remoteNodeAddress= in config file ~/.config/monero-project/monero-core.conf
source_url: https://github.com/monero-project/monero-gui/issues/2420
author: adrelanos
assignees: []
labels:
- invalid
created_at: '2019-10-28T13:26:38+00:00'
updated_at: '2019-10-28T14:00:51+00:00'
type: issue
status: closed
closed_at: '2019-10-28T14:00:51+00:00'
---

# Original Description
This user reported issues with remote nodes using SSL vs non-SSL:
https://github.com/monero-project/monero-gui/issues/2206#issuecomment-512769208

I might have suffered from a similar issue. Connecting over Tor.
`monero-gui-v0.14.1.0` on Qubes-Whonix 15 (Debian `buster` based).

Therefore I wanted to use a monero remote node which is reachable over `.onion` that I used successfully with monero CLI beforehand.

I clicked on "network status" and entered the `.onion` and port that I know that is functional. Then clicked on connect. I would have expected that this `.onion` will be tried to connect to. And if it fails, my problem. What however happened was unexpected: monero GUI tried another (from my perspective) random IP address (which is probably from a built-in list of monero remote nodes).

Then I shutdown monero GUI. Went to the configuration file `~/.config/monero-project/monero-core.conf` and set `remoteNodeAddress=` manually. (`remoteNodeAddress=theonionaddress.onion`) This setting wasn't honored either. Monero GUI proceeded with automatic remote node selection.


# Discussion History
## selsta | 2019-10-28T13:28:30+00:00
Are you using simple mode?

## adrelanos | 2019-10-28T13:34:44+00:00
Yes.

## selsta | 2019-10-28T13:59:07+00:00
Simple mode will automatically connect to a remote node. Setting a custom one is not supported. Use advanced mode for this.

There are some bugs that allow you to access the node setting screen in v0.14.1.0 but this is fixed in v0.15

+invalid

# Action History
- Created by: adrelanos | 2019-10-28T13:26:38+00:00
- Closed at: 2019-10-28T14:00:51+00:00
