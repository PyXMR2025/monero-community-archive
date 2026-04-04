---
title: Monero Research Lab Meeting - Wed 03 January 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/951
author: Rucknium
assignees: []
labels: []
created_at: '2024-01-03T15:16:15+00:00'
updated_at: '2024-01-26T19:51:14+00:00'
type: issue
status: closed
closed_at: '2024-01-26T19:51:14+00:00'
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

#949 

# Discussion History
## plowsof | 2024-01-25T11:35:30+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this channel in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/951     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< weechat2 >__ hi     

> __< g​hostway:matrix.org >__ Hello     

> __< c​ompdec:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ w​eechat2: Your handle is w​eechat2 now     

> __< weechat2 >__ ah crap this again     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ Me: OSPEAD. Also encouraging BCH<>XMR atomic swaps. A BCH developer ("pat") is working on it and BasicSwapDEX says it is planned in 2024. The bounty for BCH<>XMR atomic swaps is now up to 15 XMR and about 3 BCH.     

> __< vtnerd >__ me: I'm back on "chain hardening", temporarily given up on figuring out why the tx scanning test would fail randomly     

> __< r​ucknium:monero.social >__ https://bounties.monero.social/posts/37/15-001m-bch-xmr-atomic-swaps     

> __< g​hostway:matrix.org >__ Didn't someone already write everything?     

> __< r​ucknium:monero.social >__ bitcoincashautist wrote a proposed implementation, but no one has done it on the mainnets, and a barebones atomic swaps doesn't mean you have the other market infrastructure like peer finding, etc     

> __< r​ucknium:monero.social >__ bitcoincashautist doesn't want to claim the bounty. I think pat is trying to make a usable implementation.     

> __< g​hostway:matrix.org >__ Ah, I see. Anything to do xmr-side? Sounds like an interesting task     

> __< r​ucknium:monero.social >__ We need an independent party who can verify the atomicity of the swap if it happens. To release the bounty.     

> __< r​ucknium:monero.social >__ kayabaNerve performed that role for ETH<>XMR atomic swaps, but he said he won't for bitcoincashautist's proposed implementation.     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< c​ompdec:matrix.org >__ I've got some time to work further on my topological data analysis-analysis again for a bit.  After next week my Wednesday's are free to attend MRL meetings too.  Nothing new yet, Hope to have updates soon.  Working on some visualizations and designing experiments to scale the analysis.  In particular exploring EAE with a (hypothetical) large number of labels.     

> __< r​ucknium:monero.social >__ Thanks for the update, compdec     

> __< k​ayabanerve:matrix.org >__ I don't want to certify the BCH protocol is correct, nor that any implementation is correct. I'd be happy to confirm an impl appears to be doing an adaptor signature swap with the expected cryptography.     

> __< r​ucknium:monero.social >__ On December 19, 2023, the on-chain tx volume doubled, stayed high for a few days, and is now back to its prior level: https://bitinfocharts.com/comparison/monero-transactions.html#3m     

> __< r​ucknium:monero.social >__ I don't have any good hypotheses about the tx volume spike.     

> __< r​ucknium:monero.social >__ Ok we can make this a light meeting if there are no other discussion items.     

> __< r​ucknium:monero.social >__ Meeting end :)     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2024-01-03T15:16:15+00:00
- Closed at: 2024-01-26T19:51:14+00:00
