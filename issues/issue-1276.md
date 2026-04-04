---
title: 'Monero Community Workgroup Meeting: Oct 4th 16:00 UTC AND Oct 11th'
source_url: https://github.com/monero-project/meta/issues/1276
author: plowsof
assignees: []
labels: []
created_at: '2025-10-04T11:43:02+00:00'
updated_at: '2025-11-05T10:18:11+00:00'
type: issue
status: closed
closed_at: '2025-11-05T10:18:11+00:00'
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
    - jeffro256 CCS update + stressnet progress https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/602#note_32245
    - https://github.com/Rucknium/xmrspammer
    - https://github.com/seraphis-migration/monero/releases
    - monerod / wallet cli binaries can be downloaded directly from the above release page. if you wish to compile these yourself (or the monero GUI) jeffro256 provides a [convenience python script](https://gist.github.com/jeffro256/543932a8b9de3a42ce474e7aa9184c86)  
    - https://ccs.getmonero.org/proposals/kayabaNerve-finality-layer-book.html Funded!
    - https://github.com/monero-project/research-lab/issues
    - https://github.com/monero-project/meta/issues/1275
    - everoddandeven adds adds fcmp compatibility to monero-python @ https://github.com/everoddandeven/monero-python/releases 
    - DataHoarder makes their [GO-p2pool](https://git.gammaspectra.live/P2Pool/go-p2pool/src/branch/fcmp) implementation compatible with fcmp stressnet 
    - onion explorer for fcmp++ in progress https://github.com/moneroexamples/onion-monero-blockchain-explorer/issues/335#issuecomment-3367986641 
News: [Monero Observer](https://www.monero.observer/) - [This week in Monero](https://cyphergoat.com/blog) - [Revuo Monero](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)    
  b. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)    
  c. [v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)    
  d. [Revuo Monero Maintenance (2025 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/610)    
  e. [Boog900 full time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/611)    
  g. [acx part-time work on Monfluo 2025Q4](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/616)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 202?](https://monerokon.org/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2025-11-05T10:16:59+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> fcmp++ stressnet has launched : https://github.com/seraphis-migration/monero/releases     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> if you want to get involved, you can simply download the cli binaries (monero wallet and monerod), run monerod in --testnet mode, mine some coins, and send / receive .. and report issues in the stressnet room or on the seraphis migration repository     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> or join the #monero-stressnet:monero.social  room (##monero-stressnet on libera)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> if you wish to compile these yourself (or the monero GUI) jeffro256 provides a convenience python script (https://gist.github.com/jeffro256/543932a8b9de3a42ce474e7aa9184c86)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> There are explorers & monitors up     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a faucet from kico also @ https://faucet.xmr.pt/ (perhaps down atm as they encountered and reported a bug that crashes their wallet - rpc)      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ofrnxmr had an onion explorer instance up and founds some bugs there which will help moneroexamples progress its fcmp++ support (tracking issue at  https://github.com/moneroexamples/onion-monero-blockchain-explorer/issues/335#issuecomment-3367986641      
    
> **\<DataHoarder\>** Once I start p2pool mining again I'll do custom changes so it mines to a random testnet wallet continuously and gives may outputs. I'll post in the stress net channel for people to submit their address (or I'll just fill in random ones) so it may act as a faucet as well     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Rucknium has released his spammer script too, others also?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Ruckniums spammer @ https://github.com/Rucknium/xmrspammer     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> DataHoarder: DataHoarder makes their GO-p2pool (https://git.gammaspectra.live/P2Pool/go-p2pool/src/branch/fcmp) implementation compatible with fcmp stressnet     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Untraceable has joined the stressnet and outreach effort on twitter 🫡     
    
> **\<DataHoarder\>** ^ note this is an interim proof of concept and many things will change (as will in carrot/FCMP) so for now I'm doing a local p2pool. This allows mining via xmrig, but I'd recommend to wait until next changes (I'll say that in stressnet chan as well)     
    
> **\<@plowsof:matrix.org\>** <everoddandeven> unfortunately I was not able to prepare the script, I have to fix some bugs in the library regarding the rpc, but I think I will publish the repository tomorrow > <@plowsof:matrix.org> Rucknium has released his spammer script too, others also?     
    
> **\<rucknium\>** <rucknium> Monitors and explorers: https://stressnetnode1.moneronet.info/ https://stressnetnode2.moneronet.info/ http://stressgguj7ugyxtqe7czeoelobeb3cnyhltooueuae2t3avd5ynepid.onion/     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i propose a meeting next Saturday also to cover any further stressnet findings everoddandeven, more time to display your monero-python in use on stressnet which you added compatibility for  @ https://github.com/everoddandeven/monero-python/releases      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> as for mainnet .. it seems the re-orgs have allmost vanished https://blocks.p2pool.observer/     
    
> **\<DataHoarder\>** Qubic stopped selfish mining about two weeks ago     
    
> **\<DataHoarder\>** They say they forgot, or don't have hashrate, or don't bother turning it on, or "wait why are we talking about Monero again" on their discord      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> lol     
    
> **\<@plowsof:matrix.org\>** <ofrnxmr:xmr.mx> Ofrnspammer comibf soonTM > <@plowsof:matrix.org> Ruckniums spammer @ https://github.com/Rucknium/xmrspammer     
    
> **\<DataHoarder\>** They seem to command from 1.2 to 1.8GH/s still but they are not always mining, as usual     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> more time for kayabanerves book which was funded  https://ccs.getmonero.org/proposals/kayabaNerve-finality-layer-book.html , and for MRL to browse all of the colorful proposals community members have put forward at  https://github.com/monero-project/research-lab/issues , and, ofc, checkpointing bandaid      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thank you all for joining btw much appreciated      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> anything else to highlight? News: Monero Observer (https://www.monero.observer/) - This week in Monero (https://cyphergoat.com/blog) - Revuo Monero (https://revuo-xmr.com/)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Dont mine on stressnet with 110kh     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> 1 core max plz     
    
> **\<DataHoarder\>** Did you post Rucknium's reorg explainer?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ah sorry      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for reminder : https://rucknium.me/posts/monero-18-block-reorg/      
    
> **\<DataHoarder\>** I will mine with 80KH/s ofrnxmr (for one block then I debug for an hour in breakpoint hell :')     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Someone mined hundreds of blocks at like 30x the testnet hr     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Block every 5sec     
    
> **\<DataHoarder\>** Don't tell me their blocks have a merge mine tag in coinbase tx extra     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> "thata 20x" lemme exaggerate; willya     
    
> **\<DataHoarder\>** When I checked testnet was 3-5 kH/s a few hours ago, 20x sounds about right      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> hopefully merge mining townforge tesnet coins     
    
> **\<DataHoarder\>** Nah p2pool will do that     
    
> **\<DataHoarder\>** It is merge mining after all     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> nice :D      
    
> **\<sgp_\>** <sgp_> I might bring back Monero Coffee Chats. I think they're a very important missing community event. I intend to focus primarily on the technical developments and less on general news     
    
> **\<DataHoarder\>** And the only thing that can do p2pool stuff is my go-p2pool so hopefully no one just went mad and threw their miners there     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> nice sgp_ , iirc @anhdres:matrix.org began a similar initiative .. monero nero?     
    
> **\<sgp_\>** <sgp_> Cool I'll check with them and make sure I'm not stepping on their toes :)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> anhdres was also around for the stressnet      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> lets jump to the ccs ideas, it seems we'll only have 5 mins per item to share any feedback should there be any      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> another meeting next week mind     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a. MoneroOS Resurrection (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)     
    
> **\<4rkal\>** <4rkal> Here to answer any questions     
    
> **\<4rkal\>** <4rkal> Although don’t think there are too many     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for joining none the less 4rkal, and your new cyphergoat insured trades looks interesting      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://www.reddit.com/r/Monero/comments/1nxu6j6/cyphergoat_shield_program_trade_with_a_piece_of/      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> b. Monero Python Maintenance (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)     
    
> **\<everoddandeven\>** <everoddandeven> I'm here if you have any questions     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i dropped an updoot today as everoddandeven is doing all the right things, especially after the docker build (working) and now attempting to create a fcmp stressnet compatible transfer / spam script      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> hopefully something ready for next Saturday?      
    
> **\<@plowsof:matrix.org\>** <4rkal> Thanks! > <@plowsof:matrix.org> thanks for joining none the less 4rkal, and your new cyphergoat insured trades looks interesting      
    
> **\<everoddandeven\>** <everoddandeven> @plowsof:matrix.org: Yes, maybe even before     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i feel if monero-python can perform the same actions as munltiple instances of wallet-rpc using less resources that would gain much more interest and support      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> multiple*     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> c. v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)     
    
> **\<everoddandeven\>** <everoddandeven> @plowsof:matrix.org: Yes, there will definitely be this demonstration in the script     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> d. Revuo Monero Maintenance (2025 Q4) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/610)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> e. Boog900 full time work on Cuprate (3 months) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/611)     
    
> **\<syntheticbird\>** <syntheticbird> merge or i die     
    
> **\<syntheticbird\>** <syntheticbird> blink blink blink long blink long blink long blink blink blink blink     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> f. Memoro Vault Bounty Challenge (36 XMR Security Demonstration) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/615)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> close     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> close from me also, the whole thing seems unnecessary       
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> it started off as a dev-funded bounty to crack the safe     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Then quockly turned to "if you dont crack the safe in N months, i get my funds back"     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> To "send funds to this address to increase the bounty. If uncracked, i keep the funds"     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> To "lets get ccs to send funds to the vault, so i can keep them when nobody tries to crack it"     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ive seen first had someone remember 16 words .. or written on a piece of paper as a backup 🤷      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> g. acx part-time work on Monfluo 2025Q4 (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/616)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Latest release had big ui overhaul     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks all for joining, the above proposals are open for further feedback. also haveno.com now points to haveno.exchange and moneronews.net is offline. kewbit are you out there?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> we can meet again next saturday oct 11th     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> there is a call for presentations open, for 39C3  https://cfp.cccv.de/39c3/cfp     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> cc Rucknium / MRL members^ a contributor shared this with me and stated Even if you get rejected by the general CfP, there is second CfP for the decentralization cluster later, so you get a good second chance without additional work.     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2025-11-05T10:18:03+00:00
Logs 
    
    
    
    
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Meeting time https://github.com/monero-project/meta/issues/1276     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> greetings     
    
> **\<rucknium\>** <rucknium> Hi     
    
> **\<4rkal\>** <4rkal> Hello hello     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Hay     
    
> **\<everoddandeven\>** <everoddandeven> Hello     
    
> **\<r4v3r23\>** <r4v3r23> yo     
    
> **\<tisktisk:xmr.mx\>** <tisktisk:xmr.mx> Aloha     
    
> **\<syntheticbird\>** <syntheticbird> hello     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> jeffro256's latest CCS update that touches on stressnet alpha progress jeffro256 CCS update + stressnet progress https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/602#note_32245     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org>       
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Ruckniums spammer has received some updates since last meeting https://github.com/Rucknium/xmrspammer      
    
> **\<rucknium\>** <rucknium> AFAIK, at least two other people are using it on stressnet. Most bugs have been eliminated.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> everoddandevens monero-spammer was released also - he is fixing some issues with the monero-python .deb file for ubuntu so i can begin testing it https://github.com/everoddandeven/monero-spammer      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> you didnt think starting 10 monero-wallet-rpc's was useful but you ended up finding a bug 😅     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> My spammer remains to be vaporware     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> hello     
    
> **\<rucknium\>** <rucknium> @ofrnxmr:xmr.mx: Harder to write something usable on another person's machine.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Due to the the way my spammer works, it stopped working for a while     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> #monero-stressnet:monero.social for those who wish to follow goings on     
    
> **\<r4v3r23\>** <r4v3r23> ANONERO milestone 3 is complete and users are reporting very positive feedback     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> I did make a lot of improvements to it, for it to be usable by others. But major issue atm is the funding step. I currently run 2 variations of the script. One of them funds the spammer, the other does the spamming. I reuse wallets (so they have a large history). This lead to finding some big performance gains     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> #moneroswap:matrix.org hbs is offering to walk people through his evm atomic swaps     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> The next release of stressnet should have lightning fast refresh and wallet opening when there is a large txpool and a karge wallet     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Possibly fixes some issues noted by exchanges over the years     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> and has been discussing https://github.com/hbs/MoneroMisc/blob/master/CARROT-discussion.md      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> @spackle_xmr:matrix.org: ran a blockchain sync on an ssd vs hdd for FCMP++ from/to a set height on stressnet, and they had similar enough sync times     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> @rbrunner7:monero.social highlighted that although FCMP++ is easier on drives (without looking up decoys) , nodes will still have to sync the "old" chain     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Currently, syncing from scratch on mainnet is faster than migrating 😬     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> (like 16hrs vs 26)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> also i did a torrent, DataHoarder introduced me to webseeds https://github.com/plowsof/monero-torrent/releases/tag/v0.18.4.3     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> uhhh new monero version      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://www.getmonero.org/2025/10/08/monero-0.18.4.3-released.html     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> borked api @ https://miningpoolstats.stream/monero pls use https://blocks.p2pool.observer/ for an accurate view     
    
> **\<rucknium\>** <rucknium> New release has stronger resistance to p2p spying, thanks to @rbrunner7:monero.social for writing the code, @boog900:monero.social for discovering the spy nodes,  and @jeffro256:monero.social  and @vtnerd:monero.social for reviewing the code : https://github.com/monero-project/monero/pull/9939     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> On subject of community feedback .. (this is for -site but figure i should post here while people are present).     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> do we prefer monero.com or cake wallet to be listed on getmonero?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> list..[... more lines follow, see https://mrelay.p2pool.observer/e/8cnD7L0KbGR2QVJn ]     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Rucknium could you share you asmap web page again?      
    
> **\<rucknium\>** <rucknium> For everything you wanted to know about the new simple anti-spy technique and probably also some things you didn't want to know, you can read my research note: https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @ofrnxmr:xmr.mx: https://github.com/monero-project/monero-site/pull/2541 should be noted that cake wants 1 or 3     
    
> **\<rucknium\>** <rucknium> @plowsof:matrix.org: @plowsof:matrix.org: http://moneronet.info/     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> currently on site "monero .com" is displayed - but the hyperlink takes you to calewallet so thats like 2 SEO's for the price of 1 :P     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Thanks     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> the original issue on site with monero dot com and cake wallet was that any multi wallet can create a monero only, monero + btc, etc etc version and drown the others out if you get me which would be rejection of 0 , at least back then when it was originally brought up     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> of 1*     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://www.getmonero.org/downloads/ for reference      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> under Mobile & light wallets      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> to me, it makes more sense to list the monero wallet whenever possible, especially since the monero wallet was created at our request     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> like, firo lists campfire, not stack wallet. They are the same codebase, but campfire ks firo-only     
    
> **\<ravfx:xmr.mx\>** <ravfx:xmr.mx> [2]     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> the firo is a direct comparison      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> currently its "show monero .com" -> "link to cakewallet .com"     
    
> **\<ravfx:xmr.mx\>** <ravfx:xmr.mx> Actually, we have Stack Wallet in the list too, that is also a multi coin wallet, in that case [3] is also fine     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Stack doesnt make a monero only wallet, cuz theyre assholes cc @diego:cypherstack.com     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Firo and epic get their own wallets :(      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> After the Duo an Uno was teased to be fair     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> They make stack duo (btc + xmr), but it lagged behind stack wallet, so i never recommended it      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Im not against multiwallet listings, but if there is a "pure" option, we should be listing that. My2c     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> can move onto the CCS ideas if nothing else to share      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a. MoneroOS Resurrection (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> no feedback prev meeting     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> not looking like a merge (positive reddit threads alone seem to not be enough)      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Still feel the sane way about that. I don't think there is an audience for this, at least not as designed / written     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> or as suggested, if the idea has overwhelming support seeking funding for it on a donation platform would be easier      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moving on      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> b. Monero Python Maintenance (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> rabidmining types arent going to use it.  home miners can just use gupax or xmrig     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> @everoddandeven:monero.social through blood sweat and tears has been trying to get this to work on my machine :D     
    
> **\<everoddandeven\>** <everoddandeven> I'm here if you have any question     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> @ofrnxmr:xmr.mx: also, i noticed a home miner using 1 screen and a box (forget the name) that receives video signal from all machines + 1 mouse/keyboard which looked convenient     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://github.com/everoddandeven/monero-spammer was created using monero-python - everodd you have used and broadcasted transactions with it on stressnet correct?     
    
> **\<everoddandeven\>** <everoddandeven> Yes, I have done some transactions on stressnet     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> the .deb package for monero-python under ubuntu has some missing dependencies which you have been fixing ... almost working but not yet (1 hr ago) https://github.com/everoddandeven/monero-python/releases     
    
> **\<everoddandeven\>** <everoddandeven> Like sending to 15 subaddresses     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Whats your tps look like     
    
> **\<everoddandeven\>** <everoddandeven> @plowsof:matrix.org: I have fixed that, now v0.0.4 has working deb installer for jammy and noble distro     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> transaction per second      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moment     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ok the deb installed "Setting up python3-monero (0.0.4) ..." 👍️ riiight      
    
> **\<everoddandeven\>** <everoddandeven> @ofrnxmr:xmr.mx: The script is still very basic, and I am waiting for the transactions to be confirmed before sending a new one     
    
> **\<everoddandeven\>** <everoddandeven> But it can be improved a lot, and I'm working on it     
    
> **\<rucknium\>** <rucknium> Sorry, by the time that the suitability of monero-python for creating a spammer was brought to my attention, http://github.com/Rucknium/xmrspammer was too far along to abandon it.     
    
> **\<everoddandeven\>** <everoddandeven> @everoddandeven: But wait     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> he is not yet visited the spamming trenches , xmrspammer .... is more of a display that monero-python works Rucknium      
    
> **\<everoddandeven\>** <everoddandeven> You can create like 10 wallet and then spam 10 txs     
    
> **\<rucknium\>** <rucknium> Looking forward to seeing how your spammer operates, @everoddandeven:monero.social  . At least, different spammers hit different code paths, so there's a benefit.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> and the resources used (ideally less than multiple rpc) which i hope to see     
    
> **\<everoddandeven\>** <everoddandeven> @everoddandeven: each txs can send like to 15 subaddresses for example     
    
> **\<everoddandeven\>** <everoddandeven> And that's what I have done, I have spammed 4 txs from 4 wallets, each txs was sending to 5 subaddresses for example     
    
> **\<rucknium\>** <rucknium> You could try to do tree expansion like I do, to get more txs waiting to confirm: https://github.com/rucknium/xmrspammer?tab=readme-ov-file#design     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @everoddandeven: Yea, but im spamming using 30 wallets who send to themselves     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> The slowdown is the generation of the txs     
    
> **\<everoddandeven\>** <everoddandeven> @rucknium: Yes, I was starting doing that, but I have wasted some time fixing things, but I will improve the spammer with tree expansion     
    
> **\<everoddandeven\>** <everoddandeven> @ofrnxmr:xmr.mx: Yes     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Could be better or worse with curl -> wallet-rpc vs monero python     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> monero-spammer is an 'in good faith' contirbution to prove that monero-python works and is worth maintaining / improving - as per the CCS idea     
    
> **\<rucknium\>** <rucknium> @everoddandeven:monero.social: Let me know if you have any questions about tree expansion, or at least my implementation of it.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> My spammer doesnt exist on the interwebs, sooo..     
    
> **\<everoddandeven\>** <everoddandeven> @rucknium: Yes, I will do, becase I have mostly lost in the R syntax 😅     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Anyway, this is abt monero python, not the spammer per-say     
    
> **\<plowsof\>** my matrix org account appears to have died for a second there      
    
> **\<plowsof\>** moving on?     
    
> **\<plowsof\>**   c. [v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)         
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> AliA has seen ofrns spammer , it is real      
    
> **\<plowsof\>** there we go     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> R vs Python fight finally     
    
> **\<plowsof\>**   d. [Revuo Monero Maintenance (2025 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/610)         
    
> **\<plowsof\>**   e. [Boog900 full time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/611)         
    
> **\<plowsof\>**   g. [acx part-time work on Monfluo 2025Q4](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/616)         
    
> **\<syntheticbird\>** <syntheticbird> lmao     
    
> **\<plowsof\>** lags     
    
> **\<syntheticbird\>** <syntheticbird> ah     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> soooo     
    
> **\<plowsof\>** we can leave it there unless there is some other business to discuss      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> I never comment on skunkwheel, but he seems to have been mis(double)counting some issues. Just a note     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Re boog. Didnt syn threaten to go nuclear if not merged?     
    
> **\<plowsof\>** rottenwheels latest CCS update https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/593#note_32241      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> re acx: i wonder if we'll see a pr for monfluo to getmonero soon     
    
> **\<r4v3r23\>** <r4v3r23> @ofrnxmr:xmr.mx: ANONERO? or corporate wallets only?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> i didnt mention anoner earlier?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> an open end     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-10-04T11:43:02+00:00
- Closed at: 2025-11-05T10:18:11+00:00
