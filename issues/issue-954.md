---
title: Monero Research Lab Meeting - Wed 10 January 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/954
author: Rucknium
assignees: []
labels: []
created_at: '2024-01-10T16:14:58+00:00'
updated_at: '2024-01-26T19:51:35+00:00'
type: issue
status: closed
closed_at: '2024-01-26T19:51:35+00:00'
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

#951 

# Discussion History
## plowsof | 2024-01-25T11:43:03+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in 50 minutes     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/954     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< t​obtoht:monero.social >__ hi     

> __< rbrunner >__ Hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< t​obtoht:monero.social >__ I integrated most of the MMS in Feather this week, with the new messaging service and some experimental changes. It's very much a work in progress and a lot more thought needs to go into security and gracefully handling every possible failure mode, but the groundwork is taking shape.     

> __< t​obtoht:monero.social >__ Just finished a first iteration for a wizard that guides users through setting up a new multisig wallet: https://a.uguu.se/zrhtMwpK.mp4     

> __< t​obtoht:monero.social >__ And here is an earlier proof of concept for sending a 2/3 transaction: https://a.uguu.se/eZxZwMxu.mp4     

> __< t​obtoht:monero.social >__ I'll have more details to share in the coming weeks and hope to have a MVP ready soon so I can begin coordinating a testing group. I'm keeping a path towards future integration in the GUI (and other wallet_api wallets) in mind while I work on this.     

> __< r​ucknium:monero.social >__ me: OSPEAD. I added about 20 recent papers to moneroresearch.info . PHCitizen performed the first BCH<>XMR atomic swaps on mainnets: https://monero.observer/phcitizen-executes-first-mainnet-bch-xmr-atomic-swap/ . There is a fundraiser for a BCH<>XMR atomic swap frontend: https://atomic-flip.pat.mn     

> __< rbrunner >__ tobtoht: Looks quite promising already!     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< t​obtoht:monero.social >__ rbrunner: I have to say the MMS is beautifully written and the abundance of clearly written comments make it easy to understand and a joy to read. Can't believe I ever suggested "the nuclear option" in case we didn't find a replacement for PyBitmessage before the next hard-fork.     

> __< rbrunner >__ Thanks. Good to hear.     

> __< rbrunner >__ So it will live on after all :)     

> __< rbrunner >__ Is there interest in the BCH community for those swaps?     

> __< rbrunner >__ I mean, do you see people taking notice of the developments?     

> __< r​ucknium:monero.social >__ Yes     

> __< rbrunner >__ Nice     

> __< r​ucknium:monero.social >__ e.g. https://old.reddit.com/r/btc/comments/190m3nf/first_ever_bchxmr_atomic_swap_on_mainnet/     

> __< r​ucknium:monero.social >__ BCH developers created the swap implementation     

> __< r​ucknium:monero.social >__ The BCH fundraiser for a front-end already has 101 BCH donated: https://atomic-flip.pat.mn  . The fundraiser has been live for 4 days AFAIK     

> __< r​ucknium:monero.social >__ I skimmed some of the papers I added to moneroresearch.info . AFAIK, nothing truly groundbreaking in that set, but I can give short summaries of a few of them if people want to hear.     

> __< rbrunner >__ That's quite some money already then on that fundraiser     

> __< rbrunner >__ Is anything directly about Monero?     

> __< r​ucknium:monero.social >__ In the new moneroresearch.info papers?     

> __< rbrunner >__ Yes     

> __< r​ucknium:monero.social >__ Yes, a few     

> __< rbrunner >__ Just had a look. Interesting what is all going on.     

> __< r​ucknium:monero.social >__ There are a few that are "How can we create a Monero-like system, but allow a central authority info about tx information". A few that are "how can we embed message info in Monero." But a few that are useful:     

> __< r​ucknium:monero.social >__ Vijayakumaran (2023) "Analysis of Cryptonote transaction graphs using the Dulmage-Mendelsohn decomposition" https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=39     

> __< r​ucknium:monero.social >__ This one was released as a draft in 2021. It was presented/published at the Advances in Financial Technologies conference in 2023.     

> __< r​ucknium:monero.social >__ There was not a big change to the results from the draft. The main result was that with RingCT and ring size 11+, chain reaction attacks on Monero are not effective unless you have additional info like users spending on a fork of the Monero blockchain. This could be relevant to Mordinal analysis when "black marbles" reduce the effective ring size.     

> __< r​ucknium:monero.social >__ This new version was posted with MIT licensed code that performs the analysis with this nice documentation: https://www.respectedsir.com/cna/     

> __< r​ucknium:monero.social >__ Wang, Lin, Huang, & He (2023). "Anonymity-enhancing multi-hop locks for Monero-enabled payment channel networks." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=203     

> __< r​ucknium:monero.social >__ This is N + 1 of payment channel network (PCN) on Monero. BTC Lightning is an implementation of PCN. I think there are 3 or 4 of these papers now. This one may have better privacy than other proposals.     

> __< r​ucknium:monero.social >__ Buccafurri, De Angelis, & Lazzaro, (2023) "A traffic-analysis proof solution to allow k-anonymous payments in pseudonymous blockchains." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=199     

> __< r​ucknium:monero.social >__ This is a possible replacement for Dandelion++. But it is only two pages (I think it's just a summary for a conference). And the components seem too complicated.     

> __< rbrunner >__ Is this the output of a few months of papers?     

> __< r​ucknium:monero.social >__ Yes. I didn't update it since August 2023     

> __< r​ucknium:monero.social >__ Scheid, Küng, Franco, & Stiller (2023) "Opening Pandora's box: An analysis of the usage of the data field in blockchains" https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=212     

> __< r​ucknium:monero.social >__ This analyzed Monero and other blockchains for different filetypes embedded in transactions. The data they used stops in 2022 AFAIK. This paper could be useful for Mordinal analysis.     

> __< rbrunner >__ Yeah, only that it seems Mordinals already went the way of the Dodo ...     

> __< r​ucknium:monero.social >__ Dijk & Schröder (2023). "Proof of concept for a Ethereum virtual machine on Cryptonote."     

> __< r​ucknium:monero.social >__ https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=198     

> __< r​ucknium:monero.social >__ Schröder wrote a few papers about Monero. This is a paper for Beldex. I think this PoC is just embed plaintext Ethereum contracts in tx_extra. If anyone asks "how can smart contracts exist on Monero?", they can be sent this.     

> __< r​ucknium:monero.social >__ Movsowitz Davidow, Manevich, & Toch (2023) "Privacy-Preserving Transactions with Verifiable Local Differential Privacy."     

> __< r​ucknium:monero.social >__ https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=194     

> __< r​ucknium:monero.social >__ This maybe could help with keeping file data out of Monero signatures and with requiring a specific decoy selection algorithm. But I think it requires a trusted setup.     

> __< r​ucknium:monero.social >__ Those are the papers that I thought could be useful.     

> __< rbrunner >__ Thanks, fascinating in a way.     

> __< r​ucknium:monero.social >__ If anyone wants to add papers or write your own notes about the papers to put on the papers' webpages, I can create a user for you. Just ask me.     

> __< r​ucknium:monero.social >__ Anything else that we want to discuss?     

> __< rbrunner >__ Not from me.     

> __< r​ucknium:monero.social >__ I saw your question, chaser , but I don't know the answer     

> __< r​ucknium:monero.social >__ "could there be a method of of deriving Jamtis addresses such that once/if EdDSA is swapped for a post-quantum sig algo, the addresses remain the same? I'm very quietly hopeful because this would mean the migration could be undetectable from an end-user perspective"     

> __< c​haserene:matrix.org >__ thanks for the paper summaries, some of these are very exciting, e.g. PCN. I propose putting some in the"Open Research Q's" GH issue     

> __< rbrunner >__ No idea either about that question     

> __< rbrunner >__ I guess "no", but that's just a gut feeling     

> __< r​ucknium:monero.social >__ chaser: Good idea. IIRC already a few of the PCN are there. But I should add this one.     

> __< c​haserene:matrix.org >__ yeah, I hope II hoped kayabanerve or @tevador may be able to answer it     

> __< r​ucknium:monero.social >__ Yes, already there are three payment channel papers in the open research questions list : https://github.com/monero-project/research-lab/issues/94     

> __< c​haserene:matrix.org >__ thanks. while there, could you look at the comments? I've been stacking there papers there that may belong there     

> __< r​ucknium:monero.social >__ Sure. Thanks for that.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2024-01-10T16:14:58+00:00
- Closed at: 2024-01-26T19:51:35+00:00
