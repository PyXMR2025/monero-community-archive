---
title: 'Monero Community Workgroup Meeting: Sep 6th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1264
author: plowsof
assignees: []
labels: []
created_at: '2025-09-05T08:57:47+00:00'
updated_at: '2025-11-05T10:10:00+00:00'
type: issue
status: closed
closed_at: '2025-11-05T10:10:00+00:00'
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
    - https://github.com/monero-project/meta/issues/1263
    - https://github.com/monero-project/monero/issues/10064
    - https://www.getmonero.org/2025/08/26/monero-GUI-0.18.4.2-released.html
    - https://www.getmonero.org/2025/08/26/post-mortem-of-find-and-save-rings-bug.html
    - https://www.getmonero.org/2025/08/27/fcmp++-contest-final.html
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)    
  b. [[hbs] EVM Atomic Swaps](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)    
  c. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)    
  d. [kayabaNerve Finality Layer Book](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604)    
  e. [v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)    
  f. [selsta part-time monero development (3 months) (18)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/609)    
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1257)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2025-11-05T10:09:54+00:00
Logs 
    
    
    
    
> **\<plowsof\>** meeting time https://github.com/monero-project/meta/issues/1264     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Greetings hi     
    
> **\<spackle\>** <spackle> hello     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> Hello     
    
> **\<syntheticbird\>** <syntheticbird> hi     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> comment from binaryFate under Ruckniums "Temporary Rolling DNS checkpoints" issue https://github.com/monero-project/monero/issues/10064#issuecomment-3259592231      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> "if the community decides on a certain course of action, I am happy to help with moneropulse domains admin"      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a tldr from datahoarder reg what these checkpoints will help with https://libera.monerologs.net/monero-research-lounge/20250906#c580466      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> iiuc simply adding a checkpoint for the most recent blockheight in the recent release @ https://github.com/monero-project/monero/pull/10020/files would be proof of shaking the cobwebs off      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Nah thats probably dangerous     
    
> **\<DataHoarder\>** yeah, matching release checkpoints would be a start     
    
> **\<DataHoarder\>** highest height in DNS Checkpoints is 1680000 / 898c0e0b338edc5edd850d241578027f489167cf7b3edb33ed9d08274e15e20e     
    
> **\<DataHoarder\>** that's 2018     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Dont need dns checkpoints for released checkpoints     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> would it be dangerous?      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> for a recent checkpoint, yes, particularly if during a reorg     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> The minority of nodes that use --enforce will get forked off onto a potentially dead chain     
    
> **\<DataHoarder\>** say for height 3088000     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ADD_CHECKPOINT2(3468000, "c4024dbfa9d4b2e54ed129b413946d2d5af36eef5ab4a93abe5cb552de985f5a", "0x6d067f3e550a29b");     
    
> **\<DataHoarder\>** or yeah, 3468000     
    
> **\<DataHoarder\>** Start of August there     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> For the release height, it shouldnt make any difference     
    
> **\<DataHoarder\>** but that's what plowsof means, using a release checkpoint to dust off DNS checkpoint records     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> The checkpoints only need to be enforced by miners, and nice-to-have gor exchanges     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> DataHoarder: Just to test updating them?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> That can be done for testnet     
    
> **\<DataHoarder\>** yeah, dust off, prove we control them     
    
> **\<DataHoarder\>** testnet is a good choice 👍     
    
> **\<DataHoarder\>** I think they share setup at the moment     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> We need to figure out w good way to choose the heights that we checkpoint on mainnet, that cant be gamed too easily     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> can reflect the testnet checkpoint in release @ dns then to show proof of existence      
    
> **\<DataHoarder\>** yeah, making a test engine for that ofrnxmr      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> this is literally step 0 before considering everything else, nice to see happen     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Like, if we push every block 10 9 8 7 6, it might be possible for an attacker to always try to reorg on the 6th block     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @plowsof:matrix.org: assuming we use moneropulse domains at all     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> step 0.1 allow clients to input their chosen DNS servers rather than needing to modify source?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Discussions are leading towards having multiple records run by different ppl (like seed nodes), and requiring 2/3 + 1 of them to agree     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> I think step 0 is figuring out the best recipe for "how to update them properly"     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> what does the +1 mean there btw?      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> from the pool of public nodes?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> 2/3 + 1 means 1 more than 2/3rda     
    
> **\<DataHoarder\>** 2/3rds +1     
    
> **\<DataHoarder\>** of %     
    
> **\<DataHoarder\>** same as 50%+1     
    
> **\<DataHoarder\>** so there is a "majority"      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ah ok     
    
> **\<DataHoarder\>** ofrnxmr: is the point to totally close off selfish mining, or make the 10+ reorgs infeasible     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> to me, its to make 10+ reorgs impossible     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> lesser to punish selfish miners for attempting deep (like 4+) reorgs     
    
> **\<DataHoarder\>** with rolling, say, 2 from tip, and checkpointing every to every couple of blocks there up to 10 rolling checkpoints     
    
> **\<DataHoarder\>** the max they can reorg is the tip-2     
    
> **\<DataHoarder\>** rolling is needed due to DNS, as otherwise, single record will not match across differing servers depending on config (even if they "match" they might not in the client network)     
    
> **\<DataHoarder\>** so with rolling, some of the previous checkpoints will be seen by all     
    
> **\<DataHoarder\>** and pass the "majority" rule that is decided     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> the problem with rollibg ia that some nodes might checkpoint a higher height, and othera rolled back further     
    
> **\<DataHoarder\>** or the checkpointing nodes can be sharing this information with each other     
    
> **\<DataHoarder\>** so when issuing checkpoints, they all have access to the same information     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> anyway, i think step 0 is figuring out how to agree on checkpoints ^ yeah     
    
> **\<DataHoarder\>** I'll keep writing my testbed for this then, has ... highly configurable parameters for testing these     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> the checkpoint nodes can not have public rpc, that goes without saying, easy ddos - but i assume they will be subject to generic ddos attacks should their ip's be known      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> 99% uptime 😬     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> the checkpointing nodes should be private     
    
> **\<DataHoarder\>** yeah. you can issue DNS in secret :)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> No need for them to even be connected to the internet     
    
> **\<DataHoarder\>** they can also take more points of view across other monero nodes     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Selfish checkpointing     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> the hash is delivered via animated QR codes      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Rucknium shared a diagram of a possible setup / flow of data between the secure dns server and pools/clients     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> uhm     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> update to v0.18.4.2 as it fixes a privacy leak when using remote nodes https://www.getmonero.org/2025/08/26/post-mortem-of-find-and-save-rings-bug.html      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://ccs.getmonero.org/funding-required/     
    
> **\<DataHoarder\>** brb     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> lets cover the ccs ideas      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a. MoneroOS Resurrection (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> monero is being attacked, this proposal aims to put a mining operating system into the hands of the masses... simple monero miner, hassle free,,, no need to touch your underlying OS. why isnt this merged?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> opened on 9th July, any one care to comment? else we can move on      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> at least there is a comment from Cyrix126 to respond to, we can move on, it is open for feedback     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> b. [hbs] EVM Atomic Swaps (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/597)     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> I'm available to answer questions if there are any.     
    
> **\<nioc\>** Many questions were answered on the proposal      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> after you clarified some of my confusions in the comments, im stuck at the contract you have re-implemented having no one knowledgeable look over it. this is a very technical proposal and it seems to be going through the community / social momentum route to merge      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> rather than the dev community signing off on this      
    
> **\<yetanotherminer\>** MoneroOS ended up unmainted that first time around. Would the new version stay longer after release?     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> The proposal is for the GUI, should the contract need some modifications this would not impact the GUI as long as the ABI of the contract stays the same, even if details in its implementation change.     
    
> **\<ofrnxmr\>** Matrix issues     
    
> **\<ofrnxmr\>** Probably going to get some late messages from me there re moneroos     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> The GUI is not tied to a specific contract deployment, just to the ABI of the contract     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> yetanotherminer: yes, if you merge the proposal i will maintain it (is this what you want to hear from the proposer?)     
    
> **\<@plowsof:matrix.org\>** <ofrnxmr:xmr.mx> Imo its not a solution to any problems > <@plowsof:matrix.org> monero is being attacked, this proposal aims to put a mining operating system into the hands of the masses... simple monero miner, hassle free,,, no need to touch your underlying OS. why isnt this merged?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Its just a persistent livecd wirh xmrig on it. like cyrix said, the webgui is the biggest part of it. The rest is like 15mins to create     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Having to purchase usb sticks and write isos and configure xmrig, i dont see how this reduces friction. https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596#note_30658     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> (The above msgs probably coming in late. Internet bad)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> so its just a GUI, gui's looks nice, so its going to be merged and funded more than multisig vulnerabilities      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> what a time to be alive      
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> As I've said in the proposal, if there is a community demand for contract audit then such an audit can be funded by another CCS.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> and then later the ccs will fund an audit? have yo uexperience of arranging audits hbs     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> do you have experience of monero-oxide use?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> to increase the automation?     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> I'm not convinced this should be the way to automate the swaps at this point.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ok      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> no reason not to merge this GUI then?      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moving on     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> I'm more thinking that automation will be something market makers will want to have, and once there are enough market makers then swaps will be very quick to complete     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> I think if the goal is ease of use (as comparted to the original) that no-automation isnt going to be very nice     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> @ofrnxmr:xmr.mx: The initial ETH-XMR atomic swaps had automation, but what was in the way of adoption I think was the need to run something specific to do swaps     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> One of the biggest things i hated about basicswap (and still do about haveno) is the interactivity requirment     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> @ofrnxmr:xmr.mx: As swap state is stored onchain there is no need for participants to be online at the same time     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> well bsx didnt require manual interaction, but was the default... so essentially every swap ends up dead because someone forgot to check their computer     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> people look at their phones and use cake wallet so it wont be an issue      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> any further discussions?     
    
> **\<yetanotherminer\>** I support merging the EVM proposal      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> c. Monero Python Maintenance (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i can not for the life of me get monero-cpp to install atm due to my machines ppa's and other issues - i want to make a proof of concept script but the hurdle of instillation is too big. i personally would need a docker      
    
> **\<everoddandeven\>** <everoddandeven> Hello, I'm here if you have any questions     
    
> **\<everoddandeven\>** <everoddandeven> @plowsof:matrix.org: I have included docker build support in the proposal     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://woodser.github.io/monero-cpp/doxygen/classmonero_1_1monero__wallet__full.html is everything stressnete testers need and it should carry over to FCMP++ https://github.com/woodser/monero-cpp/issues/88#issuecomment-3253654177     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> if i can create a dockerised install and show a simple script (or recreate some simple churning script_ i know for a fact that more people will be enthusiastic about this proposal     
    
> **\<freddypa:matrix.org\>** <freddypa:matrix.org> Is monero python up to date or had somebody issues because I want to implement it into my backend?     
    
> **\<everoddandeven\>** <everoddandeven> @plowsof:matrix.org: Sorry, would you like a demonstration of the working build?     
    
> **\<everoddandeven\>** <everoddandeven> https://github.com/everoddandeven/monero-python/blob/main/.github/workflows/build.yml     
    
> **\<everoddandeven\>** <everoddandeven> @everoddandeven: Otherwise I'll try to make the docker file, I think it's quite quick, because these are the instructions to build     
    
> **\<everoddandeven\>** <everoddandeven> @freddypa:matrix.org: Now using v18.4.0, maybe you will find some issues when using rpc clients     
    
> **\<everoddandeven\>** <everoddandeven> Like MoneroDaemonRpc and MoneroWalletRpc     
    
> **\<everoddandeven\>** <everoddandeven> The proposal focuses on code consolidation and test writing     
    
> **\<everoddandeven\>** <everoddandeven> In order to create stable packages     
    
> **\<everoddandeven\>** <everoddandeven> If you've ever played with monero-ts, monero-java, or monero-cpp, this library is the same thing     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> as long as a performance increase vs using monero monero-wallet-rpc can be observed      
    
> **\<everoddandeven\>** <everoddandeven> Exactly, you could avoid launching multiple processes for multiple monero-wallet-rpc     
    
> **\<everoddandeven\>** <everoddandeven> and manage multiple wallets with a single process, using MoneroWalletFull class     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i need people to see that , and believe      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> ofrn needs poc opening 30 subaccoints and sending from all of them at once      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> we can move on, thanks for joining everoddandeven, while we have time left     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> d. kayabaNerve Finality Layer Book (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> whats wrong with a bit of research between friends?      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i think feedback has been exhausted for this proposal?      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> e. v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)     
    
> **\<yetanotherminer\>** I think kayaba‘s proposal could be pushed to a later time. The higher price tag was justified by competing priorities and urgency but given rolling DNS and tevadors PoP proposal, finality layer exploration could happen in the future      
    
> **\<v1docq47\>** yup, i am ready to answer questions     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thank you for the feedback yetanotherminer      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @plowsof:matrix.org: the monerokon videos arent even out yet     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i seen a monerokon tweet and a terrible anti meme saying they would be out soon     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> (are they?)     
    
> **\<v1docq47\>** they come out gradually, just in time for our pace of work     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> http://x.com/MoneroKon/status/1963770737694511121?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet     
    
> **\<v1docq47\>** a new video was released recently     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> The first video has been published, the others will follow at regular intervals. Sorry for the delay     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> there we go https://x.com/MoneroKon/status/1963770737694511121?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> we're gunna get the monero gospel said no one     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> No need to apologize, i just dont see how youre going to do voiceovers for videos that arent available     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> they will be available* :D     
    
> **\<v1docq47\>** 5 videos are already available and more will be released     
    
> **\<v1docq47\>** https://www.youtube.com/playlist?list=PLsSYUeVwrHBlZQl6YKwK_mCBmOxkZv1zn     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> perhaps monerokon could release an audio only version + speaker slides next year , while we wait for video to be reviewed / edited      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for joining v1docq47, any other comments     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://xmr.ru/ he even has the latest release up and translated xD     
    
> **\<v1docq47\>** of course, i follow all the latest news :)     
    
> **\<v1docq47\>** and try to publish news without delay     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> f. selsta part-time monero development (3 months) (18) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/609)     
    
> **\<yetanotherminer\>** no reason not to merge     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> will you be my friend yetanotherminer     
    
> **\<yetanotherminer\>** if you wish to :)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks all for attending x     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Same place and time in 2 weeks?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> yes that would be the 20th september      
    
> **\<yetanotherminer\>** Thanks      
    
> **\<freddypa:matrix.org\>** <freddypa:matrix.org> Noice     
    
> **\<ofrnxmr\>** <ofrnxmr> @monerobull:monero.social  https://x.com/monero/status/1964400250665234879     
    
> **\<ofrnxmr\>** <ofrnxmr> Gui release was finally announced     
    
> **\<plowsof\>** 🚀     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-09-05T08:57:47+00:00
- Closed at: 2025-11-05T10:10:00+00:00
