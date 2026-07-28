---
title: Monero Research Lab Meeting - Wed 22 July 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1426
author: Rucknium
assignees: []
labels: []
created_at: '2026-07-16T22:20:20+00:00'
updated_at: '2026-07-27T17:08:57+00:00'
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

3. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).

4. [Relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

5. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). [Jamtis](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol). 

6. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1421 

# Discussion History
## Rucknium | 2026-07-27T17:08:57+00:00
Logs

> __< jberman >__ Unfortunately won't be 100% available for today's meeting, my update: continuing upstream FCMP++ integration PR's (the next PR was approved today) and squashing the rare stressnet wallet double spend errors (with rucknium's help, who's running the latest set of fixes for the error / observed issues while debugging)     

> __< jberman >__ On FCMP++ research tasks: we're looking to solicit quotes on a secondary audit of the circuit and gadget impl in the Rust FCMP++ lib and possibly more code as well, next step is drafting a proposal and reaching out to firms     

> __< jberman >__ No additional material change to report from last week on other FCMP++ items from my end beyond above     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1426     

> __< rucknium >__ 1. Greetings     

> __< tevador >__ Hi     

> __< vtnerd >__ Hi     

> __< rbrunner >__ Hello     

> __< articmine >__ Hi     

> __< gingeropolous >__ hi     

> __< ravfx:xmr.mx >__ Hi     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Keeping stressnet stressed. Investigating bugs on stressnet.     

> __< jeffro256 >__ me: upstreaming / reviewing FCMP++/Carrot PRs, working on upstreaming bug fixes, implementing performance enhancements      

> __< tevador >__ me: time-locks / payment channels research     

> __< gingeropolous >__ me: continuing to plug away on monerosim.     

> __< vtnerd >__ Me: updated ssl stressnet pr, working on separate changes for ssl, and working on testing the p2p slowdown fix     

> __< rucknium >__ 3. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).     

> __< rucknium >__ jberman:monero.social gave an update right before the meeting:     

> __< UkoeHB >__ Hi     

> __< rucknium >__ > Unfortunately won't be 100% available for today's meeting, my update: continuing upstream FCMP++ integration PR's (the next PR was approved today) and squashing the rare stressnet wallet double spend errors (with rucknium's help, who's running the latest set of fixes for the error / observed issues while debugging)     

> __< rucknium >__ > On FCMP++ research tasks: we're looking to solicit quotes on a secondary audit of the circuit and gadget impl in the Rust FCMP++ lib and possibly more code as well, next step is drafting a proposal and reaching out to firms     

> __< UkoeHB >__ me: payment channel security thoughts, making progress on multisig PR bugfixing     

> __< jeffro256 >__ So ToB is done with auditing phase 1. I don't know if j-berman has release the report publicly yet, I think that he wanted to do a pass on it before releasing it. Justin and I want to propose something to move the timeline up: remove phase 2 and 3 audits as a dependency for HF activation and binary release      

> __< UkoeHB >__ Is hw wallet support mandatory for hf? Cause those are going to take a while.     

> __< jeffro256 >__ This doesn't mean that phase 2 and phase 3 audits wouldn't happen, but they would happen during the 6-month conventional/mandatory waiting period instead.     

> __< jeffro256 >__ No, at least not in the core repo. That's my opinion      

> __< UkoeHB >__ Ok seems reasonable     

> __< rucknium >__ Are there big technical challenges for HW wallet support, e.g. need to fit big objects on limited wallet RAM?     

> __< jeffro256 >__ The interfaces for HW devices on the non-HW side are done. Ledger is interested in making a CCS proposal to fund R&D on their side.      

> __< jeffro256 >__ rucknium: I've talked to Kayaba a bit about this a while ago, and IIRC most parts of the SA/L signing can be "streamed" like they are now with CLSAGs. But it does complicate the signing as compared to simply having all the needed parts in-memory      

> __< rucknium >__ "remove phase 2 and 3 audits as a dependency for HF activation" has confusing wording, IMHO.     

> __< rucknium >__ "HF activation" means the date that the HF occurs, to me.     

> __< jeffro256 >__ By "HF activation", I meant "HF activation code merge", sorry      

> __< rbrunner >__ What happens if after that a critical problem surfaces that is not correctable within time, as a worst case scenario?     

> __< rbrunner >__ Or, can we "take back" the HF?     

> __< rucknium >__ Here's a 2020 paper on HW wallets for Monero https://moneroresearch.info/119 Klinec, D., & Matyas, V. 2020, "Privacy-Friendly Monero Transaction Signing on a Hardware Wallet." Paper presented at ICT Systems Security and Privacy Protection.       

> __< rbrunner >__ (As a result of the on-going audits and reviews)     

> __< jeffro256 >__ rbrunner: Then the date gets pushed back 6 - N months, and people have to re-download binaries, where N is the "remaining time" between problem finding and  previous HF activation date      

> __< rucknium >__ Last HF, the announced date was moved at least once. I don't think any HF binaries were released and then withdrawn.     

> __< jeffro256 >__ rbrunner: We can "take back" the HF before it happens if users/companies stay up-to-date on releases      

> __< rucknium >__ Anyone who downloads the binaries and neglects to update will be stuck on a bad fork.     

> __< rbrunner >__ Yes, as the possibly worst outcome, however unlikely     

> __< jeffro256 >__ Note that this is something that can happen anyways without audits, with such  large update, and we should prepare for it regardless of auditing  > <rbrunner> What happens if after that a critical problem surfaces that is not correctable within time, as a worst case scenario?     

> __< rucknium >__ That's a similar outcome for people who just never update and a HF happens.     

> __< rbrunner >__ Right.     

> __< rbrunner >__ Seems to me the community of Monero users must be pretty "forking aware" now     

> __< jeffro256 >__ Phase 1 has gone well so far, and j-berman and I are somewhat confident that further finding by future audits would likely be mitigatable without causing a HF relative to the current state of the codebase, but it's absolutely possible.      

> __< rucknium >__ If only we could get Linux package managers to also be forking aware     

> __< rucknium >__ Could you describe phases 2 and 3 for us, jeffro256:monero.social  ?     

> __< jeffro256 >__ I'm extremely confident that phase 2 and phase 3 could complete within the 6-month convential waiting period. With these assumptions in mind, if we were to take a cautious optimism approach, we could merge the HF activation code before phase 2 and 3 audits complete, and shave months off the timline.      

> __< jeffro256 >__ Then we have a contingency plan in case the audit feedback requires a HF relevant to previous release      

> __< rucknium >__ You say "the 6-month conventional waiting period" as if a 6-month waiting period has ever happened before :D     

> __< jeffro256 >__ Phases 2 and 3 are defined in this document: https://github.com/seraphis-migration/monero/issues/294     

> __< tevador >__ There should generally be at least a 2-3 month code freeze before the HF, if possible.     

> __< articmine >__ rucknium: Sometimes I prefer they are not. I have had issues with Bitcoin and Linux package managers     

> __< articmine >__ Never with Monero      

> __< jeffro256 >__ tevador before HF activation, correct?     

> __< tevador >__ Yes, before the fork activation date.     

> __< jeffro256 >__ I think that that is certainly possible with the planned scopes of phase 2 and phase 3      

> __< jeffro256 >__ I'm working on a Gannt chart today because the timing and dependencies is getting hard to describe in words      

> __< jeffro256 >__ But I wanted to toss the idea of not blocking the first HF-activated release with phase 2 and phase 3 and get feedback on that      

> __< rbrunner >__ maybe "HF enabled release" or "HF ready release" ...     

> __< slstmd >__ What was the exact definition of code freeze again?     

> __< vtnerd >__ presumably there would be a branch at the very least     

> __< rucknium >__ I went back and looked. The previous HF binary was released less than a month before the HF activation date: https://github.com/monero-project/monero/releases/tag/v0.18.0.0     

> __< rucknium >__ I don't mean to say that it's a good precedent to follow. But "conventional" 6-month period is probably not the right word.     

> __< jeffro256 >__ lol fair      

> __< rbrunner >__ I think that was always "the idea" :)     

> __< jeffro256 >__ I was under the assumption that that was the target for previous HFs     

> __< rbrunner >__ That collided sooner or later with harsh cold reality     

> __< vtnerd >__ we should’ve created the branch earlier than the 1 mo, and “froze” changes, but I don’t recall now     

> __< tevador >__ Code freeze means only bug fixes can be merged... but this rule has not always been followed.     

> __< rbrunner >__ I think it's still a good idea, and maybe *this* time, swapping almost the whole technology stack, we should pull that through     

> __< rucknium >__ The 2022 HF delay was about multisig IIRC     

> __< rbrunner >__ And also with coin exploits popping up left and right ...     

> __< rucknium >__ Do we need more time to discuss this, in this meeting? We can give people time to think. I hope the Trail of Bits piece can be published by next meeting, to provide more info.     

> __< rucknium >__ Will there be a bounty on exploits against the the frozen code before the HF is activated?     

> __< rbrunner >__ Something that goes beyond the usually offered bounties would be a first, as far as I know     

> __< tevador >__ The Monero VRP states that "code in all branches; including the master branch and any release branch" are in scope     

> __< rucknium >__ The VRP scope is wide. Maybe something special isn't necessary:     

> __< rucknium >__ > This Vulnerability Response Process and subsequent bounty reward apply to the following:     

> __< rucknium >__ > Code implementation as seen in the Monero Project GitHub repositories     

> __< rucknium >__ > This includes code in all branches; including the master branch and any release branch     

> __< rucknium >__ > Written research from the Monero Research Lab which dictates said code implementation     

> __< rucknium >__ https://github.com/monero-project/meta/blob/master/VULNERABILITY_RESPONSE_PROCESS.md     

> __< rucknium >__ But the potential reward isn't defined well.     

> __< jeffro256 >__ tevador: Maybe we should reduce the scope to *current release branches...     

> __< jeffro256 >__ I don't care if there's a vuln in v0.12.0.0 that got fixed 5 years ago      

> __< tevador >__ Yes, that scope seems overly broad     

> __< rucknium >__ More on this agenda item?     

> __< articmine >__ jeffro256: Does this include anything that is pre release, or in testing for release etc.     

> __< jeffro256 >__ Does anyone currently object to not blocking the first release with phase 2 and phase 3 audits ?     

> __< articmine >__ I understand the case of clearly obsolete code     

> __< selsta >__ fwiw it has never been an issue that someone argued about old release branches, but yes the wording should be updated     

> __< jeffro256 >__ If it's still in a PR, I think it shouldn't be in-scope for payouts. If it's pre-release, it will probably be in master. If it's a planned release, it will show up in a current release branch      

> __< rbrunner >__ Right now looks like a calculated risk worth taking to me.     

> __< articmine >__ Fair enough, I just feel we should be careful and precise with the language.     

> __< rucknium >__ jeffro256: jeffro256:monero.social: I would prefer to have the Trail of Bits piece published before making a call on that, but I won't "object" to it.     

> __< jeffro256 >__ That's fair, AFAIK it should be release before next MRL meeting      

> __< jeffro256 >__ *released      

> __< selsta >__ I agree with jeffro's proposal, as long as it's timed up so that all audits complete in time before the HF activates, with a small buffer     

> __< articmine >__ selsta: I agree     

> __< tevador >__ "small buffer" should be at least 1 month     

> __< rucknium >__ How soon, from today, is the expected HF code freeze, i.e. when would the 6-month clock start ticking?     

> __< jeffro256 >__ I'll also release my Gannt chart that I'm working, so we can have something more concrete than a collection of English chat logs to describe the timeline      

> __< tobtoht >__ Are we still branching v0.19 from master to test Guix and other changes in master?     

> __< jeffro256 >__ rucknium: tevador were you talking about a pre-first-HF-enabled release code freeze, or a pre-HF-activation code freeze?     

> __< selsta >__ tobtoht: I would say yes     

> __< selsta >__ Polyseed looks more or less ready     

> __< jeffro256 >__ We should do that ASAP IMO      

> __< tevador >__ I think the code freeze should generally precede the first release binaries     

> __< jeffro256 >__ Would that be a code freeze on consensus and node related code. For example, would multisig support / HW support / wallet knowledge proofs / other wallet-specific features be under this code freeze?     

> __< selsta >__ what's the status from stressnet for txrelay v2? ready for v0.19?     

> __< tevador >__ jeffo256: That's debatable, but generally you want to freeze all features before the release and focus on bug fixes     

> __< vtnerd >__ yeah theres lws RPC changes for example that someone has to slog through (review)     

> __< rucknium >__ selsta: I think we should get at least a week of more testing with the latest proposed fix of the double-spend issue, IMHO.     

> __< jeffro256 >__ tevador If we freeze all features, that would push back the HF activation by several months for features that could be developed in parallel IMO      

> __< selsta >__ I have always disliked an overly strict code freeze     

> __< jeffro256 >__ I think that that kind of a freeze is simply too broad      

> __< jeffro256 >__ I would agree that p2p and consensus features should be frozen for some period of time before release      

> __< tevador >__ non-consensus changes can go into .1 anyways     

> __< jeffro256 >__ I think that basic sending / receiving / syncing wallet features should be frozen before the first release too      

> __< tevador >__ What is the expected timeline for the HF? Can RandomX v2 stil make it?     

> __< jeffro256 >__ But, respectfully, waiting for Trezor and Ledger to activate FCMP++ would be a mistake      

> __< jeffro256 >__ They don't move very fast      

> __< rucknium >__ Isn't RandomX v2 already ready? sech1  ?     

> __< tevador >__ It's ready but not on the daemon side AFAIK?     

> __< rbrunner >__ That's also what I dimmly remember     

> __< selsta >__ there is a PR for it on daemon side, jeffro wrote it     

> __< selsta >__ RandomX v2 wallet related code is not developed yet but that doesn't require HF     

> __< rucknium >__ Do any HW wallet manufacturers move fast? Could there at least be one sure to be ready for the HF?     

> __< jeffro256 >__ tevador: The expected timeline for the HF is what I'm trying to decide. RandomX v2 should be able to make it. I have this PR: https://github.com/monero-project/monero/pull/10038. I need to add back the tx count and update the flow charts in the documentation, if we are to keep it      

> __< jeffro256 >__ But besides that, the consensus changes are done      

> __< jeffro256 >__ I plan to integrate DoS-resistant header-only sync after #10038 is merged, but that shouldn't be a blocker to the FCMP++ release      

> __< tevador >__ Thanks, I missed that PR     

> __< jeffro256 >__ rucknium: I'm trying my damndest      

> __< jeffro256 >__ It would probably help to have a bunch of people bug them, IDK      

> __< rucknium >__ jeffro256:monero.social: I know you are. Thanks. But would users have an alternative in time for the HF?     

> __< selsta >__ realistically Ledger/Trezor will use LLMs to implement FCMP++ so I assume it won't take too long     

> __< rucknium >__ oh no     

> __< gingeropolous >__ i ponder if we should add things to make the codebase llm friendly     

> __< rucknium >__ Maybe their revenue isn't great right now.     

> __< rbrunner >__ Many, many comments help. Something we are proudly famous for :)     

> __< rucknium >__ rbrunner: Is that sarcasm from you?     

> __< rbrunner >__ Yes, of course ...     

> __< rucknium >__ I think we should move the agenda along. Feel free to discuss this agenda item after the meeting.     

> __< rbrunner >__ Well, not the comment bit. They do support the work of LLMs greatly, from the little I know so far     

> __< rucknium >__ 4. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< tevador >__ I updated the proposal. Thanks to UkoeHB and kayabaNerve's comments, the new proposal includes completely private relative time-locks using ring signatures. I also posted a trustless payment channel protocol enabled by the proposal.     

> __< rucknium >__ Thank you, tevador     

> __< rbrunner >__ Just wondering: If that proposal fully works out, may this result in the best Monero channel proposal so far?     

> __< rucknium >__ > The approximate size of a 7-ring signature is 256 bytes, which is relatively small compared to the size of the FCMP++ proof.     

> __< rucknium >__ Would the 256 bytes go into the tx_extra only of txs that need it?     

> __< tevador >__ No, this would be a hard forking change for all transactions     

> __< jeffro256 >__ I think that it need to be validated by consensus for it to be relied upon by a counterparty      

> __< articmine >__ It is still a very  small cost from a scaling perspective      

> __< jeffro256 >__ tevador: Technically, it could be a soft fork if v17 doesn't enforce unlock_time=0     

> __< tevador >__ The ring signature definitely has to be validated by consensus, otherwise transactions could spend enotes not present in the chain.     

> __< rucknium >__ I'm not very enthusiastic about adding to blockchain size in every tx for payment channels.     

> __< rucknium >__ Would this be useful to simplify atomic swaps?     

> __< tevador >__ on the flip side, it's all prunable data     

> __< tevador >__ Yes, it can also help for atomic swaps     

> __< rucknium >__ Prunable data does help     

> __< articmine >__ From a scaling perspective a payment channel that actually works can be very helpful      

> __< articmine >__ The small extra transaction weight is well worth it      

> __< tevador >__ I think this is the only way to get payment channels without a trusted 3rd party.     

> __< boog900 >__ what % of txs would have to be done off chain for this to be worth it?     

> __< sech1 >__ RandomX v2 is ready and released, XMRig version with v2 support is also released. Monero doesn't have v2 support yet.     

> __< rucknium >__ boog900:monero.social: About 5% to break even, right?     

> __< tevador >__ boog900: If the average fcmp++ tx size is 10K then about 2.5% unless I'm mistaken     

> __< tevador >__ My original proposal was using unlock_time = 1, which is an existing field, so 0 extra bytes, but it leaks.     

> __< articmine >__ boog900: 256/(tx size in bytes)     

> __< boog900 >__ do we know how much lightning does?      

> __< boog900 >__ of bitcoin's network      

> __< articmine >__ Lighting is broken because of a broken later 1 on scaliny     

> __< articmine >__ Layer 1     

> __< rucknium >__ boog900:monero.social: AFAIK, it has not been measured at the whole network scale, but some merchants have on-chain BTC and lightning enabled. That could give a hint.     

> __< rbrunner >__ So maybe motivation to use Monero payment channels is less than with lightning?     

> __< tevador >__ a quick search gives 200K lightning txs/day and 500K bitcoin txs/day     

> __< rucknium >__ Monero's low fees would push fewer user to use a PCN (payment channel network).     

> __< articmine >__ It is not a fair comparison to use LN on BTC     

> __< ravfx:xmr.mx >__ If only LN would work consistently.     

> __< ravfx:xmr.mx >__ You need to have like many channels well connected (like 4-5, to big centralized node). For it to be usable.     

> __< ravfx:xmr.mx >__ I test it on average, one time a year     

> __< articmine >__ rucknium: Not necessarily. Low fees will make the payment channel secure     

> __< articmine >__ Unlike BTC     

> __< rbrunner >__ I think we also have many unknowns here. E.g. how far we try to go with routing payments over multiple hops.     

> __< articmine >__ We don't need routing      

> __< tevador >__ I think payment channels are most useful for small single hop channels (repeated payments)     

> __< articmine >__ This is one of the problems with LN on BTC     

> __< ravfx:xmr.mx >__ Have to try all possible route til it fine one that work right or abort (if it work similar to LN).     

> __< ravfx:xmr.mx >__ Can it actually be made without routing?     

> __< ravfx:xmr.mx >__ tevador: Yeah, create a channel with the entity you are going to pay to, that's what work better     

> __< rucknium >__ tevador: I agree with that. But that's a small use case.     

> __< rbrunner >__ Could turn out be a pretty small market right now, repeated XMR payments ...     

> __< ravfx:xmr.mx >__ Everything related to IT stuff (VPS, VPN, etc, etc... repeated XMR payments     

> __< rucknium >__ Won't you still need an always-alive process to be running somewhere, with internet access?     

> __< articmine >__ I am sitting at a Starbucks. It is not a small use case      

> __< boog900 >__ 256 bytes isn't crazy but it's not so small where I think this is definitely worth it.     

> __< tevador >__ Could be reduced down to ~100 bytes with just 2 possible lock times (e.g. 10 blocks and 720 blocks)     

> __< tevador >__ The leaky version is 0 bytes     

> __< rbrunner >__ The leak is "I am a channel related tx", right?     

> __< ravfx:xmr.mx >__ One of the only advantage of BTC LN, is that they are instant (when they work). Do we need a 10 lock timer?     

> __< rbrunner >__ More or less, if people don't lock for other purposes     

> __< tevador >__ Yes, eveyone could see unlock_time = 1 in the tx     

> __< rucknium >__ tevador: tevador: After analysis, does your 0-byte leaky version still work, with the same features as the 256-byte one?     

> __< jeffro256 >__ rbrunner: More lile "I am possibly a channel-related tx. I may also be a normal spent outside where the age is >= 24 hours"     

> __< jeffro256 >__ *like     

> __< jeffro256 >__ *normal spent enote      

> __< jeffro256 >__ gah     

> __< tevador >__ The leaky version only supports 2 locks times. The ring signature-based one can have many possible times (the proposal currently lists 7 lock times from 10 blocks to 8 years).     

> __< rbrunner >__ Ok. That's not really terrible, as leaks go :)     

> __< articmine >__ It t like ~3% of a 2in 2out tx     

> __< articmine >__ 256 bytes      

> __< tevador >__ Technically, the leaky version can support more lock times at the cost of more leakage     

> __< rucknium >__ Isn't Lightning's HTLC use standardized to a specific lock time?     

> __< tevador >__ If people think 256 bytes is too much, I can put the leaky version back into the proposal as an option     

> __< tevador >__ I personally found 256 prunable bytes a rounding error     

> __< rucknium >__ "I think this is the only way to get payment channels without a trusted 3rd party." Have you looked at all the Monero payment channel papers to check this claim? > <tevador> I think this is the only way to get payment channels without a trusted 3rd party.     

> __< rbrunner >__ We could still switch / elevate to the hidden version if payment channels should become widely popular? After starting with the dead-simple leaky version, I mean.     

> __< tevador >__ rucknium: I checked published papers about Monero payment channels and they all use a key escrow. However, it's possible that I missed some paper. I'm not aware of any proposal without a trusted 3rd party.     

> __< rucknium >__ Search for "payment channel" here: https://moneroresearch.info     

> __< rucknium >__ https://moneroresearch.info/203 Wang, X., Lin, C., Huang, X., & He, D. (2023). Anonymity-Enhancing Multi-Hop Locks for Monero-Enabled Payment Channel Networks. IEEE Transactions on Information Forensics and Security, 1–1.       

> __< rucknium >__ I didn't look too closely for hidden assumptions.     

> __< rucknium >__ To me, the clearest use case for payment channels is XMRChat or similar services. You want to send multiple payments to the same recipient in less time than the 10 block lock.     

> __< rucknium >__ I don't remember if fiatdemise:matrix.org  has commented on payment channels.     

> __< boog900 >__ I don't know if this would work but we have tx pre-signing where anyone can make the membership proof right? Could we add a minimum height field to the pre-signed part of a tx and then make the membership proof when it becomes spendable?      

> __< boog900 >__ Normal txs will set this minimum height field too so no txs stand out?     

> __< jeffro256 >__ boog900: It would leak the signing date for pre-signed txs      

> __< boog900 >__ ah yeah :(     

> __< boog900 >__ We could have some txs set it to 0 randomly?     

> __< vtnerd >__ the curve tree root is the issue     

> __< vtnerd >__ or maybe Im mistaken on how that works     

> __< tevador >__ payment channels need a relative lock, a minimum height restriction is an absolute lock     

> __< tevador >__ a relative lock is more useful - you can simulate an absolute lock using a relative lock but not vice versa     

> __< boog900 >__ its a minimum height on when you can add the tx to the chain, this is the same as setting unlock_time requiring the tree root to be so many blocks old     

> __< boog900 >__ in the original      

> __< tevador >__ if it's the min height *difference* then it's exactly my "leaky" proposal with unlock_time = 1     

> __< tevador >__ The point is that you have 2 offline pre-signed transactions TA and TB. TB spends from TB. You don't know when TA will be submitted.     

> __< tevador >__ TB spends from TA*     

> __< boog900 >__ Kinda but it allows you to use the most up to date tree root so doesn't require locked txs to expose that they are spending an output over a day old.     

> __< boog900 >__ It keeps the fact the tx was locked private      

> __< tevador >__ Your proposal is an absolute lock, which won't work for payment channels     

> __< boog900 >__ I don't see how it is any different      

> __< tevador >__ You can comment your proposal in issue #161, but you are proposing an absolute lock (i.e. the signer signs the height)     

> __< rucknium >__ 5. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). Jamtis (https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).     

> __< tevador >__ I have no comments on this agenda item     

> __< rucknium >__ 6. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ jberman:monero.social and I are working on the wallet-forgetting-it-spent-a-coin problem. This might be the code that fixes it.     

> __< rucknium >__ I think we are at 100GB unpruned blockchain size now.     

> __< rucknium >__ Anything else on stressnet?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< jeffro256 >__ Thanks everyone!     

> __< tevador >__ rucknium: I checked the "multi-hop locks" paper you linked earlier. It doesn't define a payment channel protocol for Monero. It provides a method how to extend an existing single-hop PC into a multi-hop network. So naturally, it requires a pre-existing payments channel protocol (it mentions PayMo).     

> __< tevador >__ PayMo is an existing PC protocol for Monero, but it has expiring channels, which is a big disadvantage (shared with all protocols that use absolute locks) and requires a trusted setup.     

> __< rucknium >__ tevador: Thanks for giving it a look     

> __< UkoeHB >__ ravfx: re: 10 block lock. You’d need the lock for opening/closing/recover tx submission (so a minimum 30min to open/close channel + multisig setup). But state changes would be fast (a few messages back and forth).     

> __< UkoeHB >__ 60min* 30 blocks     

> __< gingeropolous >__ if anyone has any ideas for experiments for monerosim on the MRC, let me know.  I know someone recently mentioned the p2p ssl PR . Unfortunately anything PoW is off the table (proper PoW hooks require modding monero code). ( of course, anyone can use monerosim on their hardware or rent some beefy stuff to run big sims or use it on the MRC themselves)     

> __< boog900 >__ gingeropolous: What RPC endpoints do you need for monerosim? Cuprate has the ones wallet use working     

> __< boog900 >__ Or working enough for wallets, some stuff that isn't needed for wallets is still stubbed      

> __< boog900 >__ We are currently testing wallet RPC before a beta release so more testing is welcome :)     

> __< rucknium >__ boog900:monero.social: I don't think any RPC endpoints are needed. Some nodes in the simulation just act as P2P tx relay nodes. There may be other blockers to dropping cuprate into the simulation.     

> __< boog900 >__ Ah I thought RPC was the blocker from previous conversations      

> __< boog900 >__ I am happy to look at adding whatever is needed to cuprate to get it working in the sim though      

> __< gingeropolous >__ yeah i can point the bot at cuprate integration, then we can compare the networks in the sim with/without cuprate etc.      

> __< gingeropolous >__ https://github.com/cuprate/cuprate >>>> use a release or master?     

> __< rucknium >__ boog900:monero.social: Maybe you were thinking about stressnet monitoring.     

> __< boog900 >__ gingeropolous: Main     

> __< boog900 >__ https://matrix.to/#/!zPLCnZSsyeFFxUiqUZ:monero.social/$qyu0xFeLaLeaXi4LphYjoxc3ZY1itq-mMlik1xluhUo?via=monero.social&via=matrix.org&via=unredacted.org     

> __< boog900 >__ rucknium: I remember that, I'll have the ones used there ready when we have FCMP ready, hopefully in time to still have a stressnet running :)     

> __< rucknium >__ boog900: Yes you'll need RPC endpoints if you want a cuprate-only Monerosim because txs have to be submitted to nodes.     

> __< boog900 >__ Ah ok, we should support that now as that'll just fall under what wallets need     




# Action History
- Created by: Rucknium | 2026-07-16T22:20:20+00:00
