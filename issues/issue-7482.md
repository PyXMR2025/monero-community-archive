---
title: RPC connections stuck in CLOSE_WAIT on high load public RPC server
source_url: https://github.com/monero-project/monero/issues/7482
author: Gingeropolous
assignees: []
labels: []
created_at: '2021-03-09T05:06:50+00:00'
updated_at: '2022-07-16T15:56:54+00:00'
type: issue
status: closed
closed_at: '2022-07-16T15:56:54+00:00'
---

# Original Description
One of my public nodes sees a lot of connections.

I monitor the connection using nload. During normal operation, i see upwards of 100 - 200 Mbits / second upload, and an rpc connection count of 70+

sometimes, nload reports an upload of only 60 kbits/ second upload. During these times, if I use 

netstat -anp |grep 18089 | grep -v ESTABLISHED

I see loads of connections in the CLOSE_WAIT state. Once I restart monerod, the uploads go back to the 100s of mbits/sec range, and the loads of connections in CLOSE_WAIT go away. 

I notice that some of the connections in the CLOSE_WAIT state are from the same IP (9 connections). my most recent instance of this had 4 IPs that had 9 connections each, all in the CLOSE_WAIT state. Then 1 IP had 8, and 1 IP had 7. 

this happens so frequently I have to schedule monerod to restart every hour in the hopes that the service remains useful, but just recently I noticed the "bug" or whatever it is occurring after the node had 9 minutes of uptime. 

this is on ubuntu 18 on recent master (v0.17.0.0-b8f3e44a3)


# Discussion History
## vtnerd | 2021-03-12T14:38:24+00:00
Can you attach GDB the next time this happens to get a stacktrace. It sounds like something deadlocked. The [poorman's profiler](https://poormansprofiler.org/) will help with a command to execute.

## Gingeropolous | 2021-03-13T21:48:10+00:00
thread apply all bt

https://termbin.com/rnnu




## Gingeropolous | 2021-03-17T13:45:58+00:00
@vtnerd , this seems to be a problem with rpc-ssl. When rpc-ssl is disabled, this behavior no longer occurs. multiple other public node operators replicate. 

## vtnerd | 2021-03-31T13:22:14+00:00
I've been looking at this issue, and is indeed a pain to track down (duplicate). I may need some more information shortly.

## vtnerd | 2021-03-31T15:34:53+00:00
Nevermind, I can duplicate. I had the correct test, but the server shutdown was timing out and exiting, hiding the issue.

## selsta | 2022-02-19T00:20:19+00:00
This is fixed by the connection rewrite: https://github.com/monero-project/monero/pull/7760

## selsta | 2022-07-16T15:56:54+00:00
Should be fixed in #8426 / v0.18.0.0, if not please comment and I will reopen.

# Action History
- Created by: Gingeropolous | 2021-03-09T05:06:50+00:00
- Closed at: 2022-07-16T15:56:54+00:00
