---
title: 'Monero Community Workgroup Meeting: Saturday 7th January 2023 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/775
author: plowsof
assignees: []
labels: []
created_at: '2023-01-01T17:39:14+00:00'
updated_at: '2023-01-08T06:03:41+00:00'
type: issue
status: closed
closed_at: '2023-01-08T06:03:41+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
        - [Featherwallet update](https://featherwallet.org/changelog/) - including [bootstrappable](http://bootstrappable.org/benefits.html) builds, Pi and arm64 support!
        - [Bitejo.com](https://bitejo.com/) redesign by anarkiocrypto!
        - [UnstoppableSwaps GUI](https://unstoppableswap.net/) Beta released (use at your own risk as its a beta)!
        - https://basicswapdex.com/ - DEX with btc -> monero atomic swaps / dockers / guis / docs you name it
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard)
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [xmr-btc-swap development and improvement](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/355)    
  b. [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/357)    
  c. [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358) [ ** Author hired by blockstream who will sponsor completion of paper **](https://libera.monerologs.net/monero-research-lab/20221231#c184185)
  d. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/366)    
  e. [Empower Lebanon(and similar hyperinflated countries) to use Monero instead of fiat(educational and bartering platform/guerilla marketing/workshops)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/367)    
  f. [koe seraphis library work 2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/369)    
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup   [MoneroKon 2023](https://github.com/MoneroKon/) [** Draft press release **](https://monerokon.prowly.com/221722-3rd-annual-international-monero-konferenco-on-security-privacy-and-decentralization-in-blockchain-technology) - $80 for a logo from fiver? maybe [gnuteardrops](https://monero.observer/gnuteardrops-reaches-monero-graphics-milestone-100-designs/) instead?
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
      - https://github.com/monero-project/research-lab/issues/109
      - https://github.com/monero-project/research-lab/issues/108
      
   h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)

7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-01-08T06:03:40+00:00
Logs 
```
16:00:14 <plowsof11> meeting time https://github.com/monero-project/meta/issues/775

16:00:15 <plowsof11> hii

16:00:23 <ofrnxmr[m]> Greetings

16:00:52 <plowsof11> lets shill some highlights before rucknium mentions magic

16:01:06 <plowsof11>         - [Featherwallet update](https://featherwallet.org/changelog/) - including
[bootstrappable](http://bootstrappable.org/benefits.html) builds, Pi and arm64 support!

16:01:08 <plowsof11> yuck formatting

16:01:35 <plowsof11> tobtoht great work with feather!

16:01:50 <MajesticBank> big progress on feather, very good

16:01:57 <Siren[m]> This is a draft webpage but we are working on a Monero ATM.
https://kernal.eu/~siren/monero-atm/

16:02:22 <plowsof11> [Bitejo.com](https://bitejo.com/) redesign by anarkiocrypto!

16:02:34 <ofrnxmr[m]> Id like to note that Monero Moon has posted 2 new newsletters

16:03:01 <plowsof11> nice work johnfoss68 !

16:03:30 <ofrnxmr[m]> What else happened over the holidays?

16:03:41 <plowsof11> [UnstoppableSwaps GUI](https://unstoppableswap.net/) Beta released (use at your own risk
as its a beta)! well done binarybaron GL with the beta!

16:03:48 <MajesticBank> yes, john is back and working over-time on monero things from what I've seen

16:03:54 <plowsof11> wishing everyone a healthy and a successful 2023 btw!

16:04:05 <ofrnxmr[m]> Trocador.app now has a payment mode.

16:04:06 <ofrnxmr[m]> Monerkon need a design gnuteardrops:  willing to pay

16:04:54 <MajesticBank> We might see atomic swaps usable very soon, with GUI should be much user friendly

16:04:56 <plowsof11> the monero atm project has a cool looking 3d model of an atm 😁

16:05:15 <plowsof11> we should also look at : https://basicswapdex.com/ - DEX with btc -> monero atomic swaps
/ dockers / guis / docs you name it

16:05:23 <Stnby[m]> plowsof11: I am 🇲🇳 12 animal 🐗 calendar believer, but lets hope for success regardless.

16:06:16 <plowsof11> i think Rucknium wants to mention MAGIC ~ voting has began for something or other

16:06:40 <Siren[m]> Mongolian MAGIC calendar

16:07:04 <monerobull[m]1> Hello

16:07:15 <plowsof11> @monerobull has used the basicswapdex + knows about magic

16:07:20 <ofrnxmr[m]> I dont mind celebrating twice

16:07:52 <monerobull[m]1> BasicSwapdex is really cool

16:08:16 <ofrnxmr[m]> Oh whoops. I forgot to apply

16:08:20 <ofrnxmr[m]> Next time, someone nominate me :P

16:08:37 <plowsof11> are we ready to jump in to the ccs ideas?

16:08:47 <monerobull[m]1> The swaps themselves are basically automatic, just everything regarding UX around it
is not great rn

16:09:16 <Rucknium[m]> If you are a MAGIC voter (you could have applied to be one recently), please vote on
the MAGIC Monero Fund committee candidates. You should have received an email about it.

16:09:24 <ofrnxmr[m]> Good morning monerobull @monerobull:matrix.org:

16:09:26 <ofrnxmr[m]> jozsef:  are you around to comment on the radio proposal

16:09:42 <plowsof11> that would be NotMtth

16:10:26 <plowsof11> lets discuss   a. [xmr-btc-swap development and
improvement](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/355)

16:10:27 <ofrnxmr[m]> monerobull[m]1: Personally, I think comit is a complete waste if resources.

16:10:29 <plowsof11> i am ready to vote

16:11:08 <MajesticBank> You can vote this year for me at magic monero fund, I think fund can enjoy some extra
help

16:11:12 <MajesticBank> and yes commit

16:11:19 <MajesticBank> not for approval I think at this point

16:11:42 <MajesticBank> I would delay it for two weeks or something

16:12:28 <monerobull[m]1> ofrnxmr[m]: Agreed.

16:12:57 <monerobull[m]1> BasicSwapDex and Farcaster seem to be way ahead already

16:13:16 <ofrnxmr[m]> But hey. Proposal was already merged.

16:13:16 <ofrnxmr[m]> MajesticBank @MajesticBank:libera.chat: I dont see any reason for comit backend /
unstoppableswap gui being used. Last time i checked there were was probably less than $10 in liquidity

16:13:33 <plowsof11> at this moment in time im saying close

16:14:07 <MajesticBank> There is a solution for that, I feel like we hadn't tested protocol enough to
disregard funding totally

16:14:14 <plowsof11> the proposer also had wrong xmr numbers the entire time (discovered only recently) and
overall rushed / not planned well

16:14:22 <MajesticBank> this proposal is nothing something I fancy still

16:14:31 <plowsof11> they have reduced their workload and doubled the hourly rates basically

16:14:59 <monerobull[m]1> Bait and switch?

16:15:32 <plowsof11> someone called delta1 i would prefer to make a ccs proposal (if aynone follows the
repo(s) they would see this person doing alot of things and was congratulated specifically by binarybaron when
releasing the beta for their work on the cli)

16:15:43 <plowsof11> but yeha, comit isnt cool atm

16:16:32 <ofrnxmr[m]> <plowsof11> "i am ready to vote..." <- Im trying to login so i can downvote

16:16:43 <plowsof11> there are open bounties totalling +4 xmr for the cli - leito should complete these to
show his worth before considering a ccs

16:17:24 <Rucknium[m]> Farcaster released something. Has anyone tried it?

16:17:34 <plowsof11> even then.. it would require a hail mary of commit becoming popular after atomic swap gui
final is released etc + liquidity and faracaster / basicswap dex 'not existing''

16:18:25 <ofrnxmr[m]> There are 7 upvotes and no down

16:18:31 <ofrnxmr[m]> In confused, so going to downvote rn

16:18:58 <MajesticBank> makes sense that someone that spent more time with project draft ccs

16:19:20 <MajesticBank> in future if it's worth it

16:19:36 <monerobull[m]1> Well let's pull that argument again: sockpuppets 🧦

16:19:53 <plowsof11> radio time?

16:20:25 <leito[m]> sorry I'm late

16:20:37 <ofrnxmr[m]> Lovera @btclovera:matrix.org:  you upvoted

16:20:46 <plowsof11> hello

16:21:22 <plowsof11> there will also be a meeting on the 14th if a fuller picture is required

16:21:33 <ofrnxmr[m]> My vote is close it, but others such as lovera have upvoted.

16:21:33 <ofrnxmr[m]> On a fundamental basis, comit is dead, is it not

16:21:34 <Rucknium[m]> I am neutral to negative on this proposal.

16:21:46 <plowsof11> reg radio or ?

16:22:02 <leito[m]> the thing also is that some of the milestones that I set have also a bounty from baro

16:22:10 <leito[m]> s/baro/baron/

16:22:24 <plowsof11> get to work then and prove yourself

16:22:27 <plowsof11> delta1 > leito

16:22:30 <plowsof11> show me im wrong

16:22:38 <leito[m]> delta1 has been awesome that is clear

16:22:45 <plowsof11> fake xmr numbers / rushed proposal /

16:22:50 <ofrnxmr[m]> Where is the proposer

16:23:01 <leito[m]> ofrnxmr[m]: I'm here

16:23:14 <leito[m]> plowsof11: I would say more like baddly made than fake

16:23:20 <ofrnxmr[m]> Hey leito, why would we fund comit stuff

16:23:23 <leito[m]> but I do agree that could have been better then

16:23:29 <ofrnxmr[m]> At a'l

16:23:34 <ofrnxmr[m]> All*

16:24:13 <ofrnxmr[m]> Atomic swaps is a nice buzzword, but comit (RIP) is terrible

16:24:57 <leito[m]> ofrnxmr[m]: it's the only project right now that is working and competition in general
from the community is good

16:25:39 <monerobull[m]1> leito[m]: Wrong

16:25:39 <ofrnxmr[m]> Competition is basicswap

16:25:40 <monerobull[m]1> BasicSwapdex works way better already

16:25:43 <MajesticBank> next proposal?

16:25:51 <plowsof11> yes lets move on

16:25:59 <plowsof11> [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/357)

16:26:19 <plowsof11> they have posted an update / example finally at least

16:26:46 <plowsof11> cypherpunkradio.com

16:26:48 <ofrnxmr[m]> I still personally think radio is a hobby

16:26:48 <ofrnxmr[m]> Im neutral to negative

16:27:09 <monerobull[m]1> If we get decent documentation to host all of it yourself I'd be positive

16:27:38 <Rucknium[m]> One thing this proposal has in its favor is that it's cheap: 5 XMR

16:27:43 <plowsof11> the asking amount is low, and they seem to be a close knit community contributing to
monero

16:27:52 <MajesticBank> not possible to listen over website directly?

16:28:00 <plowsof11> the 5xmr would be reduced if/when they accout for current xmr prices

16:28:11 <monerobull[m]1> MajesticBank: Apparently not

16:28:24 <ofrnxmr[m]> Monero archive taught me to remember that a scam is a scam

16:28:25 <ofrnxmr[m]> 1xmr and still ran away

16:28:38 <monerobull[m]1> Not only that, mokazino too

16:28:38 <plowsof11> no cant listen on the site xD

16:28:53 <monerobull[m]1> monerobull[m]1: We got code for that but i have no idea how to deploy it

16:29:21 <monerobull[m]1> So that's why I want solid documentation for this

16:29:46 <plowsof11> the problem is the comunity has sponsored xmr.radio once, it ended up dead, then ajs
revived it again

16:30:23 <plowsof11> but again, cypherpunk radio aims to be more than "just radio"

16:30:38 <plowsof11> assurance of solid docs noted

16:30:47 <monerobull[m]1> Also, who listens to radio these days. Even if it reads out observer articles and
reddit posts

16:31:05 <ofrnxmr[m]> plowsof11: Sounds like something ill never listen to

16:31:18 <ofrnxmr[m]> These days, everything is on demand

16:31:21 <monerobull[m]1> Id rather have an RSS feed and a YouTube playlist

16:31:21 <plowsof11> i listed to yewtu . be videos

16:31:22 <plowsof11> listen*

16:31:29 <Rucknium[m]> Monero Observer came after Monero Moon. And MO turned out to be much better. But yes I
also worry that radio may not have much of a market

16:31:54 <ofrnxmr[m]> And I2p radio even less

16:31:57 <plowsof11> xmrradio had ccs money pumped into AND a full page of wishlist items funded

16:32:22 <plowsof11> average listeners topped 20? less?

16:32:22 <Rucknium[m]> It's not i2p-only, is it?

16:32:28 <plowsof11> now yes

16:32:39 <plowsof11> but even when it was clearnet + live streaming site

16:32:46 <monerobull[m]1> It's a fun idea but if we are being realistic, it's a total waste of funds

16:32:54 <ofrnxmr[m]> plowsof11: Id imagine 5 of those were themselves

16:33:03 <plowsof11> 1 was me ;_;

16:33:20 <ofrnxmr[m]> Was? WAS?!

16:33:32 <plowsof11> it was a phase i went through !

16:33:37 <monerobull[m]1> Yeah aren't you jacked into the i2p radio rn?

16:33:52 <ofrnxmr[m]> Radio, and newsletters, are "go get em" jobs

16:34:15 <plowsof11> they can act on this and we can have a vote on the 14th?

16:34:16 <ofrnxmr[m]> And have potential to be massively profitable

16:34:25 <ofrnxmr[m]> Just ask Alex Jones or Joe Rogan

16:34:31 <MajesticBank> yes, let's give them some extra time

16:34:39 <plowsof11> holidays and such

16:34:48 <monerobull[m]1> There's not much to act on, the reality is, the viewership will be tiny to none :/

16:34:59 <ajs_[m]> top was about 30

16:35:02 <ofrnxmr[m]> Right

16:35:09 <Rucknium[m]> I also think that they could get sponsors to run ads. The target audience is very clear

16:35:09 <ajs_[m]> now, about 5-10

16:35:19 <ofrnxmr[m]> ^ this is very clear but its so much easier to ask ccs

16:35:22 <ajs_[m]> streaming over i2p and tor

16:35:25 <ofrnxmr[m]> ALSO, they are sponsored

16:35:32 <monerobull[m]1> Lol what

16:35:43 <ajs_[m]> and only creative commons music

16:35:44 <ofrnxmr[m]> By cake iirc plowsof @plowsof:matrix.org:

16:35:53 <plowsof11> you mean lovera now?

16:36:01 <ofrnxmr[m]> I mean ntmth

16:36:39 <ofrnxmr[m]> Or am I wrong and they are not sponsored by cake?

16:36:47 <plowsof11> i didnt know that ? btw bulletproof ++ author was hired by blockstream to (among other
things complete the rest of their paper ) so thats nice / hopeful it will be available in a month(s) .. i hope

16:36:57 <plowsof11> i dont think theyre sponsored by cake

16:37:08 <ofrnxmr[m]> Excuse me 🙏 im probably mixing up with someone else

16:37:09 <plowsof11> right...

16:37:14 <plowsof11>   d. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/366)

16:37:29 <plowsof11> i asked about the cake sponsorship , however ,

16:37:48 <plowsof11> i am told that revealing such information is tricky

16:37:50 <ofrnxmr[m]> Lovera on the other hand, is,  and doesnt need us

16:38:03 <ofrnxmr[m]> Had a large viewershio across multiple playfortms

16:38:10 <ofrnxmr[m]> Including 20k+ on tiktok

16:38:19 <ofrnxmr[m]> Subscribers*

16:38:38 <plowsof11> lovera has 5 videos per month sponsored by cake wallet, the problem is - how much is that
earning? more than what we have to pay? less? does it matter if we dont get any more videos?

16:38:52 <plowsof11> i dont think we can be told how much cake sponsors them

16:38:55 <ofrnxmr[m]> plowsof11: Thats nice

16:39:04 <ofrnxmr[m]> plowsof11: We can

16:39:17 <ofrnxmr[m]> Them and cake dont want to disclose, we dont fund them.

16:39:28 <ofrnxmr[m]> They made that decision when they accepted under the table funding

16:39:32 <plowsof11> is this a deal breaker for anyone else

16:39:37 <monerobull[m]1> Yeah wtf

16:39:56 <MajesticBank> Not sure we can demand such info, but not sure this is suitable ccs

16:40:08 <ofrnxmr[m]> We cant DEMAND anything

16:40:24 <monerobull[m]1> *can

16:40:26 <ofrnxmr[m]> But were not obligiated to put food on their table if they dont want to offer up all the
infos

16:40:35 <plowsof11> loveras outreach is great, and they make informative videos too

16:40:37 <ofrnxmr[m]> Simple as that.

16:40:46 <MajesticBank> last time we had problem with video content because it was not possible to audit it's
work

16:40:51 <ofrnxmr[m]> Either tell me how youre screwing me, or go screw yourself

16:40:56 <MajesticBank> views, sharing

16:41:13 <MajesticBank> ccs work must be verifiable somehow

16:41:15 <ofrnxmr[m]> YouTube etc shows all of those metrics

16:41:28 <ofrnxmr[m]> Lovers was happy to say he doesnt make much off of the videos and show the YouTube
income

16:41:34 <plowsof11> lovera did disclose his youtube earnings <1$ xD

16:41:37 <ofrnxmr[m]> But wont show the cheque he gets from cake

16:41:45 <Rucknium[m]> In 2021 Monerotopia/MoneroTalk CCS was approved even though Cake sponsors them. That
was in 2021 however

16:42:03 <ofrnxmr[m]> That was before I was ready to stomp out fires

16:42:14 <monerobull[m]1> I can tell you guys that I've placed about 20 stickers in high foot traffic areas
this week, do i get my 1 xmr now plz

16:42:14 <plowsof11> this time cake wasnt mentioned in the proposal and i had to ask in the comments

16:42:49 <ofrnxmr[m]> What about sgp's yacht fund

16:42:49 <monerobull[m]1> monerobull[m]1: Someone has to pay for my drive to Italy to place them there

16:43:02 <plowsof11> only 1xmr? make a ccs - we have to pay 5xmr

16:43:25 <ofrnxmr[m]> We can get a yacht and private jet, and YouTube shorts and outreach like top g

16:43:26 <monerobull[m]1> Now that you mention it, car depreciation should be considered as well

16:43:48 <plowsof11> ok so disclosing the sponsorship is a big deal / mixed feelings

16:44:03 <ofrnxmr[m]> Cmon. Someone pay for my retirement

16:44:08 <ofrnxmr[m]> sgp:

16:44:22 <monerobull[m]1> ofrnxmr[m]: Nah influencers rent fake yet photo sets. They need to actually act
financially sound

16:44:28 <ofrnxmr[m]> monerobull[m]1: Need extra funding right after leaving the lotn

16:44:39 <monerobull[m]1> * Nah influencers rent fake jet photo sets. They need to actually act financially
sound

16:45:01 <ofrnxmr[m]> plowsof11: Its always a huge deal

16:45:03 <ofrnxmr[m]> This is business

16:45:10 <ofrnxmr[m]> You dont get to triple and quadruple dip

16:45:11 <plowsof11> ok lovera should act on this for the 14th

16:45:24 <MajesticBank> yeah, let's wait on this one

16:45:33 <plowsof11> we did tel johnfoss to be sustainable - and now we have someone who is sustainable but
wants a ccs

16:45:37 <ofrnxmr[m]> Go around telling every family member you need $500, then they talk to one another and
find out they gave you 20k a'toherther

16:45:51 <plowsof11> ok lets move on to the next

16:45:54 <plowsof11>   e. [Empower Lebanon(and similar hyperinflated countries) to use Monero instead of
fiat(educational and bartering platform/guerilla marketing/workshops)](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/367)

16:46:08 <ofrnxmr[m]> plowsof11: Be sustainable doesnt mean ask for donations. It means be sustainable

16:46:09 <ofrnxmr[m]> Aka, dont ask

16:46:10 <monerobull[m]1> Ok enough trashtalk

16:46:22 <Rucknium[m]> IMHO, wwe shouldn't punish "success" exactly. But usually CCSes are funded at a level
that the competitive market would fund something. So we would need to know total revenue before CCS to see if
it's reasonable.

16:46:22 <monerobull[m]1> Oh that proposal, continue 😂

16:46:23 <plowsof11> i am ready to vote , but the proposer wants to change it and 'work on bitejo ' suddenly

16:46:46 <ofrnxmr[m]> Rucknium:  thank you for the translation

16:47:20 <plowsof11> ive seen 2 images of stickers

16:47:37 <ofrnxmr[m]> Close

16:47:51 <plowsof11> i also say close on this one

16:48:22 <plowsof11> the proposer is going to market monero to the masses (look at how the proposal looks)

16:48:22 <monerobull[m]1> Someone subsidized a package this week, he can order that for like 10$ and get ~680
stickers. It doesn't take freaking 500$

16:49:45 <monerobull[m]1> Isn't this just Afghanistan 2.0 but spirobel actually built a functioning website
now

16:49:46 <plowsof11> does this scream developer / marketing wizard

16:49:52 <ofrnxmr[m]> Likes their own proposal as well

16:49:56 <ofrnxmr[m]> Close it

16:50:18 <plowsof11> spirobel yes, not only a website but has attended conferences

16:50:21 <ofrnxmr[m]> It screams nsfw response from ofrnxmr

16:50:31 <plowsof11> and appeared on youtube channels discussing (among other things) monero

16:50:40 <monerobull[m]1> One jillion dollars

16:51:09 <ofrnxmr[m]> Spirobel doesnt need to be mentioned here

16:51:26 <monerobull[m]1> If he does a spirobel style redemption arc we can discuss it again but as it stands
it's not something we should consider at all

16:51:47 <ofrnxmr[m]> This ccs is a completely different approach, seemingly a lower goal and a more childish
layout

16:51:56 <ofrnxmr[m]> Spirobel's was simply naive and 100% impossible

16:52:08 <plowsof11> use of markdown is advantageous

16:52:14 <monerobull[m]1> ofrnxmr[m]: Have quite similar goals and spirobel is an example on how to do it
right

16:52:27 <monerobull[m]1> * The proposals have quite similar goals and spirobel is an example on how to do it
right

16:52:36 <ofrnxmr[m]> This one is something you bring to like.. wownero

16:53:08 <plowsof11> we need visionaries ! 😁

16:53:32 <nioc> I have visions

16:53:39 <plowsof11> hi

16:53:54 <plowsof11> lets move on

16:53:58 <plowsof11>   f. [koe seraphis library work 2](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/369)

16:54:04 <monerobull[m]1> My vision is monerochan body pillows, can I get a ccs or do i have to save up my
allowance money again

16:54:20 <monerobull[m]1> > <@plowsof:matrix.org>   f. [koe seraphis library work
2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/369)

16:54:20 <monerobull[m]1> >

16:54:20 <monerobull[m]1> Fund, no question

16:54:47 <monerobull[m]1> * money again /s

16:55:33 <ofrnxmr[m]> Move to funding

16:55:52 <monerobull[m]1> Ok great meeting, see ya

16:55:53 <plowsof11> nice, yes.

16:56:01 <Rucknium[m]> I asked koe if he would consider reversing the order of the tasks to have the paper
edits be done first, but in #no-wallet-left-behind:monero.social  he said no. Anyway, I support as-is

16:56:32 <ofrnxmr[m]> At least he didnt lie to ya

16:57:09 <Rucknium[m]> So people know: The status of Seraphis is like a building that has had its skeleton
laid. Now jberman, dangerousFreedom, and rbrunner are putting in the electrical wiring, etc

16:57:21 <plowsof11> lets quickly touch on some work groups - MRL ~ Ruckniums recent work on p2pool provided
some tangible numbers of 'chain bloat' and such to push along the creation of 2 new issues

16:57:54 <ofrnxmr[m]> New issues were old issues fwiw

16:57:54 <Rucknium[m]> But the structural engineers have not done the calculations to make sure the loads are
safe. No one can occupy the building (Seraphis can't go to mainnet) without those calculations

16:57:57 <plowsof11> indeed, old issues but without Ruckniums recent work,  they would not have gained support
right now

16:58:03 <Rucknium[m]> And we would have to tear down part of the building if there are problems found with
the current structure

16:58:25 <ofrnxmr[m]> Thanks ruck for putting numbers out there

16:58:39 <plowsof11> https://github.com/monero-project/research-lab/issues/109 and https://github.com/monero-
project/research-lab/issues/108

16:58:41 <ofrnxmr[m]> Monerobull knows what I had to say about it 😃

16:58:56 <ofrnxmr[m]> P2pool and chain bloat etc

16:59:06 <Rucknium[m]> Yes, people had talked about this for six months or more. I decided to finally run the
numbers and they were higher than some people expected.

16:59:21 <monerobull[m]1> ofrnxmr[m]: I am forgetful sorry 😂

17:00:04 <plowsof11> also moneroevents - 80$ for a logo from fiver when we have gnuteardrops
https://monero.observer/gnuteardrops-reaches-monero-graphics-milestone-100-designs/

17:00:20 <nioc> Rucknium[m]: thx, not higher than some people expected  :)

17:00:24 <ofrnxmr[m]> I stopped pushing p2pool once I noticed the increase in bad decoys and high fees and tx
weight for consolidations

17:00:25 <Rucknium[m]> Now you can run the numbers yourself: https://github.com/Rucknium/misc-
research/tree/main/Monero-p2pool-Output-Stats

17:00:32 <monerobull[m]1> plowsof11: I believe we haven't heard from them yet

17:00:58 <plowsof11> they shold know the community appreciates their work and efforts

17:01:05 <ofrnxmr[m]> One thing nobody has mentioned, js the increase tx size from considations significantly
reduces the # if tx per block without bumping your fee rate

17:01:54 <Rucknium[m]> plowsof11: People (especially miners) should comment/emoji those issues. Development
isn't decentralized unless more people give input.

17:01:54 <ofrnxmr[m]> Its possible for p2pool miners to accumulate outputs for a long period of time, then
flood the network with huge tx as they consolidate

17:01:54 <plowsof11> btw the monero atm page is actually a funding page. they want to raise 7xmr and are 25~%
of the way already https://kernal.eu/~siren/monero-atm/

17:02:25 <ofrnxmr[m]> Nice

17:02:56 <plowsof11> AOB

17:03:19 <plowsof11> there will be an events meeting on the 14th too

17:05:16 <plowsof11> thank you all for joining , hope to see you next week on the 14th then back to every
other week

17:05:19 <msvb-lab> Thanks for the good meeting and grep moderation plowsof11.

17:06:20 <plowsof11> thank you msvb-lab!

17:07:26 <nioc> another meeting on the 14th?

17:07:34 <nioc> \o/ I <3 meetings

17:07:51 <plowsof11> im emotionally attached and need another asap


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-01-01T17:39:14+00:00
- Closed at: 2023-01-08T06:03:41+00:00
