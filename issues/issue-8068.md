---
title: 转出时 如果需要找零，那找零地址是每次使用一个新地址 还是找零到固定地址？？
source_url: https://github.com/monero-project/monero/issues/8068
author: miles-zhangdy
assignees: []
labels: []
created_at: '2021-11-18T06:42:47+00:00'
updated_at: '2021-11-29T17:27:18+00:00'
type: issue
status: closed
closed_at: '2021-11-29T17:27:18+00:00'
---

# Original Description
转出时 如果需要找零，那找零地址是每次使用一个新地址 还是找零到固定地址？？

# Discussion History
## selsta | 2021-11-18T07:22:47+00:00
English please, otherwise it will be difficult to help :)

## selsta | 2021-11-18T07:23:43+00:00
Google translate:

> If you need change when you transfer out, does the change address use a new address every time or change to a fixed address? ?

## miles-zhangdy | 2021-11-18T08:05:20+00:00
> Google translate:
> 
> > If you need change when you transfer out, does the change address use a new address every time or change to a fixed address? ?

Yes, just want to ask this

## XfedeX | 2021-11-18T22:16:17+00:00
> 
> 
> Google translate:
> 
> > If you need change when you transfer out, does the change address use a new address every time or change to a fixed address? ?

DeepL translates a little bit better:
`When transferring out, if change is needed, should I use a new address each time or should I change to a fixed address?`
For better privacy you should use a different address for each payment, however using the same one will work.
Just to be curious, isn't crypto banned in China?

## miles-zhangdy | 2021-11-19T02:22:24+00:00
> > Google translate:
> > > If you need change when you transfer out, does the change address use a new address every time or change to a fixed address? ?
> 
> DeepL translates a little bit better: `When transferring out, if change is needed, should I use a new address each time or should I change to a fixed address?` For better privacy you should use a different address for each payment, however using the same one will work. Just to be curious, isn't crypto banned in China?

Yes, just want to ask this

## trasherdk | 2021-11-19T16:53:13+00:00
On the basic level, diving into the hole anonymously thingy. The protocol of this, our thing, protects the leak of the sender address, and the receiver address. So, the operational security has been left up to you. There has been some efforts, trying to obfuscate, what traffic comes out. That Sech, the privacy dude, might have some input. If you want to be anonymous on the internet, it's up to you. There is a few options open, but I have no experience with your challenges.

## SamsungGalaxyPlayer | 2021-11-29T17:25:29+00:00
This seems like a support / documentation request, so this issue can be closed.

To answer the question, change addresses can really be anything since they aren't publicly viewable. That said, users should be cautious of the possibility that the receiving counterparty may be watching change outputs as poisoned outputs. So make sure to read up on poisoned outputs for strict threat model cases. Using different accounts or seeds for change may facilitate output hygiene. The vast majority of users don't need to worry about this however.

# Action History
- Created by: miles-zhangdy | 2021-11-18T06:42:47+00:00
- Closed at: 2021-11-29T17:27:18+00:00
