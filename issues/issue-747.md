---
title: 'Monero Community Workgroup Meeting: Saturday 5th November 2022'
source_url: https://github.com/monero-project/meta/issues/747
author: plowsof
assignees: []
labels: []
created_at: '2022-10-31T13:46:39+00:00'
updated_at: '2022-11-05T19:32:04+00:00'
type: issue
status: closed
closed_at: '2022-11-05T19:29:45+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/countdown/justmarried?iso=20221105T16&p0=1440&msg=Monero+Community+Workgroup+Meeting%3A+Saturday+5th+November+2022+%40+16%3A00+UTC&font=sanserif)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://www.themoneromoon.com/) - [Revuo Monero](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [[monero-bash v2.0.0]](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/333) (hidden - author asks to postpone)    
  b. [The-Monero-Moon-CCS-Proposal-August2022-John-Foss](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/336) (hidden - awaiting response from author)    
  c. [Forgotsudo monero marketplace](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/340) (awaiting re submission of Web Of Trust milestone)    
  d. [Develop selfhostable monero payment processor](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/345) (close)    
  e. [Gupax: GUI for P2Pool+XMRig](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/350) (edited after feedback - awaiting decision)    
  f. [Support for monero in rotki](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/351)  (closed)   
  g. [Monero Paper Wallets](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/352)  
  h. [Metronero Checkout](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/353)   
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon](https://github.com/MoneroKon) #749 
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup #748 
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)    
6. Open ideas time    
7. Confirm next meeting date/time    

Prev meeting logs:
#742     

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2022-11-05T19:29:44+00:00
Logs 
```
16:00:05 <plowsof> Meeting time https://github.com/monero-project/meta/issues/747

16:00:20 <plowsof> 2. Greetings

16:00:30 <plowsof> hello everyone

16:01:46 <hinto[m]> hi

16:01:48 <plowsof> while we wait for people to come in, just wanted to share that a few ccs proposals have
completed some of their milestones (namely the atomic swap gui proposal who we where asking for an update on)
https://repo.getmonero.org/monero-project/ccs-proposals/-/commits/master

16:01:49 <pwhx[m]> Hi!

16:02:05 <ofrnxmr[m]> Greetings

16:02:23 <monerobull[m]> Hello

16:02:28 <copenhagen_bram[> hola

16:02:31 <pwhx[m]> glad to be here

16:03:05 <ajs_[m]> Hi

16:03:10 <pandapaperwallet> Hi

16:04:40 <DiegoSalazar[m]> Hi

16:04:44 <pwhx[m]> Hi everyone

16:05:01 <plowsof> lets talk about the proposals we've mostly made a decision on , if anyone has any
objections

16:05:10 <plowsof> a. [[monero-bash v2.0.0]](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/333) (hidden - author asks to postpone)

16:05:24 <plowsof> 'hide' this from the ideas page yes/no

16:05:47 <plowsof> author wants that, correct hinto ?

16:06:41 <hinto[m]> yes, hidden

16:06:41 <monerobull[m]> plowsof: Yes

16:06:51 <ofrnxmr[m]> Yes

16:07:02 <plowsof> b. [The-Monero-Moon-CCS-Proposal-August2022-John-Foss](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/336) (hidden - awaiting response from author)

16:07:21 <ofrnxmr[m]> Ive said it 100x, close

16:07:26 <plowsof> i've contacted johnfoss 25th October on reddit, the last reply from him was Oct 28 where he
said he would replly on the 29th if he had time.

16:08:36 <ofrnxmr[m]> Moon should also ve removed from agenda "news" section - hasnt had a release in a long
time

16:08:39 <plowsof> does anyone want to wait for a response?

16:08:50 <Stnby[m]> plowsof: We dont like it

16:09:04 <Stnby[m]> * We dont like it with Siren

16:09:10 <plowsof> i believe localmonero have an active newsletter than can replace them

16:09:27 <monerobull[m]> Yes

16:09:40 <ofrnxmr[m]> Not me. Waited long enough. If foss doesnt went to engage now there is nothing stooping
him from opening a ccs later when he cares

16:09:42 <monerobull[m]> Monero standard is great

16:10:08 <ofrnxmr[m]> Close, please and thanks

16:10:24 <plowsof> ive pinged luigi1111 , so he should drop in soon/later

16:10:48 <plowsof> is there anyone here who wants monero moon to be funded right now?

16:11:35 <ofrnxmr[m]> No need to ask

16:11:37 <plowsof> going once.... twice.....

16:11:46 <ofrnxmr[m]> Gone

16:11:58 <ofrnxmr[m]> Next business, please

16:12:32 <plowsof> c. [Forgotsudo monero marketplace](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/340) (awaiting re submission of Web Of Trust milestone)

16:12:32 <merope> Would be nice to have at least a response from him before moving the proposal to funding

16:13:10 <plowsof> it has been a while i must say (every comment he receives a notification for)

16:13:35 <monerobull[m]> I like what onionr is doing, what's the current status on the web of trust?

16:13:48 <ofrnxmr[m]> endor00: were voting to close or wait. Do you want to see moon funded without a
response?

16:13:49 <DiegoSalazar[m]> One of the downsides of a self hosted gitlab is not logging in often to see the
notifications though.

16:13:49 <luigi1111> Driving

16:14:00 <ofrnxmr[m]> We've been waiting officially for 2 week (1week past the deadline)

16:14:08 <ofrnxmr[m]> Onionr I vote hide for now

16:14:34 <plowsof> 'forgot sudo' has support for resubmitting with just 1 milestone, they have just not
responded yet

16:14:58 <merope> ofrnxmr[m]: Oh sorry, misread. No, what I meant is that if the proposal is to move forward,
we'd need *at least* a response from him on any open questions. (Haven't followed too closely, so I'm not 100%
up to date on its status)

16:15:12 <selsta> I'd be careful with funding any kind of onion marketplaces but that's just my personal
opinion

16:15:15 <ofrnxmr[m]> Diego Salazar:  hes been pinged personally

16:15:24 <plowsof> i contacted him on the 25th and he said he would look at it 'tomorrow' on the 28th

16:15:25 <ofrnxmr[m]> Its a weekly newsletter - but its been weeks since hes checked in on his proposal and
months since releasing a newsletter. ---------- close

16:15:31 <plowsof> moon/johnfoss^

16:15:46 <ofrnxmr[m]> plowsof:  I Vote hide pending resubmission

16:16:31 <plowsof> for onionr , yes ,  the reason for resubmitting the Web of trust milestone is that it would
be useful (in isolation) for other projects (apparently)

16:16:32 <ofrnxmr[m]> C l o s e plowsof:  luigi1111:  wasting time re: moon

16:17:07 <merope> "Resubmitting" a milestone? What's that?

16:17:27 <monerobull[m]> plowsof: For example, I could put reviews for my shop on there, right?

16:18:10 <ofrnxmr[m]> They are going to edit the ccs or  resubmit a ccs for the specific milwstone (web of
trust) endor00:

16:18:48 <plowsof> i do not know exactly what this WoT provides (yet) myself

16:19:15 <merope> Oh ok, I see - so we're voting to keep the proposal hidden until they do that. I approve

16:19:29 <plowsof> resubmitting is just changing the proposal and put it up for discussion again (be it close
/ resubmit or edit)

16:19:31 <ofrnxmr[m]> So instead of funding the marketplace, it would only be for web of trust part of it,
which should - in theory - be useful to other projects

16:19:49 <selsta> ofrnxmr[m]: sounds more reasonable

16:19:57 <monerobull[m]> That's the plan

16:20:44 <merope> Yeah, not too crazy about funding the direct development of dnms myself either

16:20:45 <plowsof> i agree , that would be the plan for this one then (only with one milestone - wot)

16:20:45 <merope> One way or another, that's just asking for trouble

16:21:21 <ofrnxmr[m]> I think consensus on this one is hide and allow them to resubmit/edit and we come back
to it later

16:21:48 <plowsof> d. [Develop selfhostable monero payment processor](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/345) (close)

16:22:31 <ofrnxmr[m]> Stnby:  any comment?

16:22:57 <Stnby[m]> we tried to negotiate if he would be interested in working together with us

16:23:07 <Stnby[m]> On our project and find a common goal

16:23:16 <luigi1111> Vote to close it right now

16:23:25 <Stnby[m]> But his goals seemed a bit out of scope of ours

16:23:46 <Stnby[m]> I'd say close

16:23:46 <ofrnxmr[m]> Did you receive any info that would give us reason to merge?

16:23:52 <ofrnxmr[m]> Otherwise were at closen

16:24:33 <plowsof> i vote to close , they also want the funds upfront

16:25:10 <Siren[m]> Stnby[m]: He wants to primarily support Windows. He also wants a more monolithic solution,
download wallet-rpc etc from the website automatically or build everything into a binary (he didn't elaborate
how). Also wouldn't like to use our payment processor of choice, MoneroPay.

16:25:10 <merope> +1 close

16:25:29 <ofrnxmr[m]> Close

16:25:31 <Siren[m]> * He wants to primarily support Windows. He also wants a more monolithic solution,
download wallet-rpc etc from the website automatically or build everything into a binary (he didn't elaborate
how). Also didn't like to use our payment processor of choice, MoneroPay.

16:25:44 <plowsof> feels very 'bespoke' also

16:25:48 <monerobull[m]> Close

16:25:54 <monerobull[m]> Funds upfront are you insane

16:26:08 <ofrnxmr[m]> Ok, next

16:26:16 <plowsof> e. [Gupax: GUI for P2Pool+XMRig](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/350) (edited after feedback - awaiting decision)

16:26:55 <monerobull[m]> Tldr for changes?

16:27:07 <ofrnxmr[m]> hinto @hinto.janaiyo:matrix.org:  my only request is 75xmr for deliver of the 1.0 and 25
xmr for the 12 months of maintainence / updates (including major)

16:27:26 <plowsof> ofrnxmr has issues with "maintenance" - hinto edited in that it would be 'free as long as
he was in the community' and clarified that maintenance would only be small changes (filenames.. hashes etc)

16:28:13 <monerobull[m]> Yeah idk sounds like the maintenance is so minimal, with a tutorial even I'd be able
to keep it running

16:28:39 <hinto[m]> maintenance really wouldn't be too much, so i don't think it's necessary to make a big
deal out of it

16:28:53 <ofrnxmr[m]> I do

16:28:55 <plowsof> since the last meeting, hinto has released a version of his proof of concept for
windows/mac/linux

16:28:58 <ofrnxmr[m]> Because you dont.

16:29:16 <ofrnxmr[m]> If you thought it was np, why not accept.

16:29:37 <merope> I mean, unless p2pool's interface/behaviour changes dramatically, I wouldn't expect any
significant changes in the underlying code

16:29:37 <ofrnxmr[m]> Unless you feel like you'll lose 25 xmr by not maintaining it?

16:30:26 <plowsof> hinto does not want to accept funds for maintaining it

16:30:26 <hinto[m]> because there's no point in drawing out 25 xmr over 12 months

16:30:26 <ofrnxmr[m]> I agree, but p2pool adds features and is growing / changing all the time

16:30:42 <hinto[m]> merope: this is exactly correct

16:31:20 <DiegoSalazar[m]> I mean, we can't edit the proposal for him. His proposal is 100 for the thing upon
completion.

16:31:28 <DiegoSalazar[m]> Yay or nay on terms as stated?

16:31:55 <hinto[m]> true, mostly adding new command flags, but those are easy to implement

16:31:55 <monerobull[m]> If it's so much of a problem for ofrnxmr: and so little work for hinto
@hinto.janaiyo:matrix.org:  ask for 5 xmr extra paid out after a year ..

16:31:55 <plowsof> i say yes

16:32:20 <ofrnxmr[m]> Nay on terms as stated from me. No maintenance is included

16:32:51 <merope> ofrnxmr[m]: "Maintenance after initial release should be very minimal and would of course be
free." Sounds included to me? 🤔

16:33:54 <ofrnxmr[m]> Free =/= ccs. In the comments he says "as long as hes in the community", which could be
day, weeks, years

16:34:11 <merope> I like the proposal (which is pretty much 100XMR for a finished gui, right?), +1 in favor

16:34:14 <ofrnxmr[m]> All I ask is a 12 month commitment to a 15k project

16:34:31 <plowsof> some back story here , i have passed on suggestions from us reg monero-bash to hinto -
which he added/changed to that proposal (after a long time of discussions) - and we didnt like it / its not
going to funding. will the same happen here? this is discouraging

16:35:11 <ofrnxmr[m]> I wont block it, but in 100% against merging without guaranteed maintenance

16:35:23 <plowsof> hinto is a "valuable" alias (if we are worried he will vanish) - he has 1 prev completed
ccs and merged code in monero core

16:35:45 <Siren[m]> <merope> "I mean, unless p2pool's interfac..." <- In case of dramatic changes, maybe he
can create follow-up proposals and we can fund it this way?

16:35:52 <ofrnxmr[m]> No

16:35:54 <merope> Tbh I'm not sure what work you would expect him to do in those 12 months

16:36:10 <merope> Siren[m]: That would be a no, because he explicitly mentions free follow-up maintenance

16:36:16 <monerobull[m]> Yeah software shouldn't just break within a year

16:36:18 <ofrnxmr[m]> Siren:  I dont think there should be multiple ccs for this gui in a short span ie under
12 months

16:36:20 <Siren[m]> merope: Ah, okay

16:36:40 <ofrnxmr[m]> merope: This is my problemn

16:36:55 <ofrnxmr[m]> Monerobash did tjis

16:36:55 <merope> But beside the occasional bug fixing, I would not expect any big changes in the way p2pool
gets launched

16:36:56 <ofrnxmr[m]> I dont want to see this from gupax

16:37:49 <hinto[m]> i'll explicitly say there won't be a gupax 2.0

16:37:58 <ofrnxmr[m]> Ever?

16:38:47 <hinto[m]> if p2pool/xmrig don't have any breaking changes, there won't be a need

16:38:48 <hinto[m]> any internal gupax changes would be on my own time

16:39:01 <ofrnxmr[m]> And what if you create s gupax 2.0

16:39:08 <ofrnxmr[m]> Then what? New ccs?

16:39:26 <hinto[m]> if i ran away and refused to maintain this, i don't think i would be very welcomed back

16:39:43 <ofrnxmr[m]> Making a new alias is easy. Cmon now

16:39:47 <hinto[m]> there's a implicit social contract being made here worth a lot more than 25xmr

16:40:10 <ofrnxmr[m]> 25 xmr is too much to ask? His about 80/20

16:40:14 <ofrnxmr[m]> How about

16:40:25 <Stnby[m]> ofrnxmr[m]: Gaining some trust is another thing

16:40:27 <hinto[m]> i care about p2pool use a lot, i'm making this because i want p2pool to succeed

16:40:40 <plowsof> again, hinto has 1 completed ccs and merges in monero-core

16:40:55 <ofrnxmr[m]> Completed ccs withva follow up ccs for double the initial

16:41:10 <ofrnxmr[m]> In short order

16:41:42 <plowsof> i think we can vote now?

16:41:58 <plowsof> i vote move to funding as is

16:42:03 <ofrnxmr[m]> I'm the only no vote

16:42:56 <ofrnxmr[m]> (Yes with maintenance as a portion of ccs)

16:43:24 <monerobull[m]> I'm going to say yes since this is important software and Hinto is not a total
unknown

16:43:45 <Siren[m]> I like the idea and the WIP GUI, so a yes from me too

16:43:58 <ofrnxmr[m]> 🥳

16:44:06 <Siren[m]> (if my votes count :) )

16:44:47 <ofrnxmr[m]> hinto @hinto.janaiyo:matrix.org: 😈 I tried

16:44:53 <pandapaperwallet> it is a yes from me too but I'm new here

16:45:01 <plowsof>   g. [Monero Paper Wallets](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/352)

16:45:17 <monerobull[m]> Btw can I say it's kinda cute how we make decisions on the spending of a 3 billion
dollars project with like 5 people

16:45:20 <ofrnxmr[m]> Instaclose

16:45:27 <monerobull[m]> s/dollars/dollar/

16:45:36 <plowsof> https://xmr.gift/generator/ https://xmr.gift

16:45:55 <plowsof> close

16:45:57 <monerobull[m]> I'm against the wallet designs

16:46:18 <monerobull[m]> I can make some with ai for free

16:46:20 <merope> Why close? I like it

16:46:23 <plowsof> we have them already, #xmr.gift:matrix.org and a team dedicated

16:46:30 <Siren[m]> Panda: could you provide us with one of the designs? Or some of your previous unrelated
work?

16:46:33 <merope> plowsof: These are for gift wallets. Also, they require going through apps for qr codes and
stuff

16:46:40 <monerobull[m]> merope: No previous work

16:46:43 <merope> I just want to write down my seed on a cute piece of paper

16:46:44 <Stnby[m]> I am not against paper wallets but would like to see at least 1 design to get what you
mean/ your art style

16:46:54 <ofrnxmr[m]> Panda:  this is your proposal?

16:46:55 <monerobull[m]> merope: We have that already

16:46:58 <plowsof> doesnt msvb labs have gift wallets on indistructable paper?

16:47:12 <plowsof> whats the point

16:47:15 <monerobull[m]> The toughy wally or something like that

16:47:16 <merope> monerobull[m]: I've only seen one design "in the wild"

16:47:16 <pandapaperwallet> The idea behind it is different in my opinion. I think that whether you want to
keep your wallet completely offline by keep it on a paper wallet you should be able to. I do agree on the
qrcodes utility but this means using a phone to scan it/create the qrcode and that is exactly what I wanted to
avoid.

16:47:40 <plowsof> we have them though , i don't get it

16:47:42 <Siren[m]> plowsof: The proposal is so we pay for the designs it seems

16:48:08 <Siren[m]> But what are they like? Some epic artwork? Or tux paint?

16:48:09 <plowsof> i would rather give the contract to a contirbutor who has produced designs at
#xmr.gift:matrix.org

16:48:18 <plowsof> known in the community etc

16:48:23 <pandapaperwallet> I do understand that I’m new and you don’t know me, so I propose to split my
proposal in a pre-proposal of 3 designs (both A4 and credit card dimensions) in order to show you my thoughts.
Than, if you do like my designs, I will submit another proposal for the others.

16:48:29 <monerobull[m]> merope: We can buy assets from adobe for 20$ and remake it. No point in paying some
"designer" without any designs 2 grand

16:48:43 <plowsof> although gift cards - its not a huge leap of faith for the designer to make a cold wallet
thing

16:49:02 <ofrnxmr[m]> I think you should release a free one first

16:49:11 <pandapaperwallet> I can share a mockup (ignore errors, just a wip)

16:49:25 * pandapaperwallet posted a file: (32KiB) <
https://libera.ems.host/_matrix/media/v3/download/matrix.org/PheZOJZuDTsjqEhpbPXzBHyJ/design1.pdf >

16:49:41 <monerobull[m]> :/

16:49:45 <plowsof> that would be a start , lets discuss the remaining proposal in the last 10 mins

16:49:49 <ofrnxmr[m]> I think you need a working version

16:50:01 <ofrnxmr[m]> Lets move on

16:50:07 <plowsof>   h. [Metronero Checkout](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/353)

16:50:37 <pandapaperwallet> ofrnxmr[m]: what do you mean?

16:50:38 <plowsof> metronero was only added today, so this is an introduction

16:50:39 <ofrnxmr[m]> This one is very new

16:50:44 <ofrnxmr[m]> I havent had time to read ir

16:50:54 <plowsof> just sharing it for us

16:51:10 <ofrnxmr[m]> I Vote: postpone til best meeting

16:51:11 <ofrnxmr[m]> Next*

16:51:31 <plowsof> yes, just introducing it

16:51:31 <ofrnxmr[m]> Siren, can you ELO5

16:51:31 <Stnby[m]> plowsof: We kept it a secret, except from plowsof

16:51:31 <monerobull[m]> Haven't read it either

16:51:54 <Siren[m]> What do you mean by that? :D

16:52:03 <monerobull[m]> Explain like we're five

16:52:09 <monerobull[m]> Misspelled

16:52:18 <plowsof> what is metronero and when will i need/use it

16:52:55 <plowsof> merchants who want to sell products for monero

16:53:05 <ofrnxmr[m]> This is like hotshop 2.0?

16:53:09 <Siren[m]> Have you guys seen payment gateways provided by PayPal, Revolut and basically most of the
e-banking systems? This basically what we would like to make.

16:53:21 <Stnby[m]> Basically you geberate a payment link

16:53:30 <Stnby[m]> s/geberate/generate/

16:53:47 <Siren[m]> Let's say there's a shop using one of these gateways. Upon checkout the shop redirects you
to the gateway, and upon payment handling by the gateway you bounce back to the shop.

16:54:05 <monerobull[m]> So like btcpayserver?

16:54:12 <Siren[m]> Yes, similar

16:54:16 <Stnby[m]> monerobull[m]: Exactly

16:54:19 <plowsof> yes (or like Square for fiat checkouts)

16:54:26 <Stnby[m]> We have it under why section

16:54:43 <Stnby[m]> And whats the difference between what we are making and btcpay server

16:54:57 <Siren[m]> For short we did not like how poorly btcpayserver performed without Javascript

16:55:04 <merope> Are you sure you can do it in 5+5 weeks?

16:55:15 <Stnby[m]> And had medioker monero support and also C#

16:55:19 <Siren[m]> We have it performing perfectly fine without JS

16:55:31 <Stnby[m]> merope: Yeah we have a barely working PoC already

16:55:37 <merope> Milestone 1 involves "planning the backend, api" and rewriting a whole bunch of stuff

16:55:41 <Stnby[m]> https://metronero.digilol.net

16:55:44 <monerobull[m]> Siren[m]: So it will work well on Tor browser extreme settings?

16:55:55 <Siren[m]> monerobull[m]: Yes

16:55:55 <Stnby[m]> Stagenet btw

16:55:59 <Siren[m]> Absolutely no JS

16:56:18 <monerobull[m]> That's nice

16:56:21 <Siren[m]> We use HTTP headers for refreshing by default

16:56:22 <Stnby[m]> Http can do refreshes via Refresh header or a meta tag

16:56:33 <Stnby[m]> Absolutely no need for JS

16:57:12 <hinto[m]> Siren Stnby: would a github mirror ever be considered? ironically gitlab relies on JS

16:57:19 <Siren[m]> The PoC was working last time we checked (about a month ago) but there is a problem with
our wallet rpc server on stagenet. I will spin our own stagenet node tonight.

16:58:05 <Siren[m]> hinto[m]: We will mirror the rewrite on both public gitlab and GitHub instances

16:58:08 <Stnby[m]> Github relies on Microsoft but we could mirror it to repo.getmonero.org

16:58:13 <Siren[m]> We are not too proud of the PoC

16:58:24 <Siren[m]> But it is fully open source

16:59:26 <Stnby[m]> AGPLv3 :)

16:59:38 <monerobull[m]> Will you keep it working after potential seraphis fork

17:00:01 <plowsof> i have seen an example payment request on stagenet (where you see the qr code/address to
send funds to and it refreshes to show completion of payment) it would be ideal to have this to show us again

17:00:40 <plowsof> redirects to the 'shop after payment received etc

17:00:42 <Stnby[m]> We will keep it working as we need it for ourseleves, we would even consider making this
without a proposal like moneropay.eu, but plowsof encouraged us to create one

17:01:55 <plowsof> MoneroPay team have my support, thanks

17:02:01 <Siren[m]> monerobull[m]: It uses Moneropay to do payment processing, which uses official wallet rpc
server underneath. Unless the wallet rpc server will break after the fork, everything should be still working.

17:02:42 <Stnby[m]> If it doesnt we will shout on the core untill it starts working, jk

17:03:36 <plowsof> now the hour is up, any parting words? also waiting on jberman/selsta for their ccs
renewals

17:03:52 <Siren[m]> plowsof: In the PoC UI we have a form where you can fill a form and generate this payment
page which upon cancellation or completion redirects you to the provided URLs. But ideally you can have your
backend make a post request to create these pages automatically.

17:04:32 <selsta> plowsof: will open today lol

17:04:38 <Stnby[m]> Also meteonero will keep merchant system up to date with the satus over callbacks

17:04:40 <plowsof> +1

17:04:47 <Stnby[m]> s/satus/status/

17:05:01 <Siren[m]> <merope> "Are you sure you can do it in 5+..." <- Yes, should be enough.

17:05:04 <Stnby[m]> * Also meteonero will keep merchant system up to date with the payment status over
callbacks

17:06:32 <Stnby[m]> Siren[m]: Will be enough, if we do not finish it on time its us to blame and we will work
on it until it works!

17:06:45 <Siren[m]> ^ For free

17:07:38 <Stnby[m]> Maintenance will be free as well

17:08:28 <hinto[m]> <plowsof> "now the hour is up, any parting..." <- is luigi here?

17:08:56 <hinto[m]> i'd like to get working and a confirmed merge would take a lot of worries off my mind

17:09:22 <plowsof> almost , Driving home , soon though, ill update by the end of today on whats happening

17:10:03 <plowsof> ok , seems like we've reached the end, thank you all for attending ❤️

17:10:07 <merope> btw plowsof, I noticed a bunch of spam comments in some of the proposals

17:10:16 <ofrnxmr[m]> Yeah

17:10:37 <hinto[m]> plowsof: are you luigi :D ?

17:10:37 <merope> (dunno if you have the power to clean up)

17:10:38 <ajs_[m]> i wanted to give a quick update on MoneroKon 2023

17:10:38 <plowsof> i read the email after each gets posted , i will ask for rights to delete them

17:10:40 <ofrnxmr[m]> hinto @hinto.janaiyo:matrix.org:  im luigi

17:10:54 <plowsof> ah hello ajs_

17:11:01 <Stnby[m]> Thank you as well plowsof have a safe ride don't die while texting!

17:11:07 <Siren[m]> One of the spam comments: https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/345#note_18884

17:11:37 <ajs_[m]> We have narrowed down the venue options to two locations  - Neuchâtel, Switzerland and
Prague, Czechia

17:11:49 <merope> we are all luigi

17:11:58 <ajs_[m]> https://github.com/MoneroKon/meta/issues/1

17:11:58 <merope> luigi is a hivemind

17:11:59 <ajs_[m]> We are still waiting on further details from University of Neuchâtel and we've received a
agreement from La Fabrika.

17:11:59 <pandapaperwallet> <ofrnxmr[m]> "I think you should release a..." <- Ok I will release one upfront
and we will discuss about it later. Thank you for your suggestion

17:11:59 <ajs_[m]> La Fabrika is offering 3 days + 1 day setup... 5x10m stage, 6 long tables, 12 chairs, 12
bistro tables, PA system, stage lighting, laser projector and screen (610 x 345cm) + support staff (production
manager, light board operator, sound engineer, video engineer, cloakroom attendants, fireman, cleanup crew)...
~53k EUR

17:12:00 <ajs_[m]> Personally, I am leaning towards La Fabrika since we have close contacts with Paralelni
Polis. On the other hand, Neuchâtel might be a cheaper option since the venue is at a university and the
Nym/DarkFi teams are interested in collaborating with us.

17:12:23 <ajs_[m]> We will be making a final decision on the venue in next week's MoneroKon planning meeting.

17:12:31 <ajs_[m]> https://github.com/monero-project/meta/issues/749

17:12:34 <Stnby[m]> Will there be anyone in fossdem from monero next year

17:12:42 <plowsof> Exciting, thank you for the update!

17:12:46 <ajs_[m]> I invite everyone to chime in the choices by joining the planning meeting or commenting on
the GitHub issue

17:12:57 <ajs_[m]> Once we gather additional quotes from vendors and finalise the budget, we should be
submitting a CCS proposal sometime in early December.

17:13:12 <ajs_[m]> that's it.. thanks

17:13:16 <monerobull[m]> I'll set up talk submissions once we have a venue

17:15:23 <plowsof> ok everyone thanks for attending, if the hiveminds wishes are not implemented , it is my
fault

17:15:32 <Siren[m]> Stnby[m]: Me and Stnby are going

17:16:13 <hinto[m]> i might be the only person here not in europe

17:16:16 <plowsof> https://fosdem.org/2023/

17:16:39 <hinto[m]> ty plowsof

17:16:53 <plowsof> Brussels / Belgium

17:17:18 <Stnby[m]> Who is going!!!!

17:17:39 <Stnby[m]> We have to exchange some Monero srickers

17:18:36 <monerobull[m]> plowsof: Thank you for moderating

17:18:52 <monerobull[m]> Stnby[m]: Just order them from me 😎

17:24:34 <Stnby[m]> Do you sell them?

17:25:40 <monerobull[m]> Monerosupplies.com

17:25:41 <monerobull[m]> https://monerosupplies.com/

17:26:06 <Stnby[m]> We got like 200 of these from the guy in Vilnius for free

17:26:17 <ofrnxmr[m]> <pandapaperwallet> "Ok I will release one upfront..." <- plowsof:

17:26:22 <Stnby[m]> I think he might have bought it from you

17:26:39 <Siren[m]> monerobull[m]: We have the exact same stickers. It's probably from you. Laminated paper
right?

17:27:44 <monerobull[m]> Yeah vinyl

17:27:57 <monerobull[m]> Outdoor rated

17:28:09 * Stnby[m] uploaded an image: (69KiB) < https://libera.ems.host/_matrix/media/v3/download/kernal.eu/f
HvpNBWSimBuhLGEDMQjKqEC/PXL_20221014_182345444_20221105192752.jpg >

17:28:27 <monerobull[m]> Jup that's then

17:28:32 <monerobull[m]> * Jup that's them

17:28:41 <Stnby[m]> We already used them all

17:28:49 <plowsof> if we like the idea of monero paper wallets , then we should sponsor the gift-wallet team
(more info in my comment on the ccs idea - as 'gift wallet' is also == restoring a wallet from seed - side
stepping all of their effort / research and dev. and asking for funding when you dont have a simple PoC design
yourself feels insulting )

17:28:53 <monerobull[m]> Nice

17:29:15 <Stnby[m]> If you ever go to Vilnius you will see them absolutely everywhere

17:29:43 <Siren[m]> We have wars with nft people

17:29:51 * Siren[m] uploaded an image: (98KiB) <
https://libera.ems.host/_matrix/media/v3/download/kernal.eu/XTwZqjRyYLIAShXisMjuBAFL/IMG20221101182714.jpg >

17:30:04 <Siren[m]> They must suffer for what they have done

17:30:05 <monerobull[m]> The Vilnius person is mega based donated multiple boxes

17:30:58 <monerobull[m]> Siren[m]: Surprised that it's still on there

17:31:24 <merope> <pandapaperwallet> "design1.pdf" <- plowsof they did send a sample

17:31:24 <monerobull[m]> I thought they are decently easy to remove ion one piece

17:32:40 <Stnby[m]> monerobull[m]: Noooo

17:32:46 <Stnby[m]> They are hard af to remove

17:33:09 <Siren[m]> monerobull[m]: Nope they rip easily

17:33:18 <Siren[m]> Which is actually good

17:33:22 <Siren[m]> They get pissed and give up

17:33:24 <Stnby[m]> Perfect for vandalising the city

17:33:55 <Stnby[m]> If they rip it we put 2 extra next day

17:34:00 <monerobull[m]> Kek I've never tried to remove em

17:35:47 <plowsof> endor00: reminds me of https://xmr.gift/templates/black/ if this is something we like then
pay the community member(s) who spear headed the gift card movement voluntarily

17:37:55 <merope> But this isn't about gift cards 🤔

17:38:06 <plowsof> imagine 2 applications "hello im behind xmr - gift , i want to also make templates for
wallet recover" vs "hello i have no experience, heres a proof of concept and im a random person"

17:39:10 <merope> Strictly speaking, that doesn't preclude the latter from delivering a nice design

17:39:39 <plowsof> which of the two would have our support?

17:40:09 <plowsof> if we want nicer designs we know people who can produce them already

17:41:16 <merope> Both? While I share the reticence towards funding unknown people, I don't think that should
be enough to reject a proposal. Otherwise you're driving outsiders away

17:43:07 <merope> The final decision to fund the proposal should be up to the donors themselves, not to us
discussing it

17:43:10 <plowsof> "driving outsiders away" only when we don't need to outsource the labour

17:43:12 <plowsof> e.g. https://monero.graphics/

17:45:06 <plowsof> but ofcourse, if there is no competing proposal...

17:45:12 <merope> plowsof: I don't see a ccs proposal for paper wallet designs from them though

17:45:19 <merope> (oops, network lag)

17:47:04 <plowsof> it was posted several hours ago*

17:47:07 <merope> Aside from filtering out the "obviously bad" stuff, I don't think it's up to us to decide
whether a proposal *should* be funded

17:50:02 <plowsof> what about "obviously better"?

17:50:10 <plowsof> or shld there be 2 ccs' for monero paper wallets simultaneously (or a few weeks apart) for
paper wallets

17:51:12 <merope> Why not? Why shouldn't there be two competing proposals?

17:51:12 <plowsof> if i contact gnuteardrops of monero.graphics and he posts a ccs for example

17:51:17 <ofrnxmr[m]> plowsof:  panda said they would release a free copy for people to use and try

17:51:24 <plowsof> two competing proposals moved to funding?

17:51:27 <ofrnxmr[m]> So we can know better if we went to fund 20 more

17:51:31 <ofrnxmr[m]> Want

17:51:57 <plowsof> true, this is a great 1st step

17:52:09 <merope> plowsof: Yep

17:52:35 <plowsof> has that ever happened?

17:53:25 <merope> Otherwise, it's 10 of us in this chatroom right now deciding whether a proposal is "worthy"
of funding for *all potential monero donors*, purely based on our personal preference

17:53:59 <merope>  * Otherwise, it's 10 of us in this chatroom right now deciding whether a proposal is
"worthy" of funding in the name of _all potential monero donors_, purely based on our personal preference

17:54:04 <ofrnxmr[m]> I try not to vote with person anything

17:54:31 <ofrnxmr[m]> If I dont like a proposal, its usually for a reason I feel is valid and being overlooked

17:55:24 <merope> And I don't think that would be fair towards proposers

17:55:24 <plowsof> (sometimes less than 10) but these meetings don't decide (in isolation) , its the overall
feedback obtained throughout the time the proposal is at the idea stage (be it from gitlab/reddit/irc)

17:55:24 <ofrnxmr[m]> Example, panda proposal when nobody knows what they are actually proposing

17:56:16 <merope> ofrnxmr[m]: 10 paper wallet designs in 10 milestones? seemed pretty straightforward to me.
Why would that *not* be a **valid** proposal?

17:57:06 <ofrnxmr[m]> I can create 10 paperwallets with a pencil and my big toe

17:57:25 <merope> And nobody's stopping you

17:57:30 <ofrnxmr[m]> Which is why an example was asked of, and why I requested a working model

17:57:46 <ofrnxmr[m]> And panda seems to feel that to be reasonable

17:58:03 <ofrnxmr[m]> Which should also help garner support / clear the noise

17:58:07 <merope> And they sent a wip design

17:58:12 <aremor[m]> ofrnxmr[m]: But will you do it. Or anyone else for that matter

17:58:32 <ofrnxmr[m]> Endor, were arguing the same point?

17:59:31 <merope> My point is that, in spite of the fact that this proposal seems perfectly valid, you voted
against it (while claiming that you vote against proposals that have issues/are not valid)

18:00:04 <ofrnxmr[m]> I simply asked panda to submit a working version and they obliged?

18:00:09 <plowsof> i think it was me who voted against it? or

18:00:18 <ofrnxmr[m]> For further voting

18:00:42 <plowsof> its new so not much to vote on

18:00:56 <merope> <ofrnxmr[m]> "Instaclose" <- ^

18:01:04 <ceetee[m]> ofrnxmr[m]: live stream pls 😍

18:01:14 <ofrnxmr[m]> I missed the /s ? Lol

18:01:39 <plowsof> im just saying that i "know of people" who could do better (until of course, Panda proves
otherwise - and now he has released a proof of concept design so thats a good start)

18:03:22 <merope> But that doesn't mean that we should be rejecting someone else's proposal

18:03:54 <plowsof> Members of Core agree/share your opinion, that we should not make the decision on who is
worthy of getting funding

18:04:01 <ofrnxmr[m]> Then the better person should open a proposal

18:05:09 <merope> Then all people should open a proposal, and it should be up to the donors to decide whether
to fund one, the other, both, neither, or anything else

18:06:21 <ofrnxmr[m]> Moon and observer have "competing ccs". Cant believe I forgot about that example

18:06:24 <plowsof> if all people where able to open a proposal we might have more proposals in my
purgatory/OTHER list with unfinished milestones

18:06:53 <plowsof> thus creating a bad look for the following proposals that come after it

18:08:56 <ofrnxmr[m]> Panda: sorry for using you as an example 😂. Nothing against you or your proposal

18:09:18 <plowsof> Panda sorry, you have/are doing everything correct

18:10:21 <plowsof> my bias is that i want to show everyone the great work of some other contributors is all,
clouding my decisions


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2022-11-05T19:32:04+00:00
cont:
```
18:14:01 <ofrnxmr[m]> Like.. I could use some more monerochan from a new artist 🤷‍♂️
18:19:19 <pandapaperwallet> No problem, by the way I do have another proof of concept design as wip if you are interested. This is a project I already started for myself and I just wanted to share my work with the community
18:25:10 <Stnby[m]> <pandapaperwallet> "No problem, by the way I do have..." <- Sure, I would be interested
```

# Action History
- Created by: plowsof | 2022-10-31T13:46:39+00:00
- Closed at: 2022-11-05T19:29:45+00:00
