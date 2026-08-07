---
title: 'Monero Community Workgroup Meeting: Sat, 2026-05-30 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1398
author: nahuhh
assignees: []
labels: []
created_at: '2026-05-30T04:25:34+00:00'
updated_at: '2026-08-06T20:11:10+00:00'
type: issue
status: closed
closed_at: '2026-08-06T20:11:10+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: ofrnxmr

Please reach out in advance of the meeting if you would like to propose an agenda item.


Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Revuo Monero](https://revuo-xmr.com/) - [This week in Monero TWIM](https://cyphergoat.com/this-week-in-monero)  
MoneroKon next weekend!  
4. CCS proposals  
  a. [MRL] Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)    
  b. Marko Pohlo - [Cuprate Consensus-Rule Differential Fuzzing](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676)    
  c. SyntheticBird - [Cuprate Address Book, Reproducible Build and Supply Chain Security 3 months](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/678)  
  d. r4v3r23 - [ANONERO Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)  
  e. redsh4de - [CCS Frontend Redesign](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/641)     
  f. Selsta - [part-time monero development, 3 months](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/680)      
5. Workgroup reports    
  a. Dev workgroup  
  b. Localization workgroup  
  c. Outreach workgroup  
  d. Events workgroup  
  e. Website workgroup  
  f. Policy workgroup  
  g. Research workgroup  
  h. [FCMP++ stressnet](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1391)

# Discussion History
## nahuhh | 2026-08-06T20:07:54+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<ofrnxmr\>** Meeting time: https://github.com/monero-project/meta/issues/1398     
    
> **\<moneromavrick:matrix.org\>** Hello goyim     
    
> **\<ofrnxmr\>** Mav, please     
    
> **\<r4v3r23\>** hey     
    
> **\<michael\>** Hello.     
    
> **\<ofrnxmr\>** 3. Community highlights     
    
> **\<ofrnxmr:xmr.mx\>** Monerokon is next weekend https://www.monerokon.org     
    
> **\<ofrnxmr:xmr.mx\>** In Warsaw, Poland     
    
> **\<moneromavrick:matrix.org\>** @ofrnxmr:xmr.mx: The shooting range is hype     
    
> **\<ofrnxmr:xmr.mx\>** I shared the other day, but to repeat:     
    
> **\<ofrnxmr:xmr.mx\>** BasicSwap is presenting at MK26     
    
> **\<ofrnxmr:xmr.mx\>** "Monero atomic swaps on a phone"[... more lines follow, see https://mrelay.p2pool.observer/e/j7mRmYgLVU9VLW9Q ]     
    
> **\<ofrnxmr:xmr.mx\>** Retoswap, bisq, and eigenwallet are all back online.     
    
> **\<ofrnxmr:xmr.mx\>** Basicswap had some additional hardening done as well to avoid such things as accepting a swap where the fees are too low to be confirmed in a reasonable time. again, bsx doesnt require btc or ltc nodes anymore, so setup is much easier     
    
> **\<ofrnxmr\>** Anyone else?     
    
> **\<plowsof\>** https://github.com/seraphis-migration/monero/releases FCMP++ & Carrot beta stressnet v2.0 Pre-release     
    
> **\<plowsof\>** also July 1st     
    
> **\<ofrnxmr:xmr.mx\>** Yeah. Would be nice to have as many people as possible running the stressnet     
    
> **\<jpk68:matrix.org\>** Hello     
    
> **\<ofrnxmr:xmr.mx\>** You can use --proxy=127.0.0.1:9050 with tor, if you dont want your ip address on the network. Best ti test everything, including how the network behaved over tor     
    
> **\<r4v3r23\>** @ofrnxmr:xmr.mx: ill try to get this running on android asap     
    
> **\<ofrnxmr:xmr.mx\>** plowsof: What's july 1st?     
    
> **\<ofrnxmr:xmr.mx\>** Also would be great to have some "third party" wallet do a build with fcmp. cc @anon_contributor_xmr:monero.social  @anhdres:matrix.org     
    
> **\<ofrnxmr\>** News: [Revuo Monero](https://revuo-xmr.com/) - [This week in Monero TWIM](https://cyphergoat.com/this-week-in-monero)     
    
> **\<ofrnxmr\>** If nobody else has any community highlights to share, we can move on to the CCS proposals     
    
> **\<ofrnxmr\>** 4. CCS proposals     
    
> **\<ofrnxmr\>** a. [MRL] Dennis Trautwein - [ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)     
    
> **\<ofrnxmr\>** This was updated to remove the first milestone (dashboard) and to become more of a research CCS with the target on spy nodes and network topology. It needs feedback. I implore everyone here to please be active either in this chat, or on github     
    
> **\<ofrnxmr\>** gitlab*     
    
> **\<syntheticbird\>** need a price update     
    
> **\<ofrnxmr:xmr.mx\>** I personally don't have any comments on the updated proposal as of yet. Cc @sgp_:monero.social  to also take another look     
    
> **\<syntheticbird\>** otherwise i'm for this endeavor     
    
> **\<moneromavrick:matrix.org\>** @syntheticbird: Fcmp++ update = bullrun     
    
> **\<syntheticbird\>** I HATE MATRIX LAGGING     
    
> **\<ofrnxmr:xmr.mx\>** The lag is terrible and noticable on irc as well     
    
> **\<moneromavrick:matrix.org\>** @moneromavrick:matrix.org: (If it comes out soon and doesnt get delayed again🤪)     
    
> **\<ofrnxmr\>** b. Marko Pohlo - [Cuprate Consensus-Rule Differential Fuzzing](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/676)     
    
> **\<markopohlo:matrix.org\>** Would appreciate any feedback on this     
    
> **\<syntheticbird\>** You were sure awaiting this meeting for feedback     
    
> **\<ofrnxmr\>** > You have to drum up support for your proposal during the first two stages. Do not expect others (especially the Core Team or other trusted members of the community) to do it for you. Others may share and support if they are excited about your project, but ultimately it is nobody's responsibility but your own.     
    
> **\<ofrnxmr\>** We need more of this     
    
> **\<moneromavrick:matrix.org\>** ofrnxmr: Dumbing it down helps people on X promote it and bring support tbh     
    
> **\<@moneromavrick:matrix.org\>** <bawdyanarchist:matrix.org> you coming nga? > <@moneromavrick:matrix.org> The shooting range is hype     
    
> **\<moneromavrick:matrix.org\>** @bawdyanarchist:matrix.org: Dont tempt me broskie, if gambling was there id buy a flight with xmr immediately     
    
> **\<moneromavrick:matrix.org\>** Shooting range got me ready to finally go to an event, couldnt handle only nerd stuff     
    
> **\<ofrnxmr\>** Bawdy, mav - the topic is currently marko's proposal     
    
> **\<markopohlo:matrix.org\>** Got it, we'll spread the news throughout our network and on X in that case, if there isn't any specific feedback from the Monero contributors community at this moment!     
    
> **\<moneromavrick:matrix.org\>** @markopohlo:matrix.org: I can promote it on my X if you can dumb it down for me @XMRVoid     
    
> **\<moneromavrick:matrix.org\>** ofrnxmr: My bad     
    
> **\<ofrnxmr\>** marko, thank you. Even if you can get support from other devs or researchers etc     
    
> **\<markopohlo:matrix.org\>** @moneromavrick:matrix.org: Will keep that in mind! Appreciate it     
    
> **\<syntheticbird\>** As I said previously I'm bugged with the approach but more because of a lack of specification and extracted reference code that could permit such harness. Because of that I am afraid this will be hard to get correct, but RuntimeVerification have a track record as I understand it. So that is ok for me, but I think the price is too high     
    
> **\<jpk68:matrix.org\>** @moneromavrick:matrix.org: You might want to consider whether or not you actually support the proposal before promoting it     
    
> **\<moneromavrick:matrix.org\>** @jpk68:matrix.org: Yuh, hence why i said dumb it down     
    
> **\<markopohlo:matrix.org\>** I'll ask the lead fuzzing engineer to help me dumb it down, there's a high value to this type of work, but it's highly technical at the same time.     
    
> **\<ofrnxmr:xmr.mx\>** Yeah. We dont want noise as support     
    
> **\<moneromavrick:matrix.org\>** @ofrnxmr:xmr.mx: I promote what i understand, lots of nerd talk goes over head     
    
> **\<ofrnxmr:xmr.mx\>** Thats one of the issues with technical proposals. They need ACKs from people who actually understand the work     
    
> **\<markopohlo:matrix.org\>** @syntheticbird: Got it, we lowered the weekly rate it takes for our engineer to complete this type of work to below cost basically, but also wanted to be as transparent as possible with the community. But I'll take that feedback to the team!     
    
> **\<ofrnxmr:xmr.mx\>** The next proposal on the list is an example of such     
    
> **\<syntheticbird\>** @ofrnxmr:xmr.mx: In this case monero tech meeting could be adequate ?     
    
> **\<ofrnxmr\>** yeah     
    
> **\<ofrnxmr\>** c. SyntheticBird - [Cuprate Address Book, Reproducible Build and Supply Chain Security 3 months](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/678)     
    
> **\<syntheticbird\>** its me     
    
> **\<syntheticbird\>** 2 more weeks before beta guys     
    
> **\<jpk68:matrix.org\>** +1     
    
> **\<moneromavrick:matrix.org\>** @syntheticbird: Anyone else hyped asf for this update     
    
> **\<moneromavrick:matrix.org\>** Glad its not being rushed tho, my entire networh is in xmr LMFAO     
    
> **\<syntheticbird\>** @syntheticbird: this is a reference to the due to 2 weeks meme and this is not an engagement that Cuprate 0.1.0 will be released in 2 weeks.     
    
> **\<ofrnxmr\>** tobtoht, our resident build systems expert, commented in suppoet of the proposal. Such is an example of weighted support     
    
> **\<jpk68:matrix.org\>** Effort put into supply chain security (especially for a Rust project) is very worthwhile IMO     
    
> **\<jpk68:matrix.org\>** To be clear, I'm not a security or build systems expert     
    
> **\<ofrnxmr:xmr.mx\>** lgtm, i think.     
    
> **\<ofrnxmr:xmr.mx\>** wondering if @markopohlo:matrix.org  has a view on this?     
    
> **\<ofrnxmr\>** moving onto the next proposal: d. r4v3r23 - [ANONERO Continued development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/671)     
    
> **\<r4v3r23\>** looked into the 3 month option since it was brought up in a previous meeting, and heres what it looks like:     
    
> **\<r4v3r23\>** full time rate bumps up to $60/h: at current prices plus buffer the total is ~88 XMR     
    
> **\<r4v3r23\>** ideally we go this route, since its faster, more dedicated/focused work, and guarantees all 3 milestones will be completed in 3 months[... more lines follow, see https://mrelay.p2pool.observer/e/m5z8mYgLcGRCdXNU ]     
    
> **\<ofrnxmr\>** I believe some changes were made followinf the previous meeting to address some of @plowsof's concerns     
    
> **\<ofrnxmr\>** ((lag))     
    
> **\<syntheticbird\>** +1 for me     
    
> **\<ofrnxmr\>** +1 to what? as-is (6 months) or the prooosed 3 months?     
    
> **\<r4v3r23\>** ofrnxmr: yeah, we can go the 3 month route, id actually prefer that     
    
> **\<r4v3r23\>** can guarantee a "due by" date that way     
    
> **\<jpk68:matrix.org\>** I would have to say I support this in general as well. No such thing as too many Android wallets ;)     
    
> **\<r4v3r23\>** @r4v3r23: unless theres any complaints, ill update the proposal today     
    
> **\<ofrnxmr:xmr.mx\>** Before(current): 45/hr, 69.9xmr total (23.3 per milestone)     
    
> **\<ofrnxmr:xmr.mx\>** After: 60/hr, 88xmr (~29.3 per milestone)     
    
> **\<syntheticbird\>** money inflates with heat     
    
> **\<r4v3r23\>** @ofrnxmr:xmr.mx: part time 20hr/week was 45     
    
> **\<syntheticbird\>** stay hydrated people     
    
> **\<r4v3r23\>** 60 is the full time/ 40hr a week rate     
    
> **\<ofrnxmr\>** For people voting yes, which path are you voting yes on?     
    
> **\<syntheticbird\>** year     
    
> **\<syntheticbird\>** r4v3r23 has been there for a lot of time and is likely an agency asset spying on us all     
    
> **\<syntheticbird\>** I MEANT NOT     
    
> **\<r4v3r23\>** @syntheticbird: correct     
    
> **\<r4v3r23\>** by forcing you all to use tor     
    
> **\<r4v3r23\>** BUSTED     
    
> **\<jpk68:matrix.org\>** ofrnxmr: No preference     
    
> **\<syntheticbird\>** @r4v3r23: honesty is the path to redemption. I pardon you 👍️     
    
> **\<ofrnxmr\>** plowsof, thoughts on suggested changes?     
    
> **\<ofrnxmr:xmr.mx\>** I personally would probably say to stick with the more generous 6 month timeline and avoid issues with delivery delay / complaints etc. Also since changing again might just delay the process     
    
> **\<r4v3r23\>** @ofrnxmr:xmr.mx: that wont be an issue. dealing with an actual professional this time around     
    
> **\<r4v3r23\>** and 6 months doesnt mean no delay, it just spreads everything out more     
    
> **\<ofrnxmr:xmr.mx\>** But its gone from 1 year -> 6 months -> 3 months :P     
    
> **\<r4v3r23\>** well 1 year was overly cautious because of last time     
    
> **\<ofrnxmr:xmr.mx\>** @r4v3r23: Theres nothing wrong with finishing early     
    
> **\<syntheticbird\>** @ofrnxmr:xmr.mx: Truth nuke     
    
> **\<syntheticbird\>** blursed reaction     
    
> **\<r4v3r23\>** @ofrnxmr:xmr.mx: true. but if 3 months is the norm as suggested, those are the changes     
    
> **\<ofrnxmr:xmr.mx\>** 3 months is the norm for core devs that are working on time-based proposals     
    
> **\<ofrnxmr:xmr.mx\>** I wouldnt say its the norm in general     
    
> **\<r4v3r23\>** the only thing id say is, going for the 3 months gives possibility of extra funds for continued maintance and give the project a little more run way in terms of support     
    
> **\<ofrnxmr:xmr.mx\>** 2 more proposals to go, then we can swing back     
    
> **\<ofrnxmr\>** e. redsh4de - [CCS Frontend Redesign](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/641)     
    
> **\<r4v3r23\>** so id appreciate that in terms of keeping the project alive     
    
> **\<moneromavrick:matrix.org\>** Oooo redesign?     
    
> **\<syntheticbird\>** if this isn't merged i'll cut my water bottle in half and suicide my electronics     
    
> **\<ofrnxmr\>** I think this one is just awaiting merge     
    
> **\<syntheticbird\>** yes     
    
> **\<ofrnxmr\>** @mav this is to bring the ccs website design inline with beta.monerodevs.org     
    
> **\<pw:xmr.mx\>** new site looks nice     
    
> **\<syntheticbird\>** bro is one year late     
    
> **\<jpk68:matrix.org\>** Does the current CCS site require client-side JS? I can't remember     
    
> **\<moneromavrick:matrix.org\>** @pw:xmr.mx: Anything will look better than getmonero right now     
    
> **\<ofrnxmr:xmr.mx\>** No     
    
> **\<ofrnxmr:xmr.mx\>** No js shipped     
    
> **\<r4v3r23\>** @ofrnxmr:xmr.mx: based tbh     
    
> **\<syntheticbird\>** hold on     
    
> **\<syntheticbird\>** amend that     
    
> **\<syntheticbird\>** after stable release there will be a PR for optional light/dark toggle with optional js     
    
> **\<ofrnxmr:xmr.mx\>** A pr :P that might not be accepted     
    
> **\<ofrnxmr:xmr.mx\>** I think red also did one for beta website, but it wasnt shipped/added     
    
> **\<syntheticbird\>** @ofrnxmr:xmr.mx: 10 claude token that it get merge     
    
> **\<ofrnxmr\>** Ok, saved the best for last     
    
> **\<jpk68:matrix.org\>** How about no JS at all :_     
    
> **\<ofrnxmr\>** there is no js at all, currently     
    
> **\<ofrnxmr\>** f. Selsta - [part-time monero development, 3 months](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/680)     
    
> **\<syntheticbird\>** +1     
    
> **\<syntheticbird\>** +1     
    
> **\<syntheticbird\>** +1     
    
> **\<syntheticbird\>** +1     
    
> **\<ofrnxmr\>** +2     
    
> **\<syntheticbird\>** MMMMMMMMMMMMEEEEEEEEEEEEERRRRRRRRRGGGGGGGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEE     
    
> **\<r4v3r23\>** x3     
    
> **\<jpk68:matrix.org\>** Obvious +1     
    
> **\<selsta\>** so i thought about doing full time for the next 3 months due to extra h1 load and v0.19 branch     
    
> **\<selsta\>** last 3 months was crazy with hackerone submissions, though it seems to be slowing down again     
    
> **\<aillia:matrix.org\>** Is the image final, or is it a placeholder? (I'm just not a big fan of women with six fingers))) https://beta.monerodevs.org/_astro/landing.U9LvvXnN_D2JVt.avif     
    
> **\<syntheticbird\>** @aillia:matrix.org: all lifeform accepted onboard     
    
> **\<ofrnxmr:xmr.mx\>** I read "fat women with six fingers"     
    
> **\<syntheticbird\>** selsta: nice of you     
    
> **\<syntheticbird\>** selsta     
    
> **\<aillia:matrix.org\>** @ofrnxmr:xmr.mx: this too     
    
> **\<ofrnxmr:xmr.mx\>** @aillia:matrix.org: nothing is final. Will ping @diego:cypherstack.com  to fix her     
    
> **\<syntheticbird\>** will hackerone fixes be ever declassified     
    
> **\<syntheticbird\>** i know its hard for the Monero empire as this is a matter of national security     
    
> **\<selsta\>** yes, once there was some time for people to update     
    
> **\<jpk68:matrix.org\>** @syntheticbird: They're not fit for human consumption     
    
> **\<syntheticbird\>** ack.     
    
> **\<ofrnxmr:xmr.mx\>** @aillia:matrix.org: Lmao haha     
    
> **\<ofrnxmr\>** So selsta, does this mean that you might modify your proposal still?     
    
> **\<selsta\>** i will decide later today     
    
> **\<ofrnxmr\>** Ok thanks     
    
> **\<selsta\>** i don't want to do full time in the summer but i think there will be extra work load compared to normal which i'll have to do anyway so i might just modify the proposal     
    
> **\<ofrnxmr\>** Sounds good     
    
> **\<ofrnxmr\>** Next meeting: saturday june 13th     
    
> **\<ofrnxmr\>** 1600 utc     
    
> **\<ofrnxmr\>** Can end the meeting here. Feel free to keep discussing     
    
> **\<@r4v3r23\>** <r4v3r23> ACK on this? > <@r4v3r23> looked into the 3 month option since it was brought up in a previous meeting, and heres what it looks like:     
    
> **\<r4v3r23\>** are there any objections     
    
> **\<ofrnxmr:xmr.mx\>** jpk said no preference, i think syn preferred as-is(?). Not sure what plowsof's take is     
    
> **\<ofrnxmr:xmr.mx\>** Other who gave greetings at start of meeting have been quiet :(     
    
> **\<r4v3r23\>** if theres no clear objections, im gonna update the proposal     
    
> **\<syntheticbird\>** yeah i'm fine as is     
    
> **\<r4v3r23\>** worst case is theres a little xmr left over to keep the lights on     
    
> **\<r4v3r23\>** @syntheticbird: ok but do you object to 3 month change     
    
> **\<@ofrnxmr:xmr.mx\>** <redsh4de:matrix.org> yep, i can PR it but… contentious lol > <@ofrnxmr:xmr.mx> I think red also did one for beta website, but it wasnt shipped/added     
    
> **\<redsh4de:matrix.org\>** plus would break CI as it is rn (hates all client side JS)     
    
> **\<syntheticbird\>** @r4v3r23: no     
    
> **\<msvb-lab\>** I think my Matrix messages were never sent, anyway I got most of the meeting messages at least half. Seems like something is wrong with the bridge.     
    
> **\<msvb-lab\>** My last message was 'Dankon for the good meeting.'     
    
> **\<ofrnxmr:xmr.mx\>** Yeah, matrix was acting up today     
    
> **\<r4v3r23\>** @syntheticbird: thanks. @ofrnxmr:monero.social updating the proposal     
    
> **\<@ofrnxmr:xmr.mx\>** <diego:cypherstack.com> lmao > <@ofrnxmr:xmr.mx> nothing is final. Will ping @diego:cypherstack.com  to fix her     
    
> **\<diego:cypherstack.com\>** I'll ask Andres what happened there     
    
> **\<aillia:matrix.org\>** the good old prehistoric AI days of six-fingered people, lol )))     
    
> **\<pw:xmr.mx\>** not as good as 3 boobs     
    
> **\<moneromavrick:matrix.org\>** @diego:cypherstack.com: AI lol     
    
> **\<moneromavrick:matrix.org\>** “Claude remake it with 5 fingers. Make no mistakes”     
    
> **\<diego:cypherstack.com\>** @moneromavrick:matrix.org: Isn't. Andres draws by hand.     
    
> **\<diego:cypherstack.com\>** Allegedly. :P     
    
> **\<diego:cypherstack.com\>** @pw:xmr.mx: I'll make the request.     
    
> **\<selsta\>** I changed my CCS for full time for the next 3 months, will likely go back to 30h / week after that until we get closer to FCMP++ release     
    
> **\<selsta\>** ofrnxmr ^     
    
> **\<r4v3r23\>** i also updated my CCS for full time (40h/week, 3 months)     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: nahuhh | 2026-05-30T04:25:34+00:00
- Closed at: 2026-08-06T20:11:10+00:00
