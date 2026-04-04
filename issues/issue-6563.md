---
title: rpc call too slow.
source_url: https://github.com/monero-project/monero/issues/6563
author: redred77
assignees: []
labels: []
created_at: '2020-05-19T13:36:42+00:00'
updated_at: '2022-04-10T18:50:06+00:00'
type: issue
status: closed
closed_at: '2022-04-10T18:50:05+00:00'
---

# Original Description
I call rpc call to 15151 port like below

```
curl -X POST http://127.0.0.1:15151/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
```
```
curl -X POST http://127.0.0.1:15151/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getlastblockheader"}' -H 'Content-Type: application/json'
```

It's so slow that consumes more than few seconds for each call. Sometimes it took 2 minutes to get the result.
When my program calls this jsonrpc several times, monero wallet start to break and gets out of sync.

It didn't happen like this before. It started to fall few days ago.
I updated to latest monerod but still not fixed.

# Discussion History
## moneromooo-monero | 2020-05-19T14:28:46+00:00
Do you have something else hammering the RPC in the meantime ? Or even the P2P port ?
Can you run "sudo perf top -a" or other profiler to see anything's pushing the machine, or if it's stuck waiting for I/O, that kind of thing ?

## vtnerd | 2020-05-19T16:11:21+00:00
Also the [poor mans profiling](https://poormansprofiler.org/) technique might be able to highlight what function is dominating the call.

## moneromooo-monero | 2020-05-19T16:45:09+00:00
FWIW I have pstack on a 4.x kernel.

## selsta | 2022-04-10T18:50:05+00:00
No reply from the issue creator, closing.

# Action History
- Created by: redred77 | 2020-05-19T13:36:42+00:00
- Closed at: 2022-04-10T18:50:05+00:00
