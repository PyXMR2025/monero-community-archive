---
title: Hosting seed node
source_url: https://github.com/monero-project/monero/issues/3425
author: fengshuicoin
assignees: []
labels: []
created_at: '2018-03-17T21:09:26+00:00'
updated_at: '2022-03-16T15:35:36+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:35:36+00:00'
---

# Original Description
Hey guys not so much an issue as a how to. How can i host a monero seednode? For crytonote networks i could just use forknote and direct to conf file. How do we do this with monero. Thanks for reply. 

# Discussion History
## SamsungGalaxyPlayer | 2018-03-17T22:17:13+00:00
This is a bug and update tracker, not a help desk. Try your luck at [StackExchange](https://monero.stackexchange.com).

## fengshuicoin | 2018-03-17T22:21:38+00:00
Seems like fundamental bug not having any docs on this. Why wouldnt it be
provided to grow network. More nodes the better?

On Sat, Mar 17, 2018, 15:17 SamsungGalaxyPlayer <notifications@github.com>
wrote:

> This is a bug and update tracker, not a help desk. Try your luck at
> StackExchange <https://monero.stackexchange.com>.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3425#issuecomment-373956919>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Ah8Oa1AGYFSsvyWozU9EiHDWm76F_Ym7ks5tfYtygaJpZM4Su9z9>
> .
>


## moneromooo-monero | 2018-03-17T22:36:29+00:00
If you intend to host one for the long term (several years), and you can have a fixed IP, and are willing to update when required, then you just run a normal monero node, and make a patch to add its IP to get_seed_nodes in src/p2p/net_node.inl. Having a testnet node too would be helpful, but not required. For these, you should idle in #monero-dev to know when an update is required.

However, it's not clear whether we want that or not, given seed nodes could be malicious. We'll discuss this.

## fengshuicoin | 2018-03-17T22:43:50+00:00
Thanks for your reply. I have resources and availability to do so.
Cheers bro its guys like you that help move things forward and continue
advancements. Is it possible to have binary similar to forknote? Then its
less resources for having to make on server. Maybe i can make on labtop and
just transfer binaries to server and just install debs.

On Sat, Mar 17, 2018, 15:36 moneromooo-monero <notifications@github.com>
wrote:

> If you intend to host one for the long term (several years), and you can
> have a fixed IP, and are willing to update when required, then you just run
> a normal monero node, and make a patch to add its IP to get_seed_nodes in
> src/p2p/net_node.inl. Having a testnet node too would be helpful, but not
> required. For these, you should idle in #monero-dev to know when an update
> is required.
>
> However, it's not clear whether we want that or not, given seed nodes
> could be malicious. We'll discuss this.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3425#issuecomment-373957952>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Ah8Oa9VMIiXlGjSjERjzTAQwavV_3pbvks5tfY_1gaJpZM4Su9z9>
> .
>


## moneromooo-monero | 2018-03-17T22:48:57+00:00
Monero evolves fast, so I'm not sure forknote works for it. You'd have to ask slbb.

## moneromooo-monero | 2018-03-18T18:43:39+00:00
There's been some discussion, some people are for, some people against. anonimal will write some ideas on how to address potential maliciousness from seed nodes.

## selsta | 2022-03-16T15:35:36+00:00
See for example: https://github.com/monero-project/monero/pull/8216

# Action History
- Created by: fengshuicoin | 2018-03-17T21:09:26+00:00
- Closed at: 2022-03-16T15:35:36+00:00
