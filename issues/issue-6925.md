---
title: There were 0 blocks in the last 20 minutes,v0.17.1.1
source_url: https://github.com/monero-project/monero/issues/6925
author: crlsim
assignees: []
labels: []
created_at: '2020-10-21T01:01:40+00:00'
updated_at: '2021-08-15T02:45:53+00:00'
type: issue
status: closed
closed_at: '2021-08-15T02:45:53+00:00'
---

# Original Description
Hi,I updated to v0.17.1.1,but err still:
There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
I can't sync on time.

# Discussion History
## selsta | 2020-10-21T01:03:09+00:00
Please post the output of status (daemon)

## crlsim | 2020-10-21T01:07:18+00:00
![image](https://user-images.githubusercontent.com/63048222/96660638-af214e00-137c-11eb-81d0-96eca74ca687.png)
I must restart daemon to sync.

## selsta | 2020-10-21T01:08:12+00:00
Please enter "status" and post the output here.

## crlsim | 2020-10-21T10:19:29+00:00
It seems that this issue only occurs when the daemon is running in _pm2_ mode, and when I run the daemon under cli directly, the synchronization works well.
![image](https://user-images.githubusercontent.com/63048222/96707025-ecf89380-13c9-11eb-99b9-2b84f67efde1.png)


## Crypto2 | 2020-10-21T20:35:35+00:00
We are having issues with it stopping syncing as well on v0.17.1.1, also using --detach running in a cron job.

## qiujun8023 | 2020-10-23T02:30:11+00:00
We have the same issues, restarting can be restored, but only for a few hours

## selsta | 2020-10-23T02:32:11+00:00
@qiujun8023 Is this also in detached / cron state?

Next time it gets stuck please post the output of ./monerod sync_info

You might also try increasing out-peers to 64 with --out-peers flag

## crlsim | 2020-10-23T02:40:51+00:00
Appear again in detached state
![image](https://user-images.githubusercontent.com/63048222/96950125-29d49f80-151c-11eb-8865-3a686089d8fb.png)


## selsta | 2020-10-23T02:42:13+00:00
@crlsim Can you post the output of sync_info?

You can do ./monerod sync_info

## qiujun8023 | 2020-10-23T02:47:51+00:00
> @qiujun8023 Is this also in detached / cron state?
> 
> Next time it gets stuck please post the output of ./monerod sync_info
> 
> You might also try increasing out-peers to 64 with --out-peers flag


```bash
./bin/monerod --config-file=$configfile --detach --pidfile=$pidfile
```

configfile

```ini
rpc-bind-ip=0.0.0.0
confirm-external-bind=yes

data-dir=xxxxxxxxxxx

log-file=xxxxxxxxxxx
```

I just restarted, and I’ll report when it gets stuck after a while

## qiujun8023 | 2020-10-23T02:56:55+00:00
I put the daemon log here, don't know if it helps.

https://paste.ubuntu.com/p/YnpCDwcXXh/

## qiujun8023 | 2020-10-23T06:05:10+00:00
The node stops synchronization again, the sync_info information is as follows


```json
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "credits": 0,
        "height": 2214370,
        "next_needed_pruning_seed": 0,
        "overview": "[]",
        "peers": [
            {
                "info": {
                    "address": "94.23.163.184:18080",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "9d967c7095924c5997f870c63555a770",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214276,
                    "host": "94.23.163.184",
                    "incoming": false,
                    "ip": "94.23.163.184",
                    "live_time": 11758,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "04f91b66d0986de9",
                    "port": "18080",
                    "pruning_seed": 0,
                    "recv_count": 22700701,
                    "recv_idle_time": 1,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3066923,
                    "send_idle_time": 1,
                    "state": "synchronizing",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "51.75.157.196:18080",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "5b738acf57784060a8519d1dfd69bd80",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "51.75.157.196",
                    "incoming": false,
                    "ip": "51.75.157.196",
                    "live_time": 11960,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "43c9ba85d30fc4a7",
                    "port": "18080",
                    "pruning_seed": 0,
                    "recv_count": 23181464,
                    "recv_idle_time": 10,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3143677,
                    "send_idle_time": 10,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "188.165.17.204:6557",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "33e19755503040a58306d6332a45ecd7",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "188.165.17.204",
                    "incoming": false,
                    "ip": "188.165.17.204",
                    "live_time": 12345,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "a3eb7d21ca4adbf5",
                    "port": "6557",
                    "pruning_seed": 0,
                    "recv_count": 23898655,
                    "recv_idle_time": 0,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3159353,
                    "send_idle_time": 0,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "51.91.33.151:13496",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "30cdf80f199d41f2b9909f9ed1cecba2",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2213936,
                    "host": "51.91.33.151",
                    "incoming": false,
                    "ip": "51.91.33.151",
                    "live_time": 12344,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "cd0fb75eccea7f86",
                    "port": "13496",
                    "pruning_seed": 0,
                    "recv_count": 23895252,
                    "recv_idle_time": 7,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3123602,
                    "send_idle_time": 7,
                    "state": "synchronizing",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "45.79.210.48:28159",
                    "address_type": 1,
                    "avg_download": 0,
                    "avg_upload": 0,
                    "connection_id": "38a676e922f04ec19df92df06e8ab274",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "45.79.210.48",
                    "incoming": false,
                    "ip": "45.79.210.48",
                    "live_time": 12358,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "014beea38dcc7680",
                    "port": "28159",
                    "pruning_seed": 0,
                    "recv_count": 7294726,
                    "recv_idle_time": 19,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 2754782,
                    "send_idle_time": 19,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "144.217.199.37:5508",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "69b7b0a8bbf04c168be275a783a837ad",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "144.217.199.37",
                    "incoming": false,
                    "ip": "144.217.199.37",
                    "live_time": 11852,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "b31df5ff146c632b",
                    "port": "5508",
                    "pruning_seed": 0,
                    "recv_count": 22942614,
                    "recv_idle_time": 3,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3131385,
                    "send_idle_time": 3,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "116.202.26.111:18080",
                    "address_type": 1,
                    "avg_download": 0,
                    "avg_upload": 0,
                    "connection_id": "d7c1e6b7140046d2b6023342c0d3ec57",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "116.202.26.111",
                    "incoming": false,
                    "ip": "116.202.26.111",
                    "live_time": 12371,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "43ac06f2b73d8915",
                    "port": "18080",
                    "pruning_seed": 0,
                    "recv_count": 8078958,
                    "recv_idle_time": 17,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 18089,
                    "send_count": 2153794,
                    "send_idle_time": 17,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "70.127.119.123:18080",
                    "address_type": 1,
                    "avg_download": 0,
                    "avg_upload": 0,
                    "connection_id": "50e7501f88ac4e99b8e0b8febc9c282d",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "70.127.119.123",
                    "incoming": false,
                    "ip": "70.127.119.123",
                    "live_time": 12371,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "f924099bc458b1aa",
                    "port": "18080",
                    "pruning_seed": 0,
                    "recv_count": 8148598,
                    "recv_idle_time": 14,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 2687750,
                    "send_idle_time": 14,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "54.37.179.243:6168",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "aa7fe8a19eb74cb9baae3a8712c09862",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "54.37.179.243",
                    "incoming": false,
                    "ip": "54.37.179.243",
                    "live_time": 12374,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "6010bbe2ccea8e36",
                    "port": "6168",
                    "pruning_seed": 0,
                    "recv_count": 23898741,
                    "recv_idle_time": 4,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3159645,
                    "send_idle_time": 4,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "51.89.181.107:7813",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "719ba30c228541e4969f1a03139ff0d5",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "51.89.181.107",
                    "incoming": false,
                    "ip": "51.89.181.107",
                    "live_time": 12375,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "c23a91b5e58a70f5",
                    "port": "7813",
                    "pruning_seed": 0,
                    "recv_count": 23898612,
                    "recv_idle_time": 7,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3159008,
                    "send_idle_time": 7,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "165.22.123.105:18080",
                    "address_type": 1,
                    "avg_download": 0,
                    "avg_upload": 0,
                    "connection_id": "1a8deebd46214f97a699a600348f3ad3",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "165.22.123.105",
                    "incoming": false,
                    "ip": "165.22.123.105",
                    "live_time": 12035,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "68fb53d7065bc1b6",
                    "port": "18080",
                    "pruning_seed": 0,
                    "recv_count": 3247170,
                    "recv_idle_time": 21,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 18089,
                    "send_count": 1926063,
                    "send_idle_time": 26,
                    "state": "normal",
                    "support_flags": 1
                }
            },
            {
                "info": {
                    "address": "193.70.78.196:7456",
                    "address_type": 1,
                    "avg_download": 1,
                    "avg_upload": 0,
                    "connection_id": "7c749d295ef042448b4b039763018555",
                    "current_download": 0,
                    "current_upload": 0,
                    "height": 2214370,
                    "host": "193.70.78.196",
                    "incoming": false,
                    "ip": "193.70.78.196",
                    "live_time": 12336,
                    "local_ip": false,
                    "localhost": false,
                    "peer_id": "7a0f630ab210970a",
                    "port": "7456",
                    "pruning_seed": 0,
                    "recv_count": 23898569,
                    "recv_idle_time": 6,
                    "rpc_credits_per_hash": 0,
                    "rpc_port": 0,
                    "send_count": 3158884,
                    "send_idle_time": 6,
                    "state": "normal",
                    "support_flags": 1
                }
            }
        ],
        "status": "OK",
        "target_height": 2214298,
        "top_hash": "",
        "untrusted": false
    }
}
```

## crlsim | 2020-10-23T07:57:43+00:00
![image](https://user-images.githubusercontent.com/63048222/96971470-b5aff100-1547-11eb-812f-6765ca9ff283.png)

Ok,I think I have to increase the out-peers to 64 as you said.

## qiujun8023 | 2020-10-23T09:25:04+00:00
> @qiujun8023 Is this also in detached / cron state?
> 
> Next time it gets stuck please post the output of ./monerod sync_info
> 
> You might also try increasing out-peers to 64 with --out-peers flag

@selsta I set out-peers to 64, but it doesn't work

## selsta | 2020-10-23T09:27:54+00:00
Just to confirm to everyone this this issue, this only happens in detached state?

## qiujun8023 | 2020-10-23T09:36:00+00:00
> Just to confirm to everyone this this issue, this only happens in detached state?

I will try to remove the detached parameter



## crlsim | 2020-10-23T11:01:38+00:00
I set out-peers to 64,it works at the beginning,but it only has 4 peers left a few hours later.

2020-10-23 10:47:57.813 I Monero 'Oxygen Orion' (v0.17.1.1-release)
Height: 2214510, target: 2214518 (99.9996%)
Downloading at 15 kB/s
4 peers
207.180.221.220:18080     42b56812c640eb62  synchronizing     0         2214518  13 kB/s, 8 blocks / 0 MB queued
209.180.103.52:18080      ac8c391c30192dc9  normal            0         2214510  2 kB/s, 0 blocks / 0 MB queued
135.181.96.2:18080        9ee20df213f92bae  normal            0         2214510  0 kB/s, 0 blocks / 0 MB queued
51.75.162.171:15909       c71460ae92b14006  normal            0         2214505  0 kB/s, 0 blocks / 0 MB queued
1 spans, 0 MB
[.]
207.180.221.220:18080     8/184 (2214510 - 2214517)  -

![image](https://user-images.githubusercontent.com/63048222/96996192-06344800-1562-11eb-81be-293bc48e008f.png)


## moneromooo-monero | 2020-10-23T12:25:05+00:00
Start monerod with --log-level 2 (it will log a lot), wait for this to happen, then paste the entire log somewhere like paste.debian.net, paste.ubuntu.log, or somewhere that does not need javascript to download.

## selsta | 2020-10-23T13:00:07+00:00
You can also compress the log file and drag and drop it here into a github comment if it is too large for pastebin site

## crlsim | 2020-10-24T00:51:49+00:00
This is the log with _--log-level 2_,hope to help you.
[bitmonero-log.tar.gz](https://github.com/monero-project/monero/files/5432227/bitmonero-log.tar.gz)


## moneromooo-monero | 2020-10-24T01:03:32+00:00
That log looks like it's been receiving blocks over the entire time. It also does not show the "there were 0 blocks..." message. Did you maybe include the wrong file ?

## qiujun8023 | 2020-10-24T09:15:03+00:00
> Just to confirm to everyone this this issue, this only happens in detached state?

@selsta The issue remains when the program is running in the foreground

sync_info
https://paste.ubuntu.com/p/bBrNqYDZqv/

![image](https://user-images.githubusercontent.com/10327533/97078120-2aecf600-161c-11eb-8e94-d93ddff7463b.png)


## moneromooo-monero | 2020-10-24T11:46:49+00:00
That one shows blocks, just more than expected.

## selsta | 2020-10-24T19:53:02+00:00
@qiujun8023 As moneromooo said there is no issue on your image, the "50 blocks in the past..." message is normal if the hashrate changes.

## tcphdr | 2020-10-24T20:33:16+00:00
I'm just going to comment here saying that I'm running a daemon on v0.17.1.1 in a non-detached state (in screen, always attached) and I also experience issues with syncing. My daemon just stops syncing sometimes. I've just restarted the daemon with --out-nodes 64 to see if the issue persists. I will post here once it does.

## moneromooo-monero | 2020-10-24T20:57:13+00:00
And please include a level 2 log, I want to see *why* connections drop, assuming they do, and you can only see that if you run with log level 2 *before* it happens.
I've been running with ll2 for more than a day now, and I'm still as 12 peers (some of their being the lying ones, which can cause sync to stop if you've got only those).

## tcphdr | 2020-10-24T22:23:24+00:00
> And please include a level 2 log, I want to see _why_ connections drop, assuming they do, and you can only see that if you run with log level 2 _before_ it happens.
> I've been running with ll2 for more than a day now, and I'm still as 12 peers (some of their being the lying ones, which can cause sync to stop if you've got only those).

I've got it running in log level 2, I'll post results when this happens.

## crlsim | 2020-10-25T01:14:44+00:00
I have been running the daemon with _--log-level 2_ for about 24 hours on my 2 vps and this warning does not appear again. I found that there will be a delay in synchronization on a VPS with 512M RAM, and everything is normal on a VPS with 1G RAM. I am not sure if it is related to the RAM size.

## qiujun8023 | 2020-10-25T01:18:12+00:00
> > Just to confirm to everyone this this issue, this only happens in detached state?
> 
> @selsta The issue remains when the program is running in the foreground
> 
> sync_info
> https://paste.ubuntu.com/p/bBrNqYDZqv/
> 
> ![image](https://user-images.githubusercontent.com/10327533/97078120-2aecf600-161c-11eb-8e94-d93ddff7463b.png)

@selsta 

The block height of the node stops at 2214983, which is consistent with "sync_info.result. target_height".
But the latest blockchain is 2214856, which is consistent with "sync_info.result. result".

The server network is normal and there is no problem with the firewall. Run on AWS, Singapore

BTW, I also use log level 2 to run the node, if there are any similar results, I will append here


## crlsim | 2020-10-25T02:43:21+00:00
Sorry,It reappeared on the 512M RAM vps just now.
![image](https://user-images.githubusercontent.com/63048222/97097538-6931f600-16ac-11eb-8ecc-e5748d3d2273.png)
[bitmonero-log.tar.gz](https://github.com/monero-project/monero/files/5434085/bitmonero-log.tar.gz)
[bitmonero-log1.tar.gz](https://github.com/monero-project/monero/files/5434091/bitmonero-log1.tar.gz)


## moneromooo-monero | 2020-10-25T19:20:11+00:00
You seem to have lots of peers still, and a good number of them are lying peers. You're likely connected only to those, and they're just not sending you blocks.
#6933 should improve the situation, though not fix it outright.

## Crypto2 | 2020-10-25T21:03:09+00:00
If you are connected to even or two good ones how can lying ones stop you from syncing? Since you'd still be receiving blocks from the good ones?

## moneromooo-monero | 2020-10-26T00:54:01+00:00
If at least one peer sends you good blocks, you're good.

## crlsim | 2020-10-26T01:04:58+00:00
Ok,thanks.

## moneromooo-monero | 2020-10-26T12:56:03+00:00
#6936 should prevent this, if the reason is getting only asshole peers.

## selsta | 2020-11-13T08:42:00+00:00
v0.17.1.3 has multiple mitigations against this happening, please report back if this happens again with v0.17.1.3

## selsta | 2021-08-15T02:45:53+00:00
This issue should be resolved in v0.17.2.0

# Action History
- Created by: crlsim | 2020-10-21T01:01:40+00:00
- Closed at: 2021-08-15T02:45:53+00:00
