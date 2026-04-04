---
title: 'monerod: Couldn''t connect to daemon'
source_url: https://github.com/monero-project/monero/issues/3176
author: Phoettinave
assignees: []
labels:
- invalid
created_at: '2018-01-23T22:27:06+00:00'
updated_at: '2018-02-24T18:51:55+00:00'
type: issue
status: closed
closed_at: '2018-01-26T11:56:29+00:00'
---

# Original Description
When trying to run `monerod status` when a monero daemon is already running (started with `--detach`), I keep getting the following error message (reproducible across all my servers with v0.11.1.0 and latest master (5f09d6c8333b0b0d07252dc157b9e794f6278662)):

```sh
$ monerod status
Error: Couldn't connect to daemon: 127.0.0.1:18081
Height: 1493720/1493720 (100.0%) (...)
```

It gets more interesting with the `print_cn` command:

```sh
$ monerod print_cn
2018-01-23 22:17:25.908	    7fb166619bc0	ERROR	net.http	contrib/epee/include/storages/http_abstract_invoke.h:118	RPC call of "" returned error: -32601, message: Method not found
Error: Couldn't connect to daemon: 127.0.0.1:18081
```

# Discussion History
## Phoettinave | 2018-01-23T22:37:22+00:00
This is how I start monerod:

```
ExecStart=/root/monero/build/release/bin/monerod --rpc-bind-ip 127.0.0.1 --restricted-rpc --p2p-bind-ip 0.0.0.0 --fluffy-blocks --detach
```

## moneromooo-monero | 2018-01-26T11:54:24+00:00
Remove --restricted-rpc if you want to access restricted RPC.

+invalid


## Phoettinave | 2018-01-26T15:11:36+00:00
@moneromooo-monero thanks that helped. Its still a bug that when executing the 'status' command i get the output of it and an error message. Please reopen until that is resolved

## Phoettinave | 2018-02-24T18:51:55+00:00
@moneromooo-monero @fluffypony @dEBRUYNE-1 please open again, its not fixed! "Error: Couldn't connect to daemon" shouldnt appear.

# Action History
- Created by: Phoettinave | 2018-01-23T22:27:06+00:00
- Closed at: 2018-01-26T11:56:29+00:00
