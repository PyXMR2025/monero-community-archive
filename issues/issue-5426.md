---
title: moneroseed URI scheme to avoid dependence on default seed nodes
source_url: https://github.com/monero-project/monero/issues/5426
author: moneromooo-monero
assignees: []
labels: []
created_at: '2019-04-11T22:41:00+00:00'
updated_at: '2019-07-03T17:33:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
A while back, I played around with adding a moneroseed URI scheme, which would allow telling the OS to call monerod when clicking on such a URI. The format was moneroseed://IP[:PORT], and it's piggybacking on the --seed-node monerod command line option.

That works well on Linux at least.

This issue is to gather opinions on what other information, if any, should be included in such a link. I expect it will have to handle Tor/I2P addresses (no idea if --seed-node currently does).

The intent of such a URI is to bypass the (centralized) default seed nodes. I imagine that if Alice introduces Bob to Monero, she could tell him to install Monero from his distro's package manager, and give him a particular moneroseed URI which would point to her own node. Bob would then start monerod and not have to depend on getting good peers from the default seed nodes. This is however vulnerable to Alice being malicious, and her node only sending IPs of Sybils. This could be mitigated by using Alice's node in addition to the default seed nodes.

So, any more info that an address ?

# Discussion History
## sanderfoobar | 2019-04-12T03:55:02+00:00
Perhaps the possibility to define multiple addresses delimited by `&`; `://IP[:PORT]&IP[:PORT]`. Can imagine a scenario where Alice wants Bob to connect to a collection of nodes.

Or `://[I2P|TOR|CLEAR]?address=IP[:PORT]&address=IP[:PORT]&...`

AFAIK there is no official standard regarding query strings, but the latter seems more in line with what you see on the web. 

# Action History
- Created by: moneromooo-monero | 2019-04-11T22:41:00+00:00
