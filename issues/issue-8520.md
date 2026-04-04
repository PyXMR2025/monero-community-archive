---
title: 'monerod: incoming peers unreasonably low'
source_url: https://github.com/monero-project/monero/issues/8520
author: li5lo
assignees: []
labels:
- bug
created_at: '2022-08-20T00:09:19+00:00'
updated_at: '2023-02-28T17:42:58+00:00'
type: issue
status: closed
closed_at: '2023-02-28T17:42:22+00:00'
---

# Original Description
Running monero mainnet, stagenet, testnet and wownero mainnet on the same hardware and IP address.


Since months i have a very low count of `in` peers (5 at most and sometimes 0 over many days).
It started on testnet and stagenet long before they forked and since the recent hardfork mainnet is affected too.

Sometimes the `in` peers suddenly go up to 50-150 (mainnet) and are back close to zero a few hours later.

Changing IP address doesn't help and switching `monerod` off for a couple of days doesn't help either.

`wownerod` seems to be unaffected so i don't think it's related to my hardware or internet and `Monero CLI` was downloaded and hash verified from the official website.

I watched the peerlist size behavior on `wownerod` and it looks healthy how the greylist decreases and the whitelist increases until a new chunk is added to the greylist but with `monerod` the amount of peers in both lists seems to stay almost the same which could indicate a problem with greylist housekeeping in `monerod` but i don't know how to investigate further.

# Discussion History
## selsta | 2022-08-20T00:22:02+00:00
Since which version do you have this issue?

I run multiple nodes and so far did not notice this behavior.

## li5lo | 2022-08-20T00:51:55+00:00
> Since which version do you have this issue?

I don't know anymore which version.

I wrote [this post ](https://www.reddit.com/r/Monero/comments/r9ib3j/open_your_ports/) 9 months ago and i already had the problem at least 4 months earlier.
It could be even earlier because i was not checking peerlist sizes back then.

I got inspired to finally write this bug report because [it seems i might not be alone anymore](https://www.reddit.com/r/Monero/comments/wsd6tc/monerod_connection_problem/).

## li5lo | 2022-08-20T00:54:06+00:00
Wait, what i wrote in the post 9 months ago is not the same problem...

## li5lo | 2022-08-20T00:58:29+00:00
9 months ago apparently i had the problem to find outgoing peers, now i have a problem to find incoming peers.

## selsta | 2022-08-20T01:00:38+00:00
Which OS do you have? 4 of my Linux nodes are okay, my macOS node can reproduce the issue.

## li5lo | 2022-08-20T01:04:23+00:00
> Which OS do you have? 4 of my Linux nodes are okay, my macOS node can reproduce the issue.

Ubuntu 22.04

## selsta | 2022-08-20T01:07:07+00:00
When did this issue started showing up for you? Also are the out peers unaffected? Can you set them higher than default?

## selsta | 2022-08-20T01:18:26+00:00
Can you run your daemon with log level 2 for a couple minutes and then upload logs? Just trying to confirm if you have the same error.

## li5lo | 2022-08-20T01:30:09+00:00
> When did this issue started showing up for you?

The issue that i don't have enough **outgoing** connections apparently resolved itself somewhere between 9 months ago and _some time ago_ and i recall incoming and outgoing were normal _for some time_ and i stopped to frequently check them.

The issue that i don't have enough **incoming** connections started _recently_ (maybe after the hardfork on each of the chains but i am not sure because i just learned that the chains forked at different blocks. Some day just saw 0 connections and thought it's the same problem like before so i don't remember when it exactly started on testnet and stagenet.)

But i was checking my mainnet node peers during the hardfork and at the forkblock the incoming connections dropped significantly, recovered, then stayed at the low level it is now.

> Also are the out peers unaffected?

Almost.

Mainnet: 12 (out) 1 (in)
Testnet: 12 (out) 0 (in)
Stagenet: 5 (out) 0 (in)

> Can you set them higher than default?

I can :)
Should i? To what number?

## selsta | 2022-08-20T01:31:56+00:00
I'm more interested in log level 2, you don't have to change out peers. It is not really relevant.

## ghost | 2022-08-20T02:02:20+00:00
Hi I'm u/MPodom352 from reddit. Thanks for posting the link here.
Here's my monerod log, at log level 2
[monerod.log](https://github.com/monero-project/monero/files/9386034/monerod.log)
I ran `status` before killing it. There was only 12 outgoing peers and 1 incoming peer.
I synced the node before running it and thought it would help filtering "useless" sync info but connection status. Let me know if I did it wrong.
Here's how I ran monerod 
`./monerod --zmq-pub tcp://127.0.0.1:18083 --disable-dns-checkpoints --enable-dns-blocklist --log-level 2 --log-file /home/pc/Downloads/monerod.log`
I'm running monero-gui v0.18.1 release | Fedora 36 without firewall

## selsta | 2022-08-20T02:08:39+00:00
I don't see anything interesting in your log, but I only skimmed over it. Let's see if we can also get a log from @computerfreak94 

## selsta | 2022-08-20T02:12:00+00:00
@AsBenDoge The issue is that 3 minutes uptime is likely not enough for this issue to show up, that's why I don't see anything in your log.

## ghost | 2022-08-20T02:35:29+00:00
[monerod.log](https://github.com/monero-project/monero/files/9386068/monerod.log)
Here's the log of monerod running for ~17 minutes
I added `--out-peers 50 --in-peers 50` to the command this time. Status show `50(out)+1(in)` before killed.

## selsta | 2022-08-20T02:46:43+00:00
I still don't see anything interesting, will have to let someone else look. @AsBenDoge if you completely restart your computer, do you still not get more than 1 incoming connection?

At this point I'm unsure if the issue I have on my macOS node is related to this issue here. This is my macOS node after a complete restart:

```
Height: 2693377/2693377 (100.0%) on mainnet, not mining, net hash 2.37 GH/s, v16, 12(out)+54(in) connections, uptime 0d 1h 9m 50s
```

## ghost | 2022-08-20T02:55:47+00:00
@selsta I did multiple restart. It seems that only one incoming connection is "stable". If I start monerod and spam `status`, sometimes there's 3-4 incoming connection but a few seconds later it's gone.


## li5lo | 2022-08-20T03:04:59+00:00
OK!

I have about 20 minutes of `loglevel 2` for mainnet, stagenet and testnet together with the `loglevel 0` logs history of the last couple of days since i started monerod where i occasionally run `status` and `print_pl_stats`.

I should add that i currently have a daily changing IP address (somewhere between 02:30 and 02:40 monero log time) because my ISP is currently incompetent so don't rely on the `print_pl_stats` too much because if they were printed too soon after the IP address change the numbers are obviously odd.

My daily changing IP doesn't seemed to have an effect on this problem because if the peer number was low before the IP change it stayed low after the IP change and if they were normal before the IP change then it didn't took long to recover.

In the stagenet logs you will also see a crash at the end which can be ignored and likely happened because `monerod` and everything on this server was already running for more than a week and `lmdb` already took a lot of the RAM so opening firefox was probably too much for this poor computer.


Can i send you the logs in private somehow @selsta ? 
Not that it would really matter in a public P2P network but my IP address will obviously be prominent in the logs and the world doesn't need to know it if not necessary.

All three files together are 13 Megabyte and i could probably upload them encrypted here if they are not too big for github but i would need to send you the password.

## selsta | 2022-08-20T03:11:03+00:00
I only need 20 minutes of loglevel 2 for mainnet, log 0 does not show anything useful. Can you search for your IP in the log and redact it and then upload here on Github? Would be the easiest way.

## li5lo | 2022-08-20T03:38:26+00:00
Here you go:
[mainnet.log](https://github.com/monero-project/monero/files/9386187/mainnet.log)

## moneromooo-monero | 2022-08-20T10:17:21+00:00
You are seeing incoming connections from 91.198.115.x, with plenty of different x, every 2 seconds. Looks like someone maybe trying to spam your peerlists.

In any case, a roving IP address means that most of the network will have the old address on file, and goes a long way to explaining the low amount of incoming connections. I *think* a smaller network will not be as affected since your node is a comparatively much larger portion of the nodespace so a "replacement" for your now inaccessible node on the old address will be much less readily found by those nodes trying to fill their outgoing connection slots.


## li5lo | 2022-08-20T16:54:36+00:00
> You are seeing incoming connections from 91.198.115.x, with plenty of different x, every 2 seconds. Looks like someone maybe trying to spam your peerlists.

Indeed for mainnet.
I didn't found IP addresses starting with 91.198.115.x in the stagenet and testnet logs.

> In any case, a roving IP address means that most of the network will have the old address on file, and goes a long way to explaining the low amount of incoming connections. I _think_ a smaller network will not be as affected since your node is a comparatively much larger portion of the nodespace so a "replacement" for your now inaccessible node on the old address will be much less readily found by those nodes trying to fill their outgoing connection slots.

I see how you came to this conclusion but:
- The problem started on testnet, then stagenet, then mainnet (maybe correlated with when i started to run version 0.18.x but i really don't know this for sure anymore) and i assume stagenet and testnet are much smaller than mainnet and probably not bigger than wownero mainnet (which appears to work flawless).
- I have a daily changing IP address since February/March/April (dunno for sure anymore and can't easily check without calling my ISP) but the problem on mainnet started less than a month ago.
- If my daily changing IP address would be a big factor then my incoming connections should probably slowly fall over time, no?
But it always was a rapid fall during minutes or a few hours that didn't recovered at all even after 20+ hours.

I had occasional IP address changes before this problem and i always saw a (very) fast recover to reasonable peer numbers during minutes or few hours at most but since the problem started, my IP address change doesn't seem to make any difference at all because the peer number is always low.
It doesn't matter if my IP address is stable for the last 20 hours or if it changed 1 minute ago.
`monerod` seems to not even try to find new friends.
 
I don't know if we think that my disappeared problem with low **outgoing** connections could be related to my current problem with low **incoming**  connections (what doesn't goes `out` somewhere can not go `in` somewhere...) but the problem with the **outgoing** connections happened long before my IP address was changing daily.

(My ISP will replace their hardware in our basement _before the end of the year_ and then i should again have an IP address that changes only once each 2-3 months or when i force the IP change so if nothing is found we could wait and see how `monerod` behaves then.)

## selsta | 2022-08-20T17:01:38+00:00
Do you know how to compile monero yourself? We had a larger connection related rewrite, you might want to revert it and check if you continue to have the same issue:

```
git revert -S 9df069f4cefb20cc4dd172696a5c74888bd6d9d1 -m 1
```

## vtnerd | 2022-08-20T17:26:17+00:00
Looked at the logs. The connection object is being destroyed quickly after receiving a message, but its not clear why. There might be a case in the connection code where no async op is being queued, and therefore everything just gets closed out. Strange that there aren't more people reporting this issue though. If the poster doesn't have issues after reverting that commit then it would narrow it down.

## moneromooo-monero | 2022-08-20T18:05:30+00:00
When there is no logged reason, it's the peer cutting the connection (or, I guess some kind of network error, but this'd be one off I think).

## vtnerd | 2022-08-20T18:09:40+00:00
@computerfreak94 what type of CPU?

~I reviewed some of the code, and I think there are some issues related to async timeouts. I'm 99% (at the moment) that the handler _must_ check for `operation_canceled` in the error code; I never seen anyone use a state flag for this as it should be racy.~ 

## vtnerd | 2022-08-20T18:21:34+00:00
Nevermind, spoke too quickly, retract last comment.

## ShadowStorm0 | 2022-08-20T21:12:01+00:00
I am able to get only 1 incoming connection at the start than after a few seconds after Monerod displays all the blocked IP's, I get 0 incoming. 

## li5lo | 2022-08-20T21:16:02+00:00
> Do you know how to compile monero yourself?

@selsta 
Maaaybe ...
I compiled something from source a while ago and somehow it worked after a lot of try and error.
> 
> ```
> git revert -S 9df069f4cefb20cc4dd172696a5c74888bd6d9d1 -m 1
> ```
I don't know what this means or where to run this command.

I would feel a lot more easy with it when someone of the names i know could give me the `monerod` file (the other files can stay, no?) so that i only need to replace it with the current `monerod` file.

@vtnerd
Intel Core i5-6500 3,20 GHz

@moneromooo-monero
I will post accurate numbers in a few hours how long it took for `wownerod` to recover after an IP address change.


To be sure that nothing else on the server distracts `monerod`/`wownerod` i just rebooted and kept all my other stuff that usually runs there switched off.

## selsta | 2022-08-20T22:33:08+00:00
@computerfreak94 CI build with connection patch reverted: https://github.com/selsta/monero/suites/7904407827/artifacts/336290979

## li5lo | 2022-08-21T03:24:52+00:00
Before the IP change:
```
mainnet: 12 / 2 
testnet: 11 / 0 
stagenet: 6 / 0 
wownero: 12 / 34
```

5 minutes after the IP change:
```
mainnet: 12 / 0
testnet: 11 / 0
stagenet: 5 / 0
wownero: 12 / 6
```

10 minutes after the IP change:
```
mainnet: 12 / 0
testnet: 11 / 0
stagenet: 5 / 0
wownero: 12 / 20
```

15 minutes after the IP change:
```
mainnet: 12 / 0
testnet: 11 / 0
stagenet: 5 / 0
wownero: 12 / 33
```

20 minutes after the IP change:
```
mainnet: 12 / 0
testnet: 11 / 0
stagenet: 5 / 0
wownero: 12 / 42
```

25 minutes after the IP change:
```
mainnet: 11 / 0
testnet: 11 / 0
stagenet: 5 / 0
wownero: 12 / 53
```

So `wownerod` happily went along and was completely recovered after 15 minutes while `monerod` stayed where it was.

Will now run mainnet and stagenet with the new `monerod` from above (keeping testnet on monerod 0.18.1 for comparison) and will report back in a few hours/days.

## li5lo | 2022-08-22T07:47:13+00:00
Before the IP change:

```
mainnet (running for 23h 30m with the new monerod) : 14 / 3
testnet (running for 7h 50m with monerod 0.18.1)   : 11 / 0
stagenet (running for 23h 30m with the new monerod): 5 / 0
wownero: (running for 1d 6h 44m)                   : 12 / 41
```

Probably not related to this problem but testnet `monerod 0.18.1` crashed after a few hours, which has happened only two or three times in the last 2 years unless the server was under heavy load which couldn't be the reason this time because everything else is switched off and there is plenty of CPU and RAM.

The monero log shows nothing on `log level 0` but i think these are the relevant lines from syslog:

```
<timestamp> <servername> kernel: [78287.802036] monerod[3542]: segfault at d0 ip 000055c93cfd9e96 sp 00007f4b37afd840 error 4 in monerod[55c93cc00000+10dd000]
<timestamp> <servername> kernel: [78287.802070] Code: 51 3c 4c 89 69 40 48 89 41 30 41 8b 44 24 10 4c 89 79 50 89 41 48 f3 0f 6f 03 0f 11 41 58 48 8b 43 10 48 89 41 68 0f b6 45 a8 <41> 83 7d 00 ff 48 89 4d c0 41 89 c7 74 5c 48 8d 1d 55 75 f8 00 0f
```

I have now seen that all `monerod` and `wownerod` spam a lot of these loglines in the syslog:

```
<timestamp> <servername> tracker-extract[47114]: Task for 'file:///home/<redacted>/Monero/mainnet/lmdb/data.mdb' finished with error: Could not get any metadata for uri:'file:///home/<redacted>/Monero/mainnet/lmdb/data.mdb' and mime:'application/vnd.ms-access'
<timestamp> <servername> tracker-extract[49630]: Task for 'file:///home/<redacted>/Monero/testnet/lmdb/data.mdb' finished with error: Could not get any metadata for uri:'file:///home/<redacted>/Monero/testnet/lmdb/data.mdb' and mime:'application/vnd.ms-access'
<timestamp> <servername> tracker-extract[47168]: Task for 'file:///home/<redacted>/Monero/stagenet/lmdb/data.mdb' finished with error: Could not get any metadata for uri:'file:///home/<redacted>/Monero/stagenet/lmdb/data.mdb' and mime:'application/vnd.ms-access'
<timestamp> <servername> tracker-extract[49630]: Task for 'file:///home/<redacted>/WOWNERO/mainnet/lmdb/data.mdb' finished with error: Could not get any metadata for uri:'file:///home/<redacted>/WOWNERO/mainnet/lmdb/data.mdb' and mime:'application/vnd.ms-access'
```

5 hours after the IP change:

```
mainnet (running for 1d 4h 23m with the new monerod) : 13 / 1
testnet (running for 12h 42m with monerod 0.18.1)    : 11 / 0
stagenet (running for 1d 4h 23m with the new monerod): 6 / 0
wownero (running for 1d 11h 37m)                     : 12 / 47
```

Do we learn more when i wait another day (and another IP change) ?

## vtnerd | 2022-08-22T13:09:32+00:00
@computerfreak94 this last post was using @selsta custom build?

## li5lo | 2022-08-22T14:04:12+00:00
Yes.
Mainnet and stagenet is running @selsta custom build (aka `new monerod`) and testnet stayed on `monerod 0.18.1.0-release`.
My post above contains the results from this test.

mainnet:

```
<timestamp>	    7f51008c5bc0	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.1.0-f89dc9ea0)
<timestamp>	    7f51008c5bc0	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
<timestamp>	    7f51008c5bc0	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
<timestamp>	    7f51008c5bc0	INFO	global	src/daemon/core.h:64	Initializing core...
<timestamp>	    7f51008c5bc0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:519	Loading blockchain from folder /home/<redacted>/Monero/mainnet/lmdb ...
...
<timestamp>	    7f2a4da2a640	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 2695196/2695196 (100.0%) on mainnet, not mining, net hash 2.53 GH/s, v16, 12(out)+3(in) connections, uptime 1d 10h 53m 25s
```

testnet:

```
<timestamp>	    7fb89827f780	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.1.0-release)
<timestamp>	    7fb89827f780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
<timestamp>	    7fb89827f780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
<timestamp>	    7fb89827f780	INFO	global	src/daemon/core.h:64	Initializing core...
<timestamp>	    7fb89827f780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:519	Loading blockchain from folder /home/<redacted>/Monero/testnet/lmdb ...
...
<timestamp>	    7fb44b22d640	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 2051694/2051694 (100.0%) on testnet, not mining, net hash 2.74 kH/s, v16, 11(out)+0(in) connections, uptime 0d 19h 12m 34s
```

stagenet:

```
<timestamp>	    7fe20d392bc0	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.1.0-f89dc9ea0)
<timestamp>	    7fe20d392bc0	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
<timestamp>	    7fe20d392bc0	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
<timestamp>	    7fe20d392bc0	INFO	global	src/daemon/core.h:64	Initializing core...
<timestamp>	    7fe20d392bc0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:519	Loading blockchain from folder /home/<redacted>/Monero/stagenet/lmdb ...
...
<timestamp>	    7fd83a22b640	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 1163059/1163059 (100.0%) on stagenet, not mining, net hash 1.96 kH/s, v16, 6(out)+0(in) connections, uptime 1d 10h 53m 12s
```

## t5awd | 2022-08-22T17:13:20+00:00
> @computerfreak94 CI build with connection patch reverted: https://github.com/selsta/monero/suites/7904407827/artifacts/336290979

I've run this for five hours and still have 0 incoming connections. It seems that reverting the patch does not solve the problem.

Devuan Linux (Based on Debian Bullseye (11.1) with Linux kernel 5.10.0-17), p2p port definitely open and available.

## ghost | 2022-08-23T13:38:28+00:00
> @computerfreak94 CI build with connection patch reverted: https://github.com/selsta/monero/suites/7904407827/artifacts/336290979

Same here. Running v0.18.0/1 and your patch reverted build with/without sudo. Still 1 "stable" incoming connection.
Am able to get 3-4 incoming peers with v0.17.3.2 (with sudo), with `--limit-rate-down 100` and `out_peers 1` (everything else same) as I don't want to really re-download the blockchain. I'm sure I can get more if I didn't set the rate limit.

Could do a test with synced, pruned blockchain on v0.17.3.2 on demand. Here's the log (`loglevel 2`) of monerod v0.17.3.2 (syncing, only did ~3 mins as the log file is huge, ~50k log lines were deleted):
[bitmonero.log](https://github.com/monero-project/monero/files/9402937/bitmonero.log)
`sudo ./monerod --zmq-pub tcp://127.0.0.1:18083 --disable-dns-checkpoints --enable-dns-blocklist --out-peers 1 --in-peers 100 --limit-rate-down 100 --data-dir /home/pc/Downloads --log-level 2`

@t5awd @computerfreak94 Could you please do a test with (v0.17.3.2) the command above? Just want to make sure that it's reproduce-able. 

## selsta | 2022-08-23T16:13:20+00:00
Another thing to try is deleting `~/.bitmonero/p2pstate.bin`, it contains the peer list.

## ghost | 2022-08-24T02:12:09+00:00
> Another thing to try is deleting `~/.bitmonero/p2pstate.bin`, it contains the peer list.

Testing it right now. With a wrong command (that one in previous comment) I discovered a new warning which is not seen in either mine or @computerfreak94's log.
`2022-08-24 01:45:16.070	[P2P3]	WARNING	net.p2p	src/p2p/net_node.inl:2547	[77.231.39.205:41669 INC] COMMAND_HANDSHAKE came, but process_payload_sync_data returned false, dropping connection.`
Full log:
[bitmonero.log](https://github.com/monero-project/monero/files/9411815/bitmonero.log)

## selsta | 2022-08-24T02:16:01+00:00
If you are on v0.18 then you can't use v0.17 to do tests. The blockchain forked already.

## t5awd | 2022-08-24T02:21:51+00:00
> Another thing to try is deleting `~/.bitmonero/p2pstate.bin`, it contains the peer list.

This did not have any effect. Still 0 incoming connections after 8 hours of uptime.

## selsta | 2022-08-24T02:29:06+00:00
Does anyone want to share their IP? Or alternative they can send it on IRC / matrix to me. Then I can try to connect to it via `--add-exclusive-node` and see why it drops.

## ghost | 2022-08-24T02:48:18+00:00
> If you are on v0.18 then you can't use v0.17 to do tests. The blockchain forked already.

That's why I pointed data dir to another directory. v0.17 had more incoming peers than v0.18 under same command (except --data-dir)
My latest comment is done on v0.18.1

> Another thing to try is deleting `~/.bitmonero/p2pstate.bin`, it contains the peer list.

Did not work for me. Still one incoming connection (100 out)

> Does anyone want to share their IP? Or alternative they can send it on IRC / matrix to me. Then I can try to connect to it via `--add-exclusive-node` and see why it drops.

I can't reach you by @selsta_:libera.chat. My matrix is @bendog_1234:matrix.org


## li5lo | 2022-08-24T07:13:42+00:00
I switched off mainnet `monerod 0.18.1.0-f89dc9ea0` and testnet `monerod 0.18.1.0-release` before the daily IP change 
and deleted `p2pstate.bin` for each of them.
(Kept stagenet `monerod 0.18.1.0-f89dc9ea0` as is).

The incoming connections for testnet came back!
Mainnet stayed low where it was.

`Height: 2696388/2696388 (100.0%) on mainnet, not mining, net hash 2.31 GH/s, v16, 12(out)+2(in) connections, uptime 0d 4h 5m 57s`
`Height: 2052922/2052922 (100.0%) on testnet, not mining, net hash 3.29 kH/s, v16, 10(out)+27(in) connections, uptime 0d 4h 6m 0s`
`Height: 1164281/1164281 (100.0%) on stagenet, not mining, net hash 1.82 kH/s, v16, 4(out)+0(in) connections, uptime 3d 3h 51m 11s`

> Does anyone want to share their IP?

I _think_ i could even give you a hostname so you would survive my daily IP changes.
But definitely only in private because you _might_ get direct access to my router login interface (need to read more in their documentation).

> Or alternative they can send it on IRC / matrix to me.

I don't have matrix but i could probably do this when you tell me where.

Session messenger (or other alternatives that don't require a sign-up) would be the most suitable for me.

## moneromooo-monero | 2022-08-24T11:41:45+00:00
If you're on IPv4, there are scripts that systematically walk through the entire IPv4 space to find things like this, so I'd get on that reading pretty fast. Any sane router will listen only to LAN connections for management though.

## li5lo | 2022-08-24T13:59:01+00:00
I know what you thought and thanks for caring but it's not what you think :) @moneromooo-monero 

#offtopic
The opt-in DynDNS service is from the router manufacturer and it seems i'd have to toggle two switches in the router to be doomed.
The first one will allow specific username and password combinations to login from the internet over HTTPS without VPN.

The second switch would enable it to use port 443 or a randomly specified port to access the login page over HTTPS without VPN.
_(That's what you thought, no? :)_

So with the first one i decide which user account is allowed to access over the internet and with the second one i show the login page and now i understand why they hide the second one so deep in the settings.

~~I just don't understand why i always reach my router login page from the LAN when using the DynDNS hostname.
My current guess is that the DNS server on the router catches it and forwards me there because it's coming from the inside but better safe than sorry.
Will need to verify this when we are done here and my unbound VM is switched back on.~~

#offtopic end

## selsta | 2022-08-24T17:42:13+00:00
@t5awd sent me their IP and I had no issues connecting to it over hours. So it seems nodes don't connect in the first place, but I will need more IPs to say with certainty.

@AsBenDoge messaged you now

## li5lo | 2022-08-25T04:20:02+00:00
Although i changed nothing and stagenet still running on `monerod 0.18.1.0-f89dc9ea0` with it's old `p2pstate.bin`, it's **incoming** connections suddenly came back to life as well.

`Height: 2697058/2697058 (100.0%) on mainnet, not mining, net hash 2.52 GH/s, v16, 13(out)+2(in) connections, uptime 1d 1h 21m 40s`
`Height: 2053583/2053583 (100.0%) on testnet, not mining, net hash 3.44 kH/s, v16, 12(out)+23(in) connections, uptime 1d 1h 31m 32s`
`Height: 1164948/1164948 (100.0%) on stagenet, not mining, net hash 1.91 kH/s, v16, 5(out)+24(in) connections, uptime 4d 1h 16m 49s`

## ghost | 2022-08-25T04:30:16+00:00
Mine too....
`Height: 2697070/2697070 (100.0%) on mainnet, not mining, net hash 2.51 GH/s, v16, 100(out)+93(in) connections, uptime 1d 1h 34m 56s`
I deleted p2pstate.bin, reboot several times and it's fine. :)

## moneromooo-monero | 2022-08-25T11:47:39+00:00
If your node is on a /16 where a sybil controls a lot of the other IPs, you'll be connected to a lot less since nodes will avoid connecting to a node on a /16 they're already connected to.
In order to make a noticeable difference, they'd have to control a lot though. Like 32k IPs in order to decrease your incoming rate by 50%.
A more interesting one could be if you have a shared IP externally. In that case, I think peer lists remember only the port they've been told about last. That's a lot more easy to remove a target node from the list.
But it's a lot of hassle for being annoying to just a node. It doens't seem worth the bother, though someone has repeatedly shown before they're willing to do a lot of work for not much accomplished, so you never know.

Still, those things are not super likely to be the reason vs just an elusive bug.



## moneromooo-monero | 2022-08-25T11:51:43+00:00
Actually, a lot less than 32k IPs needed on the same /16: if Eve ensures she's actually connected via one of the IPs on that /16 to most nodes, every node she's connected to will avoid your node.

Is your IP in the 91.198.x.y range by any chance ?


## t5awd | 2022-08-25T12:28:31+00:00
No change in behavior for my daemon. I went back to the regular build of monerod because the connection-patch-reverted version 0.18.1.0-f89dc9ea0 didn't appear to help with the problem. Still 0 incoming connections, port verified open and even selsta could manually connect to me.

## li5lo | 2022-08-25T15:23:03+00:00
@moneromooo-monero 

I am not really familiar with subnetting but it looks like my ISP owns 4 /16 IPv4 subnets + roughly 70 aquired IPv4 subnets of different sizes that add up to roughly 500.000 IPv4 addresses.
I always saw IP addresses from two of these four /16 in my router and another region to where my ISP recently expanded seems to always get one of the other /16 subnets.

My ISP is a regional ISP and on monero.fail/map i found two nodes (+ my node that currently doesn't appear on the map) that are running in their IP space.

> A more interesting one could be if you have a shared IP externally.

No NAT/PAT between my router and the rest of the world.
I have a globally reachable IPv4 address and a globally reachable IPv6 /56.
Both dynamically assigned and currently both changing daily.

> Is your IP in the 91.198.x.y range by any chance ?

No.

## li5lo | 2022-08-26T12:15:03+00:00
Stagenet is back at zero incoming peers over the last hours.

`Height: 2697990/2697990 (100.0%) on mainnet, not mining, net hash 2.41 GH/s, v16, 13(out)+3(in) connections, uptime 2d 9h 20m 5s`
`Height: 2054506/2054506 (100.0%) on testnet, not mining, net hash 3.39 kH/s, v16, 10(out)+32(in) connections, uptime 2d 9h 20m 7s`
`Height: 1165891/1165891 (100.0%) on stagenet, not mining, net hash 1.93 kH/s, v16, 8(out)+0(in) connections, uptime 5d 9h 5m 17s`

## DeeDeeRanged | 2022-08-28T13:20:40+00:00
Probably won't help but I am running a full node on Debian testing (bookworm) cpu AMD 200ge with the monero-gui and it runs the following command:
monero-gui-v0.18.1.0/monerod --detach --zmq-pub tcp://127.0.0.1:18083 --disable-dns-checkpoints --check-updates disabled --non-interactive --max-concurrency 2

I constantly have 12(out) and over 110(in)
Log:
[28-08-2022 15:09] 2022-08-28 13:09:19.765 I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 2699503/2699503 (100.0%) on mainnet, not mining, net hash 2.69 GH/s, v16, 12(out)+122(in) connections, uptime 1d 2h 16m 16s

I guess monero-gui (monerod) has 12(out) set as standard.

I have all the port forwarding set as required in my modem/router. Changing of the internet ip addres should have no influence here as the ports on the internet are set 0.0.0.0 so any internet ip address is allowed.

NB
Now running monerod.service and have the following in my monero.conf:
# Bandwidth
out-peers=64
in-peers=1024
limit-rate-up=62500
limit-rate-down=125000

monerod status --log-level 2
2022-09-08 19:38:29.123	D SSL handshake success
Height: 2707604/2707604 (100.0%) on mainnet, not mining, net hash 2.57 GH/s, v16, 64(out)+107(in) connections, uptime 0d 7h 47m 36s

UPDATE:
Height: 2711893/2711893 (100.0%) on mainnet, not mining, net hash 2.88 GH/s, v16, 64(out)+67(in) connections, uptime 1d 8h 11m 32s




## jhb9 | 2022-09-14T13:36:52+00:00
Just wanted to leave a note that I'm seeing very similar behavior, 1 or 0 connections.  It looks like ports are being opened (I observe them by looking at my computers TCP connections) but just disappearing right away.  The fact that connections are being made means the "no incoming connections" warning doesn't pop up so I don't know how long it's been like this.

## t5awd | 2022-09-20T13:50:44+00:00
No change with the update to v0.18.1.1. I see other people on Reddit reporting this issue too: https://old.reddit.com/r/Monero/comments/xj0ffl/monero_v01811_flourine_fermi_released/ip6jw8r/

## selsta | 2022-09-20T13:52:40+00:00
v0.18.1.1 had no changes in this regard so that was expected.

## Meister500 | 2022-11-04T10:49:35+00:00
Hey,
I have the same problem.
I tried it on three computers: 2 Workstation and 1 Notebook.
With Windows 10 and Windows 11 and OpenSuse.
I tried it on two locations, there were 40 Kilometer between.
I live in the south east of Germany.
The Port 18080 TCP is forwarding to the right Computer.
Windows firewall is completly down- And I tried the expose function of the fritz.box router...
I tried it on version 0.18.1.2 CLI and GUI. Downloaded by "getmonero.org"

I have always:
12 Peers Out
1 Peer IN (sometimes for a few seconds 1-3) but it always fall back to 1. 

And the IN-Peer is always the same "91.198.115".73
If I ban the IP, the next up counting nummer appears immediatley.
Ban 91.198.115.73
Appears: 91.198.115.**74**
Ban 91.198.115.**74**
Appears: 91.198.115.**75**
and so on and so on...
the last nummers are always counting up.

**it is a big Probme**, I'm not able to suppport the Monero Net, although I have 2 Computers and two private house internet accounts.

At this moment I belive strong that is a try to hack Monero, and not a bug or only a spam, because who has the money for so many IP Internet Accounts and the interests, please show me the opposite.

Let me know what I should try.










## selsta | 2022-11-04T12:14:34+00:00
There have always been sybil nodes, but so far it does not make sense why an incoming sybil node would block other incoming peers.

@Meister500 you can try to ban the whole IP range by entering for example `ban 91.198.115.73/24`. Repeat this every time you only have a single incoming connection. I'm curious if at some point you get more incoming connections.

## Meister500 | 2022-11-04T15:23:16+00:00
Ok, I tested it. And now I have bad news!
I banned the hole IP adresse 91.198.115....(1-255)
This IP Adresse disappears, and I have 0 Incoming peers. After restart of the monerd and a restart of the internet router, for a new own ip adress, I stand at the same point as befor, but this time the nummer has changed!

From 91.198.115....

To 162.218.65.... (1-255)

Here I do the same as befor:
I banned 162.218.65.**20**
It appears 162.218.65.**21**
I banned it, 
and 162.218.65.**22** appers 
**23** banned
**24** banned
and so on... the same game as befor.

@selsta you sad it make no sense that an(1) incoming sybil node do this, 
and at this point I think you have right, 
but is it one(1) incoming peer? 
I have found 91.198.115.(1-255) and 162.218.65.(1-255) there are two times 255 (510) incomings. How expensive is it to rent 510 IP's? And how long "they" need to wrote the software behind? I banned one - a new one appers, and so on.

Please let me know what you thinking.





## Meister500 | 2022-11-04T21:18:31+00:00
Update:
It is the same with incomings for the IP Range:
 209.222.252.**196** 
the new one: 209.222.252.**179**
and so on.
All the Incomings are controlled:
Beacuse, each IP range /Peerline,
91.198.115.*
162.218.65.*
209.222.252.*
let only maximum one peer connect to me, although there are 255 possible peers in the line.
That is a big deal, there are (3x 255 =) 765 Peers that a controlled, wich I found.
This three IP ranges are the only Incomings that I had.




## selsta | 2022-11-04T22:18:59+00:00
I'm not convinced that these sybil nodes are even related to the issue you are seeing. Some other user in this issue sent me their IP and I was able to connect to it without any issues. It seems to me other nodes don't even attempt to connect for some unknown reason.

> That is a big deal, there are (3x 255 =) 765 Peers that a controlled, wich I found.

From what I can tell it doesn't necessarily mean that they own all 256 IPs, e.g. they might own 91.198.115.25 - 91.198.115.50.

## llacqie | 2022-11-06T19:51:14+00:00
I have the same problem.

I analyzed traffic using wireshark. And I've seen the following behavior: my node (node A) connects to node B(port n to 18080), they communicate. And at some point node B decides to connect to node A(port n to our 18080), a handshake occurs, but instead of communicating over this connection node B immediately closes it.

And all connections, except those that are started manually by me, behave like this.

## endorxmr | 2022-11-06T20:56:21+00:00
> From what I can tell it doesn't necessarily mean that they own all 256 IPs, e.g. they might own 91.198.115.25 - 91.198.115.50.

From a partial scan of the network (~200 nodes), I can say that almost every single ip in the three /24 ranges listed above shows up at least once in the peerlists I received, and many of them show up several times (even 10+ for most of the 162.218.65.x range). By "multiple times", I mean that each ip shows up with multiple different p2p-port numbers (eg. 18080, 18280, 18380, 18480, 18580, 18082, 18083, 18084, 18085, etc.), sometimes with pruning (always the same pruning seed), sometimes with rpc enabled.

## thilool | 2022-11-09T15:07:02+00:00
> Update: It is the same with incomings for the IP Range: 209.222.252.**196** the new one: 209.222.252.**179** and so on. All the Incomings are controlled: Beacuse, each IP range /Peerline, 91.198.115.* 162.218.65.* 209.222.252.* let only maximum one peer connect to me, although there are 255 possible peers in the line. That is a big deal, there are (3x 255 =) 765 Peers that a controlled, wich I found. This three IP ranges are the only Incomings that I had.

Hello to the community,

I am running a full node v.0.18.1.2 under ubuntu 20.04
I can confirm the IP addresses from @Meister500 I have exactly the same issue.

Interestingly the issue started on my end with the update after the hard-fork in August. Before that I had a normal range of 60-100 incomming connections.
I am also located in the south of Germany.

If any logs from my side can be of help please let me know.
I hope this can be resolved very soon so my tiny server can support the network with its full potential.

Greetings!

## selsta | 2022-11-09T15:10:05+00:00
@thilool Someone in our team was able to reproduce the issue and we are working on it.

## j-berman | 2022-11-10T22:18:40+00:00
I've spent a solid chunk of time investigating this (and am still investigating). Sharing my thoughts so far.

The p2p connection protocol flows something like this:

1. I start up my node and my node sees that Alice's node is in my white list.
2. My node tries to make an OUT connection to Alice's node. The connection succeeds.
3. Alice's node then tries to "back ping" my node to see if I would make a healthy OUT connection for Alice's node in the future.
4. If Alice's back ping to my node succeeds, Alice's node will add my node to the very top of her white list ([source](https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/src/p2p/net_node.inl#L2595)).
5. At this point, since my node is at the top of Alice's white list, Alice's chances of establishing a long-lived connection with me are increased. Further, Alice will include me in her white list that her node shares with her connections, which broadcasts my node's IP across the network signaling I'm a healthy node others can try to connect to.

Thus, the back ping seems to be a crucial component of the protocol toward getting incoming connections.

There seems to be a racy bug in the back ping causing consistent failures on my machines. When I run 2 nodes and connect them to each other, I consistently observe the following behavior:

1. Node A initiates OUT connection to Node B.
2. Node B accepts the connection and the nodes establish a long-lived connection A -> B.
3. Node B initiates OUT connection to back ping Node A.
4. Node A accepts the connection.

Then, the following happens:
- Node A gets an End of File error inside `on_read` (when it should be reading the ping). An EOF error indicates the peer has closed the connection.
- Node B gets a truthy but uninitialized `ec` error inside `on_read` and terminates the connection.

It looks like Node B is the one closing the connection first (if I set a breakpoint inside Node B's error handling, Node A will later timeout its connection to Node B). It seems odd that Node B's connection immediately ends up inside `on_read` with an uninitialized `ec` -- that seems like the sign of a racy bug. Generally, this area of the code is the most suspicious to me as the source of this issue. Continuing to investigate.

## j-berman | 2022-11-10T22:34:04+00:00
Somewhat related, I also think it would be beneficial to do "white list housekeeping" in addition to the ["gray list housekeeping"](https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/src/p2p/net_node.inl#L2892) already done. Nodes at the "bottom" of my white list can get stuck there it seems, since nodes will bias heavily toward selecting from the front of the white list (1: nodes select a peer from the [first 20 most recently seen peers in the white list](https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/src/p2p/net_node.inl#L1597), 2: the selection algo biases toward [the most recently seen/lowest index nodes](https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/src/p2p/net_node.inl#L1655-L1656))

## j-berman | 2022-11-12T01:41:27+00:00
I've found what's causing back pings to fail, which I still believe is the most likely cause of this issue.

The back ping uses `connect_async`'s default for `ssl_support` [here](https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/src/p2p/net_node.inl#L2367) (the default is to [autodetect SSL support](https://github.com/monero-project/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/contrib/epee/include/net/abstract_tcp_server2.h#L382)). The back ping is the only spot in the code that uses `connect_aysnc`, and AFAICT is the only spot in the code that sets `ssl_support` to autodetect.

The connection rewrite modified how outgoing SSL autodetect connections are handled downstream. Prior to the connection rewrite, ALL outgoing connections followed the else here to set up the reader the same way it would handle a non-SSL connection:

https://github.com/monero-project/monero/blob/87ec36cacfd408cfe7405f804b35e29aefd209b4/contrib/epee/include/net/abstract_tcp_server2.inl#L203-L214

After the connection rewrite, the code now sets up the reader the same as it would an SSL connection if `ssl_support` is set to autodetect here:

https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/contrib/epee/include/net/abstract_tcp_server2.inl#L906-L908

https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/contrib/epee/include/net/abstract_tcp_server2.inl#L425-L444

If I make a simple change to call `connect_async` with `ssl_support` explicitly disabled, I start seeing `PING SUCCESS` on my node since my node successfully back pings any incoming connections that come in (@selsta has confirmed this as well).

I believe the reason reverting the connection patch doesn't help anyone above is because the OUTGOING connection would need to revert, in order for the OUTGOING node to successfully back ping our node. Unfortunately this would mean that the only way to fix this issue is for the nodes we connect to to update as well.

Will submit a PR soon.

## hinto-janai | 2022-11-20T14:09:21+00:00
One of my nodes had this issue and it seems to have fixed itself. The only 1-3 incoming connections were from the IP ranges mentioned above but all of a sudden it's getting a normal amount of in peers. Weird thing is that the node hasn't been touched at all, I didn't delete p2pstate.bin either.

>Nodes at the "bottom" of my white list can get stuck there it seems

@j-berman I think this is what happened to my node.

## selsta | 2022-11-20T14:11:15+00:00
This issue won't be fixed until we put out a new release.

## hinto-janai | 2022-11-20T14:19:24+00:00
@selsta For some reason one of my nodes did fix itself without interaction though.

Although the other nodes I have that have this issue still don't have incoming connections, even after importing the known good p2pstate.bin.

## selsta | 2022-11-20T14:20:59+00:00
@hinto-janaiyo The issue is with other nodes, not your own, that's why importing p2pstate doesn't work.

## thilool | 2022-12-02T08:45:24+00:00
Was there any update happening in the background?
Since a power outage on Wednesday I get a normal number of incomming peers on my node, around 100.

## selsta | 2022-12-02T15:11:56+00:00
We didn't update anything yet but we know what causes the issue and have a bug fix ready.

## Meister500 | 2022-12-21T10:21:41+00:00
> We didn't update anything yet but we know what causes the issue and have a bug fix ready.

Perfect! 
When do you guess the update will come?

## selsta | 2022-12-21T13:51:32+00:00
v0.18.2.0 in January.

## EvertonZanotelli | 2023-01-13T08:33:34+00:00
The issue is fixed for me

## selsta | 2023-01-13T15:13:53+00:00
I'm currently testing https://github.com/monero-project/monero/pull/8640 on mainnet, so for some people the issue should fix itself now, if a node still has no incoming connections it will be fixed once v0.18.2.0 is released.

## llacqie | 2023-01-13T15:34:42+00:00
> I'm currently testing #8640 on mainnet, so for some people the issue should fix itself now, if a node still has no incoming connections it will be fixed once v0.18.2.0 is released.

I also launched a node with this fix a week ago, I have incoming peers and hope I will help someone fix this issue too.

## selsta | 2023-02-28T17:42:22+00:00
Resolved in v0.18.2.0 and #8640, release should be out today.

# Action History
- Created by: li5lo | 2022-08-20T00:09:19+00:00
- Closed at: 2023-02-28T17:42:22+00:00
