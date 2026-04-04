---
title: '[simplewallet] SOCKS5 proxy support'
source_url: https://github.com/monero-project/monero/issues/4310
author: kykeon
assignees: []
labels:
- duplicate
created_at: '2018-08-29T08:31:24+00:00'
updated_at: '2018-09-03T08:39:49+00:00'
type: issue
status: closed
closed_at: '2018-08-29T08:56:57+00:00'
---

# Original Description
Adding socks5 proxy support would make it easy for monerujo on android to connect to Orbot without using Orbot VPN mode (which has several limitations), and *nix users to proxy through tor easily by simply having Tor Browser open.

For many reasons, some people might find it preferrable to connect to a hidden .onion node, rather than going the kovri way.

I think that giving this option to the user would be a good thing.

# Discussion History
## moneromooo-monero | 2018-08-29T08:52:19+00:00
See #60.

+duplicate

## moneromooo-monero | 2018-08-29T08:53:08+00:00
And btw you don't need anything special to connect via tor, it works out of the box (see README.md for details).

## kykeon | 2018-09-03T08:39:49+00:00
torsocks is a hack though. It is not uncommon to see it fail with some unsupported call either, and in other cases like presently with android, it is actually not working at all ([link](https://github.com/termux/termux-packages/issues/2711).

Furthermore, for integrations such as with [monerujo (see discussion)](https://github.com/m2049r/xmrwallet/issues/100#issuecomment-416865943), the approach suggested in README is problematic.

Not just because torsocks happens to be broken on android right now, but more fundamentally because what is the deal then? Everyone who wants to integrate bundles their own torsocks + any dependencies in their app?

I understand if there is not enough interest to implement proper socks proxy support, but at the same time let's not pretend that using torsocks isn't a hack with its limitations.

# Action History
- Created by: kykeon | 2018-08-29T08:31:24+00:00
- Closed at: 2018-08-29T08:56:57+00:00
