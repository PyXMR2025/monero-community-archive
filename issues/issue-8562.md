---
title: SOCKS5 not supported
source_url: https://github.com/monero-project/monero/issues/8562
author: vdo
assignees: []
labels: []
created_at: '2022-09-12T11:17:17+00:00'
updated_at: '2022-09-28T21:02:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I was setting up a connection to a monero node through the NYM mixnet, using their socks5 client as described [here](https://nymtech.net/docs/stable/use-external-apps/), but I got an error because [only socks4 is supported](https://github.com/monero-project/monero/blob/master/src/net/socks.h#L59). 

This issue is inherited in the GUI wallet, so the parameter/option enabling it is misleading:
![Screenshot_2022-09-12_12-18-40](https://user-images.githubusercontent.com/170204/189640314-7aa693f2-9182-447a-8cd7-95e5edb00b94.png)




# Discussion History
## vtnerd | 2022-09-17T22:04:05+00:00
We only support Socks4a actually.

We can add Socks5, but nym should consider adding Socks4a instead if they intend to add a hidden service capability in the future. Only Socks4a has hostname support. Tor/I2P knows how to do a hostname lookup for `.onion` and `.i2p` addresses, etc. All other Socks variants support IP/Port only, and require the client to DNS lookup. This isn't realistic with Tor/I2P/Nym hidden services because each network has a custom hostname<->ip mapping facility.

## vtnerd | 2022-09-17T22:07:30+00:00
I should add - one of the I2P developers tried to get me to implement a custom protocol for hidden services. But one of the more senior developers on the project noted that Socks4a already worked as expected when a `.i2p` address was provided. There might be some feature degradation with this setup, but its far easier on our side than a custom protocol per network type. If absolutely necessary, the code was designed to handle such a requirement though.

## vdo | 2022-09-20T11:01:49+00:00
I'm not sure NYM would add hidden service/i2p support, since it's a replacement for those and it would be an overkill.

NYM is only an example I faced myself, but SOCKS5 is a pretty standard protocol when it comes to proxy support, so I think it would be desirable to add it to Monero eventually, even if it's without auth support.


## vtnerd | 2022-09-20T20:45:53+00:00
> I'm not sure NYM would add hidden service/i2p support, since it's a replacement for those and it would be an overkill.

Yes, if it is designed to replace Tor/I2P, is it adding an equivalent functionality to the network? If so, Socks4a will be more useful than Socks5 because otherwise outside processes will be forced to implement a custom protocol to make connections to the equivalent of hidden services.

> NYM is only an example I faced myself, but SOCKS5 is a pretty standard protocol when it comes to proxy support, so I think it would be desirable to add it to Monero eventually, even if it's without auth support.

Socks5 isn't really standard, because it lacks hostname support. It forces downstream projects to implement DNS lookups over Socks5 - which isn't possible in Tor hidden services (and the I2P/Nym equivalent).

## vdo | 2022-09-20T21:22:00+00:00
As I understand it, NYM is not trying to mimic the hidden service/i2p address functionality the same way, but rather as an "exit node" to clearnet DNS addresses, which are whitelisted. So for example, this would be the flow:

monero wallet -> nym-client-socks5 -> network-requester -> nym-client --- (mixnet) ---> mainnet.xmr.sh (clearnet)

The wallet would simply use `localhost:1080` and `nym-client-socks5` would point to a "provider id", which in turn connects to the whitelisted node domain, like:
`monero-wallet-cli --log-level 2  --proxy 127.0.0.1:1080  --daemon-address mainnet.xmr.sh:443  --daemon-ssl-allow-any-cert <wallet>`

So not sure if falling back to socks4a would actually solve anything from their side.

## vtnerd | 2022-09-21T02:26:12+00:00
Yes, I understand their situation exactly. I am trying to point out that Socks5 lacks features that are useful, and perhaps Nym should implement Socks4a instead.

In your example, connecting to `mainnnet.xmr.sh` is actually more involved because the lack of hostname support means `monerod` has to create custom DNS packets to send over the socks proxy. In comparison, with Socks4a we ask for a connection to a hostname, and the remote exit node does the DNS lookup and makes the TCP connection to that IP. This is how we support Tor/I2P exit nodes with hostname bootstrap nodes, etc. The lack of DNSSEC isn't that helpful in many cases because the exit node can MitM without further encryption/authentication anyway.

And on top of everything else, if Nym implements something comparable to Tor hidden services, Socks5 is completely useless. Nym has to either implement Socks4a so we can do a hostname request (`something.nym`, etc), OR we get to implement a custom protocol just for Nym and their new services feature.

So I'm pushing back because there is a decent chance we implement Socks5 for nothing if Nym chooses the first option (implements a hidden-service like feature and Socks4a to proxy requests to those services).

## vdo | 2022-09-21T20:34:03+00:00
Regardless of NYM's roadmap about internal/hidden services, the initial intent of the issue was not only to ask for support the current `nym-socks5-client` but also many other socks5 proxies that are out there. Socks4a just works for the tor/i2p use cases, but I see socks5 as a valuable addition as well.

cc/ @jstuczyn

## vtnerd | 2022-09-25T20:50:55+00:00
Someone pointed out that I was wrong about my recollection of Socks5 - it supports hostnames. A quick search of Nym code suggests they support the hostname mode too. Giant egg on face.

I will add support for this (as the original author of Socks4), unless someone else wants to jump in. I'm not sure what to do with the authentication modes yet.

## vtnerd | 2022-09-25T21:03:11+00:00
Also note - this cannot (without more complex changes) be used in "mixed mode" (`--tx-proxy`) - where blocks are downloaded over clearnet and transactions are sent over Nym. This currently requires a special hostname postfix (i.e. `.nym`) to disambiguate how to proxy (or not) the connection. Basically `--tx-proxy` is currently assuming some hidden service like feature of the network, and is using `.onion`, etc., to determine whether that particular host is available over clearnet or Tor.

This isn't a hard requirement, but there isn't a way to specify that `--add-node`, etc., should be used over Nym (instead of clearnet) without some additional changes to how proxies are handled internally. Or else we hijack the `.nym` TLD, something like `192.168.1.1.nym`, etc.

## vtnerd | 2022-09-25T21:10:15+00:00
Also, I'm not sure if `192.168.1.1.nym` is a good idea because there might be some privacy issues where hosts are shared over clearnet and then connected over `--tx-proxy`. `monerod` currently takes the conservative approach where IPv4/6, Tor, and I2P are considered separate "zones", and sharing peers from another "zone" is not allowed (because it allows "poisoning" someone with unique peers).

## vdo | 2022-09-27T10:23:39+00:00
> Also, I'm not sure if `192.168.1.1.nym` is a good idea 

Agree, I think it should be a more general approach, rather then naming it with a specific suffix for NYM. It could be used for "standard" SOCKS5 proxies. Maybe something like `.local` since the localhost is used as entrypoint ?



## vtnerd | 2022-09-28T21:02:45+00:00
The proxy system used by Tor and I2P is "standard" Socks4. The `.onion` and `.i2p` suffixes are used with `-add-node`, `--add-priority-node`, and `--add-exclusive-node` to determine how the connection to the specified address should be made. This is needed because `monerod` frequently operates in a "mixed-mode" where 1+ `--tx-proxy`s can be specified with or without `--proxy`.

These network suffixes always get routed to the corresponding `--tx-proxy`, and `--proxy` never carries these connections. There is also code to prevent addresses from mixing across network types to prevent potential fingerprinting from one network type to another. I'm not sure how to handle IPv4/6 directly in `--tx-proxy` and vice-versa because toggling `--proxy` on/off is potentially already problematic for fingerprinting purposes.

The shortened version is, Socks5 (unless other changes are made) will provide Nym access with `--proxy` but not `--tx-proxy`. The latter is interesting because only outgoing transactions are pushed over those connections.

# Action History
- Created by: vdo | 2022-09-12T11:17:17+00:00
