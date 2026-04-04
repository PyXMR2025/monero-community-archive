---
title: monerod second instance started by GUI
source_url: https://github.com/monero-project/monero-gui/issues/3911
author: MainTsk
assignees: []
labels: []
created_at: '2022-05-05T21:37:25+00:00'
updated_at: '2023-02-15T15:51:19+00:00'
type: issue
status: closed
closed_at: '2023-02-15T15:51:19+00:00'
---

# Original Description
Linux x64
Ubuntu
Monero GUI 0.17.3.2 Mining monerod p2pool second daemon


The case is as follows:

The monerod is started a boot time. NO default directories used!

My lmdb is 100% synchronized. When I start the Monero GUI it connects to my local node. So far so good. 

The GUI connects to the already running monerod flawless and all is fine.

But when I start the mining by the GUI a second instance of the monero daemon seems to  initiated. 
I selected p2pool mining with main.
This second daemon is started with the wrong directory for the database. Default settings are used.
That brings it to the negative effect that the complete lmdb will be created (downloaded) again.

The problem I described above is repeatable.

My question is:

Why is the Monero GUI trying to establish a second daemon even it has connected successfully to daemon already running? 



# Discussion History
## selsta | 2022-05-06T06:21:46+00:00
@devhyper could you take a look?

## devhyper | 2022-05-06T18:17:56+00:00
The current behavior is that the monerod process is restarted every time p2pool mining starts, in order to add the zmq parameter. The issue is that when restarting monerod, the wallet gets its arguments from a field in the gui, rather than the running monerod process. I'm working on a fix, should be done later today.

@MainTsk To clarify, the first monerod stops properly and a second one is started with incorrect arguments, correct?

## MainTsk | 2022-05-06T19:40:37+00:00
@devhyper You are correct. I checked it today again. That's right. 

## MainTsk | 2022-05-06T20:02:48+00:00
@devhyper For your information. This is the command I use to start monerod at boot time.
**monerod.service entry:**
ExecStart=/home/nsa3/Monero/monero-gui/monerod --zmq-pub tcp://127.0.0.1:18083 --disable-dns-checkpoints --enable-dns-blocklist --tx-proxy i2p,127.0.0.1:8060 --add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p --anonymous-inbound xxxxxxxxxxxxxxx.b32.i2p,127.0.0.1:8061 --detach --data-dir=/home/nsa3/Monero/bc/.bitmonero/ --pidfile=/home/nsa3/Monero/md.pid

I hope this helps a little bit.

## selsta | 2022-05-07T16:43:13+00:00
@MainTsk This is untested but it might make sense for your use case to set the following:

- Settings -> Node: Add a remote node with `127.0.0.1:18081`
- Advanced -> Mining: Add `--host 127.0.0.1` to the P2Pool startup flags.

Then the GUI won't ever try to start/stop your daemon, as you use a service for that anyway.

## MainTsk | 2022-05-07T21:20:39+00:00
@devhyper I will try it tomorrow. Thank you.

## MainTsk | 2022-05-18T22:14:19+00:00
@devhyper Sorry for the late answer, but I was off. 
 I tried it, and it seems to work fine. 
I noticed when I changed from local to remote node the GUI doesn't connect to the remote node. I waited for a long time. 
But I had to close the GUI and open it again to connect to the remote node.

One question: 
When I close a wallet in the GUI, how to open it again from the main menu? I am using a hardware wallet.
Do I need to exit the GUI to reopen the wallet at start every time?

Thank you.




## devhyper | 2022-05-24T15:59:38+00:00
> But I had to close the GUI and open it again to connect to the remote node.

@MainTsk I'll open another PR to fix that issue.

# Action History
- Created by: MainTsk | 2022-05-05T21:37:25+00:00
- Closed at: 2023-02-15T15:51:19+00:00
