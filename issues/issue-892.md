---
title: 'Seraphis wallet workgroup meeting #36 - Monday, 2023-09-11, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/892
author: rbrunner7
assignees: []
labels: []
created_at: '2023-09-08T14:31:16+00:00'
updated_at: '2023-09-11T19:47:44+00:00'
type: issue
status: closed
closed_at: '2023-09-11T19:47:43+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/889

# Discussion History
## rbrunner7 | 2023-09-11T19:47:43+00:00
```
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/892
<UkoeHB> hi, I came up with an adjustment to jeffro's jamtis modification proposal which I think is quite promising https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4688223#gistcomment-4688223
<UkoeHB> that's all from me :)
<r​brunner7> The modification of the modification :)
<r​brunner7> Thanks, koe. Nice to have you back, if even only for a short hello.
<r​brunner7> Really nobody else around, or is just my Matrix server not working correctly?
<rbrunner> Copy of my last Matrix message, maybe it's good for something: Really nobody else around, or is just my Matrix server not working correctly?
<j​berman> I'm here, hello. Background sync is still sucking me in unfortunately, I keep tinkering with it
<j​berman> Final PR is nearly fully drafted now, all tests written so should be back over to Seraphis work in the next day or so
<r​brunner7> Good to hear
<r​brunner7> In my Matrix client I have a number of peoples' icons on the left hanging up at a message from 20 minutes ago, like if not following. Strange.
<r​brunner7> Er, on the right
<r​brunner7> Just to deposit here while I am waiting anyway: Interesting question on Reddit, why not speeding up Seraphis development by adding a paid full time dev or two:
<r​brunner7> https://old.reddit.com/r/Monero/comments/16ewfkt/skepticism_sunday_september_10_2023/
<r​brunner7> I found it surprisingly difficult to describe to some outsider why that's quite difficult, and did not really try so far.
<r​ucknium> Search costs on both sides of the market.
<j​effro256> Hi !  Sorry I'm late
<r​brunner7> At least Matrix works ...
<r​brunner7> A summary of the many things you did recently, jeffro256 ?
<r​ucknium> Or maybe: the major part of the search cost can be paid by one of the two players. Neither player is willing to pay the cost, so...no deal! (The core is empty)
<j​effro256> base32 PR, base32 checksum PR, refining wallet2_basic, looking into optimizing the Jamtis changes,  & generally getting familiar with `seraphis_lib`
<r​brunner7> I will definitely have a look at your base32 PRs in the coming days.
<j​effro256> Thanks. One thing I was hoping for in terms of upstream development is when PR https://github.com/monero-project/monero/pull/8976 gets merged into the master branch of the core repo that seraphis_lib rebases against that, and then seraphis_wallet rebases against seraphis_lib. That should fix all the outstanding  compilation/testing errors
<j​effro256> Ukoe, I'm just now seeing your comment on the Jamtis gist
<j​effro256> So the idea is to do the extra derivation for normal scans only? Correct me if I'm wrong, but that's what is already done, no?
<j​effro256> Oh but you remove the 2-byte view tag?
<UkoeHB> the extra derivation (occurs after the address tag hint check
<UkoeHB> sorry the k_ua derivation occurs after address tag hint check *
<UkoeHB> in your proposal the second view tag encompasses both normal and self-send enotes
<UkoeHB> alternatively you could keep the second view tag and give it a special derivation path for self-sends
<j​effro256> In the gist comment, by the phrase "is no better than the remote scanner" are you talking about its ability to  deanonymize (b/c it would be faster I think)?
<j​effro256> Wait no it wouldn't be faster since it can't decipher address tags
<j​effro256> One thing I would like to know, is would it ever be viable to give away just the second view tag key to third-party servers (and let them filter out 1:65536 enotes)
<UkoeHB> not better or worse (although marginally more costly for the remote server, ~0.5%)
<j​effro256> jberman:  says probably not
<j​effro256> Even assuming that the tx volume will increase 256x
<j​effro256> So we could optimize for that scenario
<j​effro256> If we wanted to keep that option open, then we shouldn't do a seperate derivation path for self-sends on the second view tag
<UkoeHB> Even if it was, you are basically saying the 1-byte view tag has become useless bloat at that point. So you need to take a step back.
<UkoeHB> We should not design temporary measures into the protocol.
<j​effro256> The thing is though, if a 1-byte view tag is useless bloat, then the poor nodes will have to be supercomputers to keep up verifying everything
<j​effro256> Being able to reduce bandwidth by 256x I don't think will every be useless since the amount of work "cut" scales linearly with tx volume
<UkoeHB> I don't follow. In the case where you need a 2-byte filter, the 1-byte filter has become useless.
<UkoeHB> The 1-byte filter should always be useful.
<j​effro256> Okay it would maybe become useless for *some* devices. There could possibly be a spectrum of devices that require a 2 byte tag to keep up, and those who need only 1 byte, and those who will scan all enotes themselves.
<UkoeHB> You are just saying that all it takes is a little more scaling for the 1-byte tag to become useless on all devices.
<j​effro256> I'm saying that they could both be used simultaneously by different people with different use cases
<j​effro256> But if we didn
<j​effro256> *n't care about planning for that scenario, then we could do a custom derivation for the second view tag for self sends
<j​effro256> which would guard against people intentionally doxxing themselves somewhat but would hinder potential future use cases
<UkoeHB> I don't see what landscape would have people using both 1 and 2-byte view tags for assisted scanning.
<UkoeHB> Other than a marginal zone where both a viable
<r​brunner7> UkoeHB: Do I understand correctly, you are arguing towards a single view tag solution, which would be the new 2-byte view tag?
<UkoeHB> rbrunner: no
<r​brunner7> Ok then, I will read along ...
<j​effro256> For remote scanning, IMO by far the best performance benefit of assisted view tag scanning is the decrease in bandwidth. If you're in a scenario in which you have a mobile device in the middle of nowhere, and you get only tiny little trickles of bandwidth everyday from e.g. a sattelite, then maybe you want 2 bytes of view tag. At the same time, somebody in the city way want to hav<clipped mess
<j​effro256> e their mobile device with only 1 byte of view tag so it is usable on-the-go but they always have a pretty decent connection and 1-byte of view tag provides a good balance of privacy/usability for them
<j​effro256> If you keep the view tag computations independent from each other, then you can have different users doing both with the same address type
<j​effro256> What I think could mitigate this from a UX perspective is to have the seed phrase encode their choice of 1-byte/2-byte view tag from the very beginning. They don't have to use it, but if they do use it, then they can't use both without changing their seed phrase
<r​brunner7> Assuming there are both types of remote scanning services available. Which may turn into a problem.
<j​effro256> to be clear, I'm not currently advocating for anyone to use a 2-byte view tag service with today's tx volume
<j​berman> my preliminary thought is that it has the feel of premature optimization to me and adds complexity in significant sections of the protocol for too narrow a use case/scenario
<j​berman> (strictly as it relates to the addition of the choice between 2 byte and 1 byte view tags)
<r​brunner7> Ah, ok, because we can't just drop the 2-byte view tag and still have any privacy benefits, right? Everything is interlinked there.
<r​brunner7> The proposal is one whole package
<j​effro256> We could drop the 2-byte view tag, but that would make scanning much slower for little to no benefit. What we can't drop is the second DH derivation which is what gives the privacy benefits AND takes the most compute time. The 2-byte view just allows you to speed up scanning b/c if you already done the DH derivation, you might as well do a auick hash
<j​effro256> *quick
<j​effro256> I might need more time to think about what Ukoe posted on the Jamtis thread
<j​effro256> koe, would the proposed `k_rs` have its corresponding additional public  key in the address ?
<UkoeHB> We would retain the address tag hint if the second view tag were dropped.
<UkoeHB> The goal is to one way or another tie the second filter to the normal/self-send distinction.
<j​effro256> Yes ^ whether its address tag or view tag, if you remove the 2 byte MAC but still do a second DH derivation, you waste a lot of compute time for 2 byte smaller txs
<r​brunner7> Ok, this will anyway certainly continue for a while until everything is in place, beyond this discussion here right now. I have to go now, so allow me to close the meeting proper. Thanks everybody!
<j​effro256> Thank you
<j​effro256> Koe, with the modifications to the modifications, how would you filter out 1:65536 on-chain?
```


# Action History
- Created by: rbrunner7 | 2023-09-08T14:31:16+00:00
- Closed at: 2023-09-11T19:47:43+00:00
