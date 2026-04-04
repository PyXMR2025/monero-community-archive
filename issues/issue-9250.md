---
title: monerod broken after latest update
source_url: https://github.com/monero-project/monero/issues/9250
author: Jayd603
assignees: []
labels:
- more info needed
created_at: '2024-03-14T15:04:40+00:00'
updated_at: '2024-03-19T04:29:25+00:00'
type: issue
status: closed
closed_at: '2024-03-19T04:29:19+00:00'
---

# Original Description
It has trouble getting caught up and was stuck syncing.  I Deleted the entire monero_data directory and had it re-sync the entire blockchain, it is still getting stuck on more recent blocks and not finishing sync.

Height: 3098510/3104955 (99.8%)



# Discussion History
## selsta | 2024-03-14T15:08:34+00:00
What kind of hardware and OS are you using? Where is your blockchain stored? How long did you wait?

## Jayd603 | 2024-03-14T15:10:10+00:00
Ubuntu server, 8 cpus , 16GB it's in a docker image , I used the same build commands as the previous build.  It uses an SSD array on the backend.  I waited many hours after it stopped at 99.8%

## selsta | 2024-03-14T15:12:10+00:00
How much resources did you give the docker container?

## selsta | 2024-03-14T15:14:25+00:00
If you let it run for 10 minutes, does it stay at `3098510` exactly?

Also can you share the output of `sync_info` and `status`?

## Jayd603 | 2024-03-14T15:15:13+00:00
It has no restrictions.  The version it downloaded was 18.3.3 , site says 18.3.2 is latest but i'm assuming someone snuck out 18.3.3 after.   

## Jayd603 | 2024-03-14T15:15:42+00:00
I'll try building the older version again for now

## Jayd603 | 2024-03-14T15:46:32+00:00
> If you let it run for 10 minutes, does it stay at `3098510` exactly?
> 
> Also can you share the output of `sync_info` and `status`?

It stays at the exact block, even after restart, I'm trying 18.3.1 now just to see if ti works, i can switch back and trouble shoot later just don't have enough time at the moment.

## selsta | 2024-03-14T15:53:29+00:00
I don't think this will help but try adding `--block-sync-size 10`.

## R-Caser | 2024-03-15T04:39:00+00:00
try the option 
--db-sync-mode safe

## Jayd603 | 2024-03-15T14:11:59+00:00
It's pausing when getting to the later blocks, this time it paused at Height: 3098624/3105618 (99.8%).  This happens with every version now.   This was a very busy public node now it's dead.  Not sure how these options would work but will try them.


## selsta | 2024-03-15T14:13:36+00:00
Do you have public RPC access enabled? If yes, disable it first until you are fully synced up.

## Jayd603 | 2024-03-15T14:18:05+00:00
> Do you have public RPC access enabled? If yes, disable it first until you are fully synced up.

Ok, I'm trying that.

So far it did not resume syncing, I wiped out the entire db and data directory and started again with rpc disabled.

## glv2 | 2024-03-15T16:19:54+00:00
@Jayd603 I have a node that had difficulties syncing because it had a slow network connection (around 400 kB/s download speed). It got stuck into a loop:
 1- connect to new peer
 2- start downloading block range from peer
 3- download fails because of timeout
 4- peer blocked
 5- back to step 1

If this is what is happening to your daemon, there should be many "Peer a.b.c.d blocked' messages in the logs.


## Jayd603 | 2024-03-16T13:44:13+00:00
Same thing -2024-03-16 13:40:16.026	I [77.183.126.48:18080 OUT] Sync data returned a new top block candidate: 3098624 -> 3106351 [Your node is 7727 blocks (10.7 days) behind]

Stuck there, once it gets to the newer blocks it hangs.  I can't seem to prevent this.

@glv2 this is my speed test result, the connectivity is very fast:
Idle Latency:     2.25 ms   (jitter: 0.09ms, low: 2.23ms, high: 2.41ms)
    Download:  4658.19 Mbps (data used: 5.0 GB)                                                   
                  2.38 ms   (jitter: 0.40ms, low: 2.00ms, high: 7.29ms)
      Upload:  4283.99 Mbps (data used: 3.0 GB)                                                   
                  2.39 ms   (jitter: 0.27ms, low: 2.04ms, high: 4.10ms)
 Packet Loss:     0.0%

I'm starting monerod like this:

CMD ["--non-interactive", \
    "--data-dir=/mnt/monero_data", \
    "--restricted-rpc", \
    "--rpc-bind-ip=0.0.0.0", \
    "--confirm-external-bind", \
    "--max-concurrency=5", \
    "--out-peers=3600", \
    "--prep-blocks-threads=4", \
    "--public-node", \
    "--limit-rate-down=800000", \
    "--limit-rate-up=800000", \
    "--block-sync-size=100", \
    "--max-log-file-size=10000000", \
    "--max-log-files=5" \
    ]

2024-03-16 03:08:48.217	I Synced 3098212/3106049 (99%, 7837 left, 91% of total synced, estimated 6.3 minutes left)
2024-03-16 03:08:57.362	I Host 64.98.82.40 blocked.
2024-03-16 03:09:04.731	I Synced 3098312/3106049 (99%, 7737 left)
2024-03-16 03:09:15.894	I Synced 3098412/3106049 (99%, 7637 left)
2024-03-16 03:09:30.100	I Synced 3098512/3106049 (99%, 7537 left)
2024-03-16 03:09:31.113	I Host 35.229.149.89 blocked.
2024-03-16 03:09:31.114	I Host 217.16.183.10 blocked.
2024-03-16 03:09:31.118	I Host 34.118.151.175 blocked.
2024-03-16 03:09:39.115	I Host 139.99.123.196 blocked.
2024-03-16 03:09:55.132	I Host 85.236.190.252 blocked.
2024-03-16 03:09:55.133	I Host 185.9.77.82 blocked.
2024-03-16 03:09:55.133	I Host 122.199.14.47 blocked.

..and then there are a lot of blocked hosts and it hangs.

I'm going to try again with db sync mode safe and sync size 10


## selsta | 2024-03-16T13:57:35+00:00
Please try starting `monerod` without any configuration options.

## Jayd603 | 2024-03-16T14:32:32+00:00
Starting with the minimun of: monerod --non-interactive --data-dir=/mnt/monero_data --restricted-rpc --rpc-bind-ip=0.0.0.0 --confirm-external-bind --public-node

..seems to have allowed syncing to resume.  The defaults are an issue though since this node normally has thousands of connections.  I did tuning options to get it to perform better.  I'll try slowly adding some back that impact performance of users

## selsta | 2024-03-16T14:35:29+00:00
I think you set a too high `--block-sync-size` value. Keep it at default. It has no impact on performance once you are fully synced up, so you don't have to re-add it.

## selsta | 2024-03-16T14:37:58+00:00
Also I would recommend to not enable public node access until you are fully synced up.

## Jayd603 | 2024-03-16T14:38:54+00:00
> Also I would recommend to not enable public node access until you are fully synced up.

Right, public access wasn't enabled, it wasnt forwarded by Docker.

## Jayd603 | 2024-03-16T14:43:53+00:00
So far it seems it may have been the block sync size of 100, even though it works up until the latest blocks and has always worked in the past.   This is probably a bug.

I will report back when fully synced and back up.  sync blocks 10 seems to be much slower, this would be bad for starting a new node and downloading the blockchain again right?

## selsta | 2024-03-16T14:46:36+00:00
If you set such a high block-sync-size it can happen that you request too much data from other nodes in a single request, which causes them to drop or not reply to you.

## Jayd603 | 2024-03-16T14:54:42+00:00
> If you set such a high block-sync-size it can happen that you request too much data from other nodes in a single request, which causes them to drop or not reply to you.

Ok, I'll look out for this when doing a full sync next time, maybe i'll try 50.


## Jayd603 | 2024-03-18T03:28:00+00:00
New bug?
2024-03-18 03:05:00.689	I [165.22.2.201:53552 INC] Sync data returned a new top block candidate: 3107490 -> 4613133 [Your node is 1505643 blocks (5.7 years) behind]

Except when I connect with my client, it's the latest block?


## selsta | 2024-03-18T04:52:19+00:00
It's not a bug, it's someone sending invalid data. You can apply my block list which has most of these peers included: https://gui.xmr.pm/files/block.txt

You don't have the apply the block list, it's just a harmless log message.

## Jayd603 | 2024-03-18T14:37:38+00:00
> It's not a bug, it's someone sending invalid data. You can apply my block list which has most of these peers included: https://gui.xmr.pm/files/block.txt
> 
> You don't have the apply the block list, it's just a harmless log message.

Oh ok, that makes sense.  Everything seems to be running fine then.  Thanks for the help.


## selsta | 2024-03-19T04:29:19+00:00
Closing this as there doesn't seem to be a bug introduced in the latest version.

# Action History
- Created by: Jayd603 | 2024-03-14T15:04:40+00:00
- Closed at: 2024-03-19T04:29:19+00:00
