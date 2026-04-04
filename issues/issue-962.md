---
title: 'Monero Community Workgroup Meeting: Saturday 03 Feb 15:00UTC '
source_url: https://github.com/monero-project/meta/issues/962
author: plowsof
assignees: []
labels: []
created_at: '2024-01-29T16:09:05+00:00'
updated_at: '2024-02-15T11:35:32+00:00'
type: issue
status: closed
closed_at: '2024-02-15T11:35:32+00:00'
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
    - [MoneroKon call for sponsors](https://monerokon.org/sponsor) 
    - [Vtnerd Dev work Q1/Q2](https://monerofund.org/projects/Q1Q2_2024_dev_vtnerd) ready for funding. Rucknium has poured many hours into this funding platform. xmr/btc/fiat can be donated with featherwallet integration. 
    - bch-xmr swap app moving ahead: [nitter](https://nitter.net/mainnet_pat/status/1751272578159644733) / [X](https://twitter.com/mainnet_pat/status/1751272578159644733) - bitcoincashautist
    - Basicswap installer that lets u use remote xmr node, no docker stuffs [github repo](https://github.com/nahuhh/basicswap-bash/releases/latest) - ofrnxmr
    - PiNodeXMR looking to integrate ETH-XMR atomic swaps [github comment](https://github.com/AthanorLabs/atomic-swap/issues/505#issuecomment-1918016723) [project repo](https://github.com/shermand100/AtomicSwap_UI)
    - [NEXT UP: A Statistical Research Agenda for Monero with Rucknium](https://odysee.com/@MoneroTalk:8/Monerotopia23:8) 
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)  |  [jeffro256](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/421#note_23289)
  a. [hinto-janai - full-time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422)    
  b. [0xfffc-2024Q1-(3 months, February, March, April, 2024)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/429)    
  c. [escapethe3RA Monero Observer maintenance (2024 Q1)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/430)    
  d. [Boog900 full time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/431)    
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2024](https://monerokon.org)
  e. Website workgroup  - CCS onion url / Weblate updates 
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.   

# Discussion History
## plowsof | 2024-02-04T19:39:43+00:00
Logs 
> __< p​lowsof:matrix.org >__ Community meeting here in <1 hour https://github.com/monero-project/meta/issues/962     

> __< p​lowsof:matrix.org >__ Meeting time https://github.com/monero-project/meta/issues/962     

> __< p​lowsof:matrix.org >__ greetings!     

> __< m​ichael:monero.social >__ Hello.     

> __< r​ucknium:monero.social >__ Hi     

> __< help >__ hi     

> __< p​lowsof:matrix.org >__ monerokons sponsor page showing that several sponsors have already signed up https://monerokon.org/sponsor , only a few slots left 👀     

> __< t​rasherdk:monero.social >__ 👍️     

> __< p​lowsof:matrix.org >__ MAGIC has put vtnerd forward for funding. Rucknium has poured many hours into this funding platform. xmr/btc/fiat can be donated with featherwallet integration. https://monerofund.org/projects/Q1Q2_2024_dev_vtnerd     

> __< ofrnxmr >__ Test..     

> __< ofrnxmr >__ K hi     

> __< p​lowsof:matrix.org >__ tobtoht doing wonderful work by adding these platforms into featherwallet.. now includes bounties / ccs and magic     

> __< p​lowsof:matrix.org >__ please share any highlights you wish to be discussed     

> __< p​lowsof:matrix.org >__ https://github.com/nahuhh/basicswap-bash/releases/tag/v0.0.8-5 is a series of bash scripts from ofrnxmr to , as i understand it, setup/use/launch basicswapdex with remote monero nodes?     

> __< ofrnxmr >__ can use remote or local, but just makes it easier to setup via prompts instead of their broken instructions (or docker)     

> __< p​lowsof:matrix.org >__ without this, xmr swaps on basicswapdex is broken?     

> __< ofrnxmr >__ Simplifies the install to copy paste > follow prompts      

> __< r​ucknium:monero.social >__ Thanks, ofrn. I read that people could not get it to run     

> __< p​lowsof:matrix.org >__ so we should definitely not list basicswapdex on getmonero until this is fixed 😅     

> __< ofrnxmr >__ Xmr swaps work 👍, just getting it to install was an issue     

> __< p​lowsof:matrix.org >__ so we definitely need more people to start using/testing basicswap dex. and ofrnxmr's is a handy entry for linux users,thanks. we need around 5-10 gb free disk space to begin? (for ltc?)     

> __< r​ucknium:monero.social >__ What is basicswapdex's business model? They don't get any revenue from the atomic swaps, right?     

> __< ofrnxmr >__ You can prune ltc and others down to 550mb. But yeah, around 10gb free space, + a reliable remote node, is enough to get started     

> __< ofrnxmr >__ 0 from the swaps     

> __< p​lowsof:matrix.org >__ good question, its possible they are swapping coins at a markup themselves?     

> __< ofrnxmr >__ They make $ on particl staking, and tx fees from part     

> __< r​ucknium:monero.social >__ When they asked for ETH<>XMR atomic swaps help they said "I can't promise much at this stage in terms of renumeration however if you are interested in helping, it's worth chatting to our team directly" https://old.reddit.com/r/Monero/comments/1ag20s6/looking_for_help_to_develop_xmreth_atomic_swap/     

> __< p​lowsof:matrix.org >__ hopefully the bch guys actually make it work https://nitter.soopy.moe/mainnet_pat/status/1751272578159644733     

> __< ofrnxmr >__ I alnost guarantee they are acting as market makers on there (tip. For testing, my ltc>xmr price is lower than trocador)     

> __< ofrnxmr >__ Eth and doge are in codebase, so i assume support coming soon     

> __< r​ucknium:monero.social >__ That would make sense. But with more market makers, their markup would disappear mostly.     

> __< ofrnxmr >__ We can add bch, and imo, should have a long time ago     

> __< p​lowsof:matrix.org >__ pinodexmr dev wants to make eth-xmr swaps easier to use / integrate them into pinode , UX++ is always appreciated     

> __< p​lowsof:matrix.org >__ SPV + monero remote nodes also for a lightweight client would be ideal     

> __< ofrnxmr >__ Yes. I fell asleep before working on eletrum, but you should be able to use remote nodes for ltc and other chains. Once i get that solved, my script will let you use remote for all     

> __< s​hermand100:matrix.org >__ Eth Xmr swaps have been live through PiNodeXMR since august. Yes, just trying to make the interface better.     

> __< s​hermand100:matrix.org >__ Also hoping the new interface may be of interest to he MoneroNodo team for them to implement swaps too.     

> __< p​lowsof:matrix.org >__ thanks shermand100 https://github.com/shermand100/PiNodeXMR     

> __< r​ucknium:monero.social >__ IMHO, adding a low-fee EVM chain plus stablecoins would help the ETH<>XMR usage.     

> __< r​ucknium:monero.social >__ Requested here recently: https://old.reddit.com/r/Monero/comments/1ah77ml/monero_usdt_swap_instead_of_btc/     

> __< p​lowsof:matrix.org >__ do people self custody usdt?     

> __< r​ucknium:monero.social >__ noot/elizabethereum implemented ERC-20 swaps in the codebase. AFAIK, it just has not been set up.     

> __< ofrnxmr >__ plowsof no     

> __< ofrnxmr >__ Look at bisq volume. Even serai is dai only      

> __< p​lowsof:matrix.org >__ and usdt can block transactions lol     

> __< r​ucknium:monero.social >__ Ok, so implement Dai instead     

> __< ofrnxmr >__ as kaya said yesterdat, usdt/usdc are a threat to the exchange      

> __< p​lowsof:matrix.org >__ maybe we could add "every time a monero atomic swap is blocked" to this bounty https://bounties.monero.social/posts/99/1-000m-freeze-interactions-bot-notifier     

> __< p​lowsof:matrix.org >__ but haveno will be built on monero :(     

> __< p​lowsof:matrix.org >__ no dai needed     

> __< ofrnxmr >__ I need to have a talk with haveno about their attempted coup     

> __< p​lowsof:matrix.org >__ updates for the ccs onion url + weblate: no progress has been made since last meeting     

> __< r​ucknium:monero.social >__ I was surprised that woodser intended to implement the Engine idea after all this time and changes.     

> __< p​lowsof:matrix.org >__ we can try again between now and the next meeting - then call it a day / hire help     

> __< p​lowsof:matrix.org >__ i think we all need a refresher from woodser about this engine setup     

> __< p​lowsof:matrix.org >__ it was a very complex graph with many arrows     

> __< ofrnxmr >__ Its trash. Simple as that     

> __< ofrnxmr >__ Its 3/5 people are hand picked, 2 community folks, and they run a competitor to ccs     

> __< p​lowsof:matrix.org >__ everyone hates the ccs and wants to decentralise it so i guess its a good thing     

> __< ofrnxmr >__ Thats not decentralizing it     

> __< ofrnxmr >__ Thats almost privatizing it     

> __< r​ucknium:monero.social >__ Adding bureaucracy when Haveno is needed ASAP seems like not a great idea. IIRC the Engine idea was when the UI was going to be made from scratch. AFAIK, the front end is mostly the same as Bisq.     

> __< p​lowsof:matrix.org >__ also sharing one more time vtnerd fund raiser https://monerofund.org/projects/Q1Q2_2024_dev_vtnerd and a self doubting comment     

> __< p​lowsof:matrix.org >__ bottom of comments here: https://bounties.monero.social/posts/90/6-200m-implement-monero-light-wallet-server-client-library-for-android-native vtnerd has forgotten he can fly     

> __< ofrnxmr >__ Regardless of what happens with vt and magic, id like to that that id be happy if he came back     

> __< ofrnxmr >__ If things work out, great. Id still like him on ccs. Far better for discussion/feedback etc     

> __< ofrnxmr >__ To fragment isnt to compliment. Haveno shoukd just yolo that much into the het fund     

> __< ofrnxmr >__ And their engine council should come vote      

> __< p​lowsof:matrix.org >__ would be nice for a small update from luigi1111 about his 'offline tx signing' adventures also  (on the subject of the ccs)     

> __< ofrnxmr >__ Luigi confirms "funds are safu"     

> __< p​lowsof:matrix.org >__ ive heard people may encounter issues with drivers for e.g. built in webcams.. usb ports etc if you are attempting a clean OS install otherwise OK     

> __< r​ucknium:monero.social >__ Maybe the Core General Fund could donate to the vtnerd fundraiser 🫣. It has not donated much to CCSes since they get funded quickly.     

> __< ofrnxmr >__ Its not donated to much bcuz theyre cheapasses     

> __< p​lowsof:matrix.org >__ Rucknium i suggested the community look at what core has donated to and decide to pre fund similar proposals with a similar % but nioCat said NO     

> __< ofrnxmr >__ A lot of the last round waa supposed to be funded by general/jetfund, but none of it was     

> __< p​lowsof:matrix.org >__ that was supposed to be the "general fund workgroup" decentralise everything pillot     

> __< r​ucknium:monero.social >__ ArticMine says he supports the MAGIC Monero Fund. Maybe that is one vote for the Core General Fund to help fund the vtnerd fundraiser.     

> __< ofrnxmr >__ oook     

> __< ofrnxmr >__ Look     

> __< ofrnxmr >__ Sgp and me dont agree on this one, but afaict 8282 means ccs cant donate      

> __< ofrnxmr >__ Tax reporting obligations of donor orgs who dispost of the donation within 3 yrs must report      

> __< r​ucknium:monero.social >__ I think those formed need to be filled and filed only if the donor wants a tax deduction. Doesn't apply to the general fund.     

> __< r​ucknium:monero.social >__ No one gets a tax deduction for donating to the CCS nor the Core general fund.     

> __< p​lowsof:matrix.org >__ (letting things roll over as 3/4 ccs proposals have been merged already. congrats hinto / escapethe3ra / 0xFFFC )     

> __< r​ucknium:monero.social >__ Anyway, SGP updated the info on the website to be more specific when people want a tax deduction.     

> __< r​ucknium:monero.social >__ https://monerofund.org/faq     

> __< r​ucknium:monero.social >__ "If you would like to receive a tax deduction, we may need to collect supplementary information such as your name and email for required record keeping. If you donate over $500 with cryptocurrencies, you will need to fill out Form 8283 and email that form to info⊙mo for us to sign Part V."     

> __< ofrnxmr >__ Sgp said its "may", if they want to claim a deduction. But reading 8282 doesnt sound like its"may" for the donee org (of course im ill informed, so lets carry on)     

> __< r​ucknium:monero.social >__ Damn, there is a typo in the email address I just noticed     

> __< r​ucknium:monero.social >__ You can tell SGP wrote it because it has a typo.     

> __< ofrnxmr >__ See??? All my noise finds problems ❤️     

> __< p​lowsof:matrix.org >__ lol     

> __< r​ucknium:monero.social >__ Sometimes yes     

> __< ofrnxmr >__ Like "Contentt" on rpc docs     

> __< p​lowsof:matrix.org >__ now then boog900 has an open proposal for cuprate work. this is the first meeting to bring it up     

> __< ofrnxmr >__ first     

> __< ofrnxmr >__ Lets mention     

> __< ofrnxmr >__ Congrats to hinto on his first curprate ccs     

> __< p​lowsof:matrix.org >__ https://github.com/Cuprate/cuprate/issues - he recently clarified licensing     

> __< ofrnxmr >__ And congrats to 0xfffc on beginning his first venture into ccs     

> __< p​lowsof:matrix.org >__ hinto has been awol for 6~ days     

> __< p​lowsof:matrix.org >__ hopefully he didnt starve to death     

> __< ofrnxmr >__ I thought he works 24hr/day     

> __< p​lowsof:matrix.org >__ https://ccs.getmonero.org/funding-required/     

> __< ofrnxmr >__ Rucknium ^ the licensing discussion may interest you     

> __< p​lowsof:matrix.org >__ d. [Boog900 full time work on Cuprate (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/431)     

> __< p​lowsof:matrix.org >__ for matrix users licensing was discussed here yesterday https://matrix.to/#/!zPLCnZSsyeFFxUiqUZ:monero.social/$WNGCb0NcAhIgmwKWdbP8BSd21UQno_kPhfFcLMzaPWw?via=monero.social&via=matrix.org&via=kyun.host     

> __< p​lowsof:matrix.org >__ <b​oog900:monero.social> every crate not in the eventual `/cuprate` sub-dir is MIT     

> __< nioCat >__ oh, a meeting     

> __< r​ucknium:monero.social >__ I don't have strong opinions on licensing, especially on code that it outside my work area.     

> __< p​lowsof:matrix.org >__ <b​oog900:monero.social> `/cuprate` doesn't exist yet     

> __< p​lowsof:matrix.org >__ <b​oog900:monero.social> Not really `/cuprate` has been AGPL for a while, what will change now are the crates specific to Cuprate will now be MIT instead of AGPL, like the DB and some P2P code.     

> __< p​lowsof:matrix.org >__ <b​oog900:monero.social> (I removed `/cuprate` a couple weeks ago as it didn't contain anything but it was AGPL and the plan was, when it was added back in, to make it AGPL)     

> __< p​lowsof:matrix.org >__ maybe its a good clarification for kayabanerve     

> __< p​lowsof:matrix.org >__ do we wait for the cuprate devs to thumb up boog900's proposal then merge it or just merge it now     

> __< ofrnxmr >__ Re boog: 3 months instead of 2, including coordinating the cuprate workgroups etc. At a glance, lgtm.      

> __< p​lowsof:matrix.org >__ we had no feedback from -dev on hintos proposal so i guess there are no blockers     

> __< ofrnxmr >__ Hinto was merged yest     

> __< p​lowsof:matrix.org >__ working 50 hours a week can lead to burnouts, something we do not want for the future of cuprate     

> __< 0​xfffc:matrix.org >__ Thanks. I am so happy to be part of Monero community.     

> __< ofrnxmr >__ hours = lies     

> __< ofrnxmr >__ Like mj billing "2hrs on toilet, 13hrs ar meetings"     

> __< ofrnxmr >__ Just because it takes ofrnxmr 5 days longer to solve a problem != he should get paid 5 days more pay than plow     

> __< r​ucknium:monero.social >__ We will pay by lines of code then :P     

> __< ofrnxmr >__ 50hrs/week = let me not make it look like im asking for 70/hr     

> __< r​ucknium:monero.social >__ This is an unsolved problem in labor economics.     

> __< ofrnxmr >__ Hinto went to the extreme and claimed 3/hr at 24hrs/day 🙈     

> __< r​ucknium:monero.social >__ I understand your point. IMHO, we need closer review of what has been done by qualified people, but is there an incentive for them to perform the review?     

> __< ofrnxmr >__ Ruined it for everyone      

> __< ofrnxmr >__ I think im ok with simply trusting the dev     

> __< p​lowsof:matrix.org >__ i work 3 hours per day. as 4 hours would entitle me to a paid lunchbreak which is a waste of community funds and detrimental to my health     

> __< ofrnxmr >__ If you say you want 40xmr/mth for this work. Ok. Dont lie to me about how many weeks its going to take you     

> __< p​lowsof:matrix.org >__ 8 hours would be 2 full ohurs of all you can eat ... this is simply unsustainable     

> __< p​lowsof:matrix.org >__ (psst, selsta, small issue with your merge request, seems like your branch is == master)     

> __< selsta >__ hmmmm     

> __< selsta >__ will fix it     

> __< ofrnxmr >__ And um     

> __< ofrnxmr >__ Plowsof ccs needs to be ended/collected for jan 24 (quit it with your 6 months / half rate)     

> __< ofrnxmr >__ s/ended/renewed     

> __< ofrnxmr >__ And selsta needs a raize     

> __< p​lowsof:matrix.org >__ ive been busy being the website coordinator     

> __< p​lowsof:matrix.org >__ need to get merges done then return to ccs sorry for my absence     

> __< ofrnxmr >__ We have 200xmr /yr available for site work      

> __< p​lowsof:matrix.org >__ e. selsta part-time monero development (3 months)     

> __< p​lowsof:matrix.org >__  (3 months) https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/432     

> __< r​ucknium:monero.social >__ And Bounties coordinator. Maybe expand your formal scope.     

> __< ofrnxmr >__ Ruck - he needs to collect his pay too 🙈     

> __< ofrnxmr >__ Hes litetally does his full scope for half rate EVERYTIMEEE . Then adds on much much extra     

> __< selsta >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/433 <-- correct source branch now     

> __< p​lowsof:matrix.org >__ thanks selsta     

> __< p​lowsof:matrix.org >__ selsta new merge request for a  further 3 months +1     

> __< p​lowsof:matrix.org >__ just missing the amount: in the front matter selsta     

> __< selsta >__ done     

> __< p​lowsof:matrix.org >__ my 4 year plan includes a period of 'what does plowsof even do' so keeping the extra things quiet so reddit hates me, means i have to be saved by the community and obtain a second wind     

> __< p​lowsof:matrix.org >__ i have also accepted my weight gain and stopped wearing jeans so more community funds will not help me     

> __< p​lowsof:matrix.org >__ ok voting on selsta if anyone is still here / later     

> __< p​lowsof:matrix.org >__ ajs_ is moving at lightning speed over at events, putting all the pieces together     

> __< p​lowsof:matrix.org >__ any other business? thank you all for attending     

> __< luigi1111 >__ Offline signing works fine just have to use an external webcam     

> __< m​ichael:monero.social >__ You're welcome and dankon very much for the good moderation and great meeting.     

> __< plowsof >__ great to hear , thanks for the update luigi     

> __< plowsof >__ thanks msvb, who is currently : FOSDEM??     

> __< m​ichael:monero.social >__ Yes.     

> __< m​ichael:monero.social >__ We distributed Kastelo enclosures but they ran out in twenty minutes.     

> __< plowsof >__ wow      

> __< r​ucknium:monero.social >__ luigi1111: Would Core consider donating to vtnerd's fundraiser from the General Fund? https://monerofund.org/projects/Q1Q2_2024_dev_vtnerd     

> __< m​ichael:monero.social >__ So we are just walking around now with nothing to do and it's raining outside.     

> __< plowsof >__ lol thank you for your sacrifices msvb      

> __< luigi1111 >__ Does that require kyc?     

> __< plowsof >__ only if the general fund wants a tax deduction ->  ping Rucknium     

> __< r​ucknium:monero.social >__ l​uigi1111: Donors do not have to KYC. Recipients of the fund (vtnerd in this case) do have to KYC.     

> __< plowsof >__ please note that MAGIC put forward the proposal without any community discussion      

> __< ofrnxmr >__ luigi1111 not really YOUR problem, in any case     

> __< ofrnxmr >__ If any problems, it would be magics     

> __< plowsof >__ as they are a separate entity      

> __< luigi1111 >__ Ah. I don't run the genfund but can talk to bf     

> __< ofrnxmr >__ also that vtnerd wants feedback     

> __< plowsof >__ so who wants to join the general fund workgroup :(     

> __< r​ucknium:monero.social >__ Thanks luigi     

> __< plowsof >__ if anyone would like to vote on selsta merge request while they are here , please do so     

> __< ofrnxmr >__ oh of course. Selsta ks due for renewal tol right?      

> __< plowsof >__ yes, some issue with it not displaying but its up now     

> __< r​ucknium:monero.social >__ Ok MAGIC will do more community discussion next time.     

> __< ofrnxmr >__ Too*. Id just ask selsta to give themself a small raise if they havent      

> __< r​ucknium:monero.social >__ +1 selsta     

> __< ofrnxmr >__ cuprate setting new standards for dev pay     

> __< selsta >__ ofrnxmr: should I change it to 50€?     

> __< plowsof >__ in the case of vtnerd's proposal - he has so many things he is capable of doing so many things (like tobtoht) its best to let them have an idea of where people want them to focus their time on      

> __< r​ucknium:monero.social >__ I think MAGIC has done enough community discussion in MRL about the University of Zurich proposal. And gotten feedback from isthmus and ACk-J     

> __< ofrnxmr >__ selsta yes      

> __< ofrnxmr >__  selsta moving from 112 > 124 xmr, sound good? Rucknium plowsof     

> __< selsta >__ yes     

> __< plowsof >__ sorry wrong account, yes      

> __< ofrnxmr >__ 😂     

> __< r​ucknium:monero.social >__ On that topic, has anyone else noticed that jeffro256 is working on a lot of non-Seraphis/Jamtis things now, but his CCS said he would work on Seraphis/Jamtis?     

> __< ofrnxmr >__ If rbrunner and seraphis arent complaining, imo its ok. Hes fixing issues     

> __< plowsof >__ why work on core/serpahis when theres 50 hours a week on cuprate      

> __< r​ucknium:monero.social >__ I think a lot of Monero devs are underpricing themselves. 112 -> 124 XMR for Selsta is an improvement.     

> __< selsta >__ rucknium: he is currently working on something I asked     

> __< r​ucknium:monero.social >__ Thanks for the info, selsta.     

> __< plowsof >__ i think we can have an open end to the meeting here?     

> __< plowsof >__ sorry for going over      

> __< ofrnxmr >__ yep. Selsta to merge afer rate change     

> __< ofrnxmr >__ Whats the consensus on boog?     

> __< p​lowsof:matrix.org >__ #monero-events:monero.social meeting in 1 hour 30 mins~     

> __< p​lowsof:matrix.org >__ what was the consensus on hinto?     

> __< nioCat >__ you sure it's not 30 minutes     

> __< nioCat >__ +1 selsta      

> __< s​gp_:monero.social >__ Lol     

> __< nioCat >__ events meeting at 1700 UTC     

> __< selsta >__ ty everyone     

> __< s​gp_:monero.social >__ This is incorrect     

> __< r​ucknium:monero.social >__ sgp_: Please give luigi and bF any info they need to consider a general fund donation to vtnerd's fundraiser     

> __< p​lowsof:matrix.org >__ 8282 means ccs can't donate -> This is incorrect     

> __< r​ucknium:monero.social >__ And IRC cannot see what Matrix message you are replying to     

> __< s​gp_:monero.social >__ Ok     

> __< s​gp_:monero.social >__ MAGIC can receive donations without info from the donor, but we do need info if that donor will claim a deduction. That's where those forms come into play     

> __< p​lowsof:matrix.org >__ and consensus on boog, this is the first its been brought up. a comment from those who care about licensing perhaps? kayabanerve? can serai benefit form a AGPL 'cuprate' folder?     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2024-01-29T16:09:05+00:00
- Closed at: 2024-02-15T11:35:32+00:00
