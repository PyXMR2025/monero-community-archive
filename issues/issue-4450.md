---
title: Where is RPC  "/get_random_outs"?
source_url: https://github.com/monero-project/monero/issues/4450
author: moneroexamples
assignees: []
labels: []
created_at: '2018-09-26T00:24:24+00:00'
updated_at: '2018-11-08T17:17:48+00:00'
type: issue
status: closed
closed_at: '2018-09-26T08:42:26+00:00'
---

# Original Description
There is still code in the wallet that depends on this call, e.g. `wallet2::light_wallet_get_outs` https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L6332

`/get_random_outs`  seems to be totally gone, but the code that uses it is still in the wallet. Was it deprecated? If so, maybe to code that depends on it also should be removed or modified? 

Similarly, `struct COMMAND_RPC_GET_RANDOM_OUTS` is still present, even though its only used `wallet2::light_wallet_get_outs` which is not going to work anyway at present.



# Discussion History
## moneromooo-monero | 2018-09-26T08:38:12+00:00
It's gone. vtnerd said he'd have the light wallet server updated soon.

## moneroexamples | 2018-09-26T08:42:26+00:00
Cool. Thanks for the info.

## dooglio | 2018-11-04T23:19:45+00:00
Where is there information on the light wallet server? When will it be implemented?

Using the current version of the monero server, those RPC calls are gone. That means that you can't even use MyMonero to send anything, because `RandomOuts()` won't work against a full node:

https://github.com/mymonero/mymonero-app-js/blob/90e6fe965ccfd7097cdbf6eb0ed4d17a3204862e/local_modules/HostedMoneroAPIClient/HostedMoneroAPIClient_Base.js#L392

...unless I'm missing something?

## moneroexamples | 2018-11-04T23:52:44+00:00
MyMonero is running custom backend. So it does not matter much that `get_random_outs` is gone from offical monero sources, as all the information needed for MyMonero is provided by their own backend. 

Opensourced MyMonero backend is being developed here: https://github.com/mymonero/hostedwallet-server-staging So you can have a look at its status there. Other link to  monitor is here: https://github.com/monero-project/monero/pull/4139

## gutenye | 2018-11-05T02:45:02+00:00
@moneroexamples What's the relationship between `mymonero/hostedwallet-server-staging` and `moneroexamples/openmonero`. I saw they both are open source implementation of MyMonero backend.

## dooglio | 2018-11-05T02:57:41+00:00
@moneroexamples  Sorry, I was under the impression that `HostedMoneroAPIClient` connected to a Monero full node, not a MyMonero server.

## moneroexamples | 2018-11-05T03:02:55+00:00
@gutenye 

`mymonero/hostedwallet-server-staging` is being developed by mymonero team. `openmonero` is  an independent effort. 

## gutenye | 2018-11-08T07:02:06+00:00
@vtnerd any updates on the light wallet server? 
Without `/get_random_outs` call, how can a light wallet create a transaction at the moment?

## vtnerd | 2018-11-08T17:16:48+00:00
> Without /get_random_outs call, how can a light wallet create a transaction at the moment?

It cannot create a transaction without this endpoint working.

> @vtnerd any updates on the light wallet server?

Locally I have updated the light wallet server to do random output selection with the latest algorithm ( even the window selection change in review)! Unfortunately, it cannot duplicate _exactly_ what wallet2 is doing until the REST-API is changed to send the "real" index (for fork selection + privacy-to-`monerod`). I still need to verify the gamma distribution selection - it appeared to be clustering in an unexpecting way at first glance.

Before posting I'm likely to make one last DB change - check [the main PR](https://github.com/monero-project/monero/pull/4139) which will receive a force push of the "squashed" changeset.

EDIT: After this last DB change I expect the DB to be "stable" - any future DB changes should come with migration code like `monerod`.

# Action History
- Created by: moneroexamples | 2018-09-26T00:24:24+00:00
- Closed at: 2018-09-26T08:42:26+00:00
