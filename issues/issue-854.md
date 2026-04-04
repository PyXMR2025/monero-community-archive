---
title: 'Monero Community Workgroup Meeting: Saturday 1st July 2023 @ 15:00 UTC '
source_url: https://github.com/monero-project/meta/issues/854
author: plowsof
assignees: []
labels: []
created_at: '2023-06-27T10:15:48+00:00'
updated_at: '2023-07-03T14:08:47+00:00'
type: issue
status: closed
closed_at: '2023-07-03T14:08:47+00:00'
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
    - A filler meeting right after Monerokon (with another to happen in the normal slot on the 8th)
3. Greetings
4. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
    - Monerokon.com - [Day 1 raw/unedited videos from stream](https://www.youtube.com/channel/UCKxLNPJeEjPXOke55i5AIXA)
    - [MoneroTalk live from Monerokon](https://youtube.com/watch?v=m-qWvfhABrY)
    - [MoneroTalk interviews - ArticMine](https://youtube.com/watch?v=0305EoR45fQ) / [MoneroNodo](https://yewtu.be/watch?v=ejh2Hgks74I)
    - [Spike in daily transactions](https://bitinfocharts.com/comparison/monero-transactions.html#3m) - Perhaps the threat of Binance delisting causing withdraws
    - [Full Chain Membership Proofs](https://yewtu.be/IAcdRZSsIQo?t=816) - kayabanerve  (some commentary from Rucknium / kaya on [Reddit](https://www.reddit.com/r/Monero/comments/14iig7d/comment/jphetpy/)
        - Kaya states 10kb per tx but corrects to 5.5kb [in this comment](https://github.com/monero-project/research-lab/issues/100#issuecomment-1609536076)
    - spirobel has found (in some cases) major bugs in AcceptXMR for which BusyBoredom has pushed out a patch for - updating to the latest version is highly recommended [releases page](https://github.com/busyboredom/acceptxmr/releases) 
    - [Moneromarket.io has some updates!](https://www.reddit.com/r/Monero/comments/14mde7c/monero_market_updated_legal_goods_and_services/)
    - [p2pool v3.5 released!](https://www.reddit.com/r/Monero/comments/14n7tgu/p2pool_35_out_now_update/)
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [vtnerd 2023 q3 proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/391)
  b. [recanman monero jobs website proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/395)
  c. [Glitter Finance Cross-Chain Privacy Infrastructure with Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/396)
  d. [MSvB Group service at Defcon 31](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/397)
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/843)    

Meeting logs will be posted here afterwards.    

# Discussion History
## michaesc | 2023-07-01T14:40:11+00:00
Hi @plowsof ,

Please add to the section 'CCS updates':

d. [MSvB Group service at Defcon 31](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/397)

Dankon,
Michael

## plowsof | 2023-07-02T20:19:44+00:00
Logs 
```
15:00:06 <plowsof11> Meeting time https://github.com/monero-project/meta/issues/854

15:00:21 <plowsof11> sure thing

15:00:24 <plowsof11> 1. Greetings / Hello!

15:00:26 <msvb-lab> Hello.

15:00:47 <erectus> are there online exchanges that allow me to buy monero without getting blacklisted by
governments?

15:00:50 <recanman[m]> Hello

15:01:02 <Lovera[m]> Hi everyone

15:01:19 <spirobel[m]> hi

15:01:43 <naphtha[m]> erectus: localmonero.co

15:01:49 <Rucknium[m]> Hi

15:01:58 <plowsof11> we'll be having another meeting on the 8th , this is a quickly arranged filler

15:02:02 <erectus> naphtha[m]: is that bought by cash payment?

15:02:30 <recanman[m]> erectus: Yes, it includes cash by mail.

15:02:42 <Lovera[m]> 👍🏼👍🏼

15:02:42 <plowsof11> how is everyone? Monerokon happened (and yewtu.be is down)
https://www.youtube.com/channel/UCKxLNPJeEjPXOke55i5AIXA new videos as recent as 5 hours ago have been
uploaded

15:02:46 <erectus> recanman[m]: can may be anonymous?

15:02:53 <erectus> s/may/mail/

15:03:47 <recanman[m]> erectus: Depends on your threat model, usually it is not as anonymous. Read online for
opsec on cash and mail

15:03:55 <recanman[m]> s/as//

15:04:33 <erectus> recanman[m]: problem.  we really have to invest an anonymous physical goods transportation
mechanism.

15:04:40 <spirobel[m]> <john_r365[m]> "1-2 XMR to bring spirobel's..." <- > <@john_r365:monero.social> 1-2 XMR
to bring spirobel's project back online vs 90 XMR for a fresh one

15:04:40 <spirobel[m]> >

15:04:40 <spirobel[m]> > Was his site functional and usable? I didn't see it previously

15:04:40 <spirobel[m]> the site I built was mostly a landing page and a discourse instance with a theme. It
worked perfectly fine, because 99% of the functionality is off the shelf forum software. I can comment on this
in more detail if there is an interest.

15:04:41 <Lovera[m]> plowsof11: Enjoying the videos... Although I don’t like those titles... they could add
the name of the presentation or something similar

15:04:50 <ceetee[m]> plowsof11: Also mirrored on odysee

15:04:54 <plowsof11> 10kb transaction size initially brought down to 5kb after kayaba corrected some maths for
full-chain-membership-proofs transactions was kind of a big deal

15:05:44 <recanman[m]> Lovera[m]: I agree, it should increase traffic

15:05:51 <recanman[m]> * increase traffic when people search

15:06:44 <plowsof11> they are the .. raw / unedited videos also, thanks for the titles feedback (true,
important) ajs is on vacation atm. events next meeting is on the 8th iirc - there are a few other things to
clarify reg. the videos / timeframes also

15:07:29 <ofrnxmr[m]> They are creative commons for anyone who wants to use them

15:08:02 <Lovera[m]> ofrnxmr[m]: Oh, thanks for the clarification 👍🏼

15:08:15 <msvb-lab> Is this part of our meeting about Konferenco already? Because I need to announce the new
date and place.

15:08:44 <ofrnxmr[m]> https://matrix.to/#/!gclBVGbCMQJYuMOAYr:monero.social/$mXvGs0nz0Av6pulrlDscebDjE008P5zwX
9pD5Ly7-Jc?via=monero.social&via=matrix.org&via=libera.chat

15:09:20 <plowsof11> [p2pool v3.5
released!](https://www.reddit.com/r/Monero/comments/14n7tgu/p2pool_35_out_now_update/)

15:09:20 <plowsof11> 5. [CCS updates](https://ccs.getmonero.org/)  -  has a new feature : if your local node
is stuck, it will cycle through a list of remote alternatives that you provided

15:09:41 <plowsof11> clipboard hijacked by ccs updates^

15:09:56 <ofrnxmr[m]> Haha.

15:10:25 <Lovera[m]> 🤣

15:11:22 <plowsof11> we're having another meeting on the 8th as this was quickly arranged / filler (to further
discuss / wait for new ccs ideas)

15:12:08 <plowsof11> "I might put up a "wish" on my wishlist-as-a-service page to create a formal model and
classification rule for an attack on PocketChange." Rucknium @ rucknium.me

15:12:45 <Rucknium[m]> Breaking news ;)

15:13:29 <Rucknium[m]> (un)fortunately it won't be cheap.

15:13:42 <ofrnxmr[m]> Id ask at least 625k

15:14:18 <ofrnxmr[m]> And id tell those cheap food danglers to stopteasing or we'll go fmp tomorrow

15:14:21 <plowsof11> timeframe before/after seraphis gets security proofs + those proofs audited (also on the
roadmap)

15:14:43 <ofrnxmr[m]> They better hurry and fund the research so we can fund fmp

15:15:12 <nioc> schedule change o/

15:15:21 <plowsof11> hello!

15:15:25 <nioc> meow

15:15:54 <ofrnxmr[m]> what else has happened over the last coupke weeks?

15:16:20 <ofrnxmr[m]> Kayaproofs

15:16:27 <plowsof11> we're banning monero ' we're not, we are binance thing?

15:16:38 <Rucknium[m]> Triptych has a security proof published in a peer-reviewed outlet, yet it is not
considered a candidate for Monero mainnet implementation.

15:16:42 <plowsof11> transactions poomped https://bitinfocharts.com/comparison/monero-transactions.html#3m

15:17:14 <ofrnxmr[m]> Monero and xhv get delisted. Xhv loses 50% in value

15:17:20 <ofrnxmr[m]> xmr.. doesnt care

15:17:25 <Rucknium[m]> Seraphis, Bulletproofs++, and Curve Trees do not have security proofs published in a
peer-reviewed outlet, yet they are considered candidates for Monero mainnet implementation

15:17:56 <ofrnxmr[m]> Skip testnet, right ruck :D

15:18:15 <ofrnxmr[m]> the dark history of of 18.2.2 haha

15:18:35 <plowsof11> TODO (bolded, underlined... capitalised and pgp signed for all of the above)

15:19:32 <plowsof11> shall we move onto the ccs ideas?

15:19:48 <Lovera[m]> Go

15:19:49 <ofrnxmr[m]> 1 quick question

15:20:03 <ofrnxmr[m]> Rucknium:  any idea if those tx for that day were real?

15:20:07 <ofrnxmr[m]> Or spam?

15:20:15 <Lovera[m]> Nice question

15:20:23 <Rucknium[m]> Which day?

15:20:33 <plowsof11> the speculation is "withdraws from CEX's after news of bans

15:20:45 <Lovera[m]> Pumps  txs day

15:20:56 <ofrnxmr[m]> 42k tx on the 25th

15:20:58 <Lovera[m]> 40k+

15:21:09 <Rucknium[m]> High CEX volume days usually cause high on-chain txs

15:21:33 <ofrnxmr[m]> 16k on 24th

15:21:59 <Rucknium[m]> That conclusion is from some basic analysis of other coins like DOGE

15:21:59 <Lovera[m]> And I thought it was because of Monerokon 😅

15:22:05 <ofrnxmr[m]> Avg about 25k and declining

15:22:37 <recanman[m]> Lovera[m]: I also thought it was from MoneroKon. I did not check XMR/USD for a week,
and all of a sudden it was up 18%

15:22:45 <Rucknium[m]> IMHO, the on-chain volume was probably real

15:22:50 <ofrnxmr[m]> We also still have the were cycling of transaction days

15:23:30 <ofrnxmr[m]> s/were/weird/

15:23:31 <ofrnxmr[m]> But yes, lets move to ccs ideas

15:23:45 <ofrnxmr[m]> plowsof @plowsof:matrix.org:  thanks

15:23:59 <plowsof11> it was because of Monerokon

15:24:04 <plowsof11> ok lets move on 😄

15:24:07 <plowsof11> 5. [CCS updates](https://ccs.getmonero.org/)

15:24:20 <plowsof11>   a. [vtnerd 2023 q3 proposal](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/391)

15:24:37 <Rucknium[m]> +1 merge

15:24:42 <plowsof11> been up for a while / had feedback from the right persons, time for a vote

15:24:47 <plowsof11> +merge

15:24:48 <Lovera[m]> Merge

15:25:06 <recanman[m]> +1

15:25:08 <recanman[m]>  * +merge

15:25:11 <jeffro256[m]> merge

15:25:32 <tobtoht[m]> merge

15:25:40 <ofrnxmr[m]> Merge pls

15:26:03 <plowsof11> a clear merge, moving on

15:26:12 <plowsof11> thanks for voting all

15:26:14 <msvb-lab> +1.

15:26:20 <plowsof11>   b. [recanman monero jobs website proposal](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/395)

15:26:45 <plowsof11> thanks^

15:27:00 <recanman[m]> There have been discussions in order to rewrite [Bitejo](https://bitejo.com), an
already-existing service

15:27:15 <plowsof11> now moving on to b. recanman posted this only recently. had alot of discussion already.
is this the final version of your proposal you want people to review?

15:27:32 <recanman[m]> Yes, I don't think I have any changes to make.

15:28:07 <ceetee[m]> I would like to hear from people who want to use such a site

15:28:19 <plowsof11> if we look at it as "recreating something that already existed(exists) then is it not a
tough sell?

15:28:20 <naphtha[m]> recanman[m]: whats wrong with bitejo?

15:28:26 <ofrnxmr[m]> but not ready to be voted on. Are you planning to move forward with the bitejo rewrite?

15:28:43 <ofrnxmr[m]> naphtha[m]: Messy code, anark needs help, bitejo needs funding

15:28:48 <plowsof11> if you dont like this , then im making a bitejo proposal?

15:28:48 <recanman[m]> naphtha[m]: It is written in procedural PHP, and is maintained as a hobby. I would also
like to add on to it the jobs portion.

15:28:57 <recanman[m]> ofrnxmr[m]: I'm fine with either pathway

15:29:17 <plowsof11> ok well it takes alot of wrinkles / effort for everyone to review these proposals

15:29:30 <recanman[m]> I would prefer the Bitejo rewrite, as it gives me a basis + expands the site to more
interests.

15:29:32 <naphtha[m]> i've been thinking of creating a freelance website, such as fiverr, with an escrow. not
that i will have the time to put it into practice any time soon but i have used freelance websites in the past
and the payouts were the most annoying part

15:29:48 <recanman[m]> naphtha[m]: Yes, my proposal does include escrow.

15:30:05 <recanman[m]> With the Bitejo rewrite, a user can have one account in order to use the different
services

15:30:26 <naphtha[m]> * the past (as a seller) and the

15:30:30 <chesterfield[m]> Why is bitejo needed when there’s that other xmr shopping site

15:30:34 <recanman[m]> There is the money-raising (GoFundMe), the marketplace (craigslist), and then the
potentially-upcoming jobs (Indeed or job sites)

15:30:49 <ofrnxmr[m]> chesterfield[m]: Bitejo isnt just "craigslist"its a suite

15:30:52 <plowsof11> moneromarket dot io (probably has nsfw things)

15:30:59 <recanman[m]> I would also like to make sure that client-side JavaScript is not involved

15:31:04 <ofrnxmr[m]> kuno.bitejo.com for gofundme for example

15:31:40 <plowsof11> recanman: but atm we are reviewing the proposal youve got up now or are you going to re-
write / resubmit?

15:31:53 <recanman[m]> Due to my threat model, I have JavaScript disabled. Trocador.app was a very big help to
me, and I believe that this can also be a help to others who do not want to provide their phone number to
telegram in order to get hired/hire

15:32:04 <recanman[m]> plowsof11: Yep, the proposal is final.

15:32:15 <recanman[m]> * get hired/hire people.

15:32:18 <chesterfield[m]> plowsof11: I didn’t see anything listed in the nsfw section last time I checked

15:32:28 <Lovera[m]> If rewritten = the same amount xmr?

15:32:33 <recanman[m]> chesterfield[m]: I believe there are people selling pictures of themselves.

15:32:36 <plowsof11> true ^ swiim clicked it the other day and nothing came up

15:32:38 <chesterfield[m]> Don’t dnm’s already function as no js marketplaces

15:32:45 <ofrnxmr[m]> Recan, the proposal has to indicate thr work planned

15:33:05 <ofrnxmr[m]> So if you are going bitejo route, will need to edit the proposal to show that

15:33:05 <recanman[m]> Lovera[m]: I can do it for much less, probably 50/60. I don't want to deviate from the
normal software developer salary too much.

15:33:14 <recanman[m]> Oh, ok.

15:33:17 <ofrnxmr[m]> chesterfield[m]: These arent dnm

15:33:27 <ofrnxmr[m]> These are for mom and pops

15:33:32 <recanman[m]> Should I rewrite it now, or do I have time until the next meeting?

15:33:43 <ofrnxmr[m]> recanman[m]: Youbhave time

15:33:49 <chesterfield[m]> Wasn’t there a kernel proposal for a no js market thing or was that different

15:33:50 <recanman[m]> Great, thanks.

15:33:51 <ofrnxmr[m]> Next meeting is in 1 week

15:33:57 <naphtha[m]> recanman[m]: i would suggest to use something like fresh.deno.dev (server-side react)
instead of nunjucks. speaking from experience, it's a lot cleaner

15:34:18 <plowsof11> ideas usually pop up in 2 meeings~1 month, by then people have a good enough idea if they
like it or not

15:34:21 <ofrnxmr[m]> chesterfield[m]: Metronero?

15:34:30 <chesterfield[m]> ofrnxmr[m]: Yes

15:34:45 <chesterfield[m]> Maybe that wasn’t a shopping site though

15:35:06 <recanman[m]> The Monero jobs Telegram is immensely useful and got me involved when I knew nothing
about Monero, and just got into it. Another problem is the lack of escrow, which can be mitigated with a
dedicated solution.

15:35:08 <ofrnxmr[m]> I think youre thinking on "moneroshopping"

15:35:13 <recanman[m]>  * The Monero jobs Telegram is immensely useful and got me involved when I knew nothing
about Monero, and just got into it. Another problem is the lack of escrow, which can be mitigated with a
dedicated solution.

15:35:13 <recanman[m]> Just another point.

15:35:44 <ofrnxmr[m]> s/on/of/

15:35:58 <plowsof11> successonly dot work back online for 1-2 xmr was offered but spirobel would have to
confirm

15:36:11 <recanman[m]> naphtha[m]: Thank you very much, I will look into that. Since it looks like it will be
the Bitejo rewrite, I will probably use Nunjucks and just copy over most of the HTML/CSS for simplicity. This
is why I can do it for much less, as the frontend is not involved.

15:36:13 <spirobel[m]> recanman[m]: > <@recanman:agoradesk.com> The Monero jobs Telegram is immensely useful
and got me involved when I knew nothing about Monero, and just got into it. Another problem is the lack of
escrow, which can be mitigated with a dedicated solution.

15:36:13 <spirobel[m]> > Just another point.

15:36:13 <spirobel[m]> is there a lot of demand for Monero freelancers in this group?

15:36:17 <ofrnxmr[m]> Spirpbel is busy talking shit in another room

15:36:22 <plowsof11> (i dont know if that site is open source, also waiting for clarification)

15:36:29 <ofrnxmr[m]> Oh, nvm, hes here

15:37:08 <ofrnxmr[m]> Welcome back

15:37:26 <recanman[m]> s/50/60/65/

15:37:49 <recanman[m]> plowsof11: According to him, it's a rebranded Discourse software thing

15:38:27 <plowsof11> if it works it works

15:39:03 <plowsof11> i see more success in working on an existing project instead of rebuilding something from
scratch

15:39:09 <recanman[m]> I believe that including the Bitejo suite and expanding on it will be much more
effective than a forum.

15:39:14 <recanman[m]> I agree!

15:40:29 <Rucknium[m]> IMHO, these types of things that need to build a social/economic network usually find
success or failure based on non-technical factors

15:40:41 <ofrnxmr[m]> I like it. Let us know when youve updated (before meeting) so we can take a look

15:41:00 <spirobel[m]> the thing is this: this kind of "marketplace site" shares 99% with a forum. You need
moderation, search, categories, posts, comments, admin, register, login. There is no point to write all of
this from scratch. It will be next to impossible to do a good job at this as a single programmer building it
from scratch. Even if it is done well, it will not be comparable to the work of a large company that wrote and
maintains open source

15:41:00 <spirobel[m]> forum software.

15:41:06 <plowsof11> we could fund 15 developers to create 15 success only websites , i agree with Rucknium

15:41:10 <spirobel[m]> * shares 99% of functionality with a

15:41:27 <plowsof11> i dont think "javascript" being enabled on successonly was the deciding factor as to why
it was discontinued

15:41:43 <chesterfield[m]> I don’t think it’s a forum at all

15:42:03 <recanman[m]> spirobel[m]: I am not sure if it is too much like a forum.

15:42:43 <recanman[m]> There is the aspect of posting a "thread" (job posting), and then people "replying"
(sending your resume), but I don't have any experience with Discourse software

15:43:02 <chesterfield[m]> Bounties is probably the best example we have of using software for an unintended
use

15:43:04 <recanman[m]> I think it ends at that.

15:43:48 <ofrnxmr[m]> Any more ideas on the agenda?

15:43:51 <recanman[m]> bounties.monero.social is nice, but it serves a different purpose: crowd-sourced
funding

15:44:01 <plowsof11> yes lets hit pause on this idea for now

15:44:09 <recanman[m]> Good ideal.

15:44:11 <recanman[m]>  * Good idea.

15:44:11 <ofrnxmr[m]> And a bounty is fundamentallt different than a fundraiser

15:44:17 <chesterfield[m]> Yes I’m just saying that depending on a totally different upstream software causes
breakage and pain

15:44:29 <plowsof11>   c. [Glitter Finance Cross-Chain Privacy Infrastructure with
Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/396)

15:44:29 <plowsof11>

15:44:33 <Rucknium[m]> Why not find a way to add XMR to a jobs site that already has a userbase?

15:44:36 <ofrnxmr[m]> Burn it with fire

15:44:54 <plowsof11> i dont think we need to have much more input on the glitter proposal other than whats
been said today?

15:44:58 <plowsof11> im voting for close

15:45:09 <ofrnxmr[m]> Rucknium[m]: This 3. But a lot of these corps wont mess with us/xmr

15:45:16 <recanman[m]> I read it a few hours ago, it just seems about someone talking about money

15:45:22 <ofrnxmr[m]> Like airbnb

15:45:25 <plowsof11> they are very very rich

15:45:26 <recanman[m]> * about money. Where is their 7million usd?

15:45:36 <recanman[m]> * about money. Where is their 7million USD?

15:45:40 <recanman[m]> * about money. Where is their 7 million USD?

15:45:52 <Lovera[m]> plowsof11: > <@plowsof:matrix.org>   c. [Glitter Finance Cross-Chain Privacy
Infrastructure with Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/396)

15:45:52 <Lovera[m]> >

15:45:52 <Lovera[m]> Don’t we already have several atomic swaps projects with top coins such as Bitcoin and
Ethereum? I don’t understand very well this proposal

15:45:55 <ofrnxmr[m]> 7.2mill single handedly raised.

15:45:55 <ofrnxmr[m]> did they.. have a boating accident?

15:46:16 <recanman[m]> Rucknium[m]: Those will most likely need KYC and JavaScript, please let me know if you
find a job site dedicated to privacy

15:46:17 <recanman[m]> * to privacy.

15:46:42 <plowsof11> lol with 14 mins left we can leave it open for next week (maybe they will have a
rebuttal)

15:46:45 <Rucknium[m]> Online merchants complain that it is hard to integrate XMR into their merchant
software. Where are the CCS proposals about that?

15:46:52 <ofrnxmr[m]> Lovera[m]: Its a tunnel to fake privacy by using monero as a conduit between blockchains
that have no privacy

15:47:05 <spirobel[m]> chesterfield[m]: That is true. And i think at some point you need to write something
from scratch. But the issue why Monero job markets fail is not because of the tech. It is because there is not
enough demand and its super hard to start marketplaces. Also: many marketplaces started with forums. So I
disagree with the assessment that its not like a forum.

15:47:05 <naphtha[m]> Rucknium[m]: imagine you're a jobs site with a considerably big userbase and a community
based around a cryptocurrency that is consistently portrayed in the media as being the "criminal's bitcoin"
asks you to accept their currency

15:47:16 <naphtha[m]> why would they risk their reputation

15:47:25 <ofrnxmr[m]> plowsof11: We have 7 days. Can leave it ooen

15:47:34 <ofrnxmr[m]> But my vote stands. Burn it

15:47:34 <plowsof11> we have another new proposal to look at though from msvb

15:47:36 <Lovera[m]> ofrnxmr[m]: Ok, close it 😅

15:47:57 <recanman[m]> Based on my assessment, I agree to close

15:47:57 <msvb-lab> This one allows us to participate in an official Defcon area, it is event based and
distributes books and badges.

15:48:00 <recanman[m]> * to close.

15:48:07 <plowsof11> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/397

15:48:07 <plowsof11> Serving Defcon 31 (2023)

15:48:30 <recanman[m]> It's quite detailed, which is nice.

15:48:59 <msvb-lab> No, 90% details are missing. We just have too much Defcon historical information in our
heads and no time to record it.

15:49:37 <ofrnxmr[m]> Lol

15:49:56 <ofrnxmr[m]> Half the cost of our OWN conference

15:50:24 <ofrnxmr[m]> Cut this shit Cryptohip badges20000 USDCost of four hundred electronic badges

15:50:33 <msvb-lab> The reason distribution (hundreds instead of thousands) and related costs are reduced is
due to expected abandon.

15:50:51 <ceetee[m]> same badges as those at monerokon?

15:50:54 <naphtha[m]> ofrnxmr[m]: lmao yeah wtf is that

15:50:56 <recanman[m]> I refute my point, I skimmed over it

15:51:01 <recanman[m]> s//./

15:51:04 <ofrnxmr[m]> What the hellis a cryptohip badge

15:51:06 <msvb-lab> Very similar ceetee yes, derivatives of the Cryptohip.

15:51:16 <plowsof11> the badges are indeed the main chunk

15:51:17 <msvb-lab> And the Mastering Monero is the old one, version 1 I guess.

15:51:21 <Lovera[m]> What are cryptohit bagges?

15:51:29 <Lovera[m]> Badges

15:51:37 <ofrnxmr[m]> A fuxking scam

15:51:40 <msvb-lab> Electronic badges that hackers stand in line to get and later wear. The smart ones hack
them as well.

15:51:43 <ofrnxmr[m]> What ami looking at lmao

15:51:47 <ofrnxmr[m]> Nexxxzt

15:51:53 <recanman[m]> I think I am reading it incorrectly, but it seems that they are saying that it should
be canceled? I don't understand.

15:52:06 <recanman[m]> >Denying the Monero community an official presence at Defcon would save us money, so
it's a valid option to consider.

15:52:09 <ofrnxmr[m]> Im saying what the hell

15:52:26 <Lovera[m]> I don’t have time to read so many messages 🤣

15:52:26 <msvb-lab> We should only deny the Monero community an official presence at Defcon if we think there
will be abuse or bad behaviour.

15:52:43 <ofrnxmr[m]> 20k is abuse

15:52:46 <Lovera[m]> Is this the short or long meeting? plowsof 🤣

15:52:49 <ofrnxmr[m]> I have a better use for it

15:52:49 <recanman[m]> msvb-lab: I don't understand what that means?

15:52:51 <tobtoht[m]> $50 per badge seems.. excessive?

15:52:53 <ofrnxmr[m]> Give ofrn 20k

15:53:03 <plowsof11> it is a short/quick filler meeting Lovera 20~ mins max

15:53:11 <msvb-lab> It means recanman that if we expect bad behaviour then we should reject this CCS.

15:53:18 <ceetee[m]> handing out non monero-specific hardware for 50$ each seems a bit wasteful

15:53:22 <msvb-lab> Because of high standards at Defcon.

15:53:23 <recanman[m]> msvb-lab: That does not clarify it.

15:53:27 <ceetee[m]> ofrnxmr[m]: no

15:54:08 <naphtha[m]> defcon really is shit tbh

15:54:16 <msvb-lab> We are welcome to serve as the CCS describes if nobody brings drug merchandise, for
example. And uses no bad language, and does not abuse staff or visitors.

15:54:20 <plowsof11> are the badges compulsory msvb-lab ? does every project purchase these to attend?

15:54:23 <naphtha[m]> only good guest in the past 10 years was sam bent from doingfedtime

15:54:32 <ofrnxmr[m]> ofrnxmr[m]: s/out/put

15:54:34 <naphtha[m]> the rest were all annoying nerds

15:54:45 <ofrnxmr[m]> plowsof11: ^

15:55:04 <recanman[m]> msvb-lab: What incites that specifically from the Monero community?

15:55:15 <recanman[m]> I think we should move on.

15:55:26 <Lovera[m]> Btw seems like SDK proposal, It has stopped with founding

15:55:30 <msvb-lab> recanman: There is a lot of history of abuse, that is the reason for the clause.

15:55:46 <msvb-lab> And that we are trying to increase family contributions and child friendly content,
especially at DC31.

15:55:47 <ofrnxmr[m]> Yeah. lets move on. Lol

15:56:09 <ofrnxmr[m]> if no more ideas, where do we stand with funding current proposals

15:56:11 <recanman[m]> msvb-lab: You sound like a bot, I really do not understand what you are saying.

15:56:30 <msvb-lab> plowsof11: I'm not sure which groups are distributing badges, most are incapable of
producing them.

15:56:42 <plowsof11> ok thanks for clarifying

15:56:46 <msvb-lab> And some groups not invited to Defcon like Whiskey Pirates produce them but distribute
offsite in a hotel room.

15:57:05 <ofrnxmr[m]> msvb-lab: 20k

15:57:10 <ofrnxmr[m]> Im crying

15:57:23 <Lovera[m]> 20k $ is a lot of money

15:57:28 <ofrnxmr[m]> Who's producing them for you

15:58:02 <msvb-lab> Lovera: It's much less than most years while distributing thousands and much more than the
years when we had no badge distribution at all.

15:58:03 <ofrnxmr[m]> ofrnxmr[m]: ok. ^^ lets move on.

15:58:20 <msvb-lab> There has also never been a widespread distribution of paper books which could be
interesting.

15:58:35 <ofrnxmr[m]> 2 mins left

15:58:45 <plowsof11> i like the books available for distribution

15:58:47 <msvb-lab> We didn't have time to reach serhack.

15:59:09 <msvb-lab> If we reject this CCS there will still be a lot of books available, because O'Reilly is
next in line.

15:59:11 <ofrnxmr[m]> 20k, 8 months, no time

15:59:15 <ofrnxmr[m]> U crack me up

15:59:20 <plowsof11> any surplus books could be absorbed back into storage for the next monerokon too

15:59:37 <plowsof11> and serhack benefits (i assume)

15:59:52 <msvb-lab> The 8 months is only during our negotiations, other activities began about 11 months ago.

16:00:27 <msvb-lab> We have a 16 month work cycle for Konferenco and 12 month work cycle for Defcon.

16:00:59 <ceetee[m]> <msvb-lab> "And the Mastering Monero is..." <- plowsof @plowsof:matrix.org:  dont want
the old version for monerokon

16:01:01 <plowsof11> eh oh

16:01:18 <msvb-lab> There is only the old version available at Amazon, which is where we would buy them.

16:01:32 <msvb-lab> Unless hbs or sgp or others at the publisher have advice.

16:01:44 * ofrnxmr[m] uploaded an image: (108KiB) <
https://libera.ems.host/_matrix/media/v3/download/monero.social/QfZGQPdtEJTDcdaztwdjnZdI/yq1uqm7v3jewosw6.jpg
>

16:01:54 <ofrnxmr[m]> msvb-lab: Man youre terrible

16:02:25 <plowsof11> SerHack: could maybe shed some light on that (how to get the new printed version)

16:02:42 <nioc> is there a new version?

16:02:59 <ofrnxmr[m]> Wallet sdk is the only proposal not fully funded. plowsof @plowsof:matrix.org:
anybreasonnthe site isnt updating?

16:03:00 <spirobel[m]> msvb-lab: you are the organizers behind monero kon, right?

16:03:06 <Lovera[m]> ofrnxmr[m]: Stuck SDK for Android

16:03:08 <msvb-lab> Yes spirobel.

16:03:10 <plowsof11> right.. eta for the new version* nioc

16:03:11 <ofrnxmr[m]> Are jeffro and vost overfunded now?

16:03:24 <msvb-lab> I am one of the Konferenco staff, we are about five or six people.

16:03:32 <spirobel[m]> msvb-lab: thank you for your work! It seems like it was an awsome conference!

16:03:45 <plowsof11> += 0.060425224358 for the jet fund ofrnxmr

16:03:49 <msvb-lab> You're welcome. I want to announce the 2024 date now, if it's the correct time.

16:03:55 <nioc> ajs is the organizer, there are many that did a great deal of work

16:04:48 <ofrnxmr[m]> I am ceo of monerokon. Good job team

16:05:29 <ceetee[m]> was a pleasure to meet you

16:05:36 <plowsof11> i think we can end the meeting here and continue discussions ... vtnerd merge , glitter
close, other ideas to be discussed on the 8th

16:05:38 <nioc> eta for mastering monero 2.0 is 2021

16:06:10 <plowsof11> thank you all for attending , Cat too

16:06:33 <msvb-lab> Thanks for the good meeting and plowsof for moderating.

16:08:16 <Lovera[m]> Thanks

16:08:16 <spirobel[m]> ofrnxmr[m]: did you attend a monero conference before?

16:09:07 <Lovera[m]> nioc: I would like to see an updated version of Zero to Monero

16:09:57 <nioc> it's needed for sure

16:10:07 <recanman[m]> My first meeting, and it went very well. I will be attending more in the future.
Goodbye everyone!

16:11:02 <sgp[m]> MSvB:  I know you're really passionate about the badges, but they are simply too expensive
imho

16:12:12 <sgp[m]> If we want presense at Defcon to talk about Monero (reasonable), we should do flyers or
something, and find people in Vegas or nearby area. We could pay them for their time and still come out way
ahead of transatlantic flights

16:15:15 <sgp[m]> Having a fraction of a vendor section for Monero stuff simply isn't as valuable as this CCS
is for

16:16:09 <spirobel[m]> sgp[m]: There are probably some infosec people in the Monero community that will go
anyway. Maybe it could be a  job for them.

16:16:46 <sgp[m]> Exactly. Find someone going, give them flyers and some money

16:17:23 <spirobel[m]> where the electronic badges supposed to be self made by the proposer?

16:17:30 <spirobel[m]> s/where/were/

16:17:53 <sgp[m]> Maybe the vendor booth is worth $1000 or so for the space, but I'd need to learn more about
that

16:18:54 <spirobel[m]> guerrilla marketing is probably a better approach than a vendor both though ... just
wonder if something like this is against the defcon CoC and they would kick you out for doing it ...

16:19:21 <spirobel[m]> because otherwise we are seen in the same way as many dodgy AV product vendors ...

16:19:33 <sgp[m]> spirobel[m]: The vendor booth or guerilla stuff?

16:19:37 <ceetee[m]> spirobel[m]: Monerokon badges were originally designed for another conference, with
updated branding. Assembled professionally, so I'd guess the work was outsourced

16:19:45 <spirobel[m]>  * because otherwise we could be seen in the same way as many dodgy AV product vendors
...

16:19:53 <sgp[m]> spirobel[m]: Eh, people should be relieved to see Monero there. Space isn't a bad idea imo

16:20:59 <spirobel[m]> the first time I saw Bitcoin was in the form of an ATM at a CCC conference.

16:21:08 <spirobel[m]> Maybe an atm is a good idea. Makes it feel real

16:23:16 <sgp[m]> Couldn't function though. That was a weak point of Defcon 2018

16:56:45 <SerHack> Out of the loop, what do you need?

17:39:28 <plowsof11> SerHack: i thought the new version was mastering Monero complete but not yet


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued:
```
16:11:02 <sgp[m]> MSvB:  I know you're really passionate about the badges, but they are simply too expensive imho
16:12:12 <sgp[m]> If we want presense at Defcon to talk about Monero (reasonable), we should do flyers or something, and find people in Vegas or nearby area. We could pay them for their time and still come out way ahead of transatlantic flights
16:15:15 <sgp[m]> Having a fraction of a vendor section for Monero stuff simply isn't as valuable as this CCS is for
16:16:09 <spirobel[m]> sgp[m]: There are probably some infosec people in the Monero community that will go anyway. Maybe it could be a  job for them.
16:16:46 <sgp[m]> Exactly. Find someone going, give them flyers and some money
16:17:23 <spirobel[m]> where the electronic badges supposed to be self made by the proposer? 
16:17:30 <spirobel[m]> s/where/were/
16:17:53 <sgp[m]> Maybe the vendor booth is worth $1000 or so for the space, but I'd need to learn more about that
16:18:54 <spirobel[m]> guerrilla marketing is probably a better approach than a vendor both though ... just wonder if something like this is against the defcon CoC and they would kick you out for doing it ... 
16:19:21 <spirobel[m]> because otherwise we are seen in the same way as many dodgy AV product vendors ...
16:19:33 <sgp[m]> spirobel[m]: The vendor booth or guerilla stuff?
16:19:37 <ceetee[m]> spirobel[m]: Monerokon badges were originally designed for another conference, with updated branding. Assembled professionally, so I'd guess the work was outsourced
16:19:45 <spirobel[m]>  * because otherwise we could be seen in the same way as many dodgy AV product vendors ...
16:19:53 <sgp[m]> spirobel[m]: Eh, people should be relieved to see Monero there. Space isn't a bad idea imo
16:20:59 <spirobel[m]> the first time I saw Bitcoin was in the form of an ATM at a CCC conference.
16:21:08 <spirobel[m]> Maybe an atm is a good idea. Makes it feel real
16:23:16 <sgp[m]> Couldn't function though. That was a weak point of Defcon 2018
16:56:45 <SerHack> Out of the loop, what do you need?
17:39:28 <plowsof11> SerHack: i thought the new version was mastering Monero complete but not yet 
18:07:23 <plowsof11> is "mastering Monero complete" a way to describe something that is very complete 
19:21:36 <xmrscott[m]> <spirobel[m]> "There are probably some infosec..." <- I will be there this year, less sure about next year if they keep hiking the prices the way they did this year
19:34:27 <xmrscott[m]> Flyers in the actual Villages is a big no no. There are however plenty of tables in the hallways and open spaces to leave flyers w/o reprocussion if it wants. That's usually how people put out things for puzzles to exclusive parties, etc
19:34:43 <xmrscott[m]> s/reprocussion/repercussion/, s/it/you/, s/wants/want/
20:00:40 <ajs_[m]> To be honest, we were politely kicked out of Defcon by being downgraded from a full named village to a cryptocurrency village to being lumped in with t-shirt vendors
20:00:57 <ajs_[m]> There is little to no value engaging there 
```

# Action History
- Created by: plowsof | 2023-06-27T10:15:48+00:00
- Closed at: 2023-07-03T14:08:47+00:00
