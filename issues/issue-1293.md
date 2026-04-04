---
title: 'Monero Community Workgroup Meeting: Nov 8th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1293
author: plowsof
assignees: []
labels: []
created_at: '2025-11-08T12:00:34+00:00'
updated_at: '2025-12-02T13:38:06+00:00'
type: issue
status: closed
closed_at: '2025-12-02T13:38:05+00:00'
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
    -  [FCMP++ & Carrot alpha stressnet v1.4](https://github.com/seraphis-migration/monero/releases/tag/v0.19.0.0-alpha.1.4)
    - New p2pool update - via [monero.observer](https://monero.observer/p2pool-v4.12-released-full-tor-support/)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This Week In Monero](https://cyphergoat.com/this-week-in-monero) 

4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)    
  b. [v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)    
  c. [acx part-time work on Monfluo 2025Q4](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/616)    
  d. [xmr-support-thorchain](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/619)    
  e. [Getmonero.org Redesign Implementation](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/620)    
  f. [anon: full-time on daemon & fcmp](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/621)    
  g. [39C3 Support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2026](https://MoneroKon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [FCMP++ Stressnet updates](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1286)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2025-12-02T13:33:44+00:00
Logs 
    
    
    
    
    
    
> **\<plowsof\>** Meeting time https://github.com/monero-project/meta/issues/1293     
    
> **\<plowsof\>** Greetings!     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/WJjRniwhcPCPmZALDsvBGRzl.jpg (media_G4ylB7dakAAh33L.jpg)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Aloha     
    
> **\<plowsof\>** i missed the new p2pool update, seen it on https://monero.observer/p2pool-v4.12-released-full-tor-support/     
    
> **\<plowsof\>** DataHoarder discovered that today Qubic had their centralized mining task server stop working for several hours ... https://libera.monerologs.net/monero-research-lounge/20251108#c608798     
    
> **\<DataHoarder\>** ^ context, onion was supported before, but now there's explicit support for exposing them and connecting to onion servers. Onion seeds are exposed too     
    
> **\<plowsof\>** FCMP++ stressnet 1.4, whats new? 👀 https://github.com/seraphis-migration/monero/releases/tag/v0.19.0.0-alpha.1.4     
    
> **\<DataHoarder\>** Onion discovery is done via publishing the addresses on shares, effectively gating it after PoW     
    
> **\<DataHoarder\>** both p2pool and go-p2pool support this (seed servers are both implementations!)     
    
> **\<plowsof\>** "exposed" as in available for connecting to or      
    
> **\<plowsof\>** sorry, ignore^     
    
> **\<DataHoarder\>** I always had onion p2pool nodes for observer, for example :)     
    
> **\<plowsof\>** nice     
    
> **\<DataHoarder\>** but now these addresses can be discovered and automatically connected via standard means, not manually added     
    
> **\<DataHoarder\>** I'd give you an example but I didn't build any UI for it. Mini has a couple of users already exposing a .onion this way :)     
    
> **\<DataHoarder\>** (they set it up + found a share to list it). Note that this links addr <> .onion, but as we say in p2pool, always use a different wallet for mining     
    
> **\<DataHoarder\>** There's other good to have patches in v4.12 so upgrade :)     
    
> **\</ad\>** </ad>     
    
> **\<plowsof\>** DH's go-p2pool @ https://git.gammaspectra.live/P2Pool/consensus      
    
> **\<DataHoarder\>** https://git.gammaspectra.live/P2Pool/go-p2pool but yes, < this is a wrapper around consensus library     
    
> **\<plowsof\>** jberman CCS update is FCMP++ progress heavy https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/600#note_32851      
    
> **\<plowsof\>** getmonero beta from redshade @ https://getmonero-redesign-impl.vercel.app/downloads/ , who has an open CCS idea for it also      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Cake reached 1million downloads     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Monero-project/monero repo reached 10000 stars     
    
> **\<plowsof\>** https://github.com/monero-project/monero wow     
    
> **\<plowsof\>** i've added a star, hadn't starred it, sorry      
    
> **\<plowsof\>** almost there https://ccs.getmonero.org/funding-required/      
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> hello     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> o/     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> last big update on that part was to add i18n support to the downloads page     
    
> **\<plowsof\>** (i did not see ofrnxmrs message on matrix from my morg account)     
    
> **\<plowsof\>** homeserver chainsplit? irc remains unaffected https://libera.monerologs.net/monero-community/20251108     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> yeah getting delayed msgs here     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> we can speak slowly     
    
> **\<datahoarder\>** <datahoarder> I see monero.social getting IRC messages fast     
    
> **\<plowsof\>** thanks      
    
> **\<datahoarder\>** <datahoarder> so seems to be Matrix federation as usual     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> dont join irc, it leaks ip address for all chat to see, so unless you're behind a vpn, then do the cloak thing, wouldnt recommend irc (there is some heavy irc shills that been around tho, that never mentioned that)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> devoice fungible plz     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> ofrn = on feds payroll     
    
> **\<datahoarder\>** <datahoarder> @fungible.:matrix.org: you can force-join with cloak before being in the server, which is default in many servers nowadays.      
    
> **\<nioc\>** everyone already knows that       
    
> **\<datahoarder\>** <datahoarder> Yeah. They joined a few days ago to prepare for spam     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> 👍️     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> the matrix lag seems to be better now, all good     
    
> **\<DataHoarder\>** monerologs should get messages relatively quick for other Matrix users     
    
> **\<plowsof\>** you can also join via https://web.libera.chat/      
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> nothx     
    
> **\<plowsof\>** tor is allowed but the account "must be created without tor". an alternative IRC network which afaict is more tor firiendly is OFTC      
    
> **\<plowsof\>** anywhos     
    
> **\<plowsof\>** #feather is on oftc for example, right      
    
> **\<plowsof\>** redshade is here, lets discuss their ccs first      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Can talk about how-to-join-irc-with-tor after the meeting     
    
> **\<plowsof\>** yeye     
    
> **\<plowsof\>**   e. [Getmonero.org Redesign Implementation](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/620)         
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> redeshade, from the new monero implementation blitz fame     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Looks good and solid progress already     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> I appreciate that the work has begun and the repos are available     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> 🫡 wanted to have solid "proof of work" available first     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> And that everything seems to be done well (in my uneducated opinion). I haven critiqued the codebase     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Ignoring the finer details of the proposal, its a +1 from me inho     
    
> **\<plowsof\>** is your downloads page translated for both desktop and mobile view?      
    
> **\<plowsof\>** the official getmonero downloads page is only translated for mobile users , not desktop, i noticed this today, so you may have surpassed the existing      
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> yes, all components used are exactly the same for both mobile desktop, some have responsive styling within components in order to adapt to smaller screens     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> so no more one big custom.css file     
    
> **\<plowsof\>** existing site has functionality (50% broken but still) for displaying different versions of binaries ,  this is rare but it has happened , have to confirm with selsta      
    
> **\<plowsof\>** i also discovered this today with my torrent PR , as the torrent will lag behind official relase for a week or 2 until DNS are updated https://github.com/monero-project/monero-site/pull/2555      
    
> **\<plowsof\>** example https://deploy-preview-2555--barolo-time-757cf9.netlify.app/downloads/      
    
> **\<plowsof\>** so the betas downloads page is better than what we have already? xD     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Do we have to rely on dns? Or can we just use the commited hashes.txt     
    
> **\<DataHoarder\>** afaik that's just for webseeds^     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> for a delayed torrent if accepted on site? just a delayed release incase there is a bug found. when dns go live that means the software is presumed OK enough      
    
> **\<DataHoarder\>** unless you mean plowsof to get new domain in for torrents     
    
> **\<plowsof\>** if you want to see a torrent update you follow an rss feed :P      
    
> **\<plowsof\>** the future is now     
    
> **\<plowsof\>** <redsh4de:matrix.org> i'd prob add that in by changing the "Download" dropdown to have buttons for direct link/magnet link, something to try around in the design > <plowsof> existing site has functionality (50% broken but still) for displaying different versions of binaries ,  this is rare but it has happened , have to confirm with selsta     
    
> **\<plowsof\>** the torrent itself wont even touch the DNS' or anything, its just a good time to display the updated / seeding^ yeah      
    
> **\<plowsof\>** any other things to mention from your end redsh4de      
    
> **\<plowsof\>** sad that our getmonreo downloads page is horrible spaghetti code      
    
> **\<plowsof\>** alot of headaches caused there      
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> plowsof: currently i am planning to work on the i18n system to be more easier to use when translating a paragraph or any text content that includes links, or lists, line breaksm etc. Currently doing inline html as a proof of concept, but probably going to do a markdown preprocessor for that, as just inline opens up to XSS attacks via translation files     
    
> **\<plowsof\>** existing site is locked to a version of po4a because....... something about lists being used in tags ... but here is po4a worklow i cobbled together , dunno if useful now or later https://github.com/plowsof/monero-site/blob/po4a-staged/.github/workflows/po4a.yml      
    
> **\<plowsof\>** ok thanks redsh4de     
    
> **\<plowsof\>** <redsh4de:matrix.org> new one should be very easy to extend - i seperated core downloads and community downloads into two distinct files, the one for Core is meant to be auto updated by CI, second for community should be manually edited, then descriptions must be translated in the respective i18n file > <plowsof> sad that our getmonreo downloads page is horrible spaghetti code      
    
> **\<plowsof\>** nice, ok lets move on     
    
> **\<redsh4de:matrix.org\>** <redsh4de:matrix.org> site imports the data and displays it all nice and pretty: https://github.com/redsh4de/monero-site/blob/main/src/data/downloads/community.json     
    
> **\<plowsof\>** 👀     
    
> **\<plowsof\>** make "add this" , "remove that" great again 💪     
    
> **\<plowsof\>** any comments on :     
    
> **\<plowsof\>**   a. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)         
    
> **\<plowsof\>** i've been too busy past 2 weeks to test :(      
    
> **\<plowsof\>**   b. [v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)         
    
> **\<plowsof\>** v1do left a follow up comment to mine @ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607#note_32601     
    
> **\<plowsof\>**   c. [acx part-time work on Monfluo 2025Q4](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/616)         
    
> **\<plowsof\>**   d. [xmr-support-thorchain](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/619)         
    
> **\<plowsof\>** no updates on thorchains proposal , unless?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Arent they doing it on their own     
    
> **\<plowsof\>** by choice and force (after community feedback)     
    
> **\<plowsof\>**   f. [anon: full-time on daemon & fcmp](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/621)         
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> 👍️     
    
> **\<0xfffc\>** <0xfffc> +1 for anon CCS     
    
> **\<nioc\>** for anon, the people working with him should get the say as to whether or not to merge     
    
> **\<plowsof\>** thanks for feedback      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> +1     
    
> **\<0xfffc\>** <0xfffc> nioc: We are already quite short on developers. And we need a experienced dev like him. DEFINITELY     
    
> **\<0xfffc\>** <0xfffc> s/a/an/     
    
> **\<rucknium\>** <rucknium> IMHO, potential contributions by anon need to be reviewable, meaning at least two (preferably three) longtime developers are willing to review his code to check its mergeability. Potential reviewers should look at his previous PRs to see what they would get themselves into. jberman said he would be willing to be a reviewer. That's one.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> There are 2 or 3 devs willing to review (and even restructure) his code     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> 0xfffc is 2     
    
> **\<0xfffc\>** <0xfffc> @ofrnxmr:xmr.mx: Me for example     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Selsta already +1'd the proposal     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> 2 in 1?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> powerful 0xfffc 😄     
    
> **\<rucknium\>** <rucknium> sech1 commented that anon's PRs are usually too big. That they change too much sensitive code. But if the architecture is bad, then wouldn't the changes need to be big and all at once?     
    
> **\<nioc\>** 0xffc I did not say no     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> jberman and 0xfffc dont care about the size     
    
> **\<rucknium\>** <rucknium> Would selsta be wiling to review anon's code?     
    
> **\<nioc\>** I just said who should be making the decision      
    
> **\<0xfffc\>** <0xfffc> @rucknium: Do we need selsta to review all the codes? Of course selsta input is valuable. But forcing him to review?!     
    
> **\<rucknium\>** <rucknium> OK. It seems that there are a minimum of two willing reviewers now.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> remember selstas monero fork we used to run binaries from for stable servers?      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Selsta was involved in the prior submissions (even submitted some via proxy) and ran the code and tests     
    
> **\<0xfffc\>** <0xfffc> And I don’t understand why we should ask selsta reviews for approval     
    
> **\<0xfffc\>** <0xfffc> Of this ccs     
    
> **\<0xfffc\>** <0xfffc> ( again, which is fine. )     
    
> **\<rucknium\>** <rucknium> We don't need selsta to review, but @ofrnxmr:xmr.mx replied that selsta +1'ed the proposal. I want to clarify that selsta would not be one of the reviewers (or, would).     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> as long as he doesnt introduce an inflation bug in the code like an insider dev did in ravencoin few years ago lol     
    
> **\<0xfffc\>** <0xfffc> @rucknium: Selsta +1 is valuable imho.     
    
> **\<rucknium\>** <rucknium> selsta needs to speak more.     
    
> **\<selsta\>** I +1 because we need more developers and in his last CCS he did valuable work.     
    
> **\<boog900\>** <boog900> @fungible.:matrix.org: this is one of the huge problems of making massive changes to subsystems and why reviewing takes so long      
    
> **\<boog900\>** <boog900> I am not against this proposal though      
    
> **\<selsta\>** I'm not going to review all his code, I don't know where that comes from. I would not have the knowledge for this.     
    
> **\<rucknium\>** <rucknium> Thanks, selsta, for explaining your +1.     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> (I didnt say you would review, fwiw :P. I think ruck was just asking)     
    
> **\<rucknium\>** <rucknium> Yes, I think there was just confusion with the sequence of messages that seemed to be a direct reply to my suggestion.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> just to quickly share the pre-announcement (as no budget has been supplied yet) for this ccs:   g. 39C3 Support (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/622)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> at the hour, any other things to mention?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Simplex going on monerotopia in a few mins     
    
> **\<fungible.:matrix.org\>** <fungible.:matrix.org> when the next meeting?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> in 2 weeks fungible which is...      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> @ofrnxmr:xmr.mx:  after the price report 😂     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> @fungible.:matrix.org: Bi-weekly. Every two weeks.      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @plowsof:matrix.org: Price report is done     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> 11/22, should bee.     
    
> **\<lordx3nu:matrix.org\>** <lordx3nu:matrix.org> @ofrnxmr:xmr.mx: So we are in hour three of twenty?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Ya     
    
> **\<plowsof\>** lol thanks all for joining the hour     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-11-08T12:00:34+00:00
- Closed at: 2025-12-02T13:38:05+00:00
