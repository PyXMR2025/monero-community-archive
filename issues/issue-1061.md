---
title: Monero Research Lab Meeting - Wed 21 August 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1061
author: Rucknium
assignees: []
labels: []
created_at: '2024-08-21T16:50:18+00:00'
updated_at: '2024-09-03T20:39:50+00:00'
type: issue
status: closed
closed_at: '2024-09-03T20:39:50+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1057 

# Discussion History
## Rucknium | 2024-08-26T20:24:16+00:00
Log

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1061     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< o​ne-horse-wagon:monero.social >__ Hello.     

> __< a​rticmine:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< k​ayabanerve:matrix.org >__ Managing academia, largely.     

> __< j​berman:monero.social >__ *waves*     

> __< j​berman:monero.social >__ continuing fcmp++ integration, opened a new CCS     

> __< r​ucknium:monero.social >__ me: Finishing initial research on boog900 's transaction relay proposal: https://github.com/monero-project/monero/issues/9334 . I will post it in a few hours. Also discovered that you can natively render LaTeX in GitHub comments now :D     

> __< r​ucknium:monero.social >__ 3) Stress testing `monerod` https://github.com/monero-project/monero/issues/9348     

> __< r​ucknium:monero.social >__ 0xfffc has a WIP PR to implement dynamic block sync size: https://github.com/spackle-xmr/monero/pull/26     

> __< r​ucknium:monero.social >__ In the previous stressnet we encountered a limit when the block sync size was set to the default 20. Too much data in 20 blocks. Then we cut block sync size to 1 to be safe, but that's inefficient.     

> __< 0​xfffc:monero.social >__ Hi everyone. I am debugging the dynamic-bss algorithm. I will be absent from today's meeting. my apologies. ( if you want to take a quick look, you can find the code here: https://github.com/0xFFFC0000/monero/pull/35 )     

> __< r​ucknium:monero.social >__ Stressnet is actually not being spammed right now. AFAIK, we will merge this dynamic BSS code plus the newest Monero release code and then start spamming to test it.     

> __< r​ucknium:monero.social >__ Anything else about stressnet?     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< j​effro256:monero.social >__ howdy     

> __< j​effro256:monero.social >__ that BSS PR doesn't touch the serialization limits, right?     

> __< k​ayabanerve:matrix.org >__ GBP review is almost back (should have a shareable copy in a couple hours) and should be good to move forward with. It opened a new topic on quantifying security, former and upcoming, which may be worth spending the time on.     

> __< 0​xfffc:monero.social >__ 1. Not directly. But indirectly can user have huge values for their BSS size.      

> __< 0​xfffc:monero.social >__ 2. Serialization limit proposal is here and approved ( https://github.com/monero-project/monero/pull/9433 ).  Although obviously extra reviews can help.     

> __< r​ucknium:monero.social >__ Quantifying security meaning N-bit security?     

> __< 0​xfffc:monero.social >__ "New serialization limit" I should say.     

> __< k​ayabanerve:matrix.org >__ Goodell did the GBP review and raised this note, so they'd be an obvious candidate to do such work, yet I believe they're unavailable. Considering we in general don't have researchers to spare, I'd kick the work to the backburner.     

> __< k​ayabanerve:matrix.org >__ Rucknium: Yes, there's a question of if on paper, we should be using 700-bit elliptic curves even today.     

> __< k​ayabanerve:matrix.org >__ The security of GBPs should follow BPs and shouldn't aggravate the problem though.     

> __< k​ayabanerve:matrix.org >__ And that 'on paper' number is largely worthless. The open question was raised for more precise quantification however.     

> __< k​ayabanerve:matrix.org >__ So it isn't in any way a delay to GBPs and their deployment.     

> __< k​ayabanerve:matrix.org >__ Once that's published, we can move forward with auditing the GBP crate I wrote? I believe that's ready and I'll commit my final touches.     

> __< k​ayabanerve:matrix.org >__ The divisor review by CS came back. I forgot if we discussed that. The technique itself holds. Aaron was concerned about the method of taking the logarithmic derivative being unspecified *and* the lack of an exact proof being specified premised on the technique.     

> __< k​ayabanerve:matrix.org >__ I did specify an exact proof, somewhat. I wrote out the exact R1CS gadget, defined how it's instantiated, etc. That was part of Veridise's work conducted while Aaron reviewed the technique itself.     

> __< k​ayabanerve:matrix.org >__ Veridise did share their review with me, as it stands. It correctly takes the logarithmic derivative per their confirmation, and is secure, except for an open question on how I handled some variables.     

> __< k​ayabanerve:matrix.org >__ The technique assumes all variables are positive. That definition loses meaning over a prime field. Numbers are [0, p). The best definition would likely be [0, p/2]? But even that is largely meaningless.     

> __< k​ayabanerve:matrix.org >__ So the next step re: Veridise would presumably be to have them respond to Aaron's review, expand on variables being 'positive' when applied to a prime field (expanding the security proofs as necessary/clarifying them), and update their review of the gadget itself.     

> __< k​ayabanerve:matrix.org >__ Then to kick that back to Aaron.     

> __< k​ayabanerve:matrix.org >__ I'll also note I personally consider the technique being proven yet the application of the technique being questioned the first hitch in this academic process, and effectively a perfect exemplification of Aaron's concerns.     

> __< k​ayabanerve:matrix.org >__ cc Aaron Feickert: who I forgot to ping, sorry.     

> __< k​ayabanerve:matrix.org >__ I'm still discussing hours and timeline with Veridise to get the quote there. The MRL prior approved a limited set of extended hours (I believe bringing Veridise's total approved expenditure up to ~15k). I'm unsure how those hours have been exhausted.     

> __< k​ayabanerve:matrix.org >__ We can get the quote and discuss it at the next meeting or continue discussing approving extended hours. I'll also contextualize even with this discussion, I believe Veridise is still less than the other quotes we received. I don't have an inclination either way as I don't like how handwavy I'm being and not having the firm numbers in front of me.     

> __< k​ayabanerve:matrix.org >__ TL;DR 1) GBPs should be able to move to auditing. 2) Divisors had a hitch in conversion to a proof we're following up on.     

> __< r​ucknium:monero.social >__ So Veridise would be asked to create a new proof of a new proposition or repair a proof?     

> __< k​ayabanerve:matrix.org >__ I've also now asked 3 researchers regarding investigating our HtP to no success yet.     

> __< k​ayabanerve:matrix.org >__ That summarizes research, can hand over to jberman for development.     

> __< r​ucknium:monero.social >__ HtP = Hash-to-point. The one that exists now on mainnet     

> __< k​ayabanerve:matrix.org >__ I don't know if they'd provide the necessary commentary on why integers over a prime field qualify as positive, or if they'd remove the bound on it being positive.     

> __< k​ayabanerve:matrix.org >__ I discussed the work with Veridise's researcher and they seemed to enjoy the work and want to continue, and also believed (with their initial thoughts as a fallible person) it'd be resolvable.     

> __< k​ayabanerve:matrix.org >__ I do support their continued engagement. Their researcher has an extensive track record regarding fields, and their rates have been solid, so I do think they're still the best fit.     

> __< k​ayabanerve:matrix.org >__ And yes, sorry for the unexplained acronym.     

> __< r​ucknium:monero.social >__ "We can get the quote and discuss it at the next meeting or continue discussing approving extended hours. " Is this something to discuss at this meeting? I don't know the difference between these two options.     

> __< k​ayabanerve:matrix.org >__ If y'all agree it makes sense to continue the work, and want to approve *some* hour extension even though I don't have the details on it, that'd be at this meeting.     

> __< k​ayabanerve:matrix.org >__ If we want to quantify the expected extension, current used hours, running total, and new total (upper bound based on hours), I need to wait for their updated quote.     

> __< r​ucknium:monero.social >__ Maybe state a reasonable limit now and we can get loose consensus for that limit. If the new "quote" exceeds the limit, then come back next meeting     

> __< k​ayabanerve:matrix.org >__ I think the latter feels better but I also don't think there's a practical issue with the former and it may get things dome a few days faster, but eh, a few days isn't the end of the world.     

> __< k​ayabanerve:matrix.org >__ Setting a limit on our end so we do properly quantify it, despite the unknown quantities, also works out.     

> __< r​ucknium:monero.social >__ Although no one else is talking so it's  hard to measure loose consensus :)     

> __< k​ayabanerve:matrix.org >__ I'd expect 5-10k to be the scale of extended work.     

> __< j​effro256:monero.social >__ Most of this stuff is over my head, I don't know how to evaluate how much this work should cost ;)     

> __< j​effro256:monero.social >__ How much of the original CCS fund has been exhausted BTW?     

> __< k​ayabanerve:matrix.org >__ Though I'll practically note 10k, that upper bound, may put us a few k past Cypher Stack raising the question of if we could've gotten more affordable work by choosing them originally. I think that depends on if Aaron would've done the work successfully to this depth, and if work was kicked back to me on issue, it was graced into the existing work without additional cost. Somethin<clipped message     

> __< k​ayabanerve:matrix.org >__ g to potentially consider in the future, despite our inability to change the past.     

> __< k​ayabanerve:matrix.org >__ I also don't regret it as Aaron has done the review and if we didn't have Aaron do the review, we'd need another entity for that purpose which... would've been back to Veridise?     

> __< k​ayabanerve:matrix.org >__ I'll pull up how much of the CCS has been exhausted... I believe less than or about half.     

> __< j​effro256:monero.social >__ Without knowing too much about the depth of work, 10k is a reasonable enough extension...     

> __< k​ayabanerve:matrix.org >__ Initial GBP review was a separate CCS     

> __< k​ayabanerve:matrix.org >__ GBP review by Goodell - still pulling up the amount     

> __< k​ayabanerve:matrix.org >__ Veridise on divisors - ~15k USD     

> __< k​ayabanerve:matrix.org >__ CS on composition review @ 198 XMR     

> __< k​ayabanerve:matrix.org >__ CS on divisor review @ 38 XMR     

> __< k​ayabanerve:matrix.org >__ That's the only scopes done under this CCS at this time. We haven't moved to code audits.     

> __< j​effro256:monero.social >__ I did have a gut feeling that Veredise might have underestimated the work somewhat given the disparity of the quotes, but it seems like they have been doing good work thus far     

> __< k​ayabanerve:matrix.org >__ So I'd have to ask sgp_: how much XMR they received for the 10k USD initially for Veridise.     

> __< k​ayabanerve:matrix.org >__ Goodell was 20-24k USD.     

> __< k​ayabanerve:matrix.org >__ So 40k USD liability and 240 XMR of 2000 XMR raised.     

> __< k​ayabanerve:matrix.org >__ *236 to be specific.     

> __< s​gp_:monero.social >__ MAGIC's current balance for an audit program is $5,151.73, though I believe I am waiting on an invoice from Veridise     

> __< k​ayabanerve:matrix.org >__ 300 grand if 150 a XMR, now just 225 grand. We have only spent 25% of the CCS.     

> __< k​ayabanerve:matrix.org >__ sgp_: I was asking the XMR quantity you received for the 10k USD MAGIC handled.     

> __< s​gp_:monero.social >__ 70 I think? I need to check     

> __< r​ucknium:monero.social >__ IMHO, 10K USD to Veridise would be acceptable, but 5K is more reasonable since AFAIK they are sort of fixing a hole in the original work.     

> __< s​gp_:monero.social >__ yes, MAGIC received 70 XMR     

> __< k​ayabanerve:matrix.org >__ In that case, 306 XMR spent with a ~27k USD liability.     

> __< k​ayabanerve:matrix.org >__ I'll keep 10k as the upper limit approved, barring objections here. I'd like Veridise in total to still be cheaper than other quotes we received so I'd try and keep notably under that.     

> __< j​berman:monero.social >__ On the alternative of having gone with CS from the start: to be clear you're saying CS may have caught this issue (this issue that Aaron identified reviewing the application of the technique) that Veridise did not, and so it may have made sense to go with CS from the start?     

> __< k​ayabanerve:matrix.org >__ Another candidate, who provided a flat quote, may have successfully performed and upon noting the positive bound didn't enable a proof in practice, removed that bound successfully.     

> __< k​ayabanerve:matrix.org >__ If Veridise's work ends up more expensive than the flat quotes we received as we pay by the hour for this unexpected edge, then yes, for this work it'd have made sense to go with a flat quote (assuming their success).     

> __< k​ayabanerve:matrix.org >__ Though again, Veridise would then become the candidate for proof review so the quotes for review would change. It's impossible to comment in totality.     

> __< k​ayabanerve:matrix.org >__ I'm just being mindful of this position and trying to be responsible about that it.     

> __< j​berman:monero.social >__ Got it. Sounding like a natural review process to me. 10k seems a reasonable upper bound to me, especially considering that's still within the ballpark of the altnerantive quote     

> __< r​ucknium:monero.social >__ Hopefully Veridise aren't reading this chat and know our exact negotiation limits :P     

> __< k​ayabanerve:matrix.org >__ To be clear, Aaron's review was there was a lack of a proof provided by Veridise. That was because I provided a proof. When they moved to reviewing my proof, they didn't mesh seamlessly, creating this hitch.     

> __< k​ayabanerve:matrix.org >__ We already have an hourly rate. I'm not saying it's static across the now months we've been working together, but them changing their rates would be explicitly discussed.     

> __< k​ayabanerve:matrix.org >__ *When Veridise moved to reviewing my proof     

> __< r​ucknium:monero.social >__ I think we have loose consensus to go forward if their quote is 10K USD and below. If above, then bring the quote to the next MRL meeting.     

> __< r​ucknium:monero.social >__ 5) Confirm next meeting agenda     

> __< r​ucknium:monero.social >__ I want to ask if boog900 , 0xfffc , and vtnerd  want to discuss possible next-generation transaction relay protocols for Monero next MRL meeting, especially this proposal: https://github.com/monero-project/monero/issues/9334     

> __< r​ucknium:monero.social >__ Or another meeting date is OK too. Or never, but that's not as good ;)     

> __< 0​xfffc:monero.social >__ ( quick update: I am close to finishing BSS PR, final testing right now. Once finished, I will work on 9334 full capacity. )     

> __< r​ucknium:monero.social >__ Maybe MRL should discuss if issue #9334 is a good idea first :D     

> __< r​ucknium:monero.social >__ IMHO, it has some privacy issues that might be fixed by injecting some noise     

> __< a​rticmine:monero.social >__ This broadcast proposal is critical for determining bandwidth propagation limits for scaling     

> __< a​rticmine:monero.social >__ Limiting unnecessary tx broadcasts     

> __< plowsof >__ Kayabanerve 70 from ccs to magic     

> __< plowsof >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/blob/master/fcmp++-research.md     

> __< 0​xfffc:monero.social >__ In my opinion it is critical too. Bitcoin is using it right now IIRC.     

> __< 0​xfffc:monero.social >__ ( approach similar to 9334 )     

> __< r​ucknium:monero.social >__ Yes there is a lot of wasted bandwidth now. Adding some "pull" methods can allow an adversary to query a node's transaction pool.     

> __< 0​xfffc:monero.social >__ I am sure there are some defensive mechanism for that. I have to look at the literature.     

> __< r​ucknium:monero.social >__ I already have. That's the comment I will post in a few hours     

> __< r​ucknium:monero.social >__ The comment is about where the risks come from (black hole attack scenario and network topology learning) and what some of the options are.     

> __< r​ucknium:monero.social >__ We can end the meeting here.     

> __< 0​xfffc:monero.social >__ Great. Thanks :)     

> __< a​rticmine:monero.social >__ Thanks for hosting     

> __< b​oog900:monero.social >__ Rucknium: yeah I would be happy to discuss that next meeting, I'm waiting for your comment on 9334 but FWIW 9334 does not make the problem worse, we already have methods to directly query a nodes pool + some other methods that allow it as a side effect.     

> __< b​oog900:monero.social >__ IMO we shouldn't delay work on 9334 when we are still exposed to this attack vector.     

> __< b​oog900:monero.social >__ I have also been thinking about ways we can stop peers from using the new messages in 9334 to query a nodes pool, and one way would be to send a 1 byte random token with the tx hash and require this same token to be sent when the tx is requested     

> __< b​oog900:monero.social >__ Slightly more data would need to be sent but still a lot better than the current protocol     

> __< r​ucknium:monero.social >__ boog900: Yes, those existing methods could be modified     

> __< r​ucknium:monero.social >__ Maybe it could be rushed, but is that necessary? Have all the options been evaluated? Will more technical debt be created if #9334 is implemented, then a better way is discovered?     

> __< r​ucknium:monero.social >__ Probably it would be good to have the next generation relay protocol ready for the next hard fork.     

> __< r​ucknium:monero.social >__ The bandwidth could be cut in half without new methods by setting a maximum limit on the connection fluff timer. If above the 50 percentile, then don't relay.     

> __< r​ucknium:monero.social >__ I don't think that's a good long-term solution, but it's just another option     

> __< b​oog900:monero.social >__ To completely remove this attack vector would not be a small task IMO     

> __< b​oog900:monero.social >__ Rucknium: do we have numbers on how knowledge of the P2P graph affects D++ stem stage     

> __< r​ucknium:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ Section "How much does p2p network topology discovery help an adversary link a transaction to an IP?" of my https://github.com/monero-project/monero/pull/9218#issuecomment-2260917643     

> __< r​ucknium:monero.social >__ Actually some of the D++ paper's graphs are hard to interpret since their scales have just one labeled tick     

> __< r​ucknium:monero.social >__ and they are log-scaled     

> __< r​ucknium:monero.social >__ So I tried my best to use eyeballs. Their simulation code is open source on GitHub (recently updated for Python3) so we could re-run a lot of that     

> __< b​oog900:monero.social >__ Fig 3 is made with knowledge of the anonymity graph right?     

> __< b​oog900:monero.social >__ anonymity graph = exact 4-regular     

> __< b​oog900:monero.social >__ graph in this case     

> __< r​ucknium:monero.social >__ IIRC, the Max Weight estimator is what the adversary would use if it knows the p2p graph     

> __< r​ucknium:monero.social >__ I think knowing the private subgraph (4-regular) or the p2p wasn't completely clear from how they explained it, but later in the paper it looks like they mean knowledge of the p2p graph     

> __< b​oog900:monero.social >__ `On the other hand, if a 4-regular graph is unknown to the adversary, it has a precision very     

> __< b​oog900:monero.social >__ close to that of line graphs (orange solid line in Figure 3). But if the graph becomes known to the     

> __< b​oog900:monero.social >__ adversary (orange dotted line), the increase in precision is smaller. At p = 0.15, the gain is 0.06—half     

> __< b​oog900:monero.social >__ as large as the gain for line graphs. This suggests that 4-regular graphs are more robust than lines     

> __< b​oog900:monero.social >__ to adversaries learning the graph, while sacrificing minimal precision when the adversary does not     

> __< b​oog900:monero.social >__ know the graph.`     

> __< r​ucknium:monero.social >__ Ah. Hm. I was looking at appendix C too.     

> __< b​oog900:monero.social >__ I think C is also talking about knowledge of the anonymity graph:     

> __< b​oog900:monero.social >__ `However, Figure 15 illustrates the average precision for an adversary that     

> __< b​oog900:monero.social >__ knows both the graph and the internal routing decisions of each node. Here, the trend is reversed:     

> __< b​oog900:monero.social >__ line graphs have a precision that is upper bounded by p, whereas on 4-regular graphs, the precision     

> __< b​oog900:monero.social >__ can be higher than p. This makes sense because on line graphs, each node has only one possible     

> __< b​oog900:monero.social >__ routing decision, so the additional routing knowledge of the adversary does not help.`     

> __< r​ucknium:monero.social >__ I think you could be right. I was thinking they were talking about the overall p2p graph since their earlier paper of bitcoin diffusion analyzed what additional accuracy an adversary could get from knowing the p2p graph. So maybe the D++ paper doesn't analyze how an adversary could use the overall p2p graph to de-anonymize the stem phase.     

> __< r​ucknium:monero.social >__ At the end of Appendix C, they say that an attack to learn the routing dicisions (deeper knowledge than just the 4-regular graph) is very expensive. Basically Sharma, Gosain, & Diaz (2022)  took that as a challenge and developed an estimator and simulations of how to learn the 4-regular private subgraph https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=130     

> __< r​ucknium:monero.social >__ Sharma, Gosain, & Diaz (2022)  needed to create an unreasonable (IMHO) large number of transactions per node to estimate the private subgraph. AFAIK they needs the overall p2p graph first to run their estimator.     

> __< r​ucknium:monero.social >__ But knowledge of the p2p graph still helps an adversary that black holes a transaction since honest node(s) in the preceding stem path go into fluff mode.     

> __< r​ucknium:monero.social >__ There are other attacks that use knowledge of the network graph like 0-conf double spending, partitioning, and eclipse. (But some researchers think these attacks are hard to execute anyway.)     

> __< r​ucknium:monero.social >__ Granted, those same researchers said "please use our new protocol that makes the p2p graph public, because those possible attacks aren't so bad."     

> __< r​ucknium:monero.social >__ Same researchers that suggested the Clover protocol as an alternative to D++     

> __< r​ucknium:monero.social >__ I'll revise my comment on PR #9218. Thanks for catching my misinterpretation, boog900     

> __< 0​xfffc:monero.social >__ ( I skimmed this last week. Basically very similar to dandelion++. I didn’t see a substantial redesign. )     

> __< b​oog900:monero.social >__ ehh it is different, from routing txs from inbound peers to other inbound peers and vice versa for outbound peers.     

> __< b​oog900:monero.social >__ My initial thoughts are it probably is an improvement from D++ given that peers that don't accept inbound connections are not useful for D++ but I agree with Rucknium that they did not do as deep a dive as the D++ paper.     

> __< b​oog900:monero.social >__ according to the clover paper only 10% of the Bitcoin network is reachable 

# Action History
- Created by: Rucknium | 2024-08-21T16:50:18+00:00
- Closed at: 2024-09-03T20:39:50+00:00
