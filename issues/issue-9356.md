---
title: monerod started mining on its own
source_url: https://github.com/monero-project/monero/issues/9356
author: CocolinoFan
assignees: []
labels: []
created_at: '2024-06-07T12:25:49+00:00'
updated_at: '2024-06-22T16:24:45+00:00'
type: issue
status: closed
closed_at: '2024-06-13T13:55:07+00:00'
---

# Original Description
Similar to [issue 5523](https://github.com/monero-project/monero/issues/5523).
All of a sudden I notice my computer's utilization is at 100%. I check what is using the resources and it was monerod.
Looking at the console output I see:
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
I shutdown monerod and start it again. And monerod started mining again. I am running monerod for years this never happened before. 
Console output from the second monerod run:
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

No additional relevant software was installed and no monerod settings have been changed.
If relevant I am also running, on the same computer: xmrig, p2pool and bitcoind.

# Discussion History
## selsta | 2024-06-07T12:48:38+00:00
You are still using v0.18.2.2 which is a year old, so it's not possible that monerod itself changed. Can you try to start monerod with restricted rpc to see if it's some external program that does the RPC call to start mining?

## CocolinoFan | 2024-06-07T13:33:51+00:00
When trying to reproduce the bug, monerod was acting odd (not shutting down with Ctrl+C, exit command taking minutes); p2pool was not starting either, complaining that port 3333 was already in use (by monerod somehow I think). But, it did not start mining on its own again (at least in the two minutes I kept it open).
After a reboot, everything seems normal. I will report back if it happens again, but looks unlikely to be a hacking situation. Thank you for the idea of running monerod with RPC disabled.
In hindsight, I should probably not have opened a new issue.

v0.18.3.3 is out 👀

## selsta | 2024-06-07T13:36:03+00:00
If open RPC causes the mining to start automatically there is a risk that some program or malware is sending the RPC call to start mining. You might be able to increase the log level and see to which address is being mined, though not sure if that's getting printed at a higher log level. You'd have to try.

## CocolinoFan | 2024-06-10T14:30:48+00:00
Well, I've installed the latest version of `monerod` from my distribution's repository and re-downloaded the blockchain. After one day `monerod` starts mining on it's own again.
```
2024-06-10 03:22:24.066	I difficulty:	294057258027
2024-06-10 03:50:26.067	W WARNING: no two valid DNS TXT records were received
2024-06-10 05:48:27.015	W WARNING: no two valid DNS TXT records were received
2024-06-10 07:46:22.444	W WARNING: no two valid DNS TXT records were received
2024-06-10 09:44:18.377	W WARNING: no two valid DNS TXT records were received
2024-06-10 10:09:34.853	W WARNING: no two valid DNS TXT records were received
2024-06-10 11:42:17.076	W WARNING: no two valid DNS TXT records were received
2024-06-10 13:40:20.742	W WARNING: no two valid DNS TXT records were received
2024-06-10 14:09:44.823	I Miner thread was started [0]
2024-06-10 14:09:44.823	I Miner thread was started [1]
2024-06-10 14:09:44.823	I Miner thread was started [8]
2024-06-10 14:09:44.823	I Miner thread was started [2]
2024-06-10 14:09:44.823	I Miner thread was started [3]
2024-06-10 14:09:44.823	I Miner thread was started [11]
2024-06-10 14:09:44.823	I Miner thread was started [12]
2024-06-10 14:09:44.823	I Miner thread was started [13]
2024-06-10 14:09:44.823	I Miner thread was started [6]
2024-06-10 14:09:44.823	I Miner thread was started [7]
2024-06-10 14:09:44.824	I Miner thread was started [5]
2024-06-10 14:09:44.824	I Miner thread was started [15]
2024-06-10 14:09:44.824	I Miner thread was started [4]
2024-06-10 14:09:44.824	I Miner thread was started [14]
2024-06-10 14:09:44.824	I Miner thread was started [10]
2024-06-10 14:09:44.824	I Miner thread was started [9]
```
I was ready this time. Typing `mining_status` gave me
```
Mining at 931 H/s with 16 threads
PoW algorithm: RandomX
Mining address: 47aMSgJnHgcTefoPB2fAkKWEZWZPRYjgci67aQnFRrNXKAtW7uveU2BSFuxzpky9ntWnKAkZemKgfLA3zzGdnvcT4xGNPJn
```
Needless to say I don't know that address, unless `monerod` is a wallet as well and somehow made a default wallet and started mining in it? But I don't see any commands related to wallet management.

I start `monerod` with the command `monerod --zmq-pub tcp://127.0.0.1:18083 --out-peers 32 --in-peers 64 --add-priority-node=p2pmd.xmrvsbeast.com:18080 --add-priority-node=nodes.hashvault.pro:18080 --disable-dns-checkpoints --enable-dns-blocklist` as instructed in the [p2pool documentation](https://p2pool.io/#help)

I have not stooped the node, so let me know if I should run any commands or look in any logs.

## selsta | 2024-06-10T14:33:10+00:00
There is no code in monerod that would create an address and mine to it, I assume some software on your computer is sending a RPC call to start mining.

## CocolinoFan | 2024-06-10T14:35:56+00:00
That is very alarming. How would I check this? I have Gentoo Linux 6.9.3

## moneromooo-monero | 2024-06-10T14:50:29+00:00
If you set log level to, say... 2, you should have all you need to check where the request to mine comes from. So:

> set_log 2
> stop_mining

Then wait for mining to start again. After it does, check logs for "start_mining". You should get a line with "calling /start_mining" in it.
A bit earlier in that line, you will see the IP and port the request is coming from.

If it is 127.0.0.1, then it is a process on your machine. You can run:

> netstat -anpt

to see what's running with network connections. If it's some malware, it might not be running network at the time though, but if something is connected to your daemon, you'll see it. Wallets are connected to it, and it might be a wallet if you setup background mining (you'd have been asked when creating a wallet). Exit wallet software to make sure it's not that. It'd be a known wallet address here though.

If the origin IP is not 127.0.0.x (or anything in the 127 range), then it's coming from the internet (unless a non routable IP from your local network, but I assume you'd know if you had set that up).

If you have some setup to masquerade/forward ports on your machine, it might be coming from outside and appear to be coming from the local machine. Again, you should know if you set something like that up too.


## CocolinoFan | 2024-06-10T15:05:56+00:00
Thank you, I understand. I set the log level 2 and I will output everything to a file.
Is gonna be a bit hard to know when exactly the mining starts (log level 2, text scrolling by fast) but I will see the CPU use.
I'm only using the official Monero GUI wallet .AppImage and my network setup is a typical home network, nothing exotic going on.

## moneromooo-monero | 2024-06-10T15:13:51+00:00
The log is also written to ~/.bitmonero/bitmonero.log so it can be grepped later. There is also a bit more info in it.

## CocolinoFan | 2024-06-10T18:27:53+00:00
Caught it!
[bitmonero.log.tar.gz](https://github.com/user-attachments/files/15777574/bitmonero.log.tar.gz)
[monerod_manual_log_2.txt.tar.gz](https://github.com/user-attachments/files/15777579/monerod_log_2.txt.tar.gz)
```
cat monerod_log_2.txt | grep -i3 "start_mining"
2024-06-10 18:12:08.035	D Percent used: 89.6441  Percent threshold: 90.0000
2024-06-10 18:12:08.038	D Queueing 3 transaction(s) for Dandelion++ fluffing
2024-06-10 18:12:08.109	D SSL detection buffer, 9 bytes: 80 79 83 84 32 47 115 116 97
2024-06-10 18:12:08.109	I HTTP [127.0.0.1] POST /start_mining
2024-06-10 18:12:08.109	I [127.0.0.1:46724 INC] calling /start_mining
2024-06-10 18:12:08.111	D Filling block template, median weight 300000, 28 txes in the pool
2024-06-10 18:12:08.111	D DB map size:     233496887296
2024-06-10 18:12:08.111	D Space used:      209316081664
--
2024-06-10 18:12:08.138	I Ignoring battery
2024-06-10 18:12:08.138	I Miner thread was started [1]
2024-06-10 18:12:08.138	I Miner thread was started [2]
2024-06-10 18:12:08.138	D /start_mining processed with 0/29/0ms
2024-06-10 18:12:08.138	I Miner thread was started [5]
2024-06-10 18:12:08.138	I Miner thread was started [6]
2024-06-10 18:12:08.138	I Miner thread was started [7]
```

`127.0.0.1:46724` 👀
Of course I can't find anything open with `netstat -anpt | grep 46724`

## moneromooo-monero | 2024-06-10T18:45:21+00:00
The caller will have closed the connection.
If you can compile your own, you could...

in src/rpc/core_rpc_server.cpp, look for:
> core_rpc_server::on_start_mining

One of the first lines in this function reads:

> CHECK_CORE_READY();

Right after it, insert this:

> sleep(1000);

Build again. Run again. Wait till monerod freezes. It will not go full CPU, it'll just wait 1000 seconds, giving you time to look at what's connected to it.



## moneromooo-monero | 2024-06-10T18:46:01+00:00
Might have to "#include <stdlib.h>" at the top of the file for sleep it it complains.

## CocolinoFan | 2024-06-13T13:55:07+00:00
I've successfully added the `sleep(1000);` and compiled the code (had to do it manually as the default `make release` did not work). Unfortunately the `sleep(1000)` did not work, it just started mining on its own again (it is possible I compiled wrong).
But I came up with another way of figuring out what program is starting the mining:

1) Start `monerod` and make it output to a file
```
monerod --zmq-pub tcp://127.0.0.1:18083 --out-peers 32 --in-peers 64 --add-priority-node=p2pmd.xmrvsbeast.com:18080 --add-priority-node=nodes.hashvault.pro:18080 --disable-dns-checkpoints --enable-dns-blocklist| tee ~/output.txt`
```
2) Set `set_log 2` in `monerod`
3) Run this script in the same directory where `output.txt` is (preferably as root)
```
#!/bin/bash

# Start tailing the output.txt file
tail -F output.txt | while read line; do
    # Check if the line contains the specific pattern
    if echo "$line" | grep -q '\[127.0.0.1:[0-9]* INC\] calling /start_mining'; then
        echo "Start to mine call detected!"
	echo "$line"
	echo ""

	# Extract the port number
        port_number=$(echo "$line" | grep -oP '(?<=127\.0\.0\.1:)\d+(?= INC)')
	echo "Port used: $port_number"
	echo ""

        if [ ! -z "$port_number" ]; then
            # Run netstat for the extracted port number
            netstat_output=$(netstat -anpt | grep "$port_number")
	   ps_number=$(echo "$netstat_output" | awk '{print $7}' | cut -d'/' -f1)
	   ps_output=$(ps auxww | grep "$ps_number")

            # Print the netstat output
            echo "netstat output:"
	   echo "$netstat_output"
	   echo ""

	   echo "ps output:"
	   echo "$ps_output"
        fi
    fi
done
```

When `monerod` starts mining it should output information about the program that started the mining. It worked for me for the official Monero GUI Wallet. With this setup, `monerod` crashes often tho, so is not ideal. 
I gave up on trying to find out what program was starting the mining for me. I'm doing a clean re-install of my OS.

In any case, this is expected behavior from `monerod` no bug or issue.

## ki9us | 2024-06-16T15:08:52+00:00
I have two machines running monerod in docker, one local and one VPS, and they both started doing this on the same date this issue was opened (June 7).  Neither have open RPCs.  One was running `monero:latest` and the other used an older version I built from the source.  

I just upped the log level and it didn't take more than a minute for the mining to start up again.  I found that the call was coming from "inside the house" too.  In this case 172.27.2.2 is the container's IP and 172.27.2.1 is the gateway to the host machine.  

```
$ docker logs monerod | grep -A4 -B4 start_mining
2024-06-16 13:27:14.726 D New server for RPC connections, SSL autodetection
2024-06-16 13:27:14.726 D Spawned connection #301 to 0.0.0.0 currently we have sockets count:2
2024-06-16 13:27:14.727 D  connection type 1 172.27.2.2:18081 <--> 172.27.2.1:57364 (via 172.27.2.1:57364)
2024-06-16 13:27:14.728 D SSL detection buffer, 9 bytes: 80 79 83 84 32 47 115 116 97
2024-06-16 13:27:14.728 I HTTP [172.27.2.1] POST /start_mining
2024-06-16 13:27:14.728 I [172.27.2.1:57364 INC] calling /start_mining
2024-06-16 13:27:14.731 D Filling block template, median weight 300000, 103 txes in the pool
2024-06-16 13:27:14.732 D DB map size:     90026735616
2024-06-16 13:27:14.732 D Space used:      79798337536
2024-06-16 13:27:14.732 D Space remaining: 10228398080
--
2024-06-16 13:27:14.806 I Ignoring battery
2024-06-16 13:27:14.806 I Miner thread was started [4]
2024-06-16 13:27:14.806 I Miner thread was started [5]
2024-06-16 13:27:14.806 I Miner thread was started [1]
2024-06-16 13:27:14.806 D /start_mining processed with 0/78/0ms
2024-06-16 13:27:14.806 D Destructing connection #300 to 0.0.0.0
2024-06-16 13:27:14.807 I Miner thread was started [8]
2024-06-16 13:27:14.808 I Miner thread was started [7]
2024-06-16 13:27:14.808 I Miner thread was started [6]
```

I actually have a third machine running monerod but not listed on monero.fail and it was not affected.  

I find it hard to believe that both my machines and @CocolinoFan's were compromised at the same time.  I'm a little suspect that someone figured out how to send RPC calls through port 18080.  But I suppose then the calls would have come from 172.27.2.2.  

I'd be interested to learn: 

- If anyone else is seeing this
- If @CocolinoFan's node is listed on monero.fail
- If the problem can be reproduced on the fresh OS install
- How to determine to what address is being mined

I have zero time to look into this further so for now I disabled RPC.  In about a week I could do some more debugging such as packet sniffing or trying to pinpoint the program making the call.  

## selsta | 2024-06-16T15:17:45+00:00
@ki9us `mining_status` shows you the address.

## ki9us | 2024-06-16T16:05:44+00:00
The request hung a few times but after several tries I got this: 

```json
{
  "active": true,
  "address": "47aMSgJnHgcTefoPB2fAkKWEZWZPRYjgci67aQnFRrNXKAtW7uveU2BSFuxzpky9ntWnKAkZemKgfLA3zzGdnvcT4xGNPJn",
  "bg_idle_threshold": 0,
  "bg_ignore_battery": false,
  "bg_min_idle_seconds": 0,
  "bg_target": 0,
  "block_reward": 601211460000,
  "block_target": 120,
  "difficulty": 326217709391,
  "difficulty_top64": 0,
  "is_background_mining_enabled": false,
  "pow_algorithm": "RandomX",
  "speed": 1069,
  "status": "OK",
  "threads_count": 16,
  "untrusted": false,
  "wide_difficulty": "0x4bf417374f"
}
```

I don't recognize it of course.  Different from [the address](https://github.com/monero-project/monero/issues/5523#issuecomment-490465646) in #5523.  

## selsta | 2024-06-16T16:09:39+00:00
From what I can tell @CocolinoFan's node was not on monero.fail, it wasn't even publicly accessible.

## selsta | 2024-06-16T16:10:52+00:00
@ki9us were the two docker nodes that started mining set to have a restricted RPC?

## ki9us | 2024-06-16T16:15:12+00:00
No, I will try one with `--restricted-rpc` and see if it comes back. 

## selsta | 2024-06-16T16:17:23+00:00
Having nodes publicly accessible without restricted RPC means anyone can send a start mining command. Though I don't fully know your setup and you said the RPC call came from your host machine, so not sure if that's what is going on here.

## ki9us | 2024-06-16T16:24:44+00:00
As with OP's setup, the port is firewalled off.  Checking from a remote VPS off the network: 

```sh
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-16 10:21 MDT
Nmap scan report for gf4.pw (64.57.57.12)
Host is up.
rDNS record for 64.57.57.12: 64.57.57.12-dyn.gojade.org

PORT      STATE    SERVICE
18081/tcp filtered unknown

Nmap done: 1 IP address (1 host up) scanned in 2.15 seconds
```

But the call came from the host machine, which does have access to the RPC. 

## CocolinoFan | 2024-06-16T16:47:48+00:00
Oh no! The two address are the same! [Mine](https://github.com/monero-project/monero/issues/9356#issuecomment-2158529096) and @[ki9us](https://github.com/monero-project/monero/issues/9356#issuecomment-2171754056)!


## ki9us | 2024-06-16T20:41:17+00:00
Ok, I found the leak and it _is_ my fault and it _is_ embarrassing.  

I set up this same unrestricted node as a web-compatible public rpc.  Port 18081 _was_ blocked but the rpc was accessible at https://xmr.gf4.pw/ through an nginx proxy.  

## selsta | 2024-06-17T09:41:11+00:00
@CocolinoFan can you rule out that you had some network misconfiguration that allowed external access to your node? To me it seems like this isn't malware but instead someone scanning the internet for publicly accessible nodes and sending RPC commands to start mining.

## CocolinoFan | 2024-06-17T10:15:58+00:00
That's the thing, I can't rule it out. When I first setup my node I was a beginner and I red somewhere you should forward port 18081 (i think, I am not 100% sure if it was forwarded or not).
I am doing some more testing now. With and without port 18081 accessible over the internet and, with and without the default starting parameters for p2pool. 
I will report back if anything interesting happens.

## selsta | 2024-06-17T10:18:34+00:00
Usually people recommend to port forward 18080 so that others can connect to your node. If you have 18081 accessible from the internet without restricted RPC it means anyone can start mining.

## ki9us | 2024-06-22T13:57:28+00:00
After I stopped the nginx proxy, the malicious mining commands stopped.  Port 18081 was always closed when the node was unrestricted.  So the threat actor was definitely accessing it through the web proxy

In my experience [and that of others](https://serverfault.com/a/1112336), nginx has a tendency to ignore the `default_server` directive.  So while I'm pretty sure that the node was only accessible at xmr.gf4.pw, it might have leaked out to [IP]:80 or [IP]:443.  

We were mining to the same address, therefore we had the same attacker, likely with the same TTPs.  That is, your system was probably not compromised because mine wasn't.  @CocolinoFan, did you have any web server or proxy running on your system?  If so, grep your config files for `18081`.  

## CocolinoFan | 2024-06-22T14:49:30+00:00
I did use to have an Apache website, but was moved to a different machine and network weeks *before* "the attack". 
I've reinstalled my OS, but recreated the `monerod` setup (port 18081 accessible over the internet, mining in the same address, with the same IP), but `monerod` *did not* start mining on its own again.

## selsta | 2024-06-22T15:46:49+00:00
@CocolinoFan if 18081 is accessible over the internet you have to make the node restricted, otherwise it's a matter of time until this happens again

## CocolinoFan | 2024-06-22T16:24:44+00:00
I understand. And if it does start mining on it's own again I will be very happy. I would know, without a shadow of a doubt, that it was just an exposed port 18081 and nothing more serious.

# Action History
- Created by: CocolinoFan | 2024-06-07T12:25:49+00:00
- Closed at: 2024-06-13T13:55:07+00:00
