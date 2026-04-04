---
title: DNS checkpoint query timeout on OSX
source_url: https://github.com/monero-project/monero/issues/1535
author: ManfredKarrer
assignees: []
labels: []
created_at: '2017-01-07T12:02:56+00:00'
updated_at: '2021-08-13T06:38:05+00:00'
type: issue
status: closed
closed_at: '2021-08-13T06:38:05+00:00'
---

# Original Description
When I run the daemon (10.1 or GUI app) it takes about 4-7 minutes until it is synced OK, even if I have the latest blocks already. I also removed the database so redownloaded the blockchain but it is the same. I use OSX 10.11.6. 

The 6 min. delay is before I get that warning. I run it also once with logLevel 2 and saw more of those warnings. No idea if it relelated.
 
2017-Jan-07 12:53:56.062363 Blockchain initialized. last block: 1218534, d0.h0.m3.s24 time ago, current difficulty: 6260530991
2017-Jan-07 12:59:19.236466 WARNING: no two valid MoneroPulse DNS checkpoint records were received


Full logs:
2017-Jan-07 12:53:51.167354 Initializing cryptonote protocol...
2017-Jan-07 12:53:51.167379 Cryptonote protocol initialized OK
2017-Jan-07 12:53:51.167476 Initializing p2p server...
2017-Jan-07 12:53:51.974665 Set limit-up to 2048 kB/s
2017-Jan-07 12:53:51.974725 Set limit-down to 8192 kB/s
2017-Jan-07 12:53:51.974749 Set limit-up to 2048 kB/s
2017-Jan-07 12:53:51.974779 Set limit-down to 8192 kB/s
2017-Jan-07 12:53:51.975533 Binding on 0.0.0.0:18080
2017-Jan-07 12:53:51.975849 Net service bound to 0.0.0.0:18080
2017-Jan-07 12:53:51.975871 Attempting to add IGD port mapping.
2017-Jan-07 12:53:55.986699 No IGD was found.
2017-Jan-07 12:53:55.986779 P2p server initialized OK
2017-Jan-07 12:53:55.986880 Initializing core rpc server...
2017-Jan-07 12:53:55.986927 Binding on 127.0.0.1:18081
2017-Jan-07 12:53:55.987352 Core rpc server initialized OK on port: 18081
2017-Jan-07 12:53:55.987390 Initializing core...
2017-Jan-07 12:53:55.989111 Loading blockchain from folder /Users/dev/.bitmonero/lmdb ...
2017-Jan-07 12:53:55.989155 option: fast
2017-Jan-07 12:53:55.989172 option: async
2017-Jan-07 12:53:55.989186 option: 1000
2017-Jan-07 12:53:56.062363 Blockchain initialized. last block: 1218534, d0.h0.m3.s24 time ago, current difficulty: 6260530991
2017-Jan-07 12:59:19.236466 WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-Jan-07 12:59:19.236985 Core initialized OK
2017-Jan-07 12:59:19.237009 Starting core rpc server...
2017-Jan-07 12:59:19.237024 Run net_service loop( 2 threads)...
2017-Jan-07 12:59:19.237326 [SRV_MAIN]Core rpc server started ok
2017-Jan-07 12:59:19.237459 [SRV_MAIN]Starting p2p net loop...
2017-Jan-07 12:59:19.237509 [SRV_MAIN]Run net_service loop( 10 threads)...
2017-Jan-07 12:59:20.238148 [P2P1]
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level>" command*, where <level> is between 0 (no details) and 4 (very verbose).

Use "help" command to see the list of available commands.

Note: in case you need to interrupt the process, use "exit" command. Otherwise, the current progress won't be saved.
**********************************************************************
2017-Jan-07 12:59:21.473905 [P2P9][128.199.192.43:18080 OUT]Sync data returned a new top block candidate: 1218535 -> 1218537 [Your node is 2 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-Jan-07 12:59:22.189217 [P2P7][139.59.11.117:18080 OUT]Sync data returned a new top block candidate: 1218535 -> 1218537 [Your node is 2 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-Jan-07 12:59:23.209686 [P2P2][119.28.61.122:18080 OUT]Sync data returned a new top block candidate: 1218535 -> 1218537 [Your node is 2 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-Jan-07 12:59:24.438428 [P2P3][139.59.11.117:18080 OUT]Synced 1218537/1218537
2017-Jan-07 12:59:24.438489 [P2P3][139.59.11.117:18080 OUT] SYNCHRONIZED OK
2017-Jan-07 12:59:24.438507 [P2P3]
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Please note, that the blockchain will be saved only after you quit the daemon with "exit" command or if you use "save" command.
Otherwise, you will possibly need to synchronize the blockchain again.

Use "help" command to see the list of available commands.
**********************************************************************
2017-Jan-07 12:59:24.438678 [P2P2][128.199.192.43:18080 OUT]Synced 1218537/1218537
2017-Jan-07 12:59:24.438705 [P2P2][128.199.192.43:18080 OUT] SYNCHRONIZED OK
2017-Jan-07 12:59:26.099206 [P2P3][119.28.61.122:18080 OUT] SYNCHRONIZED OK



# Discussion History
## moneromooo-monero | 2017-01-07T12:52:40+00:00
Can you rename this to, eg, DNS checkpoint query timeout on OSX, please ?

Also, does the following work without timeout:

dig -t TXT checkpoints.moneropulse.se

You can replace by whatever other DNS tool you might have instead.

## ManfredKarrer | 2017-01-07T16:20:35+00:00
First call worked, second i got  a timeout:

mbp:~ dev$ dig -t TXT checkpoints.moneropulse.se

; <<>> DiG 9.8.3-P1 <<>> -t TXT checkpoints.moneropulse.se
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 11284
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;checkpoints.moneropulse.se.	IN	TXT

;; Query time: 4751 msec
;; SERVER: 80.58.61.254#53(80.58.61.254)
;; WHEN: Sat Jan  7 17:18:23 2017
;; MSG SIZE  rcvd: 44

mbp:~ dev$ dig -t TXT checkpoints.moneropulse.se

; <<>> DiG 9.8.3-P1 <<>> -t TXT checkpoints.moneropulse.se
;; global options: +cmd
;; connection timed out; no servers could be reached
mk-mbp:~ dev$ 



## immon | 2017-06-09T09:58:51+00:00
I have debugged the issue (on linux).
The UDP DNS reply from cloudflare's nameserver for the query has TC bit set which means the reply is truncated and should be sent by TCP. Dig does it however the traffic to port 53/tcp is blocked by your firewall or ISP's.
Make sure you can reach external servers on 53/tcp.

btw, if cloudflare would reply with some data along with TC bit set (as most DNS implementations do) it had not be an issue.

## fluffypony | 2017-06-09T16:52:37+00:00
From Olafur Gudmundsson @ CloudFlare: 'I tested this with dig from a bunch of locations and see no problems, TCP works. Answer is 1652 bytes, check your path "dig org. DNSKEY" '

## immon | 2017-06-09T18:22:09+00:00
yes, cloudflare NSes work correctly over TCP. 53/tcp traffic is filtered somewhere in between (firewall on the localhost or more likely by the ISP).

Cloudflare truncated UDP response is empty. If it would include a partial data it might help people having the 53/tcp traffic filtered
```
$ dig +dnssec +ignore +norec txt checkpoints.moneropulse.se @kip.ns.cloudflare.com.
;; flags: qr aa tc; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
                ^^                   ^^^
```

## bitkevin | 2017-11-10T16:27:05+00:00
My node always failed when loading checkpoints, here is my dig records:

```
# dig -t TXT checkpoints.moneropulse.se

; <<>> DiG 9.10.3-P4-Ubuntu <<>> -t TXT checkpoints.moneropulse.se
;; global options: +cmd
;; connection timed out; no servers could be reached

# dig -t TXT checkpoints.moneropulse.org

; <<>> DiG 9.10.3-P4-Ubuntu <<>> -t TXT checkpoints.moneropulse.org
;; global options: +cmd
;; connection timed out; no servers could be reached

# dig -t TXT checkpoints.moneropulse.net

; <<>> DiG 9.10.3-P4-Ubuntu <<>> -t TXT checkpoints.moneropulse.net
;; global options: +cmd
;; connection timed out; no servers could be reached

```

monerod logs:

```
2017-11-10 15:38:02.931     7f1b2d61a740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /work/monerod/lmdb ...
2017-11-10 15:38:03.107     7f1b2d61a740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:421     Loading checkpoints
2017-11-10 15:45:42.744     7f1b2d61a740        WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-10 15:45:42.745     7f1b2d61a740        INFO    global  src/daemon/core.h:78    Core initialized OK
2017-11-10 15:45:42.745     7f1b2d61a740        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
```
Seems skip after did dns checkpoints timeout.

----

After I wrote this, I found the problem, it's DNS server, so I add `8.8.8.8` as backup dns server, it works!

So maybe use hard code dns server as backup DNS server is a good idea, at least won't take so much time at startup.

## bitkevin | 2017-11-10T16:31:03+00:00
Or use DNS server which users specified. like add args: `--checkpoints-dns-server`.

If you run `monerod` in docker, you could add specify dns server by args `--dns`, example: `docker run -it --dns 8.8.8.8 ...`

## moneromooo-monero | 2017-11-11T18:46:03+00:00
You can use DNS_PUBLIC=tcp://8.8.8.8  (an env var).

## weisjohn | 2017-12-17T03:21:45+00:00
@bitkevin thanks, that DNS entry comment saved my day!

## selsta | 2021-08-13T06:38:05+00:00
Closing as the issue doesn't seem to be on monero's side.

# Action History
- Created by: ManfredKarrer | 2017-01-07T12:02:56+00:00
- Closed at: 2021-08-13T06:38:05+00:00
