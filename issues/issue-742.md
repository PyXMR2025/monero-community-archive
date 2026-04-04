---
title: 'Monero Community Workgroup Meeting: Saturday 22nd October 2022 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/742
author: plowsof
assignees: []
labels: []
created_at: '2022-10-17T13:02:00+00:00'
updated_at: '2022-10-22T19:12:53+00:00'
type: issue
status: closed
closed_at: '2022-10-22T19:09:41+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/countdown/fall?iso=20221022T16&p0=1440&msg=Monero+Community+Workgroup+Meeting%3A+Saturday+22nd+October+2022+%40+16%3A00+UTC&font=sanserif)

Moderator: plowsof (until someone complains about COI because ccs coordinator is my idea)

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items: (we may need to focus on CCS ideas first, and then discuss other points with what time is remaining )

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://www.themoneromoon.com/) - [Revuo Monero](https://revuo-xmr.com/)
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [[monero-bash v2.0.0]](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/333)    
  b. [The-Monero-Moon-CCS-Proposal-August2022-John-Foss](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/336)    
  c. [Forgotsudo monero marketplace](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/340)    
  d. [Develop selfhostable monero payment processor](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/345)    
  e. [CCS Coordinator (6 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/348)    
  f. [Gupax: GUI for P2Pool+XMRig](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/350)    
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
        - #745 
        - #743       
  h. Seraphis-migration workgroup 
      - Mon 24th - invite only - koe will be hosting an architecture walkthrough of the seraphis library via [VDO.ninja](http://vdo.ninja/) screenshare. (a recording will hopefully be made for us all)
7. Open ideas time    
      - [Add StealthEX to swappers page](https://github.com/monero-project/monero-site/pull/1917)?  [MoneroTalk interview](https://yewtu.be/watch?v=5Ekf5sqwrL8) [Reddit thread](https://www.reddit.com/r/Monero/comments/y1d0mu/monerotalk_with_stealthex_is_out_now/)
      - Add trocador.app to newly proposed [Aggregators section](https://github.com/monero-project/monero-site/pull/2045) on getmonero
      - XMRstarter [source released](https://gitlab.com/zombie_master/xmrstarter) (proof of concept for a monero-only kickstarter)
8. Confirm next meeting date/time    

Previous meeting including logs #737 

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2022-10-22T19:11:06+00:00
Logs 
```
16:00:28 <plowsof> Meeting time https://github.com/monero-project/meta/issues/742

16:00:44 <plowsof> hello everyone

16:01:09 <monerobull[m]> Hi

16:01:16 <ofrnxmr[m]> Morning

16:01:40 <eudaimon36[m]> hey

16:01:44 <Rucknium[m]> Hi

16:02:26 <plowsof> selsta can't make it today , but hello from his spirit

16:02:51 <plowsof> hinto here?

16:04:02 <plowsof> lets jump into the ccs merge list first. i've been asked by hinto to 'hold off' on closing
monero-bash

16:04:03 <hinto[m]> hello

16:04:15 <plowsof>   a. [[monero-bash v2.0.0]](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/333)

16:05:52 <plowsof> it was decided that this proposal wouldnt go to funding because there wasn't enough
interest / doubts about it being useful enough. the request is to hold-off and keep this open. what do we
think? leave it open?

16:06:34 <hinto[m]> yes, I'd like to focus on gupax for now but I still want to work on monero-bash afterwards
if possible

16:07:14 <ofrnxmr[m]> I'm in favor if leaving open - or closing and reopening once gupax is completed

16:07:14 <Rucknium[m]> IMHO, leave it open, but make it so it doesn't appear on the Ideas page for now

16:07:30 <monerobull[m]> I don't think anyone has something against letting it sit there for a bit

16:07:45 <monerobull[m]> s/there for a bit/unmerged/

16:07:57 <monerobull[m]> s/there/unmerged/

16:08:05 <plowsof> ok we can agree on this then ^

16:08:14 <eudaimon36[m]> ofrnxmr[m]: agreed!

16:09:18 <plowsof> lets talk about moneromoon again - note : i have not attempted to contact him personally
about this meeting since the comment on his proposal idea 1 month ago. he has since been active on
twitter/reddit account

16:09:23 <plowsof> b. [The-Monero-Moon-CCS-Proposal-August2022-John-Foss](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/336)

16:09:29 <hinto[m]> Rucknium:  is there a way to hide it without deleting the proposal itself?

16:10:13 <althea_[m]> eudaimon36[m]: I agree with this

16:11:36 <plowsof> what shold we do with moon? hold off? talk about a decision yes/no?

16:11:40 <ofrnxmr[m]> Im against Moon's proposal. Requested view keys to see how much money he makes from
donations on the site. I feel news outlets should be finding other sources if income post-startup. Moon seems
to have unreported revenue steams.

16:11:40 <ofrnxmr[m]> Quality of the newsletter is mostly an aggregator. Not often if ever breaking news

16:11:46 <Rucknium[m]> hinto: I think so, but I don't remember how to

16:12:28 <plowsof> i'll make sure luigi knows we want to 'hide' it

16:12:43 <ofrnxmr[m]> Anyone else have input in moneromoon ?

16:12:43 <ofrnxmr[m]> Rates are extremely high for literally linking to observer in some cases

16:12:59 <eudaimon36[m]> Yea, I lean that way as well

16:14:10 <plowsof> my main issue was the lack of proof reading - so if moon corrected the typos in his ccs
proposal and said 'he would make sure to proof read / put more effort into it ' then i would reconsider (i
just doubt that he can compete with monero observer in terms of literacy skills)

16:14:11 <ofrnxmr[m]> The fact that hebsays moon dies without ccs makes me feel like doesnt really care to
try.

16:14:11 <ofrnxmr[m]> He buys twitter followers though, Lol. 🤔

16:14:54 <ofrnxmr[m]> Proof reading isnt necessary when youre just reading observer while you write your
newsletter

16:14:59 <plowsof> i think we need to let him respond to everything and hold off?

16:15:19 <monerobull[m]> Observer literally makes really high quality monthly roundups for everything that's
going on

16:15:33 <ofrnxmr[m]> Can someone ping him

16:16:20 <ofrnxmr[m]> He didnt respond to my request for view keys on GitLab (twice)

16:16:25 <monerobull[m]> So I'm not sure how useful a weekly newsletter that can't sustain itself is when we
already have observer and the one by rotten

16:16:28 <plowsof> johnfoss68: johnfoss68 - i have not put any effort to make sure he was aware / here for
this meeting (other than publicly posting this here/reddit)

16:17:05 <monerobull[m]> Newsletter writer should kinda figure out when there's a community meeting 🤔

16:17:14 <ofrnxmr[m]> Hahahaha

16:17:30 <ofrnxmr[m]> They will find out after they read observer

16:17:30 <plowsof> is it fair for him to put out a statement first - and then we must decide Yes/No ?

16:17:36 <monerobull[m]> Kek

16:17:59 <monerobull[m]> plowsof: Give it a deadline of EOY

16:18:00 <ofrnxmr[m]> His statement was basically fund me or gbye moon.

16:18:15 <ofrnxmr[m]> EOD

16:18:16 <Rucknium[m]> Isn't the proposal itself his statement?

16:18:34 <monerobull[m]> It really is isn't it

16:18:59 <ofrnxmr[m]> Id say close pending an update before EOD

16:19:17 <plowsof> hide it and wait for response?

16:19:20 <ofrnxmr[m]> No word from him, close it. Makes a good arguement we can push back to next meeting... ?

16:19:48 <plowsof> he could literally say ' im taking creative writing classes now and im going to proof read
everything ' and i'd support

16:20:02 <ofrnxmr[m]> Like afganistan ccs, no interest from proposer

16:20:13 <ofrnxmr[m]> plowsof: He can open a new ccs when he can do journalism

16:20:49 <plowsof> his fans are not here at the moment but he has them, so we must give hima  chance still

16:21:09 <ofrnxmr[m]> But thats my vote.

16:21:10 <ofrnxmr[m]> Close EOD

16:21:11 <plowsof> hide - final decision pending some kind of hail mary statement before EOY?

16:21:25 <ofrnxmr[m]> Im voting end of day

16:21:43 <ofrnxmr[m]> The newsletter is weekly. Not waiting months for a response

16:22:08 <plowsof> who wants to close it now?

16:22:25 <eudaimon36[m]> close it

16:22:28 <ofrnxmr[m]> Me

16:22:53 <plowsof> i just think its a 'highly contested' proposal and we should give one more chance ( i vote
to close it now though)

16:22:56 <monerobull[m]> Might as well

16:23:13 <hinto[m]> I think allowing for a response before final decision is fair

16:23:30 <plowsof> i just know for a fact that he has supporters who are not here right now and we must be
fair

16:24:02 <ofrnxmr[m]> hinto @hinto.janaiyo:matrix.org:  are you ok with end of day? End of week?

16:24:02 <ofrnxmr[m]> I dont think waiting any longer makes sense.

16:24:25 <merope> Hey everyone - just a quick update on SolOptXMR: I'm pretty close to finishing Milestone 2,
and mj has already completed most of his work for M3+M4 already, so after that it's pretty much just my part
of M3+M4 left. Unfortunately there have been some delays on my part (had some personal stuff to deal with in
the last few months), so I doubt that I'll be able to finish my part in time for the original deadline, but
rest assured that I (we) intend to

16:24:25 <merope> complete the project in full

16:24:27 <plowsof> hiding it - requesting hail mary statement before EOY seems fair - imagine there where an
equal amount of people calling for it to be funded right now - we must compromise

16:24:35 <ofrnxmr[m]> He's a journalist he should know about this conversation ASAP. Lol

16:24:59 <plowsof> thank you endor00

16:25:27 <plowsof> shall we touch on the next one

16:25:34 <ofrnxmr[m]> Thanks endor 👍

16:25:41 <ofrnxmr[m]> Wait

16:26:01 <ofrnxmr[m]> Consensus is close pending response by... end of week? 7 days from now

16:26:04 <ofrnxmr[m]> Or end of day?

16:26:49 <plowsof> i know atleast 3 people who would say put it to funding

16:27:20 <plowsof> 4* if he lowers his rates

16:27:46 <plowsof> so i will do my best to contact him after this meeting

16:28:28 <plowsof> for sure hiding it though

16:28:46 <ofrnxmr[m]> Ok well seems meeting consensus is close. These other people need to come forward at
some point

16:29:14 <hinto[m]> a week/month seems like a fair amount of time

16:29:54 <eudaimon36[m]> hinto[m]: agreed

16:29:54 <plowsof> yes its a nice compromise

16:29:55 <plowsof> ready to move on?

16:29:57 <ofrnxmr[m]> I vote week

16:30:16 <ofrnxmr[m]> Yes

16:30:23 <plowsof> ill do my best in contacting him

16:30:24 <plowsof>   c. [Forgotsudo monero marketplace](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/340)

16:30:48 <plowsof> the last meeting we seemed to agree on letting them resubmit wiht only 1 milestone Web of
trust

16:31:08 <plowsof> theyve commented on their proposal that theyre considering it, so i think we can agree to
leave this up

16:31:53 <plowsof> ill follow up/contact them too

16:32:15 <ofrnxmr[m]> I missed last meeting so ill abstain

16:32:16 <ofrnxmr[m]> I initially voted against, but if splitting into other ccs, close

16:32:37 <plowsof> they have been thumbed down but there are several people who support the proposal fully too
(for promoting circular economy and such)

16:32:51 <ofrnxmr[m]> Rebmsubmit the new ccs as a new proposal, no?

16:32:51 <plowsof> milestone 1 WoT only seems to be the path of least resistance (as we don;t know the team
very well)

16:33:23 <plowsof> editing it would be fine

16:33:44 <ofrnxmr[m]>  Leave it up

16:33:44 <plowsof> yes

16:34:02 <ofrnxmr[m]> I remember this one, I had an idea for a better oath forward - this was the one I
messages you about that I forgot the name of

16:34:03 <ofrnxmr[m]> Next?

16:34:21 <plowsof>  d. [Develop selfhostable monero payment processor](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/345)

16:34:53 <monerobull[m]> No need, first time contributing and on top wants to be paid upfront 👎

16:34:53 <plowsof> i'd say close this one ( MoneroPay have been in contact with me and are going to make their
own ccs proposal too.)

16:35:25 <monerobull[m]> Is that "merchant"?

16:35:25 <plowsof> yes

16:35:25 <monerobull[m]> Ok those are awesome

16:35:26 <plowsof> not a payment processor(*

16:35:42 <ofrnxmr[m]> Closssseeee

16:35:54 <ofrnxmr[m]> "Another payment processor" - ooo123

16:35:58 <monerobull[m]> We at magic had a dead "payment" crypto from 2018 ask for money

16:36:39 <plowsof> we have 24~ mins left so im going to put gupax before my personal idea

16:36:54 <plowsof>   f. [Gupax: GUI for P2Pool+XMRig](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/350)

16:36:55 <monerobull[m]> Yes. Gupax. Pls. 100% support

16:37:30 <ofrnxmr[m]> Yea, go gupax considering bash is stalled to allow Gulax we already decided yes

16:37:31 <plowsof> gupax was added to the p2pool readme . it is currently the only GUI for p2pool / xmrig and
has had support from reddit / matrix

16:37:44 <ofrnxmr[m]> Next

16:37:44 <Rucknium[m]> People have been asking for a user-friendly way to use p2pool for over a year.

16:38:02 <plowsof> put to funding gupax ? yes

16:38:02 <ofrnxmr[m]> Rucknium[m]: Termux node is kinda friendly too 😝

16:38:09 <monerobull[m]> It's literally what we need for p2pool to grow

16:38:13 <ofrnxmr[m]> Yes

16:38:49 <plowsof> alright lets get aggresive and talk about my idea

16:38:57 <ofrnxmr[m]> Fuck your idea

16:39:00 <ofrnxmr[m]> Haha

16:39:03 <ofrnxmr[m]> Lets go

16:39:11 <plowsof>   e. [CCS Coordinator (6 months)](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/348)

16:39:58 <ofrnxmr[m]> I am requesting you change the rates to the original 3 months / 69 xmr and add
significantly more gui work

16:40:01 <monerobull[m]> What's the status tldr?

16:40:16 <Rucknium[m]> The current dev/researcher experience with the CCS is not good. Talented people are
more likely to just not bother

16:40:19 <plowsof> its a new 'role' and we're getting 'plowsofs' other contribs. too (site ~ gui/cli/rpc
testing / liaison to core and such) so needs opinions

16:41:19 <plowsof> the status of the proposal is : presented it to reddit asking 20 hours a week ~ got called
a money grabbing scammer ~ rbrunner suggested to cut the effort in half and double the time frame which i have
done

16:41:27 <monerobull[m]> So this is more than ccs manager now?

16:41:56 <monerobull[m]> fancy "Secretary" that generally helps core be more efficient?

16:42:01 <ofrnxmr[m]> It includes all things plowsof

16:42:25 <eudaimon36[m]> Agreed, yes, change it to 3 months

16:42:45 <Siren[m]> Plowsof is my favorite secretary

16:42:54 <plowsof> yes (and also working on site / gui PRs)

16:43:19 <plowsof> its literally 'plowsof to exist' as normal

16:43:36 <althea_[m]> I’m in favor of changing it to 3 months

16:43:37 <ofrnxmr[m]> I spoke with selsta and selsta would like to see 3/69 as well with increased gui work

16:43:47 <monerobull[m]> I said before i wouldn't comment bcs potential "conflict of interest" with magic but
this is a different role now and i fully support it

16:44:27 <plowsof> except put more effort into the ccs process before / during / after - jberman suggests
looking into getting 'hard problems' funded (for this i would need to work closely with MRL members)

16:44:38 <hinto[m]> +1 plowsof has already been doing this role for free for a while, I'm also in favor of
increasing rate/shortening timespan

16:45:05 <selsta> there's so much to do with the gui and a second person to help me with testing would be
awesome

16:45:16 <nioc> whatever changes are decided for the plowsof CCS, other than not supporting it, I support the
CCS

16:45:28 <nioc> the spirit of selsta has arrived  \o/

16:45:41 <Rucknium[m]> There are very few "the buck stops here" roles in Monero, which causes things to slip
through cracks continuously. This CCS would close a lot of those cracks.

16:45:45 <plowsof> so 6 -> 3 months and increasing / restructuring hours?

16:45:48 <monerobull[m]> Ok so that plowsof doesn't have to say it: change to 3 months and move forward to
funding

16:46:04 <ofrnxmr[m]> Yes please

16:46:11 <ofrnxmr[m]> Move to funding

16:46:30 <selsta> nioc: hi :P

16:46:30 <eudaimon36[m]> yes

16:46:53 <ofrnxmr[m]> Selsta made it :D

16:46:56 <plowsof> ive included a untimely death clause - but i am in good health , do not worry

16:47:26 <eudaimon36[m]> lol, Jesus...

16:47:37 <nioc> what about timely death?

16:47:49 <eudaimon36[m]> haha

16:47:55 <plowsof> till death do us part

16:48:39 <ofrnxmr[m]> Just over 10 mins left. Ready to move on?

16:48:58 <monerobull[m]> Oh yeah can we put a auto-death on proposals that have been funded but author MiA
that pays out locked funds to general fund after like 2 years

16:49:06 <plowsof> i would like a public apology from geonic for stating that my contributions to site / gui /
ecosystem are not valuable to this community

16:49:29 <ofrnxmr[m]> On behalf of Geo, I apologize

16:50:15 <ofrnxmr[m]> Ok, next on the list iss

16:50:47 <plowsof> alright, i will modify and double check with everyone some time this week thanks for the
support

16:51:03 <plowsof> next on the list is....

16:51:47 <plowsof> mainly some bullet points to introduce to people , unless monerobull has outreach
activities he wants to share?

16:51:57 <monerobull[m]> Hehe

16:52:58 <monerobull[m]> It's not technically really outreach. I wanted cool monerochan merch so I'm making
some. This will be in the form of a limited run of plushies

16:53:45 <monerobull[m]> I want to thank reddit for basically funding this project with their nfts
consistently paying out 20x

16:54:14 <Rucknium[m]> I completed Milestone 1 of "OSPEAD - Fortifying Monero Against Statistical Attack"
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255#note_18750

16:54:25 <Siren[m]> <plowsof> "i'd say close this one ( MoneroP..." <- Hi, yes. We're working on a checkout
system. Where you can use the API or the panel to generate checkout pages. This is what the PoC looks like:
https://bin.kernal.eu/2/metronero.png

16:55:30 <monerobull[m]> is Metronero the merchant from reddit?

16:55:36 <plowsof> monerobull of monerosupplies.com (pls update certs ;_;)

16:55:37 <Siren[m]> No

16:56:17 <plowsof> the merchant on reddit is closed source at the moment

16:56:20 <monerobull[m]> plowsof: Https works and checkout enforces it, would rather not touch and break it
more :P

16:56:31 <plowsof> that was mainly a Point of sale HotShop alternative

16:56:54 <monerobull[m]> Is grampy still alive?

16:57:09 <monerobull[m]> Don't think I've seen them in quite some time

16:57:15 <plowsof> yes , active yesterday i believe

16:57:26 <plowsof> god willing he is in good health

16:57:40 <plowsof> his next ccs will need an untimely death clause

16:58:02 <plowsof> quickly introducing 3 things:

16:58:15 <plowsof> - [Add StealthEX to swappers page](https://github.com/monero-project/monero-
site/pull/1917)?  [MoneroTalk interview](https://yewtu.be/watch?v=5Ekf5sqwrL8) [Reddit thread]

16:58:23 <plowsof> Add trocador.app to newly proposed [Aggregators section](https://github.com/monero-
project/monero-site/pull/2045) on getmonero

16:58:29 <Siren[m]> Siren[m]: The PoC for metronero is here:

16:58:29 <Siren[m]> https://metronero.digilol.net

16:58:29 <Siren[m]> We coded it up in 4 days for university and we actually would like to make a CCS proposal
to rewrite it for production use. What do you guys think?

16:58:35 <plowsof>       - XMRstarter [source released](https://gitlab.com/zombie_master/xmrstarter) (proof of
concept for a monero-only kickstarter)

16:58:47 <Siren[m]> * The PoC for metronero is here (it's stagenet):

16:58:47 <Siren[m]> https://metronero.digilol.net

16:58:47 <Siren[m]> We coded it up in 4 days for university and we actually would like to make a CCS proposal
to rewrite it for production use. What do you guys think?

16:58:54 <plowsof> matrix users please forgive me for the formatting

16:58:59 <Stnby[m]> > <@siren:kernal.eu> The PoC for metronero is here:

16:58:59 <Stnby[m]> > https://metronero.digilol.net

16:58:59 <Stnby[m]> > We coded it up in 4 days for university and we actually would like to make a CCS
proposal to rewrite it for production use. What do you guys think?

16:58:59 <Stnby[m]> Its also stagenet

16:58:59 <monerobull[m]> <plowsof> "mainly some bullet points to..." <- Oh yeah and i made a video for
trocador this week

16:59:29 <monerobull[m]> How about we list that on getmonero /s

16:59:49 <ofrnxmr[m]> Ive not used stealthex or trocador

16:59:55 <plowsof> looks handy/easy to use. and this StealthEX - not heard much about it until their
monerotalk interview / (they are sponsoring them for x months) and they want to be added to getmonero as a
swapper

16:59:56 <ofrnxmr[m]> But trocador is Morpheus?

17:00:00 <monerobull[m]> Yea

17:00:04 <SerHack> Thanks stnby[m], will test it

17:00:40 <ofrnxmr[m]> Id hold off on stealthex for community trust / real reviews from users

17:01:01 <ofrnxmr[m]> Morpheus trocador - monerubull can vouch ?

17:01:03 <plowsof> hello serhack the father of all monero payment processors who also has an amazing site
https://serhack.me/articles/story-behind-alternative-genesis-block-bitcoin/

17:01:27 <monerobull[m]> ofrnxmr[m]: I did 2 15$ swaps and didn't get scammed?

17:01:34 <ofrnxmr[m]> Right

17:01:50 <plowsof> so stealthex need reviews , and also trocador

17:01:51 <monerobull[m]> But yes, Morpheus is behind it

17:01:53 <SerHack> hi plowsof! Thanks for sharing the article, currently focused on finishing MM content as
soon as possible.

17:02:44 <ofrnxmr[m]> Ok, I feel more comfortable using it if its morph and bull has used it. Perhaps have
some reviews for the next meeting

17:03:31 <monerobull[m]> ofrnxmr[m]: https://youtu.be/QYfUSImvRnQ if you need any guidance 😜

17:03:31 <ofrnxmr[m]> Thats the hour.

17:03:31 <ofrnxmr[m]> What did we have left?

17:04:04 <plowsof> Mon 24th - invite only - koe will be hosting an architecture walkthrough of the seraphis
library via [VDO.ninja](http://vdo.ninja/) screenshare. (a recording will hopefully be made for us all)

17:04:16 <plowsof> for the big brains (not myself)

17:04:41 <plowsof> shall we call the meeting then?

17:04:41 <monerobull[m]> Repost that message to MRL but I'm sure they already know about it

17:05:45 <plowsof> ok then, thank you everyone for attending the meeting x


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2022-10-22T19:12:53+00:00
continued:
```
17:05:53 <monerobull[m]> Thank you for hosting 
17:07:29 <ofrnxmr[m]> Thank you, Sir 
17:09:21 <hinto[m]> Siren: this is interesting, any more pictures or a git?
17:09:47 <hinto[m]> seems like it's locked behind registration
17:13:30 <Morpheus[m]> <ofrnxmr[m]> "But trocador is Morpheus?..." <- Yes I made it haha
17:15:17 <Morpheus[m]> The main idea is to work as a privacy layer, preventing exchanges from fingerprinting you and from tracing your ip, and at the same time finding you the best rates
17:17:31 <Morpheus[m]> We will deliver an API system that works via TOR 
17:18:06 <Morpheus[m]> And a widget that runs the trade without any javascript, so other javascript-free websites can monetize
17:20:25 <Siren[m]> <hinto[m]> "Siren: this is interesting..." <- The source code is here but the code quality is obviously bad: https://gitlab.digilol.net/moneropay/metronero-poc
17:20:25 <Siren[m]> Both the frontend and the backend needs a rewrite. It's also JS free.
17:23:15 <Morpheus[m]> <ofrnxmr[m]> "Ok, I feel more comfortable..." <- If you guys review it, feel free to send me the links, as we look forward to improving the service 
17:34:34 <hinto[m]> Siren: thanks, will try setting it up
17:34:59 <hinto[m]> I was going to ask if it used JS lol, I've been looking for something like this
17:37:10 <Siren[m]> hinto[m]: Oh no I don't suggest doing this. It's not for production use. There are possibly bugs and poor error handling. But we will rewrite it.
17:39:40 <hinto[m]> just for testing
17:39:58 <hinto[m]> would support a CCS for full development though
17:40:09 <hinto[m]> I hate having to unblock JS for payments 
17:40:09 <Siren[m]> Glad to hear that
17:42:27 <Stnby[m]> We use Refresh HTTP headers as of now, but you can also achieve an auto refresh with meta tags
17:43:16 <Stnby[m]> I guess people who require JS for payment processors spent exactly 0 hours reading HTTP/HTML standards
17:44:03 <Siren[m]> We will in the future support turning this feature off so the merchant can choose to support JS themselves and refresh using JS
17:44:14 <Siren[m]> But by default it's no JS
17:55:19 <hinto[m]> I may or may not have known a refresh header existed but very cool
```

# Action History
- Created by: plowsof | 2022-10-17T13:02:00+00:00
- Closed at: 2022-10-22T19:09:41+00:00
