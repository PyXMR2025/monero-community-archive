---
title: Monero Research Lab Meeting - Wed 02 July 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1231
author: Rucknium
assignees: []
labels: []
created_at: '2025-07-01T21:44:09+00:00'
updated_at: '2025-07-10T21:25:00+00:00'
type: issue
status: closed
closed_at: '2025-07-10T21:25:00+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3.  [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).

4. [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).

5. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

6.  CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).

7. Peer Scoring Metrics.

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1226 

# Discussion History
## Rucknium | 2025-07-06T14:45:49+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1231     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Set up a data pipeline and visualizer webapp for the Monero node network scanner. Repo: https://github.com/Rucknium/xmrnetscan Webapp: https://moneronet.info/ (not to be shared on social media yet). Continuing to monitor Qubic's hashpower share. Updated plots here: https://gist.github.com/Rucknium/0873b10b6d36ff6c9d6f8f54107d16f7     

> __< j​effro256:monero.social >__ Howdy     

> __< b​randon:cypherstack.com >__ yo. i finished up the latest draft of silver bullet and sent it along to kayaba. i will be around for a bit to answer any questions which have come up. when we are done copyediting, we will be putting it up on iacr     

> __< v​tnerd:monero.social >__ Me: updated jeffro256 mx255519 fork to support arm64 asm. Updated LWS API specs. Currently working on seeing if I can simplify the lws build process a bit     

> __< v​tnerd:monero.social >__ * the asm now does unclamped calculations correctly     

> __< s​yntheticbird:monero.social >__ Hello     

> __< a​rticmine:monero.social >__ I am finalizing scaling and fees after MoneroKon     

> __< a​rticmine:monero.social >__ For the most part the current fee structure can remain with FCMP++     

> __< a​rticmine:monero.social >__ There are some consensus changes to the Medians and transitional changes to accomodate FCMP++     

> __< j​berman:monero.social >__ me: reduced data stored per output in the curve tree, continued PR review, subaddress lookahead expansion     

> __< r​ucknium:monero.social >__ 3) [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).     

> __< r​ucknium:monero.social >__ Did kayabanerve complete his review of SLVer Bullet? Where do things stand?     

> __< k​ayabanerve:matrix.org >__ Not quite. I'm still working on mapping it into FCMP++.     

> __< r​ucknium:monero.social >__ surae/Goodell put up a thread about SLVer Bullet on BlueSky: https://bsky.app/profile/bggoodell.bsky.social/post/3lswc55nwhc2j     

> __< r​ucknium:monero.social >__ Anything more to discuss on this item?     

> __< r​ucknium:monero.social >__ 4) [FCMP++ optimization coding competition](https://www.getmonero.org/2025/04/05/fcmp++-contest.html).     

> __< r​ucknium:monero.social >__ The submission period for the competition has ended. Any info to share, jberman  and jeffro256 ?     

> __< j​berman:monero.social >__ We received 2 helioselene submissions, 1 divisors submission     

> __< j​berman:monero.social >__ Divisors submission so far looks very solid, pending further review (initial benchmark clocks in at 95%+ speed-up). We may not end up needing a blinds cache     

> __< g​ingeropolous:monero.social >__ hi, i've started fiddling with shadow, got it to at least run 2 nodes :/     

> __< s​yntheticbird:monero.social >__ Holy moly     

> __< r​ucknium:monero.social >__ 95%? Wow. How much does this operation account for, out of the whole tx verification?     

> __< s​yntheticbird:monero.social >__ Will author name be revealed ?     

> __< j​berman:monero.social >__ If the author wants yes     

> __< j​berman:monero.social >__ this is strictly blinds calculations on the proving side     

> __< j​berman:monero.social >__ does not affect verification     

> __< rbrunner >__ Just to be clear - it's almost twice as fast as the code is now?     

> __< r​ucknium:monero.social >__ Oh     

> __< j​berman:monero.social >__ Like 30 times as fast     

> __< k​ayabanerve:matrix.org >__ No, 30x.     

> __< g​ingeropolous:monero.social >__ wow     

> __< s​yntheticbird:monero.social >__ wow     

> __< rbrunner >__ Ah, I see. A bit strange to express that as "95% speed up", but yeah, wow :)     

> __< r​ucknium:monero.social >__ That means alpha stressnet can get more stressy :D     

> __< k​ayabanerve:matrix.org >__ Only provers benefit, so only sort of? Besides, provers could already cheat this if they wanted to.     

> __< r​ucknium:monero.social >__ I mean, if tx proving took a long time, then it would be hard to send a lot of txs on the stressnet, even with the blinds cache     

> __< k​ayabanerve:matrix.org >__ Unless the prover cheats, which they can.     

> __< s​yntheticbird:monero.social >__ Are there good news on the verification side?     

> __< r​ucknium:monero.social >__ Well, at least it avoids anyone needing to write "cheating" prover code specifically for the stressnet     

> __< r​ucknium:monero.social >__ (And what is this cheating, anyway?)     

> __< r​ucknium:monero.social >__ Oh, maybe make unspendable outputs?     

> __< k​ayabanerve:matrix.org >__ No. The divisor is used to prove a scalar multiplication. You can take one scalar and make a proof for it. That proof is then always usable for any instance of that scalar.     

> __< k​ayabanerve:matrix.org >__ Scalars shouldn't be reused, as it breaks the privacy of the scheme. If you don't care, you can reuse them however.     

> __< j​berman:monero.social >__ On helioselene: we have some thoughts on the submissions. Initial speed-ups clock in in the range of 20-40% as is, but have some issues that jeffro, kayaba and I have been discussing     

> __< j​effro256:monero.social >__ You can "cheat" by re-using divisors, which is bad for privacy in the real world, but allows you to create valid FCMPs really fast.     

> __< j​berman:monero.social >__ I'll get more into helioselene once we're done discussing divisors here     

> __< k​ayabanerve:matrix.org >__ There's also worse things you can do, but that's the trivial way to cheat.     

> __< r​ucknium:monero.social >__ I see. Maybe not a good idea to push that type of "cheating" code out into the wild, then, or someone might use it. Or ChatGPT would use it 😬     

> __< j​berman:monero.social >__ Ok going to continue on helioselene     

> __< j​berman:monero.social >__ The primary issue with both helioselene submissions is that they replace ed25519 arithmethic, which was not intended scope of the contest and we unfortunately did not explicitly rule it out in the contest rules (I also mistakenly told one contestant it was ok to swap out dalek-ff-group in a DM when they asked i.e. could replace ed25519, and the rules did not explicitly rule it out<clipped message>     

> __< j​berman:monero.social >__ ). One submission (the one I DM'd) is still over the 20% floor for validity swapping dalek's ed25519 back in. The other is trickier to swap back in and we don't know right now if it would still meet the bar     

> __< k​ayabanerve:matrix.org >__ I was invited to review the above and fundamentally disagree with that position.     

> __< k​ayabanerve:matrix.org >__ The libraries worked to a purpose and there was a reasonable intent the derivative libraries would work to the purpose. We explicitly included an arbitrary disqualification rule for any libraries which met the rules yet didn't meet the purpose.     

> __< k​ayabanerve:matrix.org >__ Both Helioselene submissions replaced the 2**255-19 field definition used, and in doing so, broke interoperability with the Ed25519 curve library used (where the Helioselene library implements a curve cycle whose entire purpose was interoperability with the Ed25519 curve).     

> __< rbrunner >__ So they work on their own alone, but not within the proposed framework?     

> __< k​ayabanerve:matrix.org >__ While it wasn't explicitly tested, and accordingly wasn't covered under the requirement tests pass, deleting functionality from the codebase is not a legitimate way to claim a faster codebase.     

> __< k​ayabanerve:matrix.org >__ There is the complexity in that jberman personally gave a clarification to a contestant claiming this would be legal, when I would say it absolutely shouldn't be.     

> __< k​ayabanerve:matrix.org >__ They will fundamentally not compile in the FCMP++ codebase and would require changes to the larger codebase.     

> __< rbrunner >__ And they are not that radically faster to make that look worthwhile     

> __< k​ayabanerve:matrix.org >__ With one submission, I was able to revert back to the existing definition without notable complexity. It still met the 20% minimum improvement criteria. It also included variable-time arithmetic and is accordingly invalid under that rule.     

> __< k​ayabanerve:matrix.org >__ With the other submission, I was unable to trivially revert back to the existing definition of Ed25519 due to how the library at large had been reworked. I accordingly cannot comment if it'd still meet the 20% criteria.     

> __< r​ucknium:monero.social >__ kayabanerve: Their original submission had variable-time arithmetic, not your edit?     

> __< k​ayabanerve:matrix.org >__ With those pain points aside, I'll note I'm personally disappointed neither submission implemented the Crandall-prime reduction which was a specific property tevador chose the field bespoke to Helios/Selene to have.     

> __< k​ayabanerve:matrix.org >__ Rucknium: Both libraries replaced the definitions of the representations of the mathematical finite fields. One did so with a bespoke implementation (a rather simple 256-bit representation, optimizing for how the 256th bit is unused as our fields only require 255 bits), and one did so with a distinct off-the-shelf integer representation.     

> __< k​ayabanerve:matrix.org >__ The bespoke implementation is the one which executes in variable time, and the one I was able to revert as required for potential usage in FCMP++.     

> __< r​ucknium:monero.social >__ And having variable-time disqualifies a submission, right?     

> __< k​ayabanerve:matrix.org >__ The one which used a distinct 'off-the-shelf' (it was forked and optimized to some degree my review has yet to cover, apologies for any handwaving there which is dismissive of work) implementation was the one I couldn't make legal for re-benchmarking and I'm unsure if it'd still meet the required performance metric after (as this may halve its performance gains, and it did not gai<clipped message     

> __< k​ayabanerve:matrix.org >__ n twice the required minimum).     

> __< k​ayabanerve:matrix.org >__ Correct, and that was an explicit rule.     

> __< k​ayabanerve:matrix.org >__ So to be a pedantic asshole, even with the exception granted, both of these submissions could be immediately disqualified leaving literally no one happy. While we could reconcile the good parts of the submissions, we'd still need the Crandall-prime reduction and associated bespoke finite field implementation to be optimal.     

> __< j​effro256:monero.social >__ Yes, technically it is explicitly illegal for the code to be variable time dependent on secret data. Although it can be argued whether or not a submission should be outright denied for variable timeness and the other aforementioned issues if there are other valid parts of the code that are usuable, and fixing those problems would result in the fastest now valid submission.     

> __< k​ayabanerve:matrix.org >__ Which leads us to jberman's suggestion.     

> __< j​berman:monero.social >__ Moving forward: I suggested we give both contestants 2 additional weeks to fix our major issues with their submissions, and allow them both the opportunity to improve their submissions (i.e. they can use a Crandall prime reduction, which is long term what we would hope to integrate into the helioselene lib)     

> __< rbrunner >__ Sounds pretty fair     

> __< k​ayabanerve:matrix.org >__ Sorry, clarifying:     

> __< k​ayabanerve:matrix.org >__ - The bespoke implementation present used `u128`, a Rust-language primitive which defers to the LLVM IR for 128-bit arithmetic. The LLVM IR is observed to generate variable time assembly for its 128-bit arithmetic on nontrivial platforms (and maybe also trivial platforms. Quick, who has an Amiga and a weekend to kill?)     

> __< k​ayabanerve:matrix.org >__ - The forked 'off-the-shelf' implementation, even with the exception granted to one participant universally applied (despite how they were unaware of this exception), forked a library and provided no attribution within the file tree. Beyond the rules regarding plagiarism (to be harsh), this arguably circumvents the 'no additional dependencies' rules by not adding a dependency to t<clipped message     

> __< k​ayabanerve:matrix.org >__ he dependency tree, yet inlining the 20 relevant files from the library into the Helioselene library. The library inlined WAS on the approved dependency list however, so it's a question of if a fork of a dependency counts as approved, what's a reasonable maintenance burden there, etc. Even beyond the ambiguity of 'is it a dependency* however, the lack of attribution *in file tree*<clipped message     

> __< k​ayabanerve:matrix.org >__  would be sufficient to disqualify for improper citations.     

> __< r​ucknium:monero.social >__ jberman and jeffro256 are named as the contest judges. That means they have final judgement, correct? What does jeffro256 think about this?     

> __< rbrunner >__ This is almost fractally complicated :)     

> __< r​ucknium:monero.social >__ I see a 👍 from jeffro256 on jberman's "Moving forward..."     

> __< r​ucknium:monero.social >__ Contract incompleteness theorem strikes again     

> __< k​ayabanerve:matrix.org >__ Yes, I'm solely a third-party advisor ready to be pedantic, please be aware I don't actually have a standing and now that I've played bad cop, the level-headed people may chime in.     

> __< r​ucknium:monero.social >__ Or is it a theorem? Anyway.     

> __< j​effro256:monero.social >__ If the contestants agree to it, I agree with the route of allowing 2 additional weeks to refine their submissions, where we explicitly lay out more explicit boundaries around desired behavior, and with the specific feedback for each submission. It will be awkward if one likes the idea, and the other doesn't...     

> __< k​ayabanerve:matrix.org >__ I don't hate we didn't explicitly require the Crandall reduction. I just wouldn't host the contest again. I would host the divisors contest again though, per my current understanding.     

> __< rbrunner >__ By the way, I believe to have seen some tritonn in the dev channel that wrote about running out of time. Maybe they could submit something with a 2-week extension, who knows     

> __< j​berman:monero.social >__ I will add that the second contestant (who forked a library and included in their submission) did ask us how we wanted them to proceed w.r.t attribution for that lib in their PR submission and did clarify where it came from. We missed it / didn't respond to that prior to the deadline     

> __< r​ucknium:monero.social >__ Whether the contestants are amenable to the extension may depend on how they would do (in XMR payments) without it.     

> __< k​ayabanerve:matrix.org >__ And I can fire back that it isn't up to us: it's up to the license they code was used under.     

> __< k​ayabanerve:matrix.org >__ Literally, I can't ask Microsoft how I should handle Apple source code. It's not up to them.     

> __< j​berman:monero.social >__ I personally think it would be most fair to the contestants who did get their submissions in time to have the opportunity     

> __< k​ayabanerve:matrix.org >__ I disagree with allowing more people in.     

> __< rbrunner >__ Understandable. It's complicated enough as it is     

> __< j​effro256:monero.social >__ rbrunner7: I had this same thought, but I lean towards agreeing with jberman on this one: it wouldn't be fair to the people who submitted in time. Especially since new participants now know where the benchmarks for the "leading" submission stands, whereas before they didn't know that information.     

> __< rbrunner >__ Makes sense     

> __< moneromooo >__ While I have no say in the matter, if no entry is valid, an extension of the contest is a totally fair outcome. Preventing other entries would be unfair. It would only be fair if at least one of the original submissions was valid.     

> __< k​ayabanerve:matrix.org >__ It's due to mixed legality of existing entries and of how there should've been a tighter loop for clarifications/submissions/responses to ensure legality, IMO.     

> __< moneromooo >__ (assuming the code for each entry is not public yet)     

> __< k​ayabanerve:matrix.org >__ Pedantically, none are legal IMO. Reasonably, one of these can be made legal in potentially a few hours.     

> __< j​effro256:monero.social >__ Yes, the Helios-Selene entries will remain private until further notice. The ec-divisors submission may be made public as soon as we get explicit confirmation from the author     

> __< rbrunner >__ If those two solutions, if possible to get rectified, hoover only around 20% improvement, that's still not very exciting. Is there hope for that "Crandall reduction" to make things substantially faster still?     

> __< r​ucknium:monero.social >__ And is the Crandall reduction modular, or would major parts of the submissions have to be re-written to include it?     

> __< k​ayabanerve:matrix.org >__ Yes rbrunner, and the two of them can still fight it out even if we disallow a third competitor, but if the argument is for a third competitor, so it is.     

> __< k​ayabanerve:matrix.org >__ Rucknium: It's related to how the underlying numeric data is represented, so while it's an algorithm and algorithms are implemented in code and rewritten and ported, it's not pleasant.     

> __< k​ayabanerve:matrix.org >__ But it's not an entire ZK proof, or blockchain. It's an algorithm to take 8 words on a 64-bit computer and reduce it to 4 words.     

> __< j​berman:monero.social >__ Another important element to consider here: it seems we may not spend any time integrating these solutions into the lib because the speed-up is not so drastic. With a bit of work, they can be what we would consider technically/pedantically valid submissions that also meet the 20% bar, but without a Crandall prime reduction, and with the relatively minor speed-up they realized, we <clipped message>     

> __< j​berman:monero.social >__ may not actually integrate them     

> __< rbrunner >__ True, but IMHO in the light of the contest that would be no real problem: Technically valid and best -> payout. Not useful for us, bad luck     

> __< j​berman:monero.social >__ Yea agree     

> __< j​effro256:monero.social >__ For better or worse, agreed.     

> __< k​ayabanerve:matrix.org >__ I prior said I'd consider this unfortunate and not worth repeating, but would move to accept a patched version of either library so long as they still clear the minimum performance bar.     

> __< k​ayabanerve:matrix.org >__ Except the divisors library seems to have done great, so it's less 'are contests worthwhile' and more 'why did one fail where one succeeded'     

> __< r​ucknium:monero.social >__ Low sample size. Hard to draw a conclusion :P     

> __< k​ayabanerve:matrix.org >__ We could take a survey. Surveys shows 97% of participants like taking surveys.     

> __< j​berman:monero.social >__ Ok, I still lean in favor of keeping it to the contestants because it's a small amount of work for them to "fix" their submissions relative to the work they've already done     

> __< r​ucknium:monero.social >__ Exactly. We don't know who looked at the contest and decided not to compete     

> __< r​ucknium:monero.social >__ IMHO, the decision belongs to jberman and jeffro256, including the timeline to make a decision. I think people can continue to give thoughts to them.     

> __< k​ayabanerve:matrix.org >__ Which is why they should only have two days, not two weeks, and even that should be considered generous. In fact, I say we require them eight hours from the end of this meeting, one work day. If the edits aren't done then, then the edits weren't so trivial as to justify this extension.     

> __< k​ayabanerve:matrix.org >__ /s, but I do feel two weeks is VERY generous compared to the amount of time expected for a presumed review + reconcile cycle.     

> __< s​gp_:monero.social >__ Two weeks for the two submitters seems the most reasonable to me. They may not love it but they'll like that more than being rejected     

> __< s​gp_:monero.social >__ And this is definitely a lesson in scoping imo. It's especially challenging for open contests because people may be incentived to win on a technicality. The incentive isn't to make the most useful submission, it's to win the game     

> __< rbrunner >__ Nicely put     

> __< r​ucknium:monero.social >__ The contest designers were smart to include the clause "You cannot win on a technicality", which they basically did     

> __< j​berman:monero.social >__ I did include this clause for this reason fwiw:     

> __< j​berman:monero.social >__ > We reserve the right to select a winner based on our discretion, and rule out submissions for reasons we may not have identified above. For example, if the fastest code has issues we did not identify above, we may select the 2nd fastest code. We aim to ship the winning code in Monero.     

> __< moneromooo >__ Giving those people more time but not others *is* unfair. Giving tiny amounts of time based on one's opinion of how much time is needed for those particular submissions is biased towards those submissions. Agree with the scoping fail point though.     

> __< k​ayabanerve:matrix.org >__ I feel the 20% rule largely helped with this, yet was surprisingly too low a bar given the unfortunately small sample size.     

> __< s​gp_:monero.social >__ People who didn't submit anything aren't entitled to anything ¯⁠\⁠_⁠(⁠ツ⁠)⁠_⁠/⁠¯     

> __< k​ayabanerve:matrix.org >__ Issues such as *not being interoperable with our Ed25519 lib when the entire point is Ed25519 interoperability*?     

> __< s​gp_:monero.social >__ Right, that's a fundamental issue     

> __< moneromooo >__ False. They're entitled to the same rules as others.     

> __< moneromooo >__ Rules that aren't made to fit those invalid submissions.     

> __< j​effro256:monero.social >__ Maybe we could look to other contests as how they handled similar situations?     

> __< a​ntilt:we2.ee >__ deadline is often adjusted equally for all     

> __< j​berman:monero.social >__ One (arguably worse) submission I personally wouldn't argue is invalid because of the licensing question (it's an open question if they would still meet the bar swapping dalek ed25519 back in). I think the other submission (that uses u128 arithmetic which as kayaba noted isn't constant time on all arches but can be fixed) appears superior at this point in time     

> __< j​berman:monero.social >__ > It would only be fair if at least one of the original submissions was valid.     

> __< j​berman:monero.social >__ One of the submissions I think has a reasonable claim at validity, but appears to be the worse submission, and going by this clause in the contest:     

> __< j​berman:monero.social >__ > We reserve the right to select a winner based on our discretion, and rule out submissions for reasons we may not have identified above. For example, if the fastest code has issues we did not identify above, we may select the 2nd fastest code. We aim to ship the winning code in Monero.     

> __< j​berman:monero.social >__ Gives us the right to rule it out for its inferiority     

> __< k​ayabanerve:matrix.org >__ Except they can't trivially swap ed25519 back in due to the extensive edits made.     

> __< r​ucknium:monero.social >__ You could decide that no extension will be given, and the contest ended with no acceptable submission.     

> __< k​ayabanerve:matrix.org >__ ^     

> __< j​berman:monero.social >__ Right that's another option. I think it's arguable that is a more fair outcome than opening the contest back up to everyone     

> __< r​ucknium:monero.social >__ 2-3 months of time was given, and this is all that the contest got     

> __< moneromooo >__ Closing with no winner can allow another contest, which is equivalent to a large extension for all (and allows for narrower scope).     

> __< rbrunner >__ For the joy of complicating things even more: We could close this and make a new contest :)     

> __< moneromooo >__ And existing entrants still have their code as a leg up.     

> __< k​ayabanerve:matrix.org >__ One submission illegally (US copyright law) included code, even if they asked us how to legally include it (when it's not our decision), and illegally (against the intended contest scope) replaced the Ed25519 field definition.     

> __< k​ayabanerve:matrix.org >__ One submission is variable time and replaced the Ed25519 field definition, but they were told that latter was okay.     

> __< rbrunner >__ Yes, I think the position to refuse to accept both is maybe not "nice", but defensible     

> __< moneromooo >__ Were they told using another lib was fine, or not using ed25519 was fine ? ie, was "another lib" (mis)understood as "another ed25519 lib" ?     

> __< k​ayabanerve:matrix.org >__ At this point, due to the trend of the debate, I'd say extend acceptance for two weeks to everyone, explicitly allow messaging jberman/jeffro256 for clarifications on rules, and one of them cannot unilaterally issue new clarifications. They need to talk it out with each other future.     

> __< k​ayabanerve:matrix.org >__ But it's not my contest :p     

> __< k​ayabanerve:matrix.org >__ it's either theirs, or it's the CCS's who holds the $$$     

> __< r​ucknium:monero.social >__ IMHO, rules clarification should happen in a public channel, e.g. #monero-dev:libera.chat     

> __< r​ucknium:monero.social >__ IIRC, the payment, if any, would come out of Core's general fund     

> __< a​ntilt:we2.ee >__ you may extend the d/l without giving reasons at all...      

> __< a​ntilt:we2.ee >__ we'r not in a hurry, are we     

> __< r​ucknium:monero.social >__ Or even as an edit to the rules in the GitHub repo     

> __< j​berman:monero.social >__ <m​oneromooo> Were they told using another lib was fine, or not using ed25519 was fine ? ie, was "another lib" (mis)understood as "another ed25519 lib" ?     

> __< j​berman:monero.social >__ They were told another lib was fine (they're still using ed25519, just using their own impl). Worth noting still, that submission is still over 20% when using the expected ed25519 lib     

> __< k​ayabanerve:matrix.org >__ We can require all rules clarifications be done via GH issues?     

> __< b​asses:matrix.org >__ their own implementation of ed25519? Does't that require another audit?     

> __< j​berman:monero.social >__ It can be done directly in the github readme     

> __< r​ucknium:monero.social >__ jberman: , jeffro256 : What do you want to do with this discussion? Do you have enough input to make a decision?     

> __< j​berman:monero.social >__ I'm not ready to make a decision yet but happy to hear further thoughts / continue the discussion after the meeting. I appreciate the points moneromoo and flip flop raised     

> __< r​ucknium:monero.social >__ 5) [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< r​ucknium:monero.social >__ I made this webapp: https://moneronet.info Like I said, not yet ready to share widely on social media, please     

> __< r​ucknium:monero.social >__ I think it has already given some actionable info: About 50% of honest reachable nodes have the DNS ban list enabled.     

> __< a​ntilt:we2.ee >__ 50% ?!     

> __< r​ucknium:monero.social >__ That means that it _would_ be worth it to update the DNS ban list to, at least, include all the big spy nodes subnets. The DNS banlist is "full", so a few singleton IPs would have to be dropped     

> __< r​ucknium:monero.social >__ That's according to my analysis. You can infer that a node has a ban list enabled if they share zero nodes on the ban list in their handshake. They share 250 IP addresses, selected from their white_list     

> __< moneromooo >__ It would be fairly trivial to bypass the "full" issue by checking other records. Besides, IP addresses can be represented by integers (ie, raw, not split into bytes).     

> __< r​ucknium:monero.social >__ It may be because SethForPrivacy recommended the DNS ban list flag     

> __< r​ucknium:monero.social >__ https://sethforprivacy.com/guides/run-a-monero-node/     

> __< r​ucknium:monero.social >__ https://sethforprivacy.com/guides/run-a-monero-node-advanced/     

> __< a​ntilt:we2.ee >__ sry - confused with --ban-list     

> __< r​ucknium:monero.social >__ moneromooo: I agree with that, but it would require an update to the `monerod` code, right?     

> __< moneromooo >__ Yes. I did not realize that was an obstable.     

> __< r​ucknium:monero.social >__ flip flop: Right. The MRL ban list has about 6% adoption.     

> __< r​ucknium:monero.social >__ AFAIK, nodes that check the DNS ban list will pull in the new list once per week, if they do not restart.     

> __< r​ucknium:monero.social >__ About 35% of honest reachable nodes are pruned. And 30% of honest reachable nodes say they have RPC available (But I did not check if they actually have that port open, yet).     

> __< rbrunner >__ That's already a considerable part of nodes pruned ...     

> __< r​ucknium:monero.social >__ The webapp also has an interactive treemap of spy/honest nodes and their subnets, like the static treemap in the draft MRL research bulletin. You can click on the boxes to get more info about each node. I don't think it's mobile-friendly, however.     

> __< r​ucknium:monero.social >__ I'm thinking about computing the Herfindahl-Hirschmann Index of the honest nodes, by subnet and Autonomous System Number (ASN) to measure node "concentration" through time.     

> __< r​ucknium:monero.social >__ The RPC numbers are of interest because they are nodes theoretically susceptible to any RPC vulnerabilities. The Magic Monero Fund has contracted a firm to create an RPC fuzzing harness to anticipate those vulnerabilities.     

> __< r​ucknium:monero.social >__ Any feedback on the webapp is welcome :)     

> __< r​ucknium:monero.social >__ Anything more on spy nodes?     

> __< r​ucknium:monero.social >__ 6) CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).     

> __< r​ucknium:monero.social >__ Earlier, gingeropolous said "hi, i've started fiddling with shadow, got it to at least run 2 nodes :/"     

> __< j​berman:monero.social >__ (ready to circle back to contest discussion next)     

> __< r​ucknium:monero.social >__ 7) Peer Scoring Metrics.     

> __< r​ucknium:monero.social >__ Anything on peer scoring metrics?     

> __< a​ntilt:we2.ee >__ would need a serious investment in time and also systems theory.     

> __< a​ntilt:we2.ee >__ nothing new. Exept: if a connection handshake for an anchor_node fails for whatever reason, its first_seen value is reset (its thrown out of the anchor_list).      

> __< a​ntilt:we2.ee >__ I'd keep it around for say three cx fails. But thats not how apl is designed currently. Just a theoretical thought for now.     

> __< r​ucknium:monero.social >__ Ok we can have the official end of the meeting here. And feel free to continue discussing topics, especially the coding competition. Thanks everyone.     

> __< j​berman:monero.social >__ On the contest:     

> __< j​berman:monero.social >__ New proposal: 1 week extension open to all, starting tomorrow. This gives the contestants a reasonably significant leg up compared to the field     

> __< j​berman:monero.social >__ And is the 1 week expectation kayaba initially stated     

> __< j​effro256:monero.social >__ I agree     

> __< j​berman:monero.social >__ Pinging kayabanerve moneromooo Rucknium sgp_ flip flop for potentially dissenting thoughts?     

> __< r​ucknium:monero.social >__ How would you intend to give notice of the deadline extension?     

> __< j​berman:monero.social >__ First, update the github repository. DM contestants. I can write a blog post expanding on it. And we can request monero twitter account broadcast it     

> __< r​ucknium:monero.social >__ Maybe, the people who had private forked repos, but did not submit, could be notified by some GitHub magic.     

> __< r​ucknium:monero.social >__ A blog post on getmonero.org may take a while to get deployed, FWIW     

> __< j​berman:monero.social >__ Sure, maybe no blog post then     

> __< r​ucknium:monero.social >__ Sounds OK to me. I like this passage from the `Complete contract` entry in Wikipedia:     

> __< r​ucknium:monero.social >__ > A complete contract is an important concept from contract theory. If the parties to an agreement could specify their respective rights and duties for every possible future state of the world, their contract would be complete. There would be no gaps in the terms of the contract.     

> __< r​ucknium:monero.social >__ > However, because it would be prohibitively expensive to write a complete contract, contracts in the real world are usually incomplete. When a dispute arises and the case falls into a gap in the contract, either the parties must engage in bargaining or the courts must step in and fill in the gap.     

> __< r​ucknium:monero.social >__ So, this is normal and a judgement must be made     

> __< 3​21bob321:monero.social >__ Mrl needs social media presence     

> __< j​berman:monero.social >__ Btw, the divisors contestant has made their submission public :) https://github.com/fabrizio-m/fcmp-competition/pull/1     

> __< rbrunner >__ Was that monumental speedup very surprising? Did you nearly "fall from your chair" when you saw what they did?     

> __< j​berman:monero.social >__ Yes :) Appears to be using a mathematical method I hadn't heard of before and "deserves to be known as the standard method of polynomial interpolation": https://people.maths.ox.ac.uk/trefethen/barycentric.pdf     

> __< s​yntheticbird:monero.social >__ Adding it to the endless list of things i need to learn after having assimilated the basics 📝     

> __< a​ck-j:matrix.org >__ Fabrizio was a zprize contestant (potentially winner IIRC) that we reached out to during the “marketing push” but he responded he might not have enough free time. Glad he found some time :)     

> __< r​ucknium:monero.social >__ Wow. Great job, xmrack !     

> __< a​illia:matrix.org >__ ? https://xcancel.com/MoneroResearchL/status/1940497078201078035     

> __< a​illia:matrix.org >__ you mean TikTok 🤭? https://xcancel.com/MoneroResearchL/status/1940497078201078035     

> __< d​iego:cypherstack.com >__ 5 TikTok dances you can do to help Monero research     

> __< 3​21bob321:monero.social >__ Batman listened !     

> __< 3​21bob321:monero.social >__ Also get a federated social media account, we are opensauce     

> __< j​effro256:monero.social >__ Would be nice if the MoneroResearchL twitter account clarified that this was for *Helios-Selene only*, not for divisors     

> __< 3​21bob321:monero.social >__ Maybe in the meetings discuss what mrl wants to post     

> __< j​effro256:monero.social >__ I have no idea who runs the account...     

> __< 3​21bob321:monero.social >__ Batman please wait for mrl meetings before posting     



# Action History
- Created by: Rucknium | 2025-07-01T21:44:09+00:00
- Closed at: 2025-07-10T21:25:00+00:00
