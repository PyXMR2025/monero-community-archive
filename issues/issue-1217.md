---
title: Monero Research Lab Meeting - Wed 04 June 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1217
author: Rucknium
assignees: []
labels: []
created_at: '2025-06-03T20:18:59+00:00'
updated_at: '2025-06-12T23:18:48+00:00'
type: issue
status: closed
closed_at: '2025-06-12T23:18:48+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [zkSecurity quote for review of Elliptic Curve Divisors for FCMP](https://hackmd.io/@rotn/HyyFGZcfxl) in parallel to [Cypher Stack review](https://github.com/cypherstack/divisor_deep_dive).

4. Subnet deduplication in peer selection algorithm to avoid spy nodes. [Draft research bulletin](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf), [implementation PR](https://github.com/monero-project/monero/pull/9939).

5. Web-of-Trust for node peer selection.

6. Any other business

7. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1213 

# Discussion History
## Rucknium | 2025-06-05T21:54:29+00:00
Logs

> __< r​ucknium:monero.social >__ MRL meeting in this room in about one hour.     

> __< r​ucknium:monero.social >__ kayabanerve: ^ Remind of the meeting at 17:00 UTC today     

> __< k​ayabanerve:matrix.org >__ I am aware :) Thank you     

> __< s​yntheticbird:monero.social >__ also kayaba if you see this, please answer jeffro in lounge     

> __< k​ayabanerve:matrix.org >__ FYI, the github issue says the 3rd. I noticed when I checked it for the time :p     

> __< r​ucknium:monero.social >__ Oh. Thanks     

> __< r​ucknium:monero.social >__ Fixed :)     

> __< c​haser:monero.social >__ reputational harm didn't stop Veridise from rushing their work, producing questionable proofs and not noting the core problems with Eagen's work     

> __< d​iego:cypherstack.com >__ Hey guys. I'm a stupid.     

> __< d​iego:cypherstack.com >__ Its not 70 XMR. Its 175.     

> __< d​iego:cypherstack.com >__ https://libera.monerologs.net/monero-research-lab/20250402#c515638     

> __< d​iego:cypherstack.com >__ https://gist.github.com/kayabaNerve/3a32eb393a41f48fe7c183c31dc57680     

> __< s​yntheticbird:monero.social >__ 🤏 almost     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1217     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< s​yntheticbird:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< a​rticmine:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ We have been greeted by a larger bill :D     

> __< v​tnerd:monero.social >__ Hi     

> __< s​gp_:monero.social >__ hello     

> __< 0​xfffc:monero.social >__ hi everyone     

> __< rbrunner >__ Hello     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< s​yntheticbird:monero.social >__ A deserved one neitherless     

> __< v​tnerd:monero.social >__ Hi     

> __< j​effro256:monero.social >__ Howdy     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< rbrunner >__ I could make a PR, ready for review, for the improved peer selection with less connections to spy nodes: https://github.com/monero-project/monero/pull/9939     

> __< r​ucknium:monero.social >__ me: Pushed draft version 0.3 of the MRL research bulletin on subnet deduplication to reduce spy node effectiveness: https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf . boog900 is reviewing it and once done, will be added as a co-author.  Also working on our/my MoneroKon presentations.     

> __< a​rticmine:monero.social >__ I am working on the scaling for FCMP+ The consensus part is done. The fees node relay part I expect to have next week.     

> __< j​berman:monero.social >__ me: continuing on FCMP++ / Carrot tests, ran into some snags / identified things to fix in wallet behavior     

> __< j​effro256:monero.social >__ Finally making some real progress on HW device stuff and hot/cold stuff now that I've gotten the major carrot_impl rework out of the way. Also been trying a bit to debug issues that people have sent in     

> __< d​iego:cypherstack.com >__ Auditing my own finances apparently.     

> __< 0​xfffc:monero.social >__ Addressing the PR comments. Have been off for few days. Will be part time for a few days more. I have already decided and sketched out what to do about the comments. I just have to wrote the code.     

> __< v​tnerd:monero.social >__ Me: looking at LWS stuff: why /get_random_outs was crashing on osx, and LWS push/truncated tx history stuff     

> __< r​ucknium:monero.social >__ 0xfffc: The PR you are referring to is the more efficient tx propagation implementation, right?     

> __< 0​xfffc:monero.social >__ Yes     

> __< b​randon:cypherstack.com >__ Fixing eagen's calculus mistakes     

> __< 0​xfffc:monero.social >__ https://github.com/monero-project/monero/pull/9933     

> __< r​ucknium:monero.social >__ 3) zkSecurity quote for review of Elliptic Curve Divisors for FCMP in parallel to Cypher Stack review. https://hackmd.io/@rotn/HyyFGZcfxl  https://github.com/cypherstack/divisor_deep_dive     

> __< r​ucknium:monero.social >__ surae: Maybe I could take a look at the calculus. Probably I would be little help, but there is a small chance.     

> __< k​ayabanerve:matrix.org >__ My comment from a day ago is still my primary response to immediate questions.     

> __< s​gp_:monero.social >__ Hey all, I believe that this SoW for a third reviewer of divisors is in the best interest of the Monero community. I would ideally like to get preliminary approval to pursue this contract     

> __< r​ucknium:monero.social >__ This one?     

> __< r​ucknium:monero.social >__ > zkSecurity is underestimating, has lower standards, see something not prior seen, or truly just have a domain expert. I'll note the divisors technique, without proofs, has been incorporated into a major paper by cryptographers who presumably believe it tracks. Obviously, the issue is the security proofs, but as zkSecurity's estimate is non-binding, payment is an acceptable flat <clipped message     

> __< r​ucknium:monero.social >__ rate, and the seemingly worst case is we get another set of security proofs CS still doesn't find up to standards, I'm in favor.     

> __< b​randon:cypherstack.com >__ Pretty sure we landed on the correct verification equations but more review is better     

> __< r​ucknium:monero.social >__ Cypher Stack staff should feel free to comment on this issue     

> __< s​gp_:monero.social >__ This project will aim to remove blockers preventing Monero from using the more efficient divisors technique. As stated in the SoW, it is fixed rate and requires sufficient proof to be delivered. I will work out the final payment details and any other suggested SoW modifications based on the feedback provided during this meeting and prior to this meeting     

> __< r​ucknium:monero.social >__ Where would the funds come from for the zkSecurity work?     

> __< s​gp_:monero.social >__ I am asking for a donation from the research CCS     

> __< b​randon:cypherstack.com >__ More review is better. I am not familiar with the current proposal for review on the table so I can't speak about it. If the reviewers at zksecurity are trustworthy and competent then great. It would be a shame to spend money on people who regurgitate substandard previous work though.     

> __< k​ayabanerve:matrix.org >__ Yes, Rucknium     

> __< r​ucknium:monero.social >__ Here's a list of what has to be funded with the remaining FCMP research CCS funds: https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/     

> __< s​gp_:monero.social >__ the reviewers are Mathias Hall-Andersen and Diego Aranha     

> __< k​ayabanerve:matrix.org >__ MHA is a coauthor of curve trees.     

> __< r​ucknium:monero.social >__ AFAIK, the FCMP research CCS has 897 XMR remaining.     

> __< r​ucknium:monero.social >__ These items have a combined cost of 75,000 USD: Gadgets formal verification, Gadgets impl audit, Circuit impl audit     

> __< s​gp_:monero.social >__ I also confirm 897     

> __< s​gp_:monero.social >__ after CS is paid the 175     

> __< c​haser:monero.social >__ By my calculations, 897 XMR (currently valued at ~$294 000). https://cryptpad.fr/sheet/#/2/sheet/view/7aKf7Z2rxNnMLJhx2cvkPH8nMbJcHilMoz3vKf+Q+oQ/embed/     

> __< j​berman:monero.social >__ Note that remaining funds tally currently doesn't include the 175xmr to CS. Expected balance is 897.13 including that     

> __< r​ucknium:monero.social >__ These don't have an estimated cost yet, AFAIK: GSP impl audit, EC Divisors impl audit, Towering curve cycle audit     

> __< r​ucknium:monero.social >__ ^ AFAIK, those are code audits, not mathematical reviews of the cryptographic soundness of the protocol.     

> __< s​gp_:monero.social >__ according to my notes, EC divisors is the same as towering curve cycle     

> __< j​berman:monero.social >__ Presumably we may also have non-divisors reviewed academically (?) and audited     

> __< s​gp_:monero.social >__ Veridise gadgets/circuits should be shared this week (if not today)     

> __< r​ucknium:monero.social >__ The zkSecurity quote is 50,000 USD for one week of work by two researchers. Previously, proposed work by zkSecurity to formalize Seraphis was 10,000 USD per week of work (presumably by one person): https://libera.monerologs.net/monero-research-lab/20230927#c284121     

> __< k​ayabanerve:matrix.org >__ We have the gadgets verification, impl audit, and circuit audit under our last quote with Veridise.     

> __< k​ayabanerve:matrix.org >__ cc SGP_ if MAGIC has drawn those XMR yet.     

> __< s​gp_:monero.social >__ MAGIC has received that donation already     

> __< d​iego:cypherstack.com >__ fwiw guys, our divisors work is going pretty smoothly. It's a lot of work, but we're making good time.     

> __< s​pirobel:kernal.eu >__ is it possible to get them to agree to a partial payment upfront sgp_ ? so they have an incentive to put in the extra mile?     

> __< k​ayabanerve:matrix.org >__ EC divisors lib audit and towering curve cycle lib audit are two items, but both had optimized impls scoped into the contest with audits scheduled for those optimized impls     

> __< b​randon:cypherstack.com >__ I wanted to be done today but alas     

> __< s​gp_:monero.social >__ I will specifically propose 50-50 payment for zkSecurity     

> __< k​ayabanerve:matrix.org >__ In that case, Rucknium, those items had a combined cost.     

> __< s​yntheticbird:monero.social >__ surae blink twice if you are held hostage     

> __< rbrunner >__ This is what does somehow not square for me, as already ranted yesterady: How zkSecurity can propose 2 person weeks for something Cypher Stack already spent many weeks on, and is not yet finished     

> __< s​gp_:monero.social >__ I know when valued at a weekly rate, $50k is a lot. But so long as the understanding is that they truly will ensure that we will get a fully finished deliverable that meets our requirements, then $50k is worth it imo     

> __< r​ucknium:monero.social >__ surae: Diego Salazar Maybe you don't want to say quite yet, but is the divisors work going in the direction of "it is sound", or in the direction of "it is unsound"?     

> __< j​effro256:monero.social >__ sgp: Towering curve cycle refers to the Helios/Selene pair of curves that we use, plus the technique which allows our curve, ed25519, to plug into that cycle. EC divisiors is a technique under review for FCMPs which is more-or-less "internal" to the membership proof. Even if we don't use divisors, we will always need a curve cycle for FCMPs     

> __< d​iego:cypherstack.com >__ Sound.     

> __< j​berman:monero.social >__ Hm, if CS is close to producing another divisors deliverable, perhaps it makes sense to hold on zkSecurity until that deliverable     

> __< b​randon:cypherstack.com >__ Yeah     

> __< d​iego:cypherstack.com >__ If things take a terrible turn for the worse, you all would be the first to know pretty quick.     

> __< b​randon:cypherstack.com >__ Except     

> __< b​randon:cypherstack.com >__ There are mistakes     

> __< f​reeman:cypherstack.com >__ Hello yes I would like 50k for one week of work, thank you     

> __< b​randon:cypherstack.com >__ The correct verification equations we have derived already     

> __< r​ucknium:monero.social >__ So you will write new proofs and those proofs have to be reviewed by yet another firm, probably     

> __< k​ayabanerve:matrix.org >__ I did check with surae regarding proximity and they did not recommend delaying the zkSecurity quote, and here encouraged more review.     

> __< b​randon:cypherstack.com >__ Okay so let me explain a little bit more in detail     

> __< o​frnxmr:monero.social >__ rbrunner some people underestimate their time so they can claim that their rates are high. So "1 week = 50k = our rate, even if its really 4 weeks. At best, we make 50k in a week. at worst, we can tell people that our going rate is 50k/week"     

> __< r​ucknium:monero.social >__ Does the protocol need to be altered, a little, to make it sound?     

> __< k​ayabanerve:matrix.org >__ Freeman: please email hello⊙cc and I'm sure they'll sort you out :)     

> __< j​effro256:monero.social >__ Sorry if you've already answered this question, sgp,  but is there anything specific to your knowledge that ZKSecurity will do differently (or specific expertise) that will result in a different outcome as CS?     

> __< f​reeman:cypherstack.com >__ https://matrix.monero.social/_matrix/media/v1/download/cypherstack.com/EOuiawmkasyiwspvsykDwbOb     

> __< b​randon:cypherstack.com >__ 1. The Eagan paper had some calculus mistakes which we have corrected.     

> __< b​randon:cypherstack.com >__ 2. Due to those mistakes the verification equations implemented by kayaba are not correct     

> __< r​ucknium:monero.social >__ IIRC, at time MRL has had multiple mathematical reviews and/or code audits done by different firms, for the same protocol.     

> __< b​randon:cypherstack.com >__ 3. Modifying the code to be correct will require further later review. And as kayaba says checking my proofs will also require further review     

> __< s​gp_:monero.social >__ It is primarily their different way of approaching the problem based on their different experiences     

> __< r​ucknium:monero.social >__ Does this mean that the FCMP competition coders are coding for the wrong target? I wonder how much of an effect that would have. https://www.getmonero.org/2025/04/05/fcmp++-contest.html     

> __< k​ayabanerve:matrix.org >__ Allegedly, until you demonstrate a full proof forgery on a 180 MHz pentium with 8 MB of RAM to prove it's practical /s     

> __< r​ucknium:monero.social >__ Answered by surae. Thanks.     

> __< b​randon:cypherstack.com >__ With this in mind, it seems to me like paying for ZK security to review. The current implementation is not necessarily a good usage of funds. I am biased because I work for cypher stack obviously. if the community wants to pay for this, then...     

> __< k​ayabanerve:matrix.org >__ (obviously, I joke, and the version of the equations proven secure will be the ones moved forward with)     

> __< k​ayabanerve:matrix.org >__ Rucknium: No impact if we keep divisors.     

> __< b​randon:cypherstack.com >__ If this money is going to be spent anyway, and if I had a perfect world, then I would recommend that these researchers start reviewing what I've been writing     

> __< s​yntheticbird:monero.social >__ Ig we can rejoice that there are no contester that manage to achieve the contest goal. Otherwise the ethical "should we pay them despite being insecure" question would have arrived     

> __< b​randon:cypherstack.com >__ This would land us on a correct protocol faster rather than recreating wheels over and over again with reviews     

> __< j​effro256:monero.social >__ Helios/Selene will almost certainly remain the same to my knowledge. Divisors won't, however, if we don't go with divisors..     

> __< k​ayabanerve:matrix.org >__ and the divisors lib included doesn't include the verification equations, hence why "no impact if we keep divisors"     

> __< b​randon:cypherstack.com >__ But that library is constructing proofs for the old verification equations     

> __< b​randon:cypherstack.com >__ Those proofs won't pass the correct verification equations     

> __< b​randon:cypherstack.com >__ So that code will still need to be modified?     

> __< b​randon:cypherstack.com >__ So that code will still need to be modified.     

> __< b​randon:cypherstack.com >__ Sorry voice to text is killing me today     

> __< k​ayabanerve:matrix.org >__ No, that lib is solely calculating divisors.     

> __< r​ucknium:monero.social >__ SyntheticBird: `Otherwise the ethical "should we pay them despite being insecure" question would have arrived`: IMHO, there is no question. Of course they should be paid because MRL/Core made that promise. The mistake is MRL's fault on going forward without 100% certainty.     

> __< k​ayabanerve:matrix.org >__ Does your modified verification statements still require I calculate a polynomial which I refer to as a divisor?     

> __< k​ayabanerve:matrix.org >__ If yes, then that lib is drop-in regardless.     

> __< s​yntheticbird:monero.social >__ That was my opinion as well     

> __< k​ayabanerve:matrix.org >__ The formatting for use in a ZK proof, and verification statements, is a separate lib entirely     

> __< a​ntilt:we2.ee >__ so compo may not be altered ?     

> __< b​randon:cypherstack.com >__ Yes and that interpolation code will not require modification     

> __< k​ayabanerve:matrix.org >__ Right, so this divisors lib in contest scope won't so long as that statement holds true     

> __< b​randon:cypherstack.com >__ I didn't realize the extra comps were separated, that's good. That means kayabas witness construction code is fine     

> __< j​effro256:monero.social >__ The _competition_ won't be altered regardless b/c MRL made a promise. Whether or not the results will turn out useful depends on divisor's academic journey     

> __< k​ayabanerve:matrix.org >__ Yep, one finds the polys, one does the gadget within a ZK proof with the polys.     

> __< s​gp_:monero.social >__ Fwiw, I solicited this zkSecurity quote because I believed that CS's divisors work was potentially months away from being finished. If this work is expected in the near future, and is compatible with Monero's intended use-case, then I would suggest waiting a week and down-scoping zkSecurity's work to a review of CS's work. But if it keeps getting delayed (it's been delayed many ti<clipped message>     

> __< s​gp_:monero.social >__ mes, research is hard), I'd rather have a concurrent research effort on this critical blocker (divisors)     

> __< d​iego:cypherstack.com >__ it has indeed been delayed many many times as we always thought we were close to completion and then hit bear trap after bear trap     

> __< j​effro256:monero.social >__ Good foresight     

> __< d​iego:cypherstack.com >__ so I can see how our "things are going well and we might be done soon" is....tenuous     

> __< r​ucknium:monero.social >__ As I understand, Cypher Stack is close to "some" result. What more would need to be done to prove divisors secure? What about the commentary that the security depends on choosing specific parameters? How can those be chosen and evaluated?     

> __< r​ucknium:monero.social >__ s/secure/sound     

> __< b​randon:cypherstack.com >__ I mean, that's part of the process, once we have all of our proofs written, we can assess practical security for concrete implementations     

> __< b​randon:cypherstack.com >__ But I don't want to say much more about that at the moment     

> __< s​gp_:monero.social >__ I can hold off on the zkSecurity quote until next meeting. But I definitely don't want to delay such a critical component unnecessarily, indefinitely. Worst case we waste some money to make sure this critical component (which is already a blocker!) is addressed more quickly     

> __< d​iego:cypherstack.com >__ I think one week's wait is reasonable.     

> __< rbrunner >__ Is cryptography related work really so different from dev work? Imagine I work many weeks to implement something, my boss gets impatient, gives the same work to some other guy who claims to do it in 2 weeks. Does that sound credible?     

> __< s​gp_:monero.social >__ you have 168 hours 🕐     

> __< s​gp_:monero.social >__ :)     

> __< s​yntheticbird:monero.social >__ pizzas won't be enough...     

> __< d​iego:cypherstack.com >__ This is kind of what we're saying though. What ZKSecurity would be reviewing would be incorrect (since we've already found incorrect things that we've since rectified or been working on rectifying)     

> __< r​ucknium:monero.social >__ I also think waiting a week is reasonable. In the meantime, sgp_ , do you think it would be a good idea to ask zkSecurity, informally, about switching the task to reviewing Cypher Stacks's work?     

> __< j​berman:monero.social >__ I second waiting on a week for divisors review. Additional proposal: what if we request zkSecurity do a holistic review on all already completed proofs? Essentially we get another independent party involved reviewing the academia, and that independent party happens to include a co-author of curve trees     

> __< d​iego:cypherstack.com >__ So to use your analogy rbrunner, the dev work that takes many weeks to implement is because there was an issue with architecture. The extra time is because the architecture is being tweaked and touched up. The boss gets impatient and gets someone else to do an implementation with the original, flawed architecture.     

> __< s​gp_:monero.social >__ since their earliest start date is late this month, I'll bring that up next week if applicable     

> __< s​yntheticbird:monero.social >__ What does holistic review means?     

> __< s​gp_:monero.social >__ Personally I think this is premature without divisors     

> __< r​ucknium:monero.social >__ Well, maybe it would be best to bring it up with them ASAP because that specific time "slot" won't necessarily be reserved for FCMP work indefinitely     

> __< rbrunner >__ The zkSecurity proposal contains the following point: "Proving any/all potential holes/inaccuracies left by Bassa"     

> __< rbrunner >__ They will probably move all that out of the way on the first or the second day :)     

> __< j​berman:monero.social >__ "holistic review" would include a review of all prior proofs, which right now is GBP and FCMP+SA+L composition     

> __< f​reeman:cypherstack.com >__ Rather optimistic to claim they'll patch ANY/ALL holes, with potentially unbounded pro bono hours, with a timeline of 1 week. Just my two cents.     

> __< b​randon:cypherstack.com >__ I find it credible that one of the authors of the curve trees paper can knock the crypto part of this out of the park. I am skeptical someone who didn't teach calculus for 10 years would catch the mistakes we caught. Having said that...     

> __< s​yntheticbird:monero.social >__ optimistic or they are taking adrenaline shot     

> __< b​randon:cypherstack.com >__ More review is better, it's just better to not reinvent wheels     

> __< s​gp_:monero.social >__ Personally I think we can move on to the next topic; we'll check in next week     

> __< b​randon:cypherstack.com >__ Great     

> __< r​ucknium:monero.social >__ More comments or questions on this agenda item?     

> __< d​iego:cypherstack.com >__ kthx     

> __< s​gp_:monero.social >__ jberman: DM me later with what that holistic review would look like, including divisors ideally (if those are done, we can package alltogether)     

> __< j​berman:monero.social >__ Reason I bring it up now is because I wouldn't want that author to get assigned / work on some other work and then be unavailable. Even if we decide to delay them on reviewing divisors, I think it's worth bringing up that we do want to engage them     

> __< s​gp_:monero.social >__ I'll stress to them that we're very interested in keeping the time slot with some work     

> __< j​berman:monero.social >__ I got nothing except thank you Cypher Stack <3     

> __< j​berman:monero.social >__ I got nothing more on this topic*     

> __< r​ucknium:monero.social >__ 4) Subnet deduplication in peer selection algorithm to avoid spy nodes. Draft research bulletin, implementation PR: https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf https://github.com/monero-project/monero/pull/9939     

> __< r​ucknium:monero.social >__ Now we have an implementation ready for review by rbrunner ^     

> __< r​ucknium:monero.social >__ This triggers two possible events: someone can now review it. And previously we discussed that if such a countermeasure has an implementation, then the method for distinguishing spy nodes, discovered by boog900  , maybe can be published.     

> __< o​frnxmr:monero.social >__ Without testing etc, i assume this respects --add-priority/exclusive node and --max-connections-per-ip flags? Rbrunner7     

> __< rbrunner >__ Yes.     

> __< r​ucknium:monero.social >__ Anyone interested in volunteering to review this?     

> __< o​frnxmr:monero.social >__ add-priority/exclusive dont effect incoming. Does this only deal with outgoing connections?     

> __< o​frnxmr:monero.social >__ Or does it also effect peer evictions     

> __< rbrunner >__ Yes. It is in fact a very narrow, fully drop-in replacement     

> __< rbrunner >__ Just choosing new peers to connect to differently.     

> __< o​frnxmr:monero.social >__ Ok thanks     

> __< rbrunner >__ It's a single method that changed     

> __< r​ucknium:monero.social >__ rbrunner: Does this fix the "futile connection attempt" issue you found, or would that be separate?     

> __< rbrunner >__ Yes, it does fix that. That's a small change in a second method.     

> __< r​ucknium:monero.social >__ tobtoht, selsta: Any idea yet when the next Monero release version may be? Just wondering about when may be the timeline for needing to get this and other PRs reviewed in time for next release.     

> __< o​frnxmr:monero.social >__ Anytime, master should be stable, just need to iron out the versioning (v19 instead of v0.18)     

> __< r​ucknium:monero.social >__ Like I said in updates, I pushed version 0.3 of my draft MRL research bulletin: "Subnet Deduplication for Monero Node Peer Selection" https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< r​ucknium:monero.social >__ Besides content updates, it now has the MRL research bulletin header and formatting.     

> __< o​frnxmr:monero.social >__ There havebt been many big recently. Socks5, dynamic bss, some fixes. Txrelay is a bigger one     

> __< o​frnxmr:monero.social >__ many big prs*     

> __< r​ucknium:monero.social >__ I don't know if anyone cares about this, but previous MRL bulletin used the [1] citation format. In this draft I use the [Author, Year] format. I prefer the latter format, but if someone prefers MRL keep the old format, I would be willing to change.     

> __< o​frnxmr:monero.social >__ And guix stuff, since master gets rid of gitian     

> __< r​ucknium:monero.social >__ I don't know if previous research bulletins had any formal review process. I doubt it. If there was a process, someone let me know. But, anyway, anyone can give feedback on the current draft, of course.     

> __< r​ucknium:monero.social >__ Anyone have comments on this? IIRC, jeffro256  had some views     

> __< r​ucknium:monero.social >__ > And previously we discussed that if such a countermeasure has an implementation, then the method for distinguishing spy nodes, discovered by boog900 , maybe can be published.     

> __< a​ntilt:we2.ee >__ no hurry.     

> __< r​ucknium:monero.social >__ Let's move to the final item:     

> __< r​ucknium:monero.social >__ 5) Web-of-Trust for node peer selection.     

> __< j​effro256:monero.social >__ Since I was blocking the publicization of the technique, it makes sense for me to have to review rbrunner's PR     

> __< rbrunner >__ That's one way to see it :)     

> __< r​ucknium:monero.social >__ I wonder if it would be a good idea to implement WoT in cuprate first, to see how it would perform on mainnet     

> __< a​ntilt:we2.ee >__ next step may be to agree on data structures and how the old scoring is actually used today     

> __< r​ucknium:monero.social >__ jeffro256: I would support that :)     

> __< s​yntheticbird:monero.social >__ Cuprate was meant to be testing ground for new features     

> __< s​yntheticbird:monero.social >__ At least cuprate the code, not sure about the Cuprate/cuprate repository     

> __< r​ucknium:monero.social >__ Of course, a shrewd adversary would no try its attacks on cuprate alone, probably. It would wait until most nodes adopt it.     

> __< r​ucknium:monero.social >__ would not try*     

> __< s​yntheticbird:monero.social >__ So are there any values at implementing WoT early into a subset of the network ?     

> __< s​yntheticbird:monero.social >__ I've no doubt it would be easier to implement on Cuprate than monerod     

> __< s​yntheticbird:monero.social >__ but does it return valuable data     

> __< r​ucknium:monero.social >__ IMHO, it would return some valuable data, but probably not complete or sufficient data, alone, to advise on deployment in `monerod`.     

> __< a​ntilt:we2.ee >__ ... and pr 9933 does introduce quite big changes already - I think these are a good starting point for testing, although releasing these (peer dropping) would need simulation IMHO     

> __< s​yntheticbird:monero.social >__ We really need that Shadow thingy for simulating thousands of nodes on a machine don't we...     

> __< r​ucknium:monero.social >__ Shadow could be useful here, yes.     

> __< s​yntheticbird:monero.social >__ Sure, WoT could be pushed into a specific branch for testing if still deemed worthy from a design standpoint.     

> __< s​yntheticbird:monero.social >__ boog900 thoughts?     

> __< r​ucknium:monero.social >__ Any more discussion on this item?     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thank you everyone.     

> __< a​rticmine:monero.social >__ Thank you     

> __< a​ntilt:we2.ee >__ looking foreward to 0xFFFC's report. We have subtile scoring in place, very effective imo -- thanks     

> __< b​oog900:monero.social >__ I have more of a fundamental question of what WoT is trying to solve?     

> __< b​oog900:monero.social >__ the spy nodes? or just general misbehavior?     

> __< a​ntilt:we2.ee >__ plus ddos security     

> __< a​ntilt:we2.ee >__ but WoT is misleading (thats Zimmermann's term for pgp) - I prefer scoring of quality of service     

> __< a​ntilt:we2.ee >__ ...like we do already with the "anchor node" code: thats a score of previous success ("good behavior")     

> __< selsta >__ rucknium: it depends on if the next release is v0.18.4.1 or v0.19.0.0 branched from master     

> __< selsta >__ plan was for v0.19 but it seems a lot of smaller bug fixes are accumulating     

> __< selsta >__ so a smaller release before might make sense     

> __< r​ucknium:monero.social >__ Thanks, selsta     



# Action History
- Created by: Rucknium | 2025-06-03T20:18:59+00:00
- Closed at: 2025-06-12T23:18:48+00:00
