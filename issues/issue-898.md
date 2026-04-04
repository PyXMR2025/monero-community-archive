---
title: 'Seraphis wallet workgroup meeting #38 - Monday, 2023-09-25, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/898
author: rbrunner7
assignees: []
labels: []
created_at: '2023-09-22T16:59:55+00:00'
updated_at: '2023-09-25T19:24:42+00:00'
type: issue
status: closed
closed_at: '2023-09-25T19:24:41+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/895

# Discussion History
## rbrunner7 | 2023-09-25T19:24:41+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/898
<j​berman> hello
<d​angerousfreedom> Hello
<r​brunner7> Welcome to the usual suspects :)
<r​brunner7> What's there to report from last week?
<r​brunner7> I started to look at the `wallet2` file reading code from jeffro256 . Works well so far.
<d​angerousfreedom> I'm slowly starting to work on this list I made for a new ccs.
<d​angerousfreedom> I will finish cleaning up the transaction history when the dependencies are merged.
<r​brunner7> Is this the Base32 stuff?
<d​angerousfreedom> Should we make an 'issue tracker' to see what people is working on as suggested some time ago?
<d​angerousfreedom> Base32 and basic_wallet
<d​angerousfreedom> Should we make an 'issue tracker' to see what people are working on as suggested some time ago?
<r​brunner7> I am holding off a bit to start such a tracker. As already mentioned, such a thing can be a PITA to keep current ...
<r​brunner7> I think the point in time when we start to lose overview will be hard to miss.
<d​angerousfreedom> Ok
<r​brunner7> I hope that vtnerd will have a look soon at the requested review changes and signs off the Base32 PR.
<j​berman> I'm getting back to Seraphis work this week. Making one more change to the background sync PR then hoping to get a review on my general approach before knocking out the rest of the TODO's I shared in the PR, then moving back to Seraphis work. I shared an update on my CCS here: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/401#note_22435
<r​brunner7> I will try to find time to review that.
<j​berman> ty :)
<r​brunner7> Anything to discuss today?
<r​brunner7> From me a general remark that it may be worth to watch new issues and PRs closer. Things are picking up speed.
<dangerousfreedom> +1
<v​tnerd> rbrunner7: I can approve immediately, I thought I did this already but looks like I didn't
<rbrunner7> +1
<plowsof> I guess its worth mentioning that we've had a serious offer from zksecurity to work on the seraphis papers. Under a grant type basis where they explore this space for 1 month or so. Pricing is in the low 5 figures/week. theyre open to negotiate. 
<r​brunner7> First time I hear that name. Have a link?
<r​brunner7> We can of course repeat that in the coming MRL meeting.
<plowsof> This was the blog that brought them to our attention https://www.zksecurity.xyz/blog/posts/nova-attack/ (and other work) 
<r​brunner7> Ah yes, interesting article. I stumbled over that somehow as well.
<r​ucknium> plowsof: Do we have anything in writing from them? Scope declaration, etc?
<r​brunner7> Hmmm. A month with 5 figures per week is already some serious money.
<plowsof> Nothing concrete, just this https://gist.github.com/plowsof/8cb33e2efe4bf0239927ad3bd92326e0 (however jeffro256' / tevadors recent proposal would chamge the worl to be done) but theyve read that and also looked at the papers
<r​brunner7> Interesting. Maybe a good idea to discuss Wednesday, with UkoeHB around with a bit of luck.
<j​berman> The third bullet point would be blocked until the address spec is settled, but creating a formal security model would not be
<plowsof> (not looked at that recent proposal by jeff/tev*) but yeah, theyre interested. It would definitely be pricey but if theyre good, its like.. the future of monero depending on them finding vulnerabilities .. we can ofcourse compare/contrast with others. I know cypherstack is interested too. 
<r​brunner7> Yes, @Tevador and jeffro256 are still very busy at work polishing Jamtis
<r​brunner7> I didn't have much luck getting feedback about programming styles regarding character arrays and pointer arithmetic versus `std::string`. Seems it not very controversial :) https://github.com/seraphis-migration/monero/pull/7#issuecomment-1731527431
<r​brunner7> No feedback is also a feedback, in a way
<r​brunner7> By the way, that wallet file reading PR is something where more people testing = better. I already stumbled about an edge case where the .keys is written in ASCII instead of binary which is not yet supported.
<r​brunner7> I only had wallets ready back to 2018.
<plowsof> Rucknium ah, from them, no not yet, still need to tell them what we want .. thats why they leant toward a 1 month grant type situation to 'see where were at' at the end 
<d​angerousfreedom> Which one?
<r​brunner7> https://github.com/seraphis-migration/monero/pull/4
<plowsof> I can still ask*
<r​brunner7> The one you probably also depend on, as you said, reading transactions for your proofs, right?
<r​ucknium> Has zksecurity done anything before like we want them to do with Seraphis?
<r​brunner7> Maybe: https://www.zksecurity.xyz/#chat
<d​angerousfreedom> rbrunner7: Yeah, I would say I have tested enough for my application but I dont know the level of scrutiny thats expected :p 
<d​angerousfreedom> I will to look for some edge cases too but I believe it is enough for our necessities now. We can always modify it in the future when it is more used and definitely it will be. So expect it to be polished on the way
<r​brunner7> dangerousfreedom: Sounds reasonable. I will look a bit more at the code and probably merge within a week or so.
<dangerousfreedom> +1
<r​brunner7> I still wonder about the best way to mark "TODOs". We don't want to forget to add things later, and neither want we "TODO" comments that just get years old.
<plowsof> They where involved with " non-interactive mimblewimble transactions " eprint, if that is also any relavance. David wong os their head of security/confounder
<d​angerousfreedom> Thats a good question. Maybe an issue tracker or official TODO list would be good
<plowsof> Michelle orru* is on their team
<d​angerousfreedom> Opening issues on the wallet repo does not give an overview of the work to be done
<r​brunner7> Now they even want to have overview, ts ts ts
<r​brunner7> Do I have to know that Michelle?
<r​ucknium> Michele*
<r​brunner7> Is that a famous member of the cryptoscene?
<r​ucknium> This person? https://tumbolandia.net/
<r​brunner7> Interesting, thanks
<plowsof> Thanks Rucknium *autocomplete lied to me*
<r​brunner7> Lol
<r​ucknium> Orru looks _to me_ like a good person to help complete the Seraphis paper.
<r​brunner7> Some fresh blood, able to look at it from the outside, yes.
<r​brunner7> And who knows, maybe we can catch him and get him on board somehow for more than a review.
<r​ucknium> Isn't the scope not just review?
<r​ucknium> "Establish a formal security model"
<plowsof> Orru is "highly interested" 
<r​brunner7> Yeah, I see what you mean. But on the other side, only so many things have room in a month.
<plowsof> Iirc there is nothing to review until its completed xD
<r​brunner7> Yes yes. You can also review a design ...
<r​brunner7> Positive development, in any case.
<plowsof> Could even start in mid october* scope/funding pending ofcourse (unless they go retroactive on us)
<r​brunner7> That's a bit ambitious IMHO, if I look how financing through CCS progresses, but who knows
<r​brunner7> Alright, looks like we are complete for the meeting. Thanks for attending, read you next week at the latest.
<d​angerousfreedom> Thanks rbrunner7
````


# Action History
- Created by: rbrunner7 | 2023-09-22T16:59:55+00:00
- Closed at: 2023-09-25T19:24:41+00:00
