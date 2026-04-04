---
title: 'Monero Community Workgroup Meeting: Saturday 20th Jan 15:00UTC'
source_url: https://github.com/monero-project/meta/issues/956
author: plowsof
assignees: []
labels: []
created_at: '2024-01-13T23:21:26+00:00'
updated_at: '2024-01-25T11:46:17+00:00'
type: issue
status: closed
closed_at: '2024-01-25T11:46:17+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
15:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
    - [XMR<->BCH atomic swaps FlipStarter](https://atomic-flip.pat.mn/en)
    - [100XMR donation to the general fund](https://monero.observer/monero-general-fund-100-xmr-anon-donation/)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)
    - Animated Videos: Nodes script [gitlab comment](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/412#note_23203) - VostoEmisio     
    - [Boog900](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/405#note_23183) 
    - [plowsof](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/418#note_23209)
    - Eventual Multisig wallet: 
        - gingeropolous and jwinterm have agreed to help publicly. 
        - Do we need another outside of the US? 
        - should we introduce multisig gradually by first going to a 2/3? 3/5? (depending on signer applicants)    
  
  a. [hinto-janai - full-time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422)    
  b. [0xfffc-2024Q1-(3 months, February, March, April, 2024)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/429)    
  c. [escapethe3RA Monero Observer maintenance (2024 Q1)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/430)    
7. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
        - Weblate server status
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2024](https://github.com/MoneroKon/)
  e. Website workgroup
        - Onion URL for the CCS in-progress still
        - With one of monero-sites long time contributor departing, the immediate steps forward are to handle all open pull requests and to find someone to fill the role.
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
8. Open ideas time    
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/952)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2024-01-20T20:22:15+00:00
Logs

> __< p​lowsof:matrix.org >__ Meeting time https://github.com/monero-project/meta/issues/956     

> __< ofrnxmr >__ Feels like its been almost 2 weeks. Hi     

> __< p​lowsof:matrix.org >__ greetings, what has been happening? News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)     

> __< ofrnxmr >__ Revuo >> getmonero.org pr     

> __< r​ucknium:monero.social >__ Hi     

> __< p​lowsof:matrix.org >__ the BCH<>XMR atomic swaps flipstarter was funded https://atomic-flip.pat.mn/en , further progress can be followed here https://gist.github.com/mainnet-pat/267fe6f0111ce2198559b3e19040ba26 . Rucknium is offering a reward for anyone to verify the implementation . as shown in the last comment on the related bounty https://bounties.monero.social/posts/37/18-921m-bch-xmr-atomic-swaps     

> __< ofrnxmr >__ Some further discussion on the matter in #monero-community-dev     

> __< p​lowsof:matrix.org >__ i was asked if any atomic swap implementation has been "verified" (e.g. the steps kayabanerve detailed to verify the XMR<>BCH swaps in #community-dev). would this be of interest to raise funds for if it turns out to be needed? 🤷     

> __< 0​xfffc:matrix.org >__ Hi everyone.     

> __< r​ucknium:monero.social >__ My intention was for kayaba to "verify" at the same level of thoroughness that he verified the ETH<>XMR atomic swap.     

> __< ofrnxmr >__ basicswapdex doesnt support bch. I think id ask them to verify it      

> __< msvb-lab >__ Hello.     

> __< ofrnxmr >__ They use htlc and adaptor sigs too     

> __< r​ucknium:monero.social >__ He said the cryptography passed the sniff test. I may just accept that if there is no one else capable and interested in verifying that part. The BCH script contract has already been verified.     

> __< p​lowsof:matrix.org >__ "Anybody tried BTC-XMR Atomic Swaps on Samourai?" -> yes, COMIT swaps in the palm of your hand... gingeropolous commented on reddit something to the effect of needing enough people to sell their monero for dirty btc. and, if anyone in #unstoppableswap:matrix.org  noticed, a swap provider needing to go offline because of the high fees     

> __< ofrnxmr >__ Ruchnium - you dont think the particl team would do it? Theyre going to integrate bch     

> __< r​ucknium:monero.social >__ Maybe they would, but when? I don't know how to contact them     

> __< ofrnxmr >__ I'll contact them     

> __< p​lowsof:matrix.org >__ #basicswap:matrix.org is their matrix room right?     

> __< r​ucknium:monero.social >__ pokkst said that he would like to look at the BCH<>XMR atomic swap implementation once the Samourai BTC<>XMR swap beta was launched. So he could look at it now I guess.     

> __< r​ucknium:monero.social >__ Ok. Right now I have set the "bounty" for verification of the cryptography at the "token appreciation" level of 1 BCH. But that could be negotiable.     

> __< p​lowsof:matrix.org >__ comit swaps are abandonware and one way* im assuming the bch xmr swaps are both ways?     

> __< k​ayabanerve:matrix.org >__ Rucknium: I'd pay out the bounty yet note obviously, it wasn't audited.     

> __< r​ucknium:monero.social >__ Yes, I did not intend to require a full code audit. Just a basic check     

> __< r​ucknium:monero.social >__ All swaps are both ways. Just some swap implementations only allow the limit order on one side of the book.     

> __< ofrnxmr >__ basicswap gets around it / (perhaps plans to get around it) by using their smsg system to automate the initiation of the transfer by whatever side has to initiate it     

> __< r​ucknium:monero.social >__ But the BCH<>XMR atomic swap implementation only allows the limit orders on one side like COMIT     

> __< p​lowsof:matrix.org >__ not abandonware - low fees - one way, an improvement still     

> __< r​ucknium:monero.social >__ The Samourai swaps use the COMIT protocol. So it has been abandoned, put in the orphanage, and adopted. I guess.     

> __< p​lowsof:matrix.org >__ lol     

> __< ofrnxmr >__ its 2 way if you use bch or another layer to automate the transfer intiation      

> __< ofrnxmr >__ s/bch/bsx     

> __< ofrnxmr >__ Bsx uses comit too     

> __< p​lowsof:matrix.org >__ Farcaster ccs is marked as "completed" btw     

> __< p​lowsof:matrix.org >__ nobody using it? :(     

> __< r​ucknium:monero.social >__ pokkst said he wanted to use COMIT instead of Farcaster for Samourai swaps because COMIT is a tested protocol.     

> __< nioCat >__ let's test Farcaster  :)     

> __< p​lowsof:matrix.org >__ their web-ui works* it all works*     

> __< r​ucknium:monero.social >__ "FWIW, I think Taproot is cool in theory, and I even wrote the Taproot implementation for the ExtLibJ library SW uses (that isn't used for much atm/yet). But COMIT has been pretty well-tested and it works, and looks like a P2WSH multisig except in the cases of an adversarial swap, and in the future it's entirely possible to implement other protocols if/when they're ready. Not to m<clipped message>     

> __< r​ucknium:monero.social >__ ention most of Taproot is used for jpegs and shit anyway, last I checked, which don't look like normal, single-sig spends." https://nitter.net/pokkst/status/1748134805269569709#m     

> __< k​ayabanerve:matrix.org >__ The protocol appears to have the proper cryptography from a knowledgeable source and appears to use it where appropriate to implement the swap protocol.     

> __< k​ayabanerve:matrix.org >__ This is not a full check of exact compliance nor guarantee.     

> __< k​ayabanerve:matrix.org >__ cc Rucknium:     

> __< ofrnxmr >__ Because scripts are not possible on blockchains like XMR, there are currently constraints on which coin can initiate a swap on BSX. To trade Monero for Bitcoin, for example, only the BTC-owning side can *initiate* a transaction.     

> __< ofrnxmr >__ Yet, because advance planning can be done consistent with atomic swapping, it is conceptually possible for both sides to effectively originate a swap:     

> __< ofrnxmr >__ If I have XMR and want, say, BTC, one could simply post a desire to do a trade as their offer. The BTC owner could then initiate the current, more formal process, still risk free. This process can be automated and be all but invisible to the front-end user experience, and is a major and very exciting upcoming item on the BSX roadmap.     

> __< r​ucknium:monero.social >__ Thanks for your cursory check, kayaba :D     

> __< ofrnxmr >__ https://particl.news/atomic-swap-style-showdown/     

> __< k​ayabanerve:matrix.org >__ That's really not valid commentary IMO :/     

> __< k​ayabanerve:matrix.org >__ (the above commentary on Taproot)     

> __< r​ucknium:monero.social >__ pokkst's commentary? Ok you can tweet at him     

> __< p​lowsof:matrix.org >__ hot take on pokssts commentary 1/12 👇️ 🧵     

> __< ofrnxmr >__ Pokkst is on simplex too     

> __< k​ayabanerve:matrix.org >__ I don't care to develop such an argument due to how one of their people called to lynch Seth.     

> __< p​lowsof:matrix.org >__ oh     

> __< ofrnxmr >__ You mean s*th (taboo name)     

> __< ofrnxmr >__ If you say it 3 times in the mirror..     

> __< ofrnxmr >__ Btw, while kaya is here     

> __< ofrnxmr >__ On cake's twitter space, kaya noted that he has been working on FCMP lately 😁     

> __< ofrnxmr >__ Continued work* on     

> __< p​lowsof:matrix.org >__ Seth retweeted a teaser from the passport hardware wallet account (so Monero support confirmed then?.. i don't know)     

> __< p​lowsof:matrix.org >__ any other recent highlights to discuss?     

> __< ofrnxmr >__ (Sgp since youre here - spirobels ban ended a long time ago)     

> __< nioCat >__ spirobel is in policy asking for someone's ban      

> __< ofrnxmr >__ Calling for sgp's ban (just read)     

> __< k​4r4b3y:karapara.net >__ ha     

> __< nioCat >__ sigh     

> __< p​lowsof:matrix.org >__ causing quite the stir on the reddits     

> __< ofrnxmr >__ I wouldnt go that far. But sgp banned hin for 1 week and hasnt unbanned hin afaik     

> __< r​ucknium:monero.social >__ We have an agenda. Next is...     

> __< k​4r4b3y:karapara.net >__ this banning/unbanning process looks arbitrary.     

> __< nioCat >__ plowsof: don't make me go to red it please      

> __< p​lowsof:matrix.org >__ we can circle back to the juicy stuff later on, my perception is terrible.. i forgot he was banned myself , can be resolved     

> __< p​lowsof:matrix.org >__ 5. [CCS updates](https://ccs.getmonero.org/)     

> __< p​lowsof:matrix.org >__ - Animated Videos: Nodes script [gitlab comment](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/412#note_23203) - VostoEmisio          

> __< p​lowsof:matrix.org >__     - [Boog900](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/405#note_23183)      

> __< p​lowsof:matrix.org >__     - [plowsof](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/418#note_23209)     

> __< p​lowsof:matrix.org >__ matrix users sorry for unclickable ehh.. animated videos have received some feedback already in here, vostoemisio is probably going ahead with the script linked above, and boog900 and plowsof have given updates for their ccs' this past week     

> __< r​ucknium:monero.social >__ I think I will be able to submit my proposed new decoy distributions for OSPEAD milestone 2 by January 31. More realistic is first week of February (I set an internal deadline of Jan 31 but I forgot to tell everyone who was contributing data, so we may be later 😅)     

> __< p​lowsof:matrix.org >__ if think the eventual multisig signers for the ccs wallet should be a GH issue in itself, but so far, gingeropolous and jwinterm have publicly agreed to offer themselves up. them both being in the US was raised as a concern so other signers should be from [another place] ?     

> __< p​lowsof:matrix.org >__ thanks for the update Rucknium     

> __< ofrnxmr >__ Lol     

> __< ofrnxmr >__ Next     

> __< ofrnxmr >__ Ty ruck     

> __< p​lowsof:matrix.org >__ onto the ideas then     

> __< p​lowsof:matrix.org >__ a. [hinto-janai - full-time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422)     

> __< p​lowsof:matrix.org >__ most recent change diffs can be seen here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422/diffs?diff_id=6494&start_sha=4598b1281af59f5a282720edd9f94ba06f8fa823     

> __< p​lowsof:matrix.org >__ after my comment initiated some feedback / responses https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422#note_23204     

> __< p​lowsof:matrix.org >__ the proposal now has 5 updoots     

> __< ofrnxmr >__ Ill reserve my comments and leave my vote out     

> __< k​ayabanerve:matrix.org >__ Also in monero-research and nwlb     

> __< k​ayabanerve:matrix.org >__ I support hinto's CCS     

> __< ofrnxmr >__ lgtm     

> __< p​lowsof:matrix.org >__ "Only people who care about this proposal are 1) re-write it in rust people 2) other cuprate devs and 3) kayabanerve (who wants a rust node that his serai dex can fall back on) / obtain pull requests from cuprate devs."     

> __< p​lowsof:matrix.org >__ most of this has been responded / rebutted in the comments, what do you think about number 3 kayabanerve     

> __< ofrnxmr >__ Thats an unfair comment     

> __< k​ayabanerve:matrix.org >__ Where is that quote from     

> __< p​lowsof:matrix.org >__ myself / comment     

> __< p​lowsof:matrix.org >__ we we tangentially funding serai dex without any kickbacks like we get from haveno (soon)?     

> __< jwinterm >__ it seems a bit pricey just for the database piece and then it's not clear how much further one person hours would be needed to finish cuprate I guess     

> __< k​ayabanerve:matrix.org >__ I wanted monero-serai as a more functional Rust library for Monero. It has revealed multiple bugs in Monero now and Seraphis related work upcoming.     

> __< ofrnxmr >__ No. Were funding cuprate      

> __< k​ayabanerve:matrix.org >__ Another node, in any language, will help identify bugs with the protocol and help standardize it.     

> __< ofrnxmr >__ and haveno kickbacks? Your believe erc's scamming ass?     

> __< p​lowsof:matrix.org >__ whats wrong with LMDB hyc? why do cuprate have to redesign something     

> __< k​ayabanerve:matrix.org >__ I have a CoI due to the fact I receive PRs. I have a personal preference for the usage of Rust. I don't want a Rust node though. I want another node.     

> __< b​oog900:monero.social >__ We are using LMDB ....     

> __< ofrnxmr >__ Haveno is a private, for profit project      

> __< k​ayabanerve:matrix.org >__ For Bitcoin, I'm considering a JS and/or Go node re: client diversity which proves your #3 is invalid.     

> __< ofrnxmr >__ LMDB has some problems, but thats coming up     

> __< ofrnxmr >__ Hinto doesnt seem to be working ON lmdb, just around it     

> __< k​ayabanerve:matrix.org >__ FYI, the fact Monero will generate seeds it can't read back was a byproduct of monero-serai. Then, fingerprints in the rewritten RingCt wallet under koe's Seraphis work were identified.     

> __< k​ayabanerve:matrix.org >__ Those are the most recent things I can chime in on.     

> __< k​ayabanerve:matrix.org >__ Polyseed was also so broken, unfortunately :/     

> __< p​lowsof:matrix.org >__ the 5 voters (mostly other cuprate devs want it merged) , im not jumping to say merge atm nor do i want to close     

> __< k​ayabanerve:matrix.org >__ Oh. monero-serai also caused a fingerprint fix in Monero itself re: sweeps having different fees, in extreme theory.     

> __< k​ayabanerve:matrix.org >__ I'm not a Cuprate dev and advocate for it for the health and diversity of the Monero protocol.     

> __< p​lowsof:matrix.org >__ its not a 3 month investment for the community, its more for several years     

> __< p​lowsof:matrix.org >__ we can fund fixes in the monero protocol without funding cuprate     

> __< ofrnxmr >__ One thing to confirm, this doesnt effect gupax right     

> __< k​4r4b3y:karapara.net >__ work on cuprate seems to have unearthed one or two issues in monero protocol, though. without that work, how would you know that you needed to fund fixes?     

> __< b​oog900:monero.social >__ my work on Cuprate allows me to spot issues, I would be less likely to find them just be looking at the code     

> __< ofrnxmr >__ Tobtoht can you comment      

> __< k​ayabanerve:matrix.org >__ It also helps detect accidental protocol changes.     

> __< r​ucknium:monero.social >__ I like this proposal, but I don't feel strongly about it. AFAIK, the database work probably won't uncover any subtle Monero bugs....but cuprate won't work without a database, so it's necessary for overall cuprate development.     

> __< ofrnxmr >__ Tobtoht is the best example     

> __< p​lowsof:matrix.org >__ i echo jwinterms comment about it being pricey for just the database part     

> __< ofrnxmr >__ We fund feather     

> __< ofrnxmr >__ I echo the pricy part too     

> __< ofrnxmr >__ A bit way too pricy lol     

> __< ofrnxmr >__ But im not voting.     

> __< r​ucknium:monero.social >__ If cuprate can reduce or eliminate database corruption and/or pull output public keys faster to prepare for possible larger ring sizes, then that would be wonderful.     

> __< k​ayabanerve:matrix.org >__ Back when I was doing my own crypto, I impl'd it in Nim (a thing of the time) and Python to ensure I didn't add impl-specific bugs.     

> __< k​ayabanerve:matrix.org >__ I even made sure they didn't share libs (barring RandomX, which I didn't re-impl).     

> __< p​lowsof:matrix.org >__ any other concerns to be put up for rebuttal on this?     

> __< k​ayabanerve:matrix.org >__ You stare at the abyss. FCMPs stare back.     

> __< k​ayabanerve:matrix.org >__ Roll for perception to see if you'll have a revelation.     

> __< k​ayabanerve:matrix.org >__ :p     

> __< r​ucknium:monero.social >__ FCMP is still under development and we don't know if it will work     

> __< k​ayabanerve:matrix.org >__ I'd support any node in any other language if I believed the team competent, as I do here.     

> __< ofrnxmr >__ I support the node impl     

> __< p​lowsof:matrix.org >__ i think we have a full picture now of hintos proposal? wait for hintos response to this meeting then move forward with a decision?     

> __< ofrnxmr >__ it doesnt appear to be 8hrs a day or whatever its priced at      

> __< p​lowsof:matrix.org >__ lets move on     

> __< b​oog900:monero.social >__ The original CCS was for 3 months with the database being to goal but the potential to move onto other things     

> __< p​lowsof:matrix.org >__ b. [0xfffc-2024Q1-(3 months, February, March, April, 2024)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/429)     

> __< b​oog900:monero.social >__ so should hinto change it back?     

> __< b​oog900:monero.social >__ because I feel we are just finding more and more things to delay this proposal     

> __< ofrnxmr >__ I blame my ban on your delay     

> __< ofrnxmr >__ Was on a roll getting shit done. Lol. Sorry     

> __< ofrnxmr >__ Random tuesday merge coming soon      

> __< p​lowsof:matrix.org >__ a few concerns about price where raised in this meeting     

> __< p​lowsof:matrix.org >__ the proposal was in a haystack, my comment has kick started engagement for the proposal     

> __< p​lowsof:matrix.org >__ first time 0xFFFC has been mentioned in a meeting , thoughts?     

> __< p​lowsof:matrix.org >__ has support from selsta/hyc (those mentioned in the proposal)     

> __< ofrnxmr >__ 0xfffc has been working on repo with selsta for a couple months now     

> __< ofrnxmr >__ Is working with hyc on actually fixing lmdb issues     

> __< r​ucknium:monero.social >__ C++ work on the protocol is technical and hard to evaluate by people who have not worked on the protocol. The people who have worked on the protocol support 0xfffc's proposal, so +1 merge from me.     

> __< ofrnxmr >__ +1 from me     

> __< p​lowsof:matrix.org >__ also the price is ridiculously low 15xmr/mth * 3 months = 45xmr     

> __< ofrnxmr >__ i dont see anyone else working on lmdb and we can use more devs. rates are more than acceptable and is already working      

> __< p​lowsof:matrix.org >__ +merge from me     

> __< ofrnxmr >__ https://bugs.openldap.org/show_bug.cgi?id=9378#c14      

> __< ofrnxmr >__ example of some of the work done with hyc     

> __< p​lowsof:matrix.org >__ thanks for linking     

> __< p​lowsof:matrix.org >__ thanks for attending 0xFFFC     

> __< ofrnxmr >__ Also yesterday, during review. Spotted a better fix and helped jeffro256 fix tobtohts old pr     

> __< 0​xfffc:matrix.org >__ My pleasure, to be part of Monero community.     

> __< p​lowsof:matrix.org >__ moving on with a few mins left     

> __< nioCat >__ +1     

> __< p​lowsof:matrix.org >__ c. [escapethe3RA Monero Observer maintenance (2024 Q1)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/430)     

> __< p​lowsof:matrix.org >__ most recent update from his previous ccs: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/414#note_23123     

> __< ofrnxmr >__ +1. We just did this retroactive. This is the current one, right?     

> __< p​lowsof:matrix.org >__ yes     

> __< r​ucknium:monero.social >__ +1 Monero Observer     

> __< p​lowsof:matrix.org >__ +1 consistency and quality     

> __< p​lowsof:matrix.org >__ if anyone would like to share an update of what theyre working on / wish to see worked on please mention it     

> __< ofrnxmr >__ BSX     

> __< ofrnxmr >__ i assume their install instructions are why liquidity is so bad. so going to fix.     

> __< k​4r4b3y:karapara.net >__ repo.getmonero.org was getting an .onion URL. Is this still the case?     

> __< r​ucknium:monero.social >__ I have seen a couple of recent research papers using RINO's testnet/stagenet XMR faucet for research. Thanks, RINO.     

> __< ofrnxmr >__ Yeah.      

> __< p​lowsof:matrix.org >__ Weblate server status - the volunteer back end admin has identified a need for better hardware, which has been provided from general fund costs. they know the path to completion, just need time to complete it. xmrscott has also volunteered to look into weblate     

> __< ofrnxmr >__ Look into it? Lol     

> __< p​lowsof:matrix.org >__ same for the CCS onion url - notes have been found .. they know how it all works again.. and just need a further chance to complete it , soon(tm) , much appreciated     

> __< ofrnxmr >__ So does that mean TL ccs will come back?     

> __< ofrnxmr >__ K good meeting. Will ask more questions later     

> __< p​lowsof:matrix.org >__ look into it as in, do more than what i did (type weblate into a search engine and be confused) - where files need to go to/from / driving the issue forward     

> __< p​lowsof:matrix.org >__ thanks all for attending 🙏     

> __< p​lowsof:matrix.org >__ is there anyone able to moderate the events meeting in #monero-events:monero.social ?     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2024-01-13T23:21:26+00:00
- Closed at: 2024-01-25T11:46:17+00:00
