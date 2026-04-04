---
title: monerod started mining "on its own"
source_url: https://github.com/monero-project/monero/issues/5523
author: patosullivan
assignees: []
labels:
- invalid
created_at: '2019-05-07T14:06:23+00:00'
updated_at: '2024-06-07T12:14:06+00:00'
type: issue
status: closed
closed_at: '2019-09-02T11:57:27+00:00'
---

# Original Description
I have a VPS that I am running monerod on via docker.
This is the docker image I'm using: https://hub.docker.com/r/xmrto/monero.

I ran it with these flags/environment variables:
` docker run --rm -d -p 18081:18081 -p 18089:18089 -p 18080:18080 -v /mnt/monero/monero:/monero -e RPC_BIND_PORT=18081 -e P2P_BIND_PORT=18080 -e RPC_BIND_IP=0.0.0.0
-e LOG_LEVEL=0 --name=monero_node xmrto/monero --data-dir=/monero --non-interactive --rpc-restricted-bind-port=18089`

UFW is setup and enabled on the machine, 18081 is blocked, 18080 and 18089 are both allowed.

Here are my UFW rules:

>Status: active
>To                         Action      From
>--                         ------      ----
>22                         ALLOW       Anywhere
>18080                      ALLOW       Anywhere
>8333                       ALLOW       Anywhere
>syncthing                  ALLOW       Anywhere
>18089                      ALLOW       Anywhere
>1194/udp                   ALLOW       Anywhere
>22 (v6)                    ALLOW       Anywhere (v6)
>8333 (v6)                  ALLOW       Anywhere (v6)
>syncthing (v6)             ALLOW       Anywhere (v6)
>18089 (v6)                 ALLOW       Anywhere (v6)
>1194/udp (v6)              ALLOW       Anywhere (v6)

You can see I'm also running a bitcoin node, syncthing, a vnc server and I'm allowing SSH (via pubkey authentication only).

It ran fine for a few days, but yesterday it apparently started mining "out of nowhere".  I only found out about it by checking in on it this morning and noticing the high CPU usage.

The mining started after an exception was thrown and a big stacktrace printed in the logs.

Basically I want to figure out if I missed something here and I accidentally let someone do this, or if it occurred through some kind of exploit.

I've attached a copy of the logs from the time the node was last started up until the mining began:
[moneroextract.log](https://github.com/monero-project/monero/files/3152992/moneroextract.log)

If you need any more information or if I should format any of this differently, let me know.

# Discussion History
## moneromooo-monero | 2019-05-07T14:24:30+00:00
The exception has nothing to do with it.
You can use these logs to see where this is coming from if it does it again: 0,net\*:INFO
You're certain you didn't enable it yourself in a wallet, right ?
Type "set" in your wallet and check if you have a setup-background-mining, and what its value is if you do.

## patosullivan | 2019-05-07T14:37:32+00:00
Absolutely certain that I didn't enable it myself, I never used monero-wallet-cli on this machine.

## patosullivan | 2019-05-07T14:50:45+00:00
I've restarted the daemon. It starts and runs just fine and hasn't started mining yet.

## moneromooo-monero | 2019-05-07T15:13:56+00:00
Also, what version of daemon and wallet are you using ?

## patosullivan | 2019-05-07T15:56:00+00:00
Boron Butterfly.

--
Patrick

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Tuesday, May 7, 2019 10:14 AM, moneromooo-monero <notifications@github.com> wrote:

> Also, what version of daemon and wallet are you using ?
> 

> —
> 

> You are receiving this because you authored the thread.
> 

> Reply to this email directly, view it on GitHub, or mute the thread.[https://github.com/notifications/beacon/AAJKDZT5VB3TKQETQLIIE6TPUGMEXA5CNFSM4HLJGDG2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODU3K6KQ.gif]

## moneromooo-monero | 2019-05-07T16:34:25+00:00
That's not super specific. There are hundreds, if not thousands, of commits with that name.


## patosullivan | 2019-05-07T20:20:49+00:00
Sorry, it's v0.14.0.2-release.

The same thing happened after the node ran for almost two hours today, except without the errors/stacktraces.

I can't see how this could be happening given the flags I use when running monerod and the UFW rules enforced.

## moneromooo-monero | 2019-05-07T20:44:30+00:00
Did you start a wallet recently ?

## patosullivan | 2019-05-07T21:10:33+00:00
Have never started a wallet on that machine. I've connected to it remotely via monerujo, but that's it.

## moneromooo-monero | 2019-05-07T21:51:12+00:00
Did the network logs show "calling start_mining" or so ?

## moneromooo-monero | 2019-05-07T22:07:54+00:00
Also, run mining_status and check whether the address it's mining to is one of yours or not.

## patosullivan | 2019-05-07T23:51:12+00:00
I'll make a wallet and wait until the thing starts mining again and try to issue some commands. It doesn't look like mining_status is an available command with monero-wallet-cli. I don't see it listed as a command that can be issued to monerod either. How should I issue that command?

## moneromooo-monero | 2019-05-08T00:13:25+00:00
It's a new monerod command. With your version, you'll have to call the RPC:

curl -v -k -X POST http://127.0.0.1:18081/mining_status -d '{}' -H 'Content-Type: application/json'

## patosullivan | 2019-05-08T12:26:29+00:00
It started mining again, overnight:

```
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 18081 (#0)
> POST /mining_status HTTP/1.1
> Host: 127.0.0.1:18081
> User-Agent: curl/7.64.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 2
>
* upload completely sent off: 2 out of 2 bytes
< HTTP/1.1 200 Ok
< Server: Epee-based
< Content-Length: 233
< Content-Type: application/json
< Last-Modified: Wed, 08 May 2019 12:20:21 GMT
< Accept-Ranges: bytes
<
{
  "active": true,
  "address": "493huwhiqjBhP9dXgudsmbX6gHTq7TQ1PPCapanaNEKdj4bnH4wJFh6T3RBWBPM4vCREvLd5NYYhcDnYzqSMEAHDUb3Lqos",
  "is_background_mining_enabled": true,
  "speed": 4,
  "status": "OK",
  "threads_count": 8
* Connection #0 to host 127.0.0.1 left intact
}* Closing connection 0
```

That address does not belong to me. The main address for the test wallet I created yesterday is `43LG3xcVgTDAU6BLc4BhWXgMoXBQcDV8EhP4SFCarHhf9CqRFNLocGcDRtVU9n9gmqhetQqN1sF2jjgY6MfXfyQDTKE7Rfs`.

I can provide access to the server to the monero devs if you want/need to look at this yourself.

## moneromooo-monero | 2019-05-08T13:32:25+00:00
Did the logs show "calling xxx" ? If so, check the IP address. 

## patosullivan | 2019-05-08T13:54:56+00:00
"calling" doesn't appear anywhere in the bitmonero.log file. Should I run the node with a different log-level?

--
Patrick

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Wednesday, May 8, 2019 8:32 AM, moneromooo-monero <notifications@github.com> wrote:

> Did the logs show "calling xxx" ? If so, check the IP address.
> 

> —
> 

> You are receiving this because you authored the thread.
> 

> Reply to this email directly, view it on GitHub, or mute the thread.[https://github.com/notifications/beacon/AAJKDZUI4CC37ES4TEOEZJLPULJABA5CNFSM4HLJGDG2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODU6DY4A.gif]

## moneromooo-monero | 2019-05-12T10:19:05+00:00
Might be "Calling". Those logs are in the net.http category so should show up with the settings above.
If not, then:
- stop monerod
- add this line: tools::log_stack_trace("mining starting");
- to: src/cryptonote_basic/miner.cpp, as the first line of miner::start
- add #include "common/stack_trace.h" at the start of the same file
- build monerod
- start monerod again
- wait
- post the stack trace in the logs after mining starts again

You will have to ensure libunwind-dev is installed so monerod prints stack traces.

## ndorf | 2019-05-17T07:57:43+00:00
Did you verify that port 18081 is actually unreachable from outside?

## patosullivan | 2019-05-17T17:08:52+00:00
Yep, see my UFW rules above.

@moneromooo-monero sorry I haven't gotten around to checking on this yet, have been busy.

## ndorf | 2019-05-18T00:22:07+00:00
I saw the UFW rules, but it wasn't clear if, for instance, the default policy is to allow or block. Based on the evidence, it sure looks like an unknown third party has access to your restricted RPC port. So, either those firewall rules are not working, or someone has access to the system.

Rather than relying on knowledge of your firewall configuration, it seems easier to actually try to connect from a remote system (`nc -v <IP> 18081`) and go from there.

Also, if I were you I'd check to make sure the port isn't accessible from other Docker containers on the same host. E.g., `docker run --rm -it alpine nc -v 172.17.0.1 18081`, assuming the default Docker IP address (can be verified with `ip a s docker0` on the host).

## moneromooo-monero | 2019-06-13T14:22:40+00:00
ping

## moneromooo-monero | 2019-06-29T12:07:15+00:00
ping

## moneromooo-monero | 2019-08-27T15:13:27+00:00
ping

## moneromooo-monero | 2019-09-02T11:21:51+00:00
Since no more replies for quite a while, I'll close this. Reopen if you can get the logs.

+invalid

## CocolinoFan | 2024-06-07T12:04:49+00:00
Same behavior on my side. All of a sudden I noticed CPU at 100% from monerod. Looking at the monerod, the terminal output was:
```
2024-06-07 11:53:57.075	E   failed to find tx meta: <b8b9804a6b5c7c2f211d1b1b05d88fdcc4557be1a524a1440a8b8bd76ee1dcd9> (will only print once)
2024-06-07 11:54:03.326	I Miner thread was started [0]
2024-06-07 11:55:16.612	I Miner thread stopped [0]
2024-06-07 11:56:25.221	I Miner thread was started [0]
2024-06-07 11:56:25.222	I Miner thread was started [5]
2024-06-07 11:56:25.222	I Miner thread was started [2]
2024-06-07 11:56:25.222	I Miner thread was started [3]
2024-06-07 11:56:25.222	I Miner thread was started [4]
2024-06-07 11:56:25.222	I Miner thread was started [1]
2024-06-07 11:56:25.222	I Miner thread was started [6]
2024-06-07 11:56:25.222	I Miner thread was started [7]
2024-06-07 11:56:25.222	I Miner thread was started [8]
2024-06-07 11:56:25.222	I Miner thread was started [9]
2024-06-07 11:56:25.222	I Miner thread was started [10]
2024-06-07 11:56:25.223	I Miner thread was started [11]
2024-06-07 11:56:25.223	I Miner thread was started [12]
2024-06-07 11:56:25.223	I Miner thread was started [13]
2024-06-07 11:56:25.223	I Miner thread was started [14]
2024-06-07 11:56:25.223	I Miner thread was started [15]
2024-06-07 11:56:25.223	I Miner thread was started [16]
2024-06-07 11:56:25.223	I Miner thread was started [17]
2024-06-07 11:56:25.223	I Miner thread was started [18]
2024-06-07 11:56:25.223	I Miner thread was started [19]
2024-06-07 11:56:25.223	I Miner thread was started [20]
2024-06-07 11:56:25.223	I Miner thread was started [21]
2024-06-07 11:56:25.223	I Miner thread was started [22]
2024-06-07 11:56:25.223	I Miner thread was started [23]
2024-06-07 11:56:25.227	I Miner thread was started [24]
2024-06-07 11:56:25.230	I Miner thread was started [25]
2024-06-07 11:56:25.231	I Miner thread was started [26]
2024-06-07 11:56:25.237	I Miner thread was started [27]
2024-06-07 11:56:25.244	I Miner thread was started [28]
2024-06-07 11:56:25.247	I Miner thread was started [29]
2024-06-07 11:56:25.247	I Miner thread was started [30]
2024-06-07 11:56:25.250	I Miner thread was started [31]
```
I have p2pool, xmrig and bitcoind running as well.


EDIT: I am running `monerod` for years, this never happened before. 
Just now I shutdown monerod and re-opened it and it started mining again :O Here is the console output:
```
monerod 
2024-06-07 12:06:07.825	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2024-06-07 12:06:07.825	I Initializing cryptonote protocol...
2024-06-07 12:06:07.825	I Cryptonote protocol initialized OK
2024-06-07 12:06:07.825	I Initializing core...
2024-06-07 12:06:07.825	I Loading blockchain from folder /home/cocolino/.bitmonero/lmdb ...
2024-06-07 12:06:08.977	I Loading checkpoints
2024-06-07 12:06:08.977	I Core initialized OK
2024-06-07 12:06:08.977	I Initializing p2p server...
2024-06-07 12:06:10.058	I p2p server initialized OK
2024-06-07 12:06:10.058	I Initializing core RPC server...
2024-06-07 12:06:10.067	I Binding on 127.0.0.1 (IPv4):18081
2024-06-07 12:06:10.067	I core RPC server initialized OK on port: 18081
2024-06-07 12:06:10.068	I Starting core RPC server...
2024-06-07 12:06:10.068	I core RPC server started ok
2024-06-07 12:06:10.069	I Starting p2p net loop...
2024-06-07 12:06:11.070	I 
2024-06-07 12:06:11.070	I **********************************************************************
2024-06-07 12:06:11.070	I The daemon will start synchronizing with the network. This may take a long time to complete.
2024-06-07 12:06:11.070	I 
2024-06-07 12:06:11.070	I You can set the level of process detailization through "set_log <level|categories>" command,
2024-06-07 12:06:11.070	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2024-06-07 12:06:11.070	I 
2024-06-07 12:06:11.070	I Use the "help" command to see the list of available commands.
2024-06-07 12:06:11.070	I Use "help <command>" to see a command's documentation.
2024-06-07 12:06:11.070	I **********************************************************************
2024-06-07 12:06:11.245	I [79.242.79.236:18080 OUT] Sync data returned a new top block candidate: 3165968 -> 3165969 [Your node is 1 blocks (2.0 minutes) behind] 
2024-06-07 12:06:11.245	I SYNCHRONIZATION started
2024-06-07 12:06:11.386	I Synced 3165969/3165969
2024-06-07 12:06:11.386	I 
2024-06-07 12:06:11.386	I **********************************************************************
2024-06-07 12:06:11.386	I You are now synchronized with the network. You may now start monero-wallet-cli.
2024-06-07 12:06:11.386	I 
2024-06-07 12:06:11.386	I Use the "help" command to see the list of available commands.
2024-06-07 12:06:11.386	I **********************************************************************
2024-06-07 12:07:56.360	W WARNING: no two valid DNS TXT records were received
2024-06-07 12:09:00.511	E   failed to find tx meta: <6b7853bdb1133196fa5f655e7d922a3e285fa0df1018855931151a91b75fb601> (will only print once)
2024-06-07 12:09:08.453	I Miner thread was started [0]
2024-06-07 12:09:08.454	I Miner thread was started [16]
2024-06-07 12:09:08.454	I Miner thread was started [4]
2024-06-07 12:09:08.456	I Miner thread was started [7]
2024-06-07 12:09:08.456	I Miner thread was started [14]
2024-06-07 12:09:08.456	I Miner thread was started [11]
2024-06-07 12:09:08.456	I Miner thread was started [6]
2024-06-07 12:09:08.457	I Miner thread was started [2]
2024-06-07 12:09:08.457	I Miner thread was started [10]
2024-06-07 12:09:08.457	I Miner thread was started [1]
2024-06-07 12:09:08.460	I Miner thread was started [17]
2024-06-07 12:09:08.468	I Miner thread was started [13]
2024-06-07 12:09:08.468	I Miner thread was started [5]
2024-06-07 12:09:08.469	I Miner thread was started [12]
2024-06-07 12:09:08.469	I Miner thread was started [8]
2024-06-07 12:09:08.469	I Miner thread was started [30]
2024-06-07 12:09:08.469	I Miner thread was started [15]
2024-06-07 12:09:08.470	I Miner thread was started [9]
2024-06-07 12:09:08.470	I Miner thread was started [3]
2024-06-07 12:09:08.475	I Miner thread was started [22]
2024-06-07 12:09:08.478	I Miner thread was started [18]
2024-06-07 12:09:08.486	I Miner thread was started [20]
2024-06-07 12:09:08.486	I Miner thread was started [19]
2024-06-07 12:09:08.490	I Miner thread was started [21]
2024-06-07 12:09:08.490	I Miner thread was started [24]
2024-06-07 12:09:08.491	I Miner thread was started [27]
2024-06-07 12:09:08.494	I Miner thread was started [25]
2024-06-07 12:09:08.499	I Miner thread was started [26]
2024-06-07 12:09:08.507	I Miner thread was started [28]
2024-06-07 12:09:08.514	I Miner thread was started [23]
2024-06-07 12:09:08.519	I Miner thread was started [29]
2024-06-07 12:09:08.522	I Miner thread was started [31]
2024-06-07 12:09:11.424	W WARNING: no two valid DNS TXT records were received
```

# Action History
- Created by: patosullivan | 2019-05-07T14:06:23+00:00
- Closed at: 2019-09-02T11:57:27+00:00
