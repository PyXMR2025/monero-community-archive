---
title: Monero Research Lab Meeting - Wed 09 September 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1454
author: Rucknium
assignees: []
labels: []
created_at: '2026-09-08T18:17:12+00:00'
updated_at: '2026-09-15T20:29:42+00:00'
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

3. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). [FCMP++ Integration Audit Overview](https://github.com/seraphis-migration/monero/issues/294). [Network upgrade schedule Gantt chart](https://html-preview.github.io/?url=https://github.com/jeffro256/fcmp-carrot-plan/blob/master/fcmp%2B%2B-carrot.html).

4. [`monerosim` spy node analysis](https://gist.github.com/Rucknium/ba230a2bab8a446d0997b7b002bf3af6).

5. [Relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

6. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/). [Version 3 launch checklist](https://github.com/seraphis-migration/monero/pull/415).

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1451 

# Discussion History
## Rucknium | 2026-09-15T20:29:42+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1454     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ hi     

> __< jberman >__ waves     

> __< ack-j:matrix.org >__ Hi     

> __< tevador >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< vtnerd >__ me: specifically going through the SSL review by an LLM, and otherwise have been doing serialization/lws stuff     

> __< rucknium >__ Me: Finished monerosim spy node analysis (https://gist.github.com/Rucknium/ba230a2bab8a446d0997b7b002bf3af6). Looking at selfish mining defenses again.     

> __< tevador >__ mx25519, polyseed and some relative locks work     

> __< ack-j:matrix.org >__ Me: implementing feedback from reviewers to make https://github.com/xmrack/monero-review more useful     

> __< jberman >__ me: all phase 2 FCMP++ integration upstream PR's are ready for review (including tree building here https://github.com/monero-project/monero/pull/10724 ), reviewed the FCMP++/Carrot hot-cold wallet PR, touched up the tx relay v2 PR, and some upstream PR review     

> __< rucknium >__ 3. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/). FCMP++ Integration Audit Overview (https://github.com/seraphis-migration/monero/issues/294). Network upgrade  [... too long, see https://mrelay.p2pool.observer/e/9tuNhakLcUVGRnlQ ]     

> __< jberman >__ On research tasks: we're evaluating the quotes to audit the circuit + gadgets impl + fcmp-plus-plus lib, we've received all quotes. Will have more on this next week     

> __< jberman >__ The hot/cold wallet PR I personally think is nearly complete (thank you to jeffro256:monero.social for the hard work there)     

> __< jberman >__ Making progress on upstream integration PR's with reviews     

> __< jberman >__ The hot/cold wallet PR is basically the next major milestone to keep an eye out for     

> __< rucknium >__ Thanks, jberman:monero.social . Anything more on this topic?     

> __< jberman >__ nothing from me     

> __< rucknium >__ 4. monerosim spy node analysis (https://gist.github.com/Rucknium/ba230a2bab8a446d0997b7b002bf3af6).     

> __< rucknium >__ This little project had two purposes. First, to test the resistance of Monero's implementation of Dandelion++ against a spy node adversary. Second, to test and establish a statistical methodology to use the monerosim network simulator to measure network behavior.     

> __< rucknium >__ AFAIK, this is the first test of Monero's D++ spy node resistance that uses a network of real running nodes (please correct me if I am wrong).     

> __< rucknium >__ Congratulations, it passed!     

> __< rucknium >__ Especially congratulations to vtnerd:monero.social who coded most of the D++ implementation AFAIK. And the helpers and reviewers.     

> __< rucknium >__ monerod is achieving a p percent detection of the true tx origin when the network is made up of p percent spy nodes. That is what the D++ paper claims in its theorems.     

> __< rucknium >__ In the gist, I use cluster-robust inference to augment the usability of a small number of simulations. The problem I'm overcoming is that multiple measurements in the same simulation are not statistically independent.     

> __< rucknium >__ The paper that described D++ (Fanti et al. 2018) actually did not run a network of bitcoin nodes with D++ implemented to test D++. Instead, they used simplified python simulations and a lot of theoretical results. They did implement D++ in a bitcoin patch, but they just used it to test network propagation latency on bitcoin's mainnet.     

> __< rucknium >__ Later, this paper actually did use real bitcoin nodes inside Docker containers to test D++: Franzoni & Daza (2022). "Clover: An anonymous transaction relay protocol for the bitcoin P2P network."     

> __< rucknium >__ monerosim is much better than a set of Docker nodes because it actually can use global internet latency data and its results are deterministic, i.e. the runs are reproducible.     

> __< rucknium >__ Lots of thanks to gingeropolous:monero.social who has helped fix issues in monerosim as I've encountered them.     

> __< tevador >__ It's an interesting test, but in practice, spy nodes don't have the same way as honest nodes. For example, they try to stuff their peer lists with other spy nodes.     

> __< tevador >__ behave*     

> __< rucknium >__ tevador: Yes. There are a lot of ways that the simulation isn't realistic, but I wanted to, at least at first, reproduce the D++ theoretical results.     

> __< rucknium >__ For example, the simulation has no unreachable nodes, but Monero mainnet probably has a majority unreachable nodes. The D++ paper ignored unreachable nodes, so I did, too, in this test. monerosim has the capability to have unreachable nodes, but I did not use it here.     

> __< tevador >__ But it's a good sign that our D++ implementation is working.     

> __< sgp_ >__ The goal is to make a decision during the next meeting, and I'll make sure that the info is shared in this channel on Monday. We received 7 quotes > <jberman> On research tasks: we're evaluating the quotes to audit the circuit + gadgets impl + fcmp-plus-plus lib, we've received all quotes. Will have more on this next week     

> __< boog900 >__ This test was without the changes to the embargo timer right? I wonder if that would meaningfully change anything (probably not)     

> __< sgp_ >__ rucknium:monero.social: do you consider monerosim to be "finished" or are there some things that you are still working on?     

> __< rucknium >__ There are numerous extensions of this test I could do. Or I could try another type of measurement with monerosim. I am open to either. I think I would prefer to prioritize looking again at proposed selfish mining defenses, but input on my priorities is appreciated.     

> __< rucknium >__ boog900:monero.social: I was wondering the same thing. I think the embargo timer would come into play with active spy node behavior, i.e. executing black hole attacks. Or increasing the packet loss rate in Shadow.     

> __< sgp_ >__ Is there anything you’ve already decided needs to be added/extended and will work on that next, or are you looking for fresh ideas?     

> __< rucknium >__ sgp_:monero.social: That's a good question to also ask gingeropolous:monero.social . I think all the basic functionality is there. Another purpose of doing this was to encounter problems that needed to be fixed or bring up feastures when doing a real analysis, which we did.     

> __< sgp_ >__ Basically: what do you plan to do next, I guess. The selfish mining?     

> __< rucknium >__ sgp_:monero.social: Fresh ideas are good.     

> __< rucknium >__ Yes, i want to go back to selfish mining. I anticipate I won't use monerosim much for that. Maybe at the final stages of a proposed implementation, but not at these earlier stages. I am trying to get some "hidden" metrics in Markov Decision Process results in some earlier papers.     

> __< rucknium >__ Here are some of the issued I found and were addressed by gingeropolous:monero.social : https://github.com/Fountain5405/monerosim/issues?q=is%3Aissue     

> __< rucknium >__ Well, ClaudeAI addressed them, but gingeropolous:monero.social guided it.     

> __< rucknium >__ More on this agenda item?     

> __< rucknium >__ By the way, I think log parsing could slow down other investigations with monerosim. I already had code written to parse tx broadcast logs, but you would need other ways to parse the logs for other investigations and metrics.     

> __< rucknium >__ 5. Relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< tevador >__ I tried to add some tests to the relative locks PRs, but got stuck on a hack in the FCMP++ test code: https://libera.monerologs.net/no-wallet-left-behind/20260906#c705669     

> __< rucknium >__ I mean, monerosim should theoretically be usable by any dev who wants to analyze some patch.     

> __< sgp_ >__ I have a topic/announcement for the end of the meeting if there is time, otherwise I can wait for next week     

> __< rucknium >__ sgp_:monero.social: OK I will put you at the end unless the meeting goes very long.     

> __< rucknium >__ IIRC, one of the reasons that the old lock style is deprecated is because FCMP makes it more complicated to keep track of the locked txs. Does relative locks have any interaction with that? (I hope not).     

> __< tevador >__ No, the relative locks work completely differently. They have no impact on the tree building process.     

> __< rucknium >__ git blame doesn't work on those lines. It's just a mega commit, it says. I was going to ask who wrote that so they could be queried.     

> __< tevador >__ I don't want to delay the meeting, so if someone is familiar with the test code, we can talk in #no-wallet-left-behind.     

> __< rucknium >__ Sounds good. Thanks, tevador .     

> __< rucknium >__ 6. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/). Version 3 launch checklist (https://github.com/seraphis-migration/monero/pull/415).     

> __< jberman >__ just seeing that now, will respond in a bit tevador     

> __< jberman >__ I wrote that     

> __< jberman >__ All side PR's are prepared for beta v3, next is just hot/cold wallet PR then rebasing on latest master     

> __< sech1 >__ I'm late to the meeting, here's my update: P2Pool v5 is progressing at a good pace, I think I'll start testing it on the stressnet next week - not a feature complete version, but a version with minimal required FCMP++/Carrot code     

> __< rucknium >__ Thanks, sech1 . Anything more on this agenda item?     

> __< rucknium >__ 7. Any other business     

> __< rucknium >__ Your turn, sgp_:monero.social     

> __< sgp_ >__ Thank you rucknium:monero.social . I have some humbling news for which more information will be shared by MAGIC Grants soon     

> __< sgp_ >__ A few months ago while a researcher was working on a MAGIC Grants contract, they identified potential issues with the Bulletproofs+ security proofs, which Monero uses. They reached out to MAGIC Grants to report what appeared to be a potential soundness (inflation) issue. Luckily, this was NOT a soundness issue after more analysis     

> __< sgp_ >__ It was still very scary     

> __< sgp_ >__ Immediately after receiving the report, the MAGIC Grants board approved and paid from its own funds a full review of the BP+ security proofs, and there are no known issues after a further analysis. This report will be posted publicly in full in the coming days     

> __< rucknium >__ By the way you say it, it seems that this was something that was identified in BP+, but not regular BP. Is that the case?     

> __< rucknium >__ And was the investigation AI-assisted?     

> __< sgp_ >__ There is a lot more info to share and a lot of people to thank for their work during the disclosure, but that is what I can share for now. It serves as a reminder of why these reviews are so important before we deploy FCMP++. Importantly, the level of caution that the Monero community has approached FCMP++ with has far exceeded the caution issued to prior deployments     

> __< sgp_ >__ The investigation was not AI assisted     

> __< sgp_ >__ yes, it was specific to BP+     

> __< rucknium >__ "Importantly, the level of caution that the Monero community has approached FCMP++ with has far exceeded the caution issued to prior deployments". I agree on that point. And I'm glad.     

> __< rucknium >__ Well, not glad that prior deployments didn't have as much scrutiny. But glad that FCMP++ is getting high scrutiny.     

> __< rucknium >__ Is it a real issue in BP+ proof, but not a soundness issue? Or was the mathematical proof not correct, but the proof could be correct and the soundness holds after all? Maybe I should wait for the full announcement.     

> __< sgp_ >__ That’s all from me for now     

> __< sgp_ >__ rucknium: Additional supporting proofs support Monero's use     

> __< rucknium >__ Sorry, I meant "proof could be correct_ed_", i.e. repaired.     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< gingeropolous >__ re: monerosim and spy nodes, you could script the spy nodes to stuff their peer lists. anything you can do to a monerod you can do to it in monerosim. its just monerod.  Re: monerosim and selfish mining, currently thats not really possible. Due to the nature of shadow, you can't actually mine with monerod. For the current mone [... too long, see https://mrelay.p2pool.observer/e/uouTiakLWGtqUXY5 ]     

> __< gingeropolous >__ there's also a second PR by a bot waiting that allows for testing forks. I guess i could roll both into a patch thats applied to vanilla monerod for the time being     

> __< sech1 >__ sgp_ rucknium I asked a frontier LLM what was it, and it was able to figure it out,, so you already said too much 🤷‍♂     



# Action History
- Created by: Rucknium | 2026-09-08T18:17:12+00:00
