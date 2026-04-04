---
title: 'Monero Community Workgroup Meeting: Saturday 16th September 2023 @ 15:00 UTC'
source_url: https://github.com/monero-project/meta/issues/893
author: plowsof
assignees: []
labels: []
created_at: '2023-09-11T08:13:27+00:00'
updated_at: '2023-09-25T11:29:25+00:00'
type: issue
status: closed
closed_at: '2023-09-25T11:29:25+00:00'
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
    - Monero celebrates 80M outputs https://p2pool.io/explorer/tx/5dbd3a47b1174d0442aed9f4ad87e5704b2b905e35a2e4e288649b422c1aea8b
    - Release v18.3.0 imminent 
    - RandomX to undergo some changes https://github.com/tevador/RandomX/pull/274 follow the discussion in [#monero-pow](https://libera.monerologs.net/monero-pow/20230907)
    - spackle_xmr "I've put up 3 python scripts for wallet management via RPC: Fracture, Consolidate, and Churn. See here: https://github.com/spackle-xmr/MoneroTools/"     
    - monerosupplies.com adds Bitcart.ai as a payment processor and now accepts multiple cryptocurrencies (XMR/LTC/BTC/BCH)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/) - [Monero Garden](https://twitter.com/anhdres/status/1702303928530936206?t=eWOsKH_nwVqAGieL4Ziluw&s=19) / [Haveno](https://github.com/haveno-dex/haveno/releases)
  a. [recanman to take over Monero integrations pt. 3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/402) 
  b. [Add retroactive funding proposal for FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)    
  c. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/406)  
  d. [Selfhosted tor gitea instance of monero source](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/408)    
  
8. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
9. Open ideas time    
10. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-09-20T18:47:04+00:00
Logs 
```
15:00:09 <plowsof> Meeting time: https://github.com/monero-project/meta/issues/893

15:00:37 <MajesticBank> hi

15:00:42 <plowsof> greetings! hello

15:00:54 <msvb-lab> Hello.

15:00:57 <m-relay> <s​needlewoods_xmr:matrix.org> hey there

15:02:20 <nioc> Cat is here

15:02:40 <m-relay> <o​frnxmr:monero.social> Hello

15:02:47 <plowsof> lets discuss some highlights while we wait for people to roll in

15:03:31 <plowsof> selsta has been putting the next release together (18.3) - currently undergoing some
testing - so if you want to compile the release v18 branch and put up a node, please do!

15:04:22 <plowsof> moneros next hardfork will more than likely be to implement tevadors PoW verification
changes (to mitigate denial of service attacks against nodes) more info here: https://github.com/monero-
project/monero/issues/8827

15:04:39 <m-relay> <o​frnxmr:monero.social> Nice 🚀

15:04:47 <m-relay> <p​lowsof:matrix.org> this hardfork gives an opportunity for some RandomX changes:
https://github.com/tevador/RandomX/pull/274 that will give "free" hashes to some AMD cpus (around >+8% in
testing) (best palce to ask about this is in #monero-pow)

15:05:35 <MajesticBank> nodes anti-ddos is important, great work

15:06:04 <m-relay> <p​lowsof:matrix.org> Monero celebrates its 80 millionth output (via p2pool observer, the
only explorer with a tor link? thanks to sech1 outputs
https://p2pool.io/explorer/tx/5dbd3a47b1174d0442aed9f4ad87e5704b2b905e35a2e4e288649b422c1aea8b

15:06:19 <m-relay> <p​lowsof:matrix.org> s/observer/explorer

15:06:59 <m-relay> <o​frnxmr:monero.social> Both work :P p2pool.observer

15:07:34 <m-relay> <p​lowsof:matrix.org> in #monero-community-dev spackle_xmr shared a churning script
(working off of Monerujos pocketchange methods) "I've put up 3 python scripts for wallet management via RPC:
Fracture, Consolidate, and Churn. See here: https://github.com/spackle-xmr/MoneroTools/"

15:08:39 <m-relay> <o​frnxmr:monero.social> whoever is doing the churning research should look at spackles
work as well

15:09:51 <plowsof> https://bitcart.ai/ (a full featured crypto payment processor)  being used in the wild  @
monerosupplies.com (payment in XMR/BTC/LTC/BCH)

15:10:37 <plowsof> monerobull had issues with the monero wordpress / monero-php being blocked by a new host or
something, and now has bitcart as an alternative

15:11:18 <plowsof> MrNaif is the developer ... hopefully they gain support for helping Monerokon somewhere

15:12:38 <plowsof> any other community highlights people want to talk about? [Revuo Monero](https://revuo-
xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard)

15:14:05 <MajesticBank> I would like to mention that monerica.com shadow removed me from their website

15:14:14 <m-relay> <p​lowsof:matrix.org> 2 CCS projects shared updates also: [Monero
Garden](https://twitter.com/anhdres/status/1702303928530936206?t=eWOsKH_nwVqAGieL4Ziluw&s=19) /
[Haveno](https://github.com/haveno-dex/haveno/releases) (testers for haveno welcome) #haveno:haveno.network

15:14:32 <MajesticBank> on similar date as they listing on getmonero site is approved
https://github.com/monero-project/monero-site/pull/2117

15:14:53 <m-relay> <p​lowsof:matrix.org> i made an issue about this, and it was closed today with a comment
https://github.com/monerica-project/monerica/issues/129

15:15:31 <m-relay> <a​nhdres:matrix.org> Yeah now I'm really close to have the text ready. I have to learn the
whole GitHub publishing thing

15:15:32 <MajesticBank> in the index.html @
https://github.com/monerodice/monerica/blob/487419b43d0b32d774028af2c747b4eb63e14eac/src/index.html#L2180 (but
not on the live site) - monerodice was added to index (after mb) and can be seen on the live site

15:15:39 <MajesticBank> oh so site is offline, makes sense

15:15:44 <m-relay> <p​lowsof:matrix.org> sorry anhdres, i meant to tag you !

15:15:45 <m-relay> <a​nhdres:matrix.org> And right after will start working on the images

15:17:08 <m-relay> <p​lowsof:matrix.org> thank you for the update ⚽️🦶

15:17:24 <m-relay> <o​frnxmr:monero.social> Technically haveno isnt a ccs oroject

15:17:39 <m-relay> <o​frnxmr:monero.social> The frontend is, and the frontend has no updates

15:17:56 <m-relay> <p​lowsof:matrix.org> (we have to keep saying it is so we get our 0.0001% returns)

15:18:13 <m-relay> <m​onerobull:matrix.org> Hello

15:19:05 <m-relay> <p​lowsof:matrix.org> Lovera and 4rkal posted some new ccs proposals since the last
meeting, seems like anough people are here to jump into the merge list

15:20:18 <m-relay> <p​lowsof:matrix.org> right, again, recanmanns:

15:20:29 <m-relay> <p​lowsof:matrix.org> a. [recanman to take over Monero integrations pt.
3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/402)

15:21:09 <m-relay> <m​onerobull:matrix.org> Hehe

15:21:14 <m-relay> <p​lowsof:matrix.org> another dev appears to have re-written their own fork of the monero-
php library which may have solved the issues from milestone 1 in the "Monero integrations" proposal

15:21:22 <m-relay> <p​lowsof:matrix.org> https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/402#note_22340

15:21:25 <m-relay> <m​onerobull:matrix.org> Is anyone actually using that plugin 🤔 /s

15:22:10 <m-relay> <p​lowsof:matrix.org> however, that work has to be 'made sense of' / adapted / and worked
into the official monero-php library - all this, for 4 xmr

15:23:34 <m-relay> <p​lowsof:matrix.org> and milestone 2 , Monero Woocommerce payment gateway maintenance, is
uneffected, with 7 xmr in funds. i feel the proposal is unaffected and support recanmann to take it over
(basically give serhack a helping hand, who is busy)

15:26:43 <m-relay> <o​frnxmr:monero.social> I +1 what plowsof said

15:27:58 <m-relay> <p​lowsof:matrix.org> thanks for the feedback, we can move on if nobody has a comment

15:28:06 <m-relay> <p​lowsof:matrix.org> @nobody

15:28:13 <m-relay> <o​frnxmr:monero.social> @nobody

15:28:15 <m-relay> <o​frnxmr:monero.social> Lmao

15:28:20 <m-relay> <o​frnxmr:monero.social> Jinx

15:28:24 <m-relay> <p​lowsof:matrix.org> lol

15:28:42 <MajesticBank> next

15:28:43 <m-relay> <p​lowsof:matrix.org> ok moving on

15:28:45 <m-relay> <p​lowsof:matrix.org> b. [Add retroactive funding proposal for
FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)

15:29:08 <nioc> is this like that Tesla proposal?

15:29:22 <MajesticBank> close it already

15:29:23 <m-relay> <o​frnxmr:monero.social> Merge with expiry

15:29:25 <m-relay> <p​lowsof:matrix.org> luigi "I think I'll merge it if there's an expiration for funds
gathering and plan for underfunding"

15:29:40 <m-relay> <p​lowsof:matrix.org> so it will be merged

15:29:40 <m-relay> <m​onerobull:matrix.org> Merge

15:29:49 <m-relay> <m​onerobull:matrix.org> Movie ccs was retroactive

15:29:51 <m-relay> <o​frnxmr:monero.social> ```

15:29:51 <m-relay> <o​frnxmr:monero.social> <l​uigi1111w> I think I'll merge it if there's an expiration for
funds gathering and plan for underfunding

15:29:52 <m-relay> <o​frnxmr:monero.social> ```

15:30:11 <m-relay> <o​frnxmr:monero.social> Movie ccs has 0 potential roi

15:30:21 <m-relay> <m​onerobull:matrix.org> For all intents and purposes. We have precedence

15:30:27 <m-relay> <o​frnxmr:monero.social> Frontend ccs is vaporware

15:30:38 <m-relay> <o​frnxmr:monero.social> Kayas ccs is actual code

15:30:56 <m-relay> <o​frnxmr:monero.social> Solopt is "optional milestones w*th full pay"

15:31:31 <m-relay> <o​frnxmr:monero.social> While it shoyldnt set precedent, i believe kaya's attempt to get
started before putting up the ccs was in good faith

15:31:32 <MajesticBank> this merge will bring more good then bad, but I guess we can give him 1 month period
to get funded

15:31:43 <m-relay> <o​frnxmr:monero.social> He coukd be like molly and just never deliver, right lol

15:31:47 <MajesticBank> otherwise put funds back to general fund

15:31:51 <m-relay> <o​frnxmr:monero.social> 3 months

15:32:03 <nioc> 3 months better than 1

15:32:07 <m-relay> <o​frnxmr:monero.social> jet fund*

15:32:32 <m-relay> <p​lowsof:matrix.org> iirc kayaba intends on putting up another ccs for further work (but
isnt promising anything)

15:32:32 <m-relay> <o​frnxmr:monero.social> Aka, go towards other dev proposals

15:32:55 <m-relay> <o​frnxmr:monero.social> yes. Fcmp, this is just part 1. Still need a lot of work to
actually implement (proofs, audits, yadayada)

15:33:26 <m-relay> <p​lowsof:matrix.org> hopefully he didnt overwork himself and needs a hiatus

15:33:35 <MajesticBank> Kaya didn't accept any recommendation from the community, not even one

15:33:40 <MajesticBank> it's a disgrace

15:33:46 <nioc> I don't think that people will be motivated to donate if it misses the goal and the funds go
to the GF

15:33:49 <m-relay> <o​frnxmr:monero.social> Majestic doesnt have ears or eyes

15:33:59 <m-relay> <o​frnxmr:monero.social> Bribejestic shh

15:34:06 <nioc> I want devs to be funded

15:34:06 <m-relay> <o​frnxmr:monero.social> Go kick a keyboard

15:34:17 <m-relay> <m​onerobull:matrix.org> There has been less activity on serai GitHub this week 😬

15:34:29 <m-relay> <o​frnxmr:monero.social> Me too nioc:  and not shit copy pasta elitewallet devs

15:34:52 <m-relay> <m​onerobull:matrix.org> Maybe a milestone in fundraising

15:35:01 <m-relay> <m​onerobull:matrix.org> Just so he can pay the people he already hired for the work

15:35:05 <m-relay> <p​lowsof:matrix.org> thats usually why workers are forbidden to work so many hours a week

15:35:27 <m-relay> <o​frnxmr:monero.social> I thought it was so i had to take 2 jobs and not get overtime?

15:35:31 <MajesticBank> This is putting salt in mouth of other people around monero, just saying, how you can
do something on your own and ask payment whichever you want later

15:35:51 <m-relay> <o​frnxmr:monero.social> Ask geonic

15:35:58 <m-relay> <o​frnxmr:monero.social> Maybe he can tell you

15:36:23 <m-relay> <m​onerobull:matrix.org> Majestic, FCMP is arguably wanted by everyone

15:36:36 <nioc> ^^^^^^^^^^

15:36:52 <MajesticBank> You missed the comments on then ccs I guess then

15:36:55 <m-relay> <o​frnxmr:monero.social> Its research funding as far as im concerned.

15:36:56 <m-relay> <o​frnxmr:monero.social> Whether we implement or not, i support the initiative.. especially
considering its not vaporware like a lot of these other ccs

15:37:04 <m-relay> <m​onerobull:matrix.org> It's not like he is asking money for an unrelated pet project

15:37:35 <m-relay> <p​lowsof:matrix.org> we don't have to argue about it anymore, it will be merged pending
expiry dates / underfunding plans

15:37:47 <nioc> the CCS, formally known as the FFS, was created to fund devs and research

15:37:48 <MajesticBank> next

15:37:49 <m-relay> <p​lowsof:matrix.org> our suffering is relinquished

15:37:51 <nioc> not marketing

15:38:09 <m-relay> <o​frnxmr:monero.social> Ty

15:38:32 <m-relay> <p​lowsof:matrix.org> lets move on , pending kayabas input

15:38:41 <m-relay> <p​lowsof:matrix.org> c. [Create Educational Content in
Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/406)

15:38:58 <m-relay> <m​onerobull:matrix.org> Didn't we vote merge on this last time already

15:39:05 <m-relay> <o​frnxmr:monero.social> Lovera did well by us the last time

15:39:19 <m-relay> <m​onerobull:matrix.org> I remember because I was watching the final showdown of John whick
4 at that time

15:39:24 <m-relay> <p​lowsof:matrix.org> will luigi let the ccs fund someone 3 usd/hour is the question

15:39:46 <nioc> they should lower their price

15:39:50 <MajesticBank> I don't mind the merge but checked his youtube the views are like 200 views per month

15:40:11 <MajesticBank> could be a better

15:40:43 <m-relay> <m​onerobull:matrix.org>
https://matrix.monero.social/_matrix/media/v1/download/matrix.org/XNISRoDLTBJAPOaqgsSptHPv

15:40:44 <m-relay> <m​onerobull:matrix.org> We should fund this guy

15:40:44 <m-relay> <s​needlewoods_xmr:matrix.org> but if we will not merge and Lovera still does the work,
that's 0 $/h

15:40:46 <m-relay> <o​frnxmr:monero.social> same price as last time

15:41:04 <m-relay> <m​onerobull:matrix.org> But he already does it for FREE

15:41:12 <m-relay> <o​frnxmr:monero.social> Hes got moolah

15:41:22 <m-relay> <o​frnxmr:monero.social> with lovera, i expressed many concerns with the first ccs

15:41:34 <m-relay> <p​lowsof:matrix.org> he would destory his channel if he was forced to make content for us
every week probably?

15:41:35 <m-relay> <o​frnxmr:monero.social> Regarding which channek things would be posted, the focus, etc

15:41:47 <m-relay> <o​frnxmr:monero.social> Other sponsorships they have, their current revenue etc

15:42:24 <m-relay> <p​lowsof:matrix.org> or Monero content from his wouldnt be out of the norm, anyway, we are
discussing Lovera

15:43:29 <nioc> monerbull I believe it was not merged because it had just been opened

15:43:47 <m-relay> <p​lowsof:matrix.org> its the same terms as was accepted the first time, his subscribers
have increased, i did not look at any other stats, the view count was not jaw dropping. however, the
informative videos are up there for eternity* for spanish speakers

15:44:35 <m-relay> <o​frnxmr:monero.social> I'm voting merge. Im ok with the cost

15:44:37 <m-relay> <m​onerobull:matrix.org> They are on odyssey too right

15:44:54 <m-relay> <o​frnxmr:monero.social> Lovera:

15:45:41 <MajesticBank> https://imgur.com/a/cIs4fs9

15:46:14 <m-relay> <p​lowsof:matrix.org> no laser eyes ??

15:46:36 <MajesticBank> I think more people are forced to watch ofcxmr psychiatric episodes

15:46:44 <MajesticBank> but it's small amount so merge ?

15:47:01 <m-relay> <o​frnxmr:monero.social> small and he has an actual following

15:47:09 <m-relay> <m​onerobull:matrix.org> No open mouth is good, Mr beast recently said if you have your
teeth not closed the video performs wirse

15:47:17 <m-relay> <m​onerobull:matrix.org> No open mouth is good, Mr beast recently said if you have your
teeth not closed the video performs worse

15:47:23 <MajesticBank> https://i.imgur.com/woqO3z9.png

15:47:32 <m-relay> <p​lowsof:matrix.org> i think a 'how did the 1st ccs go' round up of videos produced /
titles would be helpful?

15:48:23 <m-relay> <o​frnxmr:monero.social> Monerotopia tiktok twitter as well

15:48:44 <m-relay> <p​lowsof:matrix.org> its just the absurdly low hourly rate

15:48:52 <m-relay> <o​frnxmr:monero.social> He shoukd raise it to 100xmr

15:49:14 <MajesticBank> can we hop to the next ?

15:49:42 <m-relay> <o​frnxmr:monero.social> Well with lovera, i say merge

15:49:56 <m-relay> <o​frnxmr:monero.social> Cost more man hrs to debate it

15:50:37 <m-relay> <o​frnxmr:monero.social> But i also agree with plowsof about looking into interaction stats
of most popular videos or tiktoks of that time

15:51:02 <m-relay> <p​lowsof:matrix.org> the first ccs we got some stats from lovera, they would be nice to
see this time round again, i will leave it at that

15:51:24 <m-relay> <o​frnxmr:monero.social> Yea, a comparison chsrt would be great

15:51:40 <m-relay> <p​lowsof:matrix.org> ok lets move on

15:51:48 <m-relay> <p​lowsof:matrix.org> d. [Selfhosted tor gitea instance of monero
source](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/408)

15:51:59 <m-relay> <o​frnxmr:monero.social> This is like moneroarchiver, but paid mth to mth?

15:52:12 <m-relay> <o​frnxmr:monero.social> Instead of "run with the money after 2 weeks"

15:53:02 <m-relay> <p​lowsof:matrix.org> i feel my comment on the other proposal applies to this one:
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/361#note_19727

15:53:09 <m-relay> <m​onerobull:matrix.org> Isn't git decentralized by nature and a self hosted version
basically useless

15:53:59 <m-relay> <o​frnxmr:monero.social> Were already mirrored on wownero's instance i think (?)

15:54:11 <m-relay> <p​lowsof:matrix.org> for me this is a no. lets say monero is outlawed / deleted from
github ... ok who do we get the source from, plowsofs gitea instance on tor? ok we download that, what do we
do with it? ... probably ask other devs / core members who have local copies for hashes of commits?

15:54:32 <m-relay> <p​lowsof:matrix.org> in that case we dont need step 1

15:54:46 <m-relay> <o​frnxmr:monero.social> Yeah, i agree with plow. People can self host for free

15:54:56 <m-relay> <o​frnxmr:monero.social> I self host the blockchain for free..

15:54:57 <m-relay> <m​onerobull:matrix.org> I trust core more than some random guy who wants to get paid for
hosting a backup

15:55:08 <MajesticBank> skip for now

15:55:20 <m-relay> <o​frnxmr:monero.social> Close

15:55:26 <m-relay> <m​onerobull:matrix.org> I host bridgerton:  for free

15:55:39 <m-relay> <m​onerobull:matrix.org> And the chain

15:56:22 <m-relay> <m​onerobull:matrix.org> At one point i even hosted Bitcoin but only to put monerochan
ordinals on it

15:56:26 <MajesticBank> I almost forgot to mention we are adding p2p trade option to our existing swap
service, it's in beta and expected to be live in week

15:56:31 <MajesticBank> https://majesticbank.sc/p2p/1

15:56:51 <m-relay> <p​lowsof:matrix.org> i spent 12 hours @ 45eur setting my laptop so i can work in the woods
/s

15:56:51 <m-relay> <m​onerobull:matrix.org> That sounds cool

15:57:09 <m-relay> <p​lowsof:matrix.org> *consults the EmJay invoice*

15:57:50 <m-relay> <p​lowsof:matrix.org> interesting majesticbank

15:58:09 <m-relay> <m​onerobull:matrix.org> majetic do you take custody of the coins during the trade?

15:58:09 <m-relay> <p​lowsof:matrix.org> is this done using localmoneros api? or your own service?

15:58:42 <MajesticBank> it's fully in house solution

15:59:02 <MajesticBank> there will be also on/off ramp options

15:59:09 <m-relay> <p​lowsof:matrix.org> ok impressive, will keep an eye on that link, please keep us updated

16:00:21 <m-relay> <p​lowsof:matrix.org> on the hour, AOB?

16:00:43 <m-relay> <p​lowsof:matrix.org> i've been following rekt.news (CoinEX appeared there, who have xmr
holdings, be careful out there)

16:00:44 <m-relay> <m​onerobull:matrix.org> I just got around to watching this video which has been sitting in
my playlist for months https://www.youtube.com/watch?v=WP7v9HdUceY

16:01:07 <m-relay> <p​lowsof:matrix.org> thanks !

16:01:17 <m-relay> <m​onerobull:matrix.org> The part where they explain how monero works is pretty good if you
cut before they talk about how it's used by criminals lmao

16:01:39 <MajesticBank> what happened with farcaster team

16:02:18 <MajesticBank> there was presentation on the monerokon with mainnet and silence after

16:02:37 <m-relay> <p​lowsof:matrix.org> no activity from them for a while (did they approach the events team
to hold a presentation somewhere recently?)

16:04:13 <plowsof> farcaster released a WebUI for swaps during their last update, which worked (alot of
tweaks/bugs to be fixed when i tired) after that, not much

16:04:33 <m-relay> <o​frnxmr:monero.social> Basicswap had some updates too iirc

16:05:18 <m-relay> <m​onerobull:matrix.org> Monero trades

16:05:21 <m-relay> <m​onerobull:matrix.org> Both directions

16:05:36 <m-relay> <m​onerobull:matrix.org> Still not viable since you need all the nodes

16:05:49 <m-relay> <m​onerobull:matrix.org> But very cool

16:06:23 <plowsof> nice, thanks for sharing

16:06:43 <plowsof> i think we can leave it there, thank yo uall for attending and m-relay for your moderation
via DataHoarder

16:06:52 <nioc> ty plowsoft

16:07:03 <MajesticBank> thanks for moderation

16:07:12 <msvb-lab> Good meeting everyone, dankon.

16:07:22 <m-relay> <o​frnxmr:monero.social> Ty plowgpt

16:07:42 <m-relay> <p​lowsof:matrix.org> events meeting in 53 minutes right? #monero-events:monero.social

16:10:32 <msvb-lab> Yes, in 50 minutes on the #monero-events channel.

16:11:15 <m-relay> <s​needlewoods_xmr:matrix.org> is anything special planned for 10 year anniversary?

16:14:55 <nioc> curve trees  :D

16:24:30 <m-relay> <a​js_:matrix.org> monerokon meeting at 17:00 today: https://github.com/monero-
project/meta/issues/896

16:24:30 <m-relay> <a​js_:matrix.org> utc

16:24:30 <m-relay> <a​js_:matrix.org> in #monero-events

16:30:11 -xmr-pr- [meta] ajs-xmr opened issue #896:  MoneroKon 2024 Planning Meeting: Saturday 16th September
2023 @ 17:00...

16:30:11 -xmr-pr- > https://github.com/monero-project/meta/issues/896

17:00:48 <m-relay> <k​ayabanerve:matrix.org> luigi1111w: I'm fine with any expiration you want if its sane (at
least two weeks). As for underfunding, I'd say it should still be passed through (no reason not to IMO), but
I'm willing to say funded milestones get paid and partially funded milestones go to the general fund as
traditional if that greases the wheels.

17:01:32 <m-relay> <k​ayabanerve:matrix.org> :D

17:01:49 <nioc> 2 weeks would be a short time for a proposal of this size

17:03:15 <luigi1111w> expiration is like 1mo+. I don't think partially funded should go to gen fund, I'd just
like a plan for what happens if there is underfunding (preference or pro rata or something else)

17:05:06 <m-relay> <k​ayabanerve:matrix.org> monerobull @monerobull:matrix.org: I only hired jberman and
accepted the risk I'd go out of pocket on it. I want to be clear on the limited scope there given prior
comments.

17:05:58 <m-relay> <k​ayabanerve:matrix.org> nioc: Agreed. Hence so long as it's at least :p I was going to
suggest 1m.

17:06:07 <m-relay> <k​ayabanerve:matrix.org> Though I also heard 3m mentioned.

17:06:27 <m-relay> <k​ayabanerve:matrix.org> Sorry for missing the meeting. Time zones are off for me ://

17:06:32 <m-relay> <m​onerobull:matrix.org> look at monero. researchers paying out of their own pocket and
meanwhile unnecessary stuff gets funding

17:07:41 <nioc> 3 months is a long time and 1 month is minimum but luigi already knows this  :)

17:09:41 <nioc> without milestones it would be difficult to make a partial payment if it come to that

17:09:50 <m-relay> <m​onerobull:matrix.org> i previously stated im gone if we cant fund core research /
development since it means the project has failed

17:09:57 <nioc> *payments

17:13:07 <plowsof> Monerbull, its being merged, opinions on 'what to do if underfunded' - 'how long for it to
expire' pls, no need to reiterate threats!!

17:13:14 <plowsof> Monerobull

17:13:28 <m-relay> <m​onerobull:matrix.org> ok

17:14:32 <m-relay> <m​onerobull:matrix.org> id suggest first funding milestone somewhere around what kayaba
paid to others

17:14:54 <m-relay> <k​ayabanerve:matrix.org> nioc: There are milestones, just in the metadata which isn't in
the desc. Solely the patch

17:15:01 <m-relay> <k​ayabanerve:matrix.org> I meant to move those into the desc...

17:15:07 <m-relay> <o​frnxmr:monero.social> 3 months broski

17:15:47 <m-relay> <k​ayabanerve:matrix.org> I don't have exp here and am fine deferring to luigi

17:15:58 <plowsof> Luigi os fine deferring to you

17:16:09 <m-relay> <o​frnxmr:monero.social> ^

17:17:09 <plowsof> 1 month - 1.5 - 2 - 2.5 - 3

17:17:44 <m-relay> <k​ayabanerve:matrix.org> plowsof: I'm fine deferring to you

17:17:44 <m-relay> <k​ayabanerve:matrix.org> :p

17:18:04 <plowsof> If underfunded after x months - i accept the rediction in wages , thanks all for donating

17:18:04 <m-relay> <k​ayabanerve:matrix.org> 1, or if that seems short to people with exp, 2 months would be
more than fine by me.

17:18:23 <plowsof> Add those 2 things, thanks


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-09-11T08:13:27+00:00
- Closed at: 2023-09-25T11:29:25+00:00
