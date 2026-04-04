---
title: 'Monero Community Workgroup Meeting: Saturday 2nd September 2023 @ 15:00 UTC'
source_url: https://github.com/monero-project/meta/issues/886
author: plowsof
assignees: []
labels: []
created_at: '2023-08-29T10:13:37+00:00'
updated_at: '2023-09-11T08:09:16+00:00'
type: issue
status: closed
closed_at: '2023-09-11T08:09:16+00:00'
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
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)  
    - Bitmain releases [2 year old](https://libera.monerologs.net/monero-pow/20230827#c275018) hardware that could be [bricked](https://libera.monerologs.net/monero-pow/20230827#c275167). currently [~17% of network hash](https://libera.monerologs.net/monero-pow/20230827#c275098) - sech1 the ASIC bricker
    - [HushPics](https://hushpics.xyz/) - image hosting service that obscures uploads - users send XMR to see the original - lza_menace
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [recanman to take over Monero integrations pt. 3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/402)
  b. [Add retroactive funding proposal for FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)    
  c. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/406)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/871)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2023-09-11T08:08:50+00:00
Logs 
```
15:00:39 <m-relay> <p​lowsof:matrix.org> Meeting time https://github.com/monero-project/meta/issues/886

15:00:43 <m-relay> <p​lowsof:matrix.org> Greetings!

15:00:47 <m-relay> <r​4v3r23:monero.social> yo

15:00:54 <m-relay> <r​ucknium:monero.social> hi

15:01:07 <m-relay> <p​lowsof:matrix.org> ofrnxmr and geonic have jumped over the imaginary broomstick today
and are not banned in events anymore for those wondering (events meeting in 2 hours)

15:02:39 <m-relay> <b​tclovera:matrix.org> Hi

15:03:52 <m-relay> <p​lowsof:matrix.org> lets discuss some 3. Community highlights

15:03:54 <m-relay> <s​needlewoods_xmr:matrix.org> hello everyone

15:04:08 <m-relay> <p​lowsof:matrix.org> [Revuo Monero](https://revuo-xmr.com/) has covered a fair chunk of
highlights this week i noticed

15:04:15 <m-relay> <p​lowsof:matrix.org> causing the most noise: Bitmain releases [2 year
old](https://libera.monerologs.net/monero-pow/20230827#c275018) hardware that could be
[bricked](https://libera.monerologs.net/monero-pow/20230827#c275167). currently [~17% of network
hash](https://libera.monerologs.net/monero-pow/20230827#c275098) - sech1 the ASIC bricker

15:05:08 <m-relay> <m​onerobull:matrix.org> I don't see the point in bricking them

15:05:10 <m-relay> <m​onerobull:matrix.org> It's just some above average efficiency cpus

15:05:15 <m-relay> <m​onerobull:matrix.org> Getting them distributed to real people is way better than leaving
them with Bitmain

15:05:33 <m-relay> <p​lowsof:matrix.org> i learned that risc-v is pronounced risc-five , and that is open
source / royalty free cpu

15:06:28 <m-relay> <m​onerobull:matrix.org> Crippling all of riscv for this doesn't make sense imo

15:06:46 <m-relay> <r​4v3r23:monero.social> its not an asic

15:06:51 <m-relay> <r​4v3r23:monero.social> its a nonissue

15:06:54 <m-relay> <p​lowsof:matrix.org> true not an asic

15:06:57 <m-relay> <c​trej:matrix.org> that was the sentiment in the pow room as well

15:06:59 <m-relay> <r​4v3r23:monero.social> next

15:07:39 <m-relay> <p​lowsof:matrix.org> thanks for crunching the numbers ct (comparing hardware prices for
$/H/s)

15:08:55 <m-relay> <m​onerobull:matrix.org> I wonder if Bitmain even made money

15:09:41 <m-relay> <b​tclovera:matrix.org> We need to see how much will be the price…

15:09:45 <m-relay> <p​lowsof:matrix.org> #monero-pow:monero.social is where this was discussed in detail for
those not in the know, they where in profit 2 years ago ~

15:10:15 <m-relay> <c​trej:matrix.org> after the first teardown we can estimate their profit

15:10:19 <m-relay> <b​tclovera:matrix.org> Well, they has mining 2 years + now they will sell Used hardware so
I thing yes

15:10:34 <m-relay> <p​lowsof:matrix.org> still "guess the price mode" aka let bitmain see how much profit they
can squeese out of them / tell them what you are willing to pay

15:11:20 <m-relay> <m​onerobull:matrix.org> If they didn't get special electricity prices or extra money for
providing binance with xmr, I don't think they would have made money all bear market

15:11:28 <m-relay> <p​lowsof:matrix.org> not an asic as r4v3r said earlier AND Monero appearing all over the
youtuber mining scene / news sites is a win

15:12:12 <m-relay> <m​onerobull:matrix.org> Yeah, only downside is the confused people who think "haha we just
fork the Algo"

15:12:27 <m-relay> <p​lowsof:matrix.org> bitmain should publish the schematics on
[HushPics](https://hushpics.xyz/) for some more profit - image hosting service that obscures uploads - users
send XMR to see the original - lza_menace

15:14:42 <m-relay> <p​lowsof:matrix.org> any other highlights? (other than the retroactive funding request
that is up for discussion later)

15:15:03 <m-relay> <m​onerobull:matrix.org> monerosupplies has been migrated to a new provider, if there are
any issues, please report

15:15:29 <m-relay> <m​onerobull:matrix.org> also, SerHack all throughout last week the plugin hasnt been
recognizing incoming payments, any idea what might be up with that?

15:16:17 <m-relay> <p​lowsof:matrix.org> ah yeah, "not recognising incoming payments" kinda of a big deal ...
thankfully we have someone to hopefuly work on that 👀

15:16:43 <m-relay> <m​onerobull:matrix.org> its not a big deal actually, i just have to manually check that an
order was paid

15:18:55 <m-relay> <p​lowsof:matrix.org> Boogs proposal is almost funded btw 128/130 👍️

15:19:03 <m-relay> <p​lowsof:matrix.org> lets jump into the merge requests if no more highlights

15:19:15 <m-relay> <p​lowsof:matrix.org> a. [recanman to take over Monero integrations pt.
3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/402)

15:19:17 <m-relay> <p​lowsof:matrix.org> this proposal was discussed last meeting with a positive merge
sentiment however not much activity on gitlab (thank you ceetee for leaving some feedback) - would anyone like
to voice their opinion on merging/closing this after reading the merge request description? (no extra funds
have to be raised, simply transferred to recanmann who has already made that serhack has approved). w<clipped
message>

15:19:17 <m-relay> <p​lowsof:matrix.org> e can get a 'dormant since 2020' ccs proposal completed then.

15:19:30 <m-relay> <p​lowsof:matrix.org> perhaps monerobull has an opinion (being a merchant that uses the
monero-php / wordpress plugin)

15:20:28 <m-relay> <r​ucknium:monero.social> It's probably not getting much activity on gitlab since it
doesn't appear on the Idea page of the CCS website

15:21:10 <m-relay> <m​onerobull:matrix.org> yeah

15:21:25 <m-relay> <m​onerobull:matrix.org> i didnt notice this before at all

15:22:20 <m-relay> <p​lowsof:matrix.org> so what has happened: recanman has closed the bitejo proposal
temporarily in favour of a hidden merge request

15:22:22 <m-relay> <m​onerobull:matrix.org> seems like a decent proposal with no downsides

15:24:08 <m-relay> <p​lowsof:matrix.org> anyone here who didnt vote to merge/close on this last meeting please
voice your opinion and we never have to discuss it again !

15:24:25 <m-relay> <m​onerobull:matrix.org> i like the optimism

15:26:23 <m-relay> <p​lowsof:matrix.org> i will vote my own merge request up if need be. desperate times,
desperate measures

15:27:31 <m-relay> <r​ucknium:monero.social> I think TrasherDK was concerned about security review of the PHP.
Unfortunately none of these non-core software proposals have received security reviews AFAIK, so the precedent
is caveat emptor for users. SerHack is a security researcher and could informally review the result, I guess.

15:28:07 <m-relay> <p​lowsof:matrix.org> indeed, at least, with this proposal, it is only completed after
serhack reviews and merges each pull request

15:30:28 <m-relay> <p​lowsof:matrix.org> we can move on with an extra +merge from monerobull to add to the
previous meetings votes?

15:31:23 <m-relay> <p​lowsof:matrix.org> b. [Add retroactive funding proposal for
FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)

15:31:48 <m-relay> <p​lowsof:matrix.org> now, at 10 thumbs up and 0 thumbs down - a simple decision no? :)

15:31:49 <m-relay> <m​onerobull:matrix.org> indeed.

15:34:43 <m-relay> <c​trej:matrix.org> Going by the votes its clear, but I wished that the people who were not
happy with this proposal either vote or show up today

15:34:46 <m-relay> <c​trej:matrix.org> not happy according to the gitlab comments I mean

15:36:58 <m-relay> <p​lowsof:matrix.org> there are compelling arguments in the comments. one small thing i
noticed was jtgrassie linking a rejected "RandomX Thanks" -> there are 2 'gifts' in this proposal -- one for
jberman which is not a gift - it was contracted work @ 36 hours. but the other for Liam Eagen seems to be a
definite 'Thanks' gift .. hbs requested a breakdown of hours worked that would take 3-6 hours to pro<clipped
message>

15:36:58 <m-relay> <p​lowsof:matrix.org> duce but kayaba deemed it to be not required. Koes comment too.. how
do you respond to that https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403#note_22226

15:38:38 <m-relay> <s​needlewoods_xmr:matrix.org> imo "retroactive funding" shouldn't be prohibeted in general
and I agree with kayaba on this quote "I personally believe the CCS should allow retroactive funding, with
discussion on if the work produced offers benefit appropriate to the requested amount."

15:39:57 <m-relay> <m​onerobull:matrix.org> id say the stuff hes been working on was undeniably important for
the project and people have been wanting to get rid of rings for a long time

15:40:10 <m-relay> <p​lowsof:matrix.org> mj-xmr can kick start his ccs career again via retroative funding
proposals

15:40:20 <m-relay> <m​onerobull:matrix.org> its not like he worked on some crap nobody asked for and then
demands a lof ot money for it

15:40:39 <m-relay> <m​onerobull:matrix.org> its not like he worked on some crap nobody asked for and then
demands a lot of money for it

15:40:43 <m-relay> <p​lowsof:matrix.org> monerobull how can ya say 100% of people want this tho

15:40:45 <m-relay> <c​trej:matrix.org> Breakdown of any engineering work is hard,  even more so for code - I
don't think it can be retroactively summarized, and definitely not with the accuracy we want.

15:40:50 <m-relay> <b​tclovera:matrix.org> This is true

15:40:58 <m-relay> <m​onerobull:matrix.org> you dont have to donate if you dont want it

15:41:01 <m-relay> <p​lowsof:matrix.org> 100% of the community

15:42:02 <m-relay> <m​onerobull:matrix.org> arguable the sentiment for movie ccs was abysmal compared to this
proposal

15:42:03 <m-relay> <m​onerobull:matrix.org> and it got moved to funding on the grounds that "you dont have to
donate if you dont support it"

15:42:14 <m-relay> <p​lowsof:matrix.org> when the comments show otherwise, but sitll, overwhelmingly positive
sentiments in the comment section

15:42:18 <m-relay> <c​trej:matrix.org> Moving to funding has literally no downsides, let donors decide if they
want to give retroactive support

15:42:37 <m-relay> <m​onerobull:matrix.org> i would like to hear why movie ccs deserved to go to funding and
why this proposal shouldnt

15:42:56 <m-relay> <b​tclovera:matrix.org> I don’t like “retroactive founding” but in the CCS there have been
“exceptions” and I think maybe this should be one. As Monerobull says, it’s something important for the
project and not a just expensive crap

15:43:50 <m-relay> <c​trej:matrix.org> And I think its an important to set a president that extraordinary dev
work can get paid, even if it doesn't 100% align with all detailed rules ("no retroactive funding" is not eveb
a rule btw)

15:44:11 <m-relay> <p​lowsof:matrix.org> if we approached cypherstack and said "can you beat the price of 41k
to do this research" ahead of time, perhaps they could have given a better deal? we dont know

15:44:46 <m-relay> <p​lowsof:matrix.org> we never had the opportunity

15:44:50 <m-relay> <m​onerobull:matrix.org> had we approached some indie movie studio they might have made a
whole movie about xmr for less than 25k...

15:45:03 <m-relay> <m​onerobull:matrix.org> we never had the opportunity

15:45:04 <m-relay> <c​trej:matrix.org> This kind of research/dev work can not be planned out like this plowsof

15:46:14 <m-relay> <c​trej:matrix.org> Sometimes you have to build on the spark of an idea first, before you
can even explain it well to others

15:46:21 <m-relay> <p​lowsof:matrix.org> actually we do have the opportunity " If someone wishes to point out
the work delivered could've been cheaper delivered by Cypher Stack or similar, I'd be open to reducing the
request."

15:48:36 <m-relay> <p​lowsof:matrix.org> any other talking points? the anti retros are not in attendance hm

15:49:16 <m-relay> <m​onerobull:matrix.org> merge 👍

15:49:21 <m-relay> <b​tclovera:matrix.org> +1

15:50:10 <m-relay> <c​trej:matrix.org> yes merge, let donors decide

15:50:17 <m-relay> <p​lowsof:matrix.org> is serai-dex still going to use some mordinal type stuff if we dont
get FCMP's kayabanerve (is this why your undertook the research?)

15:50:25 <m-relay> <b​tclovera:matrix.org> Where is our friend ofrnxmr ?

15:50:41 <m-relay> <p​lowsof:matrix.org> ofrnxmr is +merge for this, yesterday

15:51:07 <m-relay> <s​needlewoods_xmr:matrix.org> merge

15:51:54 <m-relay> <c​trej:matrix.org> ofrn took some time of after a fight in the events room

15:52:22 <m-relay> <p​lowsof:matrix.org> with 10 mins left lets jump to the next idea

15:52:23 <m-relay> <p​lowsof:matrix.org> c. [Create Educational Content in
Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/406)

15:52:33 <m-relay> <p​lowsof:matrix.org> by Lovera who has proposed a rate of 3.25$/hour

15:53:01 <m-relay> <c​trej:matrix.org> subsidized voluntary work

15:53:04 <m-relay> <p​lowsof:matrix.org> are we breaking any laws here?

15:53:13 <m-relay> <r​ecanman:agoradesk.com> Hello

15:53:15 <m-relay> <b​tclovera:matrix.org> This is my proposal, any questions I will be happy to answer

15:53:17 <m-relay> <p​lowsof:matrix.org> thank you to geonic for pointing this out

15:53:24 <m-relay> <m​onerobull:matrix.org> how did the last ccs go Lovera ?

15:53:53 <m-relay> <m​onerobull:matrix.org> just out of curiosity

15:54:07 <m-relay> <p​lowsof:matrix.org> subscriber count has increased at first glance, would be nice to have
stats on the previous ccs sponsored videos

15:54:19 <m-relay> <m​onerobull:matrix.org> i remember there was also some drama with videos sponsored by cake
or something like that

15:54:19 <m-relay> <c​trej:matrix.org> I would very much like a brief review of the content by someone who
speaks/understands spanish

15:54:45 <m-relay> <b​tclovera:matrix.org> All good 😅 I think 🧐

15:55:19 <m-relay> <r​ecanman:agoradesk.com> 10xmr for that work is unreasonable, it should be a little more

15:55:23 <m-relay> <b​tclovera:matrix.org> Yep, I made a clarification that the sponsored cake videos had
nothing to do with the work proposed in the CCS

15:55:39 <m-relay> <m​onerobull:matrix.org> alright, id say merge

15:55:45 <m-relay> <r​ecanman:agoradesk.com> +1

15:56:04 <m-relay> <r​ecanman:agoradesk.com> Maybe payment should be increased a little

15:56:07 <m-relay> <p​lowsof:matrix.org> the ccs videos are without sponsored ads (however youtube may ad some
cus reasons - but lovera disables them on his end)

15:56:28 <m-relay> <p​lowsof:matrix.org> what if the previous ccs had 0 views on all the videos?

15:56:55 <m-relay> <p​lowsof:matrix.org> i checked and this was not the case of course

15:57:10 <m-relay> <r​ecanman:agoradesk.com> The videos get pretty good traction from what I've seen

15:57:32 <m-relay> <b​tclovera:matrix.org> Well, as I told Geonic, I promised in my first CCS that I would not
raise the price in XMR. So I won’t do it.

15:57:32 <m-relay> <b​tclovera:matrix.org> Also, in Venezuela the salary is $20 a week so lol, I’m fine.

15:58:52 <m-relay> <p​lowsof:matrix.org> i will need to talk to chatgpt as to why such low wages are bad

15:58:53 <m-relay> <p​lowsof:matrix.org> e.g. i am a spanish person who wishes to do the same but i can't
undercut you

15:59:00 <m-relay> <p​lowsof:matrix.org> thus no ccs for me

16:00:10 <m-relay> <p​lowsof:matrix.org> hinto made a proposal of low wages and was told to higher it to
something reasonable

16:00:13 <m-relay> <r​ecanman:agoradesk.com> In my opinion, I don't feel right with merging it, but it seems
that you are insisting

16:00:13 <m-relay> <c​trej:matrix.org> plowsof you are notorious for doing community work off-hours, I can't
undercut that price either

16:00:13 <m-relay> <p​lowsof:matrix.org> job security ++ / not eating for a month if i make a bad move to
compensate

16:00:49 <m-relay> <b​tclovera:matrix.org> I’m fine, guys! Seriously!’s I think 3.5 XMR is a fair sum for the
work to be done.

16:00:49 <m-relay> <b​tclovera:matrix.org> I work ~8 hours but I like what I do.

16:00:50 <m-relay> <b​tclovera:matrix.org> If I really need it, I will increase the fee. Nex CCS? 🤣

16:01:57 <m-relay> <s​needlewoods_xmr:matrix.org> it's hard to judge the impact, but just looking at the
amount of work, this seems more than fair

16:02:21 <m-relay> <b​tclovera:matrix.org> Yes! This

16:02:56 <m-relay> <p​lowsof:matrix.org> thank you for the proposal Lovera, a comment from a native spanish
again e.g. anhdres is always good to have, early days yet, and geonics comment about perhaps teaming up with
the RU (i know you also speak Russian) is food for thought also

16:03:58 <m-relay> <p​lowsof:matrix.org> 1 xmr = 1xmr but slave labour sponsored by the CCS 💀

16:04:36 <m-relay> <p​lowsof:matrix.org> we have reached the hour, any further comments on Loveras proposal?
or AOB?

16:06:35 <m-relay> <b​tclovera:matrix.org> To be honest, a while ago I asked them for help with “Hugo” to
create a kind of Wiki Monero in Spanish but I think they passed me 😅 I will insist again.

16:06:35 <m-relay> <b​tclovera:matrix.org> The community in Russian has an very good Wiki about Monero

16:06:37 <m-relay> <p​lowsof:matrix.org> Lovera also went above and beyond with his previous proposal and
incorporated some Monerokon stuff 👍️ (saved the community some funds instead of paying someone else to do the
same work)

16:07:07 <m-relay> <r​ecanman:agoradesk.com> Hugo isn't too hard to get started with, message me and I can
help you with it

16:07:53 <m-relay> <p​lowsof:matrix.org> events meeting in a little under 1 hours #monero-events:monero.social


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-08-29T10:13:37+00:00
- Closed at: 2023-09-11T08:09:16+00:00
