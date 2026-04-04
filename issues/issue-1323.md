---
title: 'Monero Community Workgroup Meeting: Jan 10th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1323
author: plowsof
assignees: []
labels: []
created_at: '2026-01-10T10:48:14+00:00'
updated_at: '2026-03-25T09:47:12+00:00'
type: issue
status: closed
closed_at: '2026-03-25T09:47:12+00:00'
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
    - Monero CLI/GUI v0.18.4.5 ready for release 
    - Moneronet updated https://moneronet.info/ - Rucknium
    - MRL ban-list to receive an update in https://github.com/Boog900/monero-ban-list/pull/10
    - Stressnet 1.5 is released https://github.com/seraphis-migration/monero/releases
    - RandomX v2 in progress by sech1 https://www.reddit.com/r/Monero/comments/1pyzdpc/randomx_v2_update/
    - https://blocks.p2pool.observer/proofs DataHoarder
    - Registered MAGIC committee voters have until 20th - sgp https://github.com/MAGICGrants/Monero-Fund-Elections/issues
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This Week In Monero](https://cyphergoat.com/this-week-in-monero) 
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)    
  b. [Open-source Monero browser extension wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/636)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://Monerokon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [FCMP++ Stressnet](https://github.com/seraphis-migration)
6. Open ideas time    
    - Swap service review and Changelly. - msvb
8. Confirm next meeting date/time    
[Previous meeting including logs](https://github.com/monero-project/meta/issues/1314)    

Meeting logs will be posted here afterwards.    

# Discussion History
## michaesc | 2026-01-10T13:28:36+00:00
Hello @plowsof , can you please add to the agenda title six a subtitle **Swap service review and Changelly.** It's a relation to research done since the **6 December** meeting, with a report, request, and discussion. Hopefully in just five minutes, let's try hard to limit duration this time.

Thanks for adding the entry. I'll probably be late to the meeting but on time for the Open ideas time. I apologise.

## plowsof | 2026-03-25T09:47:03+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof\>** meeting time https://github.com/monero-project/meta/issues/1323     
    
> **\<plowsof\>** Greetings     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> is it 4'oblock already?     
    
> **\<plowsof\>** current block of https://xmrchain.net/block/3584850     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> greetings     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Nope. Its 1600     
    
> **\<plowsof\>** hbs im sorry yes :(     
    
> **\<plowsof\>** new releases: Monero CLI/GUI v0.18.4.5 soon and stressnet v1.5 is out now (with gui binaries) https://github.com/seraphis-migration/monero/releases      
    
> **\<plowsof\>** hi     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Includes memory fixes     
    
> **\<michael\>** <michael> Hello, saluton.     
    
> **\<plowsof\>** monerotech.info by rbrunner was lined in #monero just now, and  Moneronet.info by Rucinium has been updated https://moneronet.info/      
    
> **\<plowsof\>** s/lined/mentioned      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Rucinium is a new element     
    
> **\<plowsof\>** yes ive been going to rbrunners site for a long time checking confirming base addresses shown on ledger      
    
> **\<plowsof\>** ofrnxmr nice, memory fixes and sync improvements? 👀     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Huge improvements     
    
> **\<plowsof\>** is there a list of stressnet public rpc nodes somewhere? node3.monerodevs.org:28289      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> On a 256 thread host, goes from 150+gb to ~15gb     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> plowsof: 185.141.216.177:28189     
    
> **\<plowsof\>** if you dont feel like draining the entire mempool with 100% global hash you can get some testnet coins from kico s faucet here  https://faucet.xmr.pt/     
    
> **\<plowsof\>** the gui for your os is in the attachments @ https://github.com/seraphis-migration/monero/releases     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> At least we showed that fcmp can handle like 2+ blocks per minute at 2mb     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> RandomX v2 in progress by sech1 https://www.reddit.com/r/Monero/comments/1pyzdpc/randomx_v2_update/     
    
> **\<sech1\>** yep     
    
> **\<sech1\>** my WIP branch is here https://github.com/SChernykh/RandomX/tree/v2     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> Registered MAGIC committee voters have until 20th to vote - sgp https://github.com/MAGICGrants/Monero-Fund-Elections/issues     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> nice sech     
    
> **\<sech1\>** Basically the only thing left to do is RISC-V v2 code. Then some tweaking, and maybe more changes to test     
    
> **\<sech1\>** But RISC-V v2 code involves 2 different JIT compilers, and 3 different AES code versions, so it's quite a bit of work. Maybe a week's worth.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> good to hear. will there be any integration work for the xmrig dev / monero core to add these changes? or is it as simple as updating the submodule?     
    
> **\<DataHoarder\>** monero core uses the RandomX submodule, so it'd just need the hardfork logic afaik     
    
> **\<plowsof\>** 🙏     
    
> **\<plowsof\>** News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This Week In Monero](https://cyphergoat.com/this-week-in-monero)      
    
> **\<plowsof\>** 4. [CCS updates](https://ccs.getmonero.org/)         
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a. 39C3 Support (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> since the congress concluded, has to be either closed or renamed to 40C3     
    
> **\<sech1\>** plowsof Monero side will need to update RandomX submodule, and add RANDOMX_FLAG_V2 in the appropriate places (hardfork logic)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> @diego:cypherstack.com any new comments on this?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for confirming sech1     
    
> **\<sech1\>** XMRig... Will be a lot of work since it changed so much in 6 years     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i see     
    
> **\<sech1\>** Probably a month's worth of work, which I will start after v2 is finalized     
    
> **\<DataHoarder\>** the rounding changes weren't the worst to update for sech1 and I do have BMI2/AMD on my go one     
    
> **\<DataHoarder\>** the AES one, yeah :)     
    
> **\<DataHoarder\>** I gave up and only support that on hard AES with v2     
    
> **\<DataHoarder\>** and any other changes I guess     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ill follow the resulting global hash changes on DataHoarders page https://blocks.p2pool.observer/pools     
    
> **\<DataHoarder\>** SupportXMR was seen hitting 52% at instant hashrate measurements a couple of times, but they never reached that long term (7 days)     
    
> **\<DataHoarder\>** They have come down from that share since then     
    
> **\<DataHoarder\>** ~41% short term instant measurement and 43% long term (7 days)     
    
> **\<DataHoarder\>** hashvault keeps being attacked     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for the suggestion redsh4de. renaming to the next one in close proximity to this one requires alot of planning, im sure the team are resting. this proposal did not have an overwhelming positive merge sentiment     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> oh yes, hashvault ddos, forgot to mention that, thanks     
    
> **\<DataHoarder\>** HV recommended to move to alternates meanwhile or to set alternates as backup pools     
    
> **\<geonic\>** https://slate.com/human-interest/2016/11/close-proximity-is-a-redundant-confusing-irksome-phrase.html :p     
    
> **\<DataHoarder\>** Unknown blocks are back above 1% of share, need to investigate if it's some pool that has broken tagging     
    
> **\<DataHoarder\>** they are afaik around 2% of monero atm     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> geonic "like chewing tinfoil"? im sorry :(     
    
> **\<plowsof:matrix.org\>** geonic hides     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> b. Open-source Monero browser extension wallet (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/636)     
    
> **\<spiro_number1_fan:matrix.org\>** <spiro_number1_fan:matrix.org> where spiro dude? @spirobel:matrix.org     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> includes open source in the title, explains what open source is, does not link to previous work     
    
> **\<spiro_number1_fan:matrix.org\>** <spiro_number1_fan:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/nYZsSTsoYWzBBrPUxeHhXNsX.gif (image.gif)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Id say let them produce it first and merge if delivered     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Fkn kityy     
    
> **\<spiro_number2_fan:matrix.org\>** <spiro_number2_fan:matrix.org> 👍️     
    
> **\<spiro_number2_fan:matrix.org\>** <spiro_number2_fan:matrix.org> i mean thumbup for the ban lol     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> regarding the browser wallet, forget what i just said. If the proposer thinks it can be done securely as prescribed, id say merge it. Will probably comment on the proposal since they dont seem to be here     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> all i have to go by is text with some spelling mistakes as his previous work. with zero listed contributions to the project. 0 xmr or 5 its a no until the basics are addressed      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i would be interested to hear from woodser if there are any web wallet projects that where started / unfinished      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> But but we can grow the jetfund by 5xmr 😂     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> I think there was one using WASM which was started as part of a tipping project, but the name eludes me     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> but yeah, i admittedly did not do any background research on prior git contributions to see if capable. But i assume this would be a project that is slop prompted into the jetfund     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ah yes hbs,      
    
> **\<plowsof\>** tipxmr, moment      
    
> **\<plowsof\>** hbs, would you like to share some updates on your ccs, then redshade can do the same, and we can go to open ideas      
    
> **\<diego:cypherstack.com\>** <diego:cypherstack.com> Mm?     
    
> **\<plowsof\>** reg the 39c3 Support  CCS     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> this one https://ccs.getmonero.org/proposals/tipxmr.live.html      
    
> **\<diego:cypherstack.com\>** <diego:cypherstack.com> Oh right. Yeah the money would still be appreciated on the backend, but up to the community. The event was very successful.      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> they faced some technical issues - im not sure if relavant to just the wasm wallet sending/receiving      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> again , id like the proposer to show some previous work and actual research      
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> Sure.     
    
> **\<plowsof\>** excuse the lag on matrix side     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @hbs:matrix.org: msvb would like 5mins - so it snappy, soldier! /s     
    
> **\<spiro_number3_fan:unredacted.org\>** <spiro_number3_fan:unredacted.org> a comment on browser extension proposal here: https://monero.forum/t/monero-contents-youtubes-newsletters-etc/440/4     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> so make it* snappy     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> The GUI is done since the beginning of December for the read only part (milestone 1) and the part related to offer management is 99% complete. As stated in the December 1st update, I've decided to write a maker bot to easily provide liquidity to any MoneroSwap smart contract. The code for the bot was published around Xmas and  [... too long, see https://mrelay.p2pool.observer/e/_vnDktsKOFZSMXp3 ]     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> What would be great now is if there were more testers, either as manual makers/takers or as makers using the bot.     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> The current test contract is deployed on Gnosis Chain allowing xDAI-XMR atomic swaps. I intend to deploy another test contract on either Base or Arbitrum to do ETH-XMR swaps with low fees.     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> @ofrnxmr:xmr.mx: done sir     
    
> **\<plowsof\>** thanks hbs      
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> And anyone is welcome to join the dedicated moneroswap matrix room     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @michael:monero.social msvb-lab  you're up     
    
> **\<plowsof\>** Swap service review and Changelly. - msvb     
    
> **\<msvb-lab\>** Okay.     
    
> **\<msvb-lab\>** Anyone who is not interested in exchanges and swap services, please tune out and come back in five minutes. Thanks!     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> @hbs:matrix.org: https://matrix.to/#/#moneroswap:matrix.org     
    
> **\<msvb-lab\>** In Summer 2025 I started researching commercial exchanges and swap services for (1) fun, (2) necessity, and (3) request from peers. One request came from Changelly to gain insight (while repairing reputation) on Monero impressions.     
    
> **\<msvb-lab\>** In Autumn I did comparisons and searches (some AI) to determine the following:     
    
> **\<msvb-lab\>** A) Exchanges like Binance and Swaps like Shapeshifter cannot be accurately compared, even when an exchange acts like a swap.     
    
> **\<msvb-lab\>** B) About a dozen swap services with KYC exist, and I compared Simpleswap, ChangeNOW, Changelly, Fixedfloat, and Swapzone.     
    
> **\<spiro_number4_fan:unredacted.org\>** <spiro_number4_fan:unredacted.org> https://mrelay.p2pool.observer/m/unredacted.org/FsvNfsstHlJAknfeSbcHzjTB.gif (image.gif)     
    
> **\<msvb-lab\>** C) It seems that all have problems serving regular honest customers to 100%, so     
    
> **\<msvb-lab\>** complaints are easy to find around the Internet like Reddit.     
    
> **\<msvb-lab\>** D) It seems that Changelly is the largest of these, in some cases 10-100 times larger than most others in the list.     
    
> **\<msvb-lab\>** E) Changelly has earned a bad reputation 5-8 years ago and earned a good reputation 1-3 years ago.     
    
> **\<msvb-lab\>** F) When asked "Is Changelly's bad reputation accurate today, or only accurate years ago," a wide range of opinions respond. Nobody seems to care about other swaps like Shapeshift or their histories. Maybe because they're so small.     
    
> **\<msvb-lab\>** Z) My research is not exhaustive, and I'm sure I made a couple mistakes.     
    
> **\<msvb-lab\>** Anyway, I'm going to end my exchanges and swap research crusade very soon, I'm done. But my conclusion is that all the banning of Changelly only helps to affirm the wrong message that they don't want to respond or serve the Monero community. If anybody here disagrees, please explain why.     
    
> **\<msvb-lab\>** That's all I have ploswsof, unless people want to share their opinions, we can move on thanks!     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> I would suggest for changelly contact trocador.app and orangefren.com, put up insurance (collateral), and get listed with them.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks for sharing msvb      
    
> **\<msvb-lab\>** No problem, thanks for the stage time.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Collateral/insurance removes trust in favor of.. money     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> and reddit community as they are listed on the avoid list https://www.reddit.com/r/Monero/wiki/avoid/      
    
> **\<msvb-lab\>** Trocador and Orangefren seem to grade non-KYC services, which is a good thing. We don't have a grading system for those who properly or improperly implement KYC.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Fixedfloat has had some complaints, but they have large amounts of collateral with trocador and orangefren, and obviously dont want to lose it     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> fixedfloat has been hacked remember? and where offline for months because of it and came back rebranded as "ff dot io" :P     
    
> **\<msvb-lab\>** It's hard to obtain clarity when mixin exchanges and swaps, or mixing non-KYC services with KYC ones.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> yeah, but they have collateral, so it doesnt matter what happens since orangefren already has the $     
    
> **\<msvb-lab\>** So there is a bunch of unclarity everywhere, and about half the opinions I read don't offer facts or seem out of date.     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> All those services clearly lack transparency when it comes to the liquidity they use     
    
> **\<msvb-lab\>** There is the topic of banning all speech from Changelly on the Reddit as well, which doesn't have much to do with collateral or being listed somewhere.     
    
> **\<msvb-lab\>** They can't respond at all to compliments or complaints.     
    
> **\<msvb-lab\>** It might be good to blacklist all exchanges and swaps hbs, or at least all the ones that implement (properly or not) KYC.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @hbs:matrix.org: Orangefren list which exchanges have their own liq vs resell vs mixed     
    
> **\<msvb-lab\>** But that's not what's happening, which leads me to conclude there are serious flaws in impressions given online.     
    
> **\<msvb-lab\>** The Orangefren angle is really good, and he's ready to help I think. So let's close the topic now?     
    
> **\<msvb-lab\>** Are there any other items of 'Other business'?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> shamlessplug: if changelly has their own liq, they could always offer it on basicswap :D     
    
> **\<msvb-lab\>** Meeting is probably over, is it?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> never     
    
> **\<geonic\>** ofrnxmr: have there been any updates on basicswapdex that I missed?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks again msvb     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> geonic: Not today, the big task right now is getting electrum wallets implemented     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Hello everyone! The new website is rapidly nearing completion.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> To reduce onboarding from like 200gb bandwidth (for ltc + btc) and 2 days to like 2mins     
    
> **\<geonic\>** would be nice to get more regular updates on the gitlab too. it looks like the last one was 11 months ago     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Posted a extensive update on my CSS PR about a week ago - milestone 1 has been reached and exceeded, with some milestone 2 tasks accomplished. Currently working towards completing the rest of the routes. I have about 3-4 pages that don't have a layout left, all in the Resources section. After that - wiring in localization supp [... too long, see https://mrelay.p2pool.observer/e/nMaMk9sKRE9kOTBX ]     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> New routes since milestone 1 update:     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/get-started/accept-monero/ - currently with placeholders for images. Hoping that Diego's team will have time to draw up some nice images to complement the story of the page     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/community/workgroups/ - workgroup information     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/community/hangouts/ - chats & stuff     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/resources/press-kit/ - press kit, logos[... more lines follow, see https://mrelay.p2pool.observer/e/zIeNk9sKWG5jUzI4 ]     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> and probably will push sponsorship page later today - currently iterating on it in #monero-site:monero.social     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> geonic: There are extensive blog posts written ~monthly     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Updated designs for existing pages:     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/get-started/mining/ - mining information     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/get-started/contribute/ - some tweaks in the layout     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> https://beta.monerodevs.org/downloads/ - nicer Core downloads layouts, deduplicated the "Verify" CTA     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> Feedback appreciated, so anyone with any ideas or suggestions join #monero-site:monero.social & ping me with stuff     
    
> **\<geonic\>** are these linked anywhere in the proposal     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Hm. Not sure if the new blog website is. They used to be on particl blog (those were linked) but are now on basicswap website     
    
> **\<orangefren\>** <orangefren> msvb-lab: Sorry for not attending the meeting. Like @ofrnxmr:xmr.mx says, if Changelly wants to be listed I invite them to reach out, put up collareral and we can proceed with listing. We'll probably have a brief extra warning just to explain to our users what's happening     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks all for attending      
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> Thanks for moderating and keeping us safe from spam     
    
> **\<-julius-:matrix.org\>** <-julius-:matrix.org> fuck off hbs, you're one of the reason this community is not safe, you doxxed kewbit's country, you're a straight up fed so fuck off @hbs:matrix.org     
    
> **\<plowsof\>** invite only revealed the alts , thanks     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2026-01-10T10:48:14+00:00
- Closed at: 2026-03-25T09:47:12+00:00
