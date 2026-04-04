---
title: 'Monero Community Workgroup Meeting: Saturday 17th December 2022 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/767
author: plowsof
assignees: []
labels: []
created_at: '2022-12-12T10:59:18+00:00'
updated_at: '2022-12-18T03:41:54+00:00'
type: issue
status: closed
closed_at: '2022-12-18T03:41:04+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/countdown/generic?iso=20221217T16&p0=1361&msg=Monero+Community+Workgroup+Meeting%3A+Saturday+17th+December+2022+%40+16%3A00&font=serif)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Metronero checkout](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/353)    
  b. [xmr-btc-swap development and improvement](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/355)    
  c. [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/357)    
  d. [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358)    
  e. [escapethe3RA Monero Observer maintenance (Winter 2022)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/363)    
  f. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/366)    
  g. [Empower Lebanon(and similar hyperinflated countries) to use Monero instead of fiat(educational and bartering platform/guerilla marketing/workshops)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/367)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration/strategy/wiki)
6. Open ideas time     
    - user selenze asks 'why do we have to register an email on monero.social / why isn't it anon'
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/759)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2022-12-18T03:41:54+00:00
Logs 
```
16:00:19 <plowsof11> meeting time https://github.com/monero-project/meta/issues/767

16:00:47 <plowsof11> 2. Greetings

16:00:48 <Siren[m]> Hi

16:00:48 <plowsof11> hii

16:01:19 <Rucknium[m]> Hi

16:01:22 <Lovera[m]> Hi!!

16:01:25 <ceetee[m]> hi

16:02:00 <plowsof11> plugging the news outlets ~ News: [Monero Observer](https://www.monero.observer/) -
[Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard)

16:02:40 <Stnby[m]> Heyyy

16:03:01 <hinto[m]> hi

16:03:10 <ofrnxmr[m]> Morning

16:03:37 <plowsof11> right lets jump in to the ccs list

16:03:38 <plowsof11>   a. [Metronero checkout](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/353)

16:03:45 <Rucknium[m]> Wait. Let me announce:

16:03:49 <plowsof11> oh

16:04:16 <Rucknium[m]> MAGIC Monero Fund is having elections. There are three seats up for election. Only two
candidates so far: https://github.com/MAGICGrants/Monero-Fund-Elections

16:04:24 <Rucknium[m]> And you can apply to be a voter

16:04:41 <Rucknium[m]> The fund has the equavalent of 50,000 USD split between USD and XMR

16:04:54 <Rucknium[m]> <done>

16:05:13 <plowsof11> 3 seats up for election? interesting. thanks for sharing

16:06:49 <plowsof11> right so this metronero proposal. its been up for 2 weeks now in its current form and
seems to be missing an extra push. so my question is for the people who like it, how to improve it? my
suggestion is to drop the sylius thing and only provide a woocommerce plugin (easier/less work_ and reduce
maintenance to just 1 month or something. thoughts?

16:07:09 <plowsof11> and my question to those that don't like the proposal - is there anything you would want
changed / included / assured?

16:08:01 <sgp[m]> Morning

16:08:40 <plowsof11> (they have other commitments in the future with monerokon etc so it is in their interests
to remain in good standing with the community for the foreseeable future)

16:08:49 <Stnby[m]> Any feedback would be appreciated

16:08:58 <selsta> I also think the current "maintenance" fee is quite high and unclear what's included.

16:09:07 <Stnby[m]> * Any feedback positive or negative would be

16:09:16 <selsta> unless I overlooked it :P

16:09:43 <hinto[m]> i prefer woocommerce > no plugin & less css work > sylius

16:10:10 <plowsof11> my suggestions would drop the amount to closer to 110~xmr i think , and we'd get a
woocommerce plugin / and the final product for a month so we can see it in action

16:10:25 <Stnby[m]> selsta: I will share it once again.

16:10:25 <Stnby[m]> Labor (12 hours a month. 12 hours * 12 months * 0.25 XMR * 2 people = 72 XMR)

16:10:25 <Stnby[m]> Hosting of custodial instance without commission fees (8 XMR)

16:10:29 <hinto[m]> ccs*

16:10:46 <plowsof11> which leaves the door open for funding the more advanced sylios thing later on

16:11:04 <plowsof11> sylius*

16:11:04 <Stnby[m]> Maintenance expecting an average of no more than 12h a month of work

16:11:56 <Stnby[m]> And 8XMR on hosting for 12 months on a not too flexible of a budget

16:12:19 <Stnby[m]> * on hosting a public instance with no dev fee for 12

16:12:26 <plowsof11> im happy with woocommerce only / 1 month hosting/maintenance to bring the asking amount
right down

16:12:58 <plowsof11> am i a madman?

16:13:12 <Siren[m]> Nope, it's doable

16:13:16 <Stnby[m]> We also think that maintenance part is unnecessary. But that was the suggestion of
previous meetings

16:13:33 <Stnby[m]> To include a maintenance milestone

16:14:25 <plowsof11> i think that would give it the extra push, i just dont know if everyone else agrees

16:14:45 <Stnby[m]> We are also fine with dropping the Syllius from CCS we can do it at our own expense

16:15:01 <Rucknium[m]> Agree that current price tag is a bit expensive. Appreciate the addition of plug-ins

16:15:10 <plowsof11> and give woocommerce asap?

16:15:48 <Stnby[m]> plowsof11: Yeah

16:16:03 <ofrnxmr[m]> The longer term hosting, I think would still be ideal @8xmr

16:17:44 <plowsof11> so mainly to reduce the workload with WCom. plugin and shorter period of maintenance or
cheaper

16:18:10 <Stnby[m]> It will be hosted as long as we can financially afford, after the period of free hosting
there will be a transaction fee on our custodial instance

16:18:34 <ofrnxmr[m]> And the fee should. Over maintenance costs?

16:18:39 <ofrnxmr[m]> Cover*

16:18:46 <Stnby[m]> Transaction fee as in covering the hosting and further maintenance costs

16:18:58 <Stnby[m]> Not for profit project

16:19:11 <ofrnxmr[m]> I like

16:19:25 <plowsof11> we can move on now/change then with this feedback i think

16:19:34 <Siren[m]> Sure

16:19:50 <plowsof11>   b. [xmr-btc-swap development and improvement](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/355)

16:20:50 <plowsof11> i dont think leito can make it here today. ive left my opinions under that proposal, and
just think commit is dead rip , we have farcaster soon

16:21:07 <Rucknium[m]> Does anyone know if BasicSwap used the COMIT protocol for their BTC<>XMR atomic swaps?

16:21:14 <plowsof11> but am waiting for leito to show where he has fixed the commit protocol already during
his volunteer work to justify the rates

16:21:55 <plowsof11> i assume so? there was also a javascript thing that used COMIT also

16:21:58 <selsta> COMIT was always a proof of concept from what I remember

16:22:17 <selsta> years later now trying to "fix" it and making it a proper API is the wrong approach in my
opinion

16:22:29 <Lovera[m]> Rucknium[m]: I think they use their own protocol valley something SecureMessaging (SMSG)
Network

16:22:43 <ofrnxmr[m]> I dont like

16:24:05 <Rucknium[m]> From casual observation, COMIT could lose user funds from the beginning. We don't know
if this will be the last fix of it.

16:24:06 <plowsof11> so ive asked him to show where he has improved the protocol so far (if we're not getting
some cryptographer/developer then why bother - as we have paid binarybaron + teammate to handle those small
tweaks UX issues)

16:24:59 <ofrnxmr[m]> Sunset it

16:25:22 <Rucknium[m]> Having some competition is a good argument, but COMIT may be out-competed by Farcaster.

16:26:20 <plowsof11> if he is a cryptographer researcher developer  then sure , he can put commit on his back
and compete with the Farcaster team

16:26:51 <Siren[m]> Farcaster looks very promising and it's also in Rust

16:27:03 <Siren[m]> Perhaps they can collab

16:27:46 <plowsof11> if leito shows clearly he is skilled, then we may need him elsewhere , im ok to wait

16:28:10 <plowsof11> we can move on if anyone has other input

16:29:06 <plowsof11>   c. [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/357)

16:29:38 <plowsof11> ive pinged NotMtth a week ago here and messaged him, dont think he's seen it but theres
been no requested updates / proof of concepts since we requested weeks ago

16:29:56 <plowsof11> im ok closing it the next meeting

16:30:45 <ofrnxmr[m]> Keep that same energy when people push back 🥲

16:30:54 <hinto[m]> agreed

16:31:37 <plowsof11>   d. [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/358)

16:31:37 <plowsof11> nothing to discuss here as we're waiting for the author still ...

16:31:48 <plowsof11> other than closing it? and re-opening it ?

16:32:29 <ofrnxmr[m]> Let it sit open imo, its a different category and needs constant follow up

16:32:30 <plowsof11> Rucknium suggested to wait around 3 months so its probably better to close it until we
have an update

16:33:11 <plowsof11> just "hide it from the ides page"

16:33:12 <plowsof11> it already has community approval.. just waiting

16:33:52 <plowsof11> moving on then

16:33:53 <plowsof11>   e. [escapethe3RA Monero Observer maintenance (Winter
2022)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/363)

16:34:08 <plowsof11> last meeting it was recently posted and not many attended, but all said merge

16:34:21 <plowsof11> if no ones voted on merge or not please do so

16:34:22 <ofrnxmr[m]> Voted to merge at last meeting, but was still young (right?)

16:34:23 <ofrnxmr[m]> Yeah

16:34:44 <Siren[m]> Merge

16:35:00 <sgp[m]> Merge

16:35:33 <plowsof11> that'll do it escapethe3ra , moving on

16:35:37 <ofrnxmr[m]> Merge

16:35:49 <plowsof11>   f. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/366)

16:37:26 <Lovera[m]> 👋🏻 I’m the autor of this proposal, any comments, suggestions are welcome

16:37:26 <ofrnxmr[m]> 1. Do you get paid from youtube 🙂

16:37:27 <plowsof11> so cakewallet is already sponsoring 5 videos a month i think, and this proposal would
increase the monero related videos on loveras main channel? along with other things (tutorials etc)

16:37:42 <plowsof11> marketing / outreach too

16:38:10 <ofrnxmr[m]> Already have 15k subs and (how many watch hours?)

16:39:00 <ofrnxmr[m]> YouTube studio > monetization

16:39:17 <Lovera[m]> ofrnxmr[m]: I have 2 YT channels, 1 Monero Only and another different topics. In the
first one I don’t get paid

16:40:10 <ofrnxmr[m]> So the answer is yes.

16:40:10 <ofrnxmr[m]> How many subs and watch hours on each channel

16:40:19 <Lovera[m]> plowsof11: Yes! All milestones is separate from cake sponsor… More videos and tutoriales

16:40:51 <plowsof11> this was only posted the other day so we've not had time to absorb whats going on here.
i've checked the channel(s) out and i just great looking content, worthy of cakewallets investment clearly

16:40:52 <ofrnxmr[m]> Yeah, good channel

16:41:17 <Siren[m]> Lovera[m]: Your main channel gets more views so I think it's preferable to post there
instead of the Monero only channel

16:41:56 <plowsof11> lovera mentioned doing video tutorials on gupax/monero-bash @hinto

16:42:14 <Lovera[m]> > <@ofrnxmr:monero.social> So the answer is yes.

16:42:14 <Lovera[m]> > How many subs and watch hours on each channel

16:42:14 <Lovera[m]> In LoveraXMR 550+ and growing fast last weeks…

16:42:37 <hinto[m]> hehe one step ahead https://github.com/hinto-janaiyo/gupax#How-To

16:42:39 <Siren[m]> The content seems great (I don't speak spanish), has a bunch of comments from people and
views higher than usual when it comes to non english monero content

16:42:46 <ofrnxmr[m]> Not something that needs fundraising imo. Your YouTube presence is profitable, paid
directly from youtube, and you have outside sponsors. We also dont fund transations @plowsof re gupax

16:42:47 <Rucknium[m]> Connect with MoneroTalk/Monerotopia since they will have their conference in Mexico
CIty next year

16:43:25 <Lovera[m]> In LoveraXMR 95 hours Las 28 days in LoveraTV ~800

16:43:38 <fr33_yourself[m]> Do you need a paypal account to get paid by YouTube?

16:44:05 <ofrnxmr[m]> All time numbers for xmr please

16:44:07 <Lovera[m]> ofrnxmr[m]: I can show you how much YouTube pay for this 🤣

16:44:34 <Siren[m]> We can still sponsor, I don't think youtube pays him more than few dollars

16:45:04 <ofrnxmr[m]> Please do

16:45:04 <Siren[m]> Lovera[m]: Sure :D

16:45:05 * Lovera[m] uploaded an image: (119KiB) <
https://libera.ems.host/_matrix/media/v3/download/matrix.org/ZWbuvElmIayLeggxmxIXSPhU/ima_20d399e.jpeg >

16:45:22 <ofrnxmr[m]> While youre offering, details on all income would be nice as well

16:46:11 <Lovera[m]> And for Monero only channel there is not incomings

16:46:49 <Lovera[m]> I think that this proposal is more than just Marketing, many people in Monero Spanish
channel ask for tutorials and guides… Injust one to push more effort to create more content

16:47:32 <plowsof11> i would see this as a re-introduction of Lovera (as his last ccs was some time ago) so we
need some time to think, but i would clearly state things in a full disclosure section (if you are happy to)
to show cake sponsor . we must remember the asking amount is just 3.5xmr / month too

16:47:33 <Siren[m]> I think it's worth paying for content on your main channel for that because there's
clearly activity there

16:48:49 <plowsof11> definitely active / large outreach

16:49:02 <ofrnxmr[m]> 15k subs

16:49:42 <plowsof11> highest viewcount on one of lovers videos?

16:49:42 <Lovera[m]> I have TikTok also where I plan to push Monero News every week

16:49:44 <plowsof11> loveras*

16:50:04 <Siren[m]> ofrnxmr[m]: Compared with other channels that speak over monero moon articles in russian,
15k is something

16:50:16 <Lovera[m]> There is 27k subs, I just want to spread more Monero over the e world

16:50:35 <ofrnxmr[m]> Monerotalk 7.6k

16:50:54 <ofrnxmr[m]> Monerotalk has 7.6k subs** for comparison

16:51:04 <plowsof11> thanks

16:51:19 <Siren[m]> Well lmao he's more popular than everyone

16:52:00 <ofrnxmr[m]> Yeah

16:52:20 <Lovera[m]> plowsof11: ✅ COMO MINAR ⛏ Monero desde Windows o Linux | Guía paso a paso

16:52:20 <Lovera[m]> https://youtu.be/EjSXyxgZjZ4

16:52:22 <Lovera[m]> About Monero this one I think

16:53:13 <ofrnxmr[m]> And this is the main channel, right

16:53:32 <plowsof11> such guides / walk throughs are really important for noobs (especially in their native
language)

16:53:41 <Lovera[m]> Yes! I one to push also Monero Only channel!

16:53:58 <ofrnxmr[m]> IMO keep it all on main channel...

16:54:09 <ofrnxmr[m]> Grow your main channel, but keep monero playlists on main channel

16:55:04 <Lovera[m]> plowsof11: This is the main reason for this proposal, take a look at Telegtam Monero
channel in Spanish, all time question, about mining, wallets, nodes

16:55:40 <plowsof11> thank you for attending lovera , we learned alot and feedback seems positive, lets wait
for more feedback over the next week or so 🚀

16:55:47 <Lovera[m]> ofrnxmr[m]: Yea, I can share content through both channels

16:55:55 <Siren[m]> He also has:

16:55:55 <Siren[m]> TikTok Channel: 20,000+ suscribers

16:55:55 <Siren[m]> Telegram Channel: 1000+ suscribers

16:56:22 <plowsof11> more than me : 0 and 0

16:56:26 <Lovera[m]> Thanks you 🙏🏻

16:57:18 <plowsof11> right, moving on lastly to LebAnons proposal

16:57:19 <plowsof11>   g. [Empower Lebanon(and similar hyperinflated countries) to use Monero instead of
fiat(educational and bartering platform/guerilla marketing/workshops)](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/367)

16:57:21 <plowsof11> there are a few comments already for lebanon to act on

16:58:27 <plowsof11> show 'proof of work' basically

16:58:35 <hinto[m]> i think showing previous work is needed here

16:58:52 <Rucknium[m]> More XMR market websites. Monero is truly the wild west. Attracts all the cowboy devs.

16:59:16 <Rucknium[m]> Please collaborate and don't re-invent the wheel.

16:59:16 <ofrnxmr[m]> 🙄 im all for Lebanon using xmr, but 5xmr for stickers ?

16:59:17 <ofrnxmr[m]> monerobull @monerobull:matrix.org:

16:59:40 <monerobull[m]1> Hmm

16:59:40 <hinto[m]> too many people talk big but never deliver

16:59:40 <Siren[m]> ofrnxmr[m]: That is a lot of money for stickers

16:59:46 <monerobull[m]1> Depends how many

16:59:51 <plowsof11> i suggest @monerobull funds a guerrilla  and sends 25 euros of xmr directly so lebanon
can print stickers himself (cheaper)

17:00:09 <ofrnxmr[m]> Monerobull is like "only if they buy them from me"

17:00:10 <monerobull[m]1> plowsof11: Guerrilla fund is empty

17:00:26 <Siren[m]> And he plans to stick them around Beirut (20 km2)

17:01:03 <Siren[m]> He doesn't need that many stickers 😅

17:01:04 <ofrnxmr[m]> Ill send a real life guerrilla to deliver the stickers foe 5xmr

17:01:17 <Siren[m]> I think they have postal services that work, it's not afghanistan after all

17:01:18 <ceetee[m]> if lebanon wants some of monerobull s stickers, I'll sponsor a pack, no problem

17:01:25 <ofrnxmr[m]> I didnt read any further into the proposal than that

17:01:47 <monerobull[m]1> ceetee[m]: I doubt packages to Lebanon arrive at first try

17:01:52 <monerobull[m]1> Israel took 3 attempts to finally get through

17:01:53 <plowsof11> binance had a crypto meetup there in july (my comment asks about this)

17:01:54 <Siren[m]> They should

17:02:01 <Siren[m]> monerobull[m]1: Oh

17:02:26 <plowsof11> i barely leave the house so if i made an ourreach proposal i couldnt prove any of this

17:02:41 <plowsof11> hopefully lebanon can

17:02:47 <Siren[m]> I think his proposal should focus on the web app he's talking about

17:03:03 <plowsof11> he wants to make bitejo.com

17:03:06 <Siren[m]> And he should elaborate more on what is that going to be exactly

17:03:22 <plowsof11> a place to barter for goods/services using xmr

17:03:50 <plowsof11> how would we verify the party was a success he plans on throwing?

17:03:52 <ofrnxmr[m]> > Safe mode by Dr.Daniel Kim which is the most recommended starter talk to get to know
how XMR is true digital cash

17:03:52 <ofrnxmr[m]> Huh

17:04:13 <ofrnxmr[m]> plowsof11: Bitejo is looking for  someont to take over, no?

17:04:13 <Siren[m]> plowsof11: I'm not sure if we should fund that

17:04:30 <Rucknium[m]> plowsof11: Lots of pictures (not good for promoting XMR)

17:04:46 <plowsof11> if he has experience of planning meetups - and its going to be a mini monerokon then sure

17:04:54 <plowsof11> otherwise, no

17:04:55 <monerobull[m]1> Siren[m]: It's ZCash level of a request

17:05:34 <plowsof11> put some stickers around beirut, use bitejo.com and watch monero means money with some
friends

17:05:36 <Siren[m]> If you end up funding that please fund our Lithuania meetups so we can get unlimited free
drinks at a bar for an hour or two 😭

17:05:49 <monerobull[m]1> plowsof11: 5000$

17:06:11 <Rucknium[m]> Yes, Zcash gets a lot of these requests to their fund. They have paused them while they
are working on the tx spam issues

17:06:33 <monerobull[m]1> Siren[m]: Also my Friday gamenights so we don't have to use debians jitsi instance
anymore

17:06:51 <plowsof11> LebAnon if you are serious about this, spirobel would like to talk to you as 'feet on the
ground' anywhere is always a good start

17:07:31 <plowsof11> so we've reached the end (other than user selenzeasking why cant they sign up for matrix
account without email because monero is anonymous!)

17:07:42 <Siren[m]> plowsof11: I mean he is right

17:07:46 <Stnby[m]> We also want to stick more Monero stickers around Lithuania

17:07:49 <Siren[m]> But we get spam

17:08:05 <Stnby[m]> Hack more kiosks to display the getmonero.org intro video as well

17:08:09 <plowsof11> yeah it was without registration, but , this is why we cant have nice things

17:08:34 <Siren[m]> A good solution would be to have a bot integration that texts you on matrix

17:08:34 <plowsof11> selenze should use ccs gitlab (as that doesnt require email verification)

17:08:35 <Rucknium[m]> Sign up with verified email or pay some XMR. That will stop the spam accounts

17:08:55 <Stnby[m]> Stnby[m]: CCS to pay the possible fine

17:08:58 <plowsof11> send 1 piconero even

17:09:05 <Siren[m]> Stnby[m]: We did that in city center and it was playing for days

17:09:48 <plowsof11> the next meeting would be 31st, so there wont be one , is anyone sad?

17:10:19 <monerobull[m]1> Ccs to take holiday from ccs Meetings

17:10:35 <Stnby[m]> We will update our CCS today, maybe someone can write some feedback before the new year ;D

17:11:02 <plowsof11> i can't claim 2 meetings / milestone , how will i cope

17:11:11 <Siren[m]> Stnby[m]: Doesn't matter, still won't get merged until next meeting

17:11:48 <plowsof11> thank you everyone for attending , lets get some coffee and get ready for the #monero-
events:monero.social meeting

17:12:11 <Stnby[m]> Siren[m]: So we can make iterations until the next one

17:13:02 <monerobull[m]1> When is monerotopia

17:13:11 <monerobull[m]1> Like the talk today

17:13:14 <plowsof11> after this change, to metronero that several agreed with here , it shuldnt need another
meeting, if they have a heart they will updoot


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2022-12-12T10:59:18+00:00
- Closed at: 2022-12-18T03:41:04+00:00
