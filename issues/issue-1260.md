---
title: Proposal to change "view only wallet" to "revenue only wallet"
source_url: https://github.com/monero-project/monero-gui/issues/1260
author: bitlamas
assignees: []
labels: []
created_at: '2018-04-04T14:20:38+00:00'
updated_at: '2018-04-04T15:33:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Usually in computer software you understand `view only` or `read only` as the access to read the content of a file in its entirety, but without any means of modifying, moving, deleting, or interacting in any other way.

Monero, being a software itself, could follow the same principles. At this moment the GUI wallet offers an option to create a `view only wallet`. In this wallet one would believe that, as other computer software, one has the access to read the content of a wallet without modifying or using the money in there. But to the user's surprise, that is not the case (and this is noted nowhere).

The `view only wallet` is actually a "revenue only wallet". In this version of the wallet you can only see incoming transactions, but not outgoing. This instantly kills the reason why a normal user would create a view only wallet: to be able to check its real funds without being able to spend them. This could be probably a reality for parents who create wallets for their kids; or just someone who created a "savings wallet" and wants to check the balance from time to time without being able to spend them. Now imagine in the latter scenario that an user is using a view-only wallet and his seed gets compromised in some way (safe is robbed, etc). The user would not see the theft until the day he recovers the actual wallet. I feel like this is a design problem. The current used nomenclature gives a false impression that you will be able to "view" everything.

So the reason for this kind of wallet to exist is to facilitate business owners and related positions to easily share with other entities the incoming transactions, a.k.a the revenue that they had for that specific wallet. In this case I suggest changing the name from `view only wallet` to `revenue only wallet` in the next release.

The name view only wallet should be kept for when (and if) Monero supports the possibility of creating a full view-only wallet where the user can see both incoming and outgoing transactions. If this will never happen, then the name should never be used.

# Discussion History
## dEBRUYNE-1 | 2018-04-04T15:10:51+00:00
>In this version of the wallet you can only see incoming transactions, but not outgoing.

Fwiw, you can see outgoing transactions (and thus a proper balance) after you've imported the key images. Therefore, I don' t think it's prudent to rename the view-only wallet. 

## bitlamas | 2018-04-04T15:19:03+00:00
> you can see outgoing transactions (and thus a proper balance) after you've imported the key images. 

You're correct, but this results in two different situations:

1. The user has to do an extra step and import the key images to have a _real_ "view-only wallet". This becomes very cumbersome if you're not the only person managing the wallet, or if you're actually monitoring a third-party wallet (e.g. your kid's wallet).

2. In the event where the seed gets compromised by a third-party, the user of the view-only wallet will never know the funds are not there anymore, until he restores the seed himself.

My issue isn't with the feature, it's with the name. The name **implies** certain capabilities and access that are simply not true in a native, default level, requiring extra steps that are not necessarily convenient for the average user. Without mentioning the scenarios where the actual wallet is not in the possession of the person who's monitoring it. I don't think everyone using this feature understand what it really means. I'm not a complete computer illiterate and took me a few search engine searches before I understood why my balance wasn't being updated in the view-only wallet.

## 1337tester | 2018-04-04T15:33:52+00:00
Agree with @curumimxara , 'read-only' was evoking quite some different expectations, just after creating one -> being confused -> doing research could I understand what's the matter.

# Action History
- Created by: bitlamas | 2018-04-04T14:20:38+00:00
