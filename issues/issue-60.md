---
title: Implement support for connecting through proxy
source_url: https://github.com/monero-project/monero/issues/60
author: Jojatekok
assignees: []
labels:
- proposal
created_at: '2014-07-14T08:12:01+00:00'
updated_at: '2022-03-16T15:27:12+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:27:12+00:00'
---

# Original Description
This is a requirement for both daemon and the wallet.

![Proxy support](https://cloud.githubusercontent.com/assets/1928320/3568328/7dbeedca-0b2e-11e4-8f0a-6fed1353d1f8.png)


# Discussion History
## fluffypony | 2014-08-02T09:28:09+00:00
Because this can be done through proxify, I'm not sure if we want to spend time baking this in right now. I think @rfree2monero can comment on this - if it's easy to bake this into the p2p protocol when we rewrite the network layer, then sure.


## dEBRUYNE-1 | 2018-01-08T12:34:28+00:00
+proposal

## moneromooo-monero | 2019-09-06T13:34:33+00:00
vtnerd added support for tor and i2p proxies, and I think it also works with "normal" SOCKS proxies.

## vtnerd | 2019-09-06T17:07:57+00:00
Yup, they both provide a normal socks proxy server that has special logical for ".onion" and ".i2p" domains. Right now only the wallet provides a proxy in the normal sense though, the daemon uses proxies only for i2p / tor connections. In other words, the wallet will proxy all HTTP connections to the daemon via the proxy, whereas the daemon proxies only p2p connections that are destined for i2p or tor.

## xanoni | 2021-08-16T04:18:52+00:00
Can be closed, see here https://github.com/monero-project/monero/pull/7616

# Action History
- Created by: Jojatekok | 2014-07-14T08:12:01+00:00
- Closed at: 2022-03-16T15:27:12+00:00
