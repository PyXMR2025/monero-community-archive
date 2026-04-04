---
title: Failed to initialize p2p server -- only when adding node
source_url: https://github.com/monero-project/monero/issues/8034
author: martinoshub
assignees: []
labels: []
created_at: '2021-11-01T13:49:01+00:00'
updated_at: '2021-11-06T03:55:51+00:00'
type: issue
status: closed
closed_at: '2021-11-06T03:50:55+00:00'
---

# Original Description
Monerod starts fine (with torsocks). However, when I try to add any nodes with --add-priority-node or --add-peer, it never gets to the point of properly starting up and instead quits with:

ERROR   daemon  src/daemon/main.cpp:362 Exception in main! Failed to initialize p2p server.

The peer can be regular ipv4 or .onion, the same thing happens. It just quits. As soon as I remove the --add-priority-node or an --add-peer argument, it starts up.

Not sure what to make of this. Since monerod will connect to nodes on its own after some time, I don't see how specifying a few extra nodes on the command line should prevent it from starting up, so my guess is that this is some bug. But could be wrong. Any feedback would be appreciated.


# Discussion History
## selsta | 2021-11-01T19:15:51+00:00
Are you able to compile monero yourself? `release-v0.17` branch contains a `--proxy` flag which allows you to skip torsocks by starting monerod this way:

```
./monerod --proxy 127.0.0.1:9050 --add-peer ...
```

## martinoshub | 2021-11-02T06:22:15+00:00
Thanks for the tip. I will do that.

## martinoshub | 2021-11-02T07:28:03+00:00
I have Monero 'Oxygen Orion' (v0.17.2.3-release) - It has no --proxy parameter
I'm compiling release-v0.17 now (confused me a bit because I'd expect 0.17.2.3 to have whatever a 0.17 does).

Additionally, is there a guide on what parameters to use with the proxy-supporting version?
I'm thinking of issues like whether to specify DNS servers or TCP, whether to use --p2p-bind-ip and similar.

## martinoshub | 2021-11-02T09:08:23+00:00
Monero 'Oxygen Orion' (v0.17.2.3-97b7a41bf)

$ ./build/Linux/release-v0.17/release/bin/monerod --help |grep -i proxy
  --tx-proxy arg                        Send local txes through proxy:

(no --proxy option)

I've just compiled this, supposedly it's the latest version from github. Is there a different hash I should have checked out?
Edit: never mind, I needed the master branch rather than the release-v0.17. Thanks for your help.



## martinoshub | 2021-11-02T10:25:06+00:00
2021-11-02 10:24:47.903 I Monero 'Oxygen Orion' (v0.17.0.0-e22ec26be)
2021-11-02 10:24:47.903 I Initializing cryptonote protocol...
2021-11-02 10:24:47.903 I Cryptonote protocol initialized OK
2021-11-02 10:24:47.903 I Initializing core...
2021-11-02 10:24:47.903 I Loading blockchain from folder /data/coin/xmr/.bitmonero/lmdb ...
2021-11-02 10:24:47.903 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-02 10:24:47.940 I Loading checkpoints
2021-11-02 10:24:47.940 I Core initialized OK
2021-11-02 10:24:47.940 I Initializing p2p server...
2021-11-02 10:24:47.942 I Deinitializing core...
2021-11-02 10:24:47.961 I Stopping cryptonote protocol...
2021-11-02 10:24:47.961 I Cryptonote protocol stopped successfully
2021-11-02 10:24:47.961 E Exception in main! Failed to initialize p2p server.


## martinoshub | 2021-11-02T10:26:09+00:00
I remove this one line from the arguments:
--add-priority-node node.moneroworld.com:18089 \

And immediately I no longer get the "failed to initialize p2p server" error message and it no longer quits.


## selsta | 2021-11-02T10:29:52+00:00
I see the issue now. You are trying to add priority nodes with the wrong port.

18089 is the RPC port, what you need is the P2P port at 18080.

```
--add-priority-node node.moneroworld.com:18080
```

## martinoshub | 2021-11-02T14:58:22+00:00
Wouldn't/shouldn't the P2P port be the one listed in the node lists online? That's what I went by. I saw both 18080 and 18089 in the same lists, so the various port numbers didn't seem off because of that. Strange. Anyway, thanks for the tip. I'll do just that and will report back.


## selsta | 2021-11-02T14:59:51+00:00
If you want to connect with a wallet then you need the RPC port (most of time 18081 or 18089), if you want to connect with your node to another node you need the P2P port (18080).

Please report back if this worked, closing it for now.

## martinoshub | 2021-11-02T15:13:46+00:00
So that didn't work, either. Here's my full start line (sans backslash):

~/bin/monerod --proxy 192.168.X:9050
--db-sync-mode fast
--p2p-bind-ip 127.0.0.1 --no-igd
--pad-transactions
--disable-rpc-ban
--rpc-restricted-bind-ip 172.16.X --rpc-restricted-bind-port 18089
--rpc-bind-ip 127.0.0.1 --rpc-bind-port 18081 --rpc-ssl autodetect
--add-priority-node node.moneroworld.com:18080
--ban-list ~/block.txt

2021-11-02 15:00:22.680 I Monero 'Oxygen Orion' (v0.17.0.0-e22ec26be)
2021-11-02 15:00:22.680 I Initializing cryptonote protocol...
2021-11-02 15:00:22.680 I Cryptonote protocol initialized OK
2021-11-02 15:00:22.681 I Initializing core...
2021-11-02 15:00:22.681 I Loading blockchain from folder /data/coin/xmr/.bitmonero/lmdb ...
2021-11-02 15:00:22.681 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-02 15:00:22.717 I Loading checkpoints
2021-11-02 15:00:22.717 I Core initialized OK
2021-11-02 15:00:22.717 I Initializing p2p server...
2021-11-02 15:00:22.718 I Deinitializing core...
2021-11-02 15:00:22.728 I Stopping cryptonote protocol...
2021-11-02 15:00:22.728 I Cryptonote protocol stopped successfully
2021-11-02 15:00:22.728 E Exception in main! Failed to initialize p2p server.

So... that didn't solve it. And I don't see why the startup should fail if I add a node that doesn't work. Some could go down or come back up later as I restart it. But as you can see, the port number wasn't the issue. I've changed it to 18080 as suggested, still the same startup issue.



## selsta | 2021-11-02T15:23:27+00:00
That's a lot of options and it makes it difficult to find the issue. Try this:

```
./monerod --add-priority-node node.moneroworld.com:18080
```

This works fine on my system. Does it also work on yours?

## martinoshub | 2021-11-02T15:23:48+00:00
I'll check in a sec.

+1 question in the meantime: everything goes through the proxy when using --proxy and --tx-proxy is unnecessary when using it, correct?

## martinoshub | 2021-11-02T15:25:43+00:00
$ ~/bin/monerod --proxy 192.168.X:9050 --add-priority-node node.moneroworld.com:18080
2021-11-02 15:25:01.308 I Monero 'Oxygen Orion' (v0.17.0.0-e22ec26be)
2021-11-02 15:25:01.308 I Initializing cryptonote protocol...
2021-11-02 15:25:01.308 I Cryptonote protocol initialized OK
2021-11-02 15:25:01.309 I Initializing core...
2021-11-02 15:25:01.309 I Loading blockchain from folder /data/coin/xmr/.bitmonero/lmdb ...
2021-11-02 15:25:01.309 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-02 15:25:01.346 I Loading checkpoints
2021-11-02 15:25:01.346 I Core initialized OK
2021-11-02 15:25:01.346 I Initializing p2p server...
2021-11-02 15:25:01.348 I Deinitializing core...
2021-11-02 15:25:01.366 I Stopping cryptonote protocol...
2021-11-02 15:25:01.366 I Cryptonote protocol stopped successfully
2021-11-02 15:25:01.366 E Exception in main! Failed to initialize p2p server.

$ ~/bin/monerod --add-priority-node node.moneroworld.com:18080
2021-11-02 15:25:01.308 I Monero 'Oxygen Orion' (v0.17.0.0-e22ec26be)
2021-11-02 15:25:01.308 I Initializing cryptonote protocol...
2021-11-02 15:25:01.308 I Cryptonote protocol initialized OK
2021-11-02 15:25:01.309 I Initializing core...
2021-11-02 15:25:01.309 I Loading blockchain from folder /data/coin/xmr/.bitmonero/lmdb ...
2021-11-02 15:25:01.309 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-11-02 15:25:01.346 I Loading checkpoints
2021-11-02 15:25:01.346 I Core initialized OK
2021-11-02 15:25:01.346 I Initializing p2p server...
2021-11-02 15:25:01.348 I Deinitializing core...
2021-11-02 15:25:01.366 I Stopping cryptonote protocol...
2021-11-02 15:25:01.366 I Cryptonote protocol stopped successfully
2021-11-02 15:25:01.366 E Exception in main! Failed to initialize p2p server.



## martinoshub | 2021-11-02T15:26:27+00:00
Maybe yours is fully synced? Mine is only at around 50%. But regardless, none of these arguments should cause an issue, even during sync. Especially add-priority-node alone (with not even a proxy).

## selsta | 2021-11-02T15:27:03+00:00
Can you start with --log-level 2?

## martinoshub | 2021-11-02T15:49:18+00:00
2021-11-02 15:47:29.543 I Loading checkpoints
2021-11-02 15:47:29.543 I Core initialized OK
2021-11-02 15:47:29.543 I Initializing p2p server...
2021-11-02 15:47:29.543 D Found 0 out connections having height >= 1370980
2021-11-02 15:47:29.544 I Resolving node address: host=node.moneroworld.com, port=18080
2021-11-02 15:47:29.544 E Failed to resolve host name 'node.moneroworld.com': Host not found (non-authoritative), try again later:2
2021-11-02 15:47:29.544 E Failed to parse or resolve address from string: node.moneroworld.com:18080
2021-11-02 15:47:29.544 E Failed to handle command line
2021-11-02 15:47:29.545 I Deinitializing core...
2021-11-02 15:47:29.560 I Stopping cryptonote protocol...
2021-11-02 15:47:29.560 I Cryptonote protocol stopped successfully
2021-11-02 15:47:29.560 E Exception in main! Failed to initialize p2p server.

Hm. Should I still specify TCP DNS on the command line before starting it up? The proxy is a TOR proxy. The log isn't saying what DNS it's attempting to use. Or whether it's trying to resolve through the proxy or not. The account running monerod does not have direct internet access, only to reach the TOR SOCKS proxy.

## martinoshub | 2021-11-02T15:57:20+00:00
I've added DNS_PUBLIC=tcp://91.239.100.100 before the start line (a public DNS server which allows TCP connections on port 53). Still the same result. Although I would expect/hope that the hostname is simply passed to the SOCKS server rather than a public DNS. But either way, it doesn't work.

I've also given full access to the account running monerod to connect to and reach that public DNS server. No change.

## selsta | 2021-11-02T16:25:00+00:00
There is also the `  --proxy-allow-dns-leaks` flag.

## martinoshub | 2021-11-02T16:34:48+00:00
DNS_PUBLIC=tcp://89.233.43.71 ~/bin/monerod --proxy 192.168.X:9050 --proxy-allow-dns-leaks --add-priority-node node.moneroworld.com:18080 --db-sync-mode fast --log-level 2

...
2021-11-02 16:33:37.907 I Core initialized OK
2021-11-02 16:33:37.907 I Initializing p2p server...
2021-11-02 16:33:37.908 D Found 0 out connections having height >= 1370980
2021-11-02 16:33:37.908 I Resolving node address: host=node.moneroworld.com, port=18080
2021-11-02 16:33:37.908 E Failed to resolve host name 'node.moneroworld.com': Host not found (non-authoritative), try again later:2
2021-11-02 16:33:37.908 E Failed to parse or resolve address from string: node.moneroworld.com:18080
2021-11-02 16:33:37.908 E Failed to handle command line
2021-11-02 16:33:37.909 I Deinitializing core...
2021-11-02 16:33:37.931 I Stopping cryptonote protocol...
2021-11-02 16:33:37.931 I Cryptonote protocol stopped successfully
2021-11-02 16:33:37.931 E Exception in main! Failed to initialize p2p server.

$ host node.moneroworld.com 89.233.43.71
Using domain server:
Name: 89.233.43.71
Address: 89.233.43.71#53
Aliases:

node.moneroworld.com has address 96.43.139.226
node.moneroworld.com has address 51.79.173.165
node.moneroworld.com has address 104.238.221.81
node.moneroworld.com has address 204.27.62.98
node.moneroworld.com has address 100.14.90.31


## martinoshub | 2021-11-02T16:39:44+00:00
More debug info: no connection is made to the SOCKS proxy - with or without --proxy-allow-dns-leaks.

## martinoshub | 2021-11-02T16:50:57+00:00
+1 piece of info: no packets sent to the DNS server 89.233.43.71 - whether using --proxy-allow-dns-leaks or not. It just somehow decides the hostname is wrong regardless of what I do, and without communicating through the proxy or otherwise.

## martinoshub | 2021-11-02T16:56:49+00:00
So I've added iptables rules to log so I could check what's happening:

1) DNS_PUBLIC is ignored
2) a lack of --proxy-allow-dns-leaks is ignored
3) it will always try to do a lookup using whatever's in /etc/resolv.conf

All of those are problematic, but especially with (3), it will be pretty hard to connect to onion nodes, right? Shouldn't the hostname be passed to the TOR SOCKS proxy when I don't have --proxy-allow-dns-leaks as an argument?

I might be able to route TOR's DNS lookups to it, but at the very least I need to be able to pass monerod a custom DNS server that it will use to look up peers/priority nodes passed on the command line. If I put something in /etc/resolv.conf it will affect everything else on the box and I would prefer monerod to use something custom, separate from everything else. It would be great if I didn't need to do any of that and it could just use the socks proxy given to it on the command line.

## martinoshub | 2021-11-03T16:49:56+00:00
Seeing the ignored parameters, should this issue be re-opened perhaps? It was closed under the assumption that the issue was caused by a wrong port - which is not the case. Though even with a bad port, I believe the program should start up regardless. Otherwise nodes going down would cause the launcher to no longer be able to start up monerod.

## selsta | 2021-11-03T17:41:39+00:00
I can reopen it, but it seems something related to your local setup which I'm not familiar with so someone else has to reply.

## selsta | 2021-11-03T21:31:38+00:00
@martinoshub The --proxy flag doesn't have DNS support implemented. This means it tries to use your system DNS when using the --add-priority-node flag, which fails. As a workaround you can simply add an IP address for now.

## martinoshub | 2021-11-04T00:56:02+00:00
That explains. But it also prevents me from using .onion nodes. Sure, I can do a lookup and then use that on the command line. But when TOR is restarted, the associated IPs will no longer work.

I wonder what --enable-proxy-dns-leaks does though, if monerod will keep bypassing the proxy to look up hostnames anyway.

To summarize, IMHO the things to do are:

1) Do not abort if a node fails (an automated restart could be prevented by that - a node going down temporarily should not cause termination, rather monerod should keep re-trying the connection just like normally, during runtime). I intend to set maybe 8-10 nodes on the command line, one of them is bound to stop working after a while. So it would be imperative that this doesn't prevent a startup.

2) If a SOCKS proxy is enabled, then make all connections go through it rather than doing separate DNS lookups. The current way it works is worse than torsocks. At least with torsocks .onion connections worked fine, without much effort. Also, apparently based on this discovery, my internal DNS server address got leaked through TOR thanks to the currently suggested tutorial based on torsocks. So that's not great. Not a big deal either, but still...

3) Make an environment variable or other parameter which allows me to control what DNS server monerod uses. I think this is already there, just not working correctly and ignored in some places (like looking up nodes given on the command line).

Since these are definitely things to add, implement and fix, I propose the issue be re-opened (or consolidated into a new issue).


## selsta | 2021-11-04T13:42:43+00:00
> I wonder what --enable-proxy-dns-leaks does though, if monerod will keep bypassing the proxy to look up hostnames anyway.

monerod will lookup dns seed nodes, dns ban list and do dns update checks if you specify `--enable-proxy-dns-leaks`.

Specifying hostnames via command line arguments will resolve on startup and the program will terminate if this isn't possible (that's what you are seeing), with or without `--enable-proxy-dns-leaks`.

> Do not abort if a node fails (an automated restart could be prevented by that - a node going down temporarily should not cause termination, rather monerod should keep re-trying the connection just like normally, during runtime). I intend to set maybe 8-10 nodes on the command line, one of them is bound to stop working after a while. So it would be imperative that this doesn't prevent a startup.

It's fine if a node stops working, the daemon will only abort on startup if it is unable to resolve a hostname. If you only specify IP addresses this won't happen.

> Make an environment variable or other parameter which allows me to control what DNS server monerod uses. I think this is already there, just not working correctly and ignored in some places (like looking up nodes given on the command line).

`DNS_PUBLIC` env var is used for DNS-SEC queries (dns seed nodes, dns ban list, dns update checker, ...) , but it isn't used for resolving hostnames provided via command line args.

> +1 question in the meantime: everything goes through the proxy when using --proxy and --tx-proxy is unnecessary when using it, correct?

`--tx-proxy` is for connecting to tor / i2p nodes (https://github.com/monero-project/monero/blob/master/docs/ANONYMITY_NETWORKS.md#outbound-connections), `--proxy` is for communicating with ipv4 / ipv6 addresses over a proxy.

------------------

To sum things up, try the following:

1) Don't specify any hostnames to command line arguments that have to be resolved on startup, adding .onion peers should be fine if you add `--tx-proxy`
2) Add both `--proxy 127.0.0.1:9050` (IPv4 proxy) and `--tx-proxy tor,127.0.0.1:9050` (Tor peers)
3) Don't add `--enable-proxy-dns-leaks`

## martinoshub | 2021-11-06T03:50:55+00:00
> Specifying hostnames via command line arguments will resolve on startup and the program will terminate
> It's fine if a node stops working, the daemon will only abort on startup if it is unable to resolve a hostname. If you only specify IP addresses this won't happen.

Thanks for your answers, they have been helpful (see later below).

One thing I'd like to argue though: if I specify an IP address, it may be out of date even though the hostname is kept up-to-date. If monerod will start with a non-working node and would continue to look up DNS for the nodes as their IP changes, it doesn't make sense to refuse to launch and it would be a degraded way of handling nodes for me to do one IP lookup and insist on that for all future launches.

I get the suggestion as a workaround (and I am doing just that), but the correct proxies should be used even on startup. It should be no different in the long run. That is why I kindly request a fix to that part.

I do appreciate your pointers about adding both --proxy and --tx-proxy, something I asked about earlier. It's my fault that I missed the documentation on anonymity networks. I thought --tx-proxy was only for transactions and didn't know the implications when it's used in conjunction with --proxy.
The important line was "Only handshakes, peer timed syncs and transaction broadcast messages are supported over anonymity networks." - So that explains the need to use it. And now I can start the daemon with onion priority nodes.

The only question I still have is, if monerod gets hostnames seeded from other nodes and it tries to look them up - will it be able to do that? Since there's no local DNS available that it can use. During runtime, will those hostnames be looked up through the SOCKS proxy, or using the TCP DNS through the socks proxy? Or will it only be able to connect to nodes with an IP address advertised, if it can't use the system DNS?

I'll close the issue for now, but would appreciate clarification on the last question regardless. Thanks in advance.



# Action History
- Created by: martinoshub | 2021-11-01T13:49:01+00:00
- Closed at: 2021-11-06T03:50:55+00:00
