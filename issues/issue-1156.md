---
title: 'Monero Community Workgroup Meeting: February 15th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1156
author: plowsof
assignees: []
labels: []
created_at: '2025-02-15T10:34:02+00:00'
updated_at: '2025-03-26T23:54:09+00:00'
type: issue
status: closed
closed_at: '2025-03-26T23:54:09+00:00'
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
    - Public RPC Node operators are highly recommended to build latest release branch [release-v0.18](https://github.com/monero-project/monero/tree/release-v0.18)
    - the `m-relay` maintainer DataHoarder has launched an app service bridge that is feature packed and is in active testing in all p2pool rooms
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [Monero Moon](https://www.themoneromoon.com/)    
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [NoShore: Groundwork for on-the-go offline payments](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/525)    
  b. [dmvp2p: Donate Monero Via P2Pool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/531)    
  c. [Funding Proposal for Unstoppable Wallet: Enabling Native Monero Integration on iOS & Android](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/532)    
  d. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)    
  e. [hinto-janai full time work (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/543)    
  f. [Boog900 full time work on Cuprate (3 months) + January](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/544)    
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1149)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2025-03-26T23:52:56+00:00
> __< ofrnxmr >__ Meeting time, shh     

> __< e​longated:matrix.org >__ Oops didn’t see 🙏🏻     

> __< ofrnxmr >__ Scared plowsof away     

> __< plowsof >__ oh sorry yes      

> __< plowsof >__ thought i was in it lol     

> __< plowsof >__ Meeting time https://github.com/monero-project/meta/issues/1156     

> __< plowsof >__ greetings , hello     

> __< ofrnxmr >__ Hi     

> __< plowsof >__ i heard monero was under attack and all nods are offline     

> __< ofrnxmr >__ Yup. I shut my nodes off to make sure they didnt get infected /s     

> __< plowsof >__ cuprate / boog900 has suggested the possibility of a 'for purpose' seed node that can run on cheap hardware      

> __< plowsof >__ Public RPC Node operators are highly recommended to build latest release branch [release-v0.18](https://github.com/monero-project/monero/tree/release-v0.18)     

> __< ofrnxmr >__ on that ^, tag is coming soon. No real rush for anyone who isnt running a high volume rpc node     

> __< plowsof >__ monero could use another ipv4 seed node and 2~ tor ones i think if anyone is interested      

> __< ofrnxmr >__ Mining pools should close rpc ports if open, and wallet default nodes should update to avoid downtime. Seed nodes as well     

> __< b​tclovera:matrix.org >__ Hi everyone     

> __< ofrnxmr >__ really only need some seed nodes to update right away, and some are, so no rush     

> __< b​oog900:monero.social >__ Also would reduce the attack surface of the seed node not having any protocol logic     

> __< plowsof >__ hola Lovera     

> __< plowsof >__ ofrnxmr: monero dot fail is pretty un - recommendable for finding a tor node lol https://monero.fail/?chain=monero&network=mainnet&onion=on      

> __< ofrnxmr >__ Boog, the idea is for the seed node to ONLY do peerlists?      

> __< b​oog900:monero.social >__ Pretty much     

> __< ofrnxmr >__ Yeah, i have tor/i2p nodes, but my service provider just chanced my ip so idk if i'd provide an ipv4 seed      

> __< b​usyboredom:tchncs.de >__ Joining late, but I'm here.     

> __< p​lowsof:matrix.org >__ was contemplating moving meetings 2 hour later to 18:00 in the future     

> __< b​tclovera:matrix.org >__ No problem.  It is a good time     

> __< ofrnxmr >__ Loverraaa      

> __< p​lowsof:matrix.org >__ shou-out to datahoarder the `m-relay` maintainer. he's launched an app service bridge that is feature packed and is in active testing in all p2pool rooms     

> __< p​lowsof:matrix.org >__ News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [Monero Moon](https://www.themoneromoon.com/)     

> __< p​lowsof:matrix.org >__ #p2pool-bridge-test:bridge.p2pool.observer     

> __< p​lowsof:matrix.org >__ we  can move on to ccs updates if nothing else to bring up     

> __< ofrnxmr >__ We found 0.1xmr or so     

> __< ofrnxmr >__ No, we found 1xmr     

> __< p​lowsof:matrix.org >__ and lost 0.01 xmr which i owe to geonic     

> __< p​lowsof:matrix.org >__ would you like to share an update on your proposalLovera ?     

> __< p​lowsof:matrix.org >__ forgot to make a payout request i hear. and BusyBoredom is here 💪     

> __< b​usyboredom:tchncs.de >__ If lovera is afk for a few, I can give my brief update     

> __< p​lowsof:matrix.org >__ please do, thank you     

> __< b​usyboredom:tchncs.de >__ AcceptXMR update: working on the WordPress plugin, it's functional but ugly and the currency conversion is unreliable. I'm in the process of prettying it up and caching conversion rates to smooth out the rough edges.     

> __< b​usyboredom:tchncs.de >__ Taking inspiration on currency conversion handling from monero integrations, they have a great solution.     

> __< p​lowsof:matrix.org >__ recanmann should hopefully have an monero integrations update for us     

> __< p​lowsof:matrix.org >__ thanks for pushing this along BusyBoredom, how are they handling conversions? multiple sources?     

> __< d​iego:cypherstack.com >__ hi     

> __< b​usyboredom:tchncs.de >__ They've got a job spinning every X seconds to fetch conversion rates from coingecko and stuff them in the DB, then the gateway gets rates from the DB with no direct dependency on coingecko.     

> __< b​usyboredom:tchncs.de >__ Doesn't look like that have multiple sources, but the solution would scale well for that and its something I'm considering.     

> __< p​lowsof:matrix.org >__ indeed, sounds great 👍️ (Rucknium has a nice price fetcher idea in use on monerofund iirc) Lovera claim your funds thanks     

> __< b​tclovera:matrix.org >__ Ok in here again. Sorry guys, was afk.      

> __< b​tclovera:matrix.org >__ Yes, sorry but I forget to write my last update for the last milestone.      

> __< b​tclovera:matrix.org >__ I will update it today as Since I wanted to mention it at the meeting first     

> __< p​lowsof:matrix.org >__ yes i checked your socials and noticed you where still active doing monero things     

> __< plowsof >__ thanks for joining, will look out for your update comment 👍     

> __< plowsof >__ i think we can move on to merges.. not much changes to discuss on the first 2     

> __< ofrnxmr >__ Just that noshore posted a comment     

> __< plowsof >__   a. [NoShore: Groundwork for on-the-go offline payments](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/525)         

> __< plowsof >__ yes, they want to complete the work and seek retroactive funding , at the latest in april. regardless, i wont be bringing it up in meetings until then, or, close and re-open with a retro funding request.     

> __< plowsof >__ thoughts?     

> __< ofrnxmr >__ In the meantime, they should prob not wait for us and try to raise the funds      

> __< ofrnxmr >__ Close n reopen ack     

> __< a​ntilt:we2.ee >__ ask him kindly to detail his knowlegde about the role of key images in the protocol -- this will save on precious core dev time.     

> __< plowsof >__ vthor is busy with the MoneroSigner , which involves just that       

> __< plowsof >__ the proposer has not attended any meetings are joined this room afaict      

> __< plowsof >__ s/are/or     

> __< plowsof >__ lets move on      

> __< vthor >__ here, will read     

> __< p​lowsof:matrix.org >__ oh sorry for the direct ping , hello     

> __< plowsof >__   b. [dmvp2p: Donate Monero Via P2Pool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/531)         

> __< plowsof >__ no changes with this one     

> __< vthor >__ hi plowsof, no issue. So I show at least up to a/the meeting :)     

> __< plowsof >__ somewhat related: the GUPAXX dev has started a kuno for further work https://kuno.anne.media/fundraiser/dsrr/     

> __< plowsof >__ "- Easy UI (for beginners, automate as much as possible)" - which was one negative point raised by 4rkal about GUPAXX (it has many tabs where as dmvp2p is more streamlined for mining to a donation address)     

> __< b​tclovera:matrix.org >__ I like this project, but to be honest, I don't see any differents between mining for yourself and then just send some picometos to your favorite creator or person 😅     

> __< plowsof >__ i feel the same      

> __< plowsof >__ and i like picometos      

> __< plowsof >__ i think we can move on      

> __< s​gp_:monero.social >__ It's an interesting idea but I don't expect it to lead to meaningful donations. More of a PR opportunity than something significant unfortunately     

> __< plowsof >__ 👍     

> __< plowsof >__ thanks for the feedback      

> __< plowsof >__   c. [Funding Proposal for Unstoppable Wallet: Enabling Native Monero Integration on iOS & Android](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/532)         

> __< ofrnxmr >__ Close pending feedback     

> __< plowsof >__ iirc that was the status from the prev meeting , they've not ack'd it as being real neither lol     

> __< plowsof >__ tweeting alot about monero though      

> __< ofrnxmr >__ They havent acknowledged that its their proposal, and are on a pr campaign right now. Can come back to meeting table if they ack the proposal     

> __< plowsof >__ most likely the feedback will be that the fdroid version has all features, but the stores have the pay to play stuff? (privacy related)     

> __< ofrnxmr >__ Theyve also pivoted slightly on the removal/paywall of privacy and security. Fdroid builds will be completely free, and existing gplay users will retain the ability to opt out of analytics and to use duress password. new users may have to pay for duress and ability to opt-out of analytics. So.. better, but still not there. Also dont know of theyre     

> __< ofrnxmr >__ talking about lws or a full node wallet     

> __< ofrnxmr >__ Either way, if the proposal is fake, then theyre doing it on their own so no need to discuss here. If proposal is real, they need to respond to feedback      

> __< ofrnxmr >__ Close for lack of feedback (or even acknowledgement), come back to it if they speak up     

> __< plowsof >__ leaning on not bringing it up in meetings then unless its changed      

> __< ofrnxmr >__ I'd close so they get the notification and speak up. Lol.      

> __< plowsof >__ that would be an easy way to get an alert yes     

> __< a​ntilt:we2.ee >__ +1     

> __< plowsof >__ lets move on to the most popular proposal upvoted      

> __< plowsof >__   d. [Btcpayserver plugin](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/538)         

> __< e​longated:matrix.org >__ You don’t know when some influencer can get a few thousand ppl to mine for them     

> __< ofrnxmr >__ still needs proposers to finger the pulse and realize that the plugin exists      

> __< plowsof >__ no changes so far, although someone contacted me to begin work on the open btcpayserver bounties (working on the new official btcpayserver plugin)     

> __< ofrnxmr >__ "a few throusand ppl" lol, the entire p2pool list     

> __< s​gp_:monero.social >__ This should be closed and resubmitted with the acknowledgement that the full plugin exists imo. Maybe Nicolas is done and is waiting on the Monero community to choose a maintainer? But it's currently unclear. That code hasn't been touched in 2 weeks     

> __< ofrnxmr >__ +1 sgp     

> __< e​longated:matrix.org >__ Right now yes, as there is nobody asking for such donations via mining     

> __< plowsof >__ +1     

> __< ofrnxmr >__ Nobody wants their wallet being dusted with transparent outputs      

> __< ofrnxmr >__ And by dust, i mean dust     

> __< p​lowsof:matrix.org >__ moving on while we have time , thanks for the feedback so far     

> __< p​lowsof:matrix.org >__ e. [hinto-janai full time work (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/543)     

> __< ofrnxmr >__ cuprate bros ack'd     

> __< p​lowsof:matrix.org >__ boog900 also has a proposal     

> __< p​lowsof:matrix.org >__ f. [Boog900 full time work on Cuprate (3 months) + January](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/544)     

> __< ofrnxmr >__ +1     

> __< p​lowsof:matrix.org >__ 4 months, january back pay + 3 👍️     

> __< s​yntheticbird:monero.social >__ merge x1000     

> __< s​yntheticbird:monero.social >__ both     

> __< ofrnxmr >__ Also using a flat rate. I personally dont like the "N$ + Nxmr"     

> __< p​lowsof:matrix.org >__ it makes one number lower and when monero is 100k devs get more moneys, do you want them to starve?     

> __< ofrnxmr >__ I dont see any reason for it. Pick a side     

> __< ofrnxmr >__ I dont even like pricing in $ to begin with. Its not like we reimburse volatility      

> __< p​lowsof:matrix.org >__ semi related : the 2024 estimated xmr ~ $ ccs earnings https://gist.github.com/plowsof/0401c4823b842580cd0cb1d27b380150     

> __< ofrnxmr >__ jeffro's latest ccs was priced in xmr, cuz hes based     

> __< ofrnxmr >__ He used to write a paragraph about how to calculate the amount     

> __< ofrnxmr >__ 2 proposals remain in funding required: https://ccs.getmonero.org/funding-required/ xmrchat and v1docq47(xmr.ru)     

> __< ofrnxmr >__ Jeffro and sneedlwoods dev ccs' were merged after the last meeting. Both reached their funding goals     

> __< plowsof >__ ccs payout waiting list: ofrnxmr, tobtot, selsta, rottenwheel     

> __< plowsof >__ tobtoht*     

> __< plowsof >__ the general fund contributed to jeffro and sneedlewoods proposals      

> __< plowsof >__ thanks all for attending, any other business?     

> __< ofrnxmr >__ Need to deduct the 0.01xmr from your next pay     

> __< b​tclovera:matrix.org >__ Is there any set time that the proposal should be funded?     

> __< ofrnxmr >__ Nope     

> __< b​tclovera:matrix.org >__ I mean, is there a time limit in which a proposal must be funded? I don't remember     

> __< plowsof >__ the community has sent 15 xmr  from netrik ccs  coordinator to v1dos proposal to help      

> __< ofrnxmr >__ Yeah, nope (lovera)     

> __< b​tclovera:matrix.org >__ 👍🏻👍🏻     

> __< ofrnxmr >__ Plowsof, soon we'll actually send THE funds 😅      

> __< plowsof >__ v1do is working on the proposal. his first update 3 days ago https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/517#note_28675     

> __< plowsof >__ also the monerokon meeting started 7 mins ago     

> __< ofrnxmr >__ rip. Thanks everyone      

> __< plowsof >__ for those interested. an end to the meeting, thanks for joining all      

> __< b​tclovera:matrix.org >__ Thanks 🙏🏻     

> __< plowsof >__ ofrnxmr pls remember via outreach i helped raise a staggering 0.07 monero via https://ccs.getmonero.org/proposals/ccs_test_update.html      

> __< plowsof >__ i hope this is taken into consideration for the 0.01 i owe      

> __< plowsof >__ the proposal was also overfunded by more than 100%     

> __< s​pirobel:kernal.eu >__ I want to mention I am also done with my ccs. I managed to make the checkout dynamic and keep it javascript free at the same time https://www.youtube.com/watch?v=ldyXZB9v31k     

> __< s​pirobel:kernal.eu >__ writing writeup now     

> __< plowsof >__ thanks for the update spirobel      

> __< plowsof >__ spirobel you need that 1 click highlight html hack on the address      

> __< plowsof >__ ux score -1      

> __< o​frnxmr:xmr.mx >__ plowsof @plowsof:matrix.org  i also donated 0.069xmr     

> __< plowsof >__ thank you     

> __< plowsof >__ wait, it was not over 100% funded, it was 0.069 overfunded lol     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-02-15T10:34:02+00:00
- Closed at: 2025-03-26T23:54:09+00:00
