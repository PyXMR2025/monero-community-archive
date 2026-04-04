---
title: 'Monero Community Workgroup Meeting: Saturday 27th April 15:00UTC'
source_url: https://github.com/monero-project/meta/issues/994
author: plowsof
assignees: []
labels: []
created_at: '2024-04-21T15:33:02+00:00'
updated_at: '2024-05-06T07:21:13+00:00'
type: issue
status: closed
closed_at: '2024-05-06T07:21:13+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
15:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

- Feedback for CoC https://github.com/monero-project/meta/pull/991

1. Introduction
2. Greetings
3. Community highlights    
    - 666.67 XMR from the General Fund donated to kayabanerves [research proposal](https://ccs.getmonero.org/proposals/fcmp++-research.html)
    - GNUteardrops fundraiser received support up to 2025! [about](https://monero.graphics/about) 
    - koe proposes an intermediate hardfork for seraphis [#monero-research-lab](https://libera.monerologs.net/monero-research-lab/20240422#c368200)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [Unnamed Monero Wallet development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/437)    Merged and funded
  b. [Seraphis General Paper Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441)    
  c. [help ofrnxmr take over the world](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/444)    
  d. [Droplet - A New Easy To Use Mobile Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/445)    
  e. [FCMP++ Development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/448)    Merged and funded
  f. [FCMP++ Research
](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449)    Merged and funding required
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    



# Discussion History
## plowsof | 2024-04-27T20:25:47+00:00
Logs 
> __< plowsof >__ Ah yes, the money printer bug (/s) :)  surely a combination of incorrect wallet restore date.. or a send to self.. local/remote node issues      

> __< plowsof >__ The telegram group i know of (english) would be https://t.me/monero no_2      

> __< 3​21bob321:monero.social >__ So whats the status of multi sig?     

> __< s​yntheticbird:monero.social >__ right now or regarding FCMP++     

> __< 3​21bob321:monero.social >__ ?     

> __< 3​21bob321:monero.social >__ It was meant to be fixed by now     

> __< 3​21bob321:monero.social >__ Wondering where its at     

> __< plowsof >__ tobtoht has shared some progress recordings of multisig wallet creation (looked smooth/fast). back to back monero-core/feather releases (and other core pull requests e.g. guix repro builds) have relaxed/extended timeframes     

> __< 3​21bob321:monero.social >__ Maybe need more devs on it to help tob     

> __< r​ottenwheel:kernal.eu >__ Congratulations to gnuteardrops for getting fully funded so fast! Long life to monero.graphics. https://monero.graphics/about#help     

> __< plowsof >__ nice! and a community meeting today     

> __< plowsof >__ in 2~ hours https://github.com/monero-project/meta/issues/994      

> __< p​lowsof:matrix.org >__ matrix dot org users please follow the meeting on monerologs.net , thank you  https://github.com/monero-project/meta/issues/994     

> __< 3​21bob321:monero.social >__ Please and thanks     

> __< k​ayabanerve:monero.social >__ plowsof: Responded to your PR comments. Let me know if there is official policy here.     

> __< plowsof >__ for the readers, its in ref to a -site blog post (to youtube, or not to youtube) https://github.com/monero-project/monero-site/pull/2289     

> __< nioCat >__ agree with kayabanerve     

> __< k​ayabanerve:monero.social >__ I'd distinctly call for getmonero.org proper to host the files, yet I don't have the care to spend the effort on that proposal.     

> __< k​ayabanerve:monero.social >__ It's not that I love Youtube, but if citing Youtube, we're citing Youtube. It's past the point of discussion IMO.     

> __< k​ayabanerve:monero.social >__ We need to remove the Youtube cite ideally. I just don't want to dig through file uploading/rights releases/embedded video players...     

> __< plowsof >__ sounds sane, originally getmonero pointed to monerooutreach (which iirc indirectly linked to youtube anyway)      

> __< s​hortwavesurfer2009:monero.social >__ If we are talking about the promotional videos, why not upload them to peer tube and use that as the embedded player?     

> __< h​orixon:monero.social >__ great idea to me     

> __< nioCat >__ spread the word far and wide  :)     

> __< s​hortwavesurfer2009:monero.social >__ Who knows, maybe while we're at it, we should host the website on IPFS and link to it with an unstoppable domains and or ENS. That way, if the getminero.org domain was ever taken away by corrupt governments, people would still have a way to access the site.     

> __< s​hortwavesurfer2009:monero.social >__ Who knows, maybe while we're at it, we should host the website on IPFS and link to it with an unstoppable domains and or ENS. That way, if the getmonero.org domain was ever taken away by corrupt governments, people would still have a way to access the site.     

> __< selsta >__ what are the privacy implications of peer tube? if it uses webtorrent it will expose your IP     

> __< s​hortwavesurfer2009:monero.social >__ I'm not totally sure that would have to be looked into a little bit more.     

> __< s​hortwavesurfer2009:monero.social >__ Does getmonero have a .onion? I checked tor times and didnt see one listed unless i missed it     

> __< selsta >__ yes     

> __< selsta >__ getmonero has an .onion mirror     

> __< selsta >__ it should get suggested automatically when opening the website in Tor browser     

> __< plowsof >__ kayabanerve in monero-site "is this final" reg the blog      

> __< dEBRUYNE >__ Perhaps title the 'Development' part should be removed from the title? Simply because the blog provides an overview     

> __< dEBRUYNE >__ Just an idea though     

> __< s​hortwavesurfer2009:monero.social >__ Nope, just tried     

> __< selsta >__ works for me     

> __< selsta >__ it says .onion available and clicking on it redirects to the .onion site     

> __< s​hortwavesurfer2009:monero.social >__ Where on the page doesn't say that? Because I don't have any kind of JavaScript or anything enabled.     

> __< selsta >__ it doesn't say it on the page itself, the tor browser suggests it     

> __< selsta >__ in the URL bar     

> __< s​hortwavesurfer2009:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/LbIQClTqNfbKpBELHPmxMjri     

> __< s​hortwavesurfer2009:monero.social >__ Nope     

> __< selsta >__ what browser is this?     

> __< s​hortwavesurfer2009:monero.social >__ Tor browser     

> __< plowsof >__ we can ping pigeons about that tor url to confirm thanks     

> __< ajs-xmr >__ Hi     

> __< plowsof >__ meeting time https://github.com/monero-project/meta/issues/994      

> __< r​ucknium:monero.social >__ shortwavesurfer2009: You have to visit the page first. It looks like you just typed it in without hitting enter     

> __< plowsof >__ greetings      

> __< c​t:xmr.mx >__ hello     

> __< selsta >__ works with the desktop browser https://usercontent.irccloud-cdn.com/file/0Hqeqf58/tor.png     

> __< mrcyjanek >__ heya     

> __< msvb-lab >__ Hello.     

> __< r​4v3r23:monero.social >__ yo     

> __< plowsof >__ has anyone read a suggested code of conduct from syntheticbird? care to share some quick thoughts?  https://github.com/monero-project/meta/pull/991     

> __< r​ucknium:monero.social >__ shortwavesurfer2009: Onion hidden service URL is http://monerotoruzizulg5ttgat2emf4d6fbmiea25detrmmy7erypseyteyd.onion     

> __< s​hortwavesurfer2009:monero.social >__ Thx     

> __< r​ucknium:monero.social >__ I don't see strong support for a CoC for Matrix/IRC channels. Probably better to give moderators power to moderate based on their judgement     

> __< plowsof >__ this has been 2 weeks of merges and successful ccs funding rouds! with  666.67 XMR from the General Fund donated to kayabanerves [research proposal](https://ccs.getmonero.org/proposals/fcmp++-research.html) ... after the several thousand of xmr in donations to celebrate moneros 10th anniversary , a transparency report was requested by dethe which     

> __< plowsof >__ binaryfate has ack'd just now https://github.com/monero-project/meta/issues/998      

> __< r​ucknium:monero.social >__ And more self governance, i.e. people who are active in channels should moderate since they know the goals of the channels, can keep them on task, etc     

> __< mrcyjanek >__ +1 rucknium, I'd like the coc to be shorter, called it rules and put in the channel's motd/pinned message     

> __< r​ucknium:monero.social >__ Logs for last -community meeting did not get posted yet BTW     

> __< c​t:xmr.mx >__ The COC is not needed, a simple "stay on toppic" should be enough     

> __< k​ayabanerve:monero.social >__ I support a CoC. I unfortunately haven't had the time yet to participate other than a few comments I shared directly with SB.     

> __< r​4v3r23:monero.social >__ +1     

> __< ajs-xmr >__ I also support a CoC     

> __< plowsof >__ yep, will get on that Rucknium,, ive been a victim of 'ill do it tomorrow '     

> __< c​t:xmr.mx >__ for example, bringing up sexuality in any form in a cryptocurrency workgroup room is offtopic     

> __< c​t:xmr.mx >__ including all related insults     

> __< k​ayabanerve:monero.social >__ My frustration is when inappropriate people are inappropriate and then never get kicked and continue being inappropriate because they weren't so inappropriate, it's universally agreed they were inappropriate.     

> __< ajs-xmr >__ Mods need to at least enforce libera chat CoC     

> __< r​ucknium:monero.social >__ Maybe mods could use the No Asshole Rule: https://en.wikipedia.org/wiki/The_No_Asshole_Rule     

> __< k​ayabanerve:monero.social >__ I'm fine with an offtopic rule, as ceetee mentions, if it's combined with an explicit strike system and we enforce upon it.     

> __< r​4v3r23:monero.social >__ no to CoC. youll just drive away more people than you already have     

> __< c​t:xmr.mx >__ I'd appreciate if we had an official "town square" room, where rules are a bit more loose, this this room can focus on things like this meeting     

> __< k​ayabanerve:monero.social >__ I'm not fine if people continue insulting various minority groups but because they solely state their 'distaste' and don't use the worst slurs, they skate by.     

> __< r​4v3r23:monero.social >__ pls, no vicitim mentality either     

> __< r​4v3r23:monero.social >__ this is the internet     

> __< r​4v3r23:monero.social >__ grow a pair or log off     

> __< c​t:xmr.mx >__ the main issue with offtopic stuff is that the real work gets derailed and focus is lost     

> __< plowsof >__ *fcmp dev logs off* lol     

> __< k​ayabanerve:monero.social >__ r4v3r23 As someone who has been harassed as a minority I'm not even, it's not a victim mentality to say we shouldn't enable that harassment.     

> __< r​4v3r23:monero.social >__ pandering to those most offended never ends well     

> __< k​ayabanerve:matrix.org >__ Saying people shouldn't be bad people, and then being told I'm the bad person for being bothered by the bad people, is the exact bs I'm talking about.     

> __< k​ayabanerve:matrix.org >__ ceetee.mx: Agreed. I've personally been exhausted by irrelevant bs.     

> __< r​4v3r23:monero.social >__ the second you go down the road of what people can and cant say its over     

> __< r​4v3r23:monero.social >__ im with rucknium, leave it to the mods     

> __< r​4v3r23:monero.social >__ an obvious troll should be banned     

> __< k​ayabanerve:matrix.org >__ If someone wants a 'free speech' chat room, they can make one. Monero needs a basic 'don't be an asshole' rule at least and to enforce it.     

> __< r​4v3r23:monero.social >__ other than that you can block/ignore     

> __< k​ayabanerve:matrix.org >__ I'll be explicit, even though I don't want to start a personal feud and this inherently will. When I complain about a real issue and get told to "grow a pair or log off",. that should be flagged, and if continually happens, the person responsible should be kicked IMO.     

> __< r​4v3r23:monero.social >__ great, so we keep changing the definition of asshole?     

> __< r​4v3r23:monero.social >__ the individual is the smallest minority. pls no identity politics     

> __< r​4v3r23:monero.social >__ a "real issue" is subjective. this is exactly what im talking about: we all have to cower to your sensitivites?     

> __< r​4v3r23:monero.social >__ a "real issue" is subjective. this is exactly what im talking about: we all have to cower to your sensitivities?     

> __< r​4v3r23:monero.social >__ this is exactly what CoCs encourage^^^     

> __< c​t:xmr.mx >__ kayaba the problem with a "free speech" room is that a lot of the drama in this room was because some people were not happy with the way community is run. It does not help posting compains in another room where those people are not present     

> __< r​4v3r23:monero.social >__ i dont want an arguement over this eithet     

> __< r​4v3r23:monero.social >__ i dont want an arguement over this either     

> __< plowsof >__ there is no freedom of speech here, and there is already a libera CoC here      

> __< k​ayabanerve:matrix.org >__ I don't believe repeated harassment of community members based on sex/gender is arguable as an issue. It's off topic and removes contributors to the project. If you don't believe it's an issue, then sure, we fundamentally disagree.     

> __< r​4v3r23:monero.social >__ ok so why over regulate     

> __< mrcyjanek >__ close the IRC/matrix channels and go back to mailing lists?     

> __< k​ayabanerve:matrix.org >__ ceetee.mx: I'm not calling for Monero to host a free spech room. I'm calling for people who can't play nice to fuck off. The definition of playing nice should be determined by the community.     

> __< r​4v3r23:monero.social >__ wen Council of Niceness     

> __< c​t:xmr.mx >__ but i am     

> __< r​4v3r23:monero.social >__ <a data-mention-type="user" href="https://matrix.to/#/@plowsof:monero.social" contenteditable="false">@plowsof</a> can i be on it     

> __< c​t:xmr.mx >__ containment room works     

> __< r​4v3r23:monero.social >__ can we move on     

> __< k​ayabanerve:matrix.org >__ I personally would like the mods to be stricter. I don't want an 'explicit strike system', but if the version with the least rules and best enforcement is 'don't be an asshole' and 'amount of times you were an asshole and warned, ban upon >3', then I'm fine with that.     

> __< k​ayabanerve:matrix.org >__ I'd actually call for a proper CoC, albeit a short one, with human warnings and with human agreement if there's multiple violations, they get kicked.     

> __< plowsof >__ thanks all for sharing opinions / view points, mod team will look over them.. for those who do want a CoC, please consider reading synthetic birds contribution, its not long, maybe suggest some edits. that is all really     

> __< k​ayabanerve:matrix.org >__ (so moderator discretion, yet with more enforcement and yes, more ground explicitly covered)     

> __< r​4v3r23:monero.social >__ we dont need it     

> __< k​ayabanerve:matrix.org >__ r4v3r23 You told me to grow a pair a few minutes ago. That hostility is part of the problem causing the CoC discussions .-.     

> __< r​4v3r23:monero.social >__ it wasnt directed at you, yet yoi choose to be offended     

> __< r​4v3r23:monero.social >__ your sensitivity is part of the problem     

> __< r​4v3r23:monero.social >__ it was a general statement     

> __< k​ayabanerve:monero.social >__ It was directed at everyone in response to my commentary.     

> __< r​4v3r23:monero.social >__ see this is what i mean..     

> __< c​t:xmr.mx >__ shall we move on plowsof? I think we're going in circles again     

> __< plowsof >__ in other news,  GNUteardrops fundraiser received support up to 2025! [about](https://monero.graphics/about)      

> __< r​4v3r23:monero.social >__ pls     

> __< plowsof >__ and ajs_ has suggested monerokon attendees set up external fundraisers where possible for travel / expenses, one example already is from anhdres      

> __< plowsof >__ we can jump into the ccs idea/merge list if no one has anything else to share      

> __< ajs-xmr >__ Yes, we didn't do a CCS and have a thin budget for MK4     

> __< r​ucknium:monero.social >__ The MAGIC Monero Fund got a proposal: https://github.com/MAGICGrants/Monero-Fund/issues/28  Please comment if you want.     

> __< plowsof >__ free open source no :(     

> __< r​ucknium:monero.social >__ And vtnerd posted an update on accomplishments about his current MAGIC proposal: https://github.com/MAGICGrants/Monero-Fund/issues/27     

> __< plowsof >__ sounds like stackoverflow      

> __< r​ucknium:monero.social >__ The MMF committee will vote on Solve4Monero on Tuesday. It probably won't be approved.     

> __< r​ucknium:monero.social >__ For example, the FAQ says "All projects should be free and open source and related to Monero or an ancillary technology (like Tor, etc.) which helps Monero use." https://monerofund.org/faq     

> __< plowsof >__ thanks for sharing Rucknium, wasn't aware of vtnerds update, thanks      

> __< plowsof >__ we can move onto the ccs merge list me thinks     

> __< c​t:xmr.mx >__ Are there any past projects from the proposer? I don't recognize the name     

> __< r​ucknium:monero.social >__ ceetee.mx: Not on Monero. I think they have worked on some BCH translation and education in Nigeria.     

> __< plowsof >__ xmruw has been moved to funding/funded, congrats mrcyjanek , we dont have to cover that in depth unless you wish to share some updates?     

> __< c​t:xmr.mx >__ ah okey. I'll read through the proposal after the meeting, but the "not open source" part doesnt look great     

> __< ajs-xmr >__ although ofrnxmr likes to view himself as a maverick true teller, he is the worst candidate to server as a community liaison     

> __< mrcyjanek >__ I'll start workin on xmruw next week plowsof     

> __< plowsof >__ thanks mrcyjanek (i know its not only xmruw, just referring to that for convenience now)      

> __< plowsof >__   b. [Seraphis General Paper Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441)    to be skipped / an MRL thing :)     

> __< mrcyjanek >__ and regarding the overfund, from the initial discussion I think that it is best to wait some time before making any decisions (to see my work first, and not tip before).     

> __< plowsof >__   c. [help ofrnxmr take over the world](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/444)         

> __< plowsof >__ highlighting the recent reply to my comment here https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/444#note_24096      

> __< plowsof >__ the proposal is as far as i can see in its final form      

> __< r​4v3r23:monero.social >__ i stand by my comment. ofrn does a lot of ccs related stuff anyway, and having recently gone thru the process myself i feel more people are needed to handle such an imporant part of the monero ecosystem     

> __< ajs-xmr >__ ofrnxmr tends to make accusatory statements without really taking the time to gather evidence and fully understand the issues he gets all worked up over     

> __< xFFFC0000 >__ + from me.      

> __< r​4v3r23:monero.social >__ especially when people try to convince the cc cooridnator against  they view as competing proposal in DMs     

> __< mrcyjanek >__ regarding ofrn I really like the idea of being addinational CCS coordinator (or "just being ofrn"), while I had positive experience with plowsof, ofrnxmr also offered me help, and I can see that he doesn't drag his personal opinions into the public commends on CCS (despite having strong ones). +1 from me.     

> __< r​4v3r23:monero.social >__ especially when people try to convince the cc cooridnator against what they view as competing proposal in DMs     

> __< xFFFC0000 >__ ofrn overall is positive force for community. Particularly newcomers.      

> __< r​4v3r23:monero.social >__ the whole system needs to be more robust and decentralized (ie, not just 1 person and luigi)     

> __< ajs-xmr >__ No, he lacks emotional intelligence, is unable or unwilling to critically evaluate complex issues in a nuanced, facts-based manner     

> __< r​4v3r23:monero.social >__ i think ofrn is suitable for the role     

> __< r​4v3r23:monero.social >__ some times you just need to get shit done, and know when to call out bs     

> __< r​4v3r23:monero.social >__ effective is better than "nice" in this case     

> __< ajs-xmr >__ the Monero community is not a monolithic, it is made up of people who have different cultural, linguistic, and political backgrounds, who might not necessarily appreciate ofrnxmr’s communication style     

> __< ajs-xmr >__ It is ni     

> __< r​4v3r23:monero.social >__ then they can speak to plowsof. thats the beauty of having a team     

> __< r​ucknium:monero.social >__ From what I have seen, ofrnxmr distorts reality to fit his opinion, especially when that opinion makes him the hero of the story.     

> __< r​ucknium:monero.social >__ Support questions and better documentation and "recipes" would be an OK role to work in.     

> __< r​4v3r23:monero.social >__ and weve had previous mods who always played victim when being called out on their overreach. we need a balance     

> __< ajs-xmr >__ It is not about being nice. It is about being objective and tactful with criticisms     

> __< r​ucknium:monero.social >__ Two wrongs don't make a right. That's really strange reasoning     

> __< c​t:xmr.mx >__ agreed, ofrn is better suited for backend then frontend     

> __< r​4v3r23:monero.social >__ apparently he needs the help and this over the top ccs is a way to get attention     

> __< c​t:xmr.mx >__ agreed     

> __< k​ayabanerve:monero.social >__ If we had an explicit CoC, that'd provide a framework for evaluating moderator actions     

> __< r​4v3r23:monero.social >__ no, my reasoning is that it has been tolerated til now (and considering the CoC chat, even more so today), so there shouldnt be a problem     

> __< r​4v3r23:monero.social >__ that shouldnt detract from his ability to help     

> __< r​ucknium:monero.social >__ I don't think ofrnxmr's modus operandi nor that of mods has been well tolerated.     

> __< mrcyjanek >__ +1 to r4v3r23, ofrnxmr despite having personal opinions is also objective and very helpful     

> __< ajs-xmr >__ Far from it, no -1     

> __< r​ucknium:monero.social >__ He's not objective. He has developed a narrative in which he is single-handedly responsible for pushing FCMP dev and research.     

> __< r​4v3r23:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/YeOanvwZePUlpzsejRillrPG     

> __< e​udaimon36:matrix.org >__ Isn't ofrnxmr a perfect example of someone with "different cultural, linguistic and political backgrounds?" His background is likely far different than 99% of you here.     

> __< r​4v3r23:monero.social >__ exactly. as a persecuted minority, i know what its like     

> __< mrcyjanek >__ e​udaimon36, he is, that's why we need him. And nobody is required to talk to ofrn if they don't want to     

> __< r​4v3r23:monero.social >__ or donate for that matter     

> __< e​udaimon36:matrix.org >__ I just came to say that ofrnxmr has spent more time helping me than anyone--by far. He's harsh, yes, and I appreciate that. I can handle people with different backgrounds     

> __< plowsof >__ would it help anyone if ofrn listed things where he has objectively helped the Monero project?  otherwise, the proposal is final, and votes need to be tally'd / decision made     

> __< c​t:xmr.mx >__ I have to second this     

> __< xFFFC0000 >__ eudaimon36 very good point. I agree.      

> __< c​t:xmr.mx >__ plowsof is it possible to see who voted for what?     

> __< plowsof >__ and he has not changed the proposal to be ccs coordinator / co coordinator as i see      

> __< e​udaimon36:matrix.org >__ liberals tolerate everyone but non-liberals     

> __< r​4v3r23:monero.social >__ im exactly the same way. at the end of the day results matter, and we need people who can get shit down     

> __< plowsof >__ yes the sock accounts are blocking the 'others' who have voted up/down     

> __< r​4v3r23:monero.social >__ im exactly the same way. at the end of the day results matter, and we need people who can get shit done     

> __< r​4v3r23:monero.social >__ instead of looking around for reasons to complain and blame     

> __< r​4v3r23:monero.social >__ bingo     

> __< r​4v3r23:monero.social >__ embrace the assholes     

> __< r​4v3r23:monero.social >__ you need them     

> __< e​udaimon36:matrix.org >__ ultimately, ofrnxmr cares so much it gets him worked up. But that is a healthy balance--someone really different     

> __< 0​x1zxq7896lp2zero:matrix.org >__ better to called them by their actual name leftist     

> __< plowsof >__ oh no, we're getting political      

> __< 0​x1zxq7896lp2zero:matrix.org >__ liberals are mostly extinct group or most went to libertarian ones     

> __< e​udaimon36:matrix.org >__ I have funded ofrnxmr privately as much as I can for his now years of help. But just me doesn't pay for food and a roof.     

> __< r​4v3r23:monero.social >__ unfortunately its just the truth     

> __< r​4v3r23:monero.social >__ its a typical playbook     

> __< c​t:xmr.mx >__ offtopic     

> __< xFFFC0000 >__ overall, my point is, he has done a lot to help newcomers. Much more than many people who are raising (non-)issues right now     

> __< r​4v3r23:monero.social >__ nothing poltical about calling a spade a spade     

> __< r​4v3r23:monero.social >__ agreed     

> __< 0​x1zxq7896lp2zero:matrix.org >__ and i don't even know why i m commenting on this lol     

> __< ajs-xmr >__ hero narrative is a nice story, but he has done nothing substantial to merit the ccs     

> __< r​ucknium:monero.social >__ x​FFFC0000: You talking about me? I've pushed through a lot of projects that were not my own, too.     

> __< e​udaimon36:matrix.org >__ His dedication to xmr, and more importantly, privacy, exceeds anyone I have met. And Monero should find a way to support him in his quest     

> __< r​4v3r23:monero.social >__ hes no hero. but he has and does help     

> __< c​t:xmr.mx >__ offtopic (the political part, thanks matrix delay)     

> __< 0​x1zxq7896lp2zero:matrix.org >__ seriously what was the topic lol     

> __< r​ucknium:monero.social >__ BCH<>XMR atomic swaps to mainnet, for example.     

> __< r​4v3r23:monero.social >__ ofrnxmrs ccs proposal     

> __< xFFFC0000 >__ rucknium hi ruck. not at all. It was not directed at anybody to be honest :)      

> __< c​t:xmr.mx >__ do you want a list, ajs?     

> __< r​ucknium:monero.social >__ Ok thanks.     

> __< e​udaimon36:matrix.org >__ I do not want to be offtopic, merely voice my little voice in as strong a way as possible.     

> __< 0​x1zxq7896lp2zero:matrix.org >__ oh will look at it now     

> __< 0​x1zxq7896lp2zero:matrix.org >__ thanks for heads up     

> __< r​4v3r23:monero.social >__ @plows     

> __< e​udaimon36:matrix.org >__ He will spend all his time helping people in xmr rooms.     

> __< e​udaimon36:matrix.org >__ No one can doubt that--he's shown it     

> __< c​t:xmr.mx >__ are there other topics we need to discuss today?     

> __< xFFFC0000 >__ that was my experience with ofrn too (point raised by eudaimon36)     

> __< r​4v3r23:monero.social >__ @plowsof are you even willing to work with him on a team?     

> __< ajs-xmr >__ There are a lot of people spend lots of time helping people     

> __< r​ucknium:monero.social >__ ofrnxmr being a second CCS coordinator like plowsof isn't in his proposal, so probably we can stop discussing it.     

> __< t​urtle420:mtrx.cz >__ All this drama     

> __< t​urtle420:mtrx.cz >__ Looks so interesting     

> __< xFFFC0000 >__ ajs-xmr wrong! I know there are quite a good people around, rucknium (and many othres) for example. But I have experience with a lot, who don't respond to any DM/email or anything else.     

> __< e​udaimon36:matrix.org >__ Not nearly as much as ofrnxmr--maybe Space Guide     

> __< ajs-xmr >__ At least not the loudest tumping their own horn     

> __< 0​x1zxq7896lp2zero:matrix.org >__ since samourai wallet got taken any one know here what happen to their monero atomic swap part     

> __< plowsof >__ as a ccs coordinator co coordinator? no that would not work. for other goals i have no problem working to achieve things with ofrnxmr, i have done so in the past (termux wallet + proof of concept gift wallet)     

> __< plowsof >__ termux node*      

> __< k​ayabanerve:monero.social >__ AFAIK, it used the COMIT protocol. I'd assume that was with COMIT's p2p network?     

> __< 0​x1zxq7896lp2zero:matrix.org >__ do someone have all the backup code since both github and gitlab once got taken down     

> __< 0​x1zxq7896lp2zero:matrix.org >__ or m i missing something ?     

> __< 0​x1zxq7896lp2zero:matrix.org >__ since samourai wallet got taken, any one know here what happen to their monero atomic swap part     

> __< plowsof >__ we also have dethe proposal     

> __< plowsof >__   d. [Droplet - A New Easy To Use Mobile Wallet](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/445)         

> __< r​4v3r23:monero.social >__ on hold indefinitely     

> __< j​oiboi.crypto:matrix.org >__ Listen up, regardless of personal vendettas against ofrnxmr he's the one that got me into the Monero community his work within the community can't be overlooked.     

> __< j​oiboi.crypto:matrix.org >__ #VoteOfrn     

> __< 0​x1zxq7896lp2zero:matrix.org >__ yea he cool guy (maybe)(don't know gender lol)     

> __< e​udaimon36:matrix.org >__ Yes, a guy, lol     

> __< 0​x1zxq7896lp2zero:matrix.org >__ lol     

> __< j​oiboi.crypto:matrix.org >__ @joiboi.crypto on X this isn't some spam account pushing weak narratives for votes cut the crap     

> __< 0​x1zxq7896lp2zero:matrix.org >__ 😅     

> __< p​lowsof:matrix.org >__ theres a meeting goin on in the monero social void, your comments are totally offtopic     

> __< p​lowsof:matrix.org >__ monerologs.net     

> __< 0​x1zxq7896lp2zero:matrix.org >__ yea ofc     

> __< j​oiboi.crypto:matrix.org >__ Plowsof he's a man a real man.     

> __< 0​x1zxq7896lp2zero:matrix.org >__ 🫠     

> __< 0​x1zxq7896lp2zero:matrix.org >__ i didn't say anything this time lol     

> __< plowsof >__ are we sure that droplet is to be closed?     

> __< j​oiboi.crypto:matrix.org >__ https://x.com/joiboicrypto?t=U7R4_DfCEVdbH7n-R362fg&s=09     

> __< s​yntheticbird:monero.social >__ I don't think anyone have comments to add on this proposal     

> __< r​4v3r23:monero.social >__ i agree with the consensus that the new monero lib is not only not needed, but massive amount of work. that just leave the actual wallet part     

> __< r​4v3r23:monero.social >__ he should close/modify proposal according to the feedback he got (he hasnt)     

> __< k​ayabanerve:monero.social >__ I don't believe the proposal sane while not using an existing lib.     

> __< plowsof >__ he even hints at a LWS wallet.... im certain dethe can obtain a ccs with the correct idea      

> __< plowsof >__ thanks all for the feedback so far      

> __< plowsof >__ finally, kayabanerves 2 proposals where merged and almost funded.. where are we now     

> __< r​avfx:xmr.mx >__ +1 ofrn (a little late, just woke up and read the buffer)     

> __< plowsof >__ thanks ravfx ack     

> __< plowsof >__ https://ccs.getmonero.org/proposals/fcmp++-research.html     

> __< k​ayabanerve:matrix.org >__ I've worked on the Development CCS, posting the specification for review. I hope to submit for that milestone in a week or two, the rest being considered unordered by me (and I believe with an explicit comment that they're unordered barring the specification first).     

> __< k​ayabanerve:matrix.org >__ Regarding research, once that's funded, I'll reach out to one group regarding one item almost immediately, with three sequential items bottlenecked by a dev CCS item bottlenecked by CS's CCS.     

> __< k​ayabanerve:matrix.org >__ So movement on all ends, which I can throw in dev comments on but this wouldn't be the place.     

> __< plowsof >__ thanks for sharing kayabanerve      

> __< k​ayabanerve:matrix.org >__ Of course. Please let me know if there's any specific questions now that I've raised ~2500 XMR and have to be a responsible member of the community who actually justifies my presence :P     

> __< plowsof >__ now lets squash your blog post and get it deployed sir      

> __< plowsof >__ binaryFate already ack'd / asked if it where the final form in -site      

> __< k​ayabanerve:matrix.org >__ I merged your baseurl tweak.     

> __< plowsof >__ i noticed the patch-1 branch name, please forgive me      

> __< plowsof >__ any questions for kayabanerve? or other business?     

> __< k​ayabanerve:matrix.org >__ FWIW, I didn't mean Development as in code. I meant as in progress. I can remove that from the title if you'd rather.     

> __< r​4v3r23:monero.social >__ wheres luigi     

> __< ajs-xmr >__ MoneroKon planning meeting @ 17 UTC in #monero-events     

> __< plowsof >__ anoneros initial payout is pending, luigi1111 is aware, no ETA as of yet      

> __< r​ucknium:monero.social >__ I'm researching the cost effectiveness of increasing the ring size and/or raising the transaction fee per byte for defense against black marble flooding. This analysis would help the conversation about a hard fork in the near future. Please comment if you have feedback about how cost and benefit is defined: https://github.com/monero-project/meta/issues/995#issuecomment-2077014407     

> __< plowsof >__ 10 coordinators hands clasped in prayer will not make luigis hands scan the QR codes any faster      

> __< r​4v3r23:monero.social >__ wasnt he supposed to give up custody anyway?     

> __< ajs-xmr >__ Any progress with idea of setting up a multisig for CCS wallet?     

> __< plowsof >__ timeline has been extended/relaxed. tobtoht shared progress / videos of the multisig wallet creation (looked quick/smooth) but back to back feather/monero releases + some other large PR's incl guix repro builds delayed him)     

> __< r​ucknium:monero.social >__ I wonder about multisig CCS wallet, too. AFAIK tobtoht is working on a good UI for that.     

> __< plowsof >__ luigi1111 can confirm / deny / clarify this      

> __< k​ayabanerve:monero.social >__ Something something RINO?     

> __< k​ayabanerve:monero.social >__ I don't want to endorse a web UI yet bF is part of RINO, no?     

> __< r​4v3r23:monero.social >__ link?     

> __< ajs-xmr >__ RINO still requires trust in the person first creating the wallet     

> __< plowsof >__ binaryFate can clarify RINO 'involvement' iirc he stepped down a while ago     

> __< k​ayabanerve:monero.social >__ RINO didn't do the DKG???     

> __< k​ayabanerve:monero.social >__ 0_o     

> __< r​ucknium:monero.social >__ Link to the #monero-community logs where tobtoht said this? Or the code?     

> __< plowsof >__ rino themselves concede that it is not the same as cold / offline wallets or so      

> __< plowsof >__ tobtoht shares updates (the video(s) of multisig in the feather room)     

> __< k​ayabanerve:monero.social >__ I'll stop mentioning it. I just wanted to note a core team member was involved and it's an existing solution. That should enable technical evaluation and an assumption they're not malicious.     

> __< k​ayabanerve:monero.social >__ Oh, definitely not the same as what's Feather discussing     

> __< plowsof >__ we can wait for tobtoht to arrive / respond (holiday weekend in parts of europe)     

> __< r​4v3r23:monero.social >__ sounded like there was a demo floating around     

> __< plowsof >__ i suppose we can end the meeting there, sorry for going over , thank you all for attending      


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued:
```
17:34:46 <luigi1112> hi, payouts on Monday
17:35:26 <luigi1112> (please contact me or plowsy if you are needing a payout)
17:42:21 <plowsof> r4v3r23^
17:54:43 <tobtoht_> Re: multisig. Every major component works (setup, recovery, signing, MMS, service API, service backend). What remains is handling leftover edge cases, some bugfixing, polishing and documentation.
17:54:51 <tobtoht_> I'm confident I can get a pre-release build out next week and will then begin welcoming people to join testing rounds.
```

# Action History
- Created by: plowsof | 2024-04-21T15:33:02+00:00
- Closed at: 2024-05-06T07:21:13+00:00
