---
title: Running a monero node over tor
source_url: https://github.com/monero-project/monero/issues/4250
author: MarsAttacke
assignees: []
labels:
- invalid
created_at: '2018-08-12T14:09:24+00:00'
updated_at: '2018-08-12T19:57:40+00:00'
type: issue
status: closed
closed_at: '2018-08-12T19:48:53+00:00'
---

# Original Description
Hi guys, I have a security question to make my first sync : 
I'm following this guideline : 

https://medium.com/@kic0/running-a-monero-node-over-tor-49c3de49eda8


And on this step 

> After importing the blockchain.raw run monerod first time to make sure it syncs to latest blockheight we use some "Tor" options and a exclusive node to prevent "leakage". The node used here is node.xmr.pt:18081 an open node run by comunity members, you should really use your own or you can always run with none at all but be more "open" to the network, this is the least recomended "mode" tho.
>  
> While Monero isn't made to integrate with Tor, it can be used wrapped with torsocks, if you add --p2p-bind-ip 127.0.0.1 to the monerod command line. You also want to set DNS requests to go over TCP, so they'll be routed through Tor, by setting DNS_PUBLIC=tcp or use a particular DNS server with DNS_PUBLIC=tcp://a.b.c.d (default is 8.8.4.4, which is Google DNS). You may also disable IGD (UPnP port forwarding negotiation), which is pointless with Tor, we also add --hide-my-port so we don't anounce our node to the network itself. To allow local connections from the wallet, you might have to add TORSOCKS_ALLOW_INBOUND=1, some OSes need it and some don't...


With this command : 


> DNS_PUBLIC=tcp://8.8.4.4 TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod — p2p-bind-ip 127.0.0.1 — no-igd — add-exclusive-node 80.172.224.52 — hide-my-port

If I'm right use the 80.172.224.52 ip to sync is not very secure and I think I miss something, I tried to use 127.0.0.1 but error message when I launch it....

Could anyone explain to me if it's dangerous to use the 80.172.224.52 ip to sync or not ? and If yes they said that we have to use our own node but how ? (Is it with my onion adress created before ? 

Thanks for reading and helping ;)


# Discussion History
## moneromooo-monero | 2018-08-12T16:58:07+00:00
If you think this node is an attacker, you can select another one, like one of the seed nodes (though since you select an exclusive node, you might already have deemed those bad).
"Use your own node" is for wallet use. You can't bootstrap a node from no other node.

## MarsAttacke | 2018-08-12T18:30:06+00:00
Hm yea but can I put my own node thats I just create instead of this public node ? 

In this command that I run on my computer who is the node : 

> 
DNS_PUBLIC=tcp://8.8.4.4 TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod — p2p-bind-ip 127.0.0.1 — no-igd — add-exclusive-node **80.172.224.52** — hide-my-port

I don't want to use this eclusive node but my own...

Don't known if I'm clear...



## moneromooo-monero | 2018-08-12T18:47:24+00:00
If you want to sync off another node of yours, then:
- set its IP instead
- if it's on a local net, don't use tor (it's unclear whether "but my own" means just "my own" or "also local")

I'm not sure how familiar you are with Tor, but the Tor network will only allow you to connect to servers that are accessible via the internet.

## MarsAttacke | 2018-08-12T18:56:34+00:00
not very familiar...

> After importing the blockchain.raw run monerod first time to make sure it syncs to latest blockheight we use some "Tor" options and a exclusive node to prevent "leakage". The node used here is node.xmr.pt:18081 an open node run by comunity members, you should really use your own

In that part they said that in this exemple they use node.xmr.pt:18081 , an open node node run by the community.
But for sec reason it's better to run my own but how ? 

## moneromooo-monero | 2018-08-12T19:41:28+00:00
You're apparently trying to run your own, so you're good. Your own node will connect to other nodes in the network, that's fine. Whether you choose one single other node or not is your choice, but if you select a single one, then your node can be hoodwinked. I'd drop the exclusive node option unless you  have a specific reason for it.

Anyway, this is a bug tracker, not a help desk.

+invalid


## MarsAttacke | 2018-08-12T19:57:40+00:00
Ok thanks for your reply and sory to disturb.

# Action History
- Created by: MarsAttacke | 2018-08-12T14:09:24+00:00
- Closed at: 2018-08-12T19:48:53+00:00
