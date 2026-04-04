---
title: 'Monero Community Workgroup Meeting: Saturday 25th February 2023 @ 16:00 UTC '
source_url: https://github.com/monero-project/meta/issues/798
author: plowsof
assignees: []
labels: []
created_at: '2023-02-15T23:03:51+00:00'
updated_at: '2023-03-02T22:45:40+00:00'
type: issue
status: closed
closed_at: '2023-03-02T22:45:40+00:00'
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
- [tx_extra discussion in MRL meeting](https://github.com/monero-project/meta/issues/797)
- [Monero Meet 2023-02-14](https://www.yewtu.be/watch?v=j5K5aUbrJ24) 
- New monero cli/gui release [soon](https://libera.monerologs.net/monero-dev/20230215#c206343)
- [FeatherWallet 2.4.1 released](https://featherwallet.org/changelog/)
- [Nerostr ~ Monero meets Nostr](https://www.reddit.com/r/Monero/comments/1138nlj/nerostr_monero_meets_nostr/) pluja of kycnot.me
- [MoneroTalk](https://yewtu.be/channel/UC3Hx81QYLoEQkm3vyl4N4eQ) - sech1 interview
- [MoneroMagazine](https://yewtu.be/channel/UCRYrAjnE8FAgYeatsvhoalQ) - hyc interview 
- MoneoKon tickets for sale @ https://tickets.monerokon.com/ (XMR and other payment options) (credit to [Digilol](https://www.digilol.net/))
- Monero ATM early development 100% funded! https://atm.monero.is/
- Cake Pay extra UK merchants / [Desktop release](https://cakelabs.com/news/cake-wallet-arrives-on-desktop/)
- A user complained about monero.social matrix server displaying a users online status / i told them it was not possible/offtopic (because it does not effect matrix.org accounts) - ofrnxmr had a look and reported it to the matrix admins - disabled now
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  c. [Draft: Standalone AcceptXMR](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/374)    
  d. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/375)    

Delayed:
  a. [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358)    

6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
- Monero is going to the Oscars

  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup: Add trocador to getmonero https://github.com/monero-project/monero-site/pull/2045#issuecomment-1287162142    
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
    - Discuss bridges
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-02-26T19:09:54+00:00
Logs 
```
16:00:10 <plowsof11> meeting time https://github.com/monero-project/meta/issues/798

16:00:36 <plowsof11> Greetings. hello all

16:00:37 <ofrnxmr[m]> Greetings

16:00:41 <BusyBoredom[m]> Hi

16:00:46 <pluja[m]> Hey all

16:01:19 <jwinterm> o/

16:01:20 <ajs_[m]> Hi

16:01:22 <dsc_> hi

16:01:27 <Rucknium[m]> Hi

16:01:46 <plowsof11> hey pluja, you're one of the listed recent community highlights

16:02:09 <plowsof11> lets talk about some things that happened and such, like - [Nerostr ~ Monero meets
Nostr](https://www.reddit.com/r/Monero/comments/1138nlj/nerostr_monero_meets_nostr/) pluja of kycnot.me

16:02:25 <MajesticBank> hi

16:02:51 <plowsof11> monerobull set up https://monero.house/ (does anyone know what the fediverse is?)

16:03:35 <pluja[m]> How does the Monero community and devs feel about nostr? Should we keep on doing things
there? Most of the activity there is bitcoin-only

16:04:29 <plowsof11> im totally behind on all this tech ^ but it vaguely seems like "blockchain" tech? 'nodes'
can relay messages based on certain criteria?

16:04:41 <ofrnxmr[m]> sgp: monerobull @monerobull:matrix.org:

16:04:41 <blankpage[m]> Hi

16:04:47 <monerobull[m]> Hello

16:04:52 <sgp[m]> Hello

16:05:27 <pluja[m]> Yeah, kind of. Relays are pretty dumb, they just store and serve events. Clients do all
the hard work. Events pretty extensible, almost anything can be built with nostr.

16:06:25 <ofrnxmr[m]> I dont know anything about nostr, unable to comment 👍

16:06:31 <plowsof11> Rucknium has set up a pleroma (?) instance some time ago. its nice that we've got people
interested in this area, i doubt ill ever get it

16:06:33 <Rucknium[m]> I just set myself up on a self-hosted Pleroma (fediverse) instance two months ago.
There is useful info for me in the fediverse and I don't plan to switch to get N+1 social media.

16:06:56 <plowsof11> plujas monero integration into the whole thing is awesome

16:07:02 <blankpage[m]> I haven't actually tried nostr but btc people all seem to be jumping on board.
Building an XMR community there can't hurt.

16:07:07 <monerobull[m]> I've set up monero.house

16:07:16 <pluja[m]> https://usenostr.org/

16:07:16 <pluja[m]> Here's a basic guide to understand what it is about, if you want to read something about
it

16:07:21 <plowsof11> thanks!

16:08:27 <ofrnxmr[m]> New Wallet Releases

16:08:31 <plowsof11> do we have any speakers who want to give a talk at monerokon in this area? call for
presentations are on-going 😮 tickets are available also @ https://tickets.monerokon.com/ (XMR and other
payment options) (credit to [Digilol](https://www.digilol.net/))

16:09:11 <Rucknium[m]> pokkst has a multi-user Pleroma instance at xmrposter.club

16:09:35 <plowsof11> i wonder if Cake pay will add or have already? merchant in prague (where monerokon is
taking place) like they did for UK users recently (i can now larp as an agorist because im able to buy normal
food items with monero)

16:10:40 <ofrnxmr[m]> Speaking of Cake, they released a new Desktop app today for Mac (to start)

16:10:43 <hbs[m]> nostr is still very early in terms of security, there are very few options to not share your
private key with the service you use

16:10:44 <plowsof11> ofrnxmr[m]: - [FeatherWallet 2.4.1 released](https://featherwallet.org/changelog/) , but
everyone is waiting for luigi to merge/tag the gui !

16:10:44 <pluja[m]> You can always use extensions that act like signers

16:11:42 <pluja[m]> pluja[m]: For example https://github.com/fiatjaf/nos2x

16:12:33 <plowsof11> - [MoneroTalk](https://yewtu.be/channel/UC3Hx81QYLoEQkm3vyl4N4eQ) - sech1 interview

16:12:34 <plowsof11> - [MoneroMagazine](https://yewtu.be/channel/UCRYrAjnE8FAgYeatsvhoalQ) - hyc interview 👍️
recent interviews^ topics included p2pool and what are the odds of  ablock hash being hyc15th3s3x1estm4nal1ve

16:14:06 <plowsof11> Stnby Siren of Digilol have also had their FOSS ATM pre-dev project fully funded
https://atm.monero.is/ can follow how its going in #atm:kernal.eu (matrix only i think)

16:14:55 <hbs[m]> pluja[m]: yes, but on mobile it's still a pita, have to use kiwi

16:15:05 <plowsof11> also ehm, i was an ass to someone that complained about "online/offline" status being
public on monero.social (i tohught it was none sense) ofrnxmr had a look and reported it to the matrix admins
- disabled now

16:15:13 <Lovera[m]> Hi everyone

16:15:34 <Rucknium[m]> Mostly accurate Twitter thread on the origins of OSPEAD (the CCS proposal):
https://twitter.com/AnonShopApp/status/1628817742395756544

16:16:00 <plowsof11> the plot of a movie featuring Monero imo^

16:16:13 <ofrnxmr[m]> A good movie*

16:16:44 <plowsof11> fluffy escaping from alkatraz would be a good addition

16:17:06 <ofrnxmr[m]> Anyway, speaking of Feather Wallet , it should ve noted that Feather opened a ccs in
Feb15 and at an impromptu meeting we merged it.

16:17:26 <ofrnxmr[m]> It has been fully funded and moved to WIP 🔥

16:18:31 <plowsof11> valldrac (molly .im developer) has added transaction scanning (since the last update) to
his monero wallet sdk (and will provide a new update/demo soon) 👍️

16:18:33 <plowsof11> https://github.com/mollyim/monero-wallet-sdk

16:19:21 <ofrnxmr[m]> Regarding Molly: AJS and NYM were talking about paying to develop a monero chat app

16:20:01 <plowsof11> ive requested an honest update form them - im aware theyve put in 500+ hours of work
because wallet2 was too troublesome to work with so they had to make their own sdk :(

16:20:02 <bett3r[m]> ofrnxmr[m]: How many people user feather?

16:20:26 <ofrnxmr[m]> Feather doesnt collect ideate statistics

16:20:26 <pluja[m]> ofrnxmr[m]: From the ground up? Or based on any other chat app / platform?

16:20:42 <plowsof11> feathers ccs proposals get funded quite quickly - and i see feather support users popping
up more and more

16:20:47 <ofrnxmr[m]> But if you use monero, youve benefit from tobtoht's work

16:21:04 <ofrnxmr[m]> The feather ccs includes work on monero, gui etc as well

16:21:32 <bett3r[m]> Right, ok.

16:21:33 <plowsof11> true, some patches to feather end up in monero-core

16:21:38 <jwinterm> feather was recommended strongly by Alex at localmonero the other day

16:21:48 <dsc_> whats feather?

16:21:58 <jwinterm> wowlet fork I think

16:22:01 <pluja[m]> A monero wallet, featherwallet.org

16:22:02 <ofrnxmr[m]> Isnt feather the bases of wowlet?

16:22:08 <ofrnxmr[m]> Or the other way around?

16:22:08 <dsc_> ah I see

16:22:16 <dsc_> cool!

16:22:16 <plowsof11> dsc created feather wallet initialy , must not forget (wownero dev)

16:22:41 <ofrnxmr[m]> Yea, DSC messing with my head right now

16:22:47 <plowsof11> the lead architecht and head developer / creator of wownero from inception aka jwinterm

16:22:56 <plowsof11> mladies and gentleman

16:22:59 <dsc_> i am trying to be a valuable member of this discussion but my brain tends to go into trolling
mode

16:23:06 <dsc_> please continue :P

16:23:47 <Rucknium[m]> There is a Feather fork that works with Townforge :)

16:23:48 <plowsof11> i put respec on dsc name

16:23:57 <plowsof11> i also used dsc's pyton levin protocol recently

16:24:02 <MajesticBank> great work from tobtoht and dsc

16:24:16 <plowsof11> https://github.com/plowsof/check-monero-seed-nodes thanks dsc!

16:24:34 <dsc_> oh nice one :)

16:24:56 <plowsof11> happy face good mad face bad

16:25:43 <dsc_> thotbot was at my place for 2 weeks working on feathers new build system

16:25:55 <dsc_> i can tell you it was very annoying work for him

16:26:04 <plowsof11> just a reminder , the tx_extra discussion in MRL is still ongoing - they have meetings
every wednesday at 17:00 UTC (iirc)

16:26:12 <dsc_> .bbl

16:26:18 <ofrnxmr[m]> dsc_:  I hope you guys are well fed

16:26:32 <plowsof11> (i thought you where going to say it was very annoying having him there) lol thanks for
helping

16:26:39 <ofrnxmr[m]> Those long hours'll kill ya

16:27:23 <MajesticBank> dsc made wow in elite and stack

16:27:36 <ofrnxmr[m]> And cake

16:27:37 <plowsof11> now then, any other highlights before we talk aobut some ccs idea* (isthmus has been
radio silent on his proposal)

16:27:47 <plowsof11> i did not know that, wow

16:28:19 <ofrnxmr[m]> Regarding the Online Status for monero.social - I think that js the reason 24/25 would
DM us

16:28:31 <jwinterm> plowsof11: local monero / agora desk did AMA on r/cryptocurrency and is currently renting
the banner https://www.reddit.com/r/CryptoCurrency/comments/119zfxn/ama_im_alex_cofounder_at_localmonero_and/

16:28:35 <jwinterm> if that counts as highlights

16:28:55 <plowsof11> people on matrix .org where never shown to be online/offline, im sorry that 24/25
targetted social users like this

16:29:00 <MajesticBank> localmonero spread great picture about the monero project on AMA / banner ads

16:29:05 <plowsof11> definitely !

16:29:26 <plowsof11> nice work Alex

16:29:27 <sgp[m]> <plowsof11> "https://github.com/plowsof/check..." <- really cool! You can use Cake's onion
node there too if you want

16:30:32 <ofrnxmr[m]> Iirc there is a new monero sweden Facebook page

16:30:33 <plowsof11> im too busy buying bread cheese and milk with monero atm with cake pay

16:31:06 <ofrnxmr[m]> Facebook page by fredrikk:

16:31:16 <plowsof11> i think sech was talking to the owner here about it (they see stickers around sweden but
not many people 'know' about crypto/monero iirc)

16:32:06 <Rucknium[m]> sech had a good MoneroTalk episode recently

16:32:46 <plowsof11> yep, linked in notes (hyc's was also great @ monero magazine)

16:32:54 <ofrnxmr[m]> https://invidious.snopyta.org/watch?v=Y0C3dQnAFnE&local=true

16:33:26 <bett3r[m]> It is very important how things are explained to people. I think that one of the most
important points that should be explained to people is how communities can self-organize around XMR as a
funding/payment system.

16:33:44 <bett3r[m]> (where contributors can stay anonymous)

16:34:31 <plowsof11> monero newsletters to stay up to date with goings on : News: [Monero
Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero
Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)

16:34:43 <bett3r[m]> * funding/payment system. I mention it specifically (and possibly as a digression
depending on the topic of this discussion) for the reason that I've noticed mostly payments, services being
targeted on.

16:35:04 <ofrnxmr[m]> Please subscribe and donate to newletters when you can!

16:35:04 <bett3r[m]> * funding/payment system. I mention it specifically (and possibly as a digression
depending on the topic of this discussion) for the reason that I've noticed mostly payments, services being
focused on.

16:35:04 <plowsof11> i think we can move on to the ccs ideas, i see BusyBoredom is here

16:35:37 <plowsof11>   c. [Standalone AcceptXMR](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/374)

16:36:19 <ofrnxmr[m]> Some of the most thankless work im the community is done by those who are keeping their
eyes open for us.

16:36:35 <plowsof11> a quick back story: the xmrsale proposal was voted as being abandonned / closed 2
meetings earlier. and has 30 xmr left over. the above proposal is a suggestion to make better use of the funds

16:36:53 <ofrnxmr[m]> Regarding acceptxmr - I read the proposal and its blank! It just says "pay busyboredom
to acceptxmr"

16:36:53 <ofrnxmr[m]>  Did nobody read the ccs?

16:37:17 <jwinterm> :D

16:37:33 <plowsof11> :D

16:37:33 * jwinterm did not read the ccs

16:38:08 <plowsof11> i have read the proposal from top to bottom (out of fear/ paranoia)

16:38:32 <plowsof11> if merged it would go directly to the work in progress list

16:38:37 <Rucknium[m]> xmrsale dev should be notified by email and the CCS comment system.

16:39:00 <ofrnxmr[m]> (I am joking btw :D) the proposal is real.

16:40:01 <plowsof11> if anyone wants to merge / abstain / suggest another use of funds / please make it known
. busyboredom is also here to answer any questions

16:41:50 <ofrnxmr[m]> +1 on merge. Saves us from fully funding a new proposal. Similar product to the original
ccs

16:42:25 <ofrnxmr[m]> Perhaps though, as someone said, donations are a vote of the community

16:42:40 <Rucknium[m]> +1 on merge

16:44:02 <ofrnxmr[m]> As rough compromise (if donations are wanted to guage community sentiment) would be to
fund 2/3 milestones with xmrsale, and leave the maintenance milestone for funding by community

16:44:10 <ofrnxmr[m]> But left or right, I dont care. Both sound good to me

16:45:11 <ofrnxmr[m]> I don't remember who commented about community sentiment, I only remember someone had
brought it up

16:45:31 <Rucknium[m]> I think it was me

16:45:31 <plowsof11> interesting ideas

16:46:17 <Rucknium[m]> I just wanted to bring it up so that the issue was crisp

16:46:18 <ofrnxmr[m]> Makes sense

16:46:48 <Rucknium[m]> Because when you set a precedent, it's good to know that you're setting a precedent.

16:47:01 <Rucknium[m]> Even if precedent isn't extremely important to CCS

16:47:08 <ofrnxmr[m]> I'm ok with merging to in progress. Not to set precedent.

16:47:08 <ofrnxmr[m]> I think we should always explore the "community sentiment" if a situation arises like
this in the future

16:47:26 <ofrnxmr[m]> Took the words out of my mouth, ruck

16:49:41 <plowsof11> will pass these thoughts on, ( i could see this being funded (more than 30) regardless of
using xmrsales funds, just to stress it is indeed about setting precedent) will leave this topic here then for
this meeting?

16:50:10 <plowsof11> Isthmus hasn't responded to ... anything / anywhere afaik about their proposal

16:50:26 <plowsof11>   d. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/375)

16:51:00 <Rucknium[m]> I gave isthmus a C++ "test" for his developer. He said he would start pushing for the
CCS when the test is complete.

16:51:07 <monerobull[m]> If rucknium thinks it's important than i vote yes

16:51:21 <plowsof11> some comments do not require a c++ test to be complete

16:51:34 <plowsof11> thanks for submitting a test for your needs

16:51:56 <Lovera[m]> monerobull[m]: +1

16:52:04 <ofrnxmr[m]> I think at the least, we can merge and move 2/3 milestones in.

16:52:04 <ofrnxmr[m]> Whether to fully fund the rest, we can decide later today-this week

16:52:04 <ofrnxmr[m]> plowsof @plowsof:matrix.org:  re acceptxmr

16:52:23 <Rucknium[m]> isthmus thought it didn't make a lot of sense to push for merger when the test was not
yet complete. The test is basically an integration of R and C++. I wrote the code in R, plus a wrapper for
C++. The C++ results need to be the same as the R I already have

16:52:24 <Lovera[m]> > <@plowsof:matrix.org>   c. [Standalone AcceptXMR](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/374)

16:52:24 <Lovera[m]> >

16:52:24 <Lovera[m]> I’m in favor to merge this 👍🏼

16:53:07 <ofrnxmr[m]> Regarding isthmus, I think we can give some leeway on the timeframe (similar to bp++)

16:53:29 <ofrnxmr[m]> Perhaps change the proposal to a draft until ready to present

16:53:39 <Rucknium[m]> I wrote comments about the proposal here: https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/375#note_20706

16:53:41 <plowsof11> ill set bp++ to draft yes

16:54:14 <Rucknium[m]> Summary: "Having little knowledge of the finite-sample performance of the estimator
makes me nervous as a statistician. The phrases that come to mind are "blind spots" and "corner cutting". If
isthmus is willing to manage the C++/Rust writing and the community is willing to fund it, then we should
definitely do it."

16:56:08 <plowsof11> AOB?

16:58:01 <plowsof11> i began travelling yesterday, and should be considered as not existing 27/28/1 , and
barely alive until the 9th , please forgive me sirs

16:58:23 <ofrnxmr[m]> I covered for plowsof, np

16:58:52 <Lovera[m]> plowsof11: Enjoy your travel !! 🚌

16:59:03 <ofrnxmr[m]> Before we wrap up. There are imporant discussions in/around MRL regarding:... (full
message at
<https://libera.ems.host/_matrix/media/v3/download/libera.chat/0657d6decfbd714def146fd0cb6a25dac634bd87>)

17:00:19 <plowsof11> the first meeting that i have ever concluded on the hour , thank you all for attending


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-02-15T23:03:51+00:00
- Closed at: 2023-03-02T22:45:40+00:00
