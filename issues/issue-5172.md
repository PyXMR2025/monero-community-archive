---
title: Add wildcard support to CORS Access-Control-Allow-Origin header in Daemon RPC
source_url: https://github.com/monero-project/monero/issues/5172
author: woodser
assignees: []
labels: []
created_at: '2019-02-20T17:05:28+00:00'
updated_at: '2021-09-09T19:20:18+00:00'
type: issue
status: closed
closed_at: '2021-09-09T19:20:18+00:00'
---

# Original Description
This issue requests wildcard support in the CORS Access-Control-Allow-Origin header in Daemon RPC.  Doing so would allow web apps to query a Monero daemon to enable fully client-side web wallets.  Since the daemon is a neutral provider of information about the Monero blockchain, I see no reason for it to discriminate against clients by not allowing web clients.

# Discussion History
## woodser | 2019-02-20T18:33:26+00:00
Related: #2408, #1677

## ph4r05 | 2019-03-15T15:48:17+00:00
Good idea if  there is a command line switch and it is off by default (As mentioned on IRC).
 Otherwise public nodes could be easily DDoSed by malicious websites (e.g., XSS on popular website)

## vtnerd | 2019-03-15T23:07:23+00:00
`--rpc-access-control-origin` is already an option, but there is no wildcard support. Is there some use cases where specifying the domain is too difficult, or.. ?

## woodser | 2019-03-15T23:23:02+00:00
@vtnerd The use case is for a web wallet to choose from multiple publicly available daemons, no different from how Cake Wallet, etc work.  I supppse the additional risk is websites may DoS a daemon, but all daemons do is serve publicly available information, and I don’t see why we should restrict daemon’s from doing that if they choose to.

## hundehausen | 2020-09-14T12:36:19+00:00
I support this. We need wildcard support for web based wallets like monero-javascript wasm wallet.

## AlexAnarcho | 2020-09-16T05:33:23+00:00
Would love to see this for more awesome browser based non-custodial Monero services!

# Action History
- Created by: woodser | 2019-02-20T17:05:28+00:00
- Closed at: 2021-09-09T19:20:18+00:00
