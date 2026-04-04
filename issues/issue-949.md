---
title: Monero Research Lab Meeting - Wed 27 December 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/949
author: Rucknium
assignees: []
labels: []
created_at: '2023-12-27T15:01:08+00:00'
updated_at: '2024-01-26T19:51:24+00:00'
type: issue
status: closed
closed_at: '2024-01-26T19:51:24+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them? Info:
- [Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf)
- [Monero multi-signature patch review by Inference](https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf)
- [Rust alternative implementation](https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs) by @kayabaNerve

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#948 

# Discussion History
## plowsof | 2024-01-25T11:34:05+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/949     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< isthmus >__ Yo     

> __< h​into.janaiyo:matrix.org >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ Took some time off, but should be working on subaddress tests still later this week     

> __< a​ck-j:matrix.org >__ Hi     

> __< r​ucknium:monero.social >__ me: I think I will set Dec 31 as the cutoff day for new data to feeding into OSPEAD. There are a few minor unsolved issues, but I now have a system to produce preliminary results. I'll set a tentative internal deadline of Jan 31 to have the results ready regardless of whether I can solve the remaining minor issues.     

> __< h​into.janaiyo:matrix.org >__ preparing libraries for cuprate usage     

> __< isthmus >__ Reorganizing some code in the transaction fingerprinting library to be a bit more turnkey     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< h​into.janaiyo:matrix.org >__ Rucknium: did you make anything of the tor/i2p transaction %?     

> __< r​ucknium:monero.social >__ No. I cannot really see that in the data. But. Remember that mempool data I was collecting for the blockspace demand analysis, which then turned into the discovery about mining pools delaying tx confirmations unnecessarily? plowsof kept it running on his VPS, so we have the data about when txs first appeared in the mempool for the last 12 months     

> __< r​ucknium:monero.social >__ That tells us that those txs could be constructed no later than when they appeared in the mempool     

> __< r​ucknium:monero.social >__ Knowing when txs were constructed is important because the first spendable block after the 10 block lock has the highest probability of having a decoy selected from it. And probably the highest probability of a real spend.     

> __< r​ucknium:monero.social >__ By the way, Zano is updating their decoy selection algorithm. It has been uniform, which is bad. But they are now fitting a curve like Moser et al. (2018) to de-anonymized txs, I think: https://blog.zano.org/decoy-selection-algorithm/     

> __< r​ucknium:monero.social >__ I talked with sowle from Zano about a year ago about that. I'm glad they are following through on it.     

> __< r​ucknium:monero.social >__ Has the discussion about hard fork scheduling moved at all in the last 6 months?     

> __< h​into.janaiyo:matrix.org >__ interesting stuff - i didn't know the uniform decoy selection was inherited from cryptonote, guess it only makes sense     

> __< r​ucknium:monero.social >__ IIRC there were suggestions about including BulletProofs++ once reviewed and audited and some PoW changes.     

> __< r​ucknium:monero.social >__ I think sech1 wanted the PoW changes to be in a release candidate 6 months in advance of a hard fork to give miners a chance to update.     

> __< r​ucknium:monero.social >__ Diego Salazar said CypherStack has started its review of BP++ https://libera.monerologs.net/monero-community/20231226#c316342     

> __< d​iego:cypherstack.com >__ it's true. I said that.     

> __< r​ucknium:monero.social >__ Thanks, Diego     

> __< d​iego:cypherstack.com >__ Found a couple issues that we're in contact with the author about. Awaiting a response. Continuing forward in the meantime.     

> __< r​ucknium:monero.social >__ Thank you for the update 🙏     

> __< r​ucknium:monero.social >__ Anything more to discuss?     

> __< d​iego:cypherstack.com >__ Not at the moment. Holidays so things are a bit off and on as you might expect. It'll chug along at a better speed come early January     

> __< r​ucknium:monero.social >__ Oh. I meant for the meeting in general. I don't mean to rush or expect instant progress :)     

> __< h​into.janaiyo:matrix.org >__ does bp++ necessitate a new type in monero's codebase?     

> __< h​into.janaiyo:matrix.org >__ there's already `RCTTypeBulletproofPlus`, so now we'll have `RCTTypeBulletproofPlusPlus`... lol     

> __< r​ucknium:monero.social >__ I don't know. This is a good point to remind people that Seraphis work and research is happening in #no-wallet-left-behind:monero.social now.     

> __< r​ucknium:monero.social >__ We can end the meeting here.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-12-27T15:01:08+00:00
- Closed at: 2024-01-26T19:51:24+00:00
