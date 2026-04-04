---
title: '"status" command does not show peer counts'
source_url: https://github.com/monero-project/monero/issues/5040
author: sethforprivacy
assignees: []
labels: []
created_at: '2019-01-03T21:14:26+00:00'
updated_at: '2019-01-29T14:30:02+00:00'
type: issue
status: closed
closed_at: '2019-01-04T15:00:19+00:00'
---

# Original Description
I recently have run into an issue where my full node will not show me peer counts when running "status":

`Height: 1741006/1741006 (100.0%) on mainnet, not mining, net hash 378.72 MH/s, v9, up to date, 0(out)+0(in) connections`

This started around the same time I spun up another node on the same network and exposed on a different p2p port, but I'm not 100% sure it's related.

Some addition logs:

[print_cn (run immediately after the above "status")](https://paste.fedoraproject.org/paste/mE8ey2TWZzlHlqnGgUznxA)

If there are any other logs I can supply or things I can do to test please let me know!

# Discussion History
## sethforprivacy | 2019-01-03T21:17:08+00:00
Some environment notes:

- I am running on CentOS 7
- I have compiled from scratch with GCC 8.2/CMake 3.12.2
- I am currently running v0.13.0.0-master-e344d93 (compiled today, on 01/03)

## moneromooo-monero | 2019-01-03T22:27:18+00:00
Anything interesting or suspicious in the logs (set level 1 first) ?

## sethforprivacy | 2019-01-03T22:29:30+00:00
Not immediately, but I'll grab some logs later and upload them in case something stands out to you.

## sethforprivacy | 2019-01-04T04:19:51+00:00
Attached below is a debug log at log_level 1, during which I did both "status" and "print_cn".

I also left in a few lines before the start of the increased log level that show a trace/error of some sort, wasn't sure if that was pertinent. Let me know what else I can provide!

[monerod_debug.log.gz](https://github.com/monero-project/monero/files/2726006/monerod_debug.log.gz)


## moneromooo-monero | 2019-01-04T13:34:49+00:00
Are you running with restricted RPC ?

## sethforprivacy | 2019-01-04T14:06:32+00:00
Yes, running with the following args:

`./monerod --rpc-bind-ip 0.0.0.0 --rpc-bind-port 18089 --confirm-external-bind --restricted-rpc --disable-dns-checkpoints --log-file monerod.log`

## moneromooo-monero | 2019-01-04T14:51:14+00:00
Then don't for now. There will be an override for the local daemon, which currently uses that same code path, and that connection information is restricted.

## moneromooo-monero | 2019-01-04T14:52:03+00:00
Well, actually, don't don't, since you bind to 0.0.0.0. Just ignore the 0/0 report, it'll get fixed in the medium term.

## sethforprivacy | 2019-01-04T15:00:19+00:00
Ok, awesome! I'll leave it and ignore that for now.

Closing.

## sethforprivacy | 2019-01-29T14:30:02+00:00
This has been fixed as of the latest round of commits on 1/28/2018.

# Action History
- Created by: sethforprivacy | 2019-01-03T21:14:26+00:00
- Closed at: 2019-01-04T15:00:19+00:00
