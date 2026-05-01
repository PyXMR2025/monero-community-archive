---
title: Monero Research Lab Meeting - Wed 22 April 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1377
author: Rucknium
assignees: []
labels: []
created_at: '2026-04-21T21:26:12+00:00'
updated_at: '2026-04-29T14:45:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294). [CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/663). [Auditor quotes](https://github.com/seraphis-migration/monero/issues/294#issuecomment-4291345141).

4. FCMP beta stressnet.

5. [Increased FCMP++ membership proof size, marginally slower 1-input verification time](https://github.com/seraphis-migration/monero/issues/317).

6. [Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`](https://github.com/monero-project/research-lab/issues/125).

7. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

8. [CCS proposal: Grease Payment Channels](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).

9. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4281932714).

10. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1371 

# Discussion History
## Rucknium | 2026-04-29T14:45:02+00:00
Log



> __< gingeropolous >__ im not sure i'll be around for the meeting, but my updates: monerosim - found the bug preventing 100s of user wallets  from crafting and sending transactions. Now i'm working on optimization, making it so the auto setting creates working configs that run simulations efficiently. If the config isn't right, you can end up running 12 hrs of clock time for 4 hours of sim time.      

> __< gingeropolous >__ i also started working on transpeer, and leveraging shadow to test. but thats not really monero specific... but perhaps one day we won't need seed nodes     

> __< gingeropolous >__ https://github.com/Fountain5405/transpeer/blob/master/PROTOCOL.md     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1377     

> __< rucknium >__ 1. Greetings     

> __< sgp_ >__ Hello     

> __< vtnerd >__ hi     

> __< rbrunner >__ Hello     

> __< MarkoPohlo >__ hey everyone     

> __< boog900 >__ hi     

> __< UkoeHB >__ Hi     

> __< jberman >__ waves     

> __< tevador >__ Hi     

> __< hbs:matrix.org >__ hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< yiannisbot:matrix.org >__ Hi everyone!     

> __< jberman >__ Preparing for beta stressnet, general audit review/discussions, upstream PR's     

> __< rbrunner >__ Last week made good progress implementing Polyseed for the CLI wallet     

> __< tevador >__ PQ encryption for Jamtis     

> __< rucknium >__ me: Gathered data on recent confirmed txs with custom unlock time: https://github.com/monero-project/research-lab/issues/125#issuecomment-4297942950     

> __< yiannisbot:matrix.org >__ Diving into the details of Dandelion++      

> __< UkoeHB >__ SAL multisig     

> __< syntheticbird >__ Hi     

> __< vtnerd >__ me: still testing /feed :( and otherwise working on reviews/updates to other prs     

> __< vtnerd >__ specifically been looking at the ssl and weak_ptr prs again     

> __< rucknium >__ 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294). CCS proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/663). Auditor quotes (https://github.com/seraphis-migration/monero/issues/294#issuecomment-4291345141).     

> __< jpk68:matrix.org >__ Hello     

> __< jeffro256 >__ Howdy      

> __< sgp_ >__ MAGIC Grants helped Berman and Jeffro collect audit quotes for the 1a and 1b components. We received quotes from 8 vendors, which we evaluated and summarized here (their names redacted to protect their privacy/reputation): https://github.com/seraphis-migration/monero/issues/294#issuecomment-4291345141     

> __< sgp_ >__ I am very appreciative of the 8 vendors who submitted proposals. There remains a lot of interest in Monero related reviews ❤     

> __< rucknium >__ "Public press coordination is required" = Audit release timing must be managed closely? Any real downsides to this?     

> __< MarkoPohlo >__ is that audit quote collection period now officially completed?     

> __< jberman >__ I'll also add sgp_:monero.social has been a huge help on this, handling all comms and aggregating info. Thank you sgp     

> __< rucknium >__ This first of three audits can be done parallel in time to the 2nd and 3rd, right?     

> __< sgp_ >__ By "public press coordination required", it's less about timeline and more about us granting the vendor the ability to advertise the outcome however they want, and to be supportive of their marketing. That could include things like showing up in podcasts and interviews. Ultimately it's not a big deal since the reports will be public in the end anyway     

> __< jeffro256 >__ jberman: And you can't underestimate the value of comms, it takes a ton of time and effort      

> __< sgp_ >__ basically, the discounted quote is contingent on the vendor being able to market the work they did. often times, it's up to the purchaser of the audit to determine if the report is even made public at all     

> __< sgp_ >__ MarkoPohlo: Yeah, I don't anticipate any further submissions for 1a and 1b, and we already have good options within the $50k budget     

> __< interestingband:matrix.org >__ What does it mean "Includes X amount of work" ?     

> __< sgp_ >__ interestingband:matrix.org: that is included to give a sense of the amount of time the vendor has allocated in their quote. The review time varies     

> __< jeffro256 >__ They commit to X engineer-hours of labor      

> __< sgp_ >__ time is not the same as expertise of course, but it's one metric to consider     

> __< rbrunner >__ Who suggested the ranking in the table?     

> __< sgp_ >__ After discussing with Berman, Jeffro, and Luke, we picked the top 3 in our view which considers expertise, budget, and timeline. My personal opinion is that any of the top 3 could be justified as a good option     

> __< rbrunner >__ I see, thanks     

> __< syntheticbird >__ I hope Zellic is in the top 3     

> __< articmine >__ Sorry I am late      

> __< syntheticbird >__ nah i'm not gonna stop shilling them     

> __< rbrunner >__ I guess vendor 7 is not in the suggested top 3 because of the high price, in comparison     

> __< jberman >__ Correct rbrunner     

> __< jeffro256 >__ The timeline was probably the weakest variable in the ranking. Biggest con of vendor 4 is its timeline. People in the community may want a better timeline, so their ranking may be different      

> __< jeffro256 >__ rbrunner7 same with vendor 3      

> __< rbrunner >__ Yeah, but that is anyway not similarly attractive, without prior experience with them     

> __< sgp_ >__ There is one thing we want to ask here for feedback. Vendor 4 assigned a lot more time to the review than Vendor 1. We consider this to generally be a positive in terms of review coverage, but it has the consequence of the audit potentially taking longer to deliver. Worst case, this could be delivered in August.     

> __< sgp_ >__ What are the community's thought about timing? I can ask Vendor 4 to see how much room they have to tighten the timeline, but is there a certain delivery date that would be considered simply too far away to justify?     

> __< syntheticbird >__ 1 months, 1 year, 1 century. We're already late so who cares     

> __< rbrunner >__ They expect 400 hours of work? That's massive in comparison with the others. I wonder a bit.     

> __< rbrunner >__ Maybe that's one reason they had to put it far out in the calendar?     

> __< MarkoPohlo >__ There's a wild discrepancy in review hours suggested and hourly rate between these 8 proposals, wow.     

> __< jeffro256 >__ syntheticbird: I tend to disagree since real-life privacy is affected, but obviously I don't want a shoddy job on the audit. I think all of the top 3 would be great candidates for the job     

> __< syntheticbird >__ i know im joking     

> __< sgp_ >__ (in case any vendor representatives are here, you are free to chime in. I didn't want us to name vendors out of respect for their bids)     

> __< jberman >__ I'll add my own thoughts/opinion: given Vendor 4's estimated timeline (which we heard from today), I would switch my personal suggested ranking with Vendor 1 (I would rank Vendor 1 as 1). Vendor 1 is also highly qualified, and considering we have 3 audit phases to get through here, I would prefer to not risk delaying the timel [... too long, see https://mrelay.p2pool.observer/e/7ovZ_fsKUmpnWE9I ]     

> __< jberman >__ I would personally prefer to limit risk to have the audit released August or later     

> __< rbrunner >__ Is vendor 6 "only" rank 3 because we might use their capacity for other, subsequent audits?     

> __< jberman >__ rbrunner: yes     

> __< rbrunner >__ Aha!     

> __< rucknium >__ I don't see that my question was answered: "This 1st of three audits can be done parallel in time to the 2nd and 3rd, right?"     

> __< sgp_ >__ jberman:monero.social: other than "sooner is better", is there a specific date you have in mind for not wanting to receive a report after?     

> __< jberman >__ rucknium: It's all code building off the others. I had planned it sequentially     

> __< jberman >__ sgp_: August 1     

> __< jeffro256 >__ jberman: I'm looking at phase 1a, tho, and as long as each crypto function holds its invariants, I feel like that one could definitely be parallelized     

> __< jberman >__ I can also look into restructuring to have code segments audited in parallel, it's not impossible. But it would gum things up a bit     

> __< rucknium >__ Would that mean that we may have the full 3 audit sequence completed in 6 - 9 months from now?     

> __< rucknium >__ Or are the parts 2 and 3 expected to require less time to audit?     

> __< sgp_ >__ I can write to Vendor 4 and see if they can commit to that timeline or not     

> __< jeffro256 >__ rucknium: I would guess that 2 & 3 take the majority of the time      

> __< jberman >__ I'd estimate they're all pretty equal     

> __< jberman >__ There is an additional interesting tidbit I think worth sharing as well: Vendor 5 has already commenced work on the audit knowing that we have not decided on them, i.e. potentially doing the work for free. They have stated they can have it completed by May 6th     

> __< rbrunner >__ Er, what? :)     

> __< UkoeHB >__ Hundreds of hours of review is hard to fathom. It’s not like there’s 100k+ lines of code to look at.     

> __< jberman >__ Vendors 1, 4, 6 have the more relevant xp for this particular audit task that we're looking for, which is why we still feel it worth moving forward with another vendor     

> __< jeffro256 >__ UkoeHB that was my gut reaction too      

> __< plowsof:matrix.org >__ free as in free or retroactive request for the entire amount? :P     

> __< rbrunner >__ I wonder whether we would trust, and could trust, the result of such an audit ...     

> __< sgp_ >__ Free sounds good, but we really need the expertise of a different vendor for the implementation and FFI stuff     

> __< MarkoPohlo >__ Is there any security roadmap beyond these 3 audit phases, though?     

> __< jberman >__ plowsof:matrix.org: no request for payment made or any indication they'd request yet     

> __< plowsof:matrix.org >__ interesting indeed     

> __< jeffro256 >__ MarkoPohlo: j-berman and I have talked informally about auditing the wallet-specific implementation code as a follow up     

> __< jberman >__ MarkoPohlo: not sure what you mean by security roadmap here. We still have an mx25519 audit we want to do, and we have the completion of the Research audit items. On the integration, there is an optional audit slated for reviewing the "torsion_check_vartime" academia, which I have also mentioned to Vendor 5 as a potential item that would be nice to have them work on     

> __< ixr3:matrix.org >__ sgp_: Can't they audit it for free alongside any paid audits?     

> __< jberman >__ And ya plus some other optional wallet-specific stuff jeffro256:monero.social  refers to there     

> __< sgp_ >__ ixr3:matrix.org: I can't prevent someone from looking at the code, so yes     

> __< ixr3:matrix.org >__ sgp_: I hope they do it quickly as a pre-audit before other audits begin. Maybe they'll do a thorough job and prove us wrong. That would be great marketing for them.     

> __< rucknium >__ The choice of auditor should be decided today, right? Or is more time needed?     

> __< sgp_ >__ I would like to get tentative approval to move forward with one of the top 3. I can clarify timeline with vendor 4. If it's too long we can pick vendor 1. That is my opinion     

> __< tevador >__ Audits should preferably start ASAP     

> __< yiannisbot:matrix.org >__ Hi folks, sorry to jump in. yiannisbot from ProbeLab here. Interested to get feedback on our proposal, but I'll need to drop in 15-20mins. Any chance we could cover the topic of our proposal, or is it going to spill over to the next one?     

> __< rucknium >__ yiannisbot:matrix.org: I'll move you item to be next on the agenda once we are finished with this one. Thanks for joining.     

> __< sgp_ >__ it's also worth noting that none of the four of us are affiliated with any of the top 3 vendors     

> __< ofrnxmr >__ sgp_: "mid may. Early june" and "within 2 months" sound like the same thing     

> __< rucknium >__ How should we interpret the gap between the 400 hours from Vendor 4 and 88 hours from vendor 1?     

> __< sgp_ >__ similar start date, but one proposed 2 weeks of time to deliver and another proposed 6-8 weeks to deliver     

> __< ofrnxmr >__ rucknium: Probably more people, is my assumption     

> __< interestingband:matrix.org >__ What's the duration of these audits ? Hours / 8 per day ?     

> __< tevador >__ I think Vendor 1 looks like the best option at the moment.     

> __< rucknium >__ I am fine with Vendor 1.     

> __< gingeropolous >__ are these just one audit team per audit target?     

> __< sgp_ >__ for a total budget of 150k, one per is the most realistic     

> __< rucknium >__ But why so many more hours from Vendor 4? I don't know enough about code auditing, to be honest.     

> __< rbrunner >__ We can rule out some misunderstanding hopefully? That they misunderstood the scope     

> __< sgp_ >__ times vary quite a bit between vendors. It primarily comes down to experience, scoping, depth, and number of people reviewing     

> __< interestingband:matrix.org >__ It's either realistic amount of time to check everything or they are lacking confidence in doing it quickly, hard to tell without knowing more details about each vendor     

> __< interestingband:matrix.org >__ prior work would help, info about their ppl would help     

> __< interestingband:matrix.org >__ but it's hidden      

> __< ixr3:matrix.org >__ sgp_: Vendor 4 could be 3 people and deliver as quick as Vendor 1?     

> __< ofrnxmr >__ Vendor 1 sounds like "1 person, full time, 2 weeks"     

> __< jeffro256 >__ interestingband:matrix.org: Both Vendor 1 and Vendor 4 have done audits for Monero code in the past     

> __< interestingband:matrix.org >__ I know few such vendorsl who did bad audits from my PoV, so it's not enough      

> __< interestingband:matrix.org >__ need more info     

> __< sgp_ >__ I specifically asked for the review duration for Vendor 4 and they said 6-8 weeks. We only got that confirmed this morning     

> __< jberman >__ The presumption discussed internally was that possibly less xp compared to Vendor 1 contributed to Vendor 4's higher estimate, which they'd make up for with more people involved     

> __< interestingband:matrix.org >__ Hours is man hours or actual duration of the audit given their number of humans ?     

> __< jberman >__ We have a valid reason here for keeping vendors anon interestingband:matrix.org     

> __< interestingband:matrix.org >__ this question > <interestingband:matrix.org> What's the duration of these audits ? Hours / 8 per day ?     

> __< sgp_ >__ interestingband:matrix.org: if you want to express those thoughts, I would love if you could email them to me (justin⊙mo) or berman or jeffro     

> __< UkoeHB >__ If vendor 4 hours doesn’t mean more eyes, then vendor 1 sgtm     

> __< ixr3:matrix.org >__ UkoeHB: Agree     

> __< sgp_ >__ the primary justification for vendor 4 over 1 is more eyes (and less rush). but realistically 6-8 weeks is probably too long     

> __< rbrunner >__ Sounds reasonable to me as well, UkoeHB     

> __< tevador >__ Note that going with Vendor 1 will potentially save 1 month (unless audits are done in parallel).     

> __< ixr3:matrix.org >__ sgp_: That sounds like 1 person full time for 6-8 weeks     

> __< ofrnxmr >__ interestingband:matrix.org 's question is a good one. Is this 400 man hours? So, among 5 people would still be 2 weeks     

> __< sgp_ >__ Yeah which isn't what we were expecting tbh, so we were surprised by the long timeline estimate     

> __< rbrunner >__ We have 2 more such reviews. Vendor 4 is perfectly free to apply again, with maybe a revised offer, right?     

> __< jberman >__ I also personally feel sticking with a single auditor for all 3 phases would lead to the highest quality output, since all code builds off prior     

> __< ofrnxmr >__ ixr3:matrix.org: Exactly. The math isnt mathing.     

> __< UkoeHB >__ jberman: +1     

> __< rbrunner >__ But that makes our decision today quite a bit more important     

> __< jberman >__ By auditing in phases, we can assess quality at the end of phase 1 before progressing to the next step     

> __< ixr3:matrix.org >__ ofrnxmr: Vendor 4 confirmed 6-8 weeks     

> __< sgp_ >__ it sounds like vendor 1 is preferred here unless vendor 4 can get the delivery time estimate way down     

> __< jeffro256 >__ Personally, I think that it's more important for phase 2 & 3 to be the same team. It would be nice is phase 1 was the same, but to me, it feels much more compartmentalized      

> __< ofrnxmr >__ Vendor 5 also says they can finish before vendor 1 even starts (?)     

> __< rucknium >__ sgp_: Yes, but I don't like punishing thoroughness.     

> __< rucknium >__ So, this would not be punishing thoroughness, right?     

> __< gingeropolous >__ i don't feel the need to rush things     

> __< rucknium >__ yiannisbot:matrix.org: Sorry for the scheduling issues. Probably this agenda item will go past 18:00 UTC     

> __< interestingband:matrix.org >__ jberman: Is it anon for everyone or you (4 ppl) know who is who internally ?     

> __< jberman >__ jeffro256: A large portion of the Rust FFI types is included in phase 2 as well     

> __< yiannisbot:matrix.org >__ rucknium:monero.social: and everyone, I understand the issue under discussion is an important one, and fair that it was allocated most of the time. But unfortunately, I've got to drop now. Let's shift the issue to next week's meeting? Or inbetween - we'd also be available and happy to discuss.     

> __< sgp_ >__ all 4 know and have been CC'd on all convos     

> __< jberman >__ interestingband:matrix.org: it's anon publicly, and us 4 know who is who internally     

> __< interestingband:matrix.org >__ then you all (4 ppl) have more info to make the best decision     

> __< ixr3:matrix.org >__ Why was Vendor 4 initially marked as the top choice?     

> __< tevador >__ Taking into account the expected start date is not punishing thoroughness.     

> __< jberman >__ interestingband:matrix.org: yes that is obviously true here     

> __< ixr3:matrix.org >__ interestingband:matrix.org: Yes that is why I wonder why Vendor 4 was the top choice initially     

> __< ixr3:matrix.org >__ They seem better, but slow?     

> __< jberman >__ more people involved, more eyes, potentially a more thorough review was seen as a positive. But I'm elevating timeline concerns     

> __< jberman >__ More people involved / more eyes assumed based on the significantly higher man-hour allocation      

> __< jberman >__ The 6-8 week timeline also included a review round with fixes     

> __< ixr3:matrix.org >__ If they perform the other audits with the same speed as well, the overall process will be very slow yes     

> __< sgp_ >__ jberman:monero.social: I did ask that they exclude that from their estimate; I believe they meant just general questions/comments. But 6 should be more realistic than 8 because... everything is already ready to be reviewed     

> __< sgp_ >__ anyway, I think we have what we need from this meeting. A preference for Vendor 1 unless Vendor 4 can get the timeline condensed     

> __< ixr3:matrix.org >__ sgp_: Yes, you can push 4 now :D     

> __< sgp_ >__ fwiw, both are good choices. It's between two good options, not one good one bad     

> __< jeffro256 >__ For the record, I support vendor 1      

> __< rucknium >__ sgp_: jberman:monero.social and jeffro256:monero.social  And you satisfied with this? ^     

> __< sgp_ >__ vendor 1 will require pre-payment to "lock in" the review start date, so it would be great to have a fast turnaround on that from acceptance     

> __< jeffro256 >__ sgp_: Will need commitment to fast turnaround from luigi1111, but the CCS is already funded enough to start phase 1      

> __< luigi1111 >__ (I have no idea what this is about but I'm around as of now and can fulfill within a day)     

> __< jberman >__ I'm satisfied with it. Would MRL require that we get signoff on the de-anon'd proposed final candidate before proceeding? Or have we shared enough info to receive approval on either of Vendor 1 or 4 and move forward?     

> __< interestingband:matrix.org >__ When did you plan to de-anon candidates initially ?      

> __< interestingband:matrix.org >__ :D     

> __< jeffro256 >__ Sorry for pinging without context luigi1111 . If an audit vendor requests payment within the next couple days, would you be able to fulfill that payment (or at least a payment to MAGIC)?     

> __< luigi1111 >__ yes. how much would it be?     

> __< rucknium >__ I think we have a workable "if" conditional statement in the proposal here to get loose consensus at this stage to move forward. IMHO.     

> __< jberman >__ interestingband:matrix.org would be nice if you could contribute to the discussion     

> __< jeffro256 >__ ~50,000 USD worth of XMR from the FCMP++ integration audit proposal: https://ccs.getmonero.org/proposals/fcmp++-integration-audit.html     

> __< rucknium >__ By the way, about what fraction of the vendors require the anon bidding?     

> __< plowsof >__ about 132.5 xmr currently     

> __< rbrunner >__ For me, hard to imagine that the choice still changes after the candidate and exact terms become known, so IMHO that's good to go     

> __< MarkoPohlo >__ last one from me, when do we foresee the RFP process kicking off for audit 2 and 3?     

> __< rucknium >__ The proposal on the table is to go with Vendor 1 unless Vendor 4 can shorten timeline to the satisfaction of jeffro256:monero.social  and jberman:monero.social . Any objections to this?     

> __< jberman >__ MarkoPohlo: Imo ideally by July. I really do strongly feel it would be best to do it sequentially and aim to do it with preference to the same auditor     

> __< plowsof >__ 49,500USD to be exact for vendor 1     

> __< jberman >__ Phase 2 includes deeper Rust FFI components, and understanding the core tree building blocks of Phase 2 will be of significant advantage to understanding Phase 3     

> __< sgp_ >__ Vendor 1 should enable us to start audit 2 solicitations around late June     

> __< tevador >__ Can we move forward?     

> __< rucknium >__ I see loose consensus here in favor of hiring Vendor 1 from https://github.com/seraphis-migration/monero/issues/294#issuecomment-4291345141 for phase 1 of the FCMP++ integration audit, unless Vendor 4 can shorten its timeline to the satisfaction of jeffro256:monero.social  and jberman:monero.social .     

> __< sgp_ >__ Or maybe earlier but that tends to get messy/expensive if the quote isn't clearly defined and unchanging     

> __< interestingband:matrix.org >__ Chaper price of an audit ? Any other advantage ? > <jberman> We have a valid reason here for keeping vendors anon interestingband:matrix.org     

> __< rucknium >__ 4. FCMP beta stressnet.     

> __< sgp_ >__ Ty rucknium     

> __< jberman >__ interestingband:matrix.org: respect to the candidates, maintaining positive relationships for future work. Being useful in discussions is a good skill     

> __< jberman >__ We have an interesting update to consider for beta stressnet: kayabanerve:matrix.org  has taken a deeper pass at the GBP fix and found a mismatch to spec (kayaba would be able to speak to it best). After another pass, a new impl reduced the increase to proof sizes an estimated 25% (need to confirm the exact figures still)     

> __< jberman >__ kayaba has also opened further issues on the GBP fix repo: https://github.com/cypherstack/generalized-bulletproofs-fix/issues     

> __< kayabanerve:matrix.org >__ reduced the increase itself, not reduced the increase to just 25% relative to the old version     

> __< jberman >__ (I see kayaba's typing so I'll let kaya continue)     

> __< kayabanerve:matrix.org >__ I just wanted to clarify what was reduced, how. I'll let you cite any exact numbers you want jberman:monero.social:     

> __< jberman >__ got it     

> __< jberman >__ kayabanerve:matrix.org also mentioned that there is still further back and forth to be had with CS on it, but expects it to resolve as expected with these new figures     

> __< jberman >__ That was also the case last week though, and we have new figures today     

> __< tevador >__ Can this table be updated whent he new numbers are known? https://github.com/seraphis-migration/monero/issues/317     

> __< jberman >__ Ya I'll do it right after this meeting     

> __< tevador >__ Thanks     

> __< jberman >__ Didn't get the chance     

> __< tevador >__ So I guess we have also covered agenda item 5     

> __< jberman >__ So w.r.t beta stressnet, there is still an expected risk that there is some material change to proof sizes     

> __< jeffro256 >__ 12500 is still probably a decent choice for reference tx size      

> __< jberman >__ It's an open question when exactly this GBP fix will be fully resolved     

> __< jberman >__ So imo, we have virtually similar info as last week, and it probably still makes sense to move forward with beta     

> __< jberman >__ The code is pretty much ready to proceed. We could set a date today     

> __< jeffro256 >__ So two choices: 1) go forward with beta, knowing that the proof size on beta may be ~8% bigger than mainnet. 2) wait until we know whether or not proof sizes will change      

> __< sgp_ >__ so beta tomorrow? /s     

> __< tevador >__ I'd say go forward     

> __< jberman >__ "knowing that the proof size on beta may be ~8% bigger than mainnet" kayabanerve:matrix.org has already implemented the changes, so we can use the latest     

> __< sgp_ >__ my completely uninformed opinion is to go forward     

> __< jeffro256 >__ Well done kayabanerve:matrix.org . A lot happened while I was sleeping last night ;)     

> __< rucknium >__ How different will the code paths be if the proof size shrinks 8%? How big is the risk that beta stressnet would materially test the "wrong" code and there would be surprises on mainnet?     

> __< jeffro256 >__ I personally vote 1. Even if the proof size does change downwards slightly, the whole point of a stressnet is to stress     

> __< tevador >__ Yeah, 8% more stress testing can't hurt     

> __< jberman >__ Tbc, we can use the latest that implements the latest proof sizes with kayaba's expected fix fully implemented (which I'd advocate for using)     

> __< rucknium >__ jberman:monero.social: That sounds good to me     

> __< jeffro256 >__ So then there's two options for option 1 :): use bigger proof tx sizes (old), or 2) use smaller proof tx sizes (new)      

> __< jberman >__ The risk to a further change in proof size imo is to the up or down, not necessarily certain to be smaller imo     

> __< jeffro256 >__ Fair      

> __< jberman >__ rucknium: Imo the code paths are not likely to be materially impacted. Alpha stressnet e.g. caught tons of different issues where a change to proof size wouldn't have made them any less likely caught     

> __< rucknium >__ I am OK with setting a beta stressnet start date today.     

> __< jbabb:cypherstack.com >__ let's please proceed to stressnet beta even if minor changes may still be necessary     

> __< jeffro256 >__ rucknium: If the size / validation is off within a bound of 10%, the stressnet's stressing effects will overcome it either way. The only thing I could think of is some sort of a DoS bug in the new mainnet code that doesn't appear in the beta stressnet, but may be triggered in an edge case we didn't see      

> __< jbabb:cypherstack.com >__ these https://github.com/cypherstack/generalized-bulletproofs-fix/issues have been forwarded on and are being looked at     

> __< jberman >__ jeffro256:monero.social and I have discussed a proposed fork date of 2 weeks from today, May 6th. I'd also like to have ofrnxmr:monero.social do a quick round of testing, and then we release binaries next week     

> __< rucknium >__ jberman:monero.social: Sounds good to me     

> __< rucknium >__ This item has been covered already:  Increased FCMP++ membership proof size, marginally slower 1-input verification time (https://github.com/seraphis-migration/monero/issues/317).     

> __< jberman >__ (going to try and update those figures asap)     

> __< rucknium >__ Ready to go to next item?     

> __< tevador >__ Yes please     

> __< rucknium >__ 6. Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future unlock_time (https://github.com/monero-project/research-lab/issues/125).     

> __< rucknium >__ I found 4 transactions with binding custom lock time confirmed since the May 1st, 2025 deadline: https://github.com/monero-project/research-lab/issues/125#issuecomment-4297942950     

> __< jberman >__ Given your findings there, I'd say setting the date as June 1, 2026 should be fine, with the option to make it earlier if there is some major influx of timelocks between now and then     

> __< jeffro256 >__ What is meant by "binding"?     

> __< rucknium >__ There were thousands of non-binding custom lock times in the single and double digits. Users or wallet developers that are using those custom lock times are fingerprinting their txs, a privacy risk.     

> __< rucknium >__ jeffro256: Users thinking that lock time is relative block height instead of absolute. Such as putting lock time to 10.     

> __< jeffro256 >__ Oh I see, "binding" as in it actually makes a difference to when their funds are usable (I.e. > height + 10)?     

> __< jberman >__ Have the blog post drafted, just need to plug in the date. I can PR it to getmonero.org by EOW     

> __< jeffro256 >__ Ohhhhhh      

> __< rucknium >__ Most of the non-binding lock times were "8". That was 15499 transactions. Just another reason to get rid of custom lock time.     

> __< rbrunner >__ Recent transactions? That got mined somehow?     

> __< tevador >__ I see the last lock being 11th November 2025, so we could do 1st January 2026 in theory if announced ASAP?     

> __< rucknium >__ Yes. I didn't do an analysis of who mined them. It could be old p2pool nodes.     

> __< jeffro256 >__ rbrunner:  Unfortunately, I guess that means the miner nodes for coordination are probably still running old monerod binaries     

> __< jberman >__ tevador: Publicly announcing a past date I feel could ruffle some feathers unnecessarily     

> __< jberman >__ That's why I'm proposing June 1, 2026     

> __< tevador >__ Do we have to announce a future date, though? It could just be as of the date of the blog post.     

> __< rbrunner >__ It's probably all psychology. A past date gives chances to some people to throw mud at the project     

> __< jberman >__ I figured it's optimal optics, and the post includes this: "If we see a large influx of new Unlock Time transactions created between now and date X, the feature may be deprecated sooner"     

> __< rucknium >__ It looks like the last one of the nonbinding txs was confirmed in August 2025.     

> __< tevador >__ It's not like locks will stop working immediately. People will have at least 9 months to sort it out before the transactions unlock.     

> __< jberman >__ I anticipate some vocal people are going to come out of the woodwork and be upset over this deprecation, so giving less ammo to those folks seems a smoother path      

> __< tevador >__ OK     

> __< rbrunner >__ Yes, that, and I feel it's also objectively "nicer"     

> __< rucknium >__ "People will have at least 9 months to sort it out before the transactions unlock." Isn't the proposal to not unlock anything, but to prevent future locks from occurring?     

> __< jeffro256 >__ At the currently rate of 4 binding lock times in the last 11 months, it wouldn't be a technical issue if the deprecation date was today or in June      

> __< tevador >__ Unless the blog post triggers it.     

> __< jeffro256 >__ True      

> __< tevador >__ But we'll see. I think we can go with the June date then.     

> __< rucknium >__ I am OK with June 1, 2026.     

> __< jeffro256 >__ rucknium: It's to nullify locks only after the FCMP++ fork, but retroactively for all locks made after a certain date      

> __< ofrnxmr >__ June works, but can also just make it the date of the blog post     

> __< jeffro256 >__ So all locks made after June would be ineffective starting at the FCMP++ fork date      

> __< rucknium >__ Ready to move to next item?     

> __< tevador >__ Someone could DoS the tree building process by having a transaction unlock at every block at some point in the future if submitted before the deadline.     

> __< tevador >__ But I guess we can see and discuss that in June.     

> __< rucknium >__ jberman:monero.social  said     

> __< rucknium >__ > I figured it's optimal optics, and the post includes this: "If we see a large influx of new Unlock Time transactions created between now and date X, the feature may be deprecated sooner"     

> __< jberman >__ "If we see a large influx of new Unlock Time transactions created between now and date June 1, 2026, the feature may be deprecated earlier than June 1, 2026. Deprecating avoids complications with the FCMP++ wallet integration, enabling a smoother wallet experience for all users. Note that a FCMP++ fork date is not set at the time this is written."     

> __< rucknium >__ That covers the DDoS possibility     

> __< hbs:matrix.org >__ did you identify any tx with a timestamp instead of block height as the unlock_time? > <rucknium> I found 4 transactions with binding custom lock time confirmed since the May 1st, 2025 deadline: https://github.com/monero-project/research-lab/issues/125#issuecomment-4297942950     

> __< rucknium >__ hbs:matrix.org: No.     

> __< jeffro256 >__ tevador: It would be effective if they just set the unlock_time=499999999, because the tree building code needs to save all locked outputs at each block processing point, not just the ones that unlock at that block     

> __< rucknium >__ 7. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< rucknium >__ yiannisbot:matrix.org was here earlier, but had to leave because of time.     

> __< rucknium >__ Got these new comments from ProbeLab:     

> __< rucknium >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667#note_36005     

> __< rucknium >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667#note_36051     

> __< rucknium >__ I find it hard to recommend this CCS proposal, given the conditions offered at this time. I thought that the scanning code would be made open source, but it will remain closed source.     

> __< plowsof >__ repo is offline, our apologies      

> __< rucknium >__ I am sorry to hear that another entity previously used your open source code without contributing back. But keeping code closed source because you are afraid of it being leveraged for commercial purposes is not the Monero way. Couldn't you release it under the AGPL license and avoid the problem?     

> __< rucknium >__ plowsof: Oh     

> __< plowsof >__ :(     

> __< rucknium >__ Given the closed source code, I don't see enough benefit to the proposal. There is a lot of overlap between ProbeLab's monitoring and the code that boog900:monero.social and I already wrote for https://xmrnetscan.redteam.cash/     

> __< rucknium >__ IIRC, the ProbeLab code runs in just 11 minutes. Our code takes over 11 hours to run. I assume that ProbeLab didn't just use more hardware :D . So the speed is a benefit, especially as our runtime gets closer to 24 hours for the daily scan.     

> __< rucknium >__ If these terms cannot change, I would be more interested in using ProbeLab's expertise in network analysis to actually solve the spy node problem. Monitoring is only one piece of the puzzle.      

> __< rucknium >__ Here are some ideas presented by boog900 and myself: https://github.com/Rucknium/presentations/blob/main/Rucknium-Boog900-MoneroKon-2025-Spy-Nodes.pdf https://vimeo.com/1095371245     

> __< rucknium >__ Those are my comments.     

> __< sgp_ >__ I added one comment in the CCS that I prefer more of a research project to solve something actionable     

> __< sgp_ >__ imho we don't need a dashboard just to have one     

> __< sgp_ >__ plus we already have one     

> __< plowsof >__ +1 on this feedback     

> __< ofrnxmr >__ And be required to continuously fund a commercial offering..     

> __< rucknium >__ More comments or questions on this item?     

> __< ofrnxmr >__ sounds backwards. Other commercial entities sponsor monero, not the other way around. Thats my 2.5c     

> __< rucknium >__ 8.  CCS proposal: Grease Payment Channels (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/651).     

> __< rucknium >__ Any comments on this item?     

> __< rucknium >__ 9.  Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4281932714).     

> __< tevador >__ I wrote a simplified summary without any gory math details. The point is to agree on one of the 7 choices.     

> __< sgp_ >__ Ty tevador for all your work on this and your work organizing this     

> __< rbrunner >__ Likewise     

> __< ofrnxmr >__ seconded     

> __< rucknium >__ Yes, thank you tevador :)     

> __< tevador >__ For comparison, Zcash is going with something similar to AN509, but worse, because they will have O(N) scanning time with N = number of addresses.     

> __< plowsof >__ +1     

> __< tevador >__ Does anyone have any comments? Any opposition to moving forward with BC1024?     

> __< rucknium >__ I am going to ask some noob questions. If a PQ adversary has one of the Carrot addresses of a wallet, they can de-anonymize the txs of the wallet that share a common private key seed, e.g. the Hierarical Deterministic (HD) wallet seed phrase. Is that correct? Then an impractical countermeasure is to eliminate HD wallets and go [... too long, see https://mrelay.p2pool.observer/e/x7zkgPwKVnZXU0do ]     

> __< tevador >__ They can deanonymize transactions that share a private view key. You can avoid that by having a different view key for each transaction, but that means O(N) scanning time.     

> __< tevador >__ Different view key for every address*     

> __< jeffro256 >__ rucknium: For the new Carrot key hierarchy, the QA can deanonymize the transaction graph of the output receives externally. They cannot deanonymize the outputs which were self-sended      

> __< rucknium >__ Another hypothetical: Why would a party that is cooperating with a PQ adversary set up the infrastructure to send XMR to this special PQ address? Wouldn't they just say "Sorry, you must use the old addresses"? Isn't this a big part of the threat model that these PQ addresses are , um, addressing?     

> __< tevador >__ Yes, but self-sends are not very important in practice anyways.     

> __< jberman >__ A comment on potentially large (1kb+) address length: perhaps we could implement something like ASCII qr codes? So instead of copying and pasting massive clunky addresses, copy pasting ASCII qr codes. I see that the huge addresses aren't the only downside to the algos with huge addresses (pruned tx sizes seem lager too, which  [... too long, see https://mrelay.p2pool.observer/e/k7LugPwKNmRpTnpT ]     

> __< tevador >__ If the Monero-RPC accepts the new address format, I don't see a reason for a merchant not to support it.     

> __< jeffro256 >__ tevador: It is important because it hides where the wallet sent their funds. They would also gain importance once people realize the PQ implications and begin using self-sends as such      

> __< rucknium >__ Another question: Do these addresses get Monero closer, at all, to a countermeasure to PQ counterfeiting? I assume no, but I wanted to check.     

> __< tevador >__ No, this is purely for PQ privacy     

> __< jeffro256 >__ A QA can, in many circumstances, calculate the spending location of externally received funds, not just where they were received. So a self-send in between would hide the spend locations of those outputs     

> __< jeffro256 >__ rucknium: The mitigation of using ephemeral private keys for each tx would work. Note that your wallet scanning time would be O(N) for the number of pairs generated      

> __< tevador >__ Yes, but the QA learns the received amounts to the known address in any case, whatever you do afterwards, which is a biggest leak IMO.     

> __< rucknium >__ If the keys are designed to be single-use, then you could stop scanning after you found the first receive tx.     

> __< tevador >__ Addresses in Monero are not single-use.     

> __< jeffro256 >__ tevador: Fair      

> __< rucknium >__ Going back to 2009 😎     

> __< jeffro256 >__ tevador: There could a specific address format which singles "hey don't use this twice please"     

> __< jeffro256 >__ *signals      

> __< tevador >__ Single use addresses would prevent the whole-wallet leak, but don't prevent the main problem of leaking the receiving transaction.     

> __< jeffro256 >__ tevador: It's the biggest leak if trying to conceal income. Not the biggest leak if trying to conceal purchases      

> __< rucknium >__ I am developing the hypothetical with the sending adversary you don't trust fully, on privacy at least. So you would stop listening for txs after you got the one from the untrusted party.     

> __< tevador >__ I think you can already do this with a throwaway wallet seed.     

> __< rucknium >__ Yes. It would be a UX change.     

> __< jberman >__ tevador sorry if this is included somewhere, but why is the 2/16 tx size so much larger than the 2/2 tx size for NTRU-509 than it is for the other algos?     

> __< tevador >__ How would you do donation addresses with a single-use address format?     

> __< tevador >__ jberman: Good question. NTRU needs 16 ciphertexts in that case, but CSIDH needs just 1 shared public key for all 16 outputs in option A.     

> __< ixr3:matrix.org >__ It will take on tremendous importance! > <jeffro256> It is important because it hides where the wallet sent their funds. They would also gain importance once people realize the PQ implications and begin using self-sends as such      

> __< rucknium >__ BTCPay Sever does single-use addresses for Monero, which are used by at least one nonprofit for XMR donations. Just show each user a different address.     

> __< rucknium >__ Server*     

> __< rucknium >__ Just thinking outside the box here.     

> __< tevador >__ Do we want Monero to move to single-use addresses? Technically not publishing addresses ever (except to the sender) would solve the PQ privacy issue.     

> __< ofrnxmr >__ Tracking a lot of subaddresses begins to take its toll on scanning though, unless you stop scanning one once used?     

> __< rucknium >__ plowsof:matrix.org's Wishlist as a Service also shows each user a different address.     

> __< sgp_ >__ Single, static donation addresses have their place     

> __< ofrnxmr >__ What happens if someone sends 2 txs to the same address? Would the 2nd tx be rejected?     

> __< ofrnxmr >__ something like silent payments maybe?     

> __< jeffro256 >__ ofrnxmr: Not on CPU speed, just storage      

> __< tevador >__ I think these services would be vulnerable a denial of service by generating 1000s of addresses but never sending anything. Then the wallet has to keep scanning.     

> __< tevador >__ Also if interactive addresses are OK, we can just do this: https://github.com/monero-project/research-lab/issues/106     

> __< rucknium >__ I didn't intend to distract so much from your question, tevador, about the best PQ encryption algorithm for the addresses. Can we have more comments on the options from meeting participants?     

> __< jberman >__ I think privacy-preserving static addresses are a critical Monero feature     

> __< gingeropolous >__ agree re: jberman:monero.social     

> __< tevador >__ Btw, Jamtis brings other improvements to addresses apart from PQ privacy. PQ privacy was means as an extra feature.     

> __< rucknium >__ Reconsidering, if a service didn't offer the PQ addresses, then a competitor service could offer it. Market forces may squeeze out the non-adopter. Or at least there would be a good alternative for users who are aware of the quantum problem.     

> __< tevador >__ Technically we could still go with classical Jamtis, which has 260-char addresses.     

> __< jberman >__ I have a half debate in my head continuing about the acceptability of NTRU /  a lattice based algo. Your arguments in favor of CSIDH are strong tevador , that's still where my head is at though     

> __< rucknium >__ But many services have a lot of market power, i.e. close to a monopoly.     

> __< rucknium >__ I will put this agenda item closer to the beginning next meeting.     

> __< tevador >__ Thanks     

> __< rucknium >__ More comments on this item?     

> __< tevador >__ I didn't mention this, but NTRU and other KEMs have an extra issue in that the address generator tier can collude with the quantum attacker to deaononymize transactions.     

> __< tevador >__ CSIDH doesn't have this issue.     

> __< jpk68:matrix.org >__ Noob-ish question from me: is it really worth prioritizing smaller QR code sizes over shorter encoded address lengths? In my opinion, shorter addresses would be better from a UX perspective     

> __< jberman >__ tevador: ack     

> __< jpk68:matrix.org >__ (I'm referring to the use of Base32 over Base62/etc.)     

> __< ixr3:matrix.org >__ rucknium: No, but I want to thank tevador for this very important work. It's hard to follow alongside all other developments going on     

> __< tevador >__ base62 would shorten addresses only aby about 16%     

> __< tevador >__ QR codes would become larger by 45%     

> __< jpk68:matrix.org >__ Would there be any real-world difference when scanning/using the QR codes though? For example, would scanning a payment terminal be reasonably more difficult with higher-resolution QR codes?     

> __< jpk68:matrix.org >__ I mean, of course it would (with insanely large codes) but with the 45% larger ones, I mean     

> __< tevador >__ I'm not sure what is the max reasonable QR code size to scan with a phone     

> __< jeffro256 >__ Probably depends on camera quality and lighting     

> __< jbabb:cypherstack.com >__ Stack Wallet uses QR codes to exchange FROST information and we found that up to about 4000 chars is usable     

> __< jpk68:matrix.org >__ Just saying, from a UX perspective (in my opinion), a 16% decrease in address sizes is a 16% benefit for me. However a 45% larger QR code is about 0% less convenient, so long as the QR code is actually usable     

> __< tevador >__ What QR code size is that? in modules     

> __< rucknium >__ jbabb:cypherstack.com: Is that with zero error correction? IIRC, you can set different levels of error correction in a QR code.     

> __< tevador >__ I think Jamtis in base32 would be 69x69     

> __< jpk68:matrix.org >__ I know this is probably just bikeshedding, but I thought it would be worth bringing up     

> __< jbabb:cypherstack.com >__ tevador: 177x177, version 40 iirc, worked.  but version 10-20 (57x57 to 97x97) is better and i think everything fits under these, ill have to check what the actual payloads are in practice     

> __< tevador >__ 177x177 is the largest possible size AFAIK     

> __< jbabb:cypherstack.com >__ was awhile since that work was done.  versions 10-25 are practical imo     

> __< jbabb:cypherstack.com >__ rucknium: I will have to recheck these details sorry, twas awhile back we integrated kaya's frost     

> __< jpk68:matrix.org >__ I can't remember exactly, but when I looked into this a few days ago, the minimum QR code size that could be used for Base32 Jamtis addresses (13? 14?) had to be bumped up "only" two sizes from before     

> __< tevador >__ I think the encoding format can be resolved later anyways     

> __< tevador >__ I'm not opposed to base32 for the prefix + base62 for the data.     

> __< tevador >__ Yes, I think it would go from version 13 to 15     

> __< jpk68:matrix.org >__ xmr1a is valid Base62 though, no?     

> __< jpk68:matrix.org >__ Wrong prefix, oops     

> __< tevador >__ YEs, but the prefix also includes the 24-char checksum     

> __< jpk68:matrix.org >__ Oh, I see     

> __< tevador >__ This one should stay case insensitive for human readability     

> __< rucknium >__ We can end the meeting here. Feel free to continue discussing. Thanks everyone.     

> __< syntheticbird >__ lI     

> __< tevador >__ Thanks     

> __< ofrnxmr >__ I can generate a qr code right now for an example?     

> __< syntheticbird >__ which one is l which one is I     

> __< syntheticbird >__ Thanks     

> __< jpk68:matrix.org >__ Thanks     

> __< tevador >__ syntheticbird: In the prefix, that would be "li". In the data payload - nobody cares.     

> __< syntheticbird >__ i care     

> __< syntheticbird >__ I love handwriting a 1kB address     

> __< syntheticbird >__ 👍     

> __< rucknium >__ How would the PQ address work in hardware wallets? Is the checksum prefix enough to prevent accidental or malicious substitution of the address?     

> __< tevador >__ Answer here: https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#523-visual-checksum     

> __< rucknium >__ Thanks.     

> __< ofrnxmr >__ https://mrelay.p2pool.observer/m/monero.social/fVwXGtGNvWjJOqYRsboRbcoU.png (shared_barcode.png)     

> __< ofrnxmr >__ 621 chars, seems to scan fine     

> __< jpk68:matrix.org >__ In Base62?     

> __< ofrnxmr >__ most of it     

> __< vtnerd >__ Damn this may crush lwcli/monero-wallet-cli lol     

> __< syntheticbird >__ I am sure Claude mythos will find a way     

> __< sgp_ >__ https://mrelay.p2pool.observer/m/monero.social/qdkTlUpezMkKeNFQcMfRwtlD.png (version_40_test.png)     

> __< sgp_ >__ 2953 test     

> __< syntheticbird >__ sgp_: i'm unsure you can even grasp this thing with a 720p camera     

> __< jpk68:matrix.org >__ ofrnxmr: Works for me, up to around 6 feet away (average Android phone)     

> __< jbabb:cypherstack.com >__ scanned for me without even zooming it in. had to be 6in away from the screen tho     

> __< jbabb:cypherstack.com >__ strangely, zooming in didn't really help (scannable at about a foot from the screen)     

> __< tevador >__ Now make the version 40 qr code 5x5 cm and try to scan it     

> __< jpk68:matrix.org >__ sgp_: 2,953 characters of Bech32?     

> __< syntheticbird >__ The more we explore practicality the more I'm attracted to an online interactive system for making PQ transactions...     

> __< syntheticbird >__ even if not mandatory     

> __< ofrnxmr >__ i zoomed the pic out so its only like 5cm across     

> __< syntheticbird >__ You got this horror and most users will use a rendez-vous server to get the address. The QR code would just be the said server and a secret key     

> __< syntheticbird >__ just like some are having fun with openalias     

> __< ofrnxmr >__ Probabky too long for a dns txt entry 😅     

> __< syntheticbird >__ yeah i mean just the idea of having a shorter string to get to the address     

> __< ofrnxmr >__ sgp_: With a little zoom, this scanned at like 3x3cm     

> __< ofrnxmr >__ "this" = sgp's 2953 qr code     

> __< jpk68:matrix.org >__ Are you using a telescope? Lmao     

> __< syntheticbird >__ sgp_: almost looks artistic     

> __< syntheticbird >__ like the game of life     

> __< ixr3:matrix.org >__ sgp_:monero.social: How much time will you allow Vendor 4 to submit a counteroffer with a reduced timeline, given we must make a pre‑deposit to lock Vendor 1’s start date?     

> __< sgp_ >__ probably through Fri at the latest     

> __< syntheticbird >__ did someone just send a message with the wrong alt or ?     

> __< sgp_ >__ what';s the max length we are actually proposing, 1379?     

> __< ixr3:matrix.org >__ sgp_: They must be able to shorten the timeline for three possible audits. If they can commit to a reduced timeline for audit phase 1a/b but cannot for the potential phases 2 or 3, is that still a deal-breaker, given jberman intends to use the same auditor?     

> __< jpk68:matrix.org >__ Can someone smart please confirm: aside from the 30-char Base32 prefix, Jamtis addresses are 242 and 370 bytes decoded, for CSIDH-512 and -1024 respectively?     

> __< jpk68:matrix.org >__ I think my calculations are a bit off     

> __< sgp_ >__ https://mrelay.p2pool.observer/m/monero.social/XdLbvuYlkWaVmckQEjNVJLwo.png (version_40_test.png)     

> __< sgp_ >__ 4296 characters, alphanumeric (uppercase only)     

> __< ixr3:matrix.org >__ ixr3:matrix.org: jberman:monero.social:     

> __< jberman >__ I don't think we can request a commitment from them for the follow-up audits given we aren't actually committing to hire for the follow-up audits, it's just the preference      

> __< sgp_ >__ https://mrelay.p2pool.observer/m/monero.social/MTVWumvTpFxdlyPPXoslSOce.png (version_34-H_1379_test.png)     

> __< sgp_ >__ for 1379 characters alphanumeric, it fits in qr code version 34 with error correction level high     

> __< tevador >__ jpk68: the payload is 368 bytes for BC1024     

> __< sgp_ >__ version 22 with error correction low     

> __< tevador >__ So probably more like 617 chars in base32     

> __< UkoeHB >__ Why would QR codes be different sizes based on encoding? Can't encodings be translated? base-whatever -> QR code ideal -> QR code -> QR code ideal -> base-whatever     

> __< sgp_ >__ https://mrelay.p2pool.observer/m/monero.social/MCgKmpwjVqqvLrtKhUDsyuQG.png (image.png)     

> __< sgp_ >__ I'm just going off this     

> __< jpk68:matrix.org >__ QR codes apparently have different modes, so if you restrict yourself to a smaller charset (i.e. Base32) you can encode more efficiently     

> __< jpk68:matrix.org >__ I suppose one could encode the payload as a QR itself (in bytes)     

> __< UkoeHB >__ Sure, my question is why QR encoding has to equal address encoding.     

> __< tevador >__ UkoeHB: presumably we only want one address format (string). But yes, a binary address encoding would be tiny bit more efficient in QR codes     

> __< UkoeHB >__ 45% doesn't seem tiny, unless you mean relative to b32     

> __< syntheticbird >__ only a tiny ?     

> __< tevador >__ alphanumeric encoding encodes a 5-bit base32 character with 5.5 bits of encoding space, so the overhead is 10%     

> __< jberman >__ Updated the FCMP++ tx sizes table with the latest: https://github.com/seraphis-migration/monero/issues/317      

> __< jberman >__ Update: ~17% larger tx sizes, as opposed to the ~33% from before     

> __< jberman >__ We increased the tx reference weight from 10k bytes to 12.5k bytes before     




# Action History
- Created by: Rucknium | 2026-04-21T21:26:12+00:00
