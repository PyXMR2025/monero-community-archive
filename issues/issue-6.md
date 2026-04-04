---
title: Explaining simplified version of RingCT?
source_url: https://github.com/monero-project/research-lab/issues/6
author: kenshi84
assignees: []
labels: []
created_at: '2016-11-29T00:50:14+00:00'
updated_at: '2016-11-29T22:12:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After asking this question on [SE](http://monero.stackexchange.com/q/2551/506) and getting answer from Luigi pointing me to the [code](https://github.com/monero-project/monero/blob/83b05117310334cc000cbdeaeae6be57622f4fab/src/ringct/rctSigs.cpp#L399), I think I finally figured out how the simplified version of RingCT works, as in the note below (which is a modification to MRL-005):

https://www.overleaf.com/read/xyhymkfjfqmn

If my understanding is correct, shouldn't this be formally published under MRL?

My second question:
As I see it, each ring has a 2x(q+1) matrix containing pairs of (P,C), and also has 2 key images. I think the second key image corresponds to the commitment to zero, which seems unnecessary (we've already checked the double-spend with the first key image). Can't we skip the second key image to make the signature size even smaller?


# Discussion History
## luigi1111 | 2016-11-29T01:34:36+00:00
Yes the paper should be updated, I think. There may be some ASNL updates needed as well.

Note that the second key image is already elided, added (er, removed) by https://github.com/monero-project/monero/commit/c5be4b0beaaa7a703d4e2b84aa9f3c727bf992df

## kenshi84 | 2016-11-29T02:42:29+00:00
Thanks Luigi!

I really appreciate if you could answer my another question on [SE](http://monero.stackexchange.com/a/2844/506).

## ghost | 2016-11-29T20:22:37+00:00
>Yes the paper should be updated, I think. There may be some ASNL updates needed as well. 

Note that the ASNL were moved to an appendix sometime this summer in correspondence during the Ledger Journal Review, and finally removed from the paper in response to issue #4  . However I think the simplified version or other modifications would be more appropriate in their own writeup / blog post / whatever - that  change to the code was added by request of the monero dev community based on sybil-resistance concerns, and I personally prefer the full key matrix style due to efficiency. https://github.com/ShenNoether/MiniNero/blob/master/RingCT0.5_copy.pdf 

## luigi1111 | 2016-11-29T22:12:47+00:00
> However I think the simplified version or other modifications would be more appropriate in their own writeup / blog post / whatever

I think I agree with this.

For the ASNL stuff, maybe it makes sense to update the MRL document to match the more recent one, though I don't know if a procedure exists to do so. @fluffypony 

# Action History
- Created by: kenshi84 | 2016-11-29T00:50:14+00:00
