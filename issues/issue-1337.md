---
title: Monero Research Lab Meeting - Wed 04 February 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1337
author: Rucknium
assignees: []
labels: []
created_at: '2026-02-03T22:38:49+00:00'
updated_at: '2026-02-18T16:49:32+00:00'
type: issue
status: closed
closed_at: '2026-02-18T16:49:32+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. zkSecurity quote for reviewing Elliptic Curve Divisors for FCMP++.

4. [Goodell (2026) "Generalized Bulletproofs for Opening Vector Commitments."](https://github.com/cypherstack/generalized-bulletproofs-fix)

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. [CARROT Outgoing View Keys (OVKs)](https://github.com/jeffro256/carrot/blob/master/carrot.md#22-new-wallets-only).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1333 

# Discussion History
## Rucknium | 2026-02-11T01:47:51+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1337     

> __< rucknium >__ 1. Greetings     

> __< rbrunner >__ Hello     

> __< sgp_ >__ hello     

> __< gingeropolous >__ hi     

> __< vtnerd >__ Hi     

> __< jberman >__ waves     

> __< rucknium >__ brandon:cypherstack.com: Are you available to answer questions about agenda item 4, Goodell (2026) "Generalized Bulletproofs for Opening Vector Commitments." (https://github.com/cypherstack/generalized-bulletproofs-fix)     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Working on my Monerotopia conference talk.     

> __< gingeropolous >__ still banging my head against running 1000 monero agents on 256 threads. getting closer.     

> __< vtnerd >__ Me: resolving lwsf/monero_c issues on macos. Testing lwsf beast framework further     

> __< syntheticbird >__ Hi     

> __< ack-j:matrix.org >__ Hi     

> __< jberman >__ me: we released v1.6 of the alpha stressnet that includes tx relay v2, I submitted PR's to improve type organization & dependency management in the FCMP++ integration, and misc PR wrangling     

> __< ack-j:matrix.org >__ MAGIC: Launched a new fundraiser to research more efficient bulletproofs. Working on the reddit post     

> __< ack-j:matrix.org >__ https://donate.magicgrants.org/monero/projects/2026-range-proofs-speedup     

> __< rucknium >__ 3. zkSecurity quote for reviewing Elliptic Curve Divisors for FCMP++.     

> __< sgp_ >__ Cool this is me     

> __< rucknium >__ Last meeting sgp_:monero.social  said that zkSecurity quoted MRL 50,000 USD for performing a mathematical review of EC Divisors. This would be the third review of EC Divisors.     

> __< sgp_ >__ I would like approval here to move forward with the funding of this from the FCMP research fund     

> __< sgp_ >__ The research community previously expressed a desire for a third review of divisors, given the complexities of the review process for it in the past     

> __< sgp_ >__ This quote is an "all inclusive" quote. If it takes them longer than they anticipate to sufficiently support the scheme for Monero's intended use, then they will cover the additional time at no extra cost     

> __< rucknium >__ > <kayabanerve:matrix.org> I may or may not be present. I'm currently slammed for the next couple weeks, sorry. In this time, I've deferred primarily to sgp_:monero.social: so if they ACK the relevant work...     

> __< rucknium >__ kayabaNerve said yesterday: "I may or may not be present. I'm currently slammed for the next couple weeks, sorry. In this time, I've deferred primarily to sgp_ : so if they ACK the relevant work..."     

> __< sgp_ >__ This was chosen because I specifically didn't want to kick the can again. I would like for divisors, if zkSecurity concurs with their suitability, to be considered safe to move forward with     

> __< rucknium >__ Anyone can input their opinion here.     

> __< rbrunner >__ How much is USD 50,000 of the funds remaining for such things, give or take?     

> __< articmine >__ Hi sorry I am late      

> __< jberman >__ Strong +1 from me. Mathias Hall-Andersen, co-author on the curve trees paper, is the one communicating with sgp as well     

> __< rucknium >__ IMHO, it's a good idea to do this because getting it wrong could be catastrophic for the post-FCMP blockchain. This would be triple-checking something that is very high stakes.     

> __< sgp_ >__ there is about 760 XMR left in the fund (this may exclude one payment to CS that is due?), and this would be ~143 for XMR$350     

> __< rbrunner >__ Thanks, sounds good on that front     

> __< rbrunner >__ How will they do it, start with the results from the earlier reviews, or do it independently, to be on the safe side?     

> __< sgp_ >__ for GBP review (a separate item), an additional ~285 is expected fwiw. I'm not looking for approval for that today     

> __< jberman >__ (760 XMR does exclude the ~20-25xmr payment to CS that's due)     

> __< gingeropolous >__ im excited for another review. randomx got like 4, and i feel fcmp is even more critical     

> __< rbrunner >__ I mean, immune from influence     

> __< rucknium >__ The aim is to get loose consensus on this proposal at this meeting. I have seen support so far. Anyone want to raise another opinion with this?     

> __< articmine >__ In favor > <sgp_> I would like approval here to move forward with the funding of this from the FCMP research fund     

> __< sgp_ >__ rbrunner: We gave them flexibility to choose the method so long as they are able to confidently and clearly demonstrate its safety     

> __< rbrunner >__ Alright, they will know what they do :)     

> __< sgp_ >__ I think they will use the initial approach not the CS approach     

> __< rucknium >__ sgp_: sgp_:monero.social: Can you stay for the next agenda item for questions on that?     

> __< sgp_ >__ Ok     

> __< rbrunner >__ We will more or less put the future faith of Monero on this, right? So that's a +1 from me     

> __< sgp_ >__ yes it is essential that divisors are actually secure to use     

> __< rbrunner >__ *fate of course ...     

> __< sgp_ >__ fwiw, both Veridise and CS have signed off on the safety of them, albeit through different supporting methods     

> __< sgp_ >__ so this third one is because of an abundance of caution     

> __< rucknium >__ I see loose consensus in favor of hiring zkSecurity to review Elliptic Curve Divisors for 50,000 USD.     

> __< rucknium >__ 4. Goodell (2026) "Generalized Bulletproofs for Opening Vector Commitments." (https://github.com/cypherstack/generalized-bulletproofs-fix)     

> __< sgp_ >__ rucknium: Great, I will move ahead with the project ASAP     

> __< rucknium >__ This paper suggests a change to the Generalize Bulletproofs implementation in FCMP. It is a change to eliminate a possible vulnerability AFAIK. It could increase the computational expense of them.     

> __< rucknium >__ But kayabanerve:matrix.org  is busy with other tasks for the next few weeks.     

> __< rucknium >__ Implementing this for the beta stressnet was also discussed.     

> __< sgp_ >__ My understanding is that CS made these recommended changes because they believe the performance impact is likely to be tolerable. But ultimately this is waiting on kayaba (or anyone else crazy enough to jump into this task I guess?) to properly evaluate it. And they are busy for the immediate future     

> __< rucknium >__ Is jeffro256:monero.social  here?     

> __< syntheticbird >__ what does possible means here? It's suspected but unproven yet, or is it certain to be possible to exploit     

> __< sgp_ >__ CS believes that the prior approach is insecure, in basic terms     

> __< sgp_ >__ and they suggested this change to fix it     

> __< rucknium >__ Is the suggested change something that could be implemented in code by someone else, like jberman:monero.social  or jeffro256:monero.social ?     

> __< jberman >__ On the implementation side, I'm waiting until kayaba is availalbe to continue this task item (as well as a couple others for beta). From my view, that is likely to be the most efficient way forward at this time     

> __< sgp_ >__ I got a quote from zksecurity as well on GBPs before this change was proposed. I expect it will be the same with the change, if kayaba/others sign off on its use: $100k     

> __< rucknium >__ sgp_:monero.social: For that quote can we get a written scope of work, before it's ready for loose consensus discussion?     

> __< sgp_ >__ Sure, the quote before was just an estimate. It was less of a formal proposal     

> __< jberman >__ jberman: kayaba was in discussions with CS on this, and obviously has more acute knowledge of all sections that should be modified     

> __< articmine >__ Can we wait for kayaba's analysis for this?     

> __< rucknium >__ jberman: jberman:monero.social: That sounds good to me     

> __< sgp_ >__ fwiw I am not asking for approval of this quote today. I'm just sharing an expectation of what it'll look like when it's ready     

> __< sgp_ >__ I think the purpose of this meeting item was to discuss the blocker and see if someone other than kayaba wanted to handle it? idk     

> __< rucknium >__ Yes. And give people a chance to discuss the paper. It was posted during last week's meeting.     

> __< rbrunner >__ That could develop into the last thing that gets final form     

> __< jberman >__ We have work that can proceed in parallel for getting FCMP++ to mainnet. I think the reasonable course of action is waiting on kayaba to continue this item for now     

> __< rbrunner >__ Yeah, didn't want to propose a different course of action. Just a mini-revelation, if you want     

> __< jberman >__ w.r.t. zkSec's 100k quote to review GBP: considering we have a proposed change to GBP at this stage, I think another independent review is evidently justified     

> __< rucknium >__ jberman:monero.social: Do you mean in addition to zkSec's proposed review?     

> __< sgp_ >__ we in theory could jump straight into review of the modification, but it's likely sensible to ensure that we actually want to use it with the modification     

> __< jberman >__ Tbc, I agree with sgp^ there. I would like to see GBP independently reviewed again, after this latest proposed change is sufficiently vetted (which is blocked on kayaba)     

> __< brandon:cypherstack.com >__ syntheticbird: The old version of GBP was provably insecure. Period.     

> __< brandon:cypherstack.com >__ Also. Good morning, sorry for the delay in joining      

> __< rucknium >__ brandon:cypherstack.com: No problem. I should have pinged you earlier :)     

> __< rucknium >__ brandon:cypherstack.com: What is your opinion on review GBP, including your suggested modifications. Is zkSecurity a good choice?     

> __< brandon:cypherstack.com >__ The question is not whether the old version is acceptably secure. It isn't. The question is whether my proposed changes are going to blow up efficiency. There will be an efficiency hit, I don't think it's a game changer, but I haven't had time to work out the specific comparison.     

> __< brandon:cypherstack.com >__ rucknium: I think so.     

> __< articmine >__ By efficiency do you mean verification time, size or both?     

> __< rucknium >__ brandon:cypherstack.com: This is probably hard to answer now: How reasonable is it to expect that a more efficient method than yours could be discovered for constructing GBP? Or is it do or die with this, regardless of the efficiency loss?     

> __< brandon:cypherstack.com >__ My back of the envelope says GBPs will be about 25% larger and an unknown additional verification time. GBPs don't take up the full transaction space so the space complexity worsening should be less than 25%     

> __< brandon:cypherstack.com >__ rucknium: I don't believe that any version of gbps can be made smaller, although proving systems that are outside of the bulletproofs framework might     

> __< articmine >__ brandon:cypherstack.com: I am not covered about this ballpark. It will have a minimal impact on scaling     

> __< articmine >__ *Concerned      

> __< ack-j:matrix.org >__ brandon:cypherstack.com: how much or little would optimizations to bulletproofs+ help optimize GBP?     

> __< brandon:cypherstack.com >__ An optimization to bp+ would make the bp+ part of the proof smaller but not the GBP parts     

> __< rucknium >__ More questions or comments on this item?     

> __< rucknium >__ Thank you, brandon:cypherstack.com , for your work on GBP and answering questions here.     

> __< rucknium >__ 5. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< jberman >__ We released v1.6 of the alpha stressnet yesterday. It includes tx relay v2 (and connection patches that were upstreamed). It doesn't include FCMP++/Carrot changes      

> __< jberman >__ Hopefully we'll get some people running that just to make sure tx relay v2 is running smoothly, so we can port it to beta / upstream it     

> __< jberman >__ A related item: I also made progress on audit prep for the FCMP++ integration     

> __< rucknium >__ I have read some papers that warn that BTC's default number of outbound connections may too low to resist eclipse and network partition attacks. BTC has 8 full outbound connections and 2 block-relay-only outbound connections by default. Monero 's default outbound connection count is 12.     

> __< rucknium >__ So Monero's resistance to eclipse and partitioning attacks could increase if some of the efficiency savings for tx relay v2 is used to increase the default number of outbound connections.     

> __< jberman >__ jberman: Here is essentially what I'm thinking, 4 stages: https://paste.debian.net/hidden/82c00500     

> __< rucknium >__ "As soon as you save some money, there is the temptation to spend it." 😉     

> __< boog900 >__ Cuprate has a higher limit FWIW      

> __< boog900 >__ or default I should say      

> __< jberman >__ Raising the default after the fork could make sense, to ensure the node is connected with peers supporting tx relay v2     

> __< boog900 >__ it also helps for the fluff stage of d++      

> __< rucknium >__ jberman: jberman:monero.social: Should the integration audit prep go on the agenda next week as a dedicated item? Or is it covered in #no-wallet-left-behind:monero.social  meetings?     

> __< jberman >__ We can add it as a dedicated item for next week. I'm not planning to start reaching out to firms until the crypto code is settled (and docs are updated)     

> __< rucknium >__ Anything more on stressnet?     

> __< jberman >__ Nothing from me     

> __< rucknium >__ 6. CARROT Outgoing View Keys (OVKs) (https://github.com/jeffro256/carrot/blob/master/carrot.md#22-new-wallets-only).     

> __< rucknium >__ Anything more to discuss about OVKs at this time?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< jberman >__ thank you     

> __< articmine >__ Thanks      

> __< gingeropolous >__ thanks!     



# Action History
- Created by: Rucknium | 2026-02-03T22:38:49+00:00
- Closed at: 2026-02-18T16:49:32+00:00
