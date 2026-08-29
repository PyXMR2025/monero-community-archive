---
title: Monero Research Lab Meeting - Wed 19 August 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1443
author: Rucknium
assignees: []
labels: []
created_at: '2026-08-17T21:45:15+00:00'
updated_at: '2026-08-26T13:35:41+00:00'
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

3. [PQ turnstile spend enables a Carrot/Jamtis distinguisher (privacy leak)](https://github.com/jeffro256/carrot/issues/10).

4. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). [FCMP++ Integration Audit Overview](https://github.com/seraphis-migration/monero/issues/294). [Network upgrade schedule Gantt chart](https://html-preview.github.io/?url=https://github.com/jeffro256/fcmp-carrot-plan/blob/master/fcmp%2B%2B-carrot.html).

5. [Relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

6. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/). [Version 3 launch checklist](https://github.com/seraphis-migration/monero/pull/415).

7. [PoW-Admitted Zero-Fee Transactions for P2Pool](https://gist.github.com/SChernykh/aae5b2d414095e742437134ab20d4353).

8. Any other business

9. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1440    

# Discussion History
## Rucknium | 2026-08-26T13:35:41+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1443     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ Hi     

> __< slowbeardigger:matrix.org >__ Hello     

> __< jberman >__ waves     

> __< jeffro256 >__ Howdy     

> __< rbrunner >__ Hello     

> __< articmine >__ hi     

> __< jpk68:matrix.org >__ Hello     

> __< sech1 >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< slowbeardigger:matrix.org >__ Not sure if it is relevant to the meeting but I am working on carrot25519, a little experimental C11 allocation-free primitive implementing the raw Montgomery ladder that CARROT uses, with portable/fiat51, ARM64/cc0, x86_64-baseline and BMI2+ADX backends, still need some optimizations, and DataHoarder and Tevador been helping :)     

> __< slowbeardigger:matrix.org >__ slowbeardigger:matrix.org: parallel to that I’m pushing the xmr-pay Carrot side (view-key only scanning + settlement/reorg) so compatible payment integrations can be ready for the community as soon as public stressnet or mainnet Carrot lands. (yay)     

> __< sech1 >__ I'm working on adding Carrot-compatible coinbase transactions to P2Pool (last week I was quite busy IRL, so this work just started)     

> __< DataHoarder >__ hello. seeing sech1 move to Carrot/FCMP++ for P2Pool and reviewing anything     

> __< jpk68:matrix.org >__ Me: attempting to decrease lock contention in monerod     

> __< jberman >__ Some upstream PR handling and re-reviewing the Carrot hot/cold wallet PR     

> __< rucknium >__ me: Testing Dandelion++ privacy protections in monerosim. Not ready to share statistical results yet, but everything looks good so far. I can get precise estimates of spy node effectiveness with just a few dozen simulation runs. Continuing to report issues in monerosim: https://github.com/Fountain5405/monerosim/issues     

> __< ack-j:matrix.org >__ Hi     

> __< vtnerd >__ me: spent time updating serialization code (still not pred), updated/tested racy code in epee/levin, and now working on updating all my prs to work against head master version     

> __< jeffro256 >__ me: implemented tevador's suggestion for PQ turnstile indistinguishability: https://github.com/seraphis-migration/monero/pull/456. Reviewing upstream PRs     

> __< rucknium >__ 3. PQ turnstile spend enables a Carrot/Jamtis distinguisher (privacy leak) (https://github.com/jeffro256/carrot/issues/10).     

> __< jeffro256 >__ PR for K^j_v implementation here: https://github.com/seraphis-migration/monero/pull/456. API for scanning coinbase enotes changed slightly, requiring the user to pass their main address view pubkey, but otherwise the API didn't need updating      

> __< jeffro256 >__ If we go with the above change, I'll need to update the Carrot spec      

> __< rucknium >__ Would the change require anything to be re-audited or receive external review again?     

> __< DataHoarder >__ Carrot spec already needs update due to the personalization string / Generator T changing     

> __< DataHoarder >__ And https://github.com/seraphis-migration/monero/pull/424     

> __< jeffro256 >__ I don't think so, because actually the first Carrot spec audit had d_e bind to K^j_v, so it's actually already been audited      

> __< jeffro256 >__ DataHoarder: You're right about the T generator, but #424 doesn't require changes to the spec      

> __< jeffro256 >__ It's a big API overhaul, but it didn't change anything with the protocol itself      

> __< DataHoarder >__ Oh, fair, I guess we just pick the values differently. I do remember a few tweaks were also done for the PQ turnstile to work for coinbase outputs, cannot remember if those were brought back to spec     

> __< jeffro256 >__ Yes, the PQ stuff should already be in the latest version of the spec      

> __< rucknium >__ More on this topic? Should it appear on the agenda next week, too?     

> __< jeffro256 >__ If tevador isn't here, then there's not too much to discuss      

> __< jeffro256 >__ I think that the rest of the discussion could happen on that Github issue      

> __< rucknium >__ I will take it off the agenda next week unless someone requests it to be placed on the agenda.     

> __< rucknium >__ 4. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). FCMP++ Integration Audit Overview (https://github.com/seraphis-migration/monero/issues/294). Network upgrade  [... too long, see https://mrelay.p2pool.observer/e/yLqkpKILb3IwaHJr ]     

> __< jberman >__ Next major item: Re-reviewing jeffro256:monero.social's hot/cold wallet PR now, which is also currently a dependency for UkoeHB 's multisig work. Hot/Cold wallet stuff is very close I think     

> __< jberman >__ RFQ is going out for gadgets + circuit + fcmp-plus-plus audit, nothing to report on there yet     

> __< jeffro256 >__ Licensing discussion still ongoing in https://github.com/monero-project/monero/pull/10964 for mx25519. Tevador proposed an interesting solution: effectively make the core API+portable impl licensed permissively, and the fast assembly backends (where the magic happens) copyleft     

> __< jeffro256 >__ I was hoping that he'd be here today, oh well      

> __< rucknium >__ Thanks, jberman:monero.social  and jeffro256:monero.social . More on this topic?     

> __< rbrunner >__ That "trick" probably won't extend to the much simpler Polyseed library?     

> __< jeffro256 >__ I was wondering if it would be worth it to work on a quick license library to fetch license text to display in-binary for applicable licenses      

> __< jeffro256 >__ Unless tevador chooses to re-license, then Polyseed remains under LGPL      

> __< tobtoht >__ jeffro256: How would that work?     

> __< slowbeardigger:matrix.org >__ What about, relicensing the mx25519 to MPL-2.0 pls split the library?     

> __< slowbeardigger:matrix.org >__ like BSD-3 the core + C portable implementation, MPL-2.0 the assembly backends     

> __< slowbeardigger:matrix.org >__ Compilation flags included on the fast assembly[... more lines follow, see https://mrelay.p2pool.observer/e/mP--pKILQjhCa2N2 ]     

> __< slowbeardigger:matrix.org >__ I think Trevador said he likes a way like that     

> __< tobtoht >__ That's exactly the solution tevador suggested.     

> __< slowbeardigger:matrix.org >__ yeah     

> __< slowbeardigger:matrix.org >__ if you ask me, that seems to be the “easiest” way     

> __< articmine >__ The licensing issue raisees many questions for dicussion.     

> __< slowbeardigger:matrix.org >__ Gets the thing done in a couple of commits, and not a lot of drama     

> __< slowbeardigger:matrix.org >__ less friction way imo     

> __< articmine >__ I am just looking at the Github     

> __< jeffro256 >__ tobtoht: It would look like a license command in daemon/wallet CLI/wallet RPC etc which pulls text from an in-binary array, which is inserted during build time based on a maintained license file     

> __< jeffro256 >__ So when we add a new dependency which requires distrubuting source code information alongside the binary, a contribuor would append applicable info to the license file, which gets added into the binary during build time      

> __< jpk68:matrix.org >__ Not sure there's much point to the licensing section of the CoC if it can just be ignored     

> __< jeffro256 >__ Even without mx25519/Polyseed we should probably do this because we are out of compliance with some BSD-3 licensing      

> __< tobtoht >__ Our biggest licensing issue right now is our GPLv3'd readline dependency     

> __< tobtoht >__ I suggested replacing it with linenoise from Redis     

> __< jpk68:matrix.org >__ It would also be a drastic reduction in LoC for that functionality     

> __< rucknium >__ FWIW, R and python have a license text that can be printed with license().     

> __< rbrunner >__ Would this license content mechanism be available to smartphone wallet apps as well?     

> __< tobtoht >__ jpk68:matrix.org: Yep, would also drop ncurses.     

> __< tobtoht >__ rbrunner: We could expose it in wallet api?     

> __< rbrunner >__ Sounds reasonable.     

> __< rucknium >__ 5. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< rucknium >__ Last meeting, UkoeHB  said he would put review of https://github.com/seraphis-migration/monero/pull/445  on his list     

> __< rucknium >__ Any discussion of this for now? If not, I will move on to the next item.     

> __< rucknium >__ 6. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/). Version 3 launch checklist (https://github.com/seraphis-migration/monero/pull/415).     

> __< jberman >__ Re: relative locks, I just commented on the original issue here: https://github.com/monero-project/research-lab/issues/161#issuecomment-5345884915     

> __< slowbeardigger:matrix.org >__ oh boy     

> __< slowbeardigger:matrix.org >__ :) can’t wait     

> __< jberman >__ I think it could potentially help strengthen the case for them if the Grease people want to run with that primitive     

> __< jberman >__ Re: beta stressnet. Discussed with jeffro256:monero.social and we're going to aim to have the hot/cold wallet changes in for beta v3 as well. So desired order of operations is hot/cold wallet changes then rebase on top of latest master     

> __< jberman >__ The hot/cold wallet changes bring a pretty significant change to the wallet, and I think it'll be good to have it sorted out in that order      

> __< rucknium >__ I have shut down all my tx spammers and switched my nodes back to regular testnet.     

> __< jberman >__ So right now working on my re-review of the hot/cold wallet PR and hopefully we'll have that ready by next week. I know I said hoping by next week last week, but hot/cold wallet stuff does make sense to get in first for reasons above (which I wasn't considering when I said that)       

> __< jberman >__ And making sure hot/cold wallets are ready for the fork is obviously a requirement for the fork anyway     

> __< UkoeHB >__ Did not review that PR yet     

> __< jeffro256 >__ ukoe is the hot/cold PR sort of a prereq for some of the multisig stuff?     

> __< UkoeHB >__ Multisig branch is on top of that branch     

> __< UkoeHB >__ IIRC it's just tx_builder that's a dep     

> __< jberman >__ One thing I've been thinking that would be nice is to have some good concrete testing of the new wallet/daemon software before the fork. We don't need to spam during that period (that would spam current testnet), but a concerted effort at testing during that period would be nice     

> __< jberman >__ Maybe we'd want to consider an initial fork from current testnet that just separates networks, but maintain current rules pre-fork, that would allow people to spam     

> __< rucknium >__ jberman: You could have cuprate on stressnet for that time, too.     

> __< rucknium >__ More on stressnet?     

> __< jberman >__ nothing from me     

> __< rucknium >__ 7. PoW-Admitted Zero-Fee Transactions for P2Pool (https://gist.github.com/SChernykh/aae5b2d414095e742437134ab20d4353).     

> __< rucknium >__ sech1. And maybe DataHoarder[m]     

> __< DataHoarder >__ nothing from me here at this point     

> __< rucknium >__ sech1 was here at the beginning of the meeting.     

> __< sech1 >__ I created https://github.com/monero-project/monero/pull/11102 to make life easier for P2Pool when handling these transactions     

> __< sech1 >__ This item can be removed from agenda for the next meeting, because I'll be working on general FCMP++/Carrot support for P2Pool, and zero-fee transaction support will be added after all that.     

> __< rucknium >__ More discussion on this item?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< slowbeardigger:matrix.org >__ Thanks, have a good one y'all     

> __< tevador >__ apologies for missing the meeting     

> __< selsta >__ Polyseed could also be made optional, since we need to keep old seed code for backwards compatability anyway, it could be disabled during compile time and old seed code is used. For those niche cases where copyleft code is not acceptable it should be fine to not have Polyseed. A relicense to MPL 2.0 like mx25519 would still be good.     

> __< articmine >__ selsta: What would be an example niche case where copyleft code is not acceptable?     

> __< tevador >__ Yes, Polyseed is definitely optional. Wallets that don't support Polyseed can still be used to import Polyseed converted to a legacy seed (it's a one way conversion).     

> __< selsta >__ BTCPay Server for example would have extra compliance obligations when integrating Monero, they could disable Polyseed since it's not required for accepting payments.     

> __< selsta >__ (I did not research this example so it's possible it would not be an issue for them anyway)     

> __< tevador >__ BTCPay Server is open source, so where exactly the problem would be? https://btcpayserver.org/ links to their github, which, IMO, counts as "reasonable means" to provide the source code per the MPL-2 license.     

> __< rbrunner7 >__ "Polyseed could also be made optional" Not soure how you mean that. People who build on Monero code but don't want the license burden would compile the code without Polyseed inclusion? Or would we public 2 different versions of the CLI wallet app, one with Polyseed and one without?     

> __< tevador >__ ^ I think optional here means there is a compile-time switch to disable it.     

> __< selsta >__ yes, for the public there would only be one version     

> __< selsta >__ tevador: I don't think including MPL 2.0 code would be an issue for BTCPay Server, but tobtoht had reservations and I don't know enough about licensing to judge myself. It appears a compile time switch is a compromise everyone agress on.     

> __< rbrunner7 >__ Well, if I think about the many, many places where I put in code to handle Polyseeds ... if the way to go is #if ... #endif around all of them, I don't know whether that idea would really fly ...     

> __< rbrunner7 >__ Or would we link in a dummy Polyseed library?     

> __< rbrunner7 >__ All the methods, but no code behind it?     

> __< jpk68:matrix.org >__ What is the benefit of Polyseed using a copyleft license? I can't think of any optimizations one would want to be open-sourced, which the author would be forced to reveal under a "weak" copyleft license such as the LGPL     

> __< jpk68:matrix.org >__ Dependency injection could also be used to circumvent it to some extent     

> __< rbrunner7 >__ Maybe some significant extensions, like using the checksum polynoms to restore a single missing word (as I think to remember that is technically possible)?     

> __< tobtoht >__ We can do a cleanroom reimplementation in C++ and license it under BSD-3. We already have a BSD-3 polyseed implementation written in Dart, could use that as a template. No licensing drama, no additional obligations, and our entire downstream gets to benefit from polyseed.     

> __< tevador >__ Speaking of the dart implementation: https://github.com/cake-tech/polyseed_dart/issues/7     

> __< boog900 >__ There is a Rust impl too: https://github.com/monero-oxide/monero-wallet-util/tree/main/polyseed     

> __< kayabanerve:matrix.org >__ I don't claim that to be clean room but it wasn't a translation and was written from scratch. The most copied would solely be the definition of constants.     

> __< kayabanerve:matrix.org >__ cc tevador if they want to clarify at first glance, if they believe it's derivative (re: GPL requirements) and/or would prefer any acknowledgement/statements.     

> __< kayabanerve:matrix.org >__ TBH, I'd prefer polyseed, the spec, be copyleft but the impls be BSD-3 or comparable. I don't think that is feasible under current legal constructs, even if it can be stated as a request within respectful society.     

> __< jpk68:matrix.org >__ Ah, how conducive to the spirit of open source. Let's impound ourselves with more bureaucracy and legal requirements     

> __< kayabanerve:matrix.org >__ As in, use or derivative designs have to specified, stated, and published, but my impl of Polyseed would be MIT while citing it is an impl of this spec licensed as follows.     

> __< kayabanerve:matrix.org >__ ^ ramblings, feel free to ignore, but I do welcome any opinions from tevador on if my Rust library is respectful or not. I'm willing to make adjustments to ensure it is, even if I don't believe I'd be legally obligated to.     

> __< kayabanerve:matrix.org >__ jpk68:matrix.org: This is off-topic for Lab so for my last message on this: People can want to abolish copyright. That doesn't change if I publish something with a request, people should reasonably respect my request. I should be allowed to say, if you use this spec, please declare so and state changes, even though your impl  [... too long, see https://mrelay.p2pool.observer/e/hM-aqKILUG5jX2Ns ]     

> __< tevador >__ The rust version doesn't look like a translation at first glance, at least not to the extent that the dart one does.     

> __< kayabanerve:matrix.org >__ But it's all up to tevador as it's tevador's thing. This was just my hat in the ring on what could be a good choice of license and requirements to ensure respect, but what's respectful is following what they request or choosing not to engage with them and their work. Free choice in association and all that.     

> __< jpk68:matrix.org >__ kayabanerve:matrix.org: Sure, people can do that all they want. I wasn't really taking issue with what you said; having the spec be copyleft and the implementation be permissive would even be preferable, IMO     

> __< kayabanerve:matrix.org >__ tevador: Cool. I won't insist that's a binding legal opinion. Lmk at any time if I can do anything to better acknowledge you :)     

> __< tevador >__ Yes, polyseed is missing a formal specification. That's something that should be fixed.     

> __< jpk68:matrix.org >__ However, a license is more than just an acknowledgment to respect someone's work - not sure if I can agree with something that would potentially let the state punish someone for "copying" source code. Does that not sound a bit dissonant to what the point of digital cash is?     

> __< tevador >__ I think it would be quite hard to violate MPL just by copying code. You'd have to either remove the copyright notices (this would also violate most permissive licenses) or make it closed-source.     

> __< jeffro256 >__ DataHoarder: I misspoke about the T generator, those changes are already in the spec     

> __< DataHoarder >__ unbiashed hash to point is changing, so that'd be changed to dc42e1d3307b2d4b3b02729abe577e231d79478141cb5b310ca9fa6e127616a3     

> __< DataHoarder >__ (it'd use blake2b with the Monero personalization string)     

> __< DataHoarder >__ you changed the representation here, https://github.com/monero-oxide/monero-oxide/pull/188 which changes the derived T value     

> __< jeffro256 >__ Durrr you're right, I copy and pasted the wrong value from that PR      

> __< DataHoarder >__ Hp^2 also needs to get updated with the new target commit ids, or maybe not, as H64 was indicated for use and it just ended up with Monero personalization being good everywhere     

> __< DataHoarder >__ also, on master I don't see any pushes since 4 months ago so maybe you are talking about a different local repo?     

> __< DataHoarder >__ I am looking at https://github.com/jeffro256/carrot unless there's somewhere else with the Carrot spec     

> __< ofrnxmr >__ Fwiw, i think they ship the stock monero binary, so i dont think it has to include anything? > <selsta> BTCPay Server for example would have extra compliance obligations when integrating Monero, they could disable Polyseed since it's not required for accepting payments.     

> __< ofrnxmr >__ also, btcpayserver doesnt ship or support monero upstream, btcpay-monero ships a plugin, and its that plugin that ships prebuilt monerod and monero-wallet-rpc. Also dont think they use seeds     

> __< ofrnxmr >__ (Just imported view-only wallets)     

> __< jpk68:matrix.org >__ IIUC, if they download pre-built release binaries and Polyseed/mx25519 is licensed under LGPL, they will indeed have to include licenses     

> __< jpk68:matrix.org >__ That may not be the case for MPL, however     




# Action History
- Created by: Rucknium | 2026-08-17T21:45:15+00:00
