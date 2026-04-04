---
title: E mined block failed verification
source_url: https://github.com/monero-project/monero/issues/9496
author: Jayd603
assignees: []
labels:
- reproduction needed
created_at: '2024-10-01T14:05:09+00:00'
updated_at: '2024-12-28T06:39:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Ran this public node for years, has the latest version, restricted-rpc is enabled and CPU use doesn't show monerod mining at all. ..yet logs are flooded with these:
2024-09-23 17:51:00.906	E mined block failed verification

First i've seen it, I appear to be on the latest block and handling connections ok anyway.




# Discussion History
## selsta | 2024-10-01T14:10:06+00:00
When was the last time you saw this message?

## Jayd603 | 2024-10-01T14:13:31+00:00
They are still happening.  Started a few days ago.

2024-10-01 14:10:23.869	E Transaction not found in pool
2024-10-01 14:10:50.004	E mined block failed verification
2024-10-01 14:11:07.976	E Transaction not found in pool
2024-10-01 14:11:47.544	E mined block failed verification


## Jayd603 | 2024-10-01T15:20:51+00:00
I restarted the container, immediately the same error started showing.  



## selsta | 2024-10-01T15:22:27+00:00
Even a restricted RPC allows users to submit a mined block. Can you try if you get this message with no external RPC at all?

## Jayd603 | 2024-10-01T15:26:05+00:00
Oh, I didn't know that.  possibly just someone trying to submit bad blocks over and over?

## selsta | 2024-10-01T20:17:38+00:00
Possible, yes. But not sure why.

## nahuhh | 2024-10-03T19:31:54+00:00
Do you run with `--public-node`?

## thilool | 2024-10-04T18:52:54+00:00
I see the same issue on my node starting at 2014-09-30 at 20:00
I don't run the explicit command --public-node but I have of course restricted-rpc

## Jayd603 | 2024-10-04T18:53:46+00:00
I do run with public-node.

## thilool | 2024-10-04T18:57:22+00:00
is there a way to see the IP of the sender which spams my node and add it to a block list?

## selsta | 2024-10-04T18:58:24+00:00
It might show up with log level 2

## thilool | 2024-10-04T19:36:57+00:00
with log-level=2 I see this errors:
2024-10-04 19:33:34.586	E Exception in boosted_tcp_server<t_protocol_handler>::handle_accept: set_option: Bad file descriptor
2024-10-04 19:33:34.586	E Some problems at accept: Success, connections_count = 2

and this:
2024-10-04 19:34:58.073	E Error in boosted_tcp_server<t_protocol_handler>::handle_accept: asio.misc:1
2024-10-04 19:34:58.073	E Some problems at accept: Already open, connections_count = 2

showing up regularly

## selsta | 2024-10-04T19:39:53+00:00
Doesn't seem related to me based on the error message.

## nahuhh | 2024-10-04T19:42:18+00:00
> is there a way to see the IP of the sender which spams my node and add it to a block list?

You should see (on loglevel 1) the ip which is contacting rpc endpoints 

## thilool | 2024-10-04T19:44:49+00:00
this is more detail:
2024-10-04 19:36:17.007	D [178.25.224.210:11815 OUT] LEVIN_PACKET_RECEIVED. [len=3782, flags1, r?=?, cmd = 2002, v=1
2024-10-04 19:36:17.007	I [178.25.224.210:11815 OUT] 3782 bytes received for category command-2002 initiated by peer
2024-10-04 19:36:17.007	I [178.25.224.210:11815 OUT] Received NOTIFY_NEW_TRANSACTIONS (2 txes)
2024-10-04 19:36:17.008	I Including transaction <1ea20076555b95c2924aa092d40cd2e31e4526d61e66c9a5ef12830643ced308>
2024-10-04 19:36:17.008	I Including transaction <2674a3a3abf15b5fa6e6ba35101ed5f8f1e7e7f1a89bacd2d279bf21229bf2ef>
2024-10-04 19:36:17.008	D tx <1ea20076555b95c2924aa092d40cd2e31e4526d61e66c9a5ef12830643ced308>already have transaction in tx_pool
2024-10-04 19:36:17.009	D tx <2674a3a3abf15b5fa6e6ba35101ed5f8f1e7e7f1a89bacd2d279bf21229bf2ef>already have transaction in tx_pool
2024-10-04 19:36:17.141	D handle_accept
2024-10-04 19:36:17.142	E Error in boosted_tcp_server<t_protocol_handler>::handle_accept: asio.misc:1
2024-10-04 19:36:17.142	E Some problems at accept: Already open, connections_count = 2


looks like somebody tried to send 2 tx which are not accepted

## thilool | 2024-10-04T19:46:05+00:00
again more detail about the other error:
2024-10-04 19:36:19.508	I [113.196.177.100:29671 OUT] 1559 bytes sent for category command-2002 initiated by us
2024-10-04 19:36:19.508	D [113.196.177.100:29671 OUT] LEVIN_PACKET_SENT. [len=1559, flags1, r?=?, cmd = 2002, ver=1
2024-10-04 19:36:19.508	I [185.250.243.159:18082 OUT] 1559 bytes sent for category command-2002 initiated by us
2024-10-04 19:36:19.508	D [185.250.243.159:18082 OUT] LEVIN_PACKET_SENT. [len=1559, flags1, r?=?, cmd = 2002, ver=1
2024-10-04 19:36:19.508	I [184.75.221.43:18191 OUT] 1559 bytes sent for category command-2002 initiated by us
2024-10-04 19:36:19.508	D [184.75.221.43:18191 OUT] LEVIN_PACKET_SENT. [len=1559, flags1, r?=?, cmd = 2002, ver=1
2024-10-04 19:36:19.546	D handle_accept
2024-10-04 19:36:19.546	E Error in boosted_tcp_server<t_protocol_handler>::handle_accept: asio.misc:1
2024-10-04 19:36:19.547	E Some problems at accept: Already open, connections_count = 2


## nahuhh | 2024-10-04T20:00:36+00:00
I dont see the same mined block failed verification log. your issue seems unrelated @thilool 

## thilool | 2024-10-04T22:14:49+00:00
it does not show up in the level 2 log.
here a snipped with level 1:

024-10-04 22:12:46.650	I HTTP [194.233.152.128] POST /json_rpc
2024-10-04 22:12:46.651	I [194.233.152.128:26017 INC] Calling RPC method submitblock
2024-10-04 22:12:46.666	I [162.218.65.83:18085 OUT] 57025 bytes received for category command-2002 initiated by peer
2024-10-04 22:12:46.666	I [162.218.65.83:18085 OUT] Received NOTIFY_NEW_TRANSACTIONS (22 txes)
2024-10-04 22:12:46.667	I Including transaction <8a8f4c331557d98e8e05f950edbab177873603a0024504d0cb8b9a86db513a8a>
2024-10-04 22:12:46.667	I Including transaction <424ed8763145ffc6dc1bb9e83c83b5d35e36fbcd9395c42fe93f6175cd5b43ca>
2024-10-04 22:12:46.667	I Including transaction <f24a9496a94616dad06d142f7dfd2c4050535aa60ddae875e57a1cd4bc37ba9f>
2024-10-04 22:12:46.668	I Including transaction <fa8dea98c65525bb01557144ef11b0c3b0a911f4ce7087a8aaf0cf3d0a0cbdce>
2024-10-04 22:12:46.668	I Including transaction <1c5a8d3011041d0aba7afbf37178f552071d6dd80eeceef4f6906d0fd79a490c>
2024-10-04 22:12:46.668	I Including transaction <1cb3c2e5790c5ab7efdd53077fd83aff02f8d0940f2dee4423a1c338caa30e2c>
2024-10-04 22:12:46.669	I Including transaction <266c27026033347057d73e86d450fa43cec61d2e1fdaa2c7a733dd09f6779b30>
2024-10-04 22:12:46.669	I Including transaction <dc7a4b894f3c76ae931458b856520cdf94798c0b251adf8004254f2428a2d79b>
2024-10-04 22:12:46.670	I Including transaction <bd3334456567a7957bb8c9067b9e9046528d3e4e312285c6a70457ca65ee8300>
2024-10-04 22:12:46.670	I Including transaction <d0c92ecd82309251fc15b4a1fb5169a15652b2905470033ee43226bac3d0c7c9>
2024-10-04 22:12:46.670	I Including transaction <dab72c11e95be5a42790586ffb558f9f7bb7c329422918acfee09e170e973e26>
2024-10-04 22:12:46.671	I Including transaction <ae8ce5b76f10b249888d94659b6f15cb65569042bffd5f7a06cb5adc583ff4f7>
2024-10-04 22:12:46.671	I Including transaction <2448b230cdc110904cb06656667a6ec437af1e621084a2e7159200c2825d4c6d>
2024-10-04 22:12:46.672	I Including transaction <666417baacbd626e0ef897151ee4465b734cd46a4a5caf2c17148dd2f1e584b9>
2024-10-04 22:12:46.674	I Including transaction <52aadc3c739f39c095b8d17eac7207c710a432051307784af5f44effd38619eb>
2024-10-04 22:12:46.674	I Including transaction <0c32c21bed5be4fc1d365c3e1c702b456fdf33b289ac4a0e2fd0c6a0f291f2ce>
2024-10-04 22:12:46.674	I Including transaction <f0324afc1c9ca121d168422ed414ee123216fdb098e3d390cefd0c37d425fe98>
2024-10-04 22:12:46.675	I Including transaction <b1a72711d02945d0d10d9e60a07d3f16874033e87ec020b18950172d83b9d0ad>
2024-10-04 22:12:46.675	I Including transaction <82f0e854e6a721b3b35222775bd049dc3f2c5c78f48fdbbdc5de59e8998e4076>
2024-10-04 22:12:46.676	I Including transaction <03af9ea6634023907dd84146ac6c1b6e5a6043127619d3ca0e959a8f147b2f61>
2024-10-04 22:12:46.676	I Including transaction <83d46365bad4e695fa2249a2addf7bbe64452b9103abbdb7f40c6602bc0efe84>
2024-10-04 22:12:46.677	I Including transaction <eb97286c4cc51f3054a26c67065d1c6d0f16f20f37de5afdb3e783e07535c83d>
2024-10-04 22:12:46.688	E Block with id: <5051a2feb0afb1bbd86a28a9d54cffe191ec5cb4d8c25fdd768a29b746235562>
2024-10-04 22:12:46.688	E does not have enough proof of work: <f21f9d85a3ae70e06406404f90930c777f723ca65e809e9b8536b6acbf270000> at height 3251967, unexpected difficulty: 346407873584
2024-10-04 22:12:46.689	E mined block failed verification


## thilool | 2024-10-04T22:17:18+00:00
here another one:
2024-10-04 22:14:11.904	W [<none> OUT] back ping connect failed to 136.60.3.95:18080
2024-10-04 22:14:12.000	I [162.218.65.219:11095 INC] 227 bytes received for category command-1001 initiated by peer
2024-10-04 22:14:12.001	I [162.218.65.219:11095 INC] 10 bytes sent for category command-1007 initiated by us
2024-10-04 22:14:12.002	I [162.218.65.219:11095 INC] 15520 bytes sent for category command-1001 initiated by us
2024-10-04 22:14:12.129	I HTTP [175.176.28.62] POST /json_rpc
2024-10-04 22:14:12.129	I [175.176.28.62:46116 INC] Calling RPC method getblocktemplate
2024-10-04 22:14:12.209	I HTTP [194.233.152.128] POST /json_rpc
2024-10-04 22:14:12.209	I [194.233.152.128:26045 INC] Calling RPC method submitblock
2024-10-04 22:14:12.241	I HTTP [160.178.181.182] GET /getheight
2024-10-04 22:14:12.242	I [160.178.181.182:50518 INC] calling /getheight
2024-10-04 22:14:12.243	E Block with id: <ffd2b3a5af79592e227e3e50d6bf78eac2c58eb5794fba1c708c9a4470dd97db>
2024-10-04 22:14:12.243	E does not have enough proof of work: <a248ed5c82a43315e98fce63c24367631e38b4f2d3d2ede208fec4b529120000> at height 3251968, unexpected difficulty: 346066290034
2024-10-04 22:14:12.243	E mined block failed verification


btw I am running p2pool as well may this has something to do with it?


## thilool | 2024-10-04T22:19:17+00:00
these error are always in between:

2024-10-04 22:15:05.178	I Including transaction <96583190dda605d5b45597fd445a283c3f1c284bc5cf7bfc38a98cc2054970ac>
2024-10-04 22:15:05.190	I HTTP [197.254.96.246] POST /json_rpc
2024-10-04 22:15:05.190	I [197.254.96.246:59506 INC] Calling RPC method submitblock
2024-10-04 22:15:05.190	E Transaction not found in pool


maybe this is some hint what is going on there.
At the same time the hashrate of my server drops about 1000Hs

## thilool | 2024-10-04T22:24:56+00:00
I stopped p2pool to check but the errors still show up:
2024-10-04 22:21:12.179	I HTTP [194.233.152.128] POST /json_rpc
2024-10-04 22:21:12.179	I [193.142.4.107:37683 INC] 10 bytes received for category command-1003 initiated by peer
2024-10-04 22:21:12.179	I [194.233.152.128:25665 INC] Calling RPC method submitblock
2024-10-04 22:21:12.179	I [193.142.4.107:37683 INC] 38 bytes sent for category command-1003 initiated by us
2024-10-04 22:21:12.185	W [<none> OUT] back ping connect failed to 162.218.65.219:18080
2024-10-04 22:21:12.202	E Block with id: <b6cccb6d1badab1578437d8a5074ef4ecf4338b7d275a438fadc4ae5bf8473c2>
2024-10-04 22:21:12.202	E does not have enough proof of work: <2d3fcce41c200893435694cf1551f8c925eaebbfa6ebde1a984cb3addb370000> at height 3251971, unexpected difficulty: 346109226234
2024-10-04 22:21:12.202	E mined block failed verification

The IP 162.218.65.219:18080 seems to always show up right before the error


## nahuhh | 2024-10-05T00:13:46+00:00
If youre not using --public-node, youve likely posted your node's address publicly on a website like monero.fail.

you have a 194* ip using your RPC port and submitting bad blocks. You also have malicious node peers.

restart you nlde and add `enable-dns-blocklist=1` and stop providing public rpc to strangers

## thilool | 2024-10-05T09:04:26+00:00
enable-dns-blocklist is always on on my node so this did not prevent the issue.
actually you where right. I posted the host, thinking I do something good... well lesson learned. 
I changed my RPC port to something totally different out of spec just for my personal use from now on.

## nahuhh | 2024-10-05T14:20:23+00:00
162.218.65.219:18080

this node should have been blocked by the dns blocklist

## thisIsNotTheFoxUrLookingFor | 2024-10-06T05:10:50+00:00
monero  | 2024-10-06 05:01:05.741       E Transaction not found in pool
monero  | 2024-10-06 05:01:19.325       E mined block failed verification
monero  | 2024-10-06 05:01:41.136       E mined block failed verification
monero  | 2024-10-06 05:02:23.711       E mined block failed verification
monero  | 2024-10-06 05:02:26.886       E Transaction not found in pool
monero  | Oct 06 05:02:55.000 [notice] Closed 1 streams for service [scrubbed].onion for reason resolve failed. Fetch status: No more HSDir available to query.
monero  | 2024-10-06 05:03:04.664       E mined block failed verification
monero  | Oct 06 05:03:07.000 [notice] Closed 1 streams for service [scrubbed].onion for reason resolve failed. Fetch status: No more HSDir available to query.
monero  | Oct 06 05:03:18.000 [notice] Closed 1 streams for service [scrubbed].onion for reason resolve failed. Fetch status: No more HSDir available to query.
monero  | 2024-10-06 05:03:24.116       E mined block failed verification
monero  | 2024-10-06 05:03:27.785       E mined block failed verification
monero  | 2024-10-06 05:03:29.742       E mined block failed verification
monero  | 2024-10-06 05:03:48.033       E mined block failed verification

## nahuhh | 2024-10-06T05:12:36+00:00
@thisIsNotTheFoxUrLookingFor https://github.com/monero-project/monero/issues/9496#issuecomment-2394809444

## thisIsNotTheFoxUrLookingFor | 2024-10-06T05:14:24+00:00
> 162.218.65.219:18080

I have DNS blocklist set in my conf @nahuhh 

I guess restart monerod will force new DNS query for blocklist

Shouldn't a peer be banned after submitting x bad blocks?

Just realised as they are pushing to RPC they are not a peer, I think DNS blocklist is going to ban P2P peers and this might be why it don't work in this case

## thisIsNotTheFoxUrLookingFor | 2024-10-06T05:18:12+00:00
> At the same time the hashrate of my server drops about 1000Hs

Yah they are trying to DOS us by forcing constant block and TX verification I guess?

## nahuhh | 2024-10-06T05:23:45+00:00
> > 162.218.65.219:18080
> 
> I have DNS blocklist set in my conf @nahuhh 

The above ip is if a spy node _peer_. They arent the ones submitting the blocks

dns blocklist only works for p2p peers. The bad blocks are being submit via RPC.

> I guess restart monerod will force new DNS query for blocklist
>
> Shouldn't a peer be banned after submitting x bad blocks?

Those arent peers submitting bad blocks. 

do you have `disable-rpc-ban` enabled?

please see my previous comment - disable public-node and stop providing a remote node for strangers. 

## thisIsNotTheFoxUrLookingFor | 2024-10-06T05:30:57+00:00
> The above ip is if a spy node _peer_. They arent the ones submitting the blocks

They should spy through Tor lol that is dumb of them

## thisIsNotTheFoxUrLookingFor | 2024-10-06T05:47:53+00:00
> disable public-node and stop providing a remote node for strangers.

Probably they want this lol, I have the resources to absorb what they are doing so meh I can keep public RPC up

## Boog900 | 2024-10-06T14:58:38+00:00
I have been trying to think about what these nodes are trying to do, although just a general DOS attack would be a valid reason I find it weird how an entity like linking lion would want to do that.

Obviously I am not 100% certain but they could be trying to exploit a timing difference when handling a block to see if a node has a stem pool transaction. When we receive a block from RPC, we try to build the full block, including all the txs using our tx-pool:

https://github.com/monero-project/monero/blob/9866a0e9021e2422d8055731a586083eb5e2be67/src/cryptonote_core/cryptonote_core.cpp#L1526-L1538

As you can see we are using `relay_category::all` which means we are also pulling stem txs.

I did some rough tests submitting blocks to my own node with and without some unknown txs, when an unknown tx is included the response is around 50-100x faster. 

I think an easy way to fix this would be to not look at the whole pool for restricted RPC.

FWIW this doesn't explain the other P2P messages/RPC requests that were happening around the same time. It would be good to get more log data if anyone has any.

## thisIsNotTheFoxUrLookingFor | 2024-10-08T09:33:18+00:00
> the response is around 50-100x faster.

Perhaps in a situation like mining where block propagation time matters, the intention is to try DOS other nodes such that their blocks that are mined have a greater chance of being propagated first, that said, I'm not sure of the stats for orphaned blocks in XMR but I would reckon it would be quite low yea?

I think to find the originator of a dandelion++ TX all a malicious node has to do is not relay that stem TX and then it will force the originator to fluff it anyway wouldn't it? It would seem like a better way to do this would be to sybil the fk out of nodes get a really good connection footprint across the entire P2P network and then withhold stem TX waiting for maker to fluff it. I am assuming that each node that receives a stem TX has a fixed amount of time it waits for fluff and so if it is 10m then obviously the 10m will expire for the maker first then it fluffs. This could be fixed by making the time all nodes wait significantly random, then we get plausible deniability on who is the maker again. But this might be how it works now unsure, I been wanting to ask someone who knows.


## Boog900 | 2024-10-08T13:19:01+00:00
> the intention is to try DOS other nodes such that their blocks that are mined have a greater chance of being propagated first

If this was the case they would just send empty blocks to make your node compute the PoW hash each time, this isn't what they are doing though, in your logs:

```
monero | 2024-10-06 05:01:05.741 E Transaction not found in pool
monero | 2024-10-06 05:01:19.325 E mined block failed verification
monero | 2024-10-06 05:01:41.136 E mined block failed verification
monero | 2024-10-06 05:02:23.711 E mined block failed verification
monero | 2024-10-06 05:02:26.886 E Transaction not found in pool
```

Each of those `Transaction not found in pool` was a block that contained a tx your node did not know about, for these blocks your node was not computing the PoW hash.

> This could be fixed by making the time all nodes wait significantly random, then we get plausible deniability on who is the maker again. But this might be how it works now unsure, I been wanting to ask someone who knows.

Yeah, we do already have randomised timers for this

## thisIsNotTheFoxUrLookingFor | 2024-10-15T12:19:38+00:00
```
43.255.118.53
43.255.118.78
58.177.87.243
69.235.238.40
170.75.167.55
110.54.223.238
138.3.242.77
212.107.29.73
193.176.211.152
123.193.251.64
49.205.151.168
103.36.25.15
116.110.77.152
122.161.65.44
115.188.107.62
113.160.226.24
113.161.171.106
45.134.20.85
45.134.20.86
202.7.251.30
103.229.54.138
103.21.164.224
103.229.54.210
188.253.112.125
188.253.112.136
188.253.112.141
141.11.238.17
141.11.238.31
103.229.54.134
141.11.238.35
141.11.238.21
141.11.238.36
141.11.238.37
193.32.127.221
202.7.251.30
188.253.112.122
103.229.54.210
103.229.54.138
103.115.243.31
2001:ee0:47ec:c810::/64
2603:3024:19d1:a100::/64
2a02:587:5fe3:c200::/64
2400:1a00:bd11:3700::/64
2400:3f60:10::/64
```

^ perps proxys

## selsta | 2024-10-15T12:22:45+00:00
@thisIsNotTheFoxUrLookingFor did it stop after banning all these IPs?

## thisIsNotTheFoxUrLookingFor | 2024-10-15T12:25:46+00:00
> @thisIsNotTheFoxUrLookingFor did it stop after banning all these IPs?

Yup, I am running my node (RPC) through cloudflare and I poped in a WAF rule and it has stopped them dead... for now till they roll their proxies and get new IPs.

![image](https://github.com/user-attachments/assets/91085d4d-b746-4884-8233-bd290b0a4d0e)


## thisIsNotTheFoxUrLookingFor | 2024-10-16T07:43:44+00:00
In just under 19 hours I have blocked > 75k requests from them haha
![image](https://github.com/user-attachments/assets/db12d6f1-c87b-4f27-a1fc-753dd9f3d4e7)


## thisIsNotTheFoxUrLookingFor | 2024-10-18T03:28:08+00:00
I keep playing whackamole with their proxies. Perhaps if we could impose some restrictions on computationally expensive RPC calls in a restricted node this would assist to resolve the issue? Also they are grabbing a tx list of tx in the mempool of every node, it looks like they are trying to observe tx as they propagate through public nodes.

They have a lot of IP addresses across a massive surface area of providers, could be a nation state actor or someone using a botnet of hacked devices.

I might just whack a password on my node for now, if people are using cake wallet they have a range of public nodes to use anyway by default or choosable in the wallet, probably no merit in allowing these actors to continually scrape our mempools (/gettransactions & /get_transaction_pool) to observe what tx we see.

## nahuhh | 2024-10-18T04:18:02+00:00
@thisIsNotTheFoxUrLookingFor  dont just add a password, make sure you disable `--public-node`.

You might want to set firewall rules and perhaps change the port

## thisIsNotTheFoxUrLookingFor | 2024-10-18T04:21:29+00:00
> @thisIsNotTheFoxUrLookingFor dont just add a password, make sure you disable `--public-node`.

Always it has been disabled. They are scraping `monero.fail`.

> You might want to set firewall rules and perhaps change the port

My node is behind cloudflare so I have some defence against them by utilising cf's WAF. I will play with them I don't mind it, waste their resources haha.

In the last 24hrs alone I have blocked 129k of their RPC requests
![image](https://github.com/user-attachments/assets/79107116-392f-4e6d-9570-f63b9c612f8d)




## IronicMeme | 2024-11-20T06:36:48+00:00
Hi all,
I was looking at my logs today and also had the same errors as @Jayd603 (mined block failed verification, transaction not found in pool)

As per discussion once I enabled log-level=1 I was able to see a number of peers submitting bad transactions as well as submitting blocks that failed verification.

Example of bad block submitted:

> 2024-11-20 06:17:35.263 I HTTP [37.111.231.231] POST /json_rpc
> 2024-11-20 06:17:35.263 I [37.111.231.231:9978 INC] Calling RPC method submitblock
> 2024-11-20 06:17:35.298 E Block with id: <a0bfa8d4e04e94904072ccb3ac25ab1e9208df83e8323f4685ba409e6c031fb3>
> 2024-11-20 06:17:35.298 E does not have enough proof of work: <a711bd3b9daa5dfcd8dc52e0a57ceb4d813226b03c558682f5bf9f12b0160000> at height 3285303, unexpected difficulty: 366131419123
> 2024-11-20 06:17:35.298 E mined block failed verification


Example of bad transaction:

> 2024-11-20 06:13:48.975 I HTTP [103.117.150.132] POST /json_rpc
> 2024-11-20 06:13:48.975 I [103.117.150.132:52881 INC] Calling RPC method getblocktemplate
> 2024-11-20 06:13:49.269 I HTTP [37.111.231.231] GET /getheight
> 2024-11-20 06:13:49.269 I [37.111.231.231:9938 INC] calling /getheight
> 2024-11-20 06:13:49.366 I HTTP [103.117.150.132] GET /getheight
> 2024-11-20 06:13:49.366 I [103.117.150.132:52423 INC] calling /getheight
> 2024-11-20 06:13:49.746 I [104.167.218.235:18080 OUT] 1559 bytes received for category command-2002 initiated by peer
> 2024-11-20 06:13:49.746 I [104.167.218.235:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
> 2024-11-20 06:13:49.746 I Including transaction <e42e78c6c3402717462184c9f071476587b40a8f79717b965b969c49f2b51638>
> 2024-11-20 06:13:49.751 I transaction unlock time is not zero: 8
> 2024-11-20 06:13:49.751 E Transaction verification failed: <e42e78c6c3402717462184c9f071476587b40a8f79717b965b969c49f2b51638>
> 2024-11-20 06:13:50.392 I HTTP [103.117.150.132] GET /getheight
> 2024-11-20 06:13:50.392 I [103.117.150.132:57113 INC] calling /getheight
> 2024-11-20 06:13:50.559 I HTTP [37.111.231.231] POST /json_rpc
> 2024-11-20 06:13:50.559 I [37.111.231.231:9939 INC] Calling RPC method getblocktemplate
> 2024-11-20 06:13:51.271 I [128.127.104.80:8287 OUT] 3778 bytes received for category command-2002 initiated by peer
> 2024-11-20 06:13:51.271 I [128.127.104.80:8287 OUT] Received NOTIFY_NEW_TRANSACTIONS (2 txes)
> 2024-11-20 06:13:51.271 I Including transaction <6bd5ae4cac8229889674053b2095abb57ad6bf192920dd51f711a749f291e704>
> 2024-11-20 06:13:51.272 I Including transaction <e42e78c6c3402717462184c9f071476587b40a8f79717b965b969c49f2b51638>
> 2024-11-20 06:13:51.305 I Transaction added to pool: txid <6bd5ae4cac8229889674053b2095abb57ad6bf192920dd51f711a749f291e704> weight: 2217 fee/byte: 20000, count: 22
> 2024-11-20 06:13:51.310 I transaction unlock time is not zero: 8
> 2024-11-20 06:13:51.311 E Transaction verification failed: <e42e78c6c3402717462184c9f071476587b40a8f79717b965b969c49f2b51638>
> 2024-11-20 06:13:51.358 I HTTP [103.117.150.132] GET /getheight
> 2024-11-20 06:13:51.358 I [103.117.150.132:33893 INC] calling /getheight
> 2024-11-20 06:13:51.608 I [193.142.4.2:18480 OUT] 3778 bytes received for category command-2002 initiated by peer
> 2024-11-20 06:13:51.608 I [193.142.4.2:18480 OUT] Received NOTIFY_NEW_TRANSACTIONS (2 txes)
> 2024-11-20 06:13:51.609 I Including transaction <6bd5ae4cac8229889674053b2095abb57ad6bf192920dd51f711a749f291e704>
> 2024-11-20 06:13:51.609 I Including transaction <e42e78c6c3402717462184c9f071476587b40a8f79717b965b969c49f2b51638>
> 2024-11-20 06:13:51.614 I transaction unlock time is not zero: 8
> 2024-11-20 06:13:51.614 E Transaction verification failed: <e42e78c6c3402717462184c9f071476587b40a8f79717b965b969c49f2b51638>


My questions are:
Will non-malicious peers submit bad blocks?
Will non-malicious peers submit transactions that can fail verification?

Would it be safe to assume that the peer using RPC requests to submit a mined block that is failing verification is malicious?

Thanks. Happy to provide more logs and examples if needed.

## IronicMeme | 2024-11-20T07:12:34+00:00
> It would be good to get more log data if anyone has any.

[monerod-2.log](https://github.com/user-attachments/files/17826567/monerod-2.log)

I'm yet to ban any IPs

edit: banned 2 IPs, (the ones in above post), and following this rabbit hole and have noticed I am receiving communications from the banned IPs in @Boog900's list (eg: 128.140.85.154)

## sullystuff | 2024-12-27T22:07:10+00:00
why not just remove public access of /gettransactions & /get_transaction_pool by default? I presume most, if not all, mining pools and solo miners are running their own nodes so that won't affect them at all, otherwise mempool scraping seems very very easy.

edit: and yes I am still seeing these messages on my nodes as well

## nahuhh | 2024-12-28T00:04:10+00:00
Rpc is private by default. If someone is using your rpc, its because you've allowed access to the internet

## sullystuff | 2024-12-28T06:39:57+00:00
> Rpc is private by default. If someone is using your rpc, its because you've allowed access to the internet

Sure, but I want to help the noobs as well if possible... looks like this might be doing more harm than good for the network; yet whitelisting those functions to private rpc only would be a huge help to the network, right?

# Action History
- Created by: Jayd603 | 2024-10-01T14:05:09+00:00
