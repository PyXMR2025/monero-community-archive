---
title: 'Monero Tech Meeting #164 - Monday, 2026-04-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1366
author: rbrunner7
assignees: []
labels: []
created_at: '2026-04-03T14:19:12+00:00'
updated_at: '2026-04-06T19:08:53+00:00'
type: issue
status: closed
closed_at: '2026-04-06T19:08:53+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1360).


# Discussion History
## rbrunner7 | 2026-04-06T19:08:53+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1366
<s​needlewoods> Hi
<j​effro256> Howdy
<UkoeHB> hi
<v​tnerd> Hi
<r​brunner7> Alright, on to the reports. jberman cannot attend, reported before the meeting that last week was mostly reviews for him.
<v​tnerd> Updated lws+lwsf to match the changes to carrot. Also updated the pr for zmq to fcmp++-stage
<s​needlewoods> apart from review comments in regards to [#10378](https://github.com/monero-project/monero/pull/10378) I mainly worked on fixing functional tests with the new wallet-rpc
<UkoeHB> Me: distracted by personal matters last week. This week looking at a hackerone report and will actually finish carrot_core review.
<j​effro256> Me: wrote Keccak256 and Ed25519 field operations in Slang, a shader language , and pushed operations to a GPU using Vulkan. Just doing unit testing right now, not performance testing . At some point I wanna test the performance of the ECDH using precomputed points, the view tag check, and the amount commitment recomputation
<sneedlewoods> +1
<r​brunner7> Just to relax a bit from all that hard C++ and Rust coding I guess :)
<r​brunner7> So that's in a "proof of concept" phase right now
<r​brunner7> and I guess may still fail
<j​effro256> Yeah absolutely , there's been a lot of talk over the years about scaling Monero validation by using the GPU . Will be interesting to see if its feasible in real life
<j​effro256> But could definitely flop too
<r​brunner7> I think this will be closely watched in some circles!
<selsta> not sure if this meeting is also for new releases but we are making good progress on v0.18.5.0
<selsta> it will only contain bug fixes but a lot of them so I deemed it worthy of a larger release
<r​brunner7> Thanks for the news, selsta, good to hear. What's the main attraction of that release?
<s​needlewoods> +1
<r​brunner7> Absolutely.
<r​brunner7> Ok, if we are already through with the reports, I have a question, that I think jeffro256 will be able to answer easily: Is there already an implementation / PR of the 'wallet2' and maybe also 'account' classes that support and handle the new Carrot key hierarchy? I was suspecting this first, but could not find a smoking gun inside yet: https://github.com/seraphis-migration/monero/pull/52
<r​brunner7> And I was wondering how it will turn out if 3 parties or even more will make changes at the same time in the wallet classes, SNeedlewoods for their rewrites, jeffro256 and jberman for Carrot and FCMP++, and I myself for Polyseed support.
<r​brunner7> Wondering whether we can do something in the direction of project management to minize conflicts.
<r​brunner7> *minimize
<j​effro256> The crypto is implemented , and most of the supporting code in carrot_core and carrot_impl , respectively . But it is not integrated into wallet2
<j​effro256> That hot / cold PR supports the old key hierarchy in CARROT/FCMP++
<r​brunner7> I see
<j​effro256> What kind of conflicts do you for see?
<r​brunner7> Do you see yourself going on and putting Carrot support into `wallet2`?
<s​needlewoods> I rarely touch wallet2 and a while ago I based my Wallet API work on some fcmppp branch and there wasn't too many conflicts
<s​needlewoods> for testing*
<r​brunner7> Mostly repeated rebases and merge conflicts. But anyway, I guess the answer is that not much can be done except just "letting it run". For example, we can't predict the order things will get merged.
<jeffor256> +1
<j​effro256> At some point if it is popular
<r​brunner7> What do you mean with "popular"?
<j​effro256> Well, technically , CARROT support is already fully in there
<j​effro256> But I haven't integrated support for the new *key hierarchy*
<r​brunner7> Isn't that a pretty fundamental piece of support?
<j​effro256> Depends on if you want to use the new key hierarchy or not
<j​effro256> You don't need to
<j​babb> I do :)
<jeffro256> +1
<r​brunner7> Now I am confused. We all want to have the option for sure, no?
<j​effro256> We can ship CARROT/FCMP++ without the new key hierarchy
<j​effro256> That's what the stressnet is doing rn
<r​brunner7> Yeah, I know that technically we can, but the thought to actually *do so* really never crossed my mind ...
<j​effro256> I mean yes, I want people to have the option
<j​effro256> But there's the UX issue of how to introduce that option to users
<j​babb> With recent discussions re: adding some Jamtis features to CARROT, the propspect of delaying the new key hierarchy makes more sense to me
<r​brunner7> I think jberman made a list somewhere what everything is still on the way to the Carrot and FCMP++ hardfork. IMHO "support for new Carrot key hierarchy" absolutely belongs there.
<r​brunner7> Josh Babb: Good point. Hopefully those discussions can start soon.
<j​babb> I previously would've wholeheartedly agreed on that, rb, but it seems if we take that path that we may end up with 3 key hierarchies unless I misunderstand
<j​babb> I mean: if we rush to make CARROT available now, it seems we'll end up with users on the legacy path, CARROT, and then eventually Jamtis or similar
<j​babb> am I misunderstanding that?
<r​brunner7> I think this possibility is on the table. But anyway, I wouldn't call the introduction of the new Carrot key hierarchy "rushed". The Carrot "paper" is out for many months, and I think also reviewed.
<jbabb> +1
<j​babb> of course, poor wording.
<UkoeHB> I will do my best to finish up carrot_core today or tomorrow and get jamtis feature discussion going asap.
<j​babb> a spoonful of Jamtis makes the CARROT go down...
<r​brunner7> People might vote for dropping all non-PQ related research and dev work after the FCMP++ hardfork, so next thing might be a PQ Jamtis that is not yet fully worked out ...
<j​pk68> Just my two cents: I think the need for quantum-resistance is a good argument for releasing Carrot as it is, because it can happen sooner. It does provide something in terms of forward-secrecy
<jbabb> +1
<rbrunner7> +1
<j​effro256> Maybe , but I kind of always thought that that may be the best path: have an option for "blending in" with old users with tons of functionality (new hierarchy in CARROT spec), only missing a couple points. Then a full address scheme which doesn't try to be backwards compatible and really packs all the features and gives users a hard break (JAMTIS, maybe with PQ encryption)
<jpk68> +1
<jbabb> +1
<j​pk68> Forgive me if I got a few details wrong ;)
<r​brunner7> Yes, we don't have a lack of possible future paths, we have a bit too many :)
<UkoeHB> Ok instead I will start prepping the discussion now and finish carrot_core review after :)
<r​brunner7> That sounds like a good idea to me
<r​brunner7> I think that experience shows it anyway takes quite some time until the "wallet app ecosystem" catches up with new capabilities in the Monero core software. Right now I think we should make the new Carrot key hierachie in some form available already together with the FCMP++ hardfork. But that's to discuss of course, with more info on the table.
<jeffro256> +1
<jbabb> +1
<jpk68> +1
<s​needlewoods> as a user I'd also like to see the new Carrot key hierarchy together with FCMP++
<jpk68> +1
<j​babb> agreed, and I should be clear that I just prefer that we see if CARROT can get some more Jamtis features in it before the HF.  I wouldn't want to delay it if that can't happen in a timely fashion
<UkoeHB> Imo if more features are added, they don’t need to be fully supported immediately. Including the key hierarchy. Just need enough to match the the existing wallet api.
<r​brunner7> Agreed. If we can get in more before the hardfork, that would be terrific, and we should take the chance. Depends on the trade-offs, however.
<j​effro256> Okay I'll consider moving the timeline up for the new hierarchy integration
<r​brunner7> Would be good to know details about what that would take, certainly.
<r​brunner7> Another subject: Where do we stand regarding supporting hybrid wallets or not? I guess we won't easily get any more comments on the corresponding issue ...
<r​brunner7> And what is there looks like a "loose consensus" to not support to me. Not sure how other people look at this.
<jbabb> +1
<j​pk68> I am clearly far from the most qualified to talk about this, but I really don't think we should keep delaying the hardfork. People are getting pretty impatient and the fact that it could be Q3/Q4 is already kind of alarming
<r​brunner7> Of course that's connected with new hiearchy integration
<j​pk68> This was discussed on the last episode or two of MoneroTalk
<r​brunner7> You mean hardfork timing?
<r​brunner7> That would be pretty "outside" view ...
<j​pk68> I was adding onto my previous comment, apologies
<r​brunner7> Say again, *what* was discussed there?
<UkoeHB> Delays seem more to do with mispredicted timelines than things being pushed back. I predicted it would take this long back when the first CCS showed up.
<r​brunner7> UkoeHB: I agree. We are on our way, not really wasting time or doing unnecessary things. A little bit of progress every week.
<j​pk68> General dev/research news (as seen from whatever's posted on Twitter) is/was discussed; the fact that the hardfork could be delayed again is evidently a cause of frustration for a number of people
<UkoeHB> @jeffro256: most important is that wallets can construct txs properly for all supported address formats. Generating new wallets and providing APIs for new features can safely wait for future updates if needed.
<j​pk68> I am aware that hard timelines were never really given, but it seemed that the hardfork date would most likely be announced around the time of MoneroTalk
<r​brunner7> *MoneroTopia?
<j​pk68> Yes, sorry :)
<j​pk68> I am aware that hard timelines were never really given, but it seemed that the hardfork date would most likely be announced around the time of MoneroTopia
<UkoeHB> "the fact that the hardfork could be delayed again" No one has proposed delaying for carrot changes, although you are right it is theoretically possible.
<jpk68> +1
<j​pk68> My point is, it has already taken quite a long time (not that there's anything wrong with that), and I just feel like delaying it yet again would be a bad idea
<r​brunner7> If/when we discuss inlcuding some additional Jamtis or Jamtis like features into Carrot, time to implement and deploy will certainly play a role in discussions - among other things.
<jpk68> +1
<r​brunner7> Let's see how things look at next week's meeting then.
<r​brunner7> Alright, do we have to discuss something else today?
<v​tnerd> Yeah adding features this late ... Yikes
<j​pk68> As rbrunner said last week... a bird in the hand is worth two in the bush ;)
<r​brunner7> Isn't that a true and tested strategy in IT? :)
<r​brunner7> Ok, we are nearing the hour, and it seems we are through for today. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everybody
<UkoeHB> thanks
````


# Action History
- Created by: rbrunner7 | 2026-04-03T14:19:12+00:00
- Closed at: 2026-04-06T19:08:53+00:00
