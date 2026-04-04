---
title: 'Monero Community Workgroup Meeting: Saturday 14th Sep'
source_url: https://github.com/monero-project/meta/issues/1072
author: plowsof
assignees: []
labels: []
created_at: '2024-09-11T18:51:05+00:00'
updated_at: '2024-10-03T19:21:14+00:00'
type: issue
status: closed
closed_at: '2024-10-03T19:21:14+00:00'
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
    - We're excited 
    - Chainalysis video leak and the cointelegraph chronicles
    - Audit a Carrot?
    - https://github.com/openalias/openalias-spec
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  a. Design competition for the new getmonero Site?  
  b. [Haveno Multi-Platform Native App For Every OS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/489)    
  c. [Offline Signing Library for XmrSigner Production](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/495)    
  d. [Revuo Monero Maintenance (2024 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/496)    
  e. [Spirobel: Robust and modular wallet-rpc library](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/501)  
  f. [Part-time Work on getmonero.org (2 Month)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/502) 
  g. [CCS Coordinator - plowsof](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/503)   
  h. Proposal closures / Return funds to General Fund.  
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1065)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2024-09-26T08:26:45+00:00
Logs 
> __< plowsof >__ Meeting in 1 hour, 36~mins https://github.com/monero-project/meta/issues/1072      

> __< o​cean:matrix.thisisjoes.site >__ Banhammer: BanhammerMonero: plz ban this hs from -markets kthx     

> __< plowsof >__ Meeting time https://github.com/monero-project/meta/issues/1072      

> __< plowsof >__ greetings!     

> __< o​frnxmr:monero.social >__ Hi     

> __< geonic >__ хола     

> __< m​ichael:monero.social >__ Hello.     

> __< geonic >__ hola     

> __< vthor >__ Hi!     

> __< geonic >__ sorry was on my KGB keyboard     

> __< plowsof >__ We're excited to see everyone joining this meeting! if you take a look at @moneros tweets, instead of only "we're excited tweets" we have a mixture https://xcancel.com/monero      

> __< geonic >__ (:     

> __< plowsof >__ they mentioned jeffros Carrot 🥕 also https://xcancel.com/monero/status/1834292929877180697#m      

> __< k​ewbit:matrix.org >__ Hi     

> __< plowsof >__ so it seems an effort is being made to mix things up on the monero handle      

> __< plowsof >__ "Chainalysis video leak and the cointelegraph chronicles" -> fluffypony made a twoot https://xcancel.com/fluffypony/status/1833962340502696113#m      

> __< plowsof >__ quite the streissand effect, seeing alot of community members share their hosted versions of the film also     

> __< o​frnxmr:monero.social >__ Off topic for this meeting, but isnt there some added confusion / migration if were going from cryptonote > carrot > jamtis? 3 diff addresseses?     

> __< o​frnxmr:monero.social >__ k4r4b3y:  waz featured in fluffy's tweet     

> __< s​pirobel:kernal.eu >__ hi     

> __< plowsof >__ hello     

> __< plowsof >__ also sgp / fluffypony contributing to openaliasv2 - theyre quite a long way and are beginning testing  https://github.com/openalias/openalias-spec #openalias     

> __< plowsof >__ is carrot (https://github.com/jeffro256/carrot/blob/master/carrot.md) built on top of jamtis?      

> __< vthor >__ Probably also off topic, but could there be a map on monero-docs, for all this things, I realize the first time that Carrot has something to do with monero :/ How you all stay productive and keep track of all going on around?     

> __< plowsof >__ might even receive an implementation audit before jamtis.. will be following mrl/nwlb meetings      

> __< o​frnxmr:monero.social >__ A map?     

> __< o​frnxmr:monero.social >__ Monero-docs is still a WIP, the folder structure etc isnt set yet     

> __< o​frnxmr:monero.social >__ Afaik, carrot is an alternative to jamtis     

> __< o​frnxmr:monero.social >__ Not directly related     

> __< plowsof >__ JAMTIS++     

> __< vthor >__ yeah, where possible inclusions or sure inclusions are in some graph, and some timeline or event updates     

> __< o​frnxmr:monero.social >__ a roadmap?     

> __< vthor >__ Sorry, for being that vague, I don't have a good idea (yet) how to archive that - only one of my thought what should exist     

> __< plowsof >__ when it picks up more input from MRL / implementation audits we'll know its the more likely the direction. (unless the committee has decided??)     

> __< o​frnxmr:monero.social >__ Adding stuff like jamtis, fcmp, bulletproofs etc should all be in the plans     

> __< o​frnxmr:monero.social >__ The developer/cryptography section is pretty light atm, even missing randomx     

> __< geonic >__ 28 mentions of jamtis in the proposal, so yeah seems like it's building on top of it     

> __< vthor >__ Not really a roadmap, how somehow some things are not yet sure (I guess - if and when they will be implemented - but somehow to not loose track of parallel ongoing things who could influence the source you are working on later..     

> __< geonic >__ I mean in the readme     

> __< plowsof >__ yep tevador and jeffro mashup      

> __< plowsof >__ i think the glaring benefit would be monero-lws implementations with more privacy when compared to what we have now     

> __< plowsof >__ any other highlights to touch on before we get to ccs proposal ideas?     

> __< plowsof >__ News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [Monero Moon](https://www.themoneromoon.com/)         

> __< r​ucknium:monero.social >__ vthor: Follow discussions in the weekly Wednesday meeting in #monero-research-lab     

> __< r​ucknium:monero.social >__ What's certain and uncertain in long-term development will be a matter of opinion.     

> __< r​ucknium:monero.social >__ So you can follow discussions and form your own :)     

> __< vthor >__ rucknium, thank you, is this room also logged, and are the meatings always same day/time or how to keep track best to no miss anything?     

> __< plowsof >__ thanks Rucknium, vthor all meetings are scheduled on monero-meta repo. ok lets move on.  The "new website" proposal awaits confirming of the consensus the the website workgroup gained consensus on. i think its best we just leave it at that and      

> __< o​frnxmr:monero.social >__ The one thing to comment abt the website     

> __< plowsof >__ leave it at that, unless anyone wants to give input. they have proposed a competition / comparing of sorts. and feedback of the wider audience is being gathered, monerobull made reddit / monero.town threads   a. Design competition for the new getmonero Site?       

> __< r​ucknium:monero.social >__ Yes, always logged at https://libera.monerologs.net/monero-research-lab and https://github.com/monero-project/meta/issues?q=is%3Aissue+%22Monero+Research+Lab%22     

> __< k​ewbit:matrix.org >__ The new Monero website looks bloody amazing     

> __< o​frnxmr:monero.social >__ Is that there is a sort of competition/vote     

> __< r​ucknium:monero.social >__ Always Wednesdays at 17:00 UTC     

> __< k​ewbit:matrix.org >__ Proposal     

> __< m​onerobull:matrix.org >__ Currently a lot of feedback likes the old design too     

> __< o​frnxmr:monero.social >__ There are a fee design candidates. 1. Keep as is, add dark mode etc. 2. Hammermans design. 3. diegos's design(s) 4. Other     

> __< o​frnxmr:monero.social >__ I dont have the reddit link that has the previews     

> __< vthor >__ rucknium, cool, thank you ver much! :)     

> __< plowsof >__ searching monero.town for monerobulls thread     

> __< o​frnxmr:monero.social >__ monero.town blocks tor so no can do lok     

> __< plowsof >__ https://monero.town/post/4289749     

> __< plowsof >__ there is a mirror on reddit also.      

> __< geonic >__ https://www.reddit.com/r/Monero/comments/1felb8e/the_future_of_getmoneroorg_looking_for_feedback/     

> __< plowsof >__ thank you!     

> __< geonic >__ seems like ~80% of the comments want to stick with the old design     

> __< geonic >__ i.e. current one     

> __< plowsof >__ and the next website meeting is tomorrow https://github.com/monero-project/meta/issues/1073     

> __< plowsof >__ diegos design is just too powerful, even 10 years later the people still want it      

> __< o​frnxmr:monero.social >__ Thanks geo     

> __< geonic >__ btw Hammermann's proposal is 3+ years old     

> __< geonic >__ https://libera.monerologs.net/monero-site/20210831     

> __< plowsof >__ i thinks we can move on with a somewhat full picture of the "new site" gate      

> __< plowsof >__   b. [Haveno Multi-Platform Native App For Every OS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/489)         

> __< plowsof >__ when merge?      

> __< o​frnxmr:monero.social >__ My only comment on this ^ is that the milestone payouts should have some correlation with the mikestones     

> __< k​ewbit:matrix.org >__ I will make some minor adjustments     

> __< plowsof >__ description must == proposal but kewbit is aware, only some small changes      

> __< o​frnxmr:monero.social >__ Currently they are set to specific dates (that may or may not be in line with the work)     

> __< plowsof >__ woodser is on-board also     

> __< o​frnxmr:monero.social >__ +1     

> __< geonic >__ are the basicswap payouts correlated to milestones?     

> __< w​oodser:monero.social >__ here's my only concern     

> __< o​frnxmr:monero.social >__ Yes     

> __< plowsof >__ merge to work in progress using a portion of funds from the old project. team 'we want a web app'  have 100xmr~ bounty dedicated to the funding of such     

> __< w​oodser:monero.social >__ the haveno ccs was to create a desktop ui     

> __< plowsof >__ hi woodser     

> __< w​oodser:monero.social >__ if funds are repurposed from haveno funds for the mobile app, it will likely affect our ability to finish design and implementation of the full desktop app     

> __< o​frnxmr:monero.social >__ Haveno desktop ui ccs shoukd be forfeitted anyway     

> __< m​onerobull:matrix.org >__ I think the funding is enough to get the desktop UI concept implemented     

> __< o​frnxmr:monero.social >__ all sorts of promises were made that can and will never be kept     

> __< plowsof >__ there will be a desktop app + ui from kewbits proposal. its my understanding that 'fine tuning' of the ui may be needed for desktop? but this can be future work?      

> __< w​oodser:monero.social >__ we have plans to evolve the mobile app being developed into a desktop version, as the base framework will be established     

> __< w​oodser:monero.social >__ kewbit's proposal is for a desktop daemon and mobile app with ui, and the desktop ui will be primitive (correct me if I'm wrong)     

> __< k​ewbit:matrix.org >__ The desktop app as mentioned in our discussions. before woodser can and will be implemented natively as well which conforms to the original design specifics it seems there is also a bounty that FreeRoss is working on that may also suit those needs from a separate funding angle.     

> __< plowsof >__ the 100 xmr is for a "web app" alternative, we do have supporters of this      

> __< k​ewbit:matrix.org >__ So you got two options though it’s likely that one will deprecate the other     

> __< geonic >__ how much is sitting in the haveno ui CCS?     

> __< w​oodser:monero.social >__ we only have ~413 xmr remaining in haveno ccs last I knew, so if 215 go to mobile app, we probably would not have enough to finish design/implementation of full desktop app     

> __< k​ewbit:matrix.org >__ So you got two options though it’s likely that one will deprecate the other **possibly     

> __< m​onerobull:matrix.org >__ I think webui is a waste of money     

> __< o​frnxmr:monero.social >__ Open a new ccs     

> __< m​onerobull:matrix.org >__ App + daemon with a nice GUI benefits us much more     

> __< o​frnxmr:monero.social >__ Old one failed miserably     

> __< plowsof >__ thanks woodser, funding a multi OS app that is fine tuned for mobile, and functional / not so fine tuned for desktop is a huge improvement than nothing      

> __< m​onerobull:matrix.org >__ Kewbit has basically already built the entire app with zero funding     

> __< m​onerobull:matrix.org >__ So I'm confident they can realize GUI + app     

> __< o​frnxmr:monero.social >__ haveno desktop UI ccs should be jetfunded and funds used for new proposals (like kewbits)     

> __< geonic >__ can someone link to the Haveno ccs     

> __< k​ewbit:matrix.org >__ Please remember that the functional usage of the mobile app works just as well as it does on the mobile, so this does not block the desktop usage upon release. The v2 to complete the desktop design as per the Figma in the haveno-dex repo is a nice to have and I’m sure there will in fact be enough funding, even there is not, i will pledge to contribute a certain amount of hours as a noble cause.     

> __< o​frnxmr:monero.social >__ https://ccs.getmonero.org/proposals/haveno-frontend.html     

> __< o​frnxmr:monero.social >__ The ccs makes all sorts of bs backend promises and kept 0     

> __< geonic >__ woodser: are you expecting to complete that ccs?     

> __< k​ewbit:matrix.org >__ Please remember that the functional usage of the desktop app works just as well as it does on the mobile, so this does not block the desktop usage upon release. The v2 to complete the desktop design as per the Figma in the haveno-dex repo is a nice to have and I’m sure there will in fact be enough funding, even there is not, i will pledge to contribute a certain amount of hours as a noble cause.     

> __< m​onerobull:matrix.org >__ Kewbit da goat 🐐     

> __< o​frnxmr:monero.social >__ Its invalid and should be repurposed     

> __< m​onerobull:matrix.org >__ Ofrn nobody cares about abandoned haveno CCS     

> __< plowsof >__ the merge request llooking to close the Haveno front end ccs https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/497      

> __< o​frnxmr:monero.social >__ Its impossible to complete the ccs     

> __< s​pirobel:kernal.eu >__ okay so merge and move on?     

> __< w​oodser:monero.social >__ the current plan is to start with kewbit's mobile app, then evolve that app into a full desktop version, so it would be completed eventually, yes     

> __< m​onerobull:matrix.org >__ Just assign the 400 xmr from the CCS plus the 100 from the bounty to kewbit building app + desktop figma gui     

> __< m​onerobull:matrix.org >__ Most efficient, kewbit already proved himself     

> __< geonic >__ plowsof mentions 453 xmr left, woodser says 413. are these different pools of money?     

> __< plowsof >__ did i set aside funds for myself secretly? id have to confirm      

> __< w​oodser:monero.social >__ my numbers are approximate, I don't know exactly what's left     

> __< midipoet >__ what's 40 xmr between friends anyways      

> __< o​frnxmr:monero.social >__ Haveno frontend ccs cant be completed unless haveno runs a network. Read the proposal.     

> __< plowsof >__ the total is derrived from the payouts here https://repo.getmonero.org/monero-project/ccs-proposals/-/blob/master/haveno-frontend.md     

> __< o​frnxmr:monero.social >__ Its 453     

> __< s​pirobel:kernal.eu >__ okay merge and move on     

> __< plowsof >__ seven five five... minus... uhm      

> __< plowsof >__ hang on     

> __< m​onerobull:matrix.org >__ Ofrn nobody cares about if it can be completed or not, just give the funds to kewbit     

> __< plowsof >__ minus 151 + 151      

> __< o​frnxmr:monero.social >__ 755/5*3     

> __< k​ewbit:matrix.org >__ If anyone is still in doubt and requires builds for each platform to test I am happy to provide these, for you to test in emulators / VirtualBox but once the decision is finalised I will release all the source code anyway.     

> __< o​frnxmr:monero.social >__ 497     

> __< s​pirobel:kernal.eu >__ great     

> __< o​frnxmr:monero.social >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/497     

> __< plowsof >__ 453 is left over geonic, i audited it      

> __< geonic >__ is woodser being funded to work on Haveno atm?     

> __< plowsof >__ that is proprietary knowledge      

> __< w​oodser:monero.social >__ no     

> __< plowsof >__ sponsors / sponsorships haveno has obtained are not public knowledge     

> __< plowsof >__ i think we can move on to cover the other proposals     

> __< k​ewbit:matrix.org >__ Woodser has equity I believe     

> __< k​ewbit:matrix.org >__ With Vik     

> __< s​pirobel:kernal.eu >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/495     

> __< plowsof >__   c. [Offline Signing Library for XmrSigner Production](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/495)         

> __< s​pirobel:kernal.eu >__ vthor is next     

> __< s​pirobel:kernal.eu >__ only thing i would change is do this in rust instead     

> __< plowsof >__ tobtoht is away this weekend so is unable to comment      

> __< plowsof >__ interested to see kayabanerve s opinion on this with a fuller understanding of whats going on     

> __< o​frnxmr:monero.social >__ Vthor's proposal had a lot of commentary from tob and kaya. I'm unsure of the conclusion     

> __< plowsof >__ still pending yes     

> __< m​onerobull:matrix.org >__ Oh oh can we please have serai support 😳👉👈     

> __< vthor >__ hey, I'm on the last sentense to respond to tobtoht's comment.     

> __< r​ucknium:monero.social >__ vthor and spirobel work together and get it done in half the time. Or in the same amount of time, but twice as good :)     

> __< vthor >__ I have a hard time to speak with more then on person at once and in a high pace, so I would appreciate if you could let comments on the proposal I will respond!     

> __< r​ucknium:monero.social >__ And the Molly dev can get in there, too     

> __< o​frnxmr:monero.social >__ Or twice as long and half as good :D /s     

> __< plowsof >__ my wife says that about her bf      

> __< vthor >__ ruckmium, yes, there are some overlaps with spirobels proposal.     

> __< o​frnxmr:monero.social >__ Hahahahaha     

> __< k​ayabanerve:matrix.org >__ vthor's proposal seems possible. tobtoht, IMO, questioned impact and noted what would increase potential impact. I'm unsure this'll be used anywhere outside of xmrsigner and would not endorse it with that expectation.     

> __< k​ayabanerve:matrix.org >__ The Molly dev was a Flutter lib. vthor is C++. I'm unsure what exactly spirobel's would be.     

> __< vthor >__ spirobal I can see to do it in rust, but not as long I have no complete understanding and overview of the source - because this would be a complete new implementaion at the moment out of scope and I need to get still up to date with C++ especially build process related stuff, and I will always need to test on both sides, what would be for me today (almost) impossible to archive and so it would be for me out of scope.     

> __< k​ayabanerve:matrix.org >__ I prefer spirobel's proposed methodology to wallet2 minification. I'm unsure the latter can have the impact necessary, see tobtoht's commentary on the protocol barrier. That doesn't change entirely new protocols aren't going to be adopted at scale and would need to be upstreamed or be limited to certain use cases.     

> __< k​ayabanerve:matrix.org >__ That isn't to say these proposals should be pitted against each other. I'm just commenting on them.     

> __< k​ayabanerve:matrix.org >__ Sorry. Spirobel did say in Rust, as vthor pointed out. I forgot they confirmed that.     

> __< plowsof >__ what if cuprate are building a better monero-wallet-rpc in rust already?     

> __< k​ayabanerve:matrix.org >__ I'd note vthor's lack of experience as its own issue with vthor's proposals. I'd personally prefer some demonstration of ability prior to a CCS, but I understand how that becomes a request for free labor.     

> __< k​ayabanerve:matrix.org >__ plowsof: Cuprate isn't AFAIK, though I wouldn't be an expert on if they've ever discussed it. boog900: would be who to ping.     

> __< plowsof >__ ah yes a daemon, they / hinto is busy with RPC json things (for monerod)     

> __< plowsof >__ thanks     

> __< k​ayabanerve:matrix.org >__ What I will note is monero-rs has existed for years and has been fine to make RPC calls, even though I believe it breaks down when you try to do more with it. They only have limited wallet functionality however.     

> __< plowsof >__ ok so pending some more back and forth between vthor kayabanerve and tobtoht. kayabas preference is spirobels proposal     

> __< vthor >__ k​ayabanerve: will defenitly not do free labour, can ot even afort it . Wallet-prc on a small hardware device is BS.     

> __< plowsof >__ vthor apears to be making this, speciically for monero signer . and will benefit other low powered hard ware devices (see the 'monero passport' )     

> __< k​ayabanerve:matrix.org >__ I did not say that and I must insist you don't misquote me.     

> __< k​ayabanerve:matrix.org >__ I understand it wasn't intentionality and intake no offense but I need to be clear.     

> __< plowsof >__ so as a laymen i see them being 2 total different projects      

> __< plowsof >__ sorry, "spirobel's proposed methodology to wallet2 minification."     

> __< s​pirobel:kernal.eu >__ also consider that the target of this library is very bespoke. I need this as a basis for the browser wallet. more on that in the ccs comments     

> __< b​oog900:monero.social >__ Yeah Cuprate is just a Rust node at the moment, not a wallet, it would be something I would like to look into in the future though     

> __< r​ucknium:monero.social >__ IMHO, it would be good to get input from some people who commented on the C ABI issues: https://github.com/seraphis-migration/strategy/issues/1 https://github.com/seraphis-migration/strategy/issues/2     

> __< vthor >__ I'm no C++ developer, nor Rust (yet) and so yes, in this to language I'm still not expirienced, to putting this == to lack of experience....well what can I say...     

> __< k​ayabanerve:matrix.org >__ vthor: I'm not asking you to do free labor. I'm noting if your competency is questioned, that's against your proposal. The CCS's escrow should resolve that without too much of a concern but I'd have higher confidence if you had already done work with C++.     

> __< k​ayabanerve:matrix.org >__ Your inability to so spend the time without financial compensation is understood and I don't blame you for that.     

> __< plowsof >__ is rottenwheel here     

> __< plowsof >__ is hardenedsteel here     

> __< plowsof >__ spirobels proposal for reference:     

> __< plowsof >__   e. [Spirobel: Robust and modular wallet-rpc library](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/501)       

> __< plowsof >__ one thing i want to ask, is are you currently obtaining funding for this project elsewhere? how many xmrs? and is the project obtaining external funding (if any) the exact same work as the proposed task in your ccs proposal?     

> __< f​reeross:monero.social >__ Hi. Can you please update me on the status of the web-ui bounty?     

> __< plowsof >__ freeross the we bounty is open, and for you, anyone to claim, but not kewbits method as its not a web wallet (as stated in the bounty)     

> __< m​onerobull:matrix.org >__ That is such a tremendous waste of resources based on a technically     

> __< plowsof >__ bounties do be like that      

> __< m​onerobull:matrix.org >__ That is such a tremendous waste of resources based on a technicality     

> __< o​frnxmr:monero.social >__ Youre the one who said we should refund donors if we change scope 🙃     

> __< k​ewbit:matrix.org >__ Would be great if the donor could have his word in     

> __< m​onerobull:matrix.org >__ I said we should if the bounty op sent in the 100 xmr     

> __< plowsof >__ no we're on the hour with some proposals not discussed      

> __< plowsof >__   d. [Revuo Monero Maintenance (2024 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/496)         

> __< k​ayabanerve:matrix.org >__ I commented on where monero-rs is in the ecosystem. monero-wallet, broken out of monero-serai (soon to be monero-oxide, I know, it's a lot to keep track of right now), implements all of the tasks in spirobel's proposal except transaction storage and any e-commerce flows (it does decouple networking and doesn't do any threading/storage itself, making it portable). It also does comp<clipped message>     

> __< k​ayabanerve:matrix.org >__ ile to no-std environments (such as wasm), but I haven't used it there and seen how nice it actually is on that level.     

> __< k​ayabanerve:matrix.org >__ A practical question is how much should this library do itself, and how much should monero-wallet be used. If monero-wallet isn't viable due to some intricacies with no-std I haven't sufficiently handled, and PRs would be non-trivial, then I'm not against yet another Rust wallet impl (though my concerns about safety and ability apply as usual). If existing work can be leveraged though, great.     

> __< k​ayabanerve:matrix.org >__ jeffro256 raised the question, spirobel notes different goals. I'm unclear exactly where the goals are different. In providing e-commerce flows, sure, yet that raises the question of if this work is most efficiently done by being built around a library like monero-wallet.     

> __< f​reeross:monero.social >__ Thanks for the clarification ...     

> __< plowsof >__ freeross, be free, ignore the haters.. claim your bounty!!!     

> __< k​ayabanerve:matrix.org >__ I think more technical discussions could be had to that end. If spirobel is firm in their belief my work isn't to their benefit however, I won't say no to their proposal just because it doesn't use my work.     

> __< r​ucknium:monero.social >__ Maybe the elephant in the room about vThor's proposal is that his previous proposal was supposed to get a production-ready xmrsigner, but this new proposal says we do not have a production-ready xmrsigner yet. I guess the required work was mis-estimated in the first proposal. That type of issue has happened in the past (see koe's Seraphis wallet proposals), but maybe it is a problem.     

> __< m​onerobull:matrix.org >__ Up vote on revuo     

> __< k​ewbit:matrix.org >__ I can confirm it will never be a web wallet at and point.     

> __< k​ayabanerve:matrix.org >__ (My not saying no isn't an endorsement, I just want to be clear I don't believe that proposal should use my work or shouldn't exist)     

> __< k​ewbit:matrix.org >__ +1 revuo     

> __< s​pirobel:kernal.eu >__ anway guys i have a fever and it is 12 oclock at night here     

> __< plowsof >__ sorry to hear that spirobel, get well soon, thank you for still attending      

> __< s​pirobel:kernal.eu >__ I just hope we can get my proposal merged soon. 👍️     

> __< plowsof >__   f. [Part-time Work on getmonero.org (2 Month) hardened steel](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/502)      

> __< plowsof >__ i presume the website meeting can discuss this^      

> __< geonic >__ yep     

> __< o​frnxmr:monero.social >__ merge     

> __< plowsof >__   g. [CCS Coordinator - plowsof](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/503)        

> __< vthor >__ rucknium, how it was exactly my proposal and I decided to take it over I made only view check, seen the libraries and testest that there is a offline wallet in monero-python - without making a transaction, and yes the time was like 5-10x, but I also didn't want to make huge changes on the proposal, because of the timefactor related to finacial issues at that time and after frustration with a bounty I made before - for nothing.     

> __< o​frnxmr:monero.social >__ "website workgroup" doesn't contribute to github     

> __< plowsof >__ lol     

> __< s​pirobel:kernal.eu >__ on a more practical / less technical note: it will also help payment gateways that currently have some friction. https://x.com/DrunkDialMe_/status/1834981243865510049 many people are faced with that     

> __< geonic >__ merge plow     

> __< k​ayabanerve:matrix.org >__ There is also the argument scanning is sufficiently trivial as a reason to not use monero-wallet in spirobel's work. Sending is the really difficult one...     

> __< plowsof >__ i have decided to give myself a raise more info here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/503#note_26231      

> __< o​frnxmr:monero.social >__ Kaya, "The next step on the road map is to add transaction building and signing functionality to the library and migrate the browser wallet to it." I dont think tx building is part of the proposal?     

> __< plowsof >__ spirobel https://libera.monerologs.net/monero-community/20240914#c429645     

> __< o​frnxmr:monero.social >__ Plowsof's raise is justified imho. He's spent many hrs helping setup (and host) docs and increased responsibilities on -site     

> __< geonic >__ next item please     

> __< plowsof >__   h. Proposal closures / Return funds to General Fund.       

> __< k​ayabanerve:matrix.org >__ The list of initial tasks by spirobel is only for scanning. That's sufficiently trivial (at least, ignoring performance but that changes in a WASM env anyways) I think monero-wallet likely still makes sense to use, but isn't months of work to not use ofrnxmr     

> __< geonic >__ what happens with the remaining 200 xmr from haveno's incomplete ccs?     

> __< plowsof >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests > theres alot of Closures of proposals with funds remaining. they currently (due to the ccs hack / return already eside in the general fund wallet)     

> __< plowsof >__ reside*     

> __< plowsof >__ the remaining 200 is benched for further haveno front end work     

> __< k​ayabanerve:matrix.org >__ Sending, and matching the wallet2 behavior, is likely using monero-wallet, forking monero-wallet, at least copying the rule set from monero-wallet, or doing months of work to do it independently though.     

> __< o​frnxmr:monero.social >__ For H, propose that we Change rule "donors: 2.the default is that the remaining XMR will be put in the Monero General Fund. There are some exceptions, but they are rare, and these decisions rest with the Core Team."     

> __< s​pirobel:kernal.eu >__ no. I tried to use kuno for this before, but it didnt really work, because of the scope of the work. Didnt get enough traction (just covered the hosting / domain costs) for monerochan.news / monerochan.cash. I recognize that the CCS is the right way to go for this project.     

> __< o​frnxmr:monero.social >__ Ccs funds should stay in ccs. Generalfund is a black hole and has 0 comnuninity control or oversight.     

> __< geonic >__ what's the current rule?     

> __< geonic >__ oh that's the current rule     

> __< o​frnxmr:monero.social >__ Current rule is to send to generalfund     

> __< geonic >__ right     

> __< plowsof >__ due to the ccs hack - they are technically returned already to the generalfund ^^     

> __< geonic >__ not a hack btw     

> __< plowsof >__ alleged hack* sorry      

> __< plowsof >__ for the record i dont believe there was a hack*     

> __< o​frnxmr:monero.social >__ my point is, those funds belong to the community     

> __< geonic >__ how about a general ccs fund where we get to vote     

> __< o​frnxmr:monero.social >__ and we should be able to redistribute them however/whenever we choose.     

> __< plowsof >__ good idea, technically, we have done similar for the repurposing of funds / closing abandonned porposals. e.g. AcceptXMR was voted/funded for in a similar way     

> __< o​frnxmr:monero.social >__ example: haveno's UI ccs is technically supposed to go to generfund. If should be kept in ccs and we can vote on how to use the funds (kewbit)     

> __< o​frnxmr:monero.social >__ Dangerousfreedom as well     

> __< plowsof >__ DF will only be gone for a year, dont worry about it :)     

> __< w​oodser:monero.social >__ repurposing the 215 to build the mobile app makes sense, but I would not support repurposing the rest of the 453, which is intended to expand the mobile app into a full desktop version, to deliver on the goals of the original CCS.     

> __< o​frnxmr:monero.social >__ youre only 1 vote, woodser     

> __< geonic >__ so funds stay in the respective ccs until we have a better idea of what to do with them? or they get moved to a "general community wallet"     

> __< o​frnxmr:monero.social >__ The goals of the ccs promised a council, engine, fees, etc     

> __< o​frnxmr:monero.social >__ geonic - a general community wallet     

> __< w​oodser:monero.social >__ so because the structure changed, the ccs is invalidated? the ui is network agnostic     

> __< o​frnxmr:monero.social >__ Yes     

> __< geonic >__ woodser: what's the timeline for delivery     

> __< o​frnxmr:monero.social >__ The ccs was merged based on many things that are undeliverable     

> __< o​frnxmr:monero.social >__ the title says "ui" but the description says "kickbacks"     

> __< geonic >__ let the man speak     

> __< plowsof >__ yes, it is up to the community to decide those funds, woodser is voting, i personally agree with woodser, its just easier to repurpose funds to another proposal that is similar enough in-scope as the original, so donors will get something that they are wanted in the end      

> __< k​ewbit:matrix.org >__ What if I agreed that was sufficient to complete the entire project, including the Figma design implementation.     

> __< o​frnxmr:monero.social >__ The entire commentary is about the kickbacks as well. Almost 0 discussion about the actual UI     

> __< w​oodser:monero.social >__ this would depend on kewbit's delivery of the mobile app. I'm told refactoring the mobile version to a full desktop version is not difficult in the dart/flutter framework     

> __< s​pirobel:kernal.eu >__ alright I will go to sleep now see you later everyone  🤧🥱     

> __< plowsof >__ get well soon!     

> __< nioCat >__ <o​frnxmr:monero.social> youre only 1 vote, woodser  <<>> votes are weighted, we don't care what me357 thinks     

> __< geonic >__ ok let's agree haveno funds stay for now. kewbit gets to work and we'll see how it goes     

> __< plowsof >__ +1 from me      

> __< geonic >__ open ideas?     

> __< o​frnxmr:monero.social >__ +1 niocat     

> __< plowsof >__ right yes     

> __< w​oodser:monero.social >__ +1 from me     

> __< nioCat >__ AIUI kewbit has done much work already     

> __< w​oodser:monero.social >__ those funds could go to good use to finish the design and implementation of a full desktop version     

> __< o​frnxmr:monero.social >__ and +1 geonic     

> __< plowsof >__ any other beesknees ?     

> __< plowsof >__ business*      

> __< geonic >__ yes. I propose that the telegram link on @monero be changed     

> __< geonic >__ in the @monero bio*     

> __< k​ewbit:matrix.org >__ I might be shooting myself in the foot a tiny bit for the future, however if it would cause too much contention, I offer this to try to make things easier to finalise. EITHER way, 215 for the currently design. Is fine, I’m not over concerned about the remaining.     

> __< geonic >__ preferably to this: https://web.libera.chat/#monero     

> __< plowsof >__ (just want to thank those for showing support for me, thank you)      

> __< o​frnxmr:monero.social >__ Twitter?     

> __< geonic >__ yes     

> __< geonic >__ the anonymous twitter admin has verified that the new link fits the character limit     

> __< vthor >__ thank tou for all your services plowsof!     

> __< plowsof >__ telegram link on @monero to be changed ? delete the telegram link?     

> __< geonic >__ yes     

> __< plowsof >__ is the telegram group a cesspool or?     

> __< geonic >__ I have no idea what it is. don't recognize any of the admins there     

> __< geonic >__ and don't think we should be endorsing Telegram anyway     

> __< k​ewbit:matrix.org >__ You’re not wrong, however I don’t believe that to be a valid reason to doubt anything.     

> __< plowsof >__ needmoney90 is an admin i recognise there     

> __< geonic >__ not around     

> __< geonic >__ anyway, shouldn't we be sending newbies here instead of some chatroom on a Russian server     

> __< plowsof >__ should we endorse another platform?      

> __< geonic >__ yes, IRC. I propose we use this link instead: https://web.libera.chat/#monero     

> __< plowsof >__ signal? ah yes, IRC, sorry      

> __< k​ewbit:matrix.org >__ Anyone against Wickr?     

> __< k​ewbit:matrix.org >__ Or Simplex     

> __< k​ewbit:matrix.org >__ (Ease of use)     

> __< o​frnxmr:monero.social >__ Theres a simplex group w over 400 ppl     

> __< geonic >__ but we're here and not on wickr or simplex...     

> __< geonic >__ why send people elsewhere?     

> __< p​lowsof:matrix.org >__ less problems for us to deal witht     

> __< o​frnxmr:monero.social >__ https://simplex.chat/contact#/?v=1-4&smp=smp%3A%2F%2FPQUV2eL0t7OStZOoAsPEV2QYWt4-xilbakvGUGOItUo%3D%40smp6.simplex.im%2Fo3W26CbJDR8abO4QG7Cvl7HM1WbKt5kO%23%2F%3Fv%3D1-2%26dh%3DMCowBQYDK2VuAyEAZLrvRhnIYDQjjyAgTnuDbZ5fhMRhA9BTBRblkqMtsQc%253D%26srv%3Dbylepyau3ty4czmn77q4fglvperknl4bi2eb2fdy2bh4jxtf32kf73yd.onion&data=%7B%22type%22%3A%22group%22%2C%22groupLinkId%22%3A%22XENmd9XeJ0rcB<clipped message>     

> __< o​frnxmr:monero.social >__ 900hulObg%3D%3D%22%7D     

> __< p​lowsof:matrix.org >__ lol but yes, we are here     

> __< o​frnxmr:monero.social >__ Yeah, matrix link works     

> __< o​frnxmr:monero.social >__ i prefer spammers come to matrix     

> __< geonic >__ what's the matrix link?     

> __< k​ewbit:matrix.org >__ I was going to use this for notifications from Haveno mobile too as an option     

> __< plowsof >__ ok just for context here, the monero twitter specifically mentions, and only mentions, the telegram link      


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2024-09-11T18:51:05+00:00
- Closed at: 2024-10-03T19:21:14+00:00
