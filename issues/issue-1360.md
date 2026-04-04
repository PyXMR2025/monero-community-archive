---
title: 'Monero Tech Meeting #163 - Monday, 2026-03-30, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1360
author: rbrunner7
assignees: []
labels: []
created_at: '2026-03-27T18:42:35+00:00'
updated_at: '2026-03-30T19:04:21+00:00'
type: issue
status: closed
closed_at: '2026-03-30T19:04:21+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1357).


# Discussion History
## rbrunner7 | 2026-03-30T19:04:21+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1360
<jbabb> +1
<s​needlewoods> Hi
<j​pk68:matrix.org> Hello
<s​yntheticbird> Hi
<v​tnerd> Hi
<UkoeHB> Hi
<j​effro256> Howdy
<j​berman> *waves*
<j​babb> doing well thanks, howdydo?
<r​brunner7> Alrigh, plenty of people today, nice. What are your reports from last week?
<s​needlewoods> `grep "\<m_wallet\>" src/wallet/wallet_rpc_server.cpp -c` returns 0
<s​needlewoods> Now focus is on functional_tests, find and fix bugs not covered by tests, clean up code and notes
<s​needlewoods> Also just posted a final report on my [current CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/634#note_35515) and began to write a [new CCS proposal](https://paste.debian.net/hidden/561205b1)
<r​brunner7> I myself wanted to continue to work on Polyseed, but did not find the necessary free time ...
<UkoeHB> Reviewing carrot_core. Pointed out some limitations of the PQ turnstile design to jeffro256.
<j​berman> me: completed the monerod hang-on-exit PR and submitted it ( https://github.com/monero-project/monero/pull/10382 ), various FCMP++ integration cleanup / upstream monerod cleanup tasks
<sneedlewood> +1
<UkoeHB> Next, will write an issue advocating for more jamtis features now instead of later. Won’t do any other work on it without strong buyin.
<r​brunner7> Not sure I understand. You mean if your proposals don't find strong support you are ready to move on from Carrot into other topics?
<UkoeHB> Yes, either review carrot_impl or start on multisig.
<j​effro256> Me: talking to Koe about CARROT/Jamtis, talking to vtnerd about LWS, reviewing H1 issues, talking to auditors about the FCMP++ integration, talking to Ledger about HW development, rebased the knowledge proofs PR and working on completing the remaining tasks
<s​yntheticbird> do you happen to take your breath in between ?
<r​brunner7> Just curious anyway, what is an example for one of the Jamtis features that you would want Carrot to learn, UkoeHB?
<UkoeHB> rbrunner7: encoded address index + filter-assist key
<j​pk68:matrix.org> Any success with contacting Trezor?
<r​brunner7> Ah, ok. I remember quite vidid discussions about Seraphis indexes, probably without ever reaching a clear consensus :)
<j​pk68:matrix.org> I can't remember if you said you emailed the dev or the company :)
<j​berman> btw sgp_ is about to do an audit blitz reaching out to some more candidates soon, would be good to coordinate comms
<UkoeHB> Mostly complaints about adding bytes.
<j​effro256> I emailed the company a few months ago, but they never really followed up until someone else who had personal connections poked them about it recently, very grateful
<jpk86> +1
<UkoeHB> It sounds like mx25519 has not been touched by any audit. jberman/jeffro256 can you work it into the audit cycle?
<j​effro256> ^ My previous comment is about Ledger. Trezor said that they would forward it to a product manager and never got back
<j​berman> I liked the address indexes and filter-assist key. I'm open to re-opening a discussion on them, with strong emphasis on still ensuring FCMP++ launches within a timely manner
<r​brunner7> I wonder what their lead development times would be to be fully ready with a new FCMP++ capable firmware when we hardfork.
<j​effro256> I think mx25519 would be a good candidate for the optional follow-up PR which covers the more complex wallet-specific crypto like the point checking by fast halving
<j​berman> mx25519 seems like a good candidate to be reviewed in an isolated audit by auditors proficient in C & crypto
<j​effro256> At the least, basically anyone can verify that `mx25519` hits the standard test vectors for X25519 and doesn't use branching in the assembly
<j​effro256> Fair
<j​effro256> They need to be proficient in assembly though mainly
<j​berman> true, yes
<UkoeHB> Are the text vectors considered adequate for validity?
<j​berman> seems a marginally distinct skillset enough to warrant a distinct audit
<j​berman> edit out the marginally*
<r​brunner7> Could that mean another Carrot "crypto" review if we change anything non-trivial like indexes and/or another key like that?
<j​effro256> There's an x64 impl, an x64 with mulc/adc extensions impl, an ARM64 impl, and a portable C impl.
<jberman> +1
<j​effro256> UkoeHB: IDK, so I would leans towards "no"
<UkoeHB> rbrunner7: likely yes
<jberman> +1
<j​effro256> But it's a baseline test for completeness
<r​brunner7> I see. But could heavily build on what already happened there review-wise, I guess
<j​effro256> Yes
<UkoeHB> If there’s buy-in, I will write a PR on carrot_core with the changes so the full scale can be more accurately seen. But let’s wait until the points in favor are laid out.
<j​effro256> Ukoe makes really good arguments for basically shifting the new key hierarchy into Jamtis, but I am personally against it for the moment, especially if we go for hard separation in issue https://github.com/seraphis-migration/monero/issues/306. Perhaps I could write up an issue showing pros and cons of both
<r​brunner7> Just wanted to ask whether  anybody see a benefit if we discuss h306 here today, or do we just let that collect comments and votes for some time more :)
<UkoeHB> Not sure how many other contributors have not commented
<r​brunner7> I think jberman is the most prominent there
<j​berman> I meant to write up a comment, but I'm still pretty strongly in the camp of hard separation. I think tevador's arguments strenghthend the argument for separation and I was already for separating
<j​berman> (as did rbrunner's)
<r​brunner7> So maybe a short comment from you will already do, do make your mark clearly in a place that is visible also to people who don't follow meetings and discussions here
<j​berman> I will
<j​berman> jeffro256: I'm curious if you have some cons top-of-mind rn on bringing in the address index + filter-assist key
<r​brunner7> The new comments from jeffro convinced me that on the side of the the implementation on the side of core wallet code the hybrid scheme can work, and we would probably able to pull it through, but that does almost nothing to diminish my fears of potential chaos in the wallet apps
<UkoeHB> sneedlewoods_xmr also
<r​brunner7> Right, I think so far there is only a "like" from them somewhere, but no comment
<r​brunner7> Ok, looks like we just come back to this next week, and then we can maybe chat about how to reach something like a "loose consensus" on this
<s​needlewoods> yes, I +1'ed rbrunner, not sure if I have anything worth to add
<UkoeHB> +1
<r​brunner7> Cannot fail to remark that heavy "pro" votes are somewhat lacking ...
<j​effro256> Cons against adding address index + filter assist key is mainly two things. One, the added complexity to the addressing protocol which is already complicated. And two, the privacy implications of having people be on two completely separate distinguishable address formats. Most users probably won't be using the filter-assist tier, and would get the main benefits of the new key hierarchy without needing a change in address format. Also, the main benefit of address indexes I think is lost if one changes the way that they scan, in such a way that they can save all txs which may potentionally belong to them. Think of background scanning, but even more selective.
<r​brunner7> There would be a need of change of address format?
<r​brunner7> Like in "public Monero addresses"
<j​berman> ahhh right new filter-assist tier requires a new key pair ya?
<j​berman> so addresses would be longer too
<jeffro256> +1
<j​effro256> Yes, adding address indicies + filter-assist requires a new 8 byte field and 32-byte elliptic curve point in the address, respectively
<j​berman> So there's no way of incorporating the new address index without making the new address indistinguishable from old either
<j​effro256> Not that I know of
<r​brunner7> Hmmm ... that seems to go against one of the core achievements of Carrot, at least as I see them, that addresses magically don't have to change to still get solid benefits
<UkoeHB> The PQ scheme will do that anyway, it’s inevitable with current plans. Now is better than later for racing against adversaries.
<r​brunner7> Yes. But might be some years out, I guess?
<UkoeHB> Ok my argument is weak * in any case, GitHub is better for laying out the case.
<j​berman> I figured even Carrot addresses won't work in a fully PQ scheme
<r​brunner7> Yes, that proposal of Tevador which seems quite concrete already has longer addresses, do I remember correctly?
<j​effro256> What do you mean by "fully" PQ?
<r​brunner7> I think there is it: https://github.com/monero-project/research-lab/issues/151
<j​berman> A scheme that includes PQ key exchange
<jeffro256> +1
<j​berman> (but is not limited to)
<UkoeHB> Yes, the change would be moving new features from PQ scheme to now, and then PQ would just add PQ. So there’d be two address changes instead of one, but the features would be now instead of later (or never).
<r​brunner7> Could develop into interesting trade-offs then :)
<r​brunner7> Let's see whether our decision processes will be able to cope with those ...
<j​effro256> As for the address distinguishability problem, there is an argument is Koe's favor towards "ripping the bandaid off" now if we plan to support Jamtis later. Since if the new key hierarchy already exists and is used, then Jamtis is implemented, the only people who would really need to move to Jamtis would be the filter-assist light wallet users. Then one can categorize a Jamtis user as *probably* a filter-assist user
<jbabb> +1
<UkoeHB> Filter assist or using random address generation (assuming 16 byte indices). Or enterprise with advance index usage.
<UkoeHB> rag might be favored by the most privacy conscious.
<j​effro256> Yup
<UkoeHB> Which really covers the two biggest camps: mobile and privacy focused
<j​berman> Personally I think the con of new distinguishable address is a legitimate con that does weigh in to my calculation here pretty solidly (especially when weighed together with keeping a sane timeline for FCMP++)
<j​berman> I do think there will be support to incorporate it once we have no choice to migrate to a new distinguishable address type
<j​berman> These features were relatively popular when it was discussed / proposed for Seraphis + Jamtis
<r​brunner7> I am quite unsure here. I just looked up the English translation of a famous German saying and found "a bird in the hand is worth two in the bush". That what comes to my mind right now with all those wonderful things that we could implement, but maybe should not, to protect a sane timeline
<s​yntheticbird> this
<s​yntheticbird> I just don't have technical arguments but gosh its how i felt
<r​brunner7> Alright, I hope people will find time soon to lay out things clearly in some GitHub issues, so people can look at that and "meditate" over it
<j​berman> I also do strongly favor advancing PQ research after FCMP++/Carrot
<j​berman> so it's not like a hand wavy thing
<j​berman> I think that's a critical direction
<r​brunner7> So that could maybe start earlier if we finish early with the hardfork to FCMP++ :)
<r​brunner7> Alright, let's see how proposals and opinions here develop further over the coming week.
<r​brunner7> Anything left for this very meeting?
<s​needlewoods> not for this meeting, but would appreciate some feedback on this PR https://github.com/monero-project/monero/pull/10378
<s​needlewoods> what are your opinions on:
<s​needlewoods> a) Should `get_tx_proof`, `get_spend_proof` & `get_reserve_proof` get restricted? I didn't see a good reason to do so.
<s​needlewoods> b) Should `relay_tx` get restricted? I'm leaning towards no, because even though it's a "state-changing" command, you can't really do anything with it without getting the raw tx from an unrestricted wallet-rpc (or some other unrestricted wallet) first, AFAICT.
<s​needlewoods> c) In [10271](https://github.com/monero-project/monero/pull/10271) it was argued that there is no privacy loss in allowing `get_transfers` & `get_transfer_by_txid`, because `get_tx_key` is unrestricted anyways. I did restrict it in my PR, do you think it should stay unrestricted?
<r​brunner7> Alright, will try to find time to have a look
<r​brunner7> So it looks like we can close for today. Thanks everybody for attending, read you again next week!
<s​needlewoods> Thanks everyone, good meeting, cu
<U​koeHB> Thanks
````


# Action History
- Created by: rbrunner7 | 2026-03-27T18:42:35+00:00
- Closed at: 2026-03-30T19:04:21+00:00
