---
title: Rewrite pool mining guide
source_url: https://github.com/monero-project/monero-site/issues/1005
author: 00-matt
assignees:
- 00-matt
labels:
- ⛑️ contributor needed
- '📚 docs: user guides'
created_at: '2020-05-24T21:35:50+00:00'
updated_at: '2020-06-12T13:48:40+00:00'
type: issue
status: closed
closed_at: '2020-06-12T13:48:40+00:00'
---

# Original Description
The [pooled mining guide](https://web.getmonero.org/resources/user-guides/mine-to-pool.html) needs to be updated after the PoW changed to RandomX.

xmr-stak-cpu does not support RandomX, so instructions for configuring another miner (like XMRig or xmr-stak-rx) should be written instead.

Also the number of hugepages reserved should be increased too.

# Discussion History
## 00-matt | 2020-05-24T21:37:15+00:00
Also #999 - moneropools.com is dead.

## Sunray-Nucleon | 2020-05-25T19:06:44+00:00
Can i suggest to also have a hint about mining to .onion address? It should include the steps install tor relay (https://community.torproject.org/relay/setup/guard/) set "Limiting bandwidth usage" (https://support.torproject.org/operators/bandwidth-shaping/) to avoid congestion cause of traffic (or link to tor-post-install good practices https://community.torproject.org/relay/setup/post-install/)  and than set in /etc/tor/torrc the SocksPort 9050 - than also start Tor (systemctl restart tor) - and than set config of xMrig the same "socks5": 9050 and wallet address - than start xmRig mining - https://xmrig.com/docs/miner/tor

## 00-matt | 2020-05-25T19:10:10+00:00
Yes I think that telling people that they have the option to mine to a
hidden service pool (or to a clearnet pool via an exit mode) with Tor is
a good thing. But I don't think that we should be showing people how to
set up relay nodes in a mining article.


## Sunray-Nucleon | 2020-05-26T08:36:09+00:00
Can you maybe write it so, that it is incentivizing the reader to use i2p or Tor? I would even call it 'preferred' or 'to prefer' to mine via hidden service or i2p in the rewritten mining guide. Maybe you can write it somehow like:

"Because it is hiding the origin (the miners IP) a miner should utilize i2p or set up a tor relay and mine to a .onion address via socks5. For some people and in some areas its not possible to use Tor or i2p; so it is also possible to mine without, but than you reveal the IP of the miner to the pool operator. It is only a few more steps to set up a Tor relay."

## 00-matt | 2020-05-26T08:42:36+00:00

Yes I think this is a good idea.

Miners should be made aware that mining reveals that they use Monero,
that the pool operator can link their IP address and wallet address, and
that if they do not use TLS when mining their wallet address is visible
for all to see.



## Sunray-Nucleon | 2020-05-26T08:56:31+00:00
i would **avoid** calling it dangerous (or so) but **propagate good behavior** in the first place

also we should call it preferred to use 8... subaddress

"When mining to a pool mine to a subaddress of your wallet - so choose a pool that supports mining to subaddresses. Usually pools can do this, however its possible that a pool still did not enable the support of subaddresses; so its also possible to mine to integrated 4... addresses but this would reveal your main wallet address to the pool which a miner would usually want to avoid. Also, if you may change the pool one day, you can easily change the subaddress to avoid correlation between IPs and Pools and Subaddresses."

## erciccione | 2020-05-26T09:27:24+00:00
Please keep in mind this should be a simple guide aimed to the average user. I don't think would be wise to overcomplicate it by suggesting people to use tor/i2p to mine. I think would be great to mention the possibility, but keep in mind that this guide is not aimed to expert miners.

We could create an advanced guide for mining if we want to, with references to Tor/I2P and more, but the basic "mining to a pool" guide should be as minimal and simple as possible.

Monero it's already perceived as difficult to use, let's not scare miners away with documentation they cannot fully understand :)

## 00-matt | 2020-05-26T09:29:26+00:00
What about just a footnote that links to Tor's documentation explaining
that you might want to consider using it?


## erciccione | 2020-05-26T09:32:49+00:00
Sure, we could mention that it's possible to mine through Tor for increased anonimity and then link to the foot notes for more details and links.

## Sunray-Nucleon | 2020-05-27T20:24:34+00:00
Agree, we don't want to overwhelm (or even scare) new arriving users. A foot note or link to 'mining good practices' for use of Tor (as well subaddress for mining) seems reasonable.

# Action History
- Created by: 00-matt | 2020-05-24T21:35:50+00:00
- Closed at: 2020-06-12T13:48:40+00:00
