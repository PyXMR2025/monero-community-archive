---
title: Define default port for wallet RPC
source_url: https://github.com/monero-project/monero/issues/3509
author: arnuschky
assignees: []
labels: []
created_at: '2018-03-28T09:28:22+00:00'
updated_at: '2018-03-28T16:36:58+00:00'
type: issue
status: closed
closed_at: '2018-03-28T16:36:41+00:00'
---

# Original Description
Previous (unofficial?) default port was 18082, which has now been assigned to the zmq rpc. The wallet's help doesn't specify a default port.

I think that default ports are useful for easing deployment / installation. Looking at what happened with the zmq rpc, maybe we should offset the wallet's ports from the daemon, eg starting at 18088 or 18090.

Opinions?

# Discussion History
## jtgrassie | 2018-03-28T15:28:38+00:00
```
src/cryptonote_config.h:  uint16_t const P2P_DEFAULT_PORT = 18080;
src/cryptonote_config.h:  uint16_t const RPC_DEFAULT_PORT = 18081;
src/cryptonote_config.h:  uint16_t const ZMQ_RPC_DEFAULT_PORT = 18082;
```

## arnuschky | 2018-03-28T15:31:34+00:00
Yes, these are the daemon default ports. I am talking about defining this for the wallet too.

## jtgrassie | 2018-03-28T15:34:03+00:00
You mean the monero-wallet-rpc? There is no default port assigned to that looking at the source. You specify with `--rpc-bind-port`

## arnuschky | 2018-03-28T15:39:19+00:00
Yes, I mean monero-wallet-rpc (see title). Yes there is no default port assigned to it. This issue is about defining a default port.

## jtgrassie | 2018-03-28T15:55:28+00:00
Sorry title was ambiguous as normal wallet uses RPC to connect to daemon. Anyway...

I'm not sure defining a default port for monero-wallet-rpc is needed (or advisable). Opens up an easy port scanning security issue.   

## stoffu | 2018-03-28T16:28:51+00:00
AIUI the default port for wallet RPC is left undefined on purpose, so that uneducated users can’t easily make mistakes and lose money.

## arnuschky | 2018-03-28T16:36:41+00:00
Ah ok, I didn't think of that reason. Good point. Closing.

## jtgrassie | 2018-03-28T16:36:58+00:00
Indeed. It's a required parameter.

# Action History
- Created by: arnuschky | 2018-03-28T09:28:22+00:00
- Closed at: 2018-03-28T16:36:41+00:00
