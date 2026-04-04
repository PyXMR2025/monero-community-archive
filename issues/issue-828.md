---
title: 'Monero Community Workgroup Meeting: Saturday 29th April 2023 @ 15:00 UTC'
source_url: https://github.com/monero-project/meta/issues/828
author: plowsof
assignees: []
labels: []
created_at: '2023-04-18T02:11:43+00:00'
updated_at: '2024-04-02T17:14:51+00:00'
type: issue
status: closed
closed_at: '2023-05-13T19:13:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
15:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
    - [Moneros 9th birthday!](https://monero.observer/community-celebrate-monero-9th-birthday-monerun/) - (Note: Monero Observer has added a tarball of their source @ https://monero.observer/about/#licenses)
    - https://funding.monerujo.app ~ donate 0.01xmr to enter a MoneroKon ticket raffle! (please confirm details with them directly)
    - [Our beloved Monero, Happy birthday. All revenue from Exchanges as Donation, 2nd year](https://www.reddit.com/r/Monero/comments/12q2ocr/our_beloved_monero_happy_birthday_all_revenue/) - MajesticBank
    - [Cuprate](https://www.reddit.com/r/Monero/comments/12q2ooo/cuprate_2_months_later_and_the_quest_for/) - 2 month update
    - [monero-lws-admin](https://github.com/CryptoGrampy/monero-lws-admin) - CryptoGrampy
    - [Foundation Devices employee sets up a fork for Monero](https://www.reddit.com/r/Monero/comments/12ttiso/a_firmware_engineer_at_foundation_devices_setup_a/)
    - CakeWallet upcoming release will support restoring a wallet from QR code (scan_tx to follow later) [uri scheme](https://guides.cakewallet.com/docs/glossary/uri-scheme/) - SGP 
    - [MMgen adds offline tx signing](https://github.com/mmgen/mmgen/commit/de77f9c27d5413ec79480dedc490fbd2835ce389)  A command line multi-crypto wallet
    - Öz Fıstıkoğlu Accepts Monero - Ankara, Türkiye - shared/baklava taste audited by Siren 
    - [Overfunded list](https://github.com/plowsof/scrape_ccs_fr) / ccs wallet cache file now updated daily - plowsof
    - [MoneroTopia 2023](https://monero.observer/monerotopia-2023-conference-one-week-away/)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)
    a. [plowsof CCS Coordinator](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/385)    
7. Workgroup reports    
  a. Dev workgroup https://github.com/monero-project/monero/issues/8827#issuecomment-1518713098    
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
8. Open ideas time    
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/824)    

Meeting logs will be posted here afterwards.   

# Discussion History
## plowsof | 2023-05-01T21:58:47+00:00
Logs 
```
15:00:10 <plowsof11> Meeting time https://github.com/monero-project/meta/issues/828

15:00:26 <plowsof11> assuming that now is 15:00 UTC... hello

15:00:38 <ofrnxmr[m]> Greetings

15:01:10 <nioc> .c 11+4

15:01:33 <nioc> I am in a zoom meeting that I am trying to ignore

15:01:58 <blankpage[m]> Hi

15:02:12 <plowsof11> what has happened over the past 2 weeks, apparently Monero celebrated its 9th birthday

15:02:28 <monerobull[m]> Hello

15:04:14 <ofrnxmr[m]> Its been a long two weeks. Not much to report that isnt on agenda :)

15:04:17 <blankpage[m]> There has been some news with LWS or something

15:04:41 <ofrnxmr[m]> cryptogrampy:  admin frontend for lws

15:04:57 <blankpage[m]> Yes that

15:05:13 <plowsof11> cryptogrampys monero-lws-admin front end thingy? looks nice yeah
https://github.com/CryptoGrampy/monero-lws-admin (anyone willing to try then #monero-community-
dev:monero.social is the best place for support)

15:06:00 <plowsof11> some things not in the agenda , there is a "recurring/subscription payments thing i heard
about. but i read that the developer is using monero-wallet-cli and hasnt used the rpc wallet yet so im not so
optimistic yet

15:06:17 <ofrnxmr[m]> Still not "safe" to use mymonero "out of the box" wallets with it

15:06:19 <ofrnxmr[m]> Appears to still be risks of leaking your view keys to mymonero

15:06:37 <plowsof11> has a matrix room link for thos interested in developments there
https://matrix.to/#/#MoneroRecurringSubscriptions:matrix.org

15:06:37 <blankpage[m]> It was mentioned earlier that these community meetings clash with the regular time of
Monerotopia weekly livestream

15:07:30 <ofrnxmr[m]> Well meetings on weekdays and sundays arent ideal. Not much we can do about thr time
clash

15:07:59 <plowsof11> News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-
xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero
Moon](https://www.themoneromoon.com/)     🚀

15:08:09 <ofrnxmr[m]> We just shifted time to avoid extending into events meetings

15:09:05 <ofrnxmr[m]> Oh, an update on txextra node adoptiom

15:09:12 <plowsof11> im interested to see how this idea progresses  https://github.com/monero-
project/monero/issues/8827#issuecomment-1518713098     (will be following the MRL meetings for updates)

15:09:27 <plowsof11> there was/is a pull request already to Randomx from tevador ofrnxmr?

15:09:29 <ofrnxmr[m]> ofrnxmr[m]: At the last MRL meeting, plowsof @plowsof:matrix.org:  had noted that ~50%
of his peers had updated to the latest update

15:10:10 <prometheus1> Hi, is here where there will be a meeting?

15:10:16 <plowsof11> yes it appears to have levelled out at that (for a french / canadian node) your peer
lists may differ.

15:10:24 <plowsof11> monero.fail has added i2p support also. lza_menace nice work

15:10:32 <ofrnxmr[m]> prometheus1: Right nkw

15:11:07 <blankpage[m]> Incidentally Monerotopia live stream is live right now at
https://www.youtube.com/watch?v=Sf8X17HF27E

15:11:15 <plowsof11> [MoneroTopia 2023](https://monero.observer/monerotopia-2023-conference-one-week-away/)
May 5th - 7th, 2023 Colonia Roma,Mexico City  - monerotopia.com for tickets/more info

15:11:22 <plowsof11> they have a 3 hour price talk

15:11:29 <plowsof11> so we're fine to continue

15:12:05 <prometheus1> https://github.com/monero-project/meta/issues/828

15:12:11 <ofrnxmr[m]> Monerotopia has livestreams every saturday at 1500UTC! Let people know :)

15:12:31 <plowsof11> monerobull , has anything of note been happening in the basicdex atomic swap world?

15:12:32 <plowsof11> if you happen to know by any chance

15:12:43 <plowsof11> they are attending monerokon?

15:12:46 <monerobull[m]> They updated their UI

15:12:54 <monerobull[m]> And will be at monerotopia + monerokon

15:13:26 <plowsof11> https://basicswapdex.com/

15:14:19 <ofrnxmr[m]> context: Basicswapdex is an atomic swap service. I have not used myself but seems to be
well done

15:15:45 <plowsof11> all 4 proposals that went to funding last meeting have been funded 🫡 on Moneros birthday,
hundreds of XMR where donated to the general fund. and as majesticbank promised , they donated 75 ish
monteros. ive got a daily updated ccs wallet on github (which keeps track of any overfunding there) - handy if
you want a ccs wallet with titles pre-added

15:16:41 <plowsof11> the ccs + ccs.keys https://github.com/plowsof/scrape_ccs_fr (should maybe add a zip or
something)

15:17:28 <chesterfield[m]> Vik added qr restore to cakewallet

15:17:28 <chesterfield[m]> That’s a big deal

15:17:40 <plowsof11> ah yes , yep

15:17:41 <ofrnxmr[m]> Yup

15:17:54 <chesterfield[m]> Also https://twitter.com/MgkMshrmBrkfst/status/1652150943683624960?s=20

15:18:00 <monerobull[m]> Yeah he scammed me

15:18:00 <ofrnxmr[m]> Soon should see some services to generate "cold storage" wallets

15:18:04 <prometheus1> Cake 🎂 Cake 🎂 Cake 🎂

15:18:23 <plowsof11> after an intense battle on github - we finally got the baklava monero accepting merchant
in turkey onto https://monerica.com/

15:18:41 <ofrnxmr[m]> Nice

15:18:57 <prometheus1> Intense battle? What happened?

15:19:15 <monerobull[m]> monerobull[m]: I've spent 10 minutes refreshing his twitter and then the qr code
don't work 💢

15:19:15 <chesterfield[m]> monerobull[m]: > he’s not using iOS 🫃

15:19:16 <ofrnxmr[m]> They didnt ask me to test it :( what can i say

15:19:27 <plowsof11> how much was the giveaway monerobull :(

15:19:35 <blankpage[m]> True adoption

15:19:45 <monerobull[m]> Like 0.16 xmr

15:20:08 <chesterfield[m]> iOS chads can’t stop winning 🫃

15:20:20 <ofrnxmr[m]> Prometheus1 limbs were lost

15:20:28 <plowsof11> https://start9.com/ - seems to be 'node for noobs with preinstalled daemon' - people
often ask about ordering a 'monero node' e.g. pinodexmr , should look into that

15:21:05 <prometheus1> Anyone has a link or summary?

15:21:38 <plowsof11> at the moment the Monero support for start9 looks like you have to read a manual and
stuff / looking for testers

15:21:41 <ofrnxmr[m]> if not sent now, ping me after meeting

15:22:11 <plowsof11> cryptogrampy is always on the bleeding edge of these types of things and tested the
original / latest version for us

15:22:48 <plowsof11> prometheus https://github.com/monerica-project/monerica/issues/63#issuecomment-1523455467
xD

15:23:21 <hinto[m]> hello, forgot meeting time changed

15:23:37 <plowsof11> you are early to the 16:00 UTC meeting, i like that

15:25:12 <plowsof11> what else was there 🤔 someone reposted a 'Seth has left us' thread on reddit with some
funny comments , his company started a Monero fork [Foundation Devices employee sets up a fork for
Monero](https://www.reddit.com/r/Monero/comments/12ttiso/a_firmware_engineer_at_foundation_devices_setup_a/)

15:25:35 <plowsof11> if anyone knows what a "hoser" is please tell me

15:26:23 <ofrnxmr[m]> There are bounties available, and community members like untraceable have added to the
bounties

15:26:26 <chesterfield[m]> I think a hoser is one who helps bring high quality hardware wallets to the very
lacking Moreno hardware wallet ecosystem

15:26:26 <blankpage[m]> "Started a monero fork" is misleading

15:26:45 <plowsof11> Dan (Is not the man & Braxman Tomsparks Advocate): linked this thread earlier today
https://www.reddit.com/r/Monero/comments/131zu1e/community_member_seth_is_now_focusing_on_bitcoin/

15:26:57 <plowsof11> true started a "fork" intended to have monero support eventually ?

15:27:28 <plowsof11> definitely not forking monero 😅

15:27:54 <plowsof11> erase that from the record your honour, not trying to bring any more heat

15:28:15 <ofrnxmr[m]> S*th is forking monero?!

15:28:29 <prometheus1> Who is the honour?

15:28:36 <ofrnxmr[m]> brb. Going on a reddit rant

15:29:13 <plowsof11> https://bounties.monero.social/ going strong -> there was a delay one a recent payout for
translation work, but it has been resolved now 🙏

15:29:42 <ofrnxmr[m]> The (old)ccs translator - were they paid out?

15:29:46 <ofrnxmr[m]> German i think?

15:30:21 <plowsof11> will be paid out yes,  just confirming if  it has been

15:30:30 <ofrnxmr[m]> Ok

15:30:32 <plowsof11> remember when we decided to steal his monero if he didnt turn up in 12 months, thankfully
he showed in time

15:31:59 <plowsof11> im not seeing the webole payout as 'happened' but yeah it should (2 communiyt members
here helped alot with this) if they wish to show themselves , i can say thank you

15:33:50 <ofrnxmr[m]> agreed. Pay

15:33:52 <plowsof11> anything else? (cake will eventually add support for restoring gift wallets, ofrnxmr has
done some work on restoring from NFC cards 🫡) stackwallet.com and other wallets are available

15:34:36 <plowsof11> #monerujo:monero.social s matrix room if you're not there already

15:34:40 <prometheus1> Majestic bank the one you trust come try us

15:34:53 <ofrnxmr[m]> hhah?

15:35:03 <ofrnxmr[m]> This isnt a shilling room prometheus1:

15:35:07 <ofrnxmr[m]> Shameless plug

15:35:42 <ofrnxmr[m]> Who is "you" anyway? (the one "you" trust) lol

15:35:42 <plowsof11> trocador.app majesticbank.sc .... imcam

15:35:55 <ofrnxmr[m]> Intercambio.app i think

15:36:19 <plowsof11> ill remember it eventually

15:37:03 <ofrnxmr[m]> .. not sure though. But for a "trusted privacy service" it intercambio seems to use
cloudfkare and js (trocador.app, the service its cloned from, does not use js or cloudflare)

15:37:21 <ofrnxmr[m]> Verify, dont trust

15:38:20 <plowsof11> orangefren was accused of "being in bed" with MB but clarified on reddit that they are in
bed with everyone 😆 (orangefren has organised meetups sponsored by a few entities)

15:38:33 <ofrnxmr[m]> And i dont trust majesticbank - he lies about me and can never bring evidence to the
dicussion. Dishonesty isnt "trust"

15:38:39 <prometheus1> plowsoff11 The News from Observer Standard Moon what happened there ? Revuo

15:39:18 <plowsof11> maybe the links didnt get to irc (was just plugging those news sites)

15:39:28 <ofrnxmr[m]> They are active and putting out good news 👍

15:39:45 <ofrnxmr[m]> This is a meeting, not a "lets read the news" meetup

15:40:25 <plowsof11> shall we move on to plowsofs coordinator leach proposal

15:40:46 <ofrnxmr[m]> Is there something that isnt on the agenda that you would like to speak about today?
prometheus1:

15:40:48 <ofrnxmr[m]> Yeah, lets move on

15:41:11 <nioc> great work moving along the BP++++++ proposal plowsof11

15:41:21 <plowsof11> only idea up at the moment ( we had an animated videos idea today but too soon )

15:41:29 <ofrnxmr[m]> nioc: Seconded

15:42:06 <plowsof11> i sent, many emails, and i will continue to carry that torch with the communities support

15:42:34 <ofrnxmr[m]> plowsof @plowsof:matrix.org:  post link to next item

15:42:40 <plowsof11> thanks nioc ofrnxmr

15:43:21 <ofrnxmr[m]> drumroll

15:44:26 <plowsof11> the rates/tasks and such are the same for anyone wondering , aand the next item is

15:44:47 <moneroprophet> Mo Nero Mo Liberty

15:46:17 <ofrnxmr[m]> I cant post the link or ill crash my phone

15:46:25 <ofrnxmr[m]> Post it already 💢

15:46:29 <plowsof11> covered it all i think, molly ccs is planning on putting a monero-sdk ish proposal up for
discussion

15:46:33 <plowsof11> oh

15:46:33 <moneroprophet> What link?

15:46:40 <ofrnxmr[m]> #4

15:46:56 <plowsof11> wow, apologies https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/385

15:47:02 <ofrnxmr[m]> Ty

15:47:06 <plowsof11> plowsof CCS Coordinator

15:47:53 <ofrnxmr[m]> You have my vote 👍

15:48:16 <nioc> how many is that including socks?

15:48:36 <ofrnxmr[m]> need to ask majestic. Ive lost count

15:48:56 <plowsof11> oh, i see updoots also there, thank you all

15:49:11 <nioc> I should make an account for Cat

15:50:13 <blankpage[m]> Please add by proxy updoot

15:50:58 <hinto[m]> in the case of not many ccs's being opened, i'd like to see some work on the leftover
funds

15:51:11 <monerobull[m]> plowsof11: 👍️

15:51:38 <hinto[m]> 800+ xmr leftover from ccs just sitting around seems wasteful

15:52:06 <hinto[m]> plowsof: i'll make a proper comment on the proposal

15:52:36 <hinto[m]> more work for you :D

15:52:37 <ofrnxmr[m]> At least 200 of those are for someone who doesnt frequent these parts, but has completed
the work

15:52:42 <plowsof11> thanks hinto , i will update the work in progress issues list
https://github.com/plowsof/ccs-wip-list

15:53:23 <ofrnxmr[m]> hinto @hinto.janaiyo:matrix.org:  are you voting wait to merge? Id like to merge as
plowsof has already done more than an extra 3 months between the ccs

15:53:25 <blankpage[m]> Is 800 xmr the grand total of accidentally overfunded CCS proposals?

15:53:42 <ofrnxmr[m]> No, 242 is/was

15:53:45 <ofrnxmr[m]> 800 is unclaimed funds

15:54:05 <plowsof11> more of this type of stuff? https://github.com/plowsof/ccs-wip-list/issues

15:54:06 <blankpage[m]> Oh ok

15:54:10 <ofrnxmr[m]> unfinished ccs, or at least 1 finished and not claimed

15:54:27 <ofrnxmr[m]> And* at least

15:55:33 <ofrnxmr[m]> ofrnxmr[m]: Also took a while to fund last time

15:56:22 <blankpage[m]> Should https://ccs.getmonero.org/proposals/xmrhaelan-monero-outreach-round-3.html be
given a time limit?

15:56:31 <hinto[m]> true, the 800+ xmr work can be saved for another ccs

15:56:45 <hinto[m]> ok with merging plowsof as is

15:56:52 <blankpage[m]> This proposal is 4 years old

15:56:58 <hinto[m]> or more like, he should have been payed long ago

15:57:02 <ofrnxmr[m]> blankpage[m]: no. Imo close it

15:57:27 <ofrnxmr[m]> Its clearly abandoned. Even tk the point erc wants to delete the workgroup altogether

15:58:08 <plowsof11> the 800+ stuff is always on-going, there is only so much that can be done (seems like we
have bandwidth for 3~ items at a time), i will still focus on these things in this ccs

15:58:50 <moneroprophet> Ping geonic perhaps he can comment

15:58:54 <blankpage[m]> I agree it is fairly abandoned but what would happen to the funds?

15:59:40 <ofrnxmr[m]> On that note, i believe community has largely taken over outreach responsibilities. Im
ok with getting rid of outreach as a redundant group, and instead pointing to community for outreach.

15:59:40 <ofrnxmr[m]> not sure on that one though. But the outreach ccs? 🚮

15:59:41 <blankpage[m]> Back to general fund? Or repurposed for something else?

15:59:49 <ofrnxmr[m]> jet fund

16:00:00 <plowsof11> for me personally, the happy route was AcceptXMR https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/374 where the 'same kind of proposal' was partly funded by an
abandonned ccs

16:00:20 <plowsof11> ofc this isnt possible on all of them

16:00:24 <ofrnxmr[m]> Community* jet fund

16:01:11 <ofrnxmr[m]> im not ^

16:01:25 <ofrnxmr[m]> Those situations are very specific and need to be looked at on a case by case basis

16:01:47 <ofrnxmr[m]> Otherwise it leads to low hanging fruit for even worse grifters

16:02:01 <ofrnxmr[m]> Cant remove the barrier of "vote with wallet"

16:02:17 <ofrnxmr[m]> And just take over some other silver tongues scammers failed scam

16:02:40 <plowsof11> acceptxmr can be used as a good precedent then

16:02:52 <blankpage[m]> It is 36.68 XMR in total yes?

16:03:09 <plowsof11> yes (outreach proposal)

16:03:13 <blankpage[m]> I think acceptxmr situation was ideal but yes scams need to be avoided

16:04:06 <ofrnxmr[m]> For the funds to be available 👍

16:04:06 <ofrnxmr[m]> for the funds to be for the taking 👎

16:04:45 <blankpage[m]> The original CCS proposal milestones are not very helpful for determining what person
could class it

16:05:06 <M1234random4321[> test (it's stuck loading)

16:05:09 <blankpage[m]> "Produce a report on the economic modeling we’ve used for localization translators,
highlighting the strengths, weaknesses, and lessons learned."

16:05:27 <plowsof11> ill reach out to geonic/midipoet (last meeting we had someone who said they could contact
with people involved in that ccs too, so ill follow that up)

16:05:31 <blankpage[m]> "Create a database/directory of all Monero accepting businesses."

16:05:47 <blankpage[m]> "Improve Monero’s page on Wikipedia"

16:06:17 <plowsof11> i think someone updated the website or block explorer on wikipedia recently so it can be
paid out

16:06:39 <plowsof11> yes the milestones are vague

16:07:16 <ofrnxmr[m]> So a proposal can go to idea stage on its own. Only later should it be decided if we
fund it ourselves(rare - emergencies ot necessities), let the community fund it (ideal), or subsidizing it
when necessary (say, in the event of a good ccs without traction or simply when a better idea comes along and
we vote to use the funds directly).

16:07:16 <ofrnxmr[m]> either way, decisions on what to do with earmarked funds should only come after the
proposal is proposed without thr expectation

16:08:26 <ofrnxmr[m]> leftover food attracts rats

16:08:33 <moneroprophet> https://twitter.com/nvk/status/1649456104592617473

16:08:44 <blankpage[m]> Isn't that exactly what is being proposed in animated video stuff?

16:09:09 <ofrnxmr[m]> Prophet. Were past the hour. But still in a meeting

16:09:15 <plowsof11> selsta forgot to post a ccs idea btw, but let pretend they did

16:09:17 <ofrnxmr[m]> blankpage[m]: The post is above

16:09:30 <ofrnxmr[m]> Selsta has a new ccs coming?

16:09:34 <ofrnxmr[m]> If so > merge

16:09:36 <selsta> will post tomorrow

16:09:42 <plowsof11> renewal , +1 merge

16:10:00 <ofrnxmr[m]> good work and ty on the 18.2.2 release and more

16:11:41 <plowsof11> went over the time, sorry, to summarise : merge plowsofs proposal. and selstas (mid week
merge to funding party)


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued:
```
16:12:16 <ofrnxmr[m]> agreed
16:12:39 <ofrnxmr[m]> Comments from those reading?
16:12:50 <blankpage[m]> Sounds good
16:13:32 <nioc> +1 for selsta 
16:13:46 <tobtoht[m]> +1 selsta
16:14:27 <ofrnxmr[m]> Thanks everybody. Til next time.
16:14:27 <ofrnxmr[m]> meeting in Monero Events  in 45mins 
16:14:30 <selsta> ty
16:14:53 <plowsof11> mid week merge party luigi1111 , thanks all for attending 
```

# Action History
- Created by: plowsof | 2023-04-18T02:11:43+00:00
- Closed at: 2023-05-13T19:13:28+00:00
