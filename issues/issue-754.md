---
title: 'Monero Community Workgroup Meeting: Saturday 19th November 2022 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/754
author: plowsof
assignees: []
labels: []
created_at: '2022-11-14T12:48:02+00:00'
updated_at: '2022-11-20T01:12:06+00:00'
type: issue
status: closed
closed_at: '2022-11-20T01:10:29+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/countdown/launch?iso=20221119T16&p0=1361&msg=Monero+Community+Workgroup+Meeting%3A+Saturday+19th+November+2022&font=slab&csz=1)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [Forgotsudo monero marketplace](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/340)    
  b. [Develop selfhostable monero payment processor](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/345)    
  c. [Monero Paper Wallets](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/352)    
  d. [Metronero checkout](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/353)    
  e. [selsta part-time monero development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/354)    
  f. [xmr-btc-swap development and improvement](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/355)    
  g. [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/357)    
  h. [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358)    
  i. [j-berman full-time 3 months part 4](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/359)    
  j. [MoneroShopping](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/360)    
5. Workgroup reports    

  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
        Call For Presentations https://cfp.monerokon.com/2023/cfp
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
    - Complaints about the official Monero Twitter tweets/behaviour [logs](https://libera.monerologs.net/monero-community/20221119#c161084)
    - [Increase awareness of low-funded Mastodon tipbot bounty](https://bounties.monero.social/posts/22/0-015m-monero-tip-bot-for-mastodon-pleroma) - completed by silverpill with a new project called [Mitra](https://codeberg.org/silverpill/mitra)
    - on-going issue SoloptXMR more info in gitlab comments [here](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/299#note_19583) and Reddit [here](https://www.reddit.com/r/Monero/comments/yyohle/progress_report_on_ospead_fortifying_monero/)
8. Confirm next meeting date/time    

Previous meeting including logs #747    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2022-11-20T01:10:28+00:00
Logs 
```
16:00:17 <plowsof> Meeting time : https://github.com/monero-project/meta/issues/754

16:00:17 <plowsof> 2. Greetings

16:00:38 <plowsof> hi everyone

16:00:39 <Siren[m]> Hello

16:00:58 <spackle_xmr[m]1> hi

16:01:22 <plowsof> plug some news outlets while we wait : News: [Monero
Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero
Standard](https://localmonero.co/the-monero-standard)

16:02:16 <Rucknium[m]> Hi

16:02:43 <hinto[m]> hi

16:03:01 <sgp[m]> Hello

16:03:10 <nioc> meow

16:03:40 <plowsof> we've got some on-going drama with one of the ccs proposals (soloptxmr) but i'd like to
cover the ideas first as it would probably take up the entire hour if we start with that

16:04:01 <plowsof> with that said....

16:04:25 <plowsof>   a. [Forgotsudo monero marketplace](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/340)

16:04:33 <plowsof> last-last-final call - we're closing this pending resubmission of Web Of trust only

16:04:37 <plowsof> agree?

16:05:53 <monerobull[m]> <Stnby[m]> "What is a speaker contract?" <- Contact*

16:06:24 <Stnby[m]> Confidentiality papers 😋

16:06:38 <plowsof> and we're closing   b. [Develop selfhostable monero payment
processor](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/345)

16:06:38 <plowsof> , disagreements?

16:06:39 <Siren[m]> NDA

16:07:38 <plowsof> feedback requsted:   c. [Monero Paper Wallets](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/352)

16:08:05 <nioc> seems like a lot of money for something that we already have

16:08:16 <nioc> https://www.themonera.art/2018/01/30/printable-monero-paper-wallet-pack-1/

16:08:16 <plowsof> reg monero wallets*

16:08:34 <monerobull[m]> I'll be there in a bit

16:08:35 <plowsof> yes the proposer has submitted an "example" design

16:08:38 <Siren[m]> > <@plowsof:matrix.org> feedback requsted:   c. [Monero Paper
Wallets](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/352)

16:08:38 <Siren[m]> >

16:08:38 <Siren[m]> The designs aren't good enough

16:08:50 <Siren[m]> I think we should close it

16:09:38 <plowsof> i have contacted gnuteardrops - and being the kind soul they are they said they did not
with to interfere with anyone elses ccs' , but, if we really need new wallet designs, they open to the idea

16:10:02 <nioc> msvb also has an excellent wallet

16:10:19 <plowsof> an advanced one that is nuclear proof(tm)

16:10:33 <nioc> yes  :)

16:11:09 <plowsof> so, is there -anything- this proposer can do to win you over / change your opinions? is it
not a case of "making a better proof of concept design"?

16:11:31 <plowsof> we also have xmr.gift #xmr.gift:matrix.org

16:11:45 <MajesticBank> need better write up

16:12:00 <monerobull[m]> Did we vote on anything yet

16:12:07 <Stnby[m]> nioc: These are more visually appealing to m,e

16:12:07 <MajesticBank> add decoy designs

16:12:09 <Stnby[m]> s/m,e/me/

16:12:19 <plowsof> re-voting on closing forgotsudo/develop selfhosted (the one who wants money upfront)

16:12:56 <plowsof> so we have better alternatives already (compared to the example he has shown)

16:12:57 <nioc> close

16:13:57 <plowsof> it is specifically for 'wallet restore' i must say* but i feel we have alternatives / more
talented people than the proposer - i'd say close

16:14:06 <MajesticBank> we already have designers in the community that should have priority I guess

16:14:31 <plowsof> i agree +1 for rewarding community members who have contributed already

16:14:39 <Siren[m]>  close too imo

16:14:49 <nioc> close

16:15:05 <monerobull[m]> I don't think we should pay 2k on wallet designs by a non-professional designer

16:15:23 <plowsof> lets move on, this one needs some feedback / thoughts

16:15:26 <plowsof>   d. [Metronero checkout](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/353)

16:16:15 <monerobull[m]> Did the things get cleared up that needed clearing up?

16:16:16 <plowsof> ive left a comment with my initial thoughts / understanding of whats going on there , might
help to have a look

16:16:57 <Stnby[m]> plowsof: you understood it right Siren left a short reply

16:17:28 <Rucknium[m]> I have three main comments on this: 1) Does this solve the problems that most online
stores have with using Monero? Frequently people in IRC or Reddit ask if there is a payment system. Does this
solve it? Need research on market demand

16:17:29 <MajesticBank> checking

16:17:51 <monerobull[m]> This was the tor-optimized BTC pay server alternative

16:18:04 <Stnby[m]> rayatina: Huh?

16:18:07 <Siren[m]> Wdym? That's our real names

16:18:33 <Stnby[m]> monerobull[m]: Yeah Javascriptless and C# less

16:18:48 <Rucknium[m]> 2) I think this is "middleware", i.e. it requires an additional layer for a complete
solution. This proposal would be more useful if it developed one example of that final layer, but also allowed
other layers to be developed of course

16:18:49 <Stnby[m]> * C# less And Monero as a focus as BTCPAYserver is not ideal

16:18:51 <plowsof> thanks for the comment Siren!

16:19:24 <Siren[m]> Rucknium[m]: What final layer are you talking about?

16:19:26 <monerobull[m]> My only concern was, does it work with both viewkeys and RPC calls?

16:19:40 <Rucknium[m]> 3) It looks like it relies on monero-wallet-rpc, which is unreliable. How will
reliability  issues be handled, and is there any way that upstream fixes to reliability issues be fixed?

16:20:13 <monerobull[m]> monerobull[m]: Like serhacks wp plugin

16:20:16 <Stnby[m]> If monero-wallet-rpc is unreliable, Monero is unreloiable

16:20:22 <Stnby[m]> s/unreloiable/unreliable/

16:20:46 <Siren[m]> Rucknium[m]: Unreliable in what sense? Do you mean that it is not thread safe? Or do you
mean that the output from it is straight up inaccurate? What?

16:20:55 <plowsof> monero-wallet-rpc talking to a remote daemon is unreliable*

16:21:06 <Siren[m]> It doesn't have to remote

16:21:06 <MajesticBank> very

16:21:12 <plowsof> however  , moneropay has a health check built in?

16:21:14 <Siren[m]> It's up to the user

16:21:23 <Rucknium[m]> Merchants have to write POST requests, for example

16:21:26 <Rucknium[m]> plowsof: Can you comment on monero-wallet-rpc reliability?

16:21:31 <monerobull[m]> Siren: so viewkey support?

16:21:34 <Siren[m]> Rucknium[m]: And?

16:21:42 <Siren[m]> Yes there is viewkey support

16:22:55 <monerobull[m]> Can you point it at any xmrchain-style explorer? Wp plugin straight up didn't
acknowledge payments while xmrchain was down

16:23:03 <Siren[m]> plowsof: there is an endpoint for health checks

16:23:38 <Siren[m]> monerobull[m]: it doesn't use public blockchain explorers for payment processing. it uses
moneropay which relies on wallet-rpc server.

16:23:46 <plowsof> let me clarify a bit - it would be a "service" - hosted by a third party , that provides
you with a payment gateway (they handle everything - e.g. their node will be local etc) - it will have 2 modes
- one where you give them your view key, another , where you "withdraw funds" (custodial - where the host
provider can take a small fee)

16:24:01 <Rucknium[m]> This is plowsof's comment in the proposal 4 days ago: "With Metronero - merchants still
require a plugin to be created to actually 'use it' - If this is something that could be added/researched that
would be ideal (I believe a plugin that provides the same functionality as monerowp would make this project
complete, as it seems to be the one most widely used currently)"

16:24:12 <plowsof> OR you can be the "service" and host it yourself

16:24:24 <Siren[m]> Rucknium[m]: this is not correct

16:24:25 <MajesticBank> integration channel would be?

16:24:43 <Stnby[m]> Rucknium[m]: Yes it might need a very simple plugin, but the issue is we cannot create a
plugin for every system

16:24:44 <Siren[m]> however plugins for e-commerce would make it easier for people

16:25:10 <plowsof> yes how will it be integrated - how can someone "use" it - by creating something that makes
POST requests - would you consider making a plugin for 1 e-commerce platform

16:25:55 <plowsof> and you will have to fight the community regarding "free maintenance" - we force you to
make it paid (ask GUPAX) xD

16:26:03 <Siren[m]> what?

16:26:09 <MajesticBank> there are plugins already by monero-ecosystem

16:26:38 <Siren[m]> MajesticBank: plugins that are not functional at times because they rely on third party
blockchain explorers

16:26:46 <monerobull[m]> Bope

16:26:50 <monerobull[m]> Nope

16:26:53 <Siren[m]> or btcpay server probably

16:26:54 <monerobull[m]> They can use both explorer and rpc

16:27:15 <MajesticBank> must be 3 click integrate thing, make proposal wider I guess with plugins included

16:27:24 <plowsof> i would say most users point it at xmrchain (as its easier) but as we seen recently - it
went offline - and so did peoples shops

16:27:46 <Stnby[m]> MajesticBank: No one commented on the proposal apart from plowsof

16:27:54 <Stnby[m]> We can provide syllius plugin

16:28:02 <monerobull[m]> plowsof: My shop wasn't down, i just had to go in and mark orders paid mysel

16:28:25 <plowsof> we are just sharing feedback / sharing ideas (some people have only seen the idea just now)

16:28:46 <monerobull[m]> Which was doable since the wp plugin doesn't round so amounts would be different by
tiny amounts of picos

16:28:58 <Stnby[m]> We could also write Prefix support for ticket purchasing in the future

16:29:38 <monerobull[m]> Does it use integrated addresses?

16:29:47 <Siren[m]> no

16:30:02 <Stnby[m]> subaddresses

16:30:33 <plowsof> Prefix is the "middle layer" we're talking about?

16:30:41 <monerobull[m]> That's good to know. Wp plugin for example uses integrated addresses

16:30:58 <Siren[m]> plowsof: there is no middle layer, this is a checkout system like paypal or whatever

16:30:59 <Siren[m]> he seems confused on what this exactly is

16:31:07 <Stnby[m]> integrated addresses is a bad way to do it, subaddresses are meant exactly for this

16:31:13 <plowsof> we want someone to make that thing that lets us use the thing out of the box

16:31:30 <Stnby[m]> plowsof: everyones box is different

16:31:47 <Stnby[m]> for example I would never but wordpress in my box of things

16:31:49 <plowsof> so we must decide on what we want the box to be

16:31:59 <monerobull[m]> I want to know what a merchant needs to provide and if it's custodial it not

16:31:59 <Siren[m]> Rucknium: Take a look at one of the proprietary examples: https://coingate.com/integration

16:32:01 <Stnby[m]> s/but/put/

16:32:15 <monerobull[m]> s/it/or/

16:32:35 <Siren[m]> monerobull[m]: if it's not custodial he needs to provide viewkeys, if it's custodial just
his address.

16:33:10 <monerobull[m]> And does one need to set RPC connections or something?

16:33:25 <cryptogrampy[m]> This is basically an alternative to btcpayserver, yes?

16:33:27 <Siren[m]> monerobull[m]: if you're not the person hosting it, no

16:33:31 <Siren[m]> cryptogrampy[m]: yes

16:33:35 <plowsof> the service provider handles all the rpc/hosting stuff

16:33:37 <cryptogrampy[m]> and has the ability to host the service for other people?

16:33:40 <Siren[m]> yes

16:33:47 <plowsof> the service prov can be yourself , or a company

16:34:02 <monerobull[m]> And anyone could host the custodial version for others?

16:34:06 <Stnby[m]> Yes BTCPAY server just not written in C# and is Monero first and JSless (Tor Extreme
settings friendly)

16:34:18 <Stnby[m]> + customizations on payment page look

16:34:20 <Siren[m]> monerobull[m]: yes

16:34:25 <cryptogrampy[m]> it's very complicated to setup as well

16:34:36 <monerobull[m]> Cool, I'll become the darknets PayPal /s

16:34:54 <plowsof> so we need to decide on what we want the "let me use it for a shop that sells tickets" ?

16:34:55 <cryptogrampy[m]> I think it would be important to provide an integration with this

16:35:04 <cryptogrampy[m]> maybe wordpress or something

16:35:17 <cryptogrampy[m]> maybe not

16:35:18 <MajesticBank> just feel like we need solution for non-devs because devs can already figure it out on
their own

16:35:40 <plowsof> if they are willing to integrate it into something (wordpress) or other, then we'll have to
discuss that at a later time . solution for non-devs to use it yes

16:35:50 <monerobull[m]> I liked how simple it was to set up wp plugin checkout

16:36:10 <Stnby[m]> monerobull[m]: Not everyone uses wordpress, we don't for example

16:36:10 <MajesticBank> not sure who is end user of this

16:36:31 <monerobull[m]> Just saying the experience should be similar for setup

16:36:46 <cryptogrampy[m]> So is this a layer on top of moneropay?

16:36:53 <Siren[m]> yes

16:36:55 <Stnby[m]> MajesticBank: Larger players who want to accept Monero and have the payment paged look
well integrated

16:37:00 <Stnby[m]> s/paged/page/

16:37:18 <Siren[m]> or Tor people

16:37:22 <monerobull[m]> When i set it up, i had no idea what RPC even is and i also didn't want to point it
at my own node for privacy reasons

16:37:28 <Siren[m]> Siren[m]: including but not limited to

16:37:32 <hinto[m]> i don't mind the proposed api personally but as a compromise including a single working
out-of-the-box integration seems fair

16:37:46 <Stnby[m]> For example we are willing to write a plugin for https://sylius.com/

16:37:56 <cryptogrampy[m]> This might be another dumb question, but if you're already building out a server
with logins and templating, why not have the ability for merchant to add items/images/prices?

16:38:01 <Stnby[m]> Not some obscure wordpress clusterfuck

16:38:12 <Stnby[m]> wordpress aint even for e-commerce

16:38:16 <plowsof> if sylius can be shown to provide the same experience setup as wordpress then that would be
ideal

16:38:24 <MajesticBank> prestashop, magneto, wordpress, open-cart mostly needed

16:38:43 <Stnby[m]> World only uses Syllius and Magento

16:38:57 <Siren[m]> Stnby[m]: displaying items/images/prices pages should be handled not using a payment
gateway

16:38:58 <Stnby[m]> Who uses Prestashop?

16:39:15 <Stnby[m]> Welcome to 1964

16:39:32 <plowsof> an agreement on Magneto though

16:39:53 <MajesticBank> Just helping to shape this well for benefit of the proposal

16:39:54 <ofrnxmr[m]> Hi

16:39:55 <Stnby[m]> ofrnxmr[m]: Syllius is taking over

16:39:55 <plowsof> hi

16:40:15 <Stnby[m]> I worked in the e-commerce space I can tell Its only syllius and magento

16:40:41 <Stnby[m]> * and magento (big players)

16:41:06 <plowsof> ok so i think we've given our feedback on Metronero , to be up for re discussion , but we
like the project (and moneropay team are capable / contribute to the ecosystem already)

16:41:11 <Siren[m]> we can add another milestone for writing a sylius plugin, I'm not sure about magento
because it's mainly proprietary

16:41:26 <Stnby[m]> MajesticBank: Self hosted paypal for Monero, plugins are easy to make/fork existing

16:41:39 <cryptogrampy[m]> I think everyone would benefit if there was a plugin built out in addition to this

16:41:40 <cryptogrampy[m]> i'd be much happier to get behind it

16:41:49 <Stnby[m]> cryptogrampy[m]: Yes but not for wordpress just because someone worships it

16:42:18 <Stnby[m]> I mean we can write it by forking existing one and changing 10 lines of code

16:42:18 <cryptogrampy[m]> Stnby[m]: yeah I think choosing a popular ecommerce solution as you suggested is
fine and preferable

16:42:35 <monerobull[m]> Well, small shops are mostly WordPress and if you're a big shop you use gateways that
support multiple cryptos and fiat

16:42:45 <cryptogrampy[m]> I think people use wordpress because the plugin exists there

16:42:49 <cryptogrampy[m]> and it's fairly easy to setup

16:42:58 <plowsof> not because they like/know what wordpress is

16:43:04 <plowsof> or woocommerce

16:43:05 <Stnby[m]> They use wordpress because they go to shared-hosting solutiuons

16:43:09 <Stnby[m]> s/solutiuons/solutions/

16:43:23 <Stnby[m]> and with metronero you won't be enough just with PHP

16:43:32 <monerobull[m]> I use WordPress because woocommerce was easy to set up with the plugin

16:43:36 <Stnby[m]> as monero-wallet-rpc is obviously not written in PHP

16:43:48 <Siren[m]> well...

16:43:55 <plowsof> right, not long left now to go through the other ideas, theres alot of feedback here for
Metronero to look at

16:44:04 <plowsof>   e. [selsta part-time monero development (3 months)](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/354)

16:44:10 <monerobull[m]> Fund

16:44:11 <cryptogrampy[m]> i think coincards uses wordpress

16:44:11 <plowsof> selsta isnt with us today

16:44:15 <Siren[m]> Stnby[m]: regardless of the reason why, many people run it. we can attempt.

16:44:32 <Stnby[m]> Siren[m]: But syllius is priority

16:44:37 <Siren[m]> fair

16:44:38 <plowsof> +1 for selsta

16:44:58 <MajesticBank> selsta legit

16:45:37 <monerobull[m]> One more pls

16:45:49 <nioc> merge selsta

16:45:51 <ofrnxmr[m]> +1

16:45:54 <Rucknium[m]> +1 for selsta proposal.

16:46:10 <monerobull[m]> Ok that's 6 yes

16:46:10 <plowsof>   f. [xmr-btc-swap development and improvement](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/355)

16:46:22 <ofrnxmr[m]> Next order of business

16:46:49 <plowsof> ive contacted binarybaron who is yet to comment. this proposal seems half baked / ill
planned / money pit into an abandonned project / we've already sponsored someone else (binarybaron) to do this
work

16:47:01 <plowsof> however the title is very catchy !

16:47:01 <monerobull[m]> Does comit still have a future

16:47:22 <plowsof> no still un-maintained

16:47:33 <plowsof> and none of them are expert cryptographers

16:47:39 <monerobull[m]> And this proposal is for comit right

16:47:40 <MajesticBank> I've contacted binarybaron, still at greetins point

16:48:10 <ofrnxmr[m]> plowsof: ^

16:48:10 <plowsof> for me this is a wait for binarybaron to explain himself (because weve paid him to 'make it
work with a gui' )

16:48:15 <Rucknium[m]> Looks like a money pit to me. This proposal needs more time for feedback at least.

16:48:21 <monerobull[m]> Ok next

16:48:21 <plowsof> yeah

16:48:28 <ofrnxmr[m]> Either postpone for clarity or close

16:48:37 <plowsof>   g. [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/357)

16:48:49 <plowsof> he's not in here ehh

16:49:06 <nioc> do we already have a "radio"?

16:49:21 <monerobull[m]> We have 2 actually

16:49:22 <monerobull[m]> Or had

16:49:30 <monerobull[m]> Idk nobody listens to them

16:49:36 <ofrnxmr[m]> Target audience for a tts radio? Nobody

16:49:39 <ofrnxmr[m]> Close

16:49:39 <plowsof> ive spoken with him, he wants to come to us with some code / proof of concept that hes been
working on

16:49:40 <MajesticBank> sorry my internet is very slow

16:49:40 <MajesticBank> commit swap are not usable at this point, as website is disabled and GUI is forced on
testnet only

16:49:40 <MajesticBank> all providers seems not to be working at this point

16:50:00 <monerobull[m]> plowsof: Postpone?

16:50:04 <plowsof> majesticbank thats for raising this

16:50:07 <NotMtth[m]> Yo

16:50:26 <plowsof> NotMtth is here if you have any questions

16:50:41 <plowsof> other than wait for him to show some code?

16:50:47 <ofrnxmr[m]> Whether it works or not, it serves no purpose

16:50:57 <MajesticBank> I would listen to xmr radio but needs to be easy to use / listen

16:51:40 <ajs_[m]> nioc: yes.. xmr.radio... but can confirm not many listeners... maybe 6 on a good day

16:52:04 <plowsof> its mainly a "video show" / community

16:52:15 <hinto[m]> agree on waiting for a poc first

16:52:16 <ajs_[m]> i have move to i2p/tor only audio format

16:52:21 <ajs_[m]> due to costs

16:53:15 <ofrnxmr[m]> News will collected by us and streamed using Text2Speech directly onto the dedicated
room.

16:53:35 <plowsof> we need proof of concept / (i suggested to reach out to ajs to set up an example / hour
show or something so we can "see" what it is)

16:53:52 <plowsof> but you're busy with monerokon at the moment

16:54:05 <plowsof> we need to "see" something

16:54:07 <ofrnxmr[m]> Postpone then?

16:54:10 <plowsof> otherwise its just an idea

16:54:18 <plowsof> till next meeting

16:54:29 <plowsof>   h. [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/358)

16:54:46 <plowsof> full disclosure: i am not part of MRL or know anything about auditing

16:54:53 <monerobull[m]> Fund

16:54:59 <ofrnxmr[m]> Within 4 weeks, if at all possible

16:55:11 <monerobull[m]> MAGIC will probably fund additional audits

16:55:20 <nioc> monerobull is funding this?

16:55:22 <nioc> great

16:55:24 <ofrnxmr[m]> Fund

16:55:39 <monerobull[m]> Nono

16:55:43 <plowsof> this is part of several funding roudns to integrate bp++ into monero and eventually
seraphis. the selection process for who audited it was fair as i contacted several with previous work on
monero and CypherStack where the cheapest and available

16:55:55 <Rucknium[m]> Last MRL meeting we can to rough consensus about need and scope for this. BP++ has a
long road ahead of it and this is the first step.

16:56:09 <ofrnxmr[m]> Merge it

16:56:10 <Siren[m]> * have to be remote

16:56:11 <ofrnxmr[m]> Next

16:56:16 <monerobull[m]> nioc: MAGIC will fund audits outside of the scope of this proposal

16:56:21 <monerobull[m]> Probably

16:56:29 <nioc> oh something actually to do with the protocol?

16:56:31 <hinto[m]> i'm out of the loop, is there a roadmap for when/who will implement this after the audit?

16:56:31 <nioc> approve

16:56:41 <nioc> monerobull[m]: sorry, bad joke

16:56:44 <plowsof> begin of december , it will take 12~ days

16:57:09 <plowsof> vtnerd is working on a proof of concept. koe will work on implementation

16:57:14 <Rucknium[m]> This CCS proposal is an initial check on the mathematics in the paper. The paper is
written by a single person without any peer review so far.

16:57:58 <Rucknium[m]> If the math is incorrect and cannot be corrected, then that's the end of the line for
BP++

16:58:01 <ofrnxmr[m]> And it appears this audit will be done by cypherstack

16:58:03 <ofrnxmr[m]> (?)

16:58:10 <plowsof> to be clear : when its merged the author will be Monero Research Lab - i ave merely applied
feedback to a text document from the MRL team and contacted auditors on their behalf

16:59:07 <plowsof> there will be more than one paper review

16:59:07 <hinto[m]> ok sounds good

16:59:11 <plowsof>   i. [j-berman full-time 3 months part 4](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/359)

16:59:20 <monerobull[m]> Fund

16:59:21 <MajesticBank> more a MRL decision

16:59:32 <plowsof> MRL have appproved it

16:59:50 <plowsof> jut sharing/clarifying with community

17:00:15 <Rucknium[m]> Tentatively support. Would like to see more comments/communication from jberman's
fellow devs on the exact task list and scope.

17:00:25 <ofrnxmr[m]> Merge berman

17:01:01 <plowsof> yes i have shared it in the seraphis no wallet left behind room, awaiting their approval

17:01:03 <hinto[m]> Rucknium: agreed

17:01:12 <plowsof> which so far, from what ive read, they are supportive

17:01:41 <plowsof> shold i even mention monero shopping?

17:01:50 <ofrnxmr[m]> Yes

17:01:55 <nioc> MRL supports the proposal to review the paper is good

17:01:58 <ofrnxmr[m]> So I can say burn it

17:02:09 <monerobull[m]> ONE JILLION DOLLARS

17:02:13 <nioc> yes to jberman

17:02:15 <ofrnxmr[m]> Close monero shopping a week ago

17:02:30 <plowsof>   j. [MoneroShopping](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/360)

17:02:39 <Stnby[m]> monero shopping love the idea

17:02:54 <ofrnxmr[m]> All in favor of merging?

17:02:58 <monerobull[m]> The idea is already live in Proxystore and way cheaper

17:03:18 <ofrnxmr[m]> Yeah. Nobody.  Close it

17:03:20 <MajesticBank> next

17:03:21 <plowsof> the concept exists already yes but it was enjoyable to see

17:03:38 <plowsof> thats it, i now want to share Ruckniums update

17:03:41 <Stnby[m]> I like daily dose of spam from him

17:03:57 <Stnby[m]> * from him (10 emails from gitlab every morning)

17:04:06 <plowsof>
https://www.reddit.com/r/Monero/comments/yyohle/progress_report_on_ospead_fortifying_monero/

17:04:36 <ofrnxmr[m]> Before we leave, I want consensus that plowsof should be able to collect his first
milestone, and that mj should be collecting any more funds until the work is completed as initially proposed

17:04:36 <Rucknium[m]>
https://www.reddit.com/r/Monero/comments/yyohle/progress_report_on_ospead_fortifying_monero/

17:04:39 <ofrnxmr[m]> Anyone against?

17:04:57 <plowsof> a Public version of ruckniums OSPEAD research has been released. i have not read it myself,
but the first page seems 'reader friendly'

17:05:24 <Stnby[m]> ofrnxmr[m]: never against plowsof

17:05:48 <Rucknium[m]> For those in previous -community meetings, the document linked here ^ contains the
"Document A" mentioned previously, plus a lot of other research.

17:05:53 <ofrnxmr[m]> Mj should not* be

17:06:21 <plowsof> Thank you Rucknium!

17:06:44 <Rucknium[m]> https://github.com/Rucknium/OSPEAD/blob/main/OSPEAD-Fully-Specified-Estimation-Plan-
PUBLIC.pdf

17:06:52 <Rucknium[m]> ^ This file

17:07:23 <nioc> agree ooofrnxmr

17:07:58 <Siren[m]> i also agree with ofrnxmr, he is based

17:08:11 <plowsof> dont forget MoneroKons call for presentation submissions
https://cfp.monerokon.com/2023/cfp (moneropay set this up right? and are even volunteering for further help?)

17:08:39 <monerobull[m]> Uuhm

17:08:39 <ajs_[m]> comments, suggestions for improvement

17:08:40 <monerobull[m]> Is that already REALLY live?

17:08:43 <Stnby[m]> plowsof: Digilol.net team :) but yeah same people as MoneroPay

17:08:48 <monerobull[m]> Last time it wasn't

17:08:53 <plowsof> sorry, feedback for edits*

17:09:18 <plowsof> e.g. colour scheme? everyone was mean about the green

17:09:19 <plowsof> so it was changed/ better??

17:09:28 <ajs_[m]> should be up officially after next week's planning meeting

17:09:28 <monerobull[m]> The green was changed, nice

17:09:32 <plowsof> i like it

17:09:38 <ajs_[m]> content?

17:09:50 <plowsof> llove it

17:10:25 <monerobull[m]> Submission go to the monerokon emai

17:10:33 <monerobull[m]> s/emai/email?/

17:11:15 <plowsof> this year, having a full 5 months for people to submit will be a huge improvement , thank
you

17:11:40 <Stnby[m]> I hope the event goes all well, really thrilled for it

17:12:05 <Siren[m]> I hope we'll have enough funds for Prague

17:12:11 <ajs_[m]> i get an email alert

17:12:16 <plowsof> the edit to bursary funding , i like also, seems fair

17:12:19 <Stnby[m]> If there are more IT tasks to be done for MoneroKon ping me or Siren :)

17:12:32 <Siren[m]> Anything you want to be hosted

17:12:37 <monerobull[m]> Where would hours be logged?

17:12:42 <MajesticBank> funding for the monerokon to the roof

17:13:01 <plowsof> ajs , how many top sponsors can it have?

17:13:08 <plowsof> 8kusd with only 2 spots?

17:13:13 <monerobull[m]> 3

17:13:15 <nioc> 3 spots now

17:13:17 <ajs_[m]> 3

17:13:23 <plowsof> thank you

17:13:35 <nioc> check updated budget

17:13:40 <monerobull[m]> It's also 3 days this time

17:13:40 <ajs_[m]> here is the draft ccs by the way https://repo.getmonero.org/ajs/ccs-
proposals/-/blob/monerokon-2023-ccs-1/monerokon-2023-ccs-1.md

17:13:40 <ajs_[m]> still wip

17:13:44 <MajesticBank> more sponsors the better

17:14:19 <plowsof> how would a sponsor get on the 3 list? - is blind bidding happening?

17:14:37 <ajs_[m]> don't know yet

17:14:37 <ajs_[m]> tbd

17:14:45 <plowsof> ok ok

17:14:48 <monerobull[m]> First come first serve?

17:14:55 <plowsof> how to be first though?

17:15:05 <ajs_[m]> open to ideas

17:15:13 <Stnby[m]> Are there usually more sponsors than the allocated amount (is the demand such high)?

17:15:31 <ajs_[m]> last event we just asked cake wallet and rino.io

17:15:56 <plowsof> there might be a bit more competition for the top spots this year (this is my guess)

17:16:00 <Rucknium[m]> Bidding is a good idea IMHO. Let the market set the price. Hopefully high enough to
covers lots of cost :)

17:16:01 <Stnby[m]> Oh so we approach first?

17:16:07 <MajesticBank> it's tight, we all love to support monero

17:16:12 <nioc> last year was a bit hectic so....

17:16:23 <nioc> not much time

17:18:04 <plowsof> to follow things/meetings about monerokon -> #monero-events:monero.social

17:18:40 <plowsof> footnote regarding twitter comment complaints     - Complaints about the official Monero
Twitter tweets/behaviour [logs](https://libera.monerologs.net/monero-community/20221119#c161084)

17:18:47 <Stnby[m]> plowsof: Every single time someone suggests a different room, the conversation halts :)

17:19:03 <MajesticBank> if someone can make ccs for meetings calendar, that would be funded most likely

17:19:32 <MajesticBank> twitter went a bit

17:20:24 <Rucknium[m]> We already have a CCS-funded meetings calendar I thought:
https://monero.observer/tag/calendar/

17:20:25 <monerobull[m]> Oh yeah Twitter

17:20:32 <monerobull[m]> Not nice

17:20:55 <Stnby[m]> Feels like this room is filled with grandmas :D, Twitter seriously?

17:21:06 <Rucknium[m]> I don't know what happened, but Twitter tweeting power should be more decentralized.
Cake has too many things at this point.

17:21:31 <monerobull[m]> The official Twitter account started swearing and shitting on the ada sidechain

17:21:34 <plowsof> silverpill with a new project called [Mitra](https://codeberg.org/silverpill/mitra)
fediverse with monero tipping? eth wallet login? wat?

17:21:51 <Stnby[m]> Monero self-hosted mastodon, when?

17:22:06 <monerobull[m]> plowsof: It's cool but feedieverse has zero users

17:22:20 <monerobull[m]> * It's cool but fedieverse has zero users

17:22:20 <plowsof> this mitra project has "completed" a bounty (that had zero funding)
https://bounties.monero.social/posts/22/0-015m-monero-tip-bot-for-mastodon-pleroma

17:22:38 <MajesticBank> Rucknium[m]: thanks, great thing

17:22:41 <Rucknium[m]> I'm thinking of spinning up a single-user Mastodon instance. I've been banned on
Twotter since I created the account 🥲

17:23:17 <MajesticBank> Social networks like twitter and telegram do need some decentralization

17:23:19 <Stnby[m]> Rucknium[m]: I was banned during the CoC adoption period.

17:23:38 <Stnby[m]> * the CoC mass adoption period.

17:24:43 <ajs_[m]> Stnby[m]: i was actually thinking about doing an "invite only" mastodon instance for
monerokon.com as a perk for sponsors, VIP ticket holders, and CCS donors

17:25:29 <Rucknium[m]> *Twitter, I meant. Looks like meeting is over.

17:25:34 <plowsof> we've ran over on time so i will share the on going soloptxmr issue - gitlab comments
[here](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/299#note_19583) and Reddit
[here](https://www.reddit.com/r/Monero/comments/yyohle/progress_report_on_ospead_fortifying_monero/

17:25:54 <Stnby[m]> ajs_[m]: Maybe, don't forget the speakers

17:26:06 <plowsof> plenty of reading and reviewing to do ! thank you all for attending

17:27:27 <plowsof> oh hinto

17:27:30 <monerobull[m]> Thanks for hosting!

17:27:50 <plowsof> https://gupax.io/

17:27:50 <nioc> thx plowsof

17:27:56 <Stnby[m]> Oh yeah we will try to look at existing Syllius, Prefix and WooCommerce plugins and maybe
estimate time needed to have this in Metronero and possibly a 3rd milestone, we will be waiting for comments
on the MR. Thank you everyone for feedback

17:28:15 <plowsof> xxx


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued:
```
17:30:01 <plowsof> unban rayatina yes/no 
17:30:25 <MajesticBank> We are gentlemen for some of those "privacy" crypto projects. Was good meeting
17:31:13 <Siren[m]> plowsof: yes, my favorite turk
17:31:50 <ajs_[m]> Stnby:  of course, and volunteers as well
17:32:11 <ofrnxmr[m]> <plowsof> "we've ran over on time so i will..." <- Either close it, since its been taken over by a scammer 
17:32:32 <ofrnxmr[m]> Or dont payout until its completed as initially proposed
17:33:23 <ofrnxmr[m]> Referring to solopt and mj's repeated attempts to undermine and take advantage of ccs and the community 
17:33:48 <ofrnxmr[m]> He claims youre (plowsof) incompetent for not being able to solve the issue 
17:34:25 <ofrnxmr[m]> The issue is simple - he tried to pull a fast one again, again, again, and got caught again, again. We've already paid him to go away once
17:34:50 <ofrnxmr[m]> Since when does a scammer get to just keep coming back for more, and getting it - simply because we refuse to say "no".
17:35:35 <Siren[m]> ofrnxmr[m]: This time it was way too obvious
17:36:16 <Siren[m]> Why is he refusing to comment on it? He literally was like here you go guys, I removed it now let's not talk about it.
17:37:25 <Siren[m]> The messages where he accuses people of incompetency and then himself hard coding versions without providing hashes was also a bruh moment
17:37:55 <ofrnxmr[m]> And you didnt tell your partner? I mean, employee? I mean, this is my project but im leaving early even though I  specifically said I would not
17:38:22 <Siren[m]> Siren[m]: I think it would be a better look if he confessed to leaving that in by accident or somehow being half awake at the time of programming and messing up the maths
17:39:10 <ofrnxmr[m]> Mj claims its release ready, and in the same sentence called it a release candidate 
17:40:18 <Siren[m]> It's too shady
17:40:34 <ofrnxmr[m]> Anyway.. its a huge waste of everyones time to spend everyday worrying about what mj wants
17:40:47 <ofrnxmr[m]> Mj. You deliver the pizza, you get paid. Kapeesh?
17:43:04 <ofrnxmr[m]> "In the most profitable way" 🥹20% net mining rewards loll
```

# Action History
- Created by: plowsof | 2022-11-14T12:48:02+00:00
- Closed at: 2022-11-20T01:10:29+00:00
