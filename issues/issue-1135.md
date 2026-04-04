---
title: 'Monero Tech Meeting #102 - Monday, 2025-01-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1135
author: rbrunner7
assignees: []
labels: []
created_at: '2025-01-03T07:40:21+00:00'
updated_at: '2025-01-06T18:38:48+00:00'
type: issue
status: closed
closed_at: '2025-01-06T18:38:47+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1132).

# Discussion History
## rbrunner7 | 2025-01-06T18:38:47+00:00
````
<<rbrunner7>> Meeting time. Hello in the brand new year! https://github.com/monero-project/meta/issues/1135
<sneedlewoods> Hello
<jberman> waves
<rbrunner7> jeffro256: Now :)
<rbrunner7> So, what do you have to report from last week?
<sneedlewoods> Replied here https://github.com/monero-project/monero/pull/9368
<sneedlewoods> This is a small first step towards the new API: #9308
<sneedlewoods> Else I haven't had much time this week and only worked on small details.
<sneedlewoods> I don't really know how to continue at the moment, so I'd propose to double check the entire PR and if I don't find anything obvious that I missed I'll put it into ready to review!?
<sneedlewoods> I've been wondering, would this be a good time to squash, or when do you usually squash?
<rbrunner7> I looked over all the changes accumulated in your PR here: https://github.com/monero-project/meta/issues/1135
<rbrunner7> I didn't see anything that I would change.
<sneedlewoods> wrong link!?
<rbrunner7> Oh, yes, of course: https://github.com/monero-project/monero/pull/9464
<sneedlewoods> +1
<jeffro256> Hi
<rbrunner7> Yeah, if you sort of "release" it for review, why not squash?
<jberman> me: Integrated torsion check into tree building, tested the faster sync from genesis, pushed code, then started on integrating FCMP++ prove
<gatsby> +1
<syntheticbird> +1
<rbrunner7> +1
<jberman> Continuing on this branch: https://github.com/j-berman/monero/commits/fcmp%2B%2B-tree-sync-dev
<jeffro256> Implemented internal messaging in Carrot, did blinding factor switch commitment tests, and close to finishing the fast X25519 key exchange 
<sneedlewoods> I thought the commits may be useful to refer to in some cases, but they're also a small hassle to work with
<rbrunner7> I would be glad to get more opinions on that reordering PR #9368 linked above, so we can, after some months passed, either pushing it towards merge or else closing it.
<rbrunner7> jeffro256: What do you mean with "internal messaging" in Carrot?
<jeffro256> In Carrot, when sending change back to yourself with the new key hierarchy, your basically get 16 bytes of free data to do whatever with. You can use this for transaction memos, data attestation, etc. I just added it to the API 
<rbrunner7> Encrypted of course
<jeffro256> Yes, it is encrypted by default to your view-balance key, but if you were doing memos, you'd want it to be encrypted to some other key derived from the sender-receiver secret 
<rbrunner7> And will you go as far as adding a dummy change back if no normal change would result but people insist on adding a memo?
<jeffro256> I didn't actually add code for memos, but a general API for putting arbitary data in internal self-send anchor fields 
<jeffro256> The memo is orthogonal to the change amount. You can have an internal selfsend with 0 change and no memo, some change and no memo, 0 change and a memo, or some change and a memo
<rbrunner7> I guess these 16 bytes are there anyway for some reason? You did not add them only for this feature?
<jeffro256> Yes they're required for normal outgoing transfers to mitigate Janus attacks and small subgroup attacks
<rbrunner7> Nice
<jeffro256> But we can't remove them for internal self-sends otherwise that would convey to observers that this enote is an internal selfsend 
<jeffro256> And payment ID confirmation
<rbrunner7> I guess Carrot and QC will be a subject in this week's MRL meeting, so two more days of tension :)
<rbrunner7> I still have to read up about turnstiles and such stuff ...
<jeffro256> Yeah there's a lot of different tradeoffs to consider 
<jeffro256> It's a huge problem space 
<jeffro256> Kind of like Seraphis/FCMP++ design a few months ago
<jeffro256> It will probably eventually converge on something most people are happy about, but it's a lot 
<sneedlewoods> I appreciate you putting in so much effort
<rbrunner7> sneedlewoods: Don't you have a quite long list of things you stumbled over when looking at the existing Wallet API code, and resulting questions? Maybe some points there would be worth looking at more closely already while waiting for review results?
<rbrunner7> Probably the changes would be stuff for follow-up PRs however
<jeffro256> Thanks! I appreciate you jumping into the deep end with the wallet2 nastiness ;) It's a formidable piece of code to change
<jberman> +1
<sneedlewoods> Good idea, will have to look into it myself again, it has been a while https://github.com/SNeedlewoods/seraphis_wallet/issues/1
<rbrunner7> You are on this stuff for many months already, how time flies :)
<rbrunner7> Alright, do we have something special to discuss today beyond these reports?
<rbrunner7> Doesn't look like it, so I think we can close already. Thanks for attending everybody, read you again next week!
<sneedlewoods> thanks everyone, cu next time
<jeffro256> Thanks everyone!
````


# Action History
- Created by: rbrunner7 | 2025-01-03T07:40:21+00:00
- Closed at: 2025-01-06T18:38:47+00:00
