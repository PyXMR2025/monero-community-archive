---
title: 'Monero Community Workgroup Meeting: May 10th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1201
author: plowsof
assignees: []
labels: []
created_at: '2025-05-09T05:26:21+00:00'
updated_at: '2025-05-21T07:45:59+00:00'
type: issue
status: closed
closed_at: '2025-05-21T07:45:59+00:00'
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
    - ATH network hashrate https://bitinfocharts.com/comparison/monero-hashrate.html#alltime
    - NWLB/MRL meetings discuss adding POW to submit tx's to help nodes when FCMP++ is launched
    - Cuprate update v0.0.3 http://monero.observer/hinto-janai-releases-cuprated-v0.0.3-molybdenite/
    - p2pool mini has a whale https://mini.p2pool.observer/miners?weekly 
    - Tari launches (merge mined via p2pool) _"There will be 21 billion XTM as the initial supply, with a tail emission of 1% per year. 6.3 billion tokens, or 30% of the initial supply, will be pre-mined with significant lockups and vesting schedules."_ https://airdrop.tari.com/tokenomics
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)
  a. [Haveno App (Cross Platform)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/570)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2025](https://monerokon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2025-05-21T07:45:35+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof:matrix.org\>** Meeting time https://github.com/monero-project/meta/issues/1201     
    
> **\<plowsof:matrix.org\>** Greetings everyone     
    
> **\<aremor:matrix.org\>** Hi     
    
> **\<plowsof:matrix.org\>** why so much hash rate all of a sudden https://bitinfocharts.com/comparison/monero-hashrate.html#alltime     
    
> **\<ofrnxmr:xmr.mx\>** greets     
    
> **\<aremor:matrix.org\>** What’s the blockchain that wanted to deliberating 51% xmr? That sech mentioned.     
    
> **\<plowsof:matrix.org\>** and the p2pool mini whale has been revealed as being Tari   https://mini.p2pool.observer/miners?weekly , perhaps datahoarder could pull some strings behind the scenes and add the alias manually to avoid confusion?     
    
> **\<aremor:matrix.org\>** What’s the blockchain that wanted to deliberately 51% xmr? That sech mentioned.     
    
> **\<plowsof:matrix.org\>** indeed, "They're literally trying to 51% https://p2pool.io/u/d942b8e353666b71/image.png " via sech1     
    
> **\<DataHoarder\>** oh, it IS mini plowsof? links to that? I can flag it down if you have a specific source that shows their address in use     
    
> **\<plowsof:matrix.org\>** the name though? 😆     
    
> **\<plowsof:matrix.org\>** ah hello DataHoarder, there is some backlog in #p2pool     
    
> **\<plowsof:matrix.org\>** in #p2pool-log, also, there is apparentlya bug in the p2pool observer     
    
> **\<aremor:matrix.org\>** Yeah them. Not Tari right?     
    
> **\<plowsof:matrix.org\>** not tari no, hmmmmmm     
    
> **\<DataHoarder\>** the bug is known, unrelated to this. Have been having issues with monerod and fetching output indices     
    
> **\<DataHoarder\>** (blocks are still detected to be mined/main blocks, just can't fetch the outputs properly)     
    
> **\<aremor:matrix.org\>** Well Tari counteracts them. But def 2 chains pumping up xmr hash.     
    
> **\<plowsof:matrix.org\>** ah thanks DH, sech1/xmrvsbeast have confirmed it is tari, and feel they have made an error in judgement - did not expect so many hashes     
    
> **\<ofrnxmr:xmr.mx\>** Its broken, clearly     
    
> **\<ofrnxmr:xmr.mx\>** P2pool miners are supposed to have their own monero addresses. Tari even (afaik) generates a new monero address for you. So it shouldnt be throwing 200mh at one address unless something in misconfigured     
    
> **\<ofrnxmr:xmr.mx\>** Or unless its a "single" miner, in which case its not "tari" mining, but a miner/farm/botnet that mines tari. Or tari runs a centealized pool ontop of p2pool like aterx or minexmr2     
    
> **\<DataHoarder\>** let's talk after the meeting is done - and yeah, they should have definitely just used p2pool main (not mini) besides fuzzy feelings on using mini     
    
> **\<ofrnxmr\>** Obv matrix had to be slow      
    
> **\<ofrnxmr\>** Sent those messages like 4mins ago     
    
> **\<plowsof:matrix.org\>** 👍️     
    
> **\<plowsof:matrix.org\>** also, Cuprate update v0.0.3 http://monero.observer/hinto-janai-releases-cuprated-v0.0.3-molybdenite/     
    
> **\<sech1\>** I didn't confirm "it was tari"     
    
> **\<sech1\>** I only confirmed the miner merge mined Tari     
    
> **\<plowsof:matrix.org\>** is it only a hypothesis at this point?     
    
> **\<ofrnxmr\>** DataHoarder looks like supportxmr is down      
    
> **\<sech1\>** No, I analyzed merge mining tag in tx_extra of their shares     
    
> **\<plowsof:matrix.org\>** ahh apologies for the error , so this is totally unrelated to the Tari project?     
    
> **\<DataHoarder\>** that can be known with certainty ^     
    
> **\<sech1\>** So not a hypothesis     
    
> **\<sech1\>** They're definitely merge mining _something_     
    
> **\<sech1\>** And this _something_ must be Tari because there is no other option at the moment     
    
> **\<plowsof:matrix.org\>** ok Tari "project" are not involved - like the official tari binaries     
    
> **\<syntheticbird:monero.social\>** \* scary music starts to play \*     
    
> **\<sech1\>** No     
    
> **\<sech1\>** It's some individual with rented hashrate merge mining Tari     
    
> **\<sech1\>** They're probably gambling that they can pay back the rental with mined XMR     
    
> **\<plowsof:matrix.org\>** yeah thanks, i been spreading fud about the Project , Sorry FP     
    
> **\<sech1\>** and get Tari coins in the process     
    
> **\<DataHoarder\>** ok, I hadn't missed anything then plowsof, this is the backlog I know :)     
    
> **\<sech1\>** And so far they're successful because XMR went up in price, so they will be able to pay the rental     
    
> **\<plowsof:matrix.org\>** thanks for investigating and confirming this     
    
> **\<plowsof:matrix.org\>** side note: i wonder if any high fee tx's have appeared during this rental     
    
> **\<ofrnxmr\>** i tried to reach out to one of supportxmr admin but no response     
    
> **\<ofrnxmr\>** Nanopool is 38% of the hash right now as a result of support being offline     
    
> **\<spirobel:kernal.eu\>** sech1 so its a bit like someone farming an airdrop with a sybil?     
    
> **\<sech1\>** there's no sybil     
    
> **\<sech1\>** they just have a lot of hashrate     
    
> **\<sech1\>** Ah, an airdrop     
    
> **\<spirobel:kernal.eu\>** some people do professional airdrop farming     
    
> **\<plowsof:matrix.org\>** ah, from the supportxmr chat, mining is apparently OK, just the API is being DDosD     
    
> **\<spirobel:kernal.eu\>** they make tons of wallets and do transfers / activity that is likely to be rewarded     
    
> **\<sech1\>** ahhhh     
    
> **\<sech1\>** Here, they just rented a lot of hashrate to mine Tari     
    
> **\<ofrnxmr\>** plowsof, the blocks found dont look like sxmrs ok     
    
> **\<sech1\>** and they get mined XMR to pay for the rent     
    
> **\<spirobel:kernal.eu\>** this could be a similar pattern / motivation     
    
> **\<sech1\>** it can be a self-sustainable process if the rental price is not too high, or as long as XMR keeps going up in price     
    
> **\<monerobull:matrix.org\>** Nah     
    
> **\<monerobull:matrix.org\>** Tari airdrop has nothing to do with transactions     
    
> **\<monerobull:matrix.org\>** Someone definitely rented hash to merge mine     
    
> **\<plowsof:matrix.org\>** ofrnxmr but an admin said its ok 😭😭     
    
> **\<spirobel:kernal.eu\>** monerobull: I know. just gave this as an example to explain the concept.     
    
> **\<spirobel:kernal.eu\>** there is a whole subculture related to airdrop farming     
    
> **\<monerobull:matrix.org\>** And sometimes it works     
    
> **\<plowsof:matrix.org\>** so tari has 2 mining algorithms. i wonders if its more profitable to rent SHA3 or RandomX hashes? i have no idea     
    
> **\<monerobull:matrix.org\>** I wish I had airdrop farmed hyperliquid     
    
> **\<monerobull:matrix.org\>** For sure sha3     
    
> **\<monerobull:matrix.org\>** Because of AI hype, you can rent 4060s for 15 cents an hour     
    
> **\<sech1\>** SHA3 can be mined on FPGAs and ASICs     
    
> **\<plowsof:matrix.org\>** so the profit incentive would be to do this with sha3 perhaps? tbh i have no idea     
    
> **\<sech1\>** it's a matter of time before GPUs are non-competitive there     
    
> **\<ofrnxmr\>** Also depends on how the algos are weighted (idk how they are)     
    
> **\<monerobull:matrix.org\>** 50/50     
    
> **\<ofrnxmr\>** hash per hash 50:50?     
    
> **\<ofrnxmr\>** Sounds unreasonable / unlikely      
    
> **\<monerobull:matrix.org\>** Targeted distribution is 50/50     
    
> **\<plowsof:matrix.org\>** tokenomics of tari / mining uhhh all i know is Messi and Paris hilton make moneys if tari pumps so thats re assuring xD     
    
> **\<ofrnxmr\>** lil wayne hopefully too     
    
> **\<plowsof:matrix.org\>** https://airdrop.tari.com/tokenomics     
    
> **\<ofrnxmr\>** 😂     
    
> **\<plowsof:matrix.org\>** "Network rewards are split 50/50, with half of the Tari block reward going towards merge mining performed with the RandomX hashing algorithm and 50% of the block rewards going to Tari standalone miners using the SHA3x hashing algorithm. "     
    
> **\<ofrnxmr\>** Yeah, so regardless of randomx hash, randomx gets 50% of the block reward     
    
> **\<ofrnxmr\>** s     
    
> **\<ofrnxmr\>** so sha doesnt have an advantage. Sounds like 2 difficulties are at play. Ok enough premine token talk :D     
    
> **\<plowsof:matrix.org\>** any other highlights as of late? News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)     
    
> **\<sech1\>** ofrnxmr both algos target 4 minute per block     
    
> **\<sech1\>** so Tari gets blocks every 2 minutes on average, with 50/50 distribution between RandomX and SHA3     
    
> **\<ofrnxmr\>** Nice     
    
> **\<plowsof:matrix.org\>** perfect daemon, anon, ooo123ooo123 has been paid for his services to the monero project     
    
> **\<plowsof:matrix.org\>** aremor is here, hello sir     
    
> **\<plowsof:matrix.org\>** shall we move on to the Haveno APP ccs idea?     
    
> **\<NorrinRadd\>** sure      
    
> **\<syntheticbird:monero.social\>** close     
    
> **\<plowsof:matrix.org\>** 4. [CCS updates](https://ccs.getmonero.org/)     
    
> **\<syntheticbird:monero.social\>** too good to be true     
    
> **\<plowsof:matrix.org\>** a. [Haveno App (Cross Platform)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/570)     
    
> **\<syntheticbird:monero.social\>** i don't want to live in a world in which an haveno app does exist     
    
> **\<syntheticbird:monero.social\>** this ccs proposal might succeed and thats an issue     
    
> **\<plowsof:matrix.org\>** doesnt? 😄     
    
> **\<NorrinRadd\>** There was a reddit thread where the idea got lots of support      
    
> **\<plowsof:matrix.org\>** ohhh     
    
> **\<NorrinRadd\>** 8,500 views and no negative comments      
    
> **\<ofrnxmr\>** https://github.com/atsamd21/Haveno-app syn      
    
> **\<syntheticbird:monero.social\>** thx     
    
> **\<ofrnxmr\>** Thats a different one     
    
> **\<syntheticbird:monero.social\>** ig its over     
    
> **\<syntheticbird:monero.social\>** well then +1 for aremor     
    
> **\<plowsof:matrix.org\>** bisq users will get an app soon too https://bisq.network/blog/mobile-app-survey/     
    
> **\<syntheticbird:monero.social\>** \> Bisq Easy Mobile     
    
> **\<ofrnxmr\>** I assume it works but havent tried it     
    
> **\<NorrinRadd\>** how soon?      
    
> **\<syntheticbird:monero.social\>** \> thumbnail shows Bisq Desktop     
    
> **\<ofrnxmr\>** Bisq has 3 apps in the works     
    
> **\<NorrinRadd\>** bisq does tend to move pretty slowly      
    
> **\<syntheticbird:monero.social\>** like java? HAHAHAHAHA     
    
> **\<ofrnxmr\>** one of them connects to bisw desktoo     
    
> **\<syntheticbird:monero.social\>** this joke was sponsored by the rustacean gang     
    
> **\<plowsof:matrix.org\>** Haveno is Java =(     
    
> **\<NorrinRadd\>** at this point, i'm working on milestone 3 out of 5     
    
> **\<ofrnxmr\>** https://github.com/bisq-network/bisq-mobile     
    
> **\<syntheticbird:monero.social\>** sorry plowsof i don't hear you im under a tunnel     
    
> **\<NorrinRadd\>** "I assume it works but havent tried it" - can't compile it on linux      
    
> **\<plowsof:matrix.org\>** its nice to see that people still have an interest in the Haveno APP's scene after qtip     
    
> **\<ofrnxmr\>** Even qtip lootspam still does     
    
> **\<NorrinRadd\>** how many approvals are needed to go into funding?      
    
> **\<plowsof:matrix.org\>** thats too awkward to ask about     
    
> **\<plowsof:matrix.org\>** thanks though     
    
> **\<ofrnxmr\>** enough to make it look like it would be funded     
    
> **\<plowsof:matrix.org\>** 'this many'     
    
> **\<NorrinRadd\>** lol shouldn't it be defined somewhere?     
    
> **\<NorrinRadd\>** it goes on 'vibez'?      
    
> **\<ofrnxmr\>** no, numbers arent concrete. You can have 20 upvotes and not get funding     
    
> **\<plowsof:matrix.org\>** how long have you been around for again? welcome to the CCS     
    
> **\<ofrnxmr\>** its on the proposer to rally support     
    
> **\<ofrnxmr\>** its also on the proposer to raise the funds      
    
> **\<NorrinRadd\>** before the idea is approved, there is no contract?     
    
> **\<NorrinRadd\>** so i can distribute the app before the proposal is approved?      
    
> **\<NorrinRadd\>** because at this point, it's almost done      
    
> **\<plowsof:matrix.org\>** ive not signed anything     
    
> **\<ofrnxmr\>** yea, you can do whatever you like before it goes to funding     
    
> **\<NorrinRadd\>** (distribute without source code, I mean)      
    
> **\<ofrnxmr\>** Has to be foss at time it goes to funding though     
    
> **\<ofrnxmr\>** Oh, nk     
    
> **\<NorrinRadd\>** ?     
    
> **\<ofrnxmr\>** it being closed source will nacks on the proposal     
    
> **\<plowsof:matrix.org\>** distirbute closed source haveno app binaries, yes you can do that, but you've bee around for long enough to know how that would be perceived right??     
    
> **\<plowsof:matrix.org\>** or do i have to bank my head on this desk     
    
> **\<plowsof:matrix.org\>** bang     
    
> **\<NorrinRadd\>** i'm asking because the proposal is not currrently approved     
    
> **\<NorrinRadd\>** if it was approved, i know the rules      
    
> **\<ofrnxmr\>** its an easy way to have the proposal closed, and have nobody trust your work     
    
> **\<ofrnxmr\>** It has to be foss at all stages      
    
> **\<ofrnxmr\>** Including the idea stage     
    
> **\<NorrinRadd\>** to garner support, i can put the app in the app store for millions to see the value in it     
    
> **\<ofrnxmr\>** You can release binaries, but not w/o the source and a proper license       
    
> **\<plowsof:matrix.org\>** close the idea - release closed source binaries - re-open proposal 😆     
    
> **\<ofrnxmr\>** If its not foss, proposal should be closed      
    
> **\<ofrnxmr\>** Reopen when you decide to go foss     
    
> **\<NorrinRadd\>** ok, i can see how that goes      
    
> **\<spirobel:kernal.eu\>** haveno is agpl licensed     
    
> **\<plowsof:matrix.org\>** there are vibe coders waiting to poach the code so i understand     
    
> **\<plowsof:matrix.org\>** but do you realise the audible HISSING sound of all the cats reading this when yo usuggest anythig closed source?     
    
> **\<NorrinRadd\>** again, only asking because it's currently not approved      
    
> **\<ofrnxmr\>** Yeah. Foss at all stages     
    
> **\<ofrnxmr\>** Technically supposed to be "permissive", but i think were allowing copyleft      
    
> **\<ofrnxmr\>** 4 stages. Idea, funding, wip, completed     
    
> **\<NorrinRadd\>** is there any feedback to the proposal?      
    
> **\<spirobel:kernal.eu\>** agpl is copyleft so sources have to be distributed with the release     
    
> **\<spirobel:kernal.eu\>** agpl is copyleft sources have to be distributed with the release     
    
> **\<NorrinRadd\>** I mostly get support & silence, so not really aware of why it's not moving forward      
    
> **\<plowsof:matrix.org\>** i suppose alot of devs are tuned out of the haveno app scene because of kewbit cloud of drama     
    
> **\<ofrnxmr\>** Not juat devs     
    
> **\<ofrnxmr\>** Usually therr are 10s of people commenting on haveno related stuff     
    
> **\<ofrnxmr\>** Theres like 0 commenting on this proposal     
    
> **\<plowsof:matrix.org\>** we're all devs, i decided to promote us all     
    
> **\<syntheticbird:monero.social\>** thx plowsof     
    
> **\<ofrnxmr\>** its not a passive environment     
    
> **\<ofrnxmr\>** Go rally support     
    
> **\<NorrinRadd\>** do note, no negative comments      
    
> **\<NorrinRadd\>** there are comments, all positive     
    
> **\<aremor:matrix.org\>** Tor connection is lagging     
    
> **\<NorrinRadd\>** batting 100%     
    
> **\<plowsof:matrix.org\>** hm     
    
> **\<NorrinRadd\>** on reddit & getmonero.org      
    
> **\<NorrinRadd\>** so you're saying, if it were not for qtip, it would probably be approved already?      
    
> **\<ofrnxmr\>** Nah, i'm saying that theres almost no activity on the proposal      
    
> **\<ofrnxmr\>** No known handles (need to check again] have shown support on the proposal      
    
> **\<plowsof:matrix.org\>** if we do nothing - haveno apps will appear with or without you, the sad truth     
    
> **\<NorrinRadd\>** i'm replying to "i suppose alot ofdevs are tuned out of the haveno app scene because of kewbit cloud of drama"     
    
> **\<ofrnxmr\>** And there are still 2 (maybe more) bounties available to be claimed      
    
> **\<ofrnxmr\>** Yeah. Kewbit brought a lot of support     
    
> **\<NorrinRadd\>** i know of one, but it's android only (mine is 5 platforms)      
    
> **\<ofrnxmr\>** His marketing was top notch. his delivery, nkt so much     
    
> **\<NorrinRadd\>** 6 actually      
    
> **\<NorrinRadd\>** also, it's for an idea of an android node, which is going to have problems getting into app stores     
    
> **\<ofrnxmr\>** bisq's thin clients are for fdroid     
    
> **\<syntheticbird:monero.social\>** app stores be like: YOU WILL USE A KYC COMPANY SERVER FOR YOUR WEB-WRAPPED APP AND YOU'LL BE HAPPY     
    
> **\<NorrinRadd\>** idk how long people have followed bisq, but it's an incredibly slow moving project      
    
> **\<NorrinRadd\>** they release an idea, we can expect it 3 years later      
    
> **\<plowsof:matrix.org\>** "I've been writing software for 20 years now. I've independently published to the App Store before and shipped mobile games with large publishers, just to name a few." sadly we can't ask for proof i assume as this would dox you? - and then we have your code contributions - have any devs came forward to recommend you with their seal of approval (as was done for qbit?)     
    
> **\<NorrinRadd\>** In DMs, yes      
    
> **\<NorrinRadd\>** I've already doxxed myself     
    
> **\<plowsof:matrix.org\>** ah ok, promising that you can prove this. as for dev(s) who can come forward and recommend your skills - that would be the bare minimum for any new dev/contributor on the ccs, some kind of solid referral - this process did not work for qbit though as we got burned     
    
> **\<NorrinRadd\>** "promising that you can prove this" - which one?      
    
> **\<plowsof:matrix.org\>** or to review your previous contributions to the haveno project - who can we ask to provide a dossier about them     
    
> **\<plowsof:matrix.org\>** your work experience outside of monero*     
    
> **\<NorrinRadd\>** you can ask Woodser about that. I've done several PRs with him.      
    
> **\<NorrinRadd\>** everything he's gone over has been good      
    
> **\<hardenedsteel:monero.social\>** is it a centralized pool?     
    
> **\<NorrinRadd\>** oh, i'll DM my linkedin to whoever      
    
> **\<NorrinRadd\>** although anyone going through that proposal can find it     
    
> **\<NorrinRadd\>** plowsof where do you want these items?     
    
> **\<plowsof:matrix.org\>** thats the problem, the things i mention, proof of work / referral are only the first hurdle, the other stuff, nebulous consensus - known contributors have more weight than people looking at a reddit thread showing a nice project     
    
> **\<NorrinRadd\>** ok, so that's also desired. anything else?      
    
> **\<NorrinRadd\>** i can work on that one also      
    
> **\<ofrnxmr:xmr.mx\>** s/the first hurdle/a nice to have/     
    
> **\<ofrnxmr:xmr.mx\>** Not a dealbreaker/maker     
    
> **\<plowsof:matrix.org\>** another benefit would basically be slandering atsamd21's project, perhaps stating why yours is better     
    
> **\<NorrinRadd\>** who here is going to maintain a c# problem?      
    
> **\<plowsof:matrix.org\>** not actually slandering, just saying it like that for comedic effect, but with many options available to the community, there needs to be some kind of 'why your project'     
    
> **\<NorrinRadd\>** literally cannot be maintained on linux     
    
> **\<NorrinRadd\>** s/problem/project      
    
> **\<syntheticbird:monero.social\>** Bro is literally right     
    
> **\<ofrnxmr:xmr.mx\>** The problem we're avoiding is what happens if it is not successfully funded     
    
> **\<NorrinRadd\>** correct me if i'm wrong, that just means i don't receive the total amount, right?      
    
> **\<plowsof:matrix.org\>** other aspect yes, achieving funding if put up     
    
> **\<NorrinRadd\>** isnt that only a problem for me?      
    
> **\<ofrnxmr:xmr.mx\>** the c# project is also not seeking funding     
    
> **\<ofrnxmr:xmr.mx\>** That depends how you work your proposal. If you have a funding deadline and agree to complete work for less than requested etc.     
    
> **\<ofrnxmr:xmr.mx\>** Some people would abuse this and just abandon the project     
    
> **\<NorrinRadd\>** that ship has sailed. i'm already on milestone three. so been working without funding for 2 months now.      
    
> **\<ofrnxmr:xmr.mx\>** How you word* your proposal     
    
> **\<NorrinRadd\>** to be more clear, if approved, up to milestone three will be shipped without question, mainly because the app isn't very useful without everything defined up to that point.      
    
> **\<plowsof:matrix.org\>** thank you for attending / responding to the questions , as we're 14 mins over we can open end the meeting here     
    
> **\<spirobel:kernal.eu\>** hm ...     
    
> **\<spirobel:kernal.eu\>** still wanted to ask something     
    
> **\<plowsof:matrix.org\>** the open end is open, any other business?     
    
> **\<spirobel:kernal.eu\>** this was the question.     
    
> **\<plowsof:matrix.org\>** 4 irc , moment     
    
> **\<plowsof:matrix.org\>** https://libera.monerologs.net/monero-community/20250509#c524442     
    
> **\<clipped message\>** it is a rust wrapper for wallet2.cpp. I am wondering if there is demand for a monero-wallet-rpc replacement based on monero-serai / monero-oxide that is pure rust and not a wrapper for wallet2. Some concern was that the syncing uses a different endpoint from wallet2. I used the cuprate epee parsing crate in  https://github.com/monerochan-ecosystem/monero-wallet-api to adapt the sy<clipped message>     
    
> **\<clipped message\>** ncing to use getblocks.bin as well. The issue is for me, my priority is indexedb / sqlite in ts backend storage of outputs + fetching in typescript as well. I could implement this in rust too so we get a rust only alternative monero-wallet-rpc as a crate / binary. The question is: is there demand for this? Maybe we can add this as an agenda item. So we can see if people want this <clipped message>     
    
> **\<spirobel:kernal.eu\>** and if it makes sense for me to spend a bit of extra time on this.     
    
> **\<clipped message\>** I am wondering if there is demand for a monero-wallet-rpc replacement based on monero-serai / monero-oxide that is pure rust and not a wrapper for wallet2. Some concern was that the syncing uses a different endpoint from wallet2. I used the cuprate epee parsing crate in  https://github.com/monerochan-ecosystem/monero-wallet-api to adapt the syncing to use getblocks.bin as well. Th<clipped message>     
    
> **\<clipped message\>** e issue is for me, my priority is indexedb / sqlite in ts backend storage of outputs + fetching in typescript as well. I could implement this in rust too so we get a rust only alternative monero-wallet-rpc as a crate / binary. The question is: is there demand for this? Maybe we can add this as an agenda item. So we can see if people want this and if it makes sense for me to spend <clipped message>     
    
> **\<spirobel:kernal.eu\>** a bit of extra time on this.     
    
> **\<plowsof:matrix.org\>** edited, no no no     
    
> **\<spirobel:kernal.eu\>** :D     
    
> **\<spirobel:kernal.eu\>** the first sentence would be out of context lol     
    
> **\<plowsof:matrix.org\>** the monerlogs link takes irc to the question     
    
> **\<plowsof:matrix.org\>** perhaps something to share with boog900 / cuprate? if they are going to produce something like this? or plan to?     
    
> **\<plowsof:matrix.org\>** or need someone for the job 🫡     
    
> **\<plowsof:matrix.org\>** a chance to get more people tinkering with rust and monero development     
    
> **\<spirobel:kernal.eu\>** also happy to contribute it back into the oxide repo if they want :D     
    
> **\<NorrinRadd\>** "4 irc , moment" - much appreciated      
    
> **\<boog900:monero.social\>** I have heard monero-wallet-rpc can be unstable, so maybe having an alternative will be good. We have no plans for wallets under cuprate at the moment although it might be something we will do in the future     
    
> **\<ofrnxmr:xmr.mx\>** It was / is buggy, not unstable     
    
> **\<ofrnxmr:xmr.mx\>** Its a lot better now than it was 6 months ago     
    
> **\<spirobel:kernal.eu\>** the rpc code is interleaved with the fetching to the daemon. I think there was a PR recently that adressed that a bit     
    
> **\<ofrnxmr:xmr.mx\>** People always just worked around the issues instead of fixing them 💢     
    
> **\<spirobel:kernal.eu\>** (the concurrency is interleave)     
    
> **\<spirobel:kernal.eu\>** (the concurrency is interleaved)     
    
> **\<plowsof\>** spirobel 1000 xmr proposal to create this, congrats      
    
> **\<spirobel:kernal.eu\>** no its on me haha     
    
> **\<ofrnxmr:xmr.mx\>** It also didnt save wallets when closed, and forced resyncing 💀     
    
> **\<ofrnxmr:xmr.mx\>** So would make it appear very unresponsive     
    
> **\<ofrnxmr:xmr.mx\>** And would eat data     
    
> **\<plowsof:matrix.org\>** an end to da meeting, thank you all for attending and providing feedback     
    
> **\<plowsof:matrix.org\>** the monerokon irc bridge is working finally , woohoo     
    
> **\<ofrnxmr:xmr.mx\>** It also missed the top block when restoring, and would force a fast scan from checkpoints     
    
> **\<ofrnxmr:xmr.mx\>** Oh i thought it was over     
    
> **\<plowsof:matrix.org\>** 0 mins since meeting has been over     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-05-09T05:26:21+00:00
- Closed at: 2025-05-21T07:45:59+00:00
