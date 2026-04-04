---
title: RPC get_info gives target_height:0
source_url: https://github.com/monero-project/monero/issues/1404
author: Jaqueeee
assignees: []
labels:
- invalid
created_at: '2016-12-05T10:58:27+00:00'
updated_at: '2017-08-12T20:06:12+00:00'
type: issue
status: closed
closed_at: '2017-08-12T20:06:12+00:00'
---

# Original Description
Running current master `60633cf`. 
Daemon is fully synced but target_height is 0. 

This will cause an infinite loop and wallet freeze because of this:
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L1587-L1599


```
curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
$ curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "alt_blocks_count": 0,
    "cumulative_difficulty": 1322619695917907,
    "difficulty": 4102513309,
    "grey_peerlist_size": 4991,
    "height": 1194612,
    "incoming_connections_count": 0,
    "outgoing_connections_count": 8,
    "status": "OK",
    "target": 120,
    "target_height": 0,
    "testnet": false,
    "top_block_hash": "0930266e172f6447ae5c514e10547ad0543f9bcfaec2c6935c916b82fba1cd28",
    "tx_count": 807463,
    "tx_pool_size": 2,
    "white_peerlist_size": 1000
  }
  
```
  
  daemon status:
`  Height: 1194612/1194612 (100.0%) on mainnet, not mining, net hash 34.19 MH/s, v3, up to date, 8+0 connections`

# Discussion History
## tewinget | 2016-12-05T11:31:30+00:00
I noticed this as well, but thought it only affected not-synced daemons.
Thanks for the heads up.  I've already fixed this on my zmq branch, but I
could pr that fix upstream later today.
On Dec 5, 2016 5:58 AM, "Jaqueeee" <notifications@github.com> wrote:

> Running current master 60633cf.
> Daemon is fully synced but target_height is 0.
>
> This will cause an infinite loop and wallet freeze because of this:
> https://github.com/monero-project/monero/blob/master/
> src/wallet/wallet2.cpp#L1587-L1599
>
> curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
> $ curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
> {
>   "id": "0",
>   "jsonrpc": "2.0",
>   "result": {
>     "alt_blocks_count": 0,
>     "cumulative_difficulty": 1322619695917907,
>     "difficulty": 4102513309,
>     "grey_peerlist_size": 4991,
>     "height": 1194612,
>     "incoming_connections_count": 0,
>     "outgoing_connections_count": 8,
>     "status": "OK",
>     "target": 120,
>     "target_height": 0,
>     "testnet": false,
>     "top_block_hash": "0930266e172f6447ae5c514e10547ad0543f9bcfaec2c6935c916b82fba1cd28",
>     "tx_count": 807463,
>     "tx_pool_size": 2,
>     "white_peerlist_size": 1000
>   }
>
>
> daemon status:
> Height: 1194612/1194612 (100.0%) on mainnet, not mining, net hash 34.19
> MH/s, v3, up to date, 8+0 connections
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1404>, or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AE3k5qjbTJZod5SRK2csOnprn_yYJTVwks5rE-5UgaJpZM4LEGBt>
> .
>


## Jaqueeee | 2016-12-05T11:42:13+00:00
@tewinget That would be appreciated. This bug alone mostly gives some weird sync information in GUI (synchronizing block 115123 / 0). But together with https://github.com/monero-project/monero/commit/fd181b03bb58a8b0628d2af8637cf6bb968fc437 we get stuck in an infinite loop. ping @revler1082

After restarting daemon a couple of times the target height is now correct. 

## tewinget | 2016-12-05T11:47:00+00:00
If you want to go ahead and do it (I'm about to sleep) just change it so
before returning that rpc call says "if target height < height, target
height = height".  Should be in src/rpc/core_rpc_server.cpp search for "get
_info".
On Dec 5, 2016 6:42 AM, "Jaqueeee" <notifications@github.com> wrote:

@tewinget <https://github.com/tewinget> That would be appreciated. This bug
alone mostly gives some weird sync information in GUI (synchronizing block
115123 / 0). But together with fd181b0
<https://github.com/monero-project/monero/commit/fd181b03bb58a8b0628d2af8637cf6bb968fc437>
we get stuck in an infinite loop. ping @revler1082
<https://github.com/revler1082>

After restarting daemon a couple of times the target height is now correct.

—
You are receiving this because you were mentioned.

Reply to this email directly, view it on GitHub
<https://github.com/monero-project/monero/issues/1404#issuecomment-264833792>,
or mute the thread
<https://github.com/notifications/unsubscribe-auth/AE3k5nPaclyC_9VxgmCyX9evG2CUb55Wks5rE_iWgaJpZM4LEGBt>
.


## moneromooo-monero | 2016-12-05T11:50:24+00:00
The target height is only used for block syncing, so if your node's already synced when you start it, it will not be set to anything IIRC.

## moneromooo-monero | 2017-08-12T20:05:12+00:00
Target height is a sync indicator. Use target height and height if you want to know what's the highest chain you know about.

+invalid
+resolved

# Action History
- Created by: Jaqueeee | 2016-12-05T10:58:27+00:00
- Closed at: 2017-08-12T20:06:12+00:00
