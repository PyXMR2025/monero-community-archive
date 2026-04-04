---
title: Issue with proof of unforgeability of ASNL
source_url: https://github.com/monero-project/research-lab/issues/4
author: RandomRun
assignees: []
labels: []
created_at: '2016-10-22T21:28:24+00:00'
updated_at: '2017-01-06T22:44:39+00:00'
type: issue
status: closed
closed_at: '2017-01-06T22:44:38+00:00'
---

# Original Description
In the proof it is assumed, by contradiction, that there exists an adversary _A_ that is able to forge the ASNL, but later on something much stronger is assumed, namely that _A_ somehow knows the discrete logs of _L_-values to be numbers _a_ and _b_. I don't see how that could be implied by _A_'s ability to produce a forged signature. Isn't it possible that _A_ has a way to produce _L_\- and _s_-values that form a valid signature without knowing the discrete log of the _L_'s? If so, the proof shouldn't use the numbers _a_ and _b_.  


# Discussion History
## ghost | 2016-10-25T17:13:34+00:00
Hi, the paper states that it is a sketch of a proof (mainly it's a sketch because the things are no more efficient than the Borromean ones which are mentioned could be used on a previous page, and possibly less efficient according to the Borromean paper, in some cases (e.g. higher bases than 2 or whatever, and I guess at the time of writing the Borromean paper didn't have a proof written out, but it was sort of publicly in progress on their github, so the author didn't want to sort of steal possibly a big chunk of their paper).

Anyway, I think the point in assuming the 'a', 'b' values is that since various other bits of information are determined by the (edit: non-standard terminology from the Borromean paper) one-way nature of the hash (since you have to produce L1, L2 before knowing c1, c2) then at the end you need to find a scalar 's' so would need some way to get a scalar from the other bits of information which are already determined at that point). Moving sG by itself, it is easier to find an 's' when you already know a,b, so presumably if you can't find 's' with that advantage, then you can't find 's' without the advantage. But- this section of the paper hasn't been reviewed much, and it is just a sketch, so let me know if you see an error in that. BTW, the author e-mail is apparently not provided at the paper, so one might assume they are not open to correspondence, however, it's sort of publicly known from their github (shen.noether@gmx.com) which is linked on the first page of the paper, so I would assume they are open to correspondence for this type of question.


## ghost | 2016-10-26T06:33:36+00:00
2p: Since I'm no longer actively working on this stuff- the Monero community could try and get someone to audit- off the top of my head there is NCC crypto services or coinspect. For example, I think Zcash recently did an audit with the first of the two. I can name bugs that have been found in almost every big crypto thing that I can think of off the top of my head, so I wouldn't be too unsurprised if I wasn't immune. 


## ghost | 2016-11-01T22:24:35+00:00
I previously noted that there was a flaw in my previous comment- and that one needs to commit to the L1 values. After working this change through on paper, I realized that doing this essentially reduces to the Borromean sigs in any case (after replacing the sum with a hash of the L1)


## ghost | 2017-01-02T00:28:44+00:00
It's probably worth noting, that shortly after this thread first appeared, there was a (I think reasonable) offer setup for a crypto audit between one of the organizations in the previous comment, and Riccardo / Othe of the monero project. I'm not sure whether the monero guys followed through, but it would be nice to hear the results of that.

## ghost | 2017-01-04T18:48:25+00:00
I would like to point out that there is now a thread claiming I completed a 'deep code review' on reddit. I tried to comment there and point out this is untrue (I fixed a small piece of the borromean sigs, and compared the hash to point function with OWS recent implementation), but the comment got shadow-deleted or something.

## RandomRun | 2017-01-06T05:39:07+00:00
Hi Shen. Thank you for setting the record straight on this thread. Could you please provide the link to the Reddit thread and your comment, if possible? I couldn't find it there. If something like that was deliberately deleted that is very concerning on its own right...

## fluffypony | 2017-01-06T05:51:34+00:00
It was censored by Theymos! Quick everyone, let's head to /r/btc!

/s

## ghost | 2017-01-06T06:19:08+00:00
@RandomRun https://unreddit.com/r/Monero/comments/5lyw05/funding_required_shen_noether_for_work_on_ringct/

## taushet | 2017-01-06T21:40:36+00:00
...so why was that comment deleted? @fluffypony

## fluffypony | 2017-01-06T22:44:38+00:00
@taushet because the comment was so out of bounds, and Shen hadn't contacted myself or othe privately, that it was a safe assumption that his account had been compromised. At this stage I'm still assuming his account has been compromised and am disregarding anything he has said publicly.

# Action History
- Created by: RandomRun | 2016-10-22T21:28:24+00:00
- Closed at: 2017-01-06T22:44:38+00:00
