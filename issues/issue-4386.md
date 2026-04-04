---
title: '[Question] How to detect if there is a hard-fork or a new version'
source_url: https://github.com/monero-project/monero/issues/4386
author: gituser
assignees: []
labels: []
created_at: '2018-09-16T09:53:52+00:00'
updated_at: '2018-09-16T11:40:46+00:00'
type: issue
status: closed
closed_at: '2018-09-16T11:40:46+00:00'
---

# Original Description
Hi.

Can you clarify how to properly detect if there is a new version and hard fork is coming ?

From documentation it's not absolutely clear.

https://getmonero.org/resources/developer-guides/daemon-rpc.html#hard_fork_info

What I did is to check monerod every hour with this `hard_fork_info` RPC call and check if `state!=2`, but for some reason today the node turned this parameter `state=1` (that means hard fork is coming), so my node was shut down automatically. 

After checking github it seems there is no new release at all and hard fork is only coming in october or so (according to reddit)?

Here is what my monerod is showing right now:
```sh
curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"hard_fork_info"}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "earliest_height": 1546000,
    "enabled": true,
    "state": 1,
    "status": "OK",
    "threshold": 0,
    "untrusted": false,
    "version": 7,
    "votes": 10080,
    "voting": 7,
    "window": 10080
  }
}
```
Can you tell me how to check properly if there is hardfork event is started what to look precisely in this `hard_fork_info` output to make sure I'm not on pre-forked chain and need to update the daemon? 
Thanks.

# Discussion History
## moneromooo-monero | 2018-09-16T10:09:34+00:00
This method is "has there been a lot of time since last fork".
If you want to know whether there is a new release to download, use the "update" RPC.

As for the node shutting down, any error messages or core file ?


## gituser | 2018-09-16T10:16:37+00:00
No, I'm shutting down the node myself (just to be safe in the case of hard fork in case I've missed the update).

From documentation:
```
state - unsigned int; Current hard fork state: 0 (There is likely a hard fork), 1 (An update is needed to fork properly), or 2 (Everything looks good).
```
Also monerod shows that there is an update needed:

```./monerod status
Height: 1662511/1662511 (100.0%) on mainnet, not mining, net hash 576.80 MH/s, v7, update needed, 200(out)+0(in) connections, uptime 53d 18h 52m 48s
```

That's why I've been checking for `state==2` and right now `state` turned to 1 for some reason so my node got shut down by me. So what's the proper way to check if there is a hard fork ?

## gituser | 2018-09-16T10:23:35+00:00
> If you want to know whether there is a new release to download, use the "update" RPC.

So what you're saying I should use instead:

```
curl -X POST http://127.0.0.1:18081/update -d '{"command":"check"}' -H 'Content-Type: application/json'
{
  "auto_uri": "",
  "hash": "",
  "path": "",
  "status": "OK",
  "update": false,
  "user_uri": "",
  "version": ""
}
```
and check if `update == true` right ?

## moneromooo-monero | 2018-09-16T10:30:25+00:00
If you want to know whether there is a new binary, yes.

It is not possible to know whether there is a hard fork, though in practice you can do a few things.

If you receive a bad block, it might be it forked, or it might be an attack. If it's a "clean" fork, then the block major version will be bumped. But then it might be someone making such a block as a one off to troll people. It is decentralized, a clean fork is just a consensus of people running the latest version and generating those blocks. I suppose monerod could keep track of those blocks and estimate the hash power creating those. But then, this is not possible if the PoW algorithm changed. And if it did, then maybe someone like Bitmain could switch back to original CN (or even SHA256) and push lots of hash rate. This would not be what you want though.


## gituser | 2018-09-16T10:47:35+00:00
It's just confusing. I mean if you read the documentation regarding `hard_fork_info`: https://getmonero.org/resources/developer-guides/daemon-rpc.html#hard_fork_info there is a state which states:

```
state - unsigned int; Current hard fork state: 0 (There is likely a hard fork), 
1 (An update is needed to fork properly), or 2 (Everything looks good).
```

What it is for then ?

## moneromooo-monero | 2018-09-16T10:54:35+00:00
This method is "has there been a lot of time since last fork".

## gituser | 2018-09-16T11:40:46+00:00
OK, thanks for the clarification!

# Action History
- Created by: gituser | 2018-09-16T09:53:52+00:00
- Closed at: 2018-09-16T11:40:46+00:00
