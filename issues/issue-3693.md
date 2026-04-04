---
title: How to run monero-wallet rpc?
source_url: https://github.com/monero-project/monero/issues/3693
author: zeshanvirk
assignees: []
labels:
- invalid
created_at: '2018-04-24T06:04:50+00:00'
updated_at: '2019-07-01T15:45:30+00:00'
type: issue
status: closed
closed_at: '2018-05-16T10:56:56+00:00'
---

# Original Description
I downloaded monero-cli for windows, i double clicked monerod, when its synchronized i double clicked moneo-wallet-cli, i created wallet, then i clicked monero-wallet-rpc, it gets closed within a second, i tried to hit wallet rpc methods using postman but could not get any response, but when i hit daemon rpc methods which are on 18081 as per official documentation, it gave me response... what i am doing wrong while accessing wallet-rpc methods?


# Discussion History
## moneromooo-monero | 2018-04-24T08:10:10+00:00
You need to at least give it the port to which to bind. Also add --wallet-file /path/to/wallet/cache, maybe auth options if necessary.
There are instructions in the README.md file, and the --help option lists all options.
Run from the terminal rather then clicking on things if you want to be able to read the error messages before windows takes them away.

## mattcode55 | 2018-04-24T08:12:18+00:00
> then i clicked monero-wallet-rpc, it gets closed within a second

That means it isn't running :)

Try running it with command prompt, you should get a help message showing all of the switches and parameters you can pass to start it.

You probably want something like `monero-wallet-rpc.exe --wallet-file my-wallet --prompt-for-password --rpc-bind-port 16969`. Remember to use a different port for the daemon RPC and wallet RPC.

## zeshanvirk | 2018-04-24T11:37:15+00:00
i tried the solution but my wallet stuck at a point Starting wallet RPC server... how can i resolve this issue? as i saw an issue related to this but didn't got any help from that issue.

## moneromooo-monero | 2018-04-24T13:47:57+00:00
Stuck how ? Doesn't answer to RPC ? That message is the one that happens after init is done, when the wallet starts listening to RPC, so if it's stuck there, it may be some network problem.

## zeshanvirk | 2018-04-24T16:46:58+00:00
Solved, It was giving unauthorized access which is solved by "--disable-rpc-login"

## moneromooo-monero | 2018-05-16T10:30:39+00:00
+invalid

# Action History
- Created by: zeshanvirk | 2018-04-24T06:04:50+00:00
- Closed at: 2018-05-16T10:56:56+00:00
