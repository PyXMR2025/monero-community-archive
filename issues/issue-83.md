---
title: Moneropedia - Mix-in
source_url: https://github.com/monero-project/monero-site/issues/83
author: palexande
assignees: []
labels: []
created_at: '2015-12-13T05:12:49+00:00'
updated_at: '2017-04-20T08:07:02+00:00'
type: issue
status: closed
closed_at: '2017-04-20T08:07:02+00:00'
---

# Original Description
Need to add this term to Moneropedia.  Unknown if anybody is working on this term.  I can add it if nobody else is.  


# Discussion History
## SamsungGalaxyPlayer | 2016-12-28T13:11:18+00:00
Seconded. Newcomers often have questions about mixins, and it is a good idea to clarify the difference between Monero's use of mixins and mixing/tumbling services.

## SamsungGalaxyPlayer | 2017-01-08T16:41:49+00:00
Can we adapt the definition from [Bitcointalk](https://bitcointalk.org/index.php?topic=753252.msg9985441#msg9985441) and use what's below?

The mixin count refers to the number of other signatures (aside from yours) in the ring signature that authorizes the transaction. A default mixin of 4 means that there are 5 total signatures. Someone looking at a transaction with a mixin of 4 has no way of knowing which of the five signers is the true sender.

A higher mixin number will typically provide more privacy than a lower mixin number because it will provide a greater amount of plausible deniability. However, reusing an odd, recognizable mixin for your transactions will make your transactions stand out.

The GUI allows users to select a mixin between 4 and 25. The CLI allows users to select any value permitted by the network.

## palexande | 2017-01-12T09:15:46+00:00
Alright, I'll see what I can do.

## jonathancross | 2017-04-07T20:05:31+00:00
Hi @palexande Are you still working on this?

## palexande | 2017-04-08T01:22:00+00:00
I wanted to wait a bit and see how the ring size term turned out.  Looks like it has been updated?

## palexande | 2017-04-20T08:07:02+00:00
I'm closing this issue since it looks like ring-size is now being used fairly universally now.

# Action History
- Created by: palexande | 2015-12-13T05:12:49+00:00
- Closed at: 2017-04-20T08:07:02+00:00
