---
title: 'Monero Community Workgroup Meeting: Saturday 11th February 2023 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/791
author: plowsof
assignees: []
labels: []
created_at: '2023-02-02T20:13:37+00:00'
updated_at: '2023-02-15T23:04:33+00:00'
type: issue
status: closed
closed_at: '2023-02-15T23:04:33+00:00'
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
    - [Feather Wallet v2.30](https://featherwallet.org/changelog/)
    - [p2pool v3.0](https://github.com/SChernykh/p2pool/releases/tag/v3.0) / [GUPAX](https://gupax.io/)
    - https://github.com/monero-project/monero/pull/8724 jeffro256
    - https://github.com/monero-project/monero/pull/8733 tevador
    - [Seraphis & Jamtis FAQ](https://www.reddit.com/r/Monero/comments/10ug1zt/seraphis_and_jamtis_faq/) rbrunner
    - [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100#issuecomment-1423154798)
    - https://kuno.bitejo.com/ Anarkiocryptos first draft of a fair kickstarter alternative!
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [Help an independent film featuring Monero get to the Oscars™!](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371)
Core has decided no rules are being broken (as the ccs is for marketing, not the movie itself)
  d. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/375)    

[Animated Videos](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/308):
- [script 1](https://gitlab.com/monero-videos/monero-adoption-animated-videos/-/blob/main/Video%201%20Script%3A%20Why%20Use%20Monero%20for%20Commerce%3F.md)
- [updated story board](https://docdro.id/wkLPG5W) 
- [updated clip](https://www.reddit.com/r/Monero/comments/10zi0wn/new_animated_videos_animation_example/)

Endor Solopt Update (profitability.py) - https://github.com/mj-xmr/SolOptXMR/issues/151#issuecomment-1426619628

Valldrac Molly Update

Delayed:
  a. [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358)    

6. [Resolve WIP list](https://github.com/plowsof/ccs-wip-list/issues)
  a. https://github.com/plowsof/ccs-wip-list/issues/1
  b. https://github.com/plowsof/ccs-wip-list/issues/2
7. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
8. Open ideas time    
  - donor or donator ? 
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/785)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-02-13T23:08:28+00:00
Close XMRsale / Close Monero Archive
Need more time to discuss / review the acceptXMR suggestion
Dispersing the remaining funds to other proposals (if suggestion(s) are rejected)
acceptXMR will benefit from likely users of it to review the milestones.

The people who have down voted the movie proposal have not changed their opinion: the film being freely available after is a 'nice to have' and has been assured.. possible screening at monerokon is being discussed

Logs 
```
16:00:05 <plowsof11> Meeting time https://github.com/monero-project/meta/issues/791

16:00:23 <plowsof11> 2. Greetings

16:00:24 <plowsof11> hello

16:00:28 <ofrnxmr[m]> Greetings

16:00:59 <geonic> hola

16:01:32 <Lovera[m]> Hola

16:01:40 <geonic> :)

16:01:44 <BusyBoredom[m]> Hey

16:02:16 <plowsof11> would anyone like to spam some community highlights / interesting things while everyone
rolls in

16:02:28 <Rucknium[m]> Hi

16:02:53 <blankpage[m]> Hello

16:02:55 <ofrnxmr[m]> Most people get to stay in the bus now

16:03:08 <ofrnxmr[m]> Hey cancelling us now! I say

16:03:08 <plowsof11> ive got a bunch linked in the meeting issue (tx extra discussions.. [Feather Wallet
v2.30](https://featherwallet.org/changelog/) [p2pool
v3.0](https://github.com/SChernykh/p2pool/releases/tag/v3.0) / [GUPAX](https://gupax.io/) ... rpc pay in the
process of being removed

16:03:10 <ofrnxmr[m]> Try*

16:03:24 <plowsof11> ofrnxmr you contacted nanopool or something 👀

16:03:34 <jwinterm> o/

16:03:40 <Rucknium[m]> People are discussing restricting tx_extra again: https://github.com/monero-
project/monero/issues/6668

16:03:40 <Rucknium[m]> It is at 141 comments now

16:04:21 <Rucknium[m]> tx_extra will be discussed at the next Monero Research Lab meeting

16:04:26 <plowsof11> the btc ordinal thing sparked it up again , interesting to follow with possible huge
changes in the future

16:04:57 <Lovera[m]> > <@rucknium:monero.social> People are discussing restricting tx_extra again:
https://github.com/monero-project/monero/issues/6668

16:04:57 <Lovera[m]> > It is at 141 comments now

16:04:57 <Lovera[m]> We need to remove it

16:05:04 <plowsof11> a nice draft of a crowd funding site from anarkiocrypto https://kuno.bitejo.com/  👍️

16:05:06 <hinto[m]> hello

16:05:18 <plowsof11> selstas ccs porposal funded, and loveras almost! 🥳

16:06:52 <plowsof11> monerokon tickets? contact ajs "monerokon store is ready. if anyone wants to buy a ticket
and help us test the system before going live, send me a DM" thanks to digilol+siren+stnby for playing a huge
role in that

16:07:16 <ofrnxmr[m]> Just post the darn link

16:07:40 <Siren[m]> please test the store first 😅

16:07:53 <Siren[m]> someone anyone

16:08:09 <Stnby[m]> ofrnxmr[m]: Will you buy it?

16:08:16 <plowsof11> also ive been testing a PR from rbrunner/jberman to speed up wallet refresh times (handy
if some meany starts spamming our mempool .. decreases fetching mempool from a node by a huge %
https://github.com/rbrunner7/monero/pull/4

16:08:33 <monerobull[m]> Hi

16:09:07 <plowsof11> is it time to roll out the red carpet yet and jump into the ccs ideas

16:09:16 <ofrnxmr[m]> Plowsof, that research may be totally skewed with the faster block templates

16:09:38 <ofrnxmr[m]> Not the txpool is consistently cleared out each block, instead of every 2+ blocks

16:09:39 <blankpage[m]> I'll buy a ticket if the link can be DMed to me, for testing

16:09:47 <plowsof11> i think it is unrelated, just 'give me your mempool sir'

16:09:53 <blankpage[m]> Forgot to put myself on the waiting list

16:10:06 <plowsof11> but yes could be

16:10:27 <plowsof11> ok

16:10:29 <ofrnxmr[m]> We were waiting for Monerobull. Good to go

16:10:38 <plowsof11>   a. [Help an independent film featuring Monero get to the
Oscars™!](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371)

16:10:44 <geonic> yay

16:10:56 <geonic> so help or no help? :p

16:11:17 <ofrnxmr[m]> People have comments or want to vote?

16:11:24 <plowsof11> just to clarify its "not breaking the rules" as per cores statement
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371#note_20653

16:12:19 <jwinterm> I wanna buy tix

16:12:22 <plowsof11> i suppose the main uestion is , those who havnt voted on the gitlab issue, do you want to
vote open/close? those who have downvoted, is there anything that would make you change your decision?

16:12:32 <ofrnxmr[m]> Stnby:

16:12:47 <monerobull[m]> plowsof11: Community Edition with permissive license

16:12:48 <ofrnxmr[m]> Those of is in here voting, are known on GitLab

16:12:52 <plowsof11> nice jwinterm send pm to ajs_

16:13:12 <jwinterm> will do via matrix rn

16:13:48 <plowsof11> all of geonics movies are open after the fact iirc, its just the oscars run-up requires
it to be totes private

16:13:59 <geonic> true

16:14:01 <monerobull[m]> Many who vote yes on Gitlab have never participated in any other ccs stuff

16:14:01 <midipoet> has the option of showing the movie at a private MoneroKon screening been discussed?

16:14:38 <geonic> it's been offered. I don't think it's been discussed by the organizers

16:14:52 <ofrnxmr[m]> The current milestones are written as

16:14:52 <ofrnxmr[m]> 1. "Take me to the dance"

16:14:52 <ofrnxmr[m]> 2. "If I walk in the door, pay me foe second half"

16:14:52 <ofrnxmr[m]> Both milestones are in advance, with no room for failure. (though not much can be done
about that considering the money is to be dished out to other partied)

16:15:01 <plowsof11> there will be an events meeting in 2 hours btw

16:15:08 <midipoet> MoneroKons and DefCons in the past have screened movies (and also paid for the
priviledge).

16:15:11 <ajs_[m]> there is a small cinema close by the monerokon venue

16:15:20 <ajs_[m]> kinda cool

16:15:22 <plowsof11> can we not just watch it on geonics phone

16:15:27 <geonic> lol

16:15:50 <geonic> just worry that ppl might be disappointed if they're expecting to see a "Monero movie"

16:16:03 <ofrnxmr[m]> My vote remains a no. Maybe split ccs up into

16:16:03 <ofrnxmr[m]> "Take me to the dance"

16:16:03 <ofrnxmr[m]> And

16:16:03 <ofrnxmr[m]> "Take me to the Oscars"

16:16:12 <monerobull[m]> As head of program for monerokon, we will watch it on geonics phone

16:16:32 <geonic> but if it's marketed correctly why not. I have a nice phone.

16:16:44 <BusyBoredom[m]> I don't really buy the advertising value, so I wont be contributing to it but I
don't feel strongly enough to vote to close it.

16:16:58 <midipoet> from my understanding people enjoyed the movie experience at the conferences/events,
regardless of content (though with expectation of quality)

16:17:18 <blankpage[m]> Isn't the whole point that nomination is guaranteed for a certain amount of bribes? So
really it is

16:17:18 <blankpage[m]> 1) pay bribe

16:17:18 <blankpage[m]> 2) marketing for hopefully winning

16:17:27 <ofrnxmr[m]> 2 isnt marketing

16:17:31 <hinto[m]> BusyBoredom: agreed

16:17:33 <ofrnxmr[m]> 2 is pay me for paying bribe

16:17:34 <jwinterm> lol plowsof11

16:17:53 <geonic> blankpage[m]: yeah, it's a pay-to-play system

16:17:55 <monerobull[m]> Regarding marketing: name the last Oscar winning short film you've heard about

16:18:09 <ofrnxmr[m]> Nwver

16:18:09 <Siren[m]> I vote close

16:18:31 <geonic> tbh there's not a lot of overlap between the people in this room and the general public

16:18:33 <plowsof11> a trailer (highlighting the monero parts) has been discussed. as it stands, many peoples
will be sad if it goes to funding, and if it does not go to funding. thats why i ask for how to change the nos
into a yes , if possible, so the proposor can try to please

16:19:10 <ofrnxmr[m]> I vote close and come back with a ccs that isnt misleading, and that offers value

16:19:10 <geonic> but most people can't name a movie that came out last year either, so there's that. maybe
top gun or avatar...

16:19:13 <blankpage[m]> My opinion is the same as BusyBoredom in this case

16:19:19 <plowsof11> a trailer + monerokon / topia screening has been mentioned

16:19:28 <monerobull[m]> GF can't contribute and community needs to be able to freely watch it after the
Oscars

16:19:28 <midipoet> why will people be sad if it goes to funding?

16:19:39 <midipoet> What's the outstanding issue?

16:19:52 <ofrnxmr[m]> monerobull[m]: We paid for 25k worth of viewings

16:19:58 <geonic> monerobull[m]: agree on both counts

16:20:16 <Lovera[m]> monerobull[m]: +1 agree here

16:20:20 <ofrnxmr[m]> midipoet: Because it sets terrible precedent

16:20:33 <geonic> ofrnxmr[m]: how is the CCS misleading?

16:20:39 <midipoet> ofrnxmr[m]: ok. so explain what precedent it sets?

16:20:49 <ofrnxmr[m]> 12k upfront for ventures that barely resemble anything remotely monero

16:21:04 <Siren[m]> midipoet: non-free media, offers no marketing value, realistically won't win an oscars but
maybe smaller festival awards

16:21:11 <plowsof11> so the GF can't contribute , ok, and it will be freely available like geonics other
movies ?

16:21:24 <ofrnxmr[m]> A ccs like this only works up front.. but for that, id expect more value coming from it

16:21:27 <monerobull[m]> Not on Vimeo

16:21:40 <Siren[m]> also this proposal have been pushed to people a lot

16:21:46 <Siren[m]> I don't like pushy-ness

16:21:47 <monerobull[m]> Only available on Vimeo is like it's not free 😆

16:21:56 <geonic> monerobull[m]: torrents ok?

16:22:00 <midipoet> ofrnxmr[m]: the boat we stuck a logo on, did represent Monero?

16:22:07 <Stnby[m]> Siren[m]: Conracted a bunch if people in private lmao

16:22:20 <blankpage[m]> Torrents ❤️

16:22:22 <ofrnxmr[m]> midipoet: It had a logo on it

16:22:30 <michaelizer[m]> Didn't he say it will be publicly available after the festivals?

16:22:39 <plowsof11> so if geonic adds to the ccs in big letters ' this will be freely available after oscar
run (not on vimeo but on odysee) - GF dont donate, im releasing a trailer ' lovera and monterobull will vote
yes?

16:22:43 <Stnby[m]> Please share pics of XMR sailboat

16:22:45 <midipoet> Siren[m]: it's free post-festival, marketing value is still debateable.

16:22:53 <Stnby[m]> I am interested

16:22:56 <plowsof11> oh and screening at monerokon / topia or just one ?

16:22:59 <midipoet> ofrnxmr[m]: the movie also has a logo in it

16:23:16 <ofrnxmr[m]> In the credits? Lol

16:23:18 <Siren[m]> midipoet: I don't care I can't watch it. The plot itself sounds very problematic.

16:23:37 <midipoet> Siren[m]: the plot? It's a movie. Entertainment

16:23:38 <ofrnxmr[m]> The logo on a boat / blimp is the main feature. Cmon now

16:23:46 <geonic> can't win them all. does the CCS have to literally please everyone in the community to move
forward?

16:23:49 <jwinterm> I don't see the issue for it going to funding at this point - if you think it's dumb then
just don't contribute, right?

16:23:50 <ofrnxmr[m]> midipoet: ITS ABOUT A KID DYING

16:23:52 <Siren[m]> midipoet: based on a dead child

16:24:06 <geonic> jwinterm: that was my understanding of crowdfunding too

16:24:10 <plowsof11> geonic no it doesnt have to please everyone, but if you pretend like yo ucare its
advantagous

16:24:19 <midipoet> ofrnxmr[m]: located where most sponsorships and affiliations go. Where else would you want
it? In the subtitles?

16:24:22 <ofrnxmr[m]> jwinterm @jwinterm:libera.chat:  then we might as well stop voting in anything

16:24:25 <ofrnxmr[m]> And just let every ccs through

16:24:35 <ofrnxmr[m]> midipoet: In the movie

16:24:55 <jwinterm> ofrnxmr[m]: there is precedent for funding a monero logo on a sail boat sail in one race,
no?

16:24:59 <jwinterm> what's the diff?

16:25:03 <midipoet> ofrnxmr[m]: so now we don't want to allow it to go to funding, cause a person dies in the
movie, or because it's based on a sad story?

16:25:04 <Siren[m]> midipoet: I want "Monero" mentioned in the dialogue and that the fact that Monero is
digital should be implied. It is misleading otherwise.

16:25:16 <Stnby[m]> Why cant CCS just be funded via a private subaddress entirely via people that want to?

16:25:18 <plowsof11> wil it be freely available after the oscars (and not on vimeo) yes/no geonic

16:25:32 <monerobull[m]> You can't really change the movie at this point

16:25:39 <ofrnxmr[m]> jwinterm: That ccs was a shitstorm for years and if its going to continue to be than
were all wasting our time

16:25:45 <geonic> like other movies are freely available, yes

16:25:45 <Siren[m]> you expect people to watch through the end credits

16:25:52 <plowsof11> thanks

16:26:00 <jwinterm> maybe the people who contributed to it feel differently?

16:26:24 <plowsof11> and you are going to discuss with monero events team ... with there being a cinema "near"
the event OR on your phone

16:26:27 <geonic> I have no intention of hiding the movie in my closet :p

16:26:28 <Lovera[m]> jwinterm: We need to remember that there are “Monero whales” that they maybe donate even
not reading the proposal because they” trust “ in Monero community criteria to go funding…

16:26:34 <plowsof11> near the monerokon*

16:26:41 <ofrnxmr[m]> jwinterm: I mean

16:26:41 <ofrnxmr[m]> that the ccs system* is a shitstorm

16:26:50 <jwinterm> Lovera[m]: sounds like a them/whales problem :P

16:26:55 <midipoet> Lovera[m]: than we should  embrace the whales, not act as their gatekeepers

16:27:01 <geonic> that would be so cool if we had a proper theater screening

16:27:01 <michaelizer[m]> Lovera[m]: I've always felt that this is actually the case

16:27:21 <ofrnxmr[m]> But they also pay scammers

16:27:23 <geonic> where Siren[m] and monerobull[m] can throw eggs at me

16:27:26 <monerobull[m]> midipoet: If they run out of good will at some point we will be struggling to fund
even the most important dev wirk

16:27:27 <Lovera[m]> jwinterm: Yep! 😅 just comment. Their Monero is not infinite ♾️

16:27:28 <geonic> :)

16:27:44 <monerobull[m]> * If they run out of good will at some point we will be struggling to fund even the
most important dev work

16:27:48 <midipoet> monerobull[m]: if they donate blindly, we cannot be blamed

16:27:54 <geonic> Lovera[m]: u sure? #inflationbug

16:27:55 <blankpage[m]> Surely these careless whales would at least have a preference between Devs/marketing
so I don't think it "sucks up" donations that would otherwise fund devs

16:27:59 <plowsof11> ok, there is an events meeting soon to get some thinking about some more things you can
add to the ccs to appease some people and increase sentiment

16:28:10 <Lovera[m]> geonic: Ouch

16:28:10 <monerobull[m]> midipoet: If we waste funds yes we can

16:28:10 <plowsof11> and such there fore visa vi yeah?

16:28:24 <geonic> omg ppl worried about other people's bags is too much

16:28:33 <ofrnxmr[m]> Ok so.

16:28:33 <ofrnxmr[m]> The way I see it

16:28:34 <michaelizer[m]> midipoet: morally, maybe

16:28:35 <geonic> if you're poor it's on you. don't donate.

16:29:03 <ofrnxmr[m]> There is no clear consensus

16:29:13 <ofrnxmr[m]> Same yesses and nos as before

16:29:16 <Siren[m]> geonic: looks like you have very rich friends, why come to the general fund?

16:29:23 <geonic> general fund ?!?!?

16:29:30 <Siren[m]> aka CCS

16:29:31 <ofrnxmr[m]> CCS*

16:29:39 <plowsof11> monerobull and lovera liked it if the movie would be free after and possible screened at
a monerokon so theres that

16:29:41 <jwinterm> ccs and general fund are entirely separate things, no?

16:29:43 <midipoet> monerobull[m]: there have been plenty of much larger wastes of funds in the past and
probably will be in the future

16:29:47 <Siren[m]> sure call it CCS

16:29:51 <plowsof11> correct jwinterm, different departments

16:29:55 <ofrnxmr[m]> monerobull @monerobull:matrix.org:  confirm

16:30:04 <plowsof11> ccs(tm) and general fund(llc)

16:30:08 <monerobull[m]> I'm at best neutral leaning no

16:30:08 <ofrnxmr[m]> Are you voting yes if or no

16:30:09 <Lovera[m]> I vote yes if there adds that will be freely available after oscar + Monerokon 😎

16:30:21 <midipoet> Yeah people shoud not equate GF and CCS

16:30:22 <plowsof11> there ya go boom consensus achieved now lets move on

16:30:31 <plowsof11> that was easy

16:30:35 <Siren[m]> midipoet: Either way the question holds

16:30:38 <jwinterm> unless almighty lord and ruler luigi1111 decides to move some GF into CCS after
unilaterally deciding to move this to funding

16:30:48 <jwinterm> because tbh in my mind that's how this whole process works anyway lol

16:30:52 <Siren[m]> you're too pushy and call people poor gatekeepers for stating opinions

16:31:02 <geonic> Siren[m]: CCS has nothing to do with the general fund, except that the GF sometimes (rarely)
contributes to CCS proposals. maybe that explains your downvote?

16:31:03 <jwinterm> there is only one gatekeeper

16:31:08 <midipoet> Siren[m]: the question holds, but the GF=CCS is not sound logic

16:31:15 <jwinterm> his name starts with luigi111 and ends with 1

16:31:23 <geonic> lol

16:31:31 <ofrnxmr[m]> jwinterm: I thought it ends with w

16:31:34 <Siren[m]> midipoet: yes that has been a typo, now outta the way

16:31:36 <ofrnxmr[m]> Right

16:31:38 <ofrnxmr[m]> So as I see it

16:31:45 <jwinterm> oh there's two of them :0

16:31:54 <Siren[m]> geonic: no that doesn't explain my downvote. my downvote is because of the proposal
itself.

16:32:07 <plowsof11> not a consensus achieved but there are things which geonic can add to make some people
happier

16:32:11 <geonic> sorry for being pushy. I'll just sit back, relax and let you gatekeep every proposal you
dislike

16:32:17 <blankpage[m]> Yes CCS is basically a dictatorship and these meetings are partially an opportunity
for the masses to express their grievances to the dictators.

16:32:18 <ofrnxmr[m]> 7/8 vote. Stalled or luigi and fire are tiebreakers

16:32:21 <ofrnxmr[m]> And core

16:32:30 <monerobull[m]> geonic: That's literally how this is supposed to go

16:32:54 <Siren[m]> REEEEE negative opinion on my proposal REEEE ur poor and u gatekeep every proposal

16:33:22 <xmrscott[m]> Not just the meetings, folk can leave comments on the proposals :)

16:33:35 <geonic> hi xmrscott[m], long time.

16:34:00 <plowsof11> so add some more nice promises to the proposal as discussed above and ask core about it ,
can we move on now

16:34:03 <Stnby[m]> This is a bit of a chaotic meeting

16:34:24 <geonic> plowsof11: will do, thank you!

16:34:34 <midipoet> Also comments on the reddit post are also valid. Usually, it's weighted voting with
precedence given to known/trusted psuedonyms.

16:34:35 <plowsof11> thanks ok lets breeze through

16:34:36 <plowsof11>   d. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/375)

16:34:38 <michaelizer[m]> Stnby[m]: right? xd

16:34:52 <ofrnxmr[m]> Whoa whia

16:34:53 <BusyBoredom[m]> Yeah see if the deal can be sweetened and come back to it another time, I think this
has run its course

16:34:53 <ofrnxmr[m]> Dont just slide off and leave a ness for 2 weeks

16:34:59 <blankpage[m]> Please move on

16:35:05 <ofrnxmr[m]> I think it needs to ve confirmed that we could bit come to consensus and that someone
needs to ve tiebreaker

16:35:10 <ofrnxmr[m]> Whether core or whoever

16:35:16 <plowsof11> research proposal wants 100% upfront, ok, MRL have to discuss that, and would ideally
need core to escrow some fiat if required (like they will do for the bp++ ccs)

16:35:21 <monerobull[m]> CAN PEOPLE STOP SUBMITTING PROPOSALS 14 HOURS BEFORE A MEETING ON A FRIDAY

16:35:32 <Rucknium[m]> I don't think isthmus is here to answer questions about the proposal. But I'm here. I
cannot fully speak for isthmus.

16:35:52 <monerobull[m]> What are we supposed to do here? Say "everyone read it till next time, next"

16:35:54 <ofrnxmr[m]> Well if were considering paying get

16:35:56 <ofrnxmr[m]> Pay them

16:35:56 <michaelizer[m]> monerobull[m]: they could be overlooked until next week

16:35:59 <ofrnxmr[m]> Geo*

16:35:59 <michaelizer[m]> as a rule

16:36:26 <blankpage[m]> I have not had time to read this proposal, and it seems that no one has had time to
comment or vote on gitlab.

16:36:38 <monerobull[m]> Ok, everyone read the thing, comment on Gitlab and we'll talk about it next time

16:36:42 <monerobull[m]> Next item

16:36:47 <plowsof11> yeah to soon to dicsus isthmus' ccs just some general logsitics to discuss about 100%
payment / or core to escrow the fiat

16:36:57 <ofrnxmr[m]> Why even bring up "up front" if the other ccs that us perfectly acceptable and has
nothing  to do with xmr is favorably on the table

16:37:23 <Lovera[m]> I don’t read that proposal… I hadn’t even realized that I was in the CCS.🤣

16:37:24 <ofrnxmr[m]> Wow. Eglish much. I hope DSM doesnt see that

16:37:27 <plowsof11> lets move on to [Resolve WIP list](https://github.com/plowsof/ccs-wip-list/issues)

16:37:38 <plowsof11> https://github.com/plowsof/ccs-wip-list/issues/1

16:37:44 <ofrnxmr[m]> Xmrsale and accept xmr?

16:38:07 <blankpage[m]> Ideally isthmus will be around for the next meeting when proposal has been groked

16:38:12 <plowsof11> would anyone like to vote on deciding if xmrSal ccs should be closed?

16:38:13 <monerobull[m]> Move forward

16:38:15 <plowsof11> closed means, that if the proposer turned up tomorrow after close, theyre not getting any
monero from the ccs, it will be closed

16:38:31 <geonic> close and move the funds

16:38:44 <monerobull[m]> Agreed

16:39:00 <blankpage[m]> I think the suggester arrangement makes sense at it is a similar project with
potential for actual usefulness

16:39:02 <plowsof11> the suggestion for moving the funds is https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/374

16:39:10 <plowsof11> to entirely fund acceptxmr with the 30 xmr

16:39:22 <plowsof11> yes / no?

16:39:22 <BusyBoredom[m]> Happy to answer any questions about it

16:39:39 <Lovera[m]> Close and move the funds

16:39:42 <plowsof11> true blankpage i agree

16:39:57 <Lovera[m]> Move  the funds to AcceptXMR

16:40:01 <Siren[m]> plowsof11: yes

16:40:31 <geonic> do eeet

16:40:38 <plowsof11> can we vote to close https://github.com/plowsof/ccs-wip-list/issues/2 also?

16:40:40 <blankpage[m]> I would like to see some input from people are likely users of AcceptXMR (on
compatibility/usefulness) as I am unlikely to use it in the near future

16:40:53 <plowsof11> archive monero - we got scammed and there is 0.2 xmr left

16:40:53 <ofrnxmr[m]> Is accept xmr still in proposal phase?

16:40:57 <plowsof11> close proposal and return 0.2 to the general fund yes/no?

16:41:10 <monerobull[m]> Kek

16:41:16 <ofrnxmr[m]> I agree to close and earmark the funds for accept xmr, still subject to approval of the
proposal......

16:41:36 <hinto[m]> plowsof: to be clear - we're deciding to redirect xmrsale funds towards AcceptXMR?

16:41:56 <plowsof11> xmrsale is to be closed. the funds are to be decided

16:42:01 <Rucknium[m]> From TFM: "An expiration date for the proposal. If it's not funded or finished by a
certain time, the funds can be released to other proposals or the General Fund.. This keeps things moving
along in a timely fashion."

16:42:05 <ofrnxmr[m]> If acceotxmr proposal is rejected, split funds for other ccs

16:42:08 <plowsof11> acceptxmr is the suggestion / in the idea stage

16:42:08 <blankpage[m]> Yes please recover funds from archive scam

16:42:09 <Rucknium[m]> xmrsale's proposal says "This proposal will expire 1 March, 2022."

16:42:32 <Rucknium[m]> The guideline on expiration dates does not say shall. It says can. So funds are not
necessarily re-allocated. But they can be.

16:42:43 <Lovera[m]> ofrnxmr[m]: +1

16:42:46 <ofrnxmr[m]> Yes, so earmark and use to fund if proposal is accepted. Use for ormther ccs's if not
accepted

16:42:56 <ofrnxmr[m]> Archive monero, donate it to loveras proposal

16:42:59 <plowsof11> acceptxmr is similar / promises to offer the same / better than the original xmrsale +
has 1 year of maintenance built in, for 30xmr

16:43:19 <plowsof11> from a known community member

16:43:22 <ofrnxmr[m]> Its still not been looked at as a proposal or voted on

16:44:08 <plowsof11> so for definite : xmrsale will be closed

16:44:12 <ofrnxmr[m]> Am I saying there is any reason it wont be? No. But lets not makes mistakes, even if
good people and no bad outcome

16:44:24 <ofrnxmr[m]> Agreed

16:44:41 <plowsof11> archive will be closed

16:44:50 <monerobull[m]> Sure i vote same as ofrn

16:44:52 <ofrnxmr[m]> Agreed

16:45:09 <Rucknium[m]> A major difference with the acceptxmr proposal is that no one votes with their
piconeros. Voting with piconeros has been a good check on a proposal's support in the community.

16:45:11 <monerobull[m]> Archive too

16:45:37 <Lovera[m]> I think as ofrnxmr says., if accepted to funds goes to AceptXMR if not, split it for
others CCs

16:46:16 <plowsof11> iirc funds have never been dispursed to another proposal before so this would be
monumental

16:46:37 <BusyBoredom[m]> I'm fine waiting for more people to look through the proposal, seems fair

16:46:43 <plowsof11> busyboredom is available to answer any questions / make adjustments on the proposal

16:47:36 <Rucknium[m]> Re-allocating to acceptxmr makes the most sense since it's closest in spirit to
xmrsale. TFM also says something like "anyone can pick up milestones if they aren't completed."

16:48:08 <ceetee[m]> . +1 for move fund to Standalone AcceptXMR

16:48:08 <ceetee[m]> . +1 for closing https://github.com/plowsof/ccs-wip-list/issues/2

16:48:20 <geonic> +1 for closing Archive Monero

16:48:38 <plowsof11> a bit more time needed for feedback / input on acceptxmr then , but definitely closing
Archive and xmrsale

16:48:48 <ofrnxmr[m]> Im voting archive monero gets donated to lovera ccs

16:48:54 <plowsof11> nice idea

16:49:09 <plowsof11> shall we jump into some work in progress ccs updates?

16:49:16 <plowsof11> does anyone want to see a pretty video clip

16:49:33 <monerobull[m]> Oh god

16:49:34 <Rucknium[m]> "If the proposer disappears, no problem, someone else can pick up from their last
milestone." <- exact language from TFM.

16:49:37 <jwinterm> I did a talk with some people at privacy and scaling explorations group yesterday on
reddit - maybe monero community would consider some way to do anonymous signaling on whether or not to advance
proposals to funding

16:49:51 <jwinterm> known community members get invited to group, anyway in group can anonymously signal on
proposals

16:49:52 <Siren[m]> plowsof11: new renders? :)

16:50:01 <jwinterm> not trying to go off on tangent, just a thought

16:50:17 <monerobull[m]> Eh

16:50:19 <hinto[m]> ring signature votes?

16:50:21 <ofrnxmr[m]> I like signing my name to my yes and no's

16:50:24 <plowsof11> the reason for moving to another project entirely imo is because xmrsale is a fork, which
has fel behind, and is bilt upon monero-wallet-rpc - for 30xmr someone has to resync with upstream, learn it,
and we end up with javascript wallet rpc trash

16:50:31 <ofrnxmr[m]> Keeps you honest

16:50:33 <plowsof11> Animated videos proposal updates:

16:50:33 <jwinterm> https://appliedzkp.org/

16:50:34 <monerobull[m]> I like the reputational damage that comes with disliking a proposal

16:50:38 <plowsof11> [updated
clip](https://www.reddit.com/r/Monero/comments/10zi0wn/new_animated_videos_animation_example/)

16:50:42 <jwinterm> semaphor is the protocol, and there is one demo app now

16:50:43 <Siren[m]> jwinterm: you can have your proposal up on a webpage where people donate to your address
using Monero

16:50:52 <jwinterm> ZK, not ring sigs hinto[m]

16:50:57 <jwinterm> snarks

16:50:57 <plowsof11> - [updated story board](https://docdro.id/wkLPG5W)

16:51:12 <plowsof11> and - [script 1](https://gitlab.com/monero-videos/monero-adoption-animated-
videos/-/blob/main/Video%201%20Script%3A%20Why%20Use%20Monero%20for%20Commerce%3F.md)

16:51:27 <jwinterm> Siren[m]: that is what happens after something goes to funding tho right?

16:51:40 <plowsof11> alot to give feedback on at the moment, but they have been working on it and this is
their progress

16:51:49 <geonic> plowsof11: that's nice

16:51:53 <Siren[m]> jwinterm: yeah but not associated with CCS and the Monero community here

16:52:10 <jwinterm> well anyone can do that already and no one does that right?

16:52:15 <jwinterm> no one/very few ppl

16:52:20 <Siren[m]> jwinterm: no?

16:52:39 <Siren[m]> people do, all FOSS projects do that

16:52:43 <jwinterm> which CCS proposals that have been funded started out with that tactic?

16:52:53 <Siren[m]> it's how things are normally

16:53:01 <jwinterm> sure

16:53:06 <ofrnxmr[m]> Moneroj.net

16:53:19 <jwinterm> I am just saying this process is messy and murky, and was making a suggestion about how to
possibly codify and proceduralize a bit more

16:53:23 <jwinterm> just a suggestion

16:53:25 <Siren[m]> atm.monero.is, moneropay

16:53:28 <Stnby[m]> ofrnxmr[m]: They got refused and started their own funding

16:53:34 <plowsof11> Endor Solopt Update (profitability.py) - https://github.com/mj-
xmr/SolOptXMR/issues/151#issuecomment-1426619628 (he has fixed the script to check for another node woohoo)

16:53:47 <jwinterm> like people vote on ccs proposal, then other people claim people who are voting are
sockpuppets, etc

16:53:51 <ofrnxmr[m]> Stnby[m]: ^^ yup and are doing Fkn awesone

16:53:52 <jwinterm> this would be route to avoid that

16:53:55 <geonic> more procedure = more easily gamed imo

16:53:59 <Stnby[m]> Stnby[m]: Best wallet for Monero ;)

16:54:01 <Siren[m]> jwinterm: one way to make it normal would be to only count the votes on gitlab + this
matrix room

16:54:21 <jwinterm> but then people are yelling about sockpuppet gitlab users

16:54:35 <plowsof11> valldrac of molly.im has a demo akp available - a sandbox monero wallet which is able to
open multiple monero wallets at once - i couldnt get it work work on my phone but have not tried the new one

16:54:35 <plowsof11> ideally a public version of the demo will be available

16:54:35 <Siren[m]> gitlab admins can verify sockpuppets

16:54:40 <jwinterm> this way only people invited to vote would be able to vote, and their vote would be
anonymous

16:54:48 <Siren[m]> they were obviously sockpuppets as well

16:54:55 <Siren[m]> we all could tell anyways

16:54:56 <geonic> jwinterm: who decides who gets invited?

16:55:03 <jwinterm> luigi1111:

16:55:06 <jwinterm> obvs

16:55:09 <geonic> fair

16:55:15 <Siren[m]> fair?

16:55:22 <Siren[m]> that'd be actual gatekeeping

16:55:22 <Stnby[m]> XD

16:55:25 <geonic> yeah, this is a dictatorship after all

16:55:25 <Siren[m]> yall are on meth

16:55:26 <ofrnxmr[m]> Or only "community members" can vote

16:55:31 <ofrnxmr[m]> Ignoring macsrocks

16:55:32 <ofrnxmr[m]> And other alts

16:55:32 <jwinterm> you guys called johnny mnemonic a sock puppet and the guy made like the third post on the
*bit*monero bitcointalk post

16:55:48 <geonic> lol

16:55:52 <plowsof11> donor or donator sirs?

16:56:01 <geonic> but he never participates on CCS proposals! must be a sock

16:56:05 <ofrnxmr[m]> Siren[m]: They need to drink some

16:56:09 <geonic> donor obvs :)

16:56:15 <ofrnxmr[m]> Luigi doesnt?!?!?!

16:56:17 <plowsof11> +1 for donor

16:56:22 <plowsof11> 0 for donator

16:56:22 <ofrnxmr[m]> He merged mj's bullshit

16:56:27 <jwinterm> lol

16:56:40 <ofrnxmr[m]> He does what we want, as long as we agree with him. Otherwise, he does what he wants

16:56:49 <geonic> hehe

16:57:07 <plowsof11> dont forget the monero events meeting in 1 hour btw

16:57:22 <Rucknium[m]> Do we know if it was the same Johnny Mnemonic? Where is the PGP signature?

16:57:22 <ofrnxmr[m]> Any more WIP?

16:57:36 <ofrnxmr[m]> Can we agree to donate the 0.2xmr to lovers before lovers us fully funded?

16:57:43 <Stnby[m]> I think CCS is fucked, wish there was a section at least to list independent projects

16:57:47 <jwinterm> sorry, didn't mean to cause digression, I just thought it was neat and would share, if you
want to listen to talk recording is here:
https://www.reddit.com/r/CryptoCurrency/comments/10yyaot/reddit_talk_with_privacy_and_scaling_explorations/

16:57:59 <Siren[m]> I don't remember who the fuck but some people posted nearly identical comments, I don't
care who it is

16:58:03 <geonic> Stnby[m]: that's an interesting idea

16:58:16 <monerobull[m]> Stnby[m]: Ey it's better than what unis wap has for governance

16:58:16 <blankpage[m]> Codifying votes seems pointless when the votes are only a suggestion to the dictator
anyway. It is more an opportunity to flag up issues, through chats and comments

16:58:16 <monerobull[m]> * Ey it's better than what uniswap has for governance

16:58:22 <Siren[m]> geonic: monerodevs.org

16:58:23 <jwinterm> oh yea Siren[m] tbh I think that was vik, I do remember someone pointing that out lol

16:58:24 <ofrnxmr[m]> 0.2 from archiver to lovera

16:58:24 <ofrnxmr[m]> Yay or nay

16:58:35 <Stnby[m]> Stnby[m]: As CCS scams for example get higher budget than legit projects that do their own
funding

16:58:36 <geonic> yay!

16:58:37 <plowsof11> so in this meeting: close archive/xmrsale - wait for feedback on acceptxmr. geonics oscar
proposal at the least can benefit from adding some reassurances in the proposal that it'll be free, and to
discuss formally the possibility of a screening at monerokon in prague

16:58:43 <BusyBoredom[m]> 0.2 to lovera seems fine

16:59:01 <Siren[m]> jwinterm: nobody called him afaik a gatekeeper. I was just pointing out to the list of
unusual people who liked that proposal.

16:59:02 <plowsof11> 0.2 to lovera also fine

16:59:05 <geonic> free(ly available)

16:59:11 <Siren[m]> don't make shit up now

16:59:18 <jwinterm> someone pointed out that it seemed fairly obvious it was him

16:59:19 <plowsof11> free(tm)ly available

16:59:53 <Siren[m]> did plowsof receive his funds?

17:00:00 <plowsof11> 1 minute to continue fighting , AOB?

17:00:23 <Siren[m]> have they paid plowsof yet?

17:00:23 <ofrnxmr[m]> Siren[m]: No

17:00:23 <Siren[m]> why?

17:00:25 <plowsof11> yes siren, i was paid for 2 milestones up to now, thank you all for shouting at me to
claim them

17:00:45 <Siren[m]> great finally

17:00:49 <ofrnxmr[m]> Were busy tryin to pay Geo 12k up front

17:00:58 <ofrnxmr[m]> Siren[m]: Thus is month 4

17:01:03 <BusyBoredom[m]> We like you plowsof, gotta make sure you're getting treated well 😤

17:01:03 <Siren[m]> ah fuck

17:01:31 <ofrnxmr[m]> He started before the ccs, and is going beyond the deadline

17:01:39 <plowsof11> if i  claim the final milestone then i lose all my power

17:01:40 <blankpage[m]> monerodevs.org should perhaps be linked from the main website & reddit

17:01:49 <luigi1111> Excuse me I don't run the gf

17:01:53 <ofrnxmr[m]> If paid in full, he could ve volunteering. Thats fine. But he hasnt been

17:01:53 <plowsof11> monerodevs was redesigned by Siren BTW

17:01:53 <luigi1111> Also I'm on a boat

17:02:14 <nioc> be careful

17:02:19 <plowsof11> front end and backend totally new

17:02:30 <ofrnxmr[m]> Hahahahahahahahahaha luigi

17:02:53 <nioc> give isthmus whatever he wants

17:02:56 <plowsof11> as you should be luigi1111 , i hope you are enjoying calm waters

17:03:08 <Stnby[m]> On a private yacht with sgp :)

17:03:20 <nioc> aka Mitchell

17:03:38 <ofrnxmr[m]> Uh.. boating accident

17:03:38 <Siren[m]> lost the keys to the GF

17:03:38 <Lovera[m]> luigi1111: 🤣 lol

17:03:39 <ofrnxmr[m]> Pretty sure he meant stfu or I might crash 😂😂

17:03:39 <Siren[m]> in a boating accident

17:04:00 <jwinterm> I'm at a waterpark...watersliding accident?

17:04:05 <plowsof11> rucknium will be getting the C++ help they need from an expert team

17:04:47 <ofrnxmr[m]> Need to read over proposal about why up front is necessary

17:04:55 <blankpage[m]> monerodevs does give prominence (and potentially more donations) to projects early in
the alphabetical order it seems

17:05:00 <ofrnxmr[m]> Otherwise, im probably voting yes

17:05:06 <Siren[m]> blankpage[m]: it will be shuffled

17:05:15 <plowsof11> its the same as bulletproofs ++ proposal - but in that case - core are going to convert
and custody the fiat

17:05:20 <Siren[m]> also the images will be rendered webp or webm

17:05:26 <nioc> ofrnxmr[m]: up front to avoid volatility

17:05:28 <plowsof11> i would like that to be the same for this research porposal if possible

17:05:35 <plowsof11> proposal

17:05:37 <ofrnxmr[m]> Ehhhh nah

17:05:47 <BusyBoredom[m]> Was gonna say, I picked a good name for my project looking at monerodevs ordering 😂

17:05:51 <Siren[m]> the issue is that the old backend had images as remote content (links), I need to write a
script to get all and convert them and so on

17:05:54 <geonic> core are converting and custodying fiat now?

17:06:03 <ofrnxmr[m]> Lmfao right

17:06:21 <BusyBoredom[m]> It looks great though, bit improvement over old monerodevs

17:06:36 <plowsof11> for monoerokon , and other research proposal / audits yes

17:06:59 <geonic> is that info published anywhere

17:07:04 <geonic> under what legal entity?

17:07:08 <nioc> I am sure that an agreement can be made to satisfy people for upfront payment

17:07:16 <plowsof11> digitalrenegades iirc

17:07:35 <nioc> no issue with the work actually getting done

17:07:37 <plowsof11> if you make a reddit thread again geonic you are banned

17:07:44 <geonic> :)

17:07:58 <geonic> I think DR is being used as a favor to the MoneroKon organizers. not in an official core
capacity

17:08:04 <ofrnxmr[m]> I am banned already and I never made a thread :(

17:08:06 <blankpage[m]> Core shouldn't have any official interaction with fiat IMO, just asking for trouble

17:08:22 <Siren[m]> geonic: DR is binaryfate, which is core

17:08:24 <plowsof11> geonic yes not official

17:08:28 <geonic> I was also banned on reddit. fun times

17:08:32 <plowsof11> an affiliate?

17:08:48 <geonic> Siren[m]: so when he goes to the grocery store, it is the Core Team buying groceries?

17:08:59 <ofrnxmr[m]> Anyway

17:09:08 <ofrnxmr[m]> Transparency report on Monday it seems

17:09:28 <geonic> surely he can operate as an individual too

17:09:34 <Siren[m]> geonic: possibly

17:09:50 <plowsof11> will follow up the molly im apk / monero thing for us all btw , i think that is the
meeting wrapped up now?

17:09:52 <jwinterm> liability can be a motherfucker

17:10:30 <monerobull[m]> ofrnxmr[m]: I can unban you if you want

17:10:38 <geonic> plowsof11: can u confirm that statement please? that the Core TeamTM is converting and
custodying fiat on behalf of anyone?

17:10:42 <ofrnxmr[m]> Events meeting in 50 minutes

17:11:08 <plowsof11> thanks for all attending, and everyone with 100% attendance who is still in the running
for a gold sticker at the end of February

17:11:10 <Stnby[m]> Would be nice to have a 1st ticket sold by then

17:11:31 <plowsof11> geonic if you want an official statement contact DRR and ask them wtf theyre doing for
monerokon

17:11:38 <Siren[m]> anyways guys contact ajs_ and purchase a ticket or a t-shirt. if anything goes wrong, you
will be refunded or given a ticket manually so don't worry.

17:11:54 <geonic> no, that's clearly their own business. I've never seen Digital Renegades being conflated
with Core Team

17:11:54 <Siren[m]> (I think t-shirts are also available, but not sure)

17:12:22 <jwinterm> plowsof11: is sticker an nft?

17:12:22 <Siren[m]> s/guys/people/

17:12:39 <ofrnxmr[m]> The conflation is that the volitility risk was the proposers problem

17:12:41 <monerobull[m]> Physical bft

17:12:44 <ofrnxmr[m]> And up front ccs were taboo

17:12:47 <monerobull[m]> * Physical nft

17:12:47 <ceetee[m]> it's one of mb gold stickers

17:12:47 <Siren[m]> jwinterm: https://monerosupplies.com/product/reflective-anonymous-money/

17:13:02 <ceetee[m]> * of mb's gold

17:13:24 <ofrnxmr[m]> But as long as a core team member says up front us ok, and they will handle the
volitility, then things change.

17:13:24 <ofrnxmr[m]> Did _core_ handle that? No, but they had a COI with allowing it

17:13:38 <jwinterm> oh nice

17:13:38 <geonic> what conflict of interest?

17:13:53 <geonic> because he offered to help? where's the conflict

17:14:32 <ofrnxmr[m]> Its been stated that the volatility risk comes with ccs

17:14:46 <geonic> DR's services are free of charge and I trust the MoneroKon organizers to keep full
accounting

17:14:50 <ofrnxmr[m]> Unless youre friends, then you can get milestone 0's and fiat conversion

17:14:54 <plowsof11> in the past, the general fund has donated a certain % to account for volatility to code
audits , im trying to find the specific proposal

17:15:31 <plowsof11> https://ccs.getmonero.org/proposals/clsag-audit-take2.html

17:15:38 <ofrnxmr[m]> (Im not against milestone 0's. Im against the "for me but not thee" attitude)

17:15:40 <plowsof11> so fiat is not mentioned here, so im wrong in saying that

17:16:13 <plowsof11> core are not custodying fiat

17:16:18 <geonic> ty

17:17:11 <plowsof11> they only custody gold coins with the letter M engraved


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-02-02T20:13:37+00:00
- Closed at: 2023-02-15T23:04:33+00:00
