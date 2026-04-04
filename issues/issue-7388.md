---
title: Monerod Not Honoring Upload Bandwidth Limit?
source_url: https://github.com/monero-project/monero/issues/7388
author: downystreet
assignees: []
labels: []
created_at: '2021-02-19T17:20:46+00:00'
updated_at: '2023-10-20T14:21:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Daemon Version: 0.17.1.9
OS: CentOS 8

When running monerod for longer than several hours I noticed that the bandwidth being used by the daemon is exceeding the default upload limit of 2048 kb/s. The Download rate has been within the limit. I have used several programs to monitor the connection and each one gives somewhat different readings. Monerod is the only program running on the server. When monitoring the server with nload I am seeing upwards of 25 Mbit/s sometimes. I also checked the data from the router and it indicated a reading of approximately 17 Mbit/s upload from the server. Nethogs gives a much lower upload speed when monitoring but it did go to over 3 Mbit/s which is over the limit of 2048 Mbit/s set in the daemon. I have also been noticing a lot of blocked host and unblocked host in the daemon output. Inbound connections are around 100. Sometimes the out connection will go over the default of 12 and be 13 in the daemon. 

# Discussion History
## hyc | 2021-02-19T17:58:49+00:00
Is your node doing P2P traffic only, or does it also have RPC enabled? I've noticed that only the P2P traffic honors the bandwidth limits, there is no limiter for RPC sessions.

But also note - the daemon sets limits in kB/sec. kilobytes/second. Not kilobits/second. So the default 0f 2048kB/s is 16Mb/s.

## downystreet | 2021-02-19T18:16:34+00:00
Yes, RPC is enabled. Nethogs is in Mb/s and the router and nload are Mbit/s.

## cirocosta | 2021-09-18T19:52:20+00:00
just for completeness: yes, indeed, throttling is _not_ activated for RPC:

https://github.com/monero-project/monero/blob/a39b1d56c8835798e2f5e3cc43c33b5f2d8e13da/contrib/epee/include/net/abstract_tcp_server2.inl#L930-L933

perhaps that should be more well advertised in the flags' description?

```
  --limit-rate-up arg (=2048)           set limit-rate-up [kB/s]
  --limit-rate-down arg (=8192)         set limit-rate-down [kB/s]
  --limit-rate arg (=-1)                set limit-rate [kB/s]
```

## hyc | 2021-09-19T00:13:18+00:00
I kinda think it ought to be. That's the reason I turned off public RPC on my public node, it was eating my monthly bandwidth quota.

## asheroto | 2022-08-17T15:08:55+00:00
Agreed.... +1 vote for this for the same reason... eating up the bandwidth

## Jayd603 | 2023-10-20T14:12:53+00:00
So... is that kB/s as in kBytes/s or kb/s as in Kbits/s (where as the upper case B usually denotes Bytes not bits)?    I set mine to 80000 , which in kBytes/s (upper case B) is 80 MBytes/s or 800 Mbits/s.   



# Action History
- Created by: downystreet | 2021-02-19T17:20:46+00:00
