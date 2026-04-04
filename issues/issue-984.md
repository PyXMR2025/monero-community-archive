---
title: 'Monero Community Workgroup Meeting: Saturday 30th March 15:00UTC'
source_url: https://github.com/monero-project/meta/issues/984
author: plowsof
assignees: []
labels: []
created_at: '2024-03-29T08:56:05+00:00'
updated_at: '2024-04-08T09:29:06+00:00'
type: issue
status: closed
closed_at: '2024-04-08T09:29:06+00:00'
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
    - 2023 MoneroKon talk [ArticMine - Overview Security, Spam, Scaling & Fee Markets](https://yewtu.be/watch?v=KuIRDTsyzkQ)    
    - [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358#note_23789) completed - CypherStack
    - General fund donations! [100](https://twitter.com/WatchFund/status/1771903071611752505) / [69.696969](https://twitter.com/WatchFund/status/1772727889294758191) / [100](https://twitter.com/WatchFund/status/1772987191901176309) / [100](https://twitter.com/WatchFund/status/1773184158132511037) / [0.42069](https://twitter.com/WatchFund/status/1773201988731252952)
    - ["March 2024 Suspected Black Marble Flooding Against Monero: Privacy, User Experience, and Countermeasures"](https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf).
    - Matrix (de)federation issues [update](https://libera.monerologs.net/monero-community/20240329#c353792) - xmrscott . Pigeons is following up a lead regarding a possible cloudflare / matrix dot org firewall issue.
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [Unnamed Monero Wallet development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/437)   
  b. 0xFFFF - withdrawn idea / [in progress ccs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/438) on pause for the foreseeable future.
  c. [Rucknium Statistical Research](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/439)    
  d. [bigmenpixel payout request](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381#note_23554) 
  e. [plowsof CCS Coordinator](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/440)
  f. [Seraphis General Paper Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441)    
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2024](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2024-04-08T09:28:52+00:00
Logs 
> __< plowsof >__ community meeting today (added a link to ArticMines 2023 monerokon talk) https://github.com/monero-project/meta/issues/984     

> __< plowsof >__ Meeting in 1 hour      

> __< b​usyboredom:monero.social >__ I'm gonna be AFK during the meeting, but here's a long overdue update on AcceptXMR progress:     

> __< b​usyboredom:monero.social >__ The API is still in development, I rewrote the HTTP server using Axum last month to take better advantage of the Tower ecosystem.      

> __< b​usyboredom:monero.social >__ I'm currently working on mocking out the daemon RPC client so that I can get better test coverage of the API I'm writing without relying on slow integration tests.     

> __< plowsof >__ thanks for the update busyboredom and continued efforts!     

> __< plowsof >__ Meeting time https://github.com/monero-project/meta/issues/984      

> __< plowsof >__ Greetings!     

> __< r​ucknium:monero.social >__ Hi!     

> __< m​ichael:monero.social >__ Hello.     

> __< p​lowsof:matrix.org >__ hopefully this works.. just a headsup again for matrix dot org users, you will not be able to see messages live from IRC / monero dot social users. but they can see your messages. ill share updates on this as they come as its on-going     

> __< plowsof >__ Worth a rewatch / watch (especially with recent events) 2023 MoneroKon talk [ArticMine - Overview Security, Spam, Scaling & Fee Markets](https://yewtu.be/watch?v=KuIRDTsyzkQ)       

> __< plowsof >__ [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358#note_23789) completed - CypherStack , Rucknium has added it to the agenda for the next MRL meeting     

> __< plowsof >__ Rucknium is involved in nearly all of the highlights it seems, ["March 2024 Suspected Black Marble Flooding Against Monero: Privacy, User Experience, and Countermeasures"](https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf). nice      

> __< m​ichael:monero.social >__ Good job Rucknium.     

> __< plowsof >__ general fund donations... totaling over 370 XMR have been sent the past week, in demomninations of 69.696969 / 100's and 0.42069      

> __< nioCat >__ no 1337?     

> __< plowsof >__ not recently but im certain there is one in the archives , surely      

> __< plowsof >__ https://twitter.com/WatchFund/status/1496358951444787204      

> __< plowsof >__ feb 23 2022 a 0.1337 donation      

> __< plowsof >__ some other news would be the xz backdoor which does not effect release binaries, but possibly if you self compiled monero: https://libera.monerologs.net/monero-dev/20240329#c354025     

> __< plowsof >__ we can move on to the ccs ideas shortly unless anything pops up https://ccs.getmonero.org/ideas/      

> __< plowsof >__ iirc this is a holiday weekend , hope everyone is having a nice time      

> __< p​lowsof:matrix.org >__ thanks for joining BigmenPixel , matrix dot org users can follow the irc chat @ https://libera.monerologs.net/monero-community/20240330     

> __< plowsof >__ CCS ideas      

> __< plowsof >__   a. [Unnamed Monero Wallet development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/437)        

> __< p​lowsof:matrix.org >__ Czarek Nakamoto anything to share about this proposal? you have accomplished something recently related to DLL's for windows iirc?     

> __< mrcyjanek >__ yes, windows builds are working fine     

> __< mrcyjanek >__ they are not packaged but they work     

> __< mrcyjanek >__ macos and ios is in the works at the very moment     

> __< plowsof >__ if this something that didnt exist before for monero? and came about becaose of "monero_c"?     

> __< mrcyjanek >__ yes and no, monero was cross platform, but there was no way to use it from anything else than C++     

> __< plowsof >__ the feedback seems to have stagnated after the original input hm      

> __< mrcyjanek >__ the commits are still going into the repository.     

> __< mrcyjanek >__ so maybe feedback did but the development didnt pause     

> __< plowsof >__ nobody has questioned your skills, quite the opposite in fact, and your rates are low. (monero_c repo here https://git.mrcyjanek.net/mrcyjanek/monero_c)     

> __< plowsof >__ maybe the monero_c + xmruw all  in one is too much to digest combined with some of the feedback against investing in a 'new thing' this late in the game. but we then contrast that with the upcoming seraphis review who highlights that seraphis is not a certainty still      

> __< plowsof >__ thank you for attending, if anyone wishes to comment on the proposal, please do     

> __< plowsof >__ moving on then     

> __< plowsof >__ (maybe stackwallet could speak to the usefulness of monero_c 'now' (as this DLL thing seemed to be a hit with them)      

> __< plowsof >__   b. 0xFFFF - withdrawn idea / [in progress ccs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/438) on pause for the foreseeable future.https://twitter.com/WatchFund/status/1496358951444787204     

> __< a​remor:matrix.org >__ How long is today’s meeting expected to last?     

> __< plowsof >__ no timeframe has been given. perhaps jeffro256 would like to know as this pretains to the read/lock PR which would be effected by this      

> __< plowsof >__ for another 30 mins~     

> __< p​lowsof:matrix.org >__ aremor another 30 mins, most messages are on irc, so can't be seen from matrix dot org accounts sadly     

> __< plowsof >__   c. [Rucknium Statistical Research](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/439)         

> __< r​ucknium:monero.social >__ "I propose to carry out statistical research to improve Monero's privacy, guide protocol decisions, and respond to Monero developer requests for statistical analysis of code changes where needed. In the short term I will complete in-progress analysis of the suspected transaction spam attack to provide a comprehensive view of the options to defeat this attack and possible future ones."     

> __< p​lowsof:matrix.org >__ please check the monerologs link above and leave feedback here if you wish     

> __< r​ucknium:monero.social >__ Questions and feedback welcome :)     

> __< plowsof >__ thanks for joining Rucknium!      

> __< plowsof >__ have discussions with articmine already began? ive noticed some back and forth recently about anti spam measures?     

> __< r​ucknium:monero.social >__ We have been discussing in #monero-research-lab:monero.social     

> __< plowsof >__ nice, thank you     

> __< plowsof >__ so this is going to be a general / all encompassing CCS proposal. focussing on the important tasks at hand (that being your black marble research draft paper?)      

> __< r​ucknium:monero.social >__ https://libera.monerologs.net/monero-research-lab/20240320#c350623 "When you have a range of fee and blocksize adjustment options available, I can do some modeling."  Response: "👍️"     

> __< plowsof >__ similar to other tasks / services you have completed, some listed on your page @  https://rucknium.me/     

> __< r​ucknium:monero.social >__ Yes black marble flooding is the first priority. Once that's done, in this CCS I will continue with other research priorities like PocketChange analysis, fee discretization and prediction, etc     

> __< plowsof >__ so this would be business as usual, as you have been contributing in a similar fashion since your OSPEAD proposal (which was delayed for reasons out of your control)     

> __< r​ucknium:monero.social >__ Not really business as usual. More input from the community and developers on research priorities since I would be paid for my time.     

> __< plowsof >__ i note midipoets comment about having that ccs completed first      

> __< r​ucknium:monero.social >__ I explained in the proposal why it's better to switch the order because of realtime developments like the suspected black marble attack.     

> __< plowsof >__ sounds logical      

> __< plowsof >__ does anyone have any feedback? i dont mind to share a +1      

> __< r​ucknium:monero.social >__ Maybe this black marble attack was feasible since no one did this research before on how parameters should be set to prevent the attack. I won't put much more time into this research until this CCS gets approved.     

> __< r​ucknium:monero.social >__ Without analysis, the programmers are just guessing.     

> __< nioCat >__ have already upvoted on he CCS site     

> __< r​ucknium:monero.social >__ Maybe good guesses. Maybe bad guesses.     

> __< plowsof >__ thanks for the feedback nioCat      

> __< plowsof >__ we can move on at that me thinks      

> __< plowsof >__   d. [bigmenpixel payout request](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381#note_23554)      

> __< r​ucknium:monero.social >__ This question: "Are there any viable flooding countermeasures, like a decentralized counter-flood?" was in my https://github.com/Rucknium/presentations/blob/main/Rucknium-Monerotopia-2023-Slides.pdf . But it didn't get answered because too many things to do. And not being paid for expertise makes it harder.     

> __< plowsof >__ kinghat , a supported from the beginning of this proposal / flathub gui user has left a positive comment/feedback , combined with the stats shown for me leaves no doubt that bigmenpixel has been maintaining monero gui for 12 months and again i would like to push for the milestones (except number 1) to be paid out      

> __< plowsof >__ definitely Rucknium. looking forward to what comes of your proposal     

> __< r​ucknium:monero.social >__ +1 for payout to BigMenPixel since kinghat has done independent testing.     

> __< tobtoht_ >__ voicing support for payout     

> __< p​lowsof:matrix.org >__ bigmenpixel is here on matrix side     

> __< plowsof >__ moving forward - yeah, flathub .. supply chain attacks, i dont know. but bigmenpixel is a good maintainer for a flatpak solution - whatever it ends up being for monero-gui. thank you for your contributions      

> __< plowsof >__ thanks for the feedback!     

> __< p​lowsof:matrix.org >__ payout for all milestones (except 1) seems to be approved.. now.. moving on     

> __< plowsof >__   e. [plowsof CCS Coordinator](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/440)     

> __< plowsof >__ i had closed out my previous ccs here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/418#note_23583      

> __< tobtoht_ >__ +1 plowsof     

> __< nioCat >__ +1     

> __< plowsof >__ thanks <3      

> __< r​ucknium:monero.social >__ I think you've been doing a good job. Two feedback items: Sometimes people don't understand that you are saying something in jest. Maybe say "(This is a joke)" to make it more obvious. 2) Would this include the extended set of things you have been doing like monero.bounties and some website things?     

> __< plowsof >__ 1) ill have to work on that, probably a deep rooted issue i need to consult help for / coping mechanism ,, semi joke - but i will try! thanks for the heads up     

> __< nioCat >__ yes, english is not everyone's first language      

> __< plowsof >__ 2) yes this would be everything that ive been doing.. checking on bounties / handling  issues there (to be honest its just checking emails and asking for feedback but yes all included) and with site, there will be more effort put into that where possible.. gathering PR's / handling small conflicts and what not      

> __< r​ucknium:monero.social >__ Sounds great :)     

> __< plowsof >__ i only put the idea up yesterday so i hope to gather some other feedback, thank you all for the input. will work on number 1) hmmmmm lets move on      

> __< plowsof >__   f. [Seraphis General Paper Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441)         

> __< plowsof >__ me thinks MRL need to see a Scope Of Work (i know jberman has been working closely with Dr Aaron to draft one up     

> __< r​ucknium:monero.social >__ I have wanted a review of Seraphis's mathematics for about two years. Glad to see it will happen.     

> __< plowsof >__ and clarification on the payout method... same as the bulletproofs++ peer review (third party fiat only) or simply the xmr (with volatility risks)     

> __< d​iego:cypherstack.com >__ Hi its me     

> __< plowsof >__ hello!     

> __< r​ucknium:monero.social >__ This scope may change if kayabaNerve can convince at the MRL meeting next week that FCMP can be implemented on mainnet before Seraphis. Then maybe this work item would change to writing a security proof for FCMP-without-Seraphis.     

> __< plowsof >__ after my brief interations with crypto auditors, i can say the price point can't be beaten compared to the one serious quote received already)     

> __< nioCat >__ ruck beat me to it     

> __< nioCat >__ will b e discussed at Wed's MRL meeting      

> __< r​ucknium:monero.social >__ IMHO if the payout is expected as fiat, you must confirm that there is a XMR-to-fiat intermediary ready and willing to do it.     

> __< d​iego:cypherstack.com >__ We give Monero good prices     

> __< plowsof >__ thanks for the context, looking forward to the MRL meeting.      

> __< d​iego:cypherstack.com >__ Consider the deep discount our contusion     

> __< d​iego:cypherstack.com >__ Contribution* :P     

> __< plowsof >__ :D     

> __< r​ucknium:monero.social >__ Diego Salazar: For the "half completed" milestone, would you post a draft of the review at that point?     

> __< d​iego:cypherstack.com >__ Yep. Same as last time.     

> __< r​ucknium:monero.social >__ Great     

> __< plowsof >__ and payout would be in xmr? no third party to handle fiat?     

> __< plowsof >__ that would be the only housekeeping for me to check off the list     

> __< r​ucknium:monero.social >__ Diego Salazar: About your BP++ review. I plan to post it to moneroresearch.info . Do you have any objection to that?     

> __< d​iego:cypherstack.com >__ None.     

> __< d​iego:cypherstack.com >__ Chevy     

> __< d​iego:cypherstack.com >__ Correct     

> __< d​iego:cypherstack.com >__ Gosh my typing is bad today on phone     

> __< r​ucknium:monero.social >__ Great. search engines are indexing MR.info now. Posting it should make it easier for others to find your work :)     

> __< p​lowsof:matrix.org >__ ok thanks for confirming     

> __< plowsof >__ any further comments on this, while we wait for wednesdays MRL meeting? otherwise thank you for attending Diego     

> __< d​iego:cypherstack.com >__ Not from me, no. Hope you all see value in our work. :)     

> __< plowsof >__ i think we can call the meeting here then? thank you for all attending... shame about the matrix issues     

> __< plowsof >__ have a nice weekend everyone      


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2024-03-29T08:56:05+00:00
- Closed at: 2024-04-08T09:29:06+00:00
