---
title: 'Monero Community Workgroup Meeting: Aug 9th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1251
author: plowsof
assignees: []
labels: []
created_at: '2025-08-09T08:39:16+00:00'
updated_at: '2025-08-21T17:06:28+00:00'
type: issue
status: closed
closed_at: '2025-08-21T17:06:28+00:00'
---

# Original Description

Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
    - https://moneroconsensus.info/ visualization of recent [orphaned blocks](https://monero.stackexchange.com/questions/3311/what-are-orphaned-blocks) and alternative chains of the Monero blockchain. - Rucknium [shares in MRL meeting](https://libera.monerologs.net/monero-research-lab/20250806#c549923)
    - tevador shares bandwidth costs for his proposed anti centralised pool / pro p2pool randomx adjustments @ [comment](https://github.com/monero-project/research-lab/issues/98#issuecomment-3170712102)
    - https://github.com/monero-project/research-lab/issues/136
    - [Selfish mining examined](https://kevinnegy.github.io/Selfish%20Mining%20Re-Examined.pdf)
    - TradeOgre offline for 11+ days, [kycnot.me](https://kycnot.me/service/tradeogre) has placed a 'scam' flair until the situation is resolved (or not)
      News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589)    
  b. [hinto-janai full-time development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/591)    
  c. [acx Monfluo maintenance and further development 2025Q3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/592)    
  d. [Revuo Monero Maintenance (2025 Q3)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/593)    
  e. [vtnerd 2025 Q3 Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/594)    
  f. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)    
  g. [[hbs] EVM Atomic Swaps](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)    
  h. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)    
  i. [Rucknium Research II](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/599)    
  j. [j-berman full-time development (4 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/600)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://moneroKon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards

# Discussion History
## plowsof | 2025-08-21T17:05:14+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof:matrix.org\>** Meeting time 👋     
    
> **\<ofrnxmr\>** 👋     
    
> **\<plowsof:matrix.org\>** for ccs merges : waiting for hinto, vtnerd, acx, rottenwheel  to update rates) will bring up gingeropolous one last time as it had some requested changes     
    
> **\<plowsof:matrix.org\>** tevador has returned https://github.com/monero-project/research-lab/issues/98#issuecomment-3170712102     
    
> **\<vtnerd:monero.social\>** I just updated rates     
    
> **\<plowsof:matrix.org\>** and alot of fresh comments under kayabanerves issue for bolstering PoW to be resistant against 51% attack https://github.com/monero-project/research-lab/issues/136     
    
> **\<plowsof:matrix.org\>** vtnerd again! (thank you)     
    
> **\<plowsof:matrix.org\>** so tevadors proposed solution could see pools increase fee's to 6% as an example     
    
> **\<rucknium:monero.social\>** I created https://moneroconsensus.info/ to visualize orphan blocks and alternative chains, which could indicate "selfing mining" behavior. Covered by press here and elsewhere: https://www.coinspeaker.com/is-monero-at-risk-5-orphan-blocks-spotted-amid-qubic-mining-war/     
    
> **\<rucknium:monero.social\>** Open source code here: https://github.com/Rucknium/xmrconsensus     
    
> **\<rucknium:monero.social\>** You can run it locally on your own machine.     
    
> **\<ofrnxmr\>** rucknium quick to improve if any issues or suggestions found     
    
> **\<plowsof\>** has the deepest recent re-org been 2 blocks? Rucknium suggests it becomes exponentially harder the further you go?     
    
> **\<plowsof:matrix.org\>** he also shared that moneromooo added a re-org notifier along with --tx-notify, thank you     
    
> **\<plowsof:matrix.org\>** i wonders if our payment processors are aware of this     
    
> **\<ofrnxmr\>** It with a minority hashrate. With a majority, i think you just need average luck     
    
> **\<rucknium:monero.social\>** According to my data, yes the deepest re-org recently has been 2 blocks deep. Deeper re-orgs are roughly exponential for each block depth, yes.     
    
> **\<rucknium:monero.social\>** With minority hashpower share, yes     
    
> **\<plowsof:matrix.org\>** ive never looked at the --reorg-notify to be honest https://docs.getmonero.org/interacting/monerod-reference/#accepting-monero     
    
> **\<ofrnxmr\>** i think reorg-notify for merchants isnt necessary unless were getting to 10 block deep reorgs      
    
> **\<rucknium:monero.social\>** If you want exact formulas and exact tables for two different attack strategies with minority hashpower share, I direct you to my comment here:  "Success probability of a double-spend attack with minority hashpower share"  https://github.com/monero-project/research-lab/issues/102#issuecomment-2402750881     
    
> **\<plowsof:matrix.org\>** something to put on the radar of btcpayserver perhaps, napoly / deverickapollo? you have a update to share?     
    
> **\<ofrnxmr\>** while attacker could reorg with confirmed txs -> empty blocks, those txs would still be confirmed by an honest miner      
    
> **\<deverickapollo:matrix.org\>** Ya that's a good idea actually.     
    
> **\<ofrnxmr\>** and would only not be confirmed if 72hrs go by w/o a confirmation     
    
> **\<ofrnxmr\>** (reorgs dont drop the tx from the txpool)     
    
> **\<deverickapollo:matrix.org\>** For our work, we're moving into milestone 2 now. We want request payout for M1 if all concerns have been addressed at this time.     
    
> **\<ofrnxmr\>** Isnt the plugin broken tho lol     
    
> **\<rucknium:monero.social\>** ofrnexmr: Exactly. The answer to that question only gets complicated if the re-org is 10 blocks or deeper. Then it is possible that a tx won't be valid on the other chain because, well, you can read the issue that I linked from the top.     
    
> **\<deverickapollo:matrix.org\>** On existing work, we are addressing a few bugs that have plagued the environment.     
    
> **\<plowsof:matrix.org\>** Jberman has 3 outstanding payouts FYI plowsof     
    
> **\<deverickapollo:matrix.org\>** https://github.com/btcpayserver/dockerfile-deps/pull/119 - I've refactored our original dockerfiles to support upgrades.     
    
> **\<ofrnxmr\>** The refactoe broke it tho, didnt it?     
    
> **\<deverickapollo:matrix.org\>** We never properly handled permissions on mounted volumes so it has been common experience for merchants to fuss with permissions on the host.     
    
> **\<plowsof:matrix.org\>** side note: we need something like  "Support? join support alt coins @ btcpayserver mattermost" at the top of the proposal, i am in there now     
    
> **\<deverickapollo:matrix.org\>** Refactor? It was an upgrade to the OS. We've seen this issue exposed many ways. It was always a bug. The upgrade only exposed it     
    
> **\<plowsof:matrix.org\>** do you know if btcpayserver played any role in coincards recent security event?     
    
> **\<plowsof:matrix.org\>** likely not, as accounts where compromised. just checking     
    
> **\<ofrnxmr\>** the upgrade didnt break because of changinf 18.3.4 -> 18.4.0     
    
> **\<ofrnxmr\>** It broke because of the refactor, afaict     
    
> **\<deverickapollo:matrix.org\>** My understanding is there are no vulnerabilities related to the plugin that caused that incident. I would ask coincards to comment on that further.     
    
> **\<deverickapollo:matrix.org\>** No, permissions were never properly handled for mounted volumes.     
    
> **\<ofrnxmr\>** it worked before the refactor and not after     
    
> **\<ofrnxmr\>** So you mean to say, reverting the refactor would still lead to broken upgrades?     
    
> **\<deverickapollo:matrix.org\>** Note: https://sethforprivacy.com/guides/accepting-monero-via-btcpay-server/#fixing-issues-with-permissions-on-btcpay-server-monero-daemons     
    
> **\<deverickapollo:matrix.org\>** Permissions were never properly handled and vendors have been plagued with this issue in many different ways     
    
> **\<clipped message\>** FWD from #monero-hardware:matrix.org MSvB "Saluton everyone, today Saturday (yesterday as well) 9 August 2025 at 10-18 in the Cryptocurrency areas of DEFCON 33 in Las Vegas USA we are distributing Kastelo enclosures free of charge. They are available in the Las Vegas Convention Center (LVCC) West Hall 4 on the ground level, very easy to find. If you are a Monero community member p<clipped message>     
    
> **\<plowsof:matrix.org\>** lease take one free of charge."     
    
> **\<deverickapollo:matrix.org\>** My PR introduces an entrypoint to ensure those files are accessible by monero user     
    
> **\<deverickapollo:matrix.org\>** From our end, M1 is complete. We are prepared to continue with M2. We plan to remove wallet file functionality and replace with viewkey. This will allow for a more seamless onboarding experience with wallets.     
    
> **\<ofrnxmr\>** Remove the "upload wallet file" functionality, right?     
    
> **\<plowsof:matrix.org\>** https://github.com/btcpay-monero/btcpayserver-monero-plugin/issues/27 discussed here     
    
> **\<deverickapollo:matrix.org\>** That's correct - its the other area of the integration that is poorly designed.     
    
> **\<deverickapollo:matrix.org\>** I wanted to share this as it represents a significant change that customers will see in our first release.     
    
> **\<plowsof:matrix.org\>** its in the payout queue, todo: if broken, fix - if not broken - add to the top of proposal "support available @ alt coin support" pointing to the mattermost instance, i think we can move on to the ccs ideas     
    
> **\<ofrnxmr\>** wait     
    
> **\<ofrnxmr\>** fcmp++ news: jberman moved fcmp work to be based on the latest monero master     
    
> **\<ofrnxmr\>** In my uneducated look, it seems that sync times are similar (byte-for-byte) with ringct     
    
> **\<ofrnxmr\>** Stressnet is likely around the corner     
    
> **\<plowsof:matrix.org\>** jbermans latest CCS update https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/574#note_31061     
    
> **\<plowsof:matrix.org\>** spackle: senior stressnetter and ack-j     
    
> **\<plowsof:matrix.org\>** nice     
    
> **\<plowsof:matrix.org\>** a. [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589)     
    
> **\<plowsof:matrix.org\>** has been simplified to cover only the creation of monero sim tool assisted by our new intern Large Larry Montgomery     
    
> **\<plowsof:matrix.org\>** LLM-AI for short     
    
> **\<ofrnxmr\>** I'm on the party of retroactive. A bunch of hallucinations etc      
    
> **\<plowsof:matrix.org\>** the repo is now also linked in the proposal https://github.com/Fountain5405/monerosim/commits/main/     
    
> **\<ofrnxmr\>** If completed successfully, i'm pro-merge. But based on the 98.7% LLM work that is filled with hopes and fantasies, i can't bring my self to vote yes     
    
> **\<rucknium:monero.social\>** > Milestones - I have edited this CCS to be just a single deliverable based milestone. I will request payout once I can run a simulated monero network with 1000 nodes, provide setup scripts and documentation.     
    
> **\<ofrnxmr\>** To vote yes before its completed*     
    
> **\<plowsof:matrix.org\>** it went through a major python re-write https://github.com/Fountain5405/monerosim/commit/82b15a3a575683d719a2cafc4f1323ec9c8293f6     
    
> **\<rucknium:monero.social\>** I suppose if gingeropolous isn't successful with running 1000 nodes, this basically turns into a bounty. That's the way that CCS is supposed to work.     
    
> **\<ofrnxmr\>** and llm did 100% of the rewrite too, even left its notes in there      
    
> **\<ofrnxmr\>** Yeah, if he's not successful it becomes a jetfund     
    
> **\<ofrnxmr\>** maybe this _should_ be a bounty     
    
> **\<plowsof:matrix.org\>** we need someone to review that its running 1000 nodes and not just echo;ing things :P     
    
> **\<plowsof:matrix.org\>** but sounds good to me     
    
> **\<ofrnxmr\>** Need someone willing to run the 1million lines (literally) of LLM slop     
    
> **\<rucknium:monero.social\>** This thing will probably be run on one of MRL's research machines, for verification and production operation.     
    
> **\<ofrnxmr\>** Its already rin on the MRL machines 😆     
    
> **\<rucknium:monero.social\>** The machines are administered by gingeropolous himself, so I assume he would be willing to have his machines run it :)     
    
> **\<rucknium:monero.social\>** Right     
    
> **\<rucknium:monero.social\>** But it should be verifiable by anyone, too. Do it in a VM if you are scared     
    
> **\<plowsof:matrix.org\>** side note: how many hours of run time per year has the MRL used the machine, and is that possible to quantify (i have no idea) gingeropolous     
    
> **\<plowsof:matrix.org\>** i thinks we can move on, no need to discuss gingers proposal again, merge after rate change?     
    
> **\<plowsof:matrix.org\>** moving on     
    
> **\<plowsof:matrix.org\>** f. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)     
    
> **\<rucknium:monero.social\>** I think it's a good idea to merge, given that it is a deliverable-based milestone and it would be great to have _someone_ write this well-defined software. I am not excited about the AI assistance, but you don't always get what's ideal.     
    
> **\<rucknium:monero.social\>** By "well-defined" I mean the requirements are well-defined: Make `shadow` work with `monerod`.     
    
> **\<plowsof:matrix.org\>** reg MoneroOS the proposal remains open for feedback     
    
> **\<ofrnxmr\>** Ruck, i'd implore you to take a look at the code that has been churned out. LLM seems to make a lot of incorrect assumptions, as well as yolo commiting a lot of nonsense     
    
> **\<ofrnxmr\>** I'm not confident that it will result in a viable solution, especially not one that can be run outside of the environment. At least not with the repo that is available (with 1 million lines of drunken llm commiting environment specific stuff)     
    
> **\<rucknium:monero.social\>** Could you point to a specific file or dir for me to look in? There are one million lines of code, after all.     
    
> **\<ofrnxmr\>** i'm not against raising funds for it, but i feel like this is bounty territory     
    
> **\<ofrnxmr\>** https://github.com/Fountain5405/monerosim/commit/82b15a3a575683d719a2cafc4f1323ec9c8293f6     
    
> **\<rucknium:monero.social\>** I remember when this was a Shell/Rust repo: https://github.com/Rucknium/monerosim     
    
> **\<ofrnxmr\>** This is a single commit. But after meeting (or during, let me get distracted for a few mins), i can pull up some of LLM's incorrect assumptions       
    
> **\<rucknium:monero.social\>** Ok thanks.     
    
> **\<rucknium:monero.social\>** Sorry to overrun the other agenda items.     
    
> **\<ofrnxmr\>** Np. (jk. Sorry too)     
    
> **\<plowsof:matrix.org\>** g. [[hbs] EVM Atomic Swaps](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)     
    
> **\<ofrnxmr\>** i think ravfx might have comment on moneroos     
    
> **\<n1oc\>** [CCS Proposals] Lee Clagett opened merge request #601: Mark vtnerd-2025-q1 as completed. https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/601     
    
> **\<plowsof:matrix.org\>** h. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)     
    
> **\<plowsof:matrix.org\>** everoddandeven is currently busy with integrating i2p into the gui https://github.com/monero-project/monero-gui/pull/4444/files     
    
> **\<plowsof:matrix.org\>** and this monero python should help vthor and Monero Signer on the pi - allegedly     
    
> **\<vthor\>** greatings! reading in 7 minutes     
    
> **\<plowsof:matrix.org\>** no more monero-wallet-rpc , using python->monero-cpp bindings->wallet2     
    
> **\<plowsof:matrix.org\>** thanks vthor, your opinion on this would be great     
    
> **\<ofrnxmr\>** I think everodd said it still uaes wallet-rpc     
    
> **\<plowsof:matrix.org\>** sorry yes, it has the option(al) to use wallet-rpc     
    
> **\<plowsof:matrix.org\>** but still everything the wallet2 api offers (everything monero-cpp offers)     
    
> **\<rucknium:monero.social\>** I wonder of this could be useful for stressnet spamming. Or worth a try, at least.     
    
> **\<plowsof:matrix.org\>** and some extra things that should be PR'd upstream to monero-cpp and reviewed 😬     
    
> **\<rucknium:monero.social\>** I wonder if this...*     
    
> **\<ofrnxmr\>** i think wallet-rpc or prepating outpurs ahead of time is the most useful      
    
> **\<plowsof:matrix.org\>** the tldr is to just think of it as python being able to use https://github.com/woodser/monero-cpp     
    
> **\<ofrnxmr\>** or rather, works as well as possible. Issue i'm having today seems to be that the output selected has changed. Somehow, most of my txmr has consolidated into single inputs      
    
> **\<plowsof:matrix.org\>** more food for thought everoddandeven, while we reach the hour we can share Rucks prior to merge as he is present , maybe some has questions     
    
> **\<plowsof:matrix.org\>** and vthor can hopefully catch up shortly     
    
> **\<ofrnxmr\>** +1 ruck, berman, vtnerd      
    
> **\<plowsof:matrix.org\>** i. [Rucknium Research II](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/599)     
    
> **\<plowsof:matrix.org\>** j. [j-berman full-time development (4 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/600)     
    
> **\<vthor\>** so, i'm here     
    
> **\<rucknium:monero.social\>** Yes I can take questions and comments about my proposal live here.     
    
> **\<plowsof:matrix.org\>** perhaps this can spring board DataHoarder into creating his ccs proposal finally     
    
> **\<ravfx:xmr.mx\>** MoneroOs. Sorry for delay, just woke up.     
    
> **\<ravfx:xmr.mx\>** PXE boot capability should be a requirement for it to be more useful for me. (and probably other miners with many machine... )     
    
> **\<clipped message\>** Once Monero OS is booted, have a small script that allow creating PXE capabilities, that also print the required settings that need to be stuffed into the DHCP server. That way you could have one booted monero os on one of the machine then you can boot the 15 others thinkcentres from the network with a minimal image just for mining, no need to have the whole blockchain on more tha<clipped message>     
    
> **\<ravfx:xmr.mx\>** n one machine anyway.     
    
> **\<ravfx:xmr.mx\>** That's how I would use it personally, I don't know if that's possible considering there is already one milestone done.     
    
> **\<rucknium:monero.social\>** Yes DataHoarder helped me a lot with pool data collection for https://moneroconsensus.info/ . His code for the data gathering script is here: https://git.gammaspectra.live/WeebDataHoarder/monero-blocks     
    
> **\<vthor\>** So, it will probably not really help me, I have already the python wrapper for the OTS(offline transaction signing) library (C++/C-ABI), my biggest challenge ahead is to get the RandomX part compiled for armv6 (not right sure if it was v6 or v7, need to check).     
    
> **\<plowsof\>** ravfx is arch linux known for the odd bugs here and there? would miners care to deal with that? what about ansible giving updates / stats?     
    
> **\<plowsof\>** vthor thanks for checking - if there was a time machine, it would have helped you?     
    
> **\<vthor\>** but for https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598 +1, this is what I in reality expected python-monero to do when I started with the XmrMiner, and of the SDK (modularized) I dream of is probably still lightyears away     
    
> **\<plowsof\>** python implementation of Polyseed which you created many moons ago, will not be required once polyseed is added into monero core  - accessible via python->monero-cpp      
    
> **\<vthor\>** yes, think so, probably I would still have to fight with compliling for the armv? (now I will look it up)6     
    
> **\<plowsof:matrix.org\>** i assume if monero-cpp compiles for armv woodser it wouldnt be a problem? i dont know     
    
> **\<vthor\>** nope, but in OTS I added already Poolyseed, maybe worth a look before reimplementing     
    
> **\<clipped message\>** All distributions have they own possible quirks and/or issues. Assuming the maintainers can maintains the relevent monero stuff it should be OK. Personally I am fine with Arch. Alpine would be better considering it look like it's a "server" distribution (smaller footprint, more reliable updates in the long term but agains if it's only monero stuff and not used for a desktop usecas<clipped message>     
    
> **\<ravfx:xmr.mx\>** e then it should be OK with arch)     
    
> **\<woodser:monero.social\>** it should be able to compile to whatever wallet2 can compile to afaik     
    
> **\<plowsof:matrix.org\>** can end the meeting here i thinks, thanks all for attending 🙏     
    
> **\<ofrnxmr\>** @rucknium https://github.com/Fountain5405/monerosim/blob/main/SHADOW_OPTIMIZATIONS.md for example     
    
> **\<plowsof:matrix.org\>** LLM NO... this is a tool for stress testing. DO NOT OPTIMISE things.     
    
> **\<plowsof:matrix.org\>** You're absolutely right     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2025-08-21T17:06:06+00:00
continued:
```
17:25:53 <ofrnxmr> Monero isnt 8out 64in by default. Log level 4 is absolutely brutal / not an optimization at all. P2p-use-ipv6=false is default, but this sets the flag to disable ipv6
17:54:44 <m-relay> <g​ingeropolous:monero.social> log level 4 helped the bots debug some shit. it was wild watching it match timings between logs.
17:55:06 <m-relay> <g​ingeropolous:monero.social> my apologies for using git as a means to track changes and not whatever you imagine it to be
17:58:40 <m-relay> <g​ingeropolous:monero.social> and the repo is by no means production ready or collaboration ready obvi. i shared it because it was requested. last time i do that
18:01:03 <ofrnxmr> No need to play the victim card when youre letting LLM commit the entire working directory¸ including multiple venvs and million of lines of "code"
18:02:21 <ofrnxmr> and again, i'm not against funding the deliverable, but the repo shoes that this is a lot of  "jesus take the wheel"
18:07:33 <m-relay> <g​ingeropolous:monero.social> yeah i shoulda stuck to bash. stupid python
18:08:34 <m-relay> <g​ingeropolous:monero.social> at some point ima get that venv crap cleaned up. its just not important to me at this phase
18:12:34 <ofrnxmr> Personally, id never let an llm make commits on my behalf
18:20:12 <ofrnxmr> ofrnLLM https://github.com/Fountain5405/monerosim/pull/1
18:20:54 <ofrnxmr> this might delete your local venv (which youll have to recreate), YMMV
18:23:41 <ofrnxmr> alternative: instead of having these massive commits in the history, i'd probably go back and modify the commit history and fix the commits that added in the first place
18:25:48 <m-relay> <g​ingeropolous:monero.social> when it gets to a clean working state im going to post it up fresh somehow
```

# Action History
- Created by: plowsof | 2025-08-09T08:39:16+00:00
- Closed at: 2025-08-21T17:06:28+00:00
