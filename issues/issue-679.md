---
title: '[feature request] Simplify display of confirmations'
source_url: https://github.com/monero-project/monero-gui/issues/679
author: jonathancross
assignees: []
labels:
- feature
created_at: '2017-04-16T12:59:56+00:00'
updated_at: '2019-04-27T10:55:13+00:00'
type: issue
status: closed
closed_at: '2019-04-27T10:55:13+00:00'
---

# Original Description
After a transaction receives the suggested 10 confirmations, the user is not left with a clear sense that this is now safe / complete.

It would be nice to see a checkmark (or another visual indicator) marking the tx as "confirmed" with the actual number of confirmations added to the "Transaction Details" modal along with "BlockHeight". Could optionally show the number of confirmations on mouseover.

This would allow us to reduce the noise on the main list by removing "BlockHeight".

Thoughts?

# Discussion History
## medusadigital | 2017-04-20T08:19:47+00:00
i like the idea.
also in the same spot is this: https://github.com/monero-project/monero-core/issues/200

so the whole section probably needs a slight redesign. 

having something visual to show the confirmations (maybe in form of a clock that fills up like in bitcoinQT) would sure be nice. 

however, we shouldnt start working on this before having at least some draft of how things should look like. 

if its worth it or if the overall redesign of the whole application should be pushed, that needs to be discussed.

removing blockheight probably wont be possible, since the main sorting is happening there (and the timestamp cant be used)

## jonathancross | 2017-04-20T11:10:48+00:00
> having something visual to show the confirmations...

Yeah, this would be great.

> removing blockheight probably wont be possible, since the main sorting is happening there (and the timestamp cant be used)

Good point.  But why can't the timestamp be used?


## medusadigital | 2017-04-20T11:52:55+00:00
> Good point. But why can't the timestamp be used?

becasue timestamps are set by the miners and can be slightly off:

![timestamps](https://cloud.githubusercontent.com/assets/17108301/25229288/f37b16ec-25cf-11e7-9171-3a03311b0460.png)


also its much easier to test, since the same default sorting applies in the CLI wallet. 

also, we just had issues with the sorting in the past and just chose the easy route due to time pressure: https://github.com/mbg033/monero-core/issues/70




## dEBRUYNE-1 | 2017-08-09T13:26:12+00:00
+feature

## jonathancross | 2017-08-11T20:21:51+00:00
Thanks for explaining @medusadigital... strange that times they can be so far off.
I need to research how a miner can set a UTC timestamp that is **_earlier_** than the previous block.  I'd expect this to be rejected.

## selsta | 2019-04-27T00:02:28+00:00
The history page looks like this now:

<img width="1092" alt="Screenshot 2019-04-27 at 01 59 34" src="https://user-images.githubusercontent.com/7697454/56841777-1cd7e100-6890-11e9-8d06-5e05355f276f.png">

@jonathancross Do you consider this resolved?

## jonathancross | 2019-04-27T10:55:13+00:00
Yes, thanks!

# Action History
- Created by: jonathancross | 2017-04-16T12:59:56+00:00
- Closed at: 2019-04-27T10:55:13+00:00
