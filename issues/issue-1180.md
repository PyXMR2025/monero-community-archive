---
title: 'Monero Community Workgroup Meeting: April 12th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1180
author: plowsof
assignees: []
labels: []
created_at: '2025-03-30T01:07:19+00:00'
updated_at: '2025-05-20T21:30:47+00:00'
type: issue
status: closed
closed_at: '2025-05-20T21:30:47+00:00'
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
     - recommended update [v0.18.4.0](https://www.getmonero.org/2025/04/05/monero-0.18.4.0-released.html) released
     - [FCMP++ contest](https://www.getmonero.org/2025/04/05/fcmp++-contest.html) submissions open April 28th
     - _"FeatherWallet  rebased on top of j-berman's fcmp++ staging branch and set up a private testnet. Mining works. Tx construction isn't fully working yet with carrot changes. Looking forward to shipping a beta as soon as public testnet goes live."_ - tobtoht [Image](https://github.com/user-attachments/assets/52f008c2-36ec-453e-970a-baf1d004af28)  
     - [cuprated update](https://www.reddit.com/r/Monero/comments/1jvfrgl/cuprate_v002_released/) via hinto-janaiyo
     - [Monerokon Tickets](https://www.monerokon.org/) for sale!
     - https://AXESwap.net an $XMR 🔄 $BCH atomic swap web-app [X](https://x.com/mainnet_pat/status/1907800302071296186) / [xcancel](https://x.com/mainnet_pat/status/1907800302071296186) - mainnet pat
     - [Monfluo new tag](https://www.reddit.com/r/Monero/comments/1ju68ry/monfluo_v070/) via Revuo
     - Coin which added 'Exchange addresses' de-listed from Binance [Xcancel](https://x.com/monerobull/status/1909517550020370711) via monerobull
     - [Kabus](https://github.com/sukunetsiz/kabus) - open source monero market platform (currently none multisig, you send funds to the platforms wallet) 
     News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)    
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)    
  b. [Monero Browser Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555)    
  c. [Revuo Monero Maintenance (2025 Q2)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/559) Merged and funded
  d. [New Year's resolutions](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/537) Merged
  e. [ANONERO: remove self imposed deadline](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/569) /  [Remove deadline](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/573) 
  f. [Haveno iOS and Android App](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/570)
  g. [tobtoht full-time feather + core development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/571)
  h. [j-berman full-time development (4 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/574)    

5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2025](https://Monerokon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1178)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2025-05-20T20:51:20+00:00
> **\<plowsof\>** meeting time https://github.com/monero-project/meta/issues/1180      
    
> **\<plowsof\>** greetings hi      
    
> **\<ofrnxmr\>** 👋     
    
> **\<msvb-lab\>** Hello.     
    
> **\<s​pirobel:kernal.eu\>** hi     
    
> **\<plowsof\>** recommended update [v0.18.4.0](https://www.getmonero.org/2025/04/05/monero-0.18.4.0-released.html) released , Kevin McSheehan reported a p2p crash vulnerability, which sadly made the release notes after site was deployed https://github.com/monero-project/monero-site/commit/3d6ac52ef83d7063d771bd21250dda3f913ca863     
    
> **\<ofrnxmr\>** We'll get site redeployed shortly     
    
> **\<plowsof\>** tobtoht is sadly unable to make this meeting today. i hear he was building transactions on fcmp++ testnet in featherwallet :-o      
    
> **\<ofrnxmr\>** Was not added to release notes because the vulnerability was a nasty one. Had to notify mining pools etc before it was disclosed      
    
> **\<plowsof\>** 👍 i did personally send a support email to all the pools who had not yet updates after ofrnxmr requested. not sure if they have updated though      
    
> **\<ofrnxmr\>** anyway, if you havent updated to 18.4.0, do so.     
    
> **\<ofrnxmr\>** At least 1 of the top 3 pools have updates      
    
> **\<NorrinRadd\>** Hi      
    
> **\<plowsof\>** j-berman and jeffro256 have announced the competition entry date https://www.getmonero.org/2025/04/05/fcmp++-contest.html this will ideally reduce transaction creation from several minutes to not several minutes :D     
    
> **\<ofrnxmr\>** I read somewhere that it should be ~3seconds pre-competition      
    
> **\<nioc\>** should be from <3 seconds to half of that     
    
> **\<plowsof\>** ok that is a relief      
    
> **\<nioc\>** from MRL meeting     
    
> **\<plowsof\>** back links https://github.com/monero-project/meta/issues/1186#issuecomment-2798092566 , thank you      
    
> **\<ofrnxmr\>** https://github.com/monero-project/meta/issues/1184 looking to add an "official" / reference for sharing node credentials via qr code      
    
> **\<ofrnxmr\>** Currently, i think nodo and cake are the only parties using qrs to share nodes (maybe umbrel), but i want to standarize it with similar syntax to existing uris     
    
> **\<plowsof\>** 👍 nice idea , instead o filling in several boxes like a peasant      
    
> **\<ofrnxmr\>** We've had the ability to share wifi via qr/nfc for like 10yrs     
    
> **\<plowsof\>** perhaps monerokon attendees can use the node qr to connect their wallets to  the kon's node(s) [Monerokon Tickets](https://www.monerokon.org/) for sale!     
    
> **\<plowsof\>**  [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)         
    
> **\<plowsof\>** 4. [CCS updates](https://ccs.getmonero.org/)        
    
> **\<plowsof\>** oops, any other highlights people want to bring up*     
    
> **\<plowsof\>** Coin which added 'Exchange addresses' de-listed from Binance [Xcancel](https://x.com/monerobull/status/1909517550020370711) via monerobull      
    
> **\<ofrnxmr\>** Yeah, thats what monerotopia did     
    
> **\<ofrnxmr\>** (used nodo to allow merchants to scan the qr)     
    
> **\<ofrnxmr\>** Merchants and attendees     
    
> **\<plowsof\>** 👍     
    
> **\<ofrnxmr\>** "coin" are we referring to firo?     
    
> **\<plowsof\>** correct      
    
> **\<ofrnxmr\>** also to note that they have fully transparent addresses     
    
> **\<plowsof\>** Following the completion of the standard delisting due diligence process, Binance will delist BADGER, BAL, BETA, CREAM, CTXC, ELF, FIRO, HARD, NULS, PROS, SNT, TROY, UFT and VIDT on 2025-04-16.     
    
> **\<ofrnxmr\>** They rolled over, played dead, and did what they were told. and then got discarded like they were garbage. Tldr: lol     
    
> **\<plowsof\>** ok lets move on to ccs ideas      
    
> **\<ofrnxmr\>** its 420. Good idea     
    
> **\<plowsof\>** [Monfluo new tag](https://www.reddit.com/r/Monero/comments/1ju68ry/monfluo_v070/) via Revuo     
    
> **\<plowsof\>**   a. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)         
    
> **\<plowsof\>** https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_29498     
    
> **\<plowsof\>** plugin migration complete ^      
    
> **\<plowsof\>** i thought monero-lws milestones where highly contested , i was wrong on that      
    
> **\<ofrnxmr\>** I feel like they dont intend to address any comments.      
    
> **\<s​pirobel:kernal.eu\>** wasnt the consensus the last time to make some changes and then merge?     
    
> **\<s​pirobel:kernal.eu\>** but the changes didnt happen?     
    
> **\<ofrnxmr\>** You werent "wrong". More that nobody outright said to remove them     
    
> **\<ofrnxmr\>** Yeah, changes didnt happen     
    
> **\<ofrnxmr\>** Their lws plans conflict with other oarts of the ccs     
    
> **\<d​everickapollo:matrix.org\>** What changes?     
    
> **\<d​everickapollo:matrix.org\>** M1 is good     
    
> **\<d​everickapollo:matrix.org\>** Each of those deliverables should remain     
    
> **\<s​pirobel:kernal.eu\>** ofrnxmr made some suggestions     
    
> **\<d​everickapollo:matrix.org\>** Sure - let’s be clear what change.     
    
> **\<d​everickapollo:matrix.org\>** Each of those deliverables represents work we’re doing at this time and should continue. Which deliverable should not stay     
    
> **\<ofrnxmr\>** Migrating the plugin takes all of 120 seconds     
    
> **\<plowsof\>** ofrnxmrs suggestion https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#note_29353 (not sure if changed)      
    
> **\<ofrnxmr\>** Quite literally like 5 clicks in web browser, and 3 command in git     
    
> **\<d​everickapollo:matrix.org\>** It clearly hasn’t. This proposal has been open 3 months. It took 2 months for you to even process BTCPay wasn’t continuing to host.     
    
> **\<ofrnxmr\>** Hasnt what? Taken 120 seconds?     
    
> **\<n​apoly:matrix.org\>** i could do it in 5s fyi     
    
> **\<plowsof\>** will monero-plugin need their own build server?      
    
> **\<ofrnxmr\>** right      
    
> **\<d​everickapollo:matrix.org\>** No     
    
> **\<d​everickapollo:matrix.org\>** We are using GitHub actions and pushing to BTCPay     
    
> **\<d​everickapollo:matrix.org\>** They have a build server     
    
> **\<ofrnxmr\>** plowsof my suggestions havent changes. They dont cut much out of the deliverables either. Just reworded to be accurate (w/o duplication and non-work)     
    
> **\<plowsof\>** and that wouldnt require and change in total work per milestone?     
    
> **\<plowsof\>** i mean total effort would remain the same      
    
> **\<ofrnxmr\>** yeah, less than advertised      
    
> **\<ofrnxmr\>** As in, theres no work involved in forking a repo, dockerizing lws, or creating remote node support (that already exists)     
    
> **\<d​everickapollo:matrix.org\>** Are we skipping unit test? That is a chunk of work that doesn’t exist 😂     
    
> **\<plowsof\>** so for example, funds have been set aside for dockerising monero-lws in milestone 3 https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538#milestone-3-minimum-viable-product-mvp-for-multiwallet-support     
    
> **\<plowsof\>** this is done? and we're paying for duplicated effort. and there are other examples of this? why can;t this be fixed?      
    
> **\<d​everickapollo:matrix.org\>** No - that says if not available     
    
> **\<plowsof\>** fix it?     
    
> **\<d​everickapollo:matrix.org\>** Meaning we have been talking with vtnerd and intend to leverage what is available once we get there     
    
> **\<d​everickapollo:matrix.org\>** If it’s not there, we contribute upstream     
    
> **\<d​everickapollo:matrix.org\>** What’s wrong with this?     
    
> **\<ofrnxmr\>** So are you sending the funds to vtnerd?     
    
> **\<ofrnxmr\>** Magic has an lws docker as well     
    
> **\<n​apoly:matrix.org\>** there has to be some adjustments for us....     
    
> **\<plowsof\>** just one example of duplication at a glance. the docker lws issue was mentioned last meeting too but nothing changed reg that      
    
> **\<plowsof\>** 1 small example :-S why cant ya just fix it D:     
    
> **\<d​everickapollo:matrix.org\>** Again, leveraging what is available. It was added to ensure we addressed a gap in implementation if it exists     
    
> **\<d​everickapollo:matrix.org\>** We sure can remove it 😂 what does it change?     
    
> **\<plowsof\>** its been 9 months since the proposal was opened please adjust for reality     
    
> **\<ofrnxmr\>** "if not available" implies that youll create an unofficisl one if there isnt an official one. But there exists an unofficial one already (magics), and vtnerd has already expressed that he'd do an "official" one     
    
> **\<plowsof\>** ofrnxmr what does it change? are you requesting a reduction in advertised work and total funcing request?     
    
> **\<plowsof\>** or will monero-plugin team fill in the gaps elsewhere to keep effort the same     
    
> **\<n​apoly:matrix.org\>** for real are you suggesting that we should use some magic container that is unofficial and can contain malicious parts?... 💀     
    
> **\<plowsof\>** are magic malicious     
    
> **\<plowsof\>** the ccs funnel tens of thousands of montero to them , this is a serious accusation we need to investigate      
    
> **\<ofrnxmr\>** What "monero" docker are you using?     
    
> **\<d​everickapollo:matrix.org\>** BTCpay until we shift     
    
> **\<d​everickapollo:matrix.org\>** Do we need a separate meeting? We do this every two weeks     
    
> **\<d​everickapollo:matrix.org\>** This is clown shit at this point     
    
> **\<s​pirobel:kernal.eu\>** okay moving on     
    
> **\<ofrnxmr\>** well, your roadmap conflicts with itself      
    
> **\<s​pirobel:kernal.eu\>** almost 1 am here     
    
> **\<d​everickapollo:matrix.org\>** Have we refined any other work like this     
    
> **\<plowsof\>**   b. [Monero Browser Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555)         
    
> **\<s​pirobel:kernal.eu\>** woodser made some great comments since the last session.     
    
> **\<ofrnxmr\>** Are you addong remote node support (exists already), are you reviewing remote node support (??), or are you running an lws server snd monerod locally     
    
> **\<plowsof\>** spirobel linked woodsers comments in this comment https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/555#note_29394     
    
> **\<s​pirobel:kernal.eu\>** seems like people are seeing the value in this. would be grateful for a merge after this 4th session.     
    
> **\<n​apoly:matrix.org\>** are you telling us the remote note wont need any more work?.. 💀     
    
> **\<ofrnxmr\>** Are you telling me that lws is intended to use remote nodes?     
    
> **\<n​apoly:matrix.org\>** i told u there will be 2 options     
    
> **\<ofrnxmr\>** and the former already uses remote nodes, single wallet instance, and wallet-rpc.      
    
> **\<d​everickapollo:matrix.org\>** Are we questioning the intention of a previous bounty here?     
    
> **\<ofrnxmr\>** no?     
    
> **\<plowsof\>** spirobel is your plugin -optional- for tor browser? or specifically / only for the tor browser?      
    
> **\<d​everickapollo:matrix.org\>** This wasn’t a feature Napoly submitted - it was one he implemented and has been waiting to merge.     
    
> **\<ofrnxmr\>** What youre referring to is a gui to define the node     
    
> **\<ofrnxmr\>** And is proposed is my suggested milestone 1     
    
> **\<ofrnxmr\>** Thats not remote node support, thats a gui to set the variable (which was done incorrectly in the pr*     
    
> **\<s​pirobel:kernal.eu\>** plowsof: it will work with all browsers     
    
> **\<plowsof\>** sprirobel i can better say is the browser wallet tied to any specific web browser? ok thank you for clarifying.      
    
> **\<s​pirobel:kernal.eu\>** no its not tied to a specific browser     
    
> **\<n​apoly:matrix.org\>** see.. so it still requires some work     
    
> **\<plowsof\>** this is also an example of suggestions being made and spirobel clarifying that they do not need to be made :D     
    
> **\<ofrnxmr\>** I never implies that the gui should be dropped from milestones @napoly     
    
> **\<plowsof\>** tor suggesting no 3rd party plugins should be used is not a blocker though     
    
> **\<ofrnxmr\>** "M1: Finish GUI for remote node configuration started here.. making sure to address this comment" napoly     
    
> **\<ofrnxmr\>** sorry for interruptions, can come back after     
    
> **\<s​pirobel:kernal.eu\>** plowsof: tor makes this suggestion because extensions could damage user privacy.  In this case it will enhance user privacy and help people keep their identity separate. I can add documentation to this specific part if that can help alleviate concerns.     
    
> **\<plowsof\>** initially the total price of spirobels proposal raised some concerns but it was clarified as being a bargain. tor being against plugins is not a blocker as the browser wallet is universal. a suggestion to drop "  - name: Multisig companion app + escrow library" as a milestone was made, but spirobel says it can not be.     
    
> **\<s​pirobel:kernal.eu\>** the tor browser has noscript preinstalled as well.     
    
> **\<plowsof\>** so what is to be done (:      
    
> **\<n​apoly:matrix.org\>** I'm not sure what u want from us.. I do value ur criticism.. Deverick did change the proposal to your liking.. but that wasn't enough.     
    
> **\<NorrinRadd\>** plowsof why can't any of the milestones be dropped?      
    
> **\<s​pirobel:kernal.eu\>** the multisig companion app is important because it will help people get over their concerns regarding browser wallet security. It makes sense to do this all in one package, because all of these pieces are related.     
    
> **\<plowsof\>** spirobel said milestone 3 is required and can not be dropped , none negotiable      
    
> **\<plowsof\>** am i foolish for thinking, well why not? and then a follow up proposal for this? likely      
    
> **\<ofrnxmr\>** Probably an easier merge if its split up into separate ccs     
    
> **\<NorrinRadd\>** imo milestone 2 is useful, could help with adoption. i don't believe the claims about increasing privacy or most of the other claims.      
    
> **\<s​pirobel:kernal.eu\>** It is better this way. Because it should be tightly integrated into the experience of using the wallet from the beginning.     
    
> **\<s​pirobel:kernal.eu\>** also this is the 4th session.     
    
> **\<NorrinRadd\>** isn't multi-sig about to change significantly with fcmp++?      
    
> **\<s​pirobel:kernal.eu\>** this was brought up so late     
    
> **\<NorrinRadd\>** so work done there will not be useful for long?      
    
> **\<s​pirobel:kernal.eu\>** no the underlying tech stays the same     
    
> **\<s​pirobel:kernal.eu\>** we just paid for the audit     
    
> **\<s​pirobel:kernal.eu\>** which will be finished soon     
    
> **\<s​pirobel:kernal.eu\>** I don't want to split this up. seriously. It is tightly related. Also because it creates a forcing function for the library design     
    
> **\<r​4v3r23:monero.social\>** so what. youre not entitled to a merge, and there will be 1000 sessions if needed     
    
> **\<NorrinRadd\>** J0J0XMR suggested removing milestones a month ago      
    
> **\<s​pirobel:kernal.eu\>** why dont you guys focus on your stuff. I spent so much time on this. you voiced your concerns. You through mud     
    
> **\<s​pirobel:kernal.eu\>** *threw     
    
> **\<s​pirobel:kernal.eu\>** and now just leave     
    
> **\<s​pirobel:kernal.eu\>** stop nitpicking     
    
> **\<s​pirobel:kernal.eu\>** you gave your 3 downvotes     
    
> **\<s​pirobel:kernal.eu\>** now leave     
    
> **\<r​4v3r23:monero.social\>** browser wallet ccs is an obvious cash grab     
    
> **\<s​pirobel:kernal.eu\>** its enough     
    
> **\<r​4v3r23:monero.social\>** i vote close     
    
> **\<s​pirobel:kernal.eu\>** anonero is an ovious cash grab     
    
> **\<r​4v3r23:monero.social\>** insanely priced and no clear objectives     
    
> **\<r​4v3r23:monero.social\>** next     
    
> **\<s​pirobel:kernal.eu\>** I open sourced the mvp too btw.     
    
> **\<s​pirobel:kernal.eu\>** crazy insulting to call this  a cash grab     
    
> **\<s​pirobel:kernal.eu\>** why do we allow this to be sabotaged by these people ?     
    
> **\<s​pirobel:kernal.eu\>** haveno mobile app is a cash grab too     
    
> **\<r​4v3r23:monero.social\>** no, just browser wallet     
    
> **\<plowsof\>** moving on for now then      
    
> **\<plowsof\>** e. [ANONERO: remove self imposed deadline](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/569)      
    
> **\<r​4v3r23:monero.social\>** i think ive said everything i needed to say in here a few days ago     
    
> **\<s​pirobel:kernal.eu\>** dont remove the deadline     
    
> **\<r​4v3r23:monero.social\>** ofrn made some changes to the erge request that ive accepted     
    
> **\<s​pirobel:kernal.eu\>** didnt deliver     
    
> **\<plowsof\>** that would be [Remove deadline](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/573)       
    
> **\<s​pirobel:kernal.eu\>** you are not entitled to  a  merge     
    
> **\<ofrnxmr\>** +1 . That deadline is like 2 weeks from now.      
    
> **\<r​4v3r23:monero.social\>** yes     
    
> **\<s​pirobel:kernal.eu\>** yeah the funds should be redistributed     
    
> **\<plowsof\>** merge 569     
    
> **\<s​pirobel:kernal.eu\>** not entitled to a merge     
    
> **\<r​4v3r23:monero.social\>** idk what the merge ppeline issue is on 569     
    
> **\<plowsof\>** ignore pipeline for these edits     
    
> **\<r​4v3r23:monero.social\>** anyway, work on NERO has already started n new branch on git     
    
> **\<plowsof\>** as for 573 - adding the notice -before- completing the payout of milestone 2 was an oversight on my part, i apologise to the ANONERO team / r4v3r23 . payout for milestone 2 was expedited to reflect recent milestone completion.      
    
> **\<r​4v3r23:monero.social\>** thanks. i just wanna complete this without any needless red tape     
    
> **\<plowsof\>** moving on as we're over      
    
> **\<plowsof\>**   f. [Haveno iOS and Android App](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/570)     
    
> **\<s​pirobel:kernal.eu\>** ofrnxmr: I provided a decent reason for why this shouldnt be split up. JOJOXMR didnt even read the proposal properly when he left his downvote     
    
> **\<s​pirobel:kernal.eu\>** splitting this up makes no sense     
    
> **\<ofrnxmr\>** Theres another haveno app in the wild     
    
> **\<s​pirobel:kernal.eu\>** and is just further obstruction by the 3 people that already gave their downvotes     
    
> **\<ofrnxmr\>** At this point, i think _any_ claim for haveno ui/app shit should be retroactive      
    
> **\<NorrinRadd\>** ofrnxmr: i went through that repo. i couldn't find any actual logic in that code      
    
> **\<NorrinRadd\>** that .net project      
    
> **\<NorrinRadd\>** what do you mean by "retroactive"?     
    
> **\<ofrnxmr\>** I havent checked, but i stand by my statement about haveno ui/app stuff being retroactive     
    
> **\<plowsof\>** are you referring to the LootSpam bounty comment(s)? https://bounties.monero.social/posts/126/37-175m-building-an-open-source-android-app-for-haveno-dex      
    
> **\<plowsof\>** after the kewbit situation - finding a team that is qualified to do a paid / trusted review of the submitted work seems essential      
    
> **\<NorrinRadd\>** monerobull, boldsuck, and woodser are capable      
    
> **\<NorrinRadd\>** i worked with woodser to get going with the api      
    
> **\<m​onerobull:matrix.org\>** I can't really review code     
    
> **\<NorrinRadd\>** I've been doing builds of all his haveno related repos, contributing to most of them, so he's aware that i know that codebase fairly well      
    
> **\<plowsof\>** do not down play your vibe skills      
    
> **\<NorrinRadd\>** would have done the cloned offers feature but he beat me to it      
    
> **\<s​pirobel:kernal.eu\>** I could review it.     
    
> **\<msvb-lab\>** Good meeting, thanks everyone.     
    
> **\<plowsof\>** thanks for attending msvb-lab      
    
> **\<NorrinRadd\>** monerobull yeah i meant at the least, testing      
    
> **\<ofrnxmr\>** we have a few more proposals to get to      
    
> **\<plowsof\>** this is the lootspam attempt : https://github.com/LootSpam/Building-an-Open-Source-Android-App-for-Haveno-Dex/      
    
> **\<ofrnxmr\>** (We should probably start with the easy /lowest discussion proposals)     
    
> **\<plowsof\>** is it garbage? AI slop? legit? i have no idea      
    
> **\<plowsof\>**   g. [tobtoht full-time feather + core development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/571)     
    
> **\<plowsof\>** tobtoht can not make it today but sent his greetings , featherwallet     
    
> **\<NorrinRadd\>** real quick, is the ability to use haveno on the go & still have offers live / available when a phone OS closes the app, is that useful for the community?      
    
> **\<ofrnxmr\>** Merge     
    
> **\<plowsof\>** thanks for leaving feedback already everyone     
    
> **\<plowsof\>**   h. [j-berman full-time development (4 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/574)         
    
> **\<ofrnxmr\>** Merge     
    
> **\<r​4v3r23:monero.social\>** auto merge last 2     
    
> **\<plowsof\>** thanks all for attending      
    
> **\<NorrinRadd\>** ofrnxmr what do you mean by "retroactive"?      
    
> **\<o​frnxmr:xmr.mx\>** I mean, like a bounty.     
    
> **\<o​frnxmr:xmr.mx\>** Present finished product -> get paid     
    
> **\<NorrinRadd\>** oh i agree, the proposal says that, each milestone is value for value      
    
> **\<o​frnxmr:xmr.mx\>** Unless your ccs is absolutely _not_ trying to claim the already-raised haveno funds     
    
> **\<NorrinRadd\>** idc where the funds come from      
    
> **\<NorrinRadd\>** there's no upfront payment anywhere in there      
    
> **\<o​frnxmr:xmr.mx\>** are you looking to raise funds from 0?     
    
> **\<NorrinRadd\>** absolutely don't care lol      
    
> **\<o​frnxmr:xmr.mx\>** Example: kewbit raised 0xmr. The funds for his ccs were repurposed from existing pool of haveno funds. If your ccs is raising its own funds, then this doesnt add any risk to the leftover funds from prior haveno ccs     
    
> **\<NorrinRadd\>** I didnt see when that happened. I don't know who makes that decision.      
    
> **\<NorrinRadd\>** I'm not aware that it's me.      
    
> **\<s​pirobel:kernal.eu\>** First people complain about the supposed insecurity of browser wallets. Then I come up with a plan to make everything multisig by default, so multiple devices have to be compromised. And people still complain and want to split it up. It is just annoying.     
    
> **\<r​4v3r23:monero.social\>** lmfao multisig browseer wallet for muh mass adaption     
    
> **\<r​4v3r23:monero.social\>** for a con thats essentally delisted     
    
> **\<r​4v3r23:monero.social\>** for a coin thats essentally delisted     
    
> **\<NorrinRadd\>** i did some searching on browser wallet security and didn't find anything alarming, hence my change in stance. i'm ok with milestone 2. the others seem pointless.      
    
> **\<r​4v3r23:monero.social\>** so easy oppressed women in afghanistan can use it!     
    
> **\<s​pirobel:kernal.eu\>** if these two have veto rights in this project I am just going to admit defeat and work on something else.     
    
> **\<s​pirobel:kernal.eu\>** leads to burn out having to "debate" the same nonsense over and over every two weeks until 3 am in the morning     
    
> **\<r​4v3r23:monero.social\>** or maybe its just a retarded overengineered idea to solve.. checks notes.. copy/pasting an address  

# Action History
- Created by: plowsof | 2025-03-30T01:07:19+00:00
- Closed at: 2025-05-20T21:30:47+00:00
