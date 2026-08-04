---
title: Monero Research Lab Meeting - Wed 29 July 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1431
author: Rucknium
assignees: []
labels: []
created_at: '2026-07-27T17:13:23+00:00'
updated_at: '2026-08-03T14:57:32+00:00'
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

3. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). [FCMP++ Integration Audit Overview](https://github.com/seraphis-migration/monero/issues/294).

4. [Relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

5. [Shi, Zhang, Ge, Lan, Zhang, & Wang (2026) "Deanonymizing Monero Transactions in Tor Network."](https://arxiv.org/abs/2607.07062)

6. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1426  

# Discussion History
## Rucknium | 2026-08-03T14:57:32+00:00
Logs

> __< rucknium >__ Trail of Bits audit of the FCMP++ integration Phase 1: https://github.com/trailofbits/publications/blob/master/reviews/2026-07-magicgrants-monerofcmp++crypto-securityreview.pdf     

> __< rucknium >__ It was already shared in the #no-wallet-left-behind:monero.social  channel.     

> __< rucknium >__ MRL meeting in this room in two hours.     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1431     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ hi     

> __< boog900 >__ hi     

> __< DataHoarder >__ hallo     

> __< tevador >__ Hi     

> __< rbrunner >__ Hello     

> __< jpk68:matrix.org >__ Hello     

> __< syntheticbird >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jfuffjcjkdrngisozkfng:matrix.org >__ Hi     

> __< jberman >__ waves     

> __< rucknium >__ me: Keeping stressnet stressed and investigating bugs on it. Read Shi, Zhang, Ge, Lan, Zhang, & Wang (2026) "Deanonymizing Monero Transactions in Tor Network." (https://arxiv.org/abs/2607.07062)     

> __< articmine >__ Hi     

> __< DataHoarder >__ stressnet/scanning updates and checking all the new incoming changes to FCMP++/Carrot for post-stressnet changes (and updating my libraries)     

> __< tevador >__ me: mx25519 + relative time-locks     

> __< vtnerd >__ me: hopefully done with p2p-write-starvation, and working on checking all my outstanding prs/branches (mainly ssl and fcmp++)     

> __< boog900 >__ I posted an update on Cuprate's RPC here: https://github.com/monero-project/meta/issues/1428#issuecomment-5107322419 it has graphs which compares how both scale with more wallets, thought it could interest some people here.     

> __< jpk68:matrix.org >__ Me: continued work on I2P-related things, reviewing a few PRs, squashing some bugs in hardware wallet code     

> __< gingeropolous >__ me: started using monerosim to test some things. fiddled with / added cuprate support     

> __< jberman >__ me: continuing FCMP++ integration PR, the Trail of Bits audit was released:  https://github.com/trailofbits/publications/blob/master/reviews/2026-07-magicgrants-monerofcmp++crypto-securityreview.pdf. With rucknium's help, should hopefully have beta stressnet v2.1 out by next week that solves the wallet's sporadic errors (reviewing to make sure all fixes are working as intended)     

> __< rucknium >__ FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). FCMP++ Integration Audit Overview (https://github.com/seraphis-migration/monero/issues/294).     

> __< rucknium >__ Agenda item 3 ^     

> __< rucknium >__ Last meeting, some participants wanted to wait for the Trail of Bits audit before making decisions on some FCMP timeline items. It's here now: https://github.com/trailofbits/publications/blob/master/reviews/2026-07-magicgrants-monerofcmp++crypto-securityreview.pdf     

> __< rucknium >__ Is right now a good time to discuss it?     

> __< jberman >__ Here's the latest FCMP++ integration PR with some discussion there on next steps to get that code in: https://github.com/monero-project/monero/pull/10359     

> __< jberman >__ Sure     

> __< rucknium >__ Does anyone want to elaborate on what Trail of Bits means by the Rust-C++ Foreign Function Interface (FFI) being "fragile"?     

> __< rucknium >__ And that was the only issue they found that was not completely resolved by a fix.     

> __< jberman >__ They mean that if the upstream type changes and/or is written to on the C/C++ side, it may be rendered incorrect. Since the upstream type comes from another lib (a fork of crypto-bigint), we'd have to be careful of that occurring. The static asserts included are a strong defense in the event of such a scenario     

> __< rucknium >__ I will ping jeffro256:monero.social  too     

> __< syntheticbird >__ I like their concerns but serialization would kill performance     

> __< DataHoarder >__ unsafe{ performance }     

> __< rucknium >__ So we need version pinning on the external library. I think you already do that anyway.     

> __< jpk68:matrix.org >__ It would be nice if the code could be vendored into a separate repo (not src/fcmp_pp/fcmp_pp_rust, I mean the dependencies)     

> __< DataHoarder[m] >__ jpk68:matrix.org: Given that even this recent PR had mismatching versions of several core packages, vendoring critical dependencies would be a plus     

> __< jberman >__ rucknium: Yes, we do pin versions. We'll probably need to update to a more recent version of the upstream lib at some point (I think we need to already), and so we'd want to double check it with that latest version we update to     

> __< DataHoarder[m] >__ Changes to these would be more obvious in reviews and allow dev copies in other platforms to not depend on crates.io or the specific git/forge they are stored, but have code local     

> __< rucknium >__ IIRC, tobtoht:monero.social  is keen on vendoring external libraries.     

> __< syntheticbird >__ rightfully     

> __< rucknium >__ More comments about the ToB audit?     

> __< jberman >__ Vendoring sounds fine to me. kayabanerve:matrix.org may have thoughts there too     

> __< rbrunner >__ So watching the original libs for importing changes to "vendor in" again is the lesser evil?     

> __< DataHoarder[m] >__ About the uninitialized receiver/output, that's a kind of scary find. I found similar issues on other languages/code while implementing parts of Monero (which caused some fun aftermath https://words.filippo.io/dependabot/ )      

> __< DataHoarder[m] >__ ToB recommends additional steps to prevent issues like this in the future/more static tooling. Would that sort of hardening be sought for?      

> __< jpk68:matrix.org >__ I would also like to bring up the impact of FCMP++ Rust code on binary sizes. I seem to remember tobtoht suggesting we remove the 'utility' binaries from release archives on the site to save space because of the increase.     

> __< DataHoarder[m] >__ Specially as a lot of the Monero crypto code, while sounds, comes from the legacy times where it was all uncommented single-letter variables, which took time to untangle (see biased hash / elligator 2 for the hash to point / key image)     

> __< jpk68:matrix.org >__ IMO, we should reconsider applying the strip option to the release profile, and maybe fat LTO     

> __< jberman >__ Imo more relevant than the ToB audit as it relates to FCMP++ audit work generally:     

> __< jberman >__ xmrack:monero.social identified a detectable double spend vuln in the consensus integration code, highlighted here: https://github.com/seraphis-migration/monero/pull/446     

> __< jberman >__ This (consensus integration) would have fallen under the scope of "Phase 3" in the integration audit plan     

> __< rucknium >__ If I may ask, did an LLM assist with finding ack-j:matrix.org 's bug?     

> __< DataHoarder[m] >__ 👍 > <jberman> xmrack:monero.social identified a detectable double spend vuln in the consensus integration code, highlighted here: https://github.com/seraphis-migration/monero/pull/446     

> __< rucknium >__ Trying to understand the role of LLMs in finding these types of bugs.     

> __< jeffro256 >__ Howdy, sorry I'm late      

> __< jberman >__ rucknium: Yes     

> __< syntheticbird >__ what LLM ?     

> __< jeffro256 >__ He mentioned using Opus on a different FCMP report      

> __< jeffro256 >__ So maybe Opus?     

> __< sech1 >__ It doesn't matter, all of the available top-tier LLMs should be used to check this code for vulnerabilities. And multiple times.     

> __< syntheticbird >__ alr     

> __< syntheticbird >__ sech1, i agree on that and i am not trying to frame one model to be better than another, it's just curiosity.     

> __< jberman >__ sech1: I'm in favor of this as well     

> __< syntheticbird >__ speaking of LLM audit I came across https://github.com/evilsocket/audit recently     

> __< syntheticbird >__ for those who have the tokens probably worth a try     

> __< DataHoarder >__ that looks neat for a more automated setup     

> __< rucknium >__ Just thinking out loud: If today's LLM catches critical bugs now, and tomorrow's LLM is even better, then what happens when tomorrow's LLM finds a critical bug after the hard fork occurs?     

> __< rucknium >__ I don't like this new reality :(     

> __< DataHoarder[m] >__ There should not be just LLM review, it's in addition to any other normal reviews     

> __< syntheticbird >__ Continuing on thinking loud: useless to recall how blueteam and other malicious actors caused a surge in critical vulnerability exploits on many DeFi projects when Opus started coming out     

> __< syntheticbird >__ blueteam = v12 = zellij     

> __< syntheticbird >__ zellic*     

> __< DataHoarder[m] >__ rucknium: This can be changed to "If today's cryptographers catches critical bugs now, and tomorrow's cryptographers learn new research then what happens when tomorrow's cryptographers finds a critical bug after the hard fork occurs?" and still has the same meaning, use all available way to audit and protect/cover.     

> __< gingeropolous >__ difference is, joe shmoe can run an llm ... but joe shmoe isn't a cryptographer     

> __< rucknium >__ Does Monero code need to do what aerospace code does and over-engineer all the code and code-writing processes in safety-critical areas?     

> __< DataHoarder[m] >__ ☝ > <rucknium> Does Monero code need to do what aerospace code does and over-engineer all the code and code-writing processes in safety-critical areas?     

> __< vtnerd >__ I would also expect diminishing returns on the llm advancement, but that's just a fut feeling      

> __< vtnerd >__ *gut     

> __< DataHoarder[m] >__ There's areas that can be upgraded/covered and others that cannot without consensus-breaking changes (or tightening that need to be hidden)     

> __< boog900 >__ You would be asking for like a full rewrite :)     

> __< jeffro256 >__ We could have said the same thing about cryptographic research by humans, albeit on a slower timeline. If cryptographic knowledge gets better and better, what hppens when people figure out ways to break current cryptography? The answer has to be vigilance and the constant cat-and-mouse game, like it always has been      

> __< syntheticbird >__ boog900: yeah this lmao     

> __< DataHoarder[m] >__ Specially if you cannot "hide" such changes in patches like done in the past (for example, the double-spend bug related to twisted outputs)     

> __< rbrunner >__ This boomer would advice, in addition to everything already said, to take each and every chance to avoid complexity     

> __< rucknium >__ We are at a specific inflection point in time. Like when old-style crypto was being broken.     

> __< selsta >__ not sure if this was linked yet but ack-j also has a fundraiser for fuzzing, including fcmp++ (though afaik this won't include LLMs, just regular fuzzing) https://donate.magicgrants.org/monero/projects/fuzzing-monero-2     

> __< syntheticbird >__ DataHoarder[m]: well there was an instance of hiding failure     

> __< syntheticbird >__ in the past     

> __< rucknium >__ I don't mean to throw a wrench in the gears, but there have been at least 3 privacy coin counterfeiting bugs revealed this year (Litecoin MWEB, Zcash Orchard, Beam).     

> __< DataHoarder[m] >__ And with today's automation flows you can even review binary changes and recover original flow/intent to do even tighter analysis/diffing across releases to catch not mentioned changelog items.     

> __< syntheticbird >__ rucknium:monero.social, I agree with you that crypto out of all other domains are the ones being hit the hardest on AI vulnerability findings because of the extreme investment to reward ratio. We can't just ignore it     

> __< DataHoarder[m] >__ rucknium: Then I'd repeat my above concern with the uninitialized output, which could have caused "fun" issues, and work on ways that such issues could have been captured early on     

> __< syntheticbird >__ i sounds like an AI bro and I hate it     

> __< DataHoarder[m] >__ Some process that can run concurrently, or within PRs as well in a lighter form, and generally review incoming areas or overall integration using classical methods or anything needed. Even pointing out general "Smell" should be a cause of concern if we are talking about safety-critical areas.     

> __< rucknium >__ Full disclosure: I sort of predicted this problem and my old mindset is coming back. I'm not a cryptographer nor a real programmer, so what do I know? :D     

> __< syntheticbird >__ DataHoarder[m]: generally my philosophy is that if safety is critical, your must increase formal verification coverage     

> __< jpk68:matrix.org >__ Sorry for bringing this up for the hundredth time, but as others have stated, it's extremely important to reduce unnecessary code complexity (which can shelter exploits). I think introducing Rust with FCMP++ is doing exactly the opposite of this; potentially investing in the code being rewritten to avoid such complexity would maybe be worthwhile.     

> __< boog900 >__ No that would take too long      

> __< jpk68:matrix.org >__ FCMP++ already brings a huge number of changes in critical pathways; the FFI stuff is not helping the matter     

> __< DataHoarder[m] >__ syntheticbird: then such formal verification should be in PR, I agree. And that should be included along     

> __< jpk68:matrix.org >__ boog900: Not before the hardfork per se, I just mean eventually     

> __< boog900 >__ eventually I agree     

> __< boog900 >__ I want multiple impls      

> __< jpk68:matrix.org >__ I would totally be against delaying the hardfork for that     

> __< syntheticbird >__ boog900: I want variable time for nodes     

> __< DataHoarder[m] >__ > <jpk68:matrix.org> Sorry for bringing this up for the hundredth time, but as others have stated, it's extremely important to reduce unnecessary code complexity (which can shelter exploits). I think introducing Rust with FCMP++ is doing exactly the opposite of this; potentially investing in the code being rewritten to avoid such complexity would maybe be worthwhile.     

> __< DataHoarder[m] >__ I generally agree that the Rust monero-oxide/Cuprate rewrite is vastly easier to read/follow than C++ specially when using undocumented load-bearing crypto operations from cryptonote era :)     

> __< jpk68:matrix.org >__ selsta: And fuzzing as well, of course ^     

> __< syntheticbird >__ its 44 shouldn't we move to another topic ?     

> __< syntheticbird >__ rucknium:monero.social:     

> __< boog900 >__ On the list of big C++ work that needs to be done I wouldn't put an FCMP rewrite high though      

> __< rucknium >__ IIRC, jeffro256:monero.social  wanted to get input on timeline for integration audit parts 2 and 3     

> __< rucknium >__ So we should get that input in this agenda item unless jeffro256:monero.social  does not want it at this meeting.     

> __< jeffro256 >__ Yes, I asked the question last MRL IIRC, whether the 6-month wait period should depend on the completition of audit parts 2 and 3. I don't think it should, but I think we should plan for audits 2 and 3 to completelt at least 3 months before the HF activation date, and plan for a period of follow-up development where we fix issues, if any, from those audits parts.     

> __< rucknium >__ And we were promised a Gantt chart :)     

> __< jeffro256 >__ ;)     

> __< jeffro256 >__ https://html-preview.github.io/?url=https://github.com/jeffro256/fcmp-carrot-plan/blob/master/fcmp%2B%2B-carrot.html     

> __< syntheticbird >__ lmao     

> __< jberman >__ jeffro256: I have the same view     

> __< jeffro256 >__ Some people wanted to see the first audit report findings before making the decision. I think that link has already been shared, correct?     

> __< syntheticbird >__ Yes > <rucknium> Agenda item 3 ^     

> __< syntheticbird >__ below i miss click     

> __< rucknium >__ jeffro256: Yes     

> __< jeffro256 >__ With that current Gannt chart I shared, according to discussions in NWLB yesterday, I have the 6-month wait period before HF activation depend on the first HF-enabled merge to master. I have a 1 month node/p2p/consensus code freeze dependent on that merge too. I have a 2 month code freeze on wallet features and any audit-related follow-up development before the HF activation      

> __< jeffro256 >__ Does all of that sound reasonable?     

> __< rucknium >__ jeffro256:monero.social: Thanks for the detailed chart     

> __< rucknium >__ jeffro256: Sounds ok to me     

> __< jeffro256 >__ That puts FCMP++ HF activation at the beginning of February if we stay on this schedule      

> __< rucknium >__ Anyone else want to comment on jeffro256:monero.social 's proposed plan?     

> __< jeffro256 >__ Which means locking in for a lot of code merging for the next month      

> __< rucknium >__ And if not, anything else to discuss during this agenda item?     

> __< rucknium >__ 4. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< rucknium >__ tevador     

> __< tevador >__ I posted updates on github. I don't want to delay the meeting, so the only thing I'd like to discuss is this proposal: https://github.com/monero-project/research-lab/issues/161#issuecomment-5100079175     

> __< rucknium >__ I have a question about tx distinguishability with the payment channel relative locks. Do the payment channel lock txs have to set the FCMP tree anchor when they are created, or can they be updated with pre-signing?     

> __< rucknium >__ Maybe my question isn't very clear, but I hope I conveyed what I was getting at.     

> __< tevador >__ No, the FCMP tree anchor is always selected just prior to tx submission.     

> __< rucknium >__ Thanks.     

> __< tevador >__ The FCMP "reference_block" field is not signed with the spend authorization proof.     

> __< rbrunner >__ Would a soft-introduction of such locks mean that we would have a mixed network, some nodes would honor the locks, some not? And if yes, would that fly?     

> __< rbrunner >__ *soft-fork-introduction     

> __< tevador >__ That's not how soft forks work. Soft fork activates when >50% of miners start following the rule. Everyone else then follows the longest chain.     

> __< jeffro256 >__ > <tevador> I posted updates on github. I don't want to delay the meeting, so the only thing I'd like to discuss is this proposal: https://github.com/monero-project/research-lab/issues/161#issuecomment-5100079175     

> __< jeffro256 >__ I think that the idea in this PR https://github.com/seraphis-migration/monero/pull/445 is fine. Since, the non-standard behavior happens when unlock_time=1, restricting the unlock_time to equal 0 is a soft-fork back to standard behavior.      

> __< rucknium >__ By the way, we know roughly what percentage of spent outputs are more than 24 hours old, thanks to the OSPEAD estimates. It is 1/3rd.     

> __< rucknium >__ Check the bottom part of the plot here: https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/performance-evaluation.html#fig-decoy-distributions-top-1-3-not-log     

> __< rbrunner >__ Ah I see,  that's a difference to normal functionality introduced in updates.     

> __< tevador >__ For Bitcoin, ~20% of spends are >24 hours     

> __< boog900 >__ IMO I don't think we really need or should have decoys which say they were locked when they were not.      

> __< jeffro256 >__ Makes sense. Higher volume coin, which has more exchanges per user, has lower median spend time      

> __< tevador >__ I think we don't need to discuss the details of time-locks now, only if it's worth reserving unlock_time = 1 for it.     

> __< boog900 >__ I am ok with reserving unlock_time = 1      

> __< rucknium >__ boog900:monero.social: I am leaning toward your position on that. You are kind of forcing some users to disclose to their tx recipients that their outputs are more than 24 hours old. That's a small privacy leak, but it's a little unfair because it's for the benefit of the payment channel users.     

> __< jeffro256 >__ I am also okay with it as long as no reference wallet software uses it      

> __< rbrunner >__ Uses it? How could that happen?     

> __< rucknium >__ jeffro256:monero.social: Also Monero has its 10-block lock and you cannot spend txs in the same block. IIRC, about 8% of BTC outputs are spent in the same block they are created in.     

> __< boog900 >__ rucknium: Exactly, especially as, from what I read in the proposal, locked txs are only published in the case where there is misbehaviour       

> __< tevador >__ Btw, only payment channel force closes reveal use unlock_time = 1, which would presumably be a tiny percentage of all payment channel closes.     

> __< jberman >__ A risk with the proposed upgrade plan IIUC: if a minority of nodes update, then start seeing txs with unlock_time=1 and reference_block<720, then those nodes would be split from the network     

> __< jeffro256 >__ Also, ostensibly , in a payment channel close, the tx output recipients would be yourself, so you're not leaking that info to a counterparty      

> __< rucknium >__ IMHO, tx heterogeneity matters most when it's a consistent pattern for every tx created by a user's wallet. If a user creates an unusual tx once, but not before or afterward, then you don't have the tx linking issue.     

> __< tevador >__ jberman: that's a general soft fork issue, not really related to the proposal. Generally, soft forks activate based on >>50% miners signaling support.     

> __< tevador >__ To clarify: if >50% of miners support the soft fork, non-updated nodes follow the rule because the longest chain follows the rule.     

> __< jberman >__ Fair     

> __< rucknium >__ Is it intended to change the name of the unlock time variable in the code to reduce confusion?     

> __< jberman >__ I'm OK with reserving unlock_time = 1 also     

> __< rucknium >__ I am ok with tevador 's proposal https://github.com/monero-project/research-lab/issues/161#issuecomment-5100079175     

> __< tevador >__ I think it's OK to keep the name "unlock_time".     

> __< earthman:unredacted.org >__ sech1: Take a look at your donos. Stay silent about the amount please     

> __< earthman:unredacted.org >__ earthman:unredacted.org: It is for monero audits, P2Pool and a part for yourself     

> __< earthman:unredacted.org >__ You can share with DataHoarder[m]  if you want     

> __< rucknium >__ More discussion of this item?     

> __< DataHoarder[m] >__ 🙇 > <earthman:unredacted.org> You can share with DataHoarder[m]  if you want     

> __< rucknium >__ 5. Shi, Zhang, Ge, Lan, Zhang, & Wang (2026) "Deanonymizing Monero Transactions in Tor Network." (https://arxiv.org/abs/2607.07062)     

> __< rucknium >__ jpk68:matrix.org and syntheticbird:monero.social     

> __< syntheticbird >__ I've read the paper and I have a piece to say     

> __< jpk68:matrix.org >__ I did end up looking through the paper, and from what I can tell, the heuristics outlined are mostly legit. It's basically a three-part pipeline that attempts to correlate outgoing transactions to Tor identifiers, and then those identifiers to IP addresses.     

> __< jpk68:matrix.org >__ The first out of three was indeed patched well over a year ago (by vtnerd in #9632), which seems to fix the issue of hidden-service nodes leaking their own onion addresses     

> __< rucknium >__ I read this paper. I want to give others the opportunity first to comment     

> __< syntheticbird >__ jpk68:matrix.org: I disagree     

> __< jpk68:matrix.org >__ However, the other two appear to be unpatched to this day. The remaining heuristics include the fact that proxies are not chosen uniformly from "neighbour" peers (instead, based off of a self-reported and unverified block height parameter), and there is also no rate limit sync/ping messages, which lets Tor relays see a timing  [... too long, see https://mrelay.p2pool.observer/e/wOPvxJsLdFB2WDFr ]     

> __< jpk68:matrix.org >__ So, if I understand correctly, we should immediately try to patch the proxy selection bias (and also add more checks for false self-reported block heights), plus add rate limits for random timed sync request flags per connection     

> __< tevador >__ The fake-height bias is quite puzzling to me, I couldn't find it in the code.     

> __< rucknium >__ I don't know how to fix the fake-height bias except to ask the Tor peer to send all the "new" blocks over Tor, which would take a while. And it's only an attack-augmenting technique. Just reduces the number of machines you need to execute the attack.     

> __< syntheticbird >__ From my understand the fix from vtnerd was to shuffle the onion address place in the local peerlist being sent at TSR. But unless my understand is incorrect, this do not remove the fact that the onion address is being sent at every TSR. Which makes it longer to correlate but still doable.     

> __< jpk68:matrix.org >__ tevador: The code I looked at for this was in cryptonote_protocol_handler.inl, lines 456 to 494     

> __< jpk68:matrix.org >__ There appears to be no upper bounds check in process_payload_sync_data()     

> __< rucknium >__ syntheticbird:monero.social: You mean you could keep requesting peer lists and see which peer address always appears in every response?     

> __< syntheticbird >__ rucknium: Exactly.     

> __< syntheticbird >__ I think the paper is elegant and exploit weaknesses effectively. I will not able to convince people here that will consider this as a nothing burger because you need to workout with adversarial Tor guards.     

> __< jpk68:matrix.org >__ syntheticbird: IIUC, this still mostly fixes the first step out of three, yes?     

> __< syntheticbird >__ I think the Tor Project is compromised and this paper actually shows an attack that while not scaling to the entire network can be added to the arsenal of Chainanalysis and Co     

> __< tevador >__ jpk68: I read that and I don't think that's it.     

> __< syntheticbird >__ jpk68:matrix.org: This only make the correlation takes longer, it do not erase it     

> __< rucknium >__ IMHO, compromising the Monero node's Tor guard node is the least plausible part of the attack. Not feasible without a lot of machines. Tor specifically tries to defend against that.     

> __< syntheticbird >__ identity_role stage     

> __< jpk68:matrix.org >__ Yeah, but it eliminates the ability for it to be done passively     

> __< tevador >__ The correct fix for the onion address leak would be to insert own address before truncating the list to 250 peers.     

> __< syntheticbird >__ rucknium: That is if you believe Tor project to be genuine but that is another topic entirely. There multiple points i would like to address     

> __< tevador >__ With randomized insertion*     

> __< rucknium >__ But IMHO, even if you don't get the true IP address of the node, you could probably still link a user's txs together if they come from the same node. So there are still issues to be addressed.     

> __< boog900 >__ this https://github.com/monero-project/monero/blob/cca58174877f7facad0c4f36807b82e76a53f3ec/src/cryptonote_protocol/levin_notify.cpp#L151? > <tevador> The fake-height bias is quite puzzling to me, I couldn't find it in the code.     

> __< monerobull:matrix.org >__ What would you guys recommend if the goal is to hide transaction origins and you don't care about the ISP knowing you run a node? --proxy, --tx-proxy (even though there is this attack, or maybe even both?      

> __< rucknium >__ I liked that they "defeated" the noise protocol by actively sending timed messages. But the noise protocol wasn't intended to defeat an active adversary. It was designed to hide info from a passive ISP_level observer AFAIK.     

> __< vtnerd >__ the biggest issue with linking tx to identity is that you can effectively “break” the ring. this closes with fcmp++     

> __< syntheticbird >__ I join you rucknium:monero.social, The bias selection is the most serious issue in my opinion and I would go as far as saying this bother me that they can so easily distribute 5000 new onion addresses to a node and it not asking any questions.     

> __< boog900 >__ boog900: maybe should add a few blocks of allowance      

> __< syntheticbird >__ Understand by that that I think the node should do some basic sanity check and reject a peerlist if its entirely composed of onion addresses it never heard of (at least when its own peerlist is full)     

> __< rucknium >__ syntheticbird:monero.social: I also liked that the paper gave a specific hardware requirements list to Sybil attack Monero onion hidden services. That's a point that boog900:monero.social  and I made in our MoneroKon presentation last year, but we didn't have the numbers.     

> __< DataHoarder[m] >__ syntheticbird: in P2Pool we only add onion addresses when they get included in a share (which has certain POW) and these timeout after a while when they leave certain window     

> __< DataHoarder[m] >__ not doable here, ofc, as otherwise spamming onions is free     

> __< rucknium >__ That presentation is "Defeating Spy Nodes on the Monero Network" https://github.com/Rucknium/presentations/blob/main/Rucknium-Boog900-MoneroKon-2025-Spy-Nodes.pdf https://vimeo.com/1095371245     

> __< syntheticbird >__ rucknium: where ?     

> __< tevador >__ boog900: Thanks, that looks like it.     

> __< rucknium >__ The hardware requirements are on page 9     

> __< syntheticbird >__ Or right thanks I skipped that part     

> __< syntheticbird >__ the hardware part     

> __< syntheticbird >__ and forgot about it     

> __< syntheticbird >__ DataHoarder[m]: why wouldn't it be doable ?     

> __< boog900 >__ We could not share onion addresses with connections we intend to send txs to at all and close the connection after 1 tx     

> __< DataHoarder >__ you'd need to attach these onions to some sort of timed pow that adjust based on a rate, so... monero blocks :)     

> __< jpk68:matrix.org >__ The paper also mentioned some mitigations (which are beyond my understanding) related to extending the Dandelion++ stem phase ambiguity     

> __< boog900 >__ boog900: litterally just send the tx     

> __< DataHoarder >__ mining a monero block to get included is quite expensive     

> __< vtnerd >__ > <rucknium> I liked that they "defeated" the noise protocol by actively sending timed messages. But the noise protocol wasn't intended to defeat an active adversary. It was designed to hide info from a passive ISP_level observer AFAIK.     

> __< vtnerd >__ they do this to get the last peer (which has been patched), how is this still effective? you’d need a passive+active adversary to use timed sync messages … ?     

> __< syntheticbird >__ DataHoarder i get it thx      

> __< rucknium >__ The paper says to 1) Eliminate the own-address identification (at least partially addressed already) 2) Extend the Dandelion++ protocol to the Tor tx-relay side (would slow down tx propagation and be complicated to implement), and     

> __< rucknium >__ 3. Limit the timed sync requests in the Noise protocol to prevent the active watermarking of tor connections.     

> __< syntheticbird >__ Yeah I am impressed by the watermarking part     

> __< rucknium >__ boog900: boog900:monero.social: How persistent are Monero peer IDs on the Tor side?     

> __< syntheticbird >__ This is the type of attack you would never thinkg about because of how cumbersome it sounds yet it works     

> __< boog900 >__ everyone sets a PeerID of 1     

> __< tevador >__ on tor, peer id = 0, no?     

> __< tevador >__ 1*     

> __< syntheticbird >__ syntheticbird: All peer id are 1     

> __< syntheticbird >__ wrong answer + lag     

> __< boog900 >__ how does bitcoin protect itself?     

> __< boog900 >__ or does it not? It allows everything over Tor too     

> __< syntheticbird >__ I don't think it does     

> __< boog900 >__ blocks etc     

> __< syntheticbird >__ May I propose a radical solution to resolve 2 and 3     

> __< vtnerd >__ I thought of this, thus the attempt to do white noise, but its certainly difficult to patch ontop of an existing p2p thing > <syntheticbird> This is the type of attack you would never thinkg about because of how cumbersome it sounds yet it works     

> __< vtnerd >__ its impressive they indeed were able to do watermarking, as I just looked at wireshark and determined it was plausible     

> __< vtnerd >__ it may be impossible to stop, because the remote side can always send data     

> __< earthman:unredacted.org >__ Do we track onion nodes? > <syntheticbird> I join you rucknium:monero.social, The bias selection is the most serious issue in my opinion and I would go as far as saying this bother me that they can so easily distribute 5000 new onion addresses to a node and it not asking any questions.     

> __< rucknium >__ vtnerd:monero.social: I think I agree with you that the watermarking would only be useful combined with Tor guard node compromise and discovering the onion address of the target node. > <vtnerd> they do this to get the last peer (which has been patched), how is this still effective? you’d need a passive+active adversary to use timed sync messages … ?     

> __< earthman:unredacted.org >__ Is there a list of all onion nodes?     

> __< rucknium >__ earthman:unredacted.org: I don't know of anyone actively probing the number of onion nodes. I mean, anyone on the MRL-friendly side of things.     

> __< syntheticbird >__ syntheticbird: I think that over Tor white noise needs to be extended to every message and enforce penalty on not respecting a give frequency.     

> __< DataHoarder >__ https://monero.fail/ lists some onion ones     

> __< earthman:unredacted.org >__ Aren't there already 5000 malicious ones? Who is tracking > <syntheticbird> I join you rucknium:monero.social, The bias selection is the most serious issue in my opinion and I would go as far as saying this bother me that they can so easily distribute 5000 new onion addresses to a node and it not asking any questions.     

> __< syntheticbird >__ It make no sense that you can send a TSR every 20 sec     

> __< rucknium >__ monero.fail and similar services have lists of the RPC onion addresses of Monero nodes, but that is different from the tx-relay addresses     

> __< boog900 >__ syntheticbird: please no 😭     

> __< DataHoarder >__ specially ones with RPC     

> __< vtnerd >__ syntheticbird: yes, likely this, otherwise we should just give up and try nym or something     

> __< rucknium >__ AFAIK     

> __< syntheticbird >__ boog900: "if someone's oppose to this wedding now is time to speak"     

> __< tevador >__ I don't think we should focus on attacks that require a compromised guard.     

> __< boog900 >__ I just don't want to add that logic to Cuprate and would question if it would even work with how dynamic our message sizes are     

> __< syntheticbird >__ If we send periodicly fixed size messages at a given frequency even tho we don't send any message at all we break watermarking and don't need dandelion because no one will be able to do a timing correlation attack. It does however expose monero usage pattern to any relay observer     

> __< syntheticbird >__ tevador, 2 years ago Tor project reported that 30% of its nodes were own by a single entity.     

> __< syntheticbird >__ We need to accept the reality that Tor is not the holy grail     

> __< DataHoarder[m] >__ syntheticbird: what is this frequency? if it's a local clock started when node started, this can be used as a fingerprint source     

> __< monerobull:matrix.org >__ monerobull:matrix.org: Any ideas?     

> __< tevador >__ I'm not saying it's not a problem.     

> __< syntheticbird >__ DataHoarder[m]: that would be random and negotiated at handshake     

> __< jpk68:matrix.org >__ monerobull:matrix.org: I mean, you could also try and use I2P     

> __< DataHoarder[m] >__ syntheticbird: an active prober with ISP viewpoint would be able to abuse this, specially if random     

> __< DataHoarder[m] >__ it'd be able to randomize to an interval that is unique, and change it every once in a while     

> __< syntheticbird >__ DataHoarder[m]: true, well my idea is shit     

> __< DataHoarder[m] >__ jpk68:matrix.org: I had to disable I2P (C one) due to active RCE... maybe time to try the (ugh) java one     

> __< jpk68:matrix.org >__ Yes, the C++ implementation's security is... not ideal     

> __< syntheticbird >__ I still think we should instantiate penalty on TSR being sent with a delta time from average that is too high     

> __< syntheticbird >__ * the peerlist sanity check i mentioned before     

> __< syntheticbird >__ if your peerlist is full there is no reason someone is just giving you 250 new nodes you never heard of     

> __< rucknium >__ Would the peerlist sanity check be very effective? An adversary could just fill your peer list slowly instead of quickly.     

> __< vtnerd >__ it makes watermarking harder has they get one shot per connection. and it makes filling up the table take longer (but not prevent)     

> __< vtnerd >__ or I guess they could still watermark if they are more patient     

> __< syntheticbird >__ Yes they can adapt without a doubt. I just think this makes the time cost considerably larger and feels like common sense enough that this mitigate trivial adversarial     

> __< DataHoarder[m] >__ longer is not long enough unless it's effectively untractable      

> __< DataHoarder[m] >__ specially for daemons/servers with 24/7 uptime     

> __< boog900 >__ syntheticbird: I have suggested this too for clear net      

> __< boog900 >__ I think it's what bitcoin does      

> __< vtnerd >__ one thing that no one mentioned is that not setting up inbound connections likely provides better privacy     

> __< boog900 >__ it makes you slightly more vulnerable when starting up but more secure to attacks after that      

> __< syntheticbird >__ nice i didn't know that     

> __< rucknium >__ Nym has ports 18080, 18081, and 18089 open for Monero nodes: https://forum.nym.com/t/nip-3-nym-exit-policy-update/1462     

> __< syntheticbird >__ The issue with Nym is that the target you connect to is not anonymous     

> __< syntheticbird >__ only outgoing connections are protected     

> __< rucknium >__ We can continue to think about this one. I'll keep it on the agenda for next meeting.     

> __< rucknium >__ 6. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ jberman:monero.social and I think we have the bug fixed where wallets forget that they spent an output and try to spend it again, causing a double-spend error on the Node side.     

> __< rucknium >__ Over 1.2 million txs from 48 separate wallets were sent to nodes with the patches and the problem did not occur in any of them.     

> __< jberman >__ Shooting for v2.1 by next week's meeting, with above issue (finally) solved     

> __< DataHoarder[m] >__ haven't seen any major altchains over past few weeks     

> __< rucknium >__ DataHoarder[m]: Fewer miners, probably, Not strong evidence that alt chains are rarer.     

> __< rucknium >__ jberman:monero.social: What are the goals for stressnet beyond v2.1?     

> __< DataHoarder[m] >__ I agree. There is some new miners or ones with low hashrate now listed on https://stressnet.p2pool.observer/pools     

> __< rucknium >__ Do we have a specific block size goal?     

> __< rucknium >__ I am moving things around so I can broadcast even more txs, but it will be tedious. And I'll occupy most of the MRC resources if we go a lot higher.     

> __< jberman >__ I didn't have a specific block size goal in mind. Stability under consistent stress (which the stressnet has experienced) was the target I was shooting for. And this set of issues seemed like the most significant lingering. Obviously we can continue with fixing the most blatant issues (e.g. slow perf when the pool is huge), bu [... too long, see https://mrelay.p2pool.observer/e/noaGxpsLd0NDZ3ln ]     

> __< DataHoarder[m] >__ Syncing a wallet via monero-cli has had some abysmal performance when I tried a few days ago, even after some patches ofrnxmr:monero.social provided. It surely does more work than just what I am doing myself, but for the explorer I am currently syncing up 130 different wallets at once on stressnet, without much CPU usage on my block explorer (With a lookahead depth of +5000 accounts)     

> __< DataHoarder[m] >__ Besides the high RAM usage of cli wallet, most of the debugging pauses I did landed on hashmap growth/insert code.     

> __< rucknium >__ DataHoarder[m]: You feel my pain :D     

> __< DataHoarder[m] >__ the good performance allowed to scan one OUTPUT per two seconds     

> __< DataHoarder[m] >__ before it was one output every few minutes...     

> __< DataHoarder[m] >__ That might be a limiting factor if rucknium:monero.social tries to grow the spamming further :)     

> __< rucknium >__ It shouldn't be that bad     

> __< ofrnxmr >__ every few mins is related to changing the lookahead     

> __< rucknium >__ That is outputs that the wallet owns or does not own?     

> __< DataHoarder[m] >__ outputs they own, it skips successuly not owned ones     

> __< boog900 >__ monerod scales awfully with more wallets      

> __< DataHoarder[m] >__ for ones it owns it uses just one core, 100% of it, doing hashmap work :)     

> __< DataHoarder[m] >__ not monerod mind you, wallet-cli     

> __< jberman >__ Def does sound like a bug with subasdress expansion there. And plausibly other wallet sync perf stuff affecting fiatdemise in the stressnet channel can take a look at     

> __< jberman >__ Subaddress*     

> __< DataHoarder[m] >__ that lookahead growth shouldn't add +1 whenever an output is received, we should be growing 1.5x or something to not trigger this growth so often     

> __< ofrnxmr >__ jberman:monero.social the patch i gave him is yours     

> __< rucknium >__ ofrnxmr: ofrnxmr:monero.social: Do you know if I am affected if I reduce the lookahead compared to the default lookahead?     

> __< ofrnxmr >__ If you change the lookahead at all, it causes issues     

> __< DataHoarder[m] >__ I increased account lookahead to try to sync one of rucknium:monero.social's spam wallets :)     

> __< rucknium >__ And I thought I was being more efficient     

> __< DataHoarder[m] >__ as with defaults it didn't reach enough to start catching all outputs     

> __< ofrnxmr >__ ofrnxmr: (i think)     

> __< ofrnxmr >__ Been a while since i tested     

> __< DataHoarder[m] >__ either way can discuss more about that lookahead behavior/perf in stressnet channel     

> __< jberman >__ I remember that one. That was an upstream issue ya? Potentially new wallet side changes still playing a role > <ofrnxmr> jberman:monero.social the patch i gave him is yours     

> __< DataHoarder[m] >__ just raising it as an issue for maxing out block sizes/spam     

> __< ofrnxmr >__ Yeah     

> __< ofrnxmr >__ A regression from the set subaddress-lookahead pr     

> __< rucknium >__ Maybe I'm not affected because once I get spamming going, I don't produce more subaddresses.     

> __< DataHoarder[m] >__ rucknium: tbh the efficient way (for your wallet) to spam would be to send everything to main address+just a few subaddress, then specifically spend outputs, not accounts. Ofc, what you are doing is now also stressing the wallet, so hey, it did accomplish that :)     

> __< DataHoarder[m] >__ rucknium: Due to the way the spammer does it it doesn't change the lookahead directly as it generates the indices directly, but creating it anew without the spammer driving it requires increasing it. still shouldn't cause this abysmal degradation     

> __< kayabanerve:matrix.org >__ Vendoring Rust crates sounds fine to me, in a repository or under Monero. There's support for that in cargo and I've done it before. I think aggressively pruning unused libs with patch files may really drop the LoC to just the libs we actually use. For example, we have 150k lines of Rust's bindings to libc, and I don't believe [... too long, see https://mrelay.p2pool.observer/e/hZ6pxpsLNGZQRGc5 ]     

> __< kayabanerve:matrix.org >__ This is an interruption, sorry. I got a ping like, an hour ago, and just wanted to leave the comment.     

> __< ofrnxmr >__ simply running mnew address 1000 after changing the lookahead will show you the regression     

> __< rucknium >__ So my own wallets aren't really affected, but I affect you who are trying to follow my wallets. If I understand right.     

> __< DataHoarder[m] >__ rucknium: via wallet cli, correct, as it exists in fcmp++ beta branches/releases. Using other means (like my code that also includes subaddress growth) is efficient or doesn't show the same perf hit     

> __< DataHoarder[m] >__ and for context, it's a view-only wallet what I am restoring/tracking     

> __< rucknium >__ My spamming wallets use monero-wallet-rpc, not monero-wallet-cli by the way.     

> __< rucknium >__ I don't know if that matters at all for this issue     

> __< rucknium >__ Anything more on this agenda item for now?     

> __< jberman >__ Datahoarder can you create an issue for this one plz so we can keep track of it there     

> __< DataHoarder[m] >__ in seraphis fork?     

> __< jberman >__ Yes please     

> __< DataHoarder[m] >__ 👍 > <jberman> Yes please     

> __< jberman >__ Ty     

> __< jberman >__ Nothing more from me     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     




# Action History
- Created by: Rucknium | 2026-07-27T17:13:23+00:00
