---
title: 'Monero Community Workgroup Meeting: Saturday 31th August 15:00UTC'
source_url: https://github.com/monero-project/meta/issues/1065
author: plowsof
assignees: []
labels: []
created_at: '2024-08-28T22:23:04+00:00'
updated_at: '2024-09-06T20:05:29+00:00'
type: issue
status: closed
closed_at: '2024-09-06T20:05:29+00:00'
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
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [New Monero Website](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/450)   placeholder / draft   
  b. [Haveno Multi-Platform Native App For Every OS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/489)    wishes to be merged into work in progress and be funded entirely by the abandoned / now void haveno front end proposal [gitlab comment for details](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/489#note_25985)
  c. [Offline Signing Library for XmrSigner Production](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/495)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1060)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2024-09-06T20:05:19+00:00
Logs 
> __< plowsof >__ meeting in      

> __< plowsof >__ 2hr35 mins allegedly https://github.com/monero-project/meta/issues/1065      

> __< plowsof >__ the "modularize monero" proposal from vthor is going to be drastically refined/edited after receiving feedback from rbrunner / tobtoht / kayabanerve to whom i am deeply thankful for      

> __< plowsof >__ kewbit has changed his haveno UI from funding required to work in progress. if we agree on this then it will be funded from the now void haveno front end proposal and work would begin immediately upon merge      

> __< plowsof >__ and 270 xmr was recently donated from the general fund to proposals on the funding required page https://nitter.poast.org/WatchFund/status/1829852188648357909#m      

> __< f​reeross:monero.social >__ m-relay: does this affect the haveno-web UI bounty?     

> __< plowsof >__ no     

> __< s​pirobel:kernal.eu >__ https://x.com/spirobel/status/1829742700876480690 kuno still stuck at 2 percent funding.     

> __< s​pirobel:kernal.eu >__ might have to go the ccs route after all.     

> __< s​pirobel:kernal.eu >__ but reading the comments by kaya it seems like he wants to eat that as well     

> __< w​oodser:monero.social >__ hey so, thinking about this, we (kewbit and I) are interested to work together to create the new haveno ui     

> __< plowsof >__ awesome woodser     

> __< w​oodser:monero.social >__ essentially thinking to:     

> __< w​oodser:monero.social >__ - find designer(s)     

> __< w​oodser:monero.social >__ - improve the design of the desktop application, incorporating "wizard" elements from bisq2     

> __< w​oodser:monero.social >__ - design for mobile     

> __< w​oodser:monero.social >__ - kewbit is the lead dev for delivering the apps     

> __< s​pirobel:kernal.eu >__ WHAT ABOUT ME lol     

> __< plowsof >__ spirobel you hate the ccs leave us alone please     

> __< w​oodser:monero.social >__ maybe there are good ways for you to help too, especially if you are familiar with dart/flutter?     

> __< s​pirobel:kernal.eu >__ i hate getting fucked over like the last time     

> __< s​pirobel:kernal.eu >__ i started a ccs     

> __< w​oodser:monero.social >__ we can talk more about this, there will be a lot to develop     

> __< k​ewbit:matrix.org >__ Designers for sure, if you're not already happy with the desktop version in Figma done before by the previous devs, this can still be mimicked in Dart, albeit, with some time. I am working on Wizard elements since this morning actually, I'm making sure the user journey is clear and swift. Just playing around with different ideas but, for the app versions, these journeys will be qu<clipped message>     

> __< k​ewbit:matrix.org >__ ite simple, you fill out some info on one page and then on the next. We have a bit more real estate on desktop screens so will likely not ultimately be the same design but the first version will be the same design. I'll bare in mind that there is some favour around the wizards in bisq 2 and use it as some inspiration.     

> __< k​ewbit:matrix.org >__ I have been keeping a very very close eye on bisq 2 anyway, they don't have a daemon yet... but it's on my todo list to see if there is any unique problems they're solving with that that we might be able to use, extend functionality on without completely switching to it!     

> __< 3​21bob321:monero.social >__ Holy shit batman     

> __< s​pirobel:kernal.eu >__ you are getting paid for by the community to be impartial. maybe time to get rid of you if you dont act the part     

> __< w​oodser:monero.social >__ for sure we want to incorporate designers and their input in the process. they should really lead the design with us     

> __< s​pirobel:kernal.eu >__ what is the point in using dart and flutter?     

> __< s​pirobel:kernal.eu >__ thats an outdated dead technology     

> __< s​pirobel:kernal.eu >__ waste of ressources     

> __< s​pirobel:kernal.eu >__ waste of resources     

> __< w​oodser:monero.social >__ I figure it's between dart/flutter or web technologies (react, electron, etc)     

> __< k​ewbit:matrix.org >__ If you were not happy with the design from the previous devs? Why did it continue to get developed     

> __< w​oodser:monero.social >__ apparently dart/flutter is one of the most common choices for creating cross platform apps for mobile and desktop     

> __< k​ewbit:matrix.org >__ Is it the best choice     

> __< k​ewbit:matrix.org >__ Nothing even comes close     

> __< w​oodser:monero.social >__ design versus development was ongoing contention between erc and I, and making any design changes was a struggle after basic development began     

> __< k​ewbit:matrix.org >__ Maybe React Native comes close but meh     

> __< w​oodser:monero.social >__ but imo, design should be prioritized first, then implement the design. that's how we'd get a modern beautiful app, versus developers doing what they like     

> __< k​ewbit:matrix.org >__ Not even facebook use that anymore and they made it!     

> __< s​pirobel:kernal.eu >__ flutter is one of these dead google projects that will get killed off at some point     

> __< k​ewbit:matrix.org >__ Absolutely nonsense     

> __< s​pirobel:kernal.eu >__ react is the better choice     

> __< k​ewbit:matrix.org >__ The community is what makes flutter powerful at this point     

> __< s​pirobel:kernal.eu >__ much bigger ecosystem     

> __< s​pirobel:kernal.eu >__ google just fired the flutter team btw     

> __< k​ewbit:matrix.org >__ I have my staff working on React native projects for about a year, thinking it was a good idea, it wasn't a terrible idea. It was just an OK idea, and it was only an OK idea because we chose to do it with Expo :)     

> __< k​ewbit:matrix.org >__ It's much quicker to deliver a lot of value in Dart and I strongly suggest learning it, it's awesome.     

> __< s​pirobel:kernal.eu >__ and canonical is not going to fill the gap     

> __< k​ewbit:matrix.org >__ ahhh the community will take over     

> __< k​ewbit:matrix.org >__ 100%     

> __< s​pirobel:kernal.eu >__ lol a cto. this thing is dead. wake up     

> __< k​ewbit:matrix.org >__ New flutter update was quite recent!     

> __< s​pirobel:kernal.eu >__ look where the rest of the ecosystem is going     

> __< s​pirobel:kernal.eu >__ look at the bigger market cap coins     

> __< k​ewbit:matrix.org >__ nah not at all you're living in a fantasy land!     

> __< k​ewbit:matrix.org >__ ;)     

> __< s​pirobel:kernal.eu >__ like ethereum or solana     

> __< s​pirobel:kernal.eu >__ they are 100x our size     

> __< s​pirobel:kernal.eu >__ most of their stuff is in react     

> __< s​pirobel:kernal.eu >__ time to wake up and not invest in dying ecosystems     

> __< k​ewbit:matrix.org >__ well apparently we dont care what frameworks we use anyway, COUGH COUGH ** 'elm'.     

> __< s​pirobel:kernal.eu >__ elm smh     

> __< k​ewbit:matrix.org >__ What makes and ecosystem grow?     

> __< s​pirobel:kernal.eu >__ when people work together instead of against each other     

> __< k​ewbit:matrix.org >__ Is it the support of a top 500 company? If thats the case, why did React Native not die of when facebook stopped supporting it.     

> __< k​ewbit:matrix.org >__ Building native, generally, is a challenge, it's a learning curve people don't want to take when there are easier options like Svelte, Vue, React, Electrum. Dart itself isn't so bad but native platform channels and FFI can deter people, it is slightly more challenging to contribute to community plugins and repos so of course there may be less volume in contribution but the quality<clipped message>     

> __< k​ewbit:matrix.org >__  tends to be higher.     

> __< k​ewbit:matrix.org >__ woodser:  https://github.com/haveno-dex/haveno/issues/1236     

> __< k​ewbit:matrix.org >__ oop wrong chat     

> __< w​oodser:monero.social >__ yeah we can bring that over to #haveno-dev:haveno.network and get more notifications implemented     

> __< ofrnxmr >__ That link is totally broken btw     

> __< o​frnxmr:monero.social >__ this should work https://matrix.to/#/#haveno.exchange:monero.social     

> __< w​oodser:monero.social >__ if I copy the link from the development room, it's https://matrix.to/#/#haveno-dev:haveno.network 🤔     

> __< o​frnxmr:monero.social >__ The `haveno.network` domain is dead     

> __< o​frnxmr:monero.social >__ So it wont load unless youre already in the group     

> __< o​frnxmr:monero.social >__ The matrix space i created "should" let you join because it has the "real" address     

> __< w​oodser:monero.social >__ I guess this should be the link that works: #haveno-dev:monero.social     

> __< o​frnxmr:monero.social >__ it might, but only for monero.social users, since its a local-only address     

> __< o​frnxmr:monero.social >__ The room cant be modified to change the main addresses bcuz the admin accounts are on haveno.network     

> __< o​frnxmr:monero.social >__ `https://matrix.to/#/!HeVhOlajgOuVMOKhvS:haveno.network?via=monero.social?via=matrix.org` should work     

> __< o​frnxmr:monero.social >__ ```     

> __< o​frnxmr:monero.social >__ https://matrix.to/#/!HeVhOlajgOuVMOKhvS:haveno.network?via=monero.social?via=matrix.org     

> __< o​frnxmr:monero.social >__ ```     

> __< o​frnxmr:monero.social >__ Ffs lol     

> __< o​frnxmr:monero.social >__ https://matrix dot to/#/!HeVhOlajgOuVMOKhvS:haveno.network?via=monero.social?via=matrix.org     

> __< s​pirobel:kernal.eu >__ shit does not work     

> __< s​pirobel:kernal.eu >__ what happend to the domain?     

> __< o​frnxmr:monero.social >__ which link?     

> __< o​frnxmr:monero.social >__ This one should work     

> __< o​frnxmr:monero.social >__ so should this one     

> __< w​oodser:monero.social >__ we switched the matrix rooms from haveno.network to matrix.social a long time ago     

> __< o​frnxmr:monero.social >__ Erciccione killed the homeserver     

> __< o​frnxmr:monero.social >__ Haveno-dev was never switched     

> __< w​oodser:monero.social >__ I can take this as a todo     

> __< o​frnxmr:monero.social >__ I switched haveno room, but matrix.org shit the bed and rolled back. Not main haveno room has no address again     

> __< o​frnxmr:monero.social >__ Its not possible to change haveno-dev's main address     

> __< w​oodser:monero.social >__ ah ok. and the only admin is @woodser:haveno.network and so dead account I guess     

> __< o​frnxmr:monero.social >__ The only admins are on haveno.network, and that homeserver is dead.     

> __< o​frnxmr:monero.social >__ main haveno room has vik as admin, so that one can be fixed again.     

> __< o​frnxmr:monero.social >__ The new haveno space i created is on monero.social, so this problem shouldnt happen again     

> __< o​frnxmr:monero.social >__ I switched haveno room, but monero.social** shit the bed and rolled back. Not main haveno room has no address again     

> __< o​frnxmr:monero.social >__ Spirobel, did the haveno space link work for you?     

> __< s​pirobel:kernal.eu >__ yes. long time no see lol     

> __< s​pirobel:kernal.eu >__ remember being in the room in the good old days lol     

> __< w​oodser:monero.social >__ so if we are to take this direction of designing and implementing for mobile and desktop, it's an evolution of haveno's previous ccs (without fees contributed back, as we do not run a network), or it should be written into any updated ccs request     

> __< w​oodser:monero.social >__ so the current ccs would need updates before being merged     

> __< w​oodser:monero.social >__ so the current ccs request would need updates before being merged     

> __< k​ewbit:matrix.org >__ I agree we can expand a bit more, perhaps lets do this today, and hopefully we can move it across, like asap? 😆     

> __< plowsof >__ noted woodser, thank you      

> __< s​pirobel:kernal.eu >__ reminds me a bit of the "facoring" thing     

> __< s​pirobel:kernal.eu >__ what happend to this guy btw?     

> __< s​pirobel:kernal.eu >__ he asked me to work with him in  a twitter dm before     

> __< s​pirobel:kernal.eu >__ saying i asked the right right questions in the dev channel     

> __< s​pirobel:kernal.eu >__ and then he disappeared     

> __< s​pirobel:kernal.eu >__ lol     

> __< s​pirobel:kernal.eu >__ it is okay to have multiple libraries I think. But there needs to be a clear purpose. Not just random changes with unclear goals.     

> __< s​pirobel:kernal.eu >__ I need to have a library that eventually is robust enough to work in the browser and inside of browser extensions. It needs to be disentangled from the file system and threading. I doubt that any of the other libraries will deliver that. The goals are too different     

> __< s​pirobel:kernal.eu >__ in my mind it is crucial to have a browser wallet. even mobile wallet apps now embed browsers to interact with decentralized exchanges, do wallet login and other things. Monero seems stale in its current approach     

> __< s​pirobel:kernal.eu >__ If I look at serai and haveno I see a massive scope that is mostly building out a second decentralized p2p protocol.     

> __< r​ucknium:monero.social >__ Have you seen https://github.com/mainnet-pat/monujo-quasar ?     

> __< s​pirobel:kernal.eu >__ yes. and I have also seen monero hotshop     

> __< s​pirobel:kernal.eu >__ and my own work https://www.youtube.com/watch?app=desktop&v=4DLcsQ45zoE     

> __< s​pirobel:kernal.eu >__ and haveno     

> __< s​pirobel:kernal.eu >__ any one using crypto grampys hotshop still?     

> __< s​pirobel:kernal.eu >__ you guys dont need to see my initiative as a replacement for what you are doing. It is just a different thing with a different goal     

> __< plowsof >__ Meeting time https://github.com/monero-project/meta/issues/1065     

> __< plowsof >__ Greetings!     

> __< jorge >__ hello     

> __< vthor >__ hi :)     

> __< o​frnxmr:monero.social >__ Morning     

> __< k​ewbit:matrix.org >__ Afternoon     

> __< o​frnxmr:monero.social >__ I'll be on the road during meeting, apologies if i miss out     

> __< msvb-lab >__ Hello.     

> __< plowsof >__ as i shared earlier, 270 xmr was recently donated from the general fund to proposals on the funding required page https://nitter.poast.org/WatchFund/status/1829852188648357909#m 🚀      

> __< d​iego:cypherstack.com >__ hi     

> __< d​iego:cypherstack.com >__ Neat!     

> __< plowsof >__ cypherstack shared a report on effects of reducing moneros 10 block lock in MRL, currently being discussed there https://libera.monerologs.net/monero-research-lab/20240831#c419510      

> __< plowsof >__ anyone like to share something thats happened over the previous week?     

> __< d​iego:cypherstack.com >__ Were some pretty neat findings imo     

> __< jorge >__ Weblate is still down, I want to finish the Esperanto translation, but currently there is no way to do it :(     

> __< plowsof >__ atomic swaps are really bogged down by the 10 block lock, to name an example that would benefit greatly from any decrease there      

> __< ofrnxmr >__ its not bad     

> __< ofrnxmr >__ slower than btc<>ltc, but not bad      

> __< plowsof >__ jorge it seems as though all translations will be thrown into the trash and starting from a-fresh with a new site over the coming month(s)      

> __< plowsof >__ this is not certain of course      

> __< plowsof >__ and https://docs.getmonero.org is live . currently a work in progress      

> __< plowsof >__ it has an A rating for http headers and everything, wow look at that      

> __< ofrnxmr >__ and an onion too      

> __< vthor >__ 8)     

> __< ofrnxmr >__ http://xmrdoc6phnvjbf5hmjbwdfu47zavzfngymlnwhs2gyxxpxmad4c65kyd.onion     

> __< plowsof >__ and Rucknium has began to tackle migrating moneroresearch.info to a newer back end with better search functionality.. i had failed to put time into it sooner but i should be able to help along the way if needed     

> __< k​ewbit:matrix.org >__ Live chat between traders on haveno app now works realtime, and in general works almost flawlessly on android, implemented AES derived PBKDF2 encryption on the app data  and files, added a caching layer so failures do not occur on network fluctuations, also implemented a cooldown mechanism to not overload the daemon, currently adding the ability to generate as many stealth address<clipped message>     

> __< k​ewbit:matrix.org >__ es as you want with labels and trying to come up with a nice way of recording your history of successful trades to make it easier to trade with trusted parties again.     

> __< plowsof >__ nice     

> __< plowsof >__ i think we can jump into the open ccs ideas now?      

> __< d​iego:cypherstack.com >__ Skip the website one please.     

> __< plowsof >__ skippethd      

> __< d​iego:cypherstack.com >__ As discussed in previous weeks it's not ready due to no design yet (which I'm working on)     

> __< plowsof >__ thanks     

> __< plowsof >__   b. [Haveno Multi-Platform Native App For Every OS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/489)    wishes to be merged into work in progress and be funded entirely by the abandoned / now void haveno front end proposal [gitlab comment for     

> __< plowsof >__ details](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/489#note_25985)     

> __< plowsof >__ kewbit     

> __< plowsof >__ quite a big development on this arrived toda     

> __< plowsof >__ today*     

> __< plowsof >__  woodser began sharing his thoughts on the direction of this here https://libera.monerologs.net/monero-community/20240831#c419609      

> __< plowsof >__ seems like they are going to discuss the plan further and come back with a modified proposal      

> __< plowsof >__ anyone have opinions? happy? sad? that haveno UI is finally going to get rolling?      

> __< plowsof >__ it would presumably move into funding required after absorbing the remaining funds from the original haveno front proposal     

> __< plowsof >__ spirobel was even offered to take part if they have flutter/dart skills      

> __< k​ewbit:matrix.org >__ I agree with the prospect of bringing on a designer, that would be really helpful. We have discussedd in private chat further since that brief chat earlier today in here, the design would come into play after this 'v1' lets called it, the app will be available on all platforms however, the designing coming in would really be to focus on the aesthetics of how the desktop design wou<clipped message>     

> __< k​ewbit:matrix.org >__ ld look, I'd work closely with whoever that may be when the time comes.     

> __< h​ardenedsteel:monero.social >__ mastodon or lemmy bot is much needed     

> __< d​iego:cypherstack.com >__ CS has flutter/dart skills, and...design skills :P     

> __< k​ewbit:matrix.org >__ I think a sufficient amount of work has been done on it to justify merging it, should any further UI improvements be requires as discussed earlier, this would be part of a different project, perhaps still under the funding of the original CCS.     

> __< plowsof >__ sounds good. so we can patiently wait for the conversation to develop, resulting in changes to the proposal     

> __< plowsof >__ oh look a designer with flutter/dart skills too      

> __< s​pirobel:kernal.eu >__ can learn it in a weekend. But tbh its the wrong direction     

> __< s​pirobel:kernal.eu >__ what we need is a real browser wallet. something i have put a lot of time and effort in     

> __< s​pirobel:kernal.eu >__ that is where the rest of crypto is moving. since ages     

> __< k​ewbit:matrix.org >__ seems like we only have biasd opinons     

> __< k​ewbit:matrix.org >__ please can we bring in an external consultant     

> __< s​pirobel:kernal.eu >__ you guys can keep going in this other direction     

> __< k​ewbit:matrix.org >__ paid     

> __< s​pirobel:kernal.eu >__ bring in mckinsey     

> __< ofrnxmr >__ Hi.     

> __< s​pirobel:kernal.eu >__ LFG     

> __< k​ewbit:matrix.org >__ who does not have any bias     

> __< k​ewbit:matrix.org >__ at all     

> __< ofrnxmr >__  😆     

> __< plowsof >__ an app on the system vs a web app has advantages in terms of security, so i've been told      

> __< k​ewbit:matrix.org >__ because this is getting a bit stupid     

> __< k​ewbit:matrix.org >__ :D     

> __< s​pirobel:kernal.eu >__ is objective. use any chain above 100billion market cap     

> __< s​pirobel:kernal.eu >__ its all web based     

> __< ofrnxmr >__ Scams     

> __< s​pirobel:kernal.eu >__ i mean fine u do yours     

> __< s​pirobel:kernal.eu >__ i will not interfere or fud     

> __< s​pirobel:kernal.eu >__ have fun guys     

> __< d​iego:cypherstack.com >__ I feel web-based scams are much easier to perform than app-based ones.     

> __< plowsof >__ so kewbit is saying merge as is, woodser is saying hold off on merging. im leaning towards holding off a bit      

> __< s​pirobel:kernal.eu >__ DONT FUD MY SHIT OKAY     

> __< d​iego:cypherstack.com >__ That's why I personally have shied away from making it. But I may just be a coward there.     

> __< ofrnxmr >__ Doesnr disq react native     

> __< s​pirobel:kernal.eu >__ you never used eth or solana?     

> __< d​iego:cypherstack.com >__ I agree that adoption would be much higher and faster with web based.     

> __< d​iego:cypherstack.com >__ both are supported in Stack Wallet. Got several requests to do web-based wallet for it. Chose not to.     

> __< s​pirobel:kernal.eu >__ so maybe all the other shit is the real grift     

> __< ofrnxmr >__ Android app > webapp all day everyday     

> __< ofrnxmr >__ Ask localmoneri     

> __< ofrnxmr >__ Couldnt catch me using their website if you paid me to     

> __< d​iego:cypherstack.com >__ In other words (and not to be wishy-washy) there are non-trivial pros and cons to both directions.     

> __< k​ewbit:matrix.org >__ I pledged my 2 months though, so we can hold off but I dont see the value in it for the community. We can look for a designer in the meantime.     

> __< ofrnxmr >__ Monero waller, who uses a webwallet     

> __< s​pirobel:kernal.eu >__ all the successful wallets include browsers now     

> __< vthor >__ I try to say nothing, but the browser is the number one vunerability on a system. And this is all I will say.     

> __< ofrnxmr >__ Anyobe even uss a cex webapp?     

> __< s​pirobel:kernal.eu >__ on mobile     

> __< r​eal_glitch:matrix.org >__ unpopular opinion:     

> __< r​eal_glitch:matrix.org >__ Tauri > electron     

> __< d​iego:cypherstack.com >__ yeah it's why I'm not successful :P     

> __< plowsof >__ woodsers offer of working together on this came today, so hoding off after he said wait, seems sane .. when you as a team are on the same page, that also feels sane      

> __< plowsof >__ this would be a matter of day(s)      

> __< plowsof >__ kewbit your proposal was also made days ago. relax please      

> __< k​ewbit:matrix.org >__ I'm sure we can work in days, sure     

> __< ofrnxmr >__ all evm is evm     

> __< k​ayabanerve:monero.social >__ plowsof: atomic swaps always have to use the confirmation depth during the swap. The coins you claim from a swap, and fund a new swap with, may be burdened by the 10-block lock yet better wallet software for atomic swaps client would resolve that without modifying the lock. Sorry for being late to chime in on that.     

> __< ofrnxmr >__ Of course they use browsers, its web3     

> __< k​ewbit:matrix.org >__ I am relaxed :D     

> __< plowsof >__ thanks for clarifying kayabanerve      

> __< d​iego:cypherstack.com >__ relax further. Massage-levels     

> __< d​iego:cypherstack.com >__ the CCS will pay for one     

> __< plowsof >__ lol     

> __< k​ewbit:matrix.org >__ unfortunately non of the massage parlours around here accept XMR yet     

> __< d​iego:cypherstack.com >__ in fact, let's open the CCS for a masseuse for every contributor     

> __< d​iego:cypherstack.com >__ can't work if we're burned out ;)     

> __< k​ewbit:matrix.org >__ You joke, but it's good.     

> __< plowsof >__ certainly a gap in the market, now then ,  waiting some day(s) for woodser and kewbits friendship to flourish?     

> __< r​eal_glitch:matrix.org >__ Diego Salazar: it seems that you got your first payment for your ccs     

> __< plowsof >__ kayabanerver vthor has closed and opened another proposal btw after your and others feedback      

> __< d​iego:cypherstack.com >__ Indeed.     

> __< plowsof >__ unless we have other things to mention regarding kewbits proposal we can move on     

> __< r​eal_glitch:matrix.org >__ can you mention the works you have done in the past month? aside from bringing back ofrnxmr     

> __< d​iego:cypherstack.com >__ Yes, there was a lot of discussion and work with the new website workgroup, a fair amount of discussion and resetting expectations with the current mod team, handling a couple of small odd jobs for luigi, and a lot of testing static site generators to determine a path forward for the new website     

> __< d​iego:cypherstack.com >__ followed by a lot of design work for the new website     

> __< plowsof >__ every CCS proposer posts milestone/payout updates on gitlab, that would be the best place to query details: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/470     

> __< msvb-lab >__ It sounds like it will be very good, and using Astro.     

> __< d​iego:cypherstack.com >__ the majority of hours were for backend exploration and preliminary design work     

> __< r​eal_glitch:matrix.org >__ so most of them are claims that you worked but nothing notable for now on backend side right?     

> __< d​iego:cypherstack.com >__ LOL     

> __< r​eal_glitch:matrix.org >__ kk pls continue     

> __< d​iego:cypherstack.com >__ You want me to do a write-up of the explored SSGs as proof?     

> __< plowsof >__ lets get to vthors proposal, only a few day(s) old but has had a major re-write      

> __< d​iego:cypherstack.com >__ you want me to share some of the designed icons here?     

> __< r​eal_glitch:matrix.org >__ no i will wait for another month to see the fruit of those efforts     

> __< plowsof >__   c. [Offline Signing Library for XmrSigner Production](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/495)         

> __< d​iego:cypherstack.com >__ The fruit of the SSG exploration was that the longstanding stand still in the website room about which SSG to go with was resolved and we now have a path forward.     

> __< d​iego:cypherstack.com >__ (one second plowsof, sorry for disrupting)     

> __< s​pirobel:kernal.eu >__ what is supported? send and receive and thats it?     

> __< d​iego:cypherstack.com >__ Things were split between Astro and Hugo, with a small pocket of Jekyll people in the mix.     

> __< tobtoht_ >__ this was just submitted, but on first reading I'm positive towards vthor's updated proposal. I may have some further comments when I get a chance to look at this in more detail.     

> __< plowsof >__ that's fine, and to confirm the things diego claims to have done i seen enough of them with my own 2 eyes to substantiate the claims      

> __< r​eal_glitch:matrix.org >__ for some reason this didnt appear on CCS ideas section     

> __< s​pirobel:kernal.eu >__ why not just use wordpress with a cdn?     

> __< vthor >__ thank you tobtoht_ :)     

> __< d​iego:cypherstack.com >__ I went through a deep dive of those ones (and others) and presented my findings and we decided as a group to move forward with Astro for a variety of reasons     

> __< plowsof >__ thanks tobtoht, yes it was _just_ submitted. rbrunner, and kayabanerves feedback helped shape the new proposal. again thank you for the quick, direct, pointed feedback      

> __< d​iego:cypherstack.com >__ anyways, that's enough tangent from me, please continue as normal plowsof     

> __< d​iego:cypherstack.com >__ happy to continue this conversation after the meetinig     

> __< plowsof >__ which didnt appear on the ccs ideas section real_glitch?     

> __< s​pirobel:kernal.eu >__ i feel like collaboration would be faster and more convenient if a normal CMS was used     

> __< plowsof >__ oh i see it now, thanks...      

> __< r​eal_glitch:matrix.org >__ vthor's new proposal     

> __< vthor >__ what is supported? send and receive and thats it? In the library? Seed generation output/key images, addresses and signing.     

> __< plowsof >__ true, will have a look     

> __< plowsof >__ vthor rename the file to .md (it has no extension currently)     

> __< r​ucknium:monero.social >__ https://moneroresearch.info successfully upgraded to the new 6.10.2 WIKINDX version. Now you can see how it looks by default before plowsof put in effort to make it look better. We'll re-add the custom display templates soon.     

> __< plowsof >__ good job Rucknium      

> __< vthor >__ vthor rename the file to .md (it has no extension currently), oh, heck. Will do.     

> __< plowsof >__ spirobel was first? one of? to lead the C ABI discussions, nice to have you here      

> __< plowsof >__ also the pre-proposal-parser will show a red circle and "this is wrong pls fix" soon      

> __< d​iego:cypherstack.com >__ spirobel: I'll answer your questions in the website channel so as not to further disrupt the meeting     

> __< ofrnxmr >__ Does c abi have any crossover with monero_c by mrcyjanek     

> __< plowsof >__ when rbrunner, tobtoht, kayabanerve have time to read the new proposal it would be great to hear. not expected now as its too soon of course.     

> __< ofrnxmr >__ https://github.com/MrCyjaneK/monero_c     

> __< plowsof >__ definitely would be great to have feedback from mrcyjanek too      

> __< s​pirobel:kernal.eu >__ my comment is: we are moving to rust     

> __< s​pirobel:kernal.eu >__ base it on the new rust libs instead of the old cpp trash     

> __< vthor >__ ofrnxmr: I dunno, not aware of it, but essentialy I will use the monero source create a new folder and build a library specific for this use case which should be as static as possible and provide a C ABI to use the library in other languages. This will be or a small shim, or declaring directly in the the needed files an `external "C"` declaration.     

> __< s​pirobel:kernal.eu >__ responding to this     

> __< s​pirobel:kernal.eu >__ we have tons of those all over the monero ecosystem     

> __< s​pirobel:kernal.eu >__ i just think we should focus resources and eyes on the new rust libraries     

> __< plowsof >__ would be good if you could take a look at monero_c , its possible that theres alot to take from / use (you mention expertise in C)     

> __< s​pirobel:kernal.eu >__ that will take over everything sooner or later     

> __< ofrnxmr >__ vthor, u should look at it ;)     

> __< vthor >__ ofrnxmr: not exactly, I will avoid wallet2 completely, but thank you for the link, could be helpful.     

> __< ofrnxmr >__ Spirobel, we have 2 devs on ccs focused entirely on cuprate      

> __< plowsof >__ listed on our -site roadmap also ( syntheticbird made cuprate.org using astro - msvb-lab who seems to be a fan of astro)       

> __< s​pirobel:kernal.eu >__ >Performance: The current implementation using wallet RPC is slow,     

> __< s​pirobel:kernal.eu >__ especially on resource-constrained devices.     

> __< s​pirobel:kernal.eu >__ 100% agree with this btw     

> __< k​ayabanerve:matrix.org >__ Are we still discussing c?     

> __< k​ayabanerve:matrix.org >__ Topic c, the new signing library     

> __< vthor >__ Spirobel, I don't now if you are aware of my previous CCS I closed some hours ago, but that was out of scope, doing it on Rust, would be for sure not less scope.     

> __< plowsof >__ we re discussing vthors new proposal. the modularizing monero one was closed      

> __< s​pirobel:kernal.eu >__ vthor: seed signer is a raspi, correct?     

> __< plowsof >__ new one from vthor https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/495     

> __< vthor >__ correct pi zero     

> __< k​ayabanerve:matrix.org >__ Yes, that's what I was referring to. I just wanted to check we hadn't moved on.     

> __< plowsof >__ tangents      

> __< k​ayabanerve:matrix.org >__ I lean towards NACK due to     

> __< k​ayabanerve:matrix.org >__ > Unsigned transaction handling (description, sanity checks, signing)     

> __< k​ayabanerve:matrix.org >__ But I may be being too harsh.     

> __< s​pirobel:kernal.eu >__ so you do buildroot arm target to cross compile the cpp ?     

> __< s​pirobel:kernal.eu >__ inb4 monero-oxide     

> __< plowsof >__ more details required? or     

> __< k​ayabanerve:matrix.org >__ Verifying an unsigned transaction requires verifying effectively every field inside the TX which isn't a proof. That requires building, and comparing, every part of the transaction.     

> __< k​ayabanerve:matrix.org >__ That's several months of work.     

> __< vthor >__ I'm overwhelmed to respond to all at the same time and additional search in the webinterface to rename the file, sorry for delayed answers     

> __< k​ayabanerve:matrix.org >__ This can be done in two months. I don't believe it can be done in two months without several security issues.     

> __< plowsof >__ a response at this very moment to everything, is not required vthor      

> __< s​pirobel:kernal.eu >__ wdym i suppose this is to display the infos on the airgapped device to make sure it hasnt been messed with     

> __< s​pirobel:kernal.eu >__ essentially just displaying the info     

> __< k​ayabanerve:matrix.org >__ The airgapped device has to make the ephemeral keys and do all the derivations itself.     

> __< k​ayabanerve:matrix.org >__ It then has to tell the host computer the ephemeral keys to use for it do the proofs *unless* the airgapped device also does the proofs.     

> __< vthor >__ Verifying an unsigned transaction requires verifying effectively every field inside the TX which isn't a proof. That requires building, and comparing, every part of the transaction. Wallet RPC is not doing sanity checks?     

> __< k​ayabanerve:matrix.org >__ I'm unsure a flow for that API even exists in Monero today.     

> __< s​pirobel:kernal.eu >__ the issue is that monero oxide is not going to solve all the issues for everyone. and you need to give others some room too kaya     

> __< k​ayabanerve:matrix.org >__ vthor: If you build a new library to sign a TX, your library must check the content of the TX.     

> __< k​ayabanerve:matrix.org >__ Wow, I haven't mentioned monero-oxide at all and don't plan to.     

> __< s​pirobel:kernal.eu >__ no ccs for monero-oxide?     

> __< s​pirobel:kernal.eu >__ put the cards on the table lol     

> __< k​ayabanerve:matrix.org >__ I'm trying to have a legitimate discussion on what the flow here needs to be for this to be secure so everyone understands the timeline this work needs.     

> __< k​ayabanerve:matrix.org >__ I don't believe 2 months is the answer.     

> __< vthor >__ This can be done in two months. I don't believe it can be done in two months without several security issues. <- I can't estimate it not knowing the source well enough at the moment and I nowhere stated that it is done in two months, did I?     

> __< tobtoht_ >__ kayabanerve: I think the idea is to use cryptonote_core to handle signing, not re-implement that logic     

> __< k​ayabanerve:matrix.org >__ vthor: Clarifying, will this library do or not do the proof?     

> __< k​ayabanerve:matrix.org >__ tobtoht_: wallet2 still has fingerprintable policy rules which need to be respected.     

> __< k​ayabanerve:matrix.org >__ *proofs?     

> __< vthor >__ I'm unsure a flow for that API even exists in Monero today. <- well I was making transaction via wallet-rpc on both sides     

> __< s​pirobel:kernal.eu >__ are they well documented?     

> __< k​ayabanerve:matrix.org >__ spirobel: of course not.     

> __< plowsof >__ xD     

> __< s​pirobel:kernal.eu >__ yeah so lets work together to document them and reimplement all of this shit in rust     

> __< k​ayabanerve:matrix.org >__ Sorry, if you're using wallet-rpc, then why are you proposing a new library vthor?     

> __< s​pirobel:kernal.eu >__ we want a piece of the library pie kaya     

> __< k​ayabanerve:matrix.org >__ spirobel: Can you please stop? I'm not trying to quash this. I'm trying to work through it so there's a proper understanding. I haven't mentioned my work at all, only you have, and it's just a distraction.     

> __< s​pirobel:kernal.eu >__ nah it is not.     

> __< vthor >__ vthor: Clarifying, will this library do or not do the proof? The work will exactly done, how it would work (is working right now, with RPC), how written in the proposal I will not invent the wheel new.     

> __< plowsof >__ wallet-rpc for example takes '2-4 mins to start up on a pi' or something to that effect.     

> __< s​pirobel:kernal.eu >__ you have a horse in this race     

> __< plowsof >__ rust is iron oxide, so oxide right?     

> __< vthor >__ orry, if you're using wallet-rpc, then why are you proposing a new library vthor? Sorry, did you read, what I wrote in the answer of your comment and in the new proposal?     

> __< k​ayabanerve:matrix.org >__ vthor: I don't follow even with your comments here     

> __< vthor >__ what?     

> __< k​ayabanerve:matrix.org >__ 1) Will this library still use wallet-rpc, or replace the need for wallet-rpc?     

> __< k​ayabanerve:matrix.org >__ 2) Will this library do the full TX flow, including the Bulletproofs, or will it outsource the Bulletproofs to a more computationally-enabled device?     

> __< msvb-lab >__ Good meeting and good moderation, dankon everyone.     

> __< plowsof >__ thanks for joining msvb-lab      

> __< vthor >__ 1) of course not 2) it will do it the same way you would to it with two wallet-cli or two wallet-rpc, only eleminating all unneeded and put the need stuff clean in a library to use is then with another language. Not needing OpenSSL, not libhidusb etc.     

> __< k​ayabanerve:matrix.org >__ I can follow up on the CCS if it'd be preferred by the way :) I don't have to get my context here and now.     

> __< plowsof >__ as we're over the hour it would be best      

> __< k​ayabanerve:matrix.org >__ Got it. Thank you for clarifying that for me.     

> __< vthor >__ thank you very much, this 1h is for me like 10h of work on energy drain level view.     

> __< plowsof >__ thanks for attending the short meeting everyone, if kayabanerve has any follow up comments, much appreciated. else it can continue under the proposal     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2024-08-28T22:23:04+00:00
- Closed at: 2024-09-06T20:05:29+00:00
