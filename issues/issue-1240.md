---
title: 'Monero Community Workgroup Meeting: July 26th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1240
author: plowsof
assignees: []
labels: []
created_at: '2025-07-16T09:19:37+00:00'
updated_at: '2025-08-21T17:03:11+00:00'
type: issue
status: closed
closed_at: '2025-08-21T17:03:11+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items: (Note* several proposals await merging and as such will be removed from the agenda)

1. Introduction
2. Greetings
3. Community highlights    
     - [v0.18.4.1 released](https://www.getmonero.org/2025/07/25/monero-0.18.4.1-released.html) 
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589)    
  b. [hinto-janai full-time development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/591)    
  c. [acx Monfluo maintenance and further development 2025Q3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/592)    
  d. [Revuo Monero Maintenance (2025 Q3)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/593)    
  e. [vtnerd 2025 Q3 Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/594)    
  f. ~~[Multisig GUI wizard](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/595) [4bdeef44](https://github.com/monero-project/ccs-proposals/-/merge_requests/595/diffs?commit_id=4bdeef44e2333b59c115d908e50da9efe83b96d0) - Funding reduced to 50XMR~~
  g. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)    
  h. [[hbs] EVM Atomic Swaps](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)    
  i.  [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)   
  j.  [Rucknium Research II](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/599)    

5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://MoneroKon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1233)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2025-08-21T17:03:03+00:00
Logs 
    
    
    
    
    
    
    
    
    
> **\<plowsof:matrix.org\>** Meeting time https://github.com/monero-project/meta/issues/1240     
    
> **\<plowsof:matrix.org\>** greetings     
    
> **\<ofrnxmr:monero.social\>** Greetings     
    
> **\<hbs:matrix.org\>** hello     
    
> **\<rucknium:monero.social\>** Hi     
    
> **\<plowsof:matrix.org\>** [v0.18.4.1 released](https://www.getmonero.org/2025/07/25/monero-0.18.4.1-released.html) please update your clients/nodes and expect a new featherwallet tag shortly 🙏     
    
> **\<michael:monero.social\>** Hello.     
    
> **\<plowsof:matrix.org\>** if interested in the current FCMP++ progress please read the well hydrated 2 hour+ Monero Research Lab meeting https://github.com/monero-project/meta/issues/1244     
    
> **\<plowsof:matrix.org\>** also confirming that the General Fund will be giving 30XMR to the 3rd place submission from rafael in the FCMP++ competition (whicih seemed to be missed from the @monero tweets and caused a bit of confusion)     
    
> **\<plowsof:matrix.org\>** great resource from Rucknium to check on the spy nodes https://moneronet.info/ , which was incuded in his milestone 3 CCS update @ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/439#note_30863     
    
> **\<rucknium:monero.social\>** You can now check if your favorite remote node(s) have enabled the MRL and/or DNS ban list of suspected malicious nodes: https://xmr.ditatompel.com/remote-nodes     
    
> **\<rucknium:monero.social\>** (Uses data collected by my moneronet.info app)     
    
> **\<plowsof:matrix.org\>** Majestic bank shutting down https://monero.observer/majesticbank-instant-exchange-shuts-down/     
    
> **\<plowsof:matrix.org\>** an addition to this could be to show which nodes are proxies (following on from digilols investigation https://www.digilol.net/blog/chainanalysis-malicious-xmr.html)     
    
> **\<plowsof:matrix.org\>** i know im paying a few peoples bills already     
    
> **\<ofrnxmr:monero.social\>** Haha. Every node is plowsof node     
    
> **\<plowsof:matrix.org\>** i suspect proxying a legitimate node will be more appealing now that the Cat has jumped onto the lap or out of the bag / cardboard boax     
    
> **\<plowsof:matrix.org\>** any other highlights? - i assume matrix . org will have updated their servers to the latest versions and pigeons will be looking into how that is going. seems fine here     
    
> **\<rucknium:monero.social\>** On the Qubic mining issue, I am updating this data occasionally. Just updated about 16 hours ago: https://gist.github.com/Rucknium/0873b10b6d36ff6c9d6f8f54107d16f7     
    
> **\<plowsof:matrix.org\>** thank you, reddit mods can auto mod or sticky this, great resource cc syntheticbird monerobull , ok we can move onto the CCS ideas, i'd like to first cover the proposals that didnt seem to require further discussion for merging to funding. i will paste several. if there is a problem you can tell me to srsly stfu.     
    
> **\<plowsof:matrix.org\>** b. [hinto-janai full-time development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/591)         
    
> **\<plowsof:matrix.org\>**   c. [acx Monfluo maintenance and further development 2025Q3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/592)         
    
> **\<plowsof:matrix.org\>**   d. [Revuo Monero Maintenance (2025 Q3)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/593)         
    
> **\<plowsof:matrix.org\>**   e. [vtnerd 2025 Q3 Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/594)     
    
> **\<plowsof:matrix.org\>** now circling back for further discussion updates:     
    
> **\<plowsof:matrix.org\>**   a. [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589)     
    
> **\<plowsof:matrix.org\>** 4 updoots. ai assistance has been confirmed. the work is open source and on-going @ https://github.com/Fountain5405/monerosim     
    
> **\<plowsof:matrix.org\>** hand wave merge it after Ruckniums positive comment. perhaps some transparency about the AI assistance written into the proposal for transparency?     
    
> **\<rucknium:monero.social\>** Yes, I think that makes sense. The funding page won't have the gitlab comments confirming AI assistance.     
    
> **\<monerobull:monero.social\>** I removed like 10 qbic posts today     
    
> **\<monerobull:monero.social\>** m-reIay you don't need to let the sub get filled up with that crap     
    
> **\<plowsof:matrix.org\>** f. ~~[Multisig GUI wizard](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/595) [4bdeef44](https://github.com/monero-project/ccs-proposals/-/merge_requests/595/diffs?commit_id=4bdeef44e2333b59c115d908e50da9efe83b96d0) - Funding reduced to 50XMR~~     
    
> **\<plowsof:matrix.org\>**  (Closed by proposer)     
    
> **\<ofrnxmr:monero.social\>** Imo payments should be contingent on the delivered product being functional / as expected, yeah?     
    
> **\<ofrnxmr:monero.social\>** one major issue with AI is stuff being horribly put together     
    
> **\<rucknium:monero.social\>** And a link to https://github.com/Fountain5405/monerosim in the proposal text     
    
> **\<plowsof:matrix.org\>** the verbose proposal basiclaly says that its new territory so the hours / week are being compensated without an end result     
    
> **\<plowsof:matrix.org\>** but LLM is excited about commits there so apparently progress has been made     
    
> **\<plowsof:matrix.org\>** after monero-sim is created will "Fountain5405" be reviewing merge requests or AI lol , i assume docs will be AI also     
    
> **\<rucknium:monero.social\>** By now, gingeropolous should have an idea of whether this can be changed to a deliverable-based CCS or time-based. Since a lot of work has been done in the monerosim repo.     
    
> **\<plowsof:matrix.org\>** great points and suggestions     
    
> **\<plowsof:matrix.org\>** i think we can move on?     
    
> **\<plowsof:matrix.org\>** g. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)     
    
> **\<plowsof:matrix.org\>** an overwhelmingly positive Reddit thread for this proposal @ https://www.reddit.com/r/Monero/comments/1lzi7g4/moneroos_resurrection/     
    
> **\<plowsof:matrix.org\>** two hundread and forty four whole updoots and everyone excited about it in the comments     
    
> **\<plowsof:matrix.org\>** im sure they are all users of the original https://github.com/4rkal/MoneroOS *tumble weeds*     
    
> **\<plowsof:matrix.org\>** and waiting with baited breath for improvements     
    
> **\<plowsof:matrix.org\>** bated*     
    
> **\<ofrnxmr:monero.social\>** I'm still a nack on that, same reasons stated before. Target audience being one of them     
    
> **\<ofrnxmr:monero.social\>** If youre running a dedi miner, you wouldnt use this. Flashing an iso is not less work than downkoadibf xmrig     
    
> **\<rucknium:monero.social\>** Does this proposal have so much support on Reddit that it could be funded on Kuno?     
    
> **\<plowsof:matrix.org\>** judging by that reddit thread yes, i think it would be funded quite quickly     
    
> **\<plowsof:matrix.org\>** unless they are bots karma farming 🤷     
    
> **\<plowsof:matrix.org\>** moving on     
    
> **\<plowsof:matrix.org\>** h. [[hbs] EVM Atomic Swaps](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)     
    
> **\<hbs:matrix.org\>** Following Rucknium's suggestion made during the first meeting where my proposal was discussed, I've researched funding opportunities within the Ethereum ecosystem.     
    
> **\<hbs:matrix.org\>** Turns out the main funding channel, gitcoin grants, is currently being redesigned and is no longer financing any project.     
    
> **\<hbs:matrix.org\>** Next I researched ESP (Ecosystem Support Program), this program is directly managed by the Ethereum foundation. It explicitely states that it doesn't finance "financial projects".     
    
> **\<ofrnxmr:monero.social\>** Atomic swaps arent financial projects     
    
> **\<hbs:matrix.org\>** As a side note the ESP was also the financing option that was sought after for the MK4 Hackathon. Ultimately the EF rejected the grant stating that their support is "primarly directed towards Ethereum focused events/communities"     
    
> **\<ofrnxmr:monero.social\>** I think that implies stuff like celcius or aave     
    
> **\<hbs:matrix.org\>** I've also looked at financing options with the Gnosis Chain community, but they don't seem to offer financing for projects using Gnosis Chain but for projects building on their other products (GnosisPay, GnosisVPN, ...)     
    
> **\<ofrnxmr:xmr.mx\>** what abt Solana     
    
> **\<hbs:matrix.org\>** Unfortunately they do not provide an explicit definition of what falls under the "financial projects" denomination     
    
> **\<hbs:matrix.org\>** Unrelated to EVM, except for the NeonEVM side project but which doesn't offer a fully compatible EVM layer     
    
> **\<hbs:matrix.org\>** Unrelated to financing, I've created a dedicated Matrix channel for discussing the EVM-XMR Atomic Swap solution I implemented, #moneroswap:matrix.org     
    
> **\<plowsof:matrix.org\>** as we're at the hour with 2 more proposals to cover. any other comments on this for now? monero<>eth integrated into existing projects such as basicswapdex would seem appealing     
    
> **\<ofrnxmr:monero.social\>** Ive reached out to some ppl. will update when i have news     
    
> **\<plowsof:matrix.org\>** lets cover the remaining 2 proposals. moving on. thank you for taking on the feedback hbs     
    
> **\<plowsof:matrix.org\>** i.  [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)     
    
> **\<clipped message\>** bit of back story: the original monero-python is abandonware https://github.com/monero-ecosystem/monero-python , it still had an open PR to add unlock_time to returned json https://github.com/monero-ecosystem/monero-python/pull/127 , when actively maintained it was popular and even made it to v1.0 with a well received announcement on reddit https://www.reddit.com/r/Monero/comments<clipped message>     
    
> **\<plowsof:matrix.org\>** /tjn1zh/were_mature_moneropython_10_has_been_released/     
    
> **\<plowsof:matrix.org\>** this proposal is from everoddandeven     
    
> **\<plowsof:matrix.org\>** the abandonned monero-python was more so a wrapper for monero-wallet-rpc, however did have some of its own crypto functions such as scanning for outputs which belong to a view key +  address (albeit at a slow python speed) and address validation.     
    
> **\<plowsof:matrix.org\>** instead of wrapping monero-wallet-rpc this is utilising monero-cpp which has direct binding to wallet2, is this generalisation correct everoddandeven?     
    
> **\<rucknium:monero.social\>** Can this software have multiple wallets open at the same time?     
    
> **\<everoddandeven:monero.social\>** Yes     
    
> **\<plowsof:matrix.org\>** monero-cpp is used by monero-ts, so its maintenance has been promised for the foreseeable future by woodser     
    
> **\<everoddandeven:monero.social\>** Yes, but it also wraps monero-wallet-rpc     
    
> **\<plowsof:matrix.org\>** my comment on the 2 extra things your have implemented: "MoneroDaemonRpc and MoneroWalletRpc (and relative data model), which are not offered by the monero-cpp library." woodser thinks these could be useful. IMO they should be PR'd to monero-cpp and reviewed for merge.     
    
> **\<rucknium:monero.social\>** everoddandeven: Any info on the RAM footprint of this software and how it scales with number of wallets open?     
    
> **\<everoddandeven:monero.social\>** It has an interface (Monerowallet) implemented by 3 classes: Monowalletfull (Full Wrappers of Wallet2), MonowalletKeys (Keys Management Only) and MonerowaLletpc (RPC Client for Monero-Wallet-RPC)     
    
> **\<rucknium:monero.social\>** `monero-wallet-rpc` can only open one wallet at a time. If you want to open more, you need to have multiple instances of it running. That takes a lot of RAM.     
    
> **\<everoddandeven:monero.social\>** Unfortunately not, for now     
    
> **\<everoddandeven:monero.social\>** But I think it doesn't change much if you compare with monero-cpp as it is all in binding with this library, using pybind11     
    
> **\<rucknium:monero.social\>** I ran into this about four years ago when I was running `townforge-wallet-rpc` on a VPS and could only have one wallet open at a time. It was annoying and seemed to be a strange design decision.     
    
> **\<plowsof:matrix.org\>** https://github.com/woodser/monero-cpp     
    
> **\<rucknium:monero.social\>** I wonder if it could help multi-wallet support for the Monero BTCPay Server plugin. AFAIK, they plan to use LWS for that, but maybe this could be added, too.     
    
> **\<everoddandeven:monero.social\>** So, we go in a wider speech here     
    
> **\<everoddandeven:monero.social\>** (Sorry, I'm using Google Translator)     
    
> **\<plowsof:matrix.org\>** does the xmrapidev final boss named woodser give this monero-python his blessing? that would be ideal     
    
> **\<everoddandeven:monero.social\>** For this I'm developing also https://github.com/everoddandeven/monero-dotnet     
    
> **\<plowsof:matrix.org\>** side note: everoddandeven translated zero to monero into italian recently https://github.com/monero-project/monero-site/pull/2502     
    
> **\<everoddandeven:monero.social\>** That would be another idea I intended to propose: to make a C bridge for Monero-Cpp in order to use it with P/Invoke for this library     
    
> **\<rucknium:monero.social\>** Does your work interact at all with SNeedlewoods 's work?     
    
> **\<rucknium:monero.social\>** https://ccs.getmonero.org/proposals/SNeedlewoods-02_part-time-dev-work.html     
    
> **\<plowsof:matrix.org\>** and example https://github.com/monero-project/monero/pull/9918/files     
    
> **\<everoddandeven:monero.social\>** No, it doesn't seem to me. This work refers to the wallet2_api.h, right?     
    
> **\<rucknium:monero.social\>** I just want to make sure that things are coordinated if they should be coordinated.     
    
> **\<plowsof:matrix.org\>** thanks for the feedback and attending the meeting everoddandeven     
    
> **\<plowsof:matrix.org\>** moving onto the final proposal     
    
> **\<plowsof:matrix.org\>** j.  [Rucknium Research II](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/599)     
    
> **\<rucknium:monero.social\>** I got feedback on research plans at the last Monero Research Lab meeting: https://github.com/monero-project/meta/issues/1244     
    
> **\<rucknium:monero.social\>** Feedback and questions are very welcome here, too.     
    
> **\<plowsof:matrix.org\>** lordxenu left a comment here earlier today     
    
> **\<rucknium:monero.social\>** The main tasks are more work on network-level privacy (i.e. against spy nodes), getting OSPEAD formally peer-reviewed, and researching mining concentration/centralization.     
    
> **\<plowsof:matrix.org\>** the closing update of your previous proposal was outstanding, looking forward to the next     
    
> **\<plowsof:matrix.org\>** what is a life without monerologs ?     
    
> **\<rucknium:monero.social\>** That update is at: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/439#note_30863     
    
> **\<lordx3nu:matrix.org\>** "<l​ordx3nu:matrix.org> Interested in the mining centralization research!"     
    
> **\<plowsof:matrix.org\>** thanks everyone who has attended and read along, an open end to this thread and meeting there 🙏     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-07-16T09:19:37+00:00
- Closed at: 2025-08-21T17:03:11+00:00
