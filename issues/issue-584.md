---
title: 'Community Workgroup Meeting: 10 July 2021 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/584
author: Keiji-C
assignees: []
labels: []
created_at: '2021-06-30T09:15:23+00:00'
updated_at: '2021-07-11T00:52:22+00:00'
type: issue
status: closed
closed_at: '2021-07-11T00:52:22+00:00'
---

# Original Description
**Location**

[Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

**Time**

17:00 UTC
19:00 CET
18:00 Irish Time
13:00 Eastern Time
10:00 Pacific Time
02:00 (2021/07/**11**) 日本標準時 


[Use this timezone calculator to convert UTC to your time zone](https://www.timeanddate.com/worldclock/converter.html?iso=20210710T170000&p1=1440&p2=28&p3=111&p4=tz_et&p5=49&p6=179&p7=70&p8=224&p9=48&p10=136&p11=248).

**Proposed Meeting Items**

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

- Introduction
- Greetings
- Community highlights
- CCS updates
- Workgroup report
    a. Daemon/CLI workgroup     
    b. Localization workgroup
    c. GUI workgroup 
    d. Outreach workgroup
    e. Defcon workgroup
    f. Website workgroup
    g. Policy workgroup
    h. Malware workgroup
- Open ideas time
- Confirm next meeting date/time


# Discussion History
## benevanoff | 2021-07-10T18:15:54+00:00
Logs:
```
bevanoff
Y’all ready for a community meeting?
sgp_@sgp_:monero.social
hello
bevanoff
Soooo when the meta issue was posted it had been decided that I’d be a moderator of sorts buttt the agenda is pretty loose so idek if that role is really necessary.
v1docq47
hi
carrington
I believe bevanoff volunteered?
tobtoht
hi all
bevanoff
It seems that it’s been a while since the last meeting so for items (1/2 introduction/greetings) I think it’d be cool if everybody present were to introduce themselves, maybe talking about what Monero thingies they’re working on or what experience/skills they might hope to contribute.
Does this sound okay? I can start to break the ice :)
mj-xmr
Sure!
ErCiccione
Hi
t-900-a joined the room.
bevanoff
My name’s Ben I’ve been kinda lurking around here for several months now. The monero thingy I’ve been working on is GUI multisig, it’s been a pretty slow work in progress but it’s getting there lol. I’m a student in linguistics and computer science so I’m happy to help with programming things to the best of my ability and I could perhaps at some point help w translations but the languages I know are pretty common ones.
msvb-lab
Hello.
sgp_@sgp_:monero.social
hello - your friendly Justin here
carrington
bevanoff is this multisig with CLSAG? Very cool to have that in the GUI
rottenstonks
wowza.
a linguistics boyo.
naisu.
carrington
I think there is nothing recent in particular to discuss under "community highlights"?
Unless there was something people wanted to discuss from recent news
bevanoff
im just using the wallet api provided by the reference implementation like the rest of the GUI so it should use the latest version of things that has been merged to master.
mj-xmr
I've been working for almost a year on Monero, part time with some breaks. I'm focusing on CI and generally conservation of resources, not just for a hobby, but without these efforts things simply... explode.
sgp_@sgp_:monero.social
The big push at the moment is Defcon, which has a meeting after this in Monero Events
ErCiccione
well. Haveno just found a massive bug in Bisq and comit gave another update. I think there are some highlights :P
rottenstonks
#monero-events libera side.
cryptocurrencyvillage.net
bevanoff
the second item on the agenda is CCS discussions if we've finished with greetings/intruduction
coinstudent2048 joined the room.
BusyBoredom
I'm pretty new to Monero, a friend told me about it a few years ago but I never got into it until recently. I am not a contributor, just trying to sit in on some community stuff and see how the monero project gets stuff done. 
carrington
The oldest CCS to discuss is this 

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/237

bevanoff
my bad ccs is after news see im a bad host lol
rottenstonks
hardfork!
bevanoff
would anybody here like to report on a CCS in progress or hype up a CCS in the ideas/funding required stage?
carrington
I suppose ErCiccione could be a good judge of if the translation related proposals are acceptable/good value?
ErCiccione
i can give my opinion, sure
zkao
hello, farcaster workgroup for atomic swaps here, catching up
bevanoff
good to see you here zkao :)
rottenstonks
hi zkao. almost there with specific workgroup updates. thanks for dropping by.
tobtoht
Short update from me on Feather Wallet:
Beta-8 will be out later today or tomorrow. 
Adds Trezor support, webcam Qr scanner, multi-output sweeps, coin labeling, better tx rebroadcasting, build reproducibility improvements and more.
rottenstonks
o/
carrington
We are discussing CCS proposal ideas found here:

https://ccs.getmonero.org/ideas/

CCS - Ideas
Ideas Funding Required Work in Progress Completed Tasks Donate Back to Getmonero.org Community Crowdfunding System
rottenstonks
tobtoht: also reducing appimage total size, right?
tobtoht
yeap
rottenstonks
based.
any thoughts on atomic swaps ever hitting feather or nay?
tobtoht
Will happen, no ETA.
rottenstonks
giga based. thx bby.
carrington
I need to dip my feet into Feather wallet, looks interesting
rottenstonks
best gui wallet in town.
mj-xmr
rottenstonks> tobtoht: also reducing appimage total size, right? <-- strip symbols?
bevanoff
tobtoht is there anything you could use help with that you might want to see if anybody here can help with?
rottenstonks
mj-xmr: wut.
bevanoff
or maybe i could help with, i remeber messaging you on reddit one time but not following up bc i started with the regular gui instead
mj-xmr
https://github.com/monero-project/monero/pull/7704
Here you can see how a simple operation can reduce the Windows binary's size by a half.
tobtoht
mj-xmr: Already stripped symbols. Just general build optimizations in Qt / Feather itself.
mj-xmr
Have you also stripped the Core's symbols or just the QTs?
Dumb question maybe.
tobtoht
I believe I also strip Core's. I would have to check.
carrington
If no one has strong opinions on the two translation CCS proposals I suppose we should move on to this proposal to buy some profit switching mining pool source code:

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/239

Open-sourcing MoneroOcean Server-Side Algorithm/Profit Switcher (!239) · Merge requests · monero-project / CCS Proposals - GitLab
What The MoneroOcean mining pool is most commonly known as a Monero mining pool with an algorithm/profit switcher. The problem that...
bevanoff
is the russian translation guy here? i thought he introduced himself
ping v1docq47
v1docq47
yup, im here
carrington
I have seen other's comment that profits switching is 

1) bad for Monero

2) not really functional at the moment as Wownero went anti-pool, other coins heading PoS
sgp_@sgp_:monero.social
I'm for the russian translation one
tobtoht
bevenoff[m]: "is there anything you could use help with" -> I have a 300+ item list of small todo's / ideas / tweaks / areas for research. After I get 1.0 release out next month, I'll push everything that remains to the issue tracker.
bevanoff
tobtoht: dope
mj-xmr
carrington> 1) bad for Monero <-- I agree. Pretty simple reasoning:
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/239#note_11076

Open-sourcing MoneroOcean Server-Side Algorithm/Profit Switcher (!239) · Merge requests · monero-project / CCS Proposals - GitLab
What The MoneroOcean mining pool is most commonly known as a Monero mining pool with an algorithm/profit switcher. The problem that...
carrington
The Russian proposal is quick detailed and has a clear track record, but I have no concept of whether it is a fair price compared to other translation proposals
mj-xmr
"Profit switching does not benefit monero, if anything it results in a lower monero hashrate which also means a lower overall network security."
carrington
Can Adorable Tanuki comment?
v1docq47
well, I am not only engaged in translation, we make various content for our youtube channel
sgp_@sgp_:monero.social
I'm not super for the Monero Ocean back-end thing. It would be cool if the code could be reused elsewhere but I don't see an obvious application
would maybe make sense if MO was a large pool but it's not
carrington
Merge mining > profit switching
bevanoff
re russian: seems fair to me
carrington
Is there some review process for translations?
bevanoff
as for the algo switching thing if people really want that they are free to fund it i guess but i dont see how it really helps monero that much
ErCiccione
carrington: yes, but ccs proposals have their own rules.
i mean translations made by ccs-funded people follow different rules
v1docq47
of course, my wife and colleagues with xmr.ru
sgp_@sgp_:monero.social
"rules" if definitely a strong word - the proposal seems in line with any "rules" but no one seems super passionate about it afaict
bevanoff
i think the russian proposal is one of the best put together from what ive seen of translation ccs proposals
carrington
It looks like ErCiccione 's proposal is up next if anyone has any comments on that
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/241

erciccione: website 3 months July-Sept (!241) · Merge requests · monero-project / CCS Proposals - GitLab
I'm proposing to continue my part time work on Getmonero.org (monero-site repository), 20 hours a week for 3 more months. What...
ErCiccione
I'm happy to answer to questions if there are any
binaryFate
IMO You're doing good work, I'm glad you made a new proposal
carrington
I am guessing "updating obsolete sections" is the biggest part of the plans?
bevanoff
mmm any research into a sexier documentation page?
ErCiccione
binaryFate: thanks :)
carrington
The website has improved a lot in recent years
ErCiccione
carrington: It's part of it, but i'm struggling to get monero devs help out for stuff like upgrading the dev docs
bevanoff: no, but i've considered migrating the docs to their own platform (like readthedocs)
sgp_@sgp_:monero.social
any updates on the press page or no? sorry I haven't had a chance to check in a while
carrington
I think torrent links for downloads would be cool, I see it is an issue on the website repo
coinstudent2048
v1docq47 You even translated some MRL logs? Good luck on your CCS! For the getmonero website, I hope I can help ☹️
ErCiccione
sgp_: i'm waiting for your images :)
crypto_grampy
ErCiccione
carrington: It's part of it, but i'm struggling to get monero devs help out for stuff like upgrading the dev docs
Not sure who is running: https://monerodocs.org/, but it's been extremely helpful with the search feature
sgp_@sgp_:monero.social
okay let me do that right now then sorry
figured it was on me
ErCiccione
crypto_grampy: yeah that's why i added it to getmonero. I would love to give it much more prominence, but that requires collaboration between many different entities
v1docq47
coinstudent2048: All translations of the MRL meeting log are available in my github repository (https://github.com/v1docq47/monero-research-lab-translations)

v1docq47/monero-research-lab-translations - GitHub
Contribute to v1docq47/monero-research-lab-translations development by creating an account on GitHub.
ErCiccione
The website has improved a lot in recent years <- it did. A lot of performance improvements and updates
rottenstonks
tobtoht: any chance you or other contributor may consider delivering feather as flatpak in the future?
tobtoht
Already on the list :)
rottenstonks
10-4. thx.
coinstudent2048
v1docq47: Yeah I am just surprised when I saw that in your CCS proposal. I am not Russian (but I am bilingual), but I'll say thanks for your work.
carrington
OK well everyone seems to like ErCiccione 's proposal so the final one is Selsta's dev proposal: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/242

selsta part-time monero development (3 months) (!242) · Merge requests · monero-project / CCS Proposals - GitLab
What Smaller dev work on CLI and GUI Some things I worked on last proposal
bevanoff
I dunno if selsta is here but he should 100% be funded
They’re basically the backbone of the gui work group
And coordinates releases
mj-xmr
selsta does all the reviews for my CI fixes.
carrington
Seems a clear thumbs up to me at least
tobtoht
Before I hop off: Imo both ErCiccione & selsta's proposals are obvious merges.
bevanoff
Yes and hella reviews
pinkybrain joined the room.
bevanoff
Ok I think we can move on then
binaryFate
no brainer, he's doing amazing job and he's always around to help with many things way more than the 30 advertised hours
mj-xmr
And asks uneasy questions which lead to a better documentations :)
rottenstonks
+1 based selsta.
SerHack
+100 for selsta and ErCiccione ccs. Amazing work
carrington
OK let's move on to the workgroups I suppose. The only proposal with strong rejection was the profit-switching pool one. I will add a comment to the gitlab issue to refer to this meeting
ErCiccione
thanks everybody for the support :)
selsta
ty everyone :D
bevanoff
If somebody wants to ping Luigi I think that means proposals from selsta, erciccione, and v1docq47 can all be merged then?
rottenstonks
luigi1111 luigi1111w get to work and stop kissing mario's cheek.
carrington
The list of active workgroups in the agenda might be out of date or not relevant, but we could probably just run through it and see who is around
bevanoff
+1
carrington
a. Daemon/CLI workgroup
luigi1111w
please give v1doc a couple upvotes
* rottenstonks gives 5 upvotes
bevanoff
I doubt anybody from there is here but that is fine
carrington
b. Localization workgroup
ErCiccione
selsta is here for a i guess?
selsta
yes but not sure what to write
zkao
what about we let the workgroups interested in discussing something specific to start?
bevanoff
Meh they have their whole own channel, unless there is something to ask of the wider non-programmer community I don’t think you need to write anything
+1 zkao
ErCiccione
If there are questions for the Localization workgroup and the Website workgroup, i can answer
rottenstonks
zkao: take it away. i may have one or two quick questions re farcaster. :)
sgp_@sgp_:monero.social
I'll give an update for Monero Space workgroup at the end
selsta
progress can be seen on github, don't have a "summary" prepared
bevanoff
That’d be great sgp
carrington
Assuming there are no big updates from devs or questions about website/translations, next is 

d. Outreach workgroup
bevanoff
sgp_ now has the floor
Thunderosa
Monero Outreach is working on a final report, but for the past 3-4 months we've been working on the Monero Merchant Directory portion which should be ready for initial launch shortly. To go with that, we've also been developing a program where merchants can request free POS sticker kits for their store/cash.
sgp_@sgp_:monero.social
outreach should go first
rottenstonks
nice.
crypto_grampy
Thunderosa
Monero Outreach is working on a final report, but for the past 3-4 months we've been working on the Monero Merchant Directory portion which should be ready for initial launch shortly. To go with that, we've also been developing a program where merchants can request free POS sticker kits for their store/cash.
very cool. will there be a search functionality on this?
Thunderosa
lh1008 has been working on getting organized to add Hindi as well, which is exciting.
Yes, it has search
rottenstonks
any updates on calendar?
Thunderosa
mapping/geo
no third parties
rottenstonks
there's another calendar... on google calendar... ¬¬
sgp_@sgp_:monero.social
yup the monero.space/calendar one is on google calendar but we keep it up to date
Next on the list is Defcon groups which I imagine has a lot going on right now:

e. Defcon workgroup
rottenstonks
meeting kicking off in 10 mins. over at #monero-events.
msvb-lab
We have a meeting on this in ten minutes.
sgp_@sgp_:monero.social
I suppose I can speak for the Defcon workgroup
rottenstonks
event is slotted for next month.
msvb-lab
Is there a agenda item or question about Defcon in particular?
sgp_@sgp_:monero.social
our kanban is here https://github.com/MoneroSpace/defcon-cryptocurrency-village/projects/1
carrington
I guess people can hop into that meeting in 10 mins for full details
sgp_@sgp_:monero.social
if you can help with any of those items, let us know in the meeting
also please let us know if you will be at Defcon and/or the Monero Party :)
rottenstonks
there'll be an after party on sat. :) https://twitter.com/MoneroSound/status/1413292275891802113
Save the date! #Monero After Party 🎈 🎉 in #LasVegas on Aug 7th, sponsored by @cakewallet ! Ticket sale will go live in the next few days pic.twitter.com/bcPkezWB5J — Monero Sound (@MoneroSound)
sgp_@sgp_:monero.social
end defcon update
zkao
Im interested in discussing monero research lab funding, since it looks like the current funding model is not working 
carrington
Wish I could teleport to Vegas for this. Unless there are updates from "Policy" or "Malware" workgroups then I guess we move to "open ideas"?
rottenstonks
zkao: ccs not working?
sgp_@sgp_:monero.social
policy should have an update today, I just need to fix some wording I've been meaning to do for a few days
ErCiccione
there isn't a single model as far as i know
zkao
garlicgambit started this discussion on reddit
https://www.reddit.com/r/Monero/comments/n2njsk/how_to_increase_the_number_of_cryptographers_and/h2spr7m/?context=3

r/Monero - How to increase the number of cryptographers and researchers working on Monero? - reddit
69 votes and 28 comments so far on Reddit
sgp_@sgp_:monero.social
nothing on malware (will almost never have a workgroup update there unless people want to help with that)
quickly on monero space then:
zkao
well, all we know that all the monero lab researchers are working elsewehre
carrington
There has been some discussion of ways to sustainably fund MRL work, I suggest a github issue under "meta" might be the best place to flesh out ideas
sgp_@sgp_:monero.social
last week we did an >8 hour Monero Twitter Space which attracted hundreds of attendees https://www.youtube.com/watch?v=OlhUPFlThAs
zkao: there is a truckload of drama pegged to researchers working elsewhere. i presume it is nuanced and would take a lot of time to dissect.
zkao
thank you, carrington, will do
sgp_@sgp_:monero.social
immediate plans are to work on the Discord, so if you are interested in the Discord at all, please let me know. I personally don't really want to moderate it
and revitalizing the flarum forum
end update
crypto_grampy
what is the flarum forum
rottenstonks
https://telegram.org/blog/voice-chats

Voice Chats Done Right - Telegram
Today, Telegram groups get an entire new dimension with Voice Chats – persistent conference calls that members can join and leave as they please. Our 12th update in 2020 brings them to you just in time for remote Christmas carols.
crypto_grampy: https://forum.monero.space/

Monero Space - Monero Space
Monero Space is an active, project-focused Monero workgroup that provides services to the Monero community. This forum is a place for Monero community member...
https://telegram.org/blog/voice-chats-on-steroids

https://forum.monero.space, something we made but didn't put much love into since launch. but we should since it's good to have a non-reddit forum community

Telegram voice are on the list too, I have the necessary permissions. so pick a date/time and we'll do it
carrington
There is also a forum by the "Monero punks" group. I guess they are a kind of workgroup so they should maybe be notified of these meetings 
rottenstonks
whenever. i got nothing better to do. :)
zkao
rottenstonks: I'm not in here for the drama, but it seems there are people willing to fund monero work, we just have to find a structure that our researchers are happy and stay working on the lab
rottenstonks
carrington: lza isn't here, unfortunately. 
anarkiocrypto maybe?
ErCiccione
zkao: if we find that structure not only for researchers but also for the other people currently working on Monero, that would be good :)
rottenstonks
zkao: it is nuanced. one of the main issues currently is receiving xmr instead of fiat. there was a recent thread considering giving stablecoins vs. xmr.
ErCiccione
we are not the mvps of Monero like MRL people are, but we would appreciate some stability as well :P

rottenstonks
any ccs taker is betting on xmr price going up, while receiving 'regular' salary. it carries taxes implications and financial burden on contributors.
carrington
I think for such a big issue maybe a Github issue and dedicated IRC/Matrix meeting should be arranged
rottenstonks
+
+1
zkao
that is it from me
sgp_@sgp_:monero.social
maybe we can talk about MAGIC MRL fund next meeting
bevanoff
MRL discussion was the major agenda item after ccs stuff but then it got merged into brainstorming
Bad idea I guess
carrington
We should quickly set a time/date for next meeting and agree on some structure 
rottenstonks
are carrington and bevanoff leading community meetings from here on out? if so, next should be in two weeks, following prior regular schedule of a community meeting every two weeks.

carrington
I am afraid in two weeks I will be unavailable to chair any kind of meeting that day
rottenstonks
i'll be out of town as well. :(
carrington
But I will take a look at commenting on gitlab issues and such in the meantime 
bevanoff
I’d like to see meeting members cycle through a sorta long list
*meeting leaders not members
I too have a hectic schedule, this time just happened to work out for me so I volunteered
carrington
Well anyways if it is set for same time in two weeks we can all stick to that
rottenstonks
sounds fair. hopefully there's people volunteering their time too... i'd be down, but alas, won't be around as i previously said.
thanks for doing this, btw.
carrington
It would be great if someone could post logs on the meeting issue page for this meeting
```

# Action History
- Created by: Keiji-C | 2021-06-30T09:15:23+00:00
- Closed at: 2021-07-11T00:52:22+00:00
