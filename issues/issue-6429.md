---
title: Monero on Tails OS - Connection Errors Download Node
source_url: https://github.com/monero-project/monero/issues/6429
author: Mike34542
assignees: []
labels: []
created_at: '2020-04-05T10:17:55+00:00'
updated_at: '2022-02-19T04:41:19+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:41:19+00:00'
---

# Original Description
I'm trying to run the Monero wallet in Tails using the [Guide to creating a Monero GUI wallet in Tails][1].
I run the following iptables command from within the extracted Monero wallet:

    sudo iptables -I OUTPUT 2 -p tcp -d 127.0.0.1 -m tcp --dport 18081 -j ACCEPT
    [sudo] password for amnesia: 
But the command does't return anything. So I'm not sure if the port has been opened through Tails' firewall. I then run command.

    DNS_PUBLIC=tcp torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --rpc-bind-ip 127.0.0.1 --data-dir /media/amnesia/monero
The node begins to download. I get a few errors.

    2020-04-03 19:19:26.124	I Synced 46512/2068842 (2%, 2022330 left)
    1585941567 ERROR torsocks[16670]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
    2020-04-03 19:19:28.302	I Synced 46612/2068842 (2%, 2022230 left)

But the node continues to download regardless. It always reaches 18% before I get these errors.

    2020-04-03 19:52:46.631	I Synced 386060/2068853 (18%, 1682793 left)
    2020-04-03 17:48:47.173	W Failed to commit a transaction to the db: Input/output error
    2020-04-03 17:48:47.173	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: Input/output error
    1585936393 ERROR torsocks[13066]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
    1585936460 ERROR torsocks[13066]: Connection timed out (in socks5_recv_connect_reply() at socks5.c:547)
    1585936582 ERROR torsocks[13066]: Connection refused to Tor SOCKS (in socks5_recv_connect_reply() at socks5.c:543)
    1585936684 ERROR torsocks[13066]: Connection timed out (in socks5_recv_connect_reply() at socks5.c:547)
    1585937052 ERROR torsocks[13066]: General SOCKS server failure (in socks5_recv_connect_reply() at socks5.c:527)
    2020-04-03 18:18:57.415	W No incoming connections - check firewalls/routers allow port 18080
    1585938270 ERROR torsocks[13066]: Connection timed out (in socks5_recv_connect_reply() at socks5.c:547)

If the problem is indeed this.

    2020-04-03 18:18:57.415 W No incoming connections - check firewalls/routers allow port 18080

Did the iptables command not run? Though that was for port 18081.
I have also already opened port 18080 on my dlink router.
[![Port Forwarding][2]][2]

And I've also tried using a virtual server on the router:
[![Virtual Server][3]][3]


I'm not sure where the problem lies. Using the latest Tails OS and Monero Wallet. Anyhelp would be great appreciated.

Thank you in advance...


  [1]: https://medium.com/@_Bosch_/sheeps-noob-guide-to-monero-gui-in-tails-3-2-d75c4e829c17
  [2]: https://i.stack.imgur.com/hGjkA.png
  [3]: https://i.stack.imgur.com/Zjc6f.png

# Discussion History
## moneromooo-monero | 2020-04-05T11:16:00+00:00
Do you have enough space on your disk ? I/O error usually means the hardware is busted, but with LMDB it can be no space left on device. The partition with the db should have at least a couple GB for resizing (ultimately, it wants either ~85 GB for a full blockchain or about ~25 GB for a pruned one).

## moneromooo-monero | 2020-04-05T11:16:45+00:00
18080 only uses TCP btw, if you want to restrict a bit.

## trasherdk | 2020-04-05T13:39:04+00:00
Not knowing the inner workings of a dlink port forward, I'd say UDP is the culprit.
The protocol should be either any, or TCP. Preferably TCP.

## Mike34542 | 2020-04-05T18:10:22+00:00
> Do you have enough space on your disk ? I/O error usually means the hardware is busted, but with LMDB it can be no space left on device. The partition with the db should have at least a couple GB for resizing (ultimately, it wants either ~85 GB for a full blockchain or about ~25 GB for a pruned one).

I'm using a SanDisk 128GB SD with a write speed of 130MB/s. Ive written to the drive already.

Will restrict the virtual server to TCP. Thanks!

## moneromooo-monero | 2020-04-05T19:36:34+00:00
FWIW I get those tor errors even when it works fine, they're not prima facie evidence of connection issues.

## Mike34542 | 2020-04-06T20:39:18+00:00
The problem was is that I formatted the SD card with a FAT32 (same as Tails OS) and the download would max out at 4gb oops. I used Linux's file system and so far have reach 93%. Can you recommend a Bitcoin to Monero exchange i can use from within Tails OS?

## moneromooo-monero | 2020-04-07T01:19:23+00:00
Ask in #monero or reddit.

## Mike34542 | 2020-04-07T02:45:59+00:00
monerod stopped syncing at 96% and ended with this massage:
```
W monerod is now disconnected from the network
```
Has it finished? If not how can i force monerod to complete its sync?

## moneromooo-monero | 2020-04-07T11:34:58+00:00
Restart with --log-level 1, wait for an error to happen in verification, post the resulting end of the log showing it.

## Mike34542 | 2020-04-07T20:15:15+00:00
Result:
```
2020-04-07 20:09:49.699	I Found "1680000:898c0e0b338edc5edd850d241578027f489167cf7b3edb33ed9d08274e15e20e" in TXT record for checkpoints.moneropulse.org
2020-04-07 20:09:49.699	I Core initialized OK
2020-04-07 20:09:49.699	I Initializing p2p server...
2020-04-07 20:09:49.700	I Setting LIMIT: 2048 kbps
2020-04-07 20:09:49.700	I Set limit-up to 2048 kB/s
2020-04-07 20:09:49.700	I Setting LIMIT: 8192 kbps
2020-04-07 20:09:49.700	I Setting LIMIT: 8192 kbps
2020-04-07 20:09:49.701	I Set limit-down to 8192 kB/s
2020-04-07 20:09:49.701	I Setting LIMIT: 2048 kbps
2020-04-07 20:09:49.701	I Set limit-up to 2048 kB/s
2020-04-07 20:09:49.701	I Setting LIMIT: 8192 kbps
2020-04-07 20:09:49.701	I Setting LIMIT: 8192 kbps
2020-04-07 20:09:49.701	I Set limit-down to 8192 kB/s
2020-04-07 20:09:53.592	I dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2020-04-07 20:09:53.796	I dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2020-04-07 20:09:54.617	I dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2020-04-07 20:10:09.701	W dns_threads[1] timed out, sending interrupt
2020-04-07 20:10:09.701	I DNS seed node lookup either timed out or failed, falling back to defaults
2020-04-07 20:10:09.702	I Resolving node address: host=107.152.130.98, port=18080
2020-04-07 20:10:09.702	I Added node: 107.152.130.98:18080
2020-04-07 20:10:09.702	I Resolving node address: host=161.67.132.39, port=18080
2020-04-07 20:10:09.702	I Added node: 161.67.132.39:18080
2020-04-07 20:10:09.702	I Resolving node address: host=163.172.182.165, port=18080
2020-04-07 20:10:09.702	I Added node: 163.172.182.165:18080
2020-04-07 20:10:09.702	I Resolving node address: host=192.110.160.146, port=18080
2020-04-07 20:10:09.702	I Added node: 192.110.160.146:18080
2020-04-07 20:10:09.702	I Resolving node address: host=195.154.123.123, port=18080
2020-04-07 20:10:09.702	I Added node: 195.154.123.123:18080
2020-04-07 20:10:09.702	I Resolving node address: host=198.74.231.92, port=18080
2020-04-07 20:10:09.702	I Added node: 198.74.231.92:18080
2020-04-07 20:10:09.702	I Resolving node address: host=212.83.172.165, port=18080
2020-04-07 20:10:09.702	I Added node: 212.83.172.165:18080
2020-04-07 20:10:09.702	I Resolving node address: host=212.83.175.67, port=18080
2020-04-07 20:10:09.702	I Added node: 212.83.175.67:18080
2020-04-07 20:10:09.702	I Resolving node address: host=5.9.100.248, port=18080
2020-04-07 20:10:09.702	I Added node: 5.9.100.248:18080
2020-04-07 20:10:09.703	I Set server type to: 2 from name: P2P, prefix_name = P2P
2020-04-07 20:10:09.703	I Binding (IPv4) on 0.0.0.0:18080
2020-04-07 20:10:09.703	E Failed to bind IPv4: bind: Address already in use
2020-04-07 20:10:09.703	F Error starting server: Failed to bind IPv4 (set to required)
2020-04-07 20:10:09.703	E Failed to bind server
2020-04-07 20:10:09.703	I Deinitializing core...
2020-04-07 20:10:09.720	I Stopping cryptonote protocol...
2020-04-07 20:10:09.720	I Cryptonote protocol stopped successfully
2020-04-07 20:10:09.721	E Exception in main! Failed to initialize p2p server.
```

## Mike34542 | 2020-04-07T20:18:55+00:00
I dont know if this helps but I also ran monerod status:
```
2020-04-07 20:11:18.939	I Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2020-04-07 20:11:18.939	I Generating SSL certificate
Height: 1999473/1999473 (100.0%) on mainnet, not mining, net hash 994.60 MH/s, v12, up to date, 0(out)+0(in) connections, uptime 0d 15h 3m 59s
```


## moneromooo-monero | 2020-04-08T00:23:01+00:00
It's failing to start because you've got another one running already:

2020-04-07 20:10:09.703	E Failed to bind IPv4: bind: Address already in use

# Action History
- Created by: Mike34542 | 2020-04-05T10:17:55+00:00
- Closed at: 2022-02-19T04:41:19+00:00
