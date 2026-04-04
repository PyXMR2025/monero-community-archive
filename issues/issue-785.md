---
title: 'Monero Community Workgroup Meeting: Saturday 28th January 2023 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/785
author: plowsof
assignees: []
labels: []
created_at: '2023-01-22T12:31:45+00:00'
updated_at: '2023-01-30T21:43:44+00:00'
type: issue
status: closed
closed_at: '2023-01-30T21:37:28+00:00'
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
 - kasejo.com (no source code yet) - [logo contest](https://www.reddit.com/r/Monero/comments/10j8pdf/update_merchant_a_foss_desktop_point_of_sale_app/)
 - Lumo - node.js donation platform [reddit thread](https://www.reddit.com/r/Monero/comments/10kvp7u/lumo_a_node_js_server_that_allows_you_to_host_a/)
 - C++ BLAKE2b Dev Challenge [ Seraphis ] [new bounty posted](https://bounties.monero.social/posts/75/0-348m-blake2b-c-dev-challenge-seraphis)
 - [Haveno bounties](https://github.com/haveno-dex/haveno/issues?q=is%3Aopen+is%3Aissue+label%3A%F0%9F%92%B0bounty)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)
5. [CCS updates](https://ccs.getmonero.org/)    
  c. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/366)    
  d. [Help an independent film featuring Monero get to the Oscars™!
](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371)
  e. [selsta part-time monero development (3 months)
](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/372)

Updates:
- [Scripts for the animated videos proposal requesting feedback](https://gitlab.com/monero-videos/monero-adoption-animated-videos/), [issues for script 1 being worked on](https://gitlab.com/monero-videos/monero-adoption-animated-videos/-/issues) and [image previews](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/308#note_20552)
- Molly IM [update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/252#note_20549)

Close:
- [xmr-btc-swap development and improvement](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/355)     
 
Delayed until new paper released OR MRL/Dev decide to move forward:     
     
-  [Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358)    
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
10. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/779)    

Meeting logs will be posted here afterwards.    

# Discussion History
## mj-xmr | 2023-01-24T07:52:37+00:00
I'd like to learn from endor an approximate completion date for [this issue](https://github.com/mj-xmr/SolOptXMR/issues/151) of SolOptXMR.

## plowsof | 2023-01-25T13:02:22+00:00
Noted @mj-xmr, ill ask for an update 

## nanostos | 2023-01-28T14:51:18+00:00
With regards to the scripts for the animated videos proposal requesting feedback, I won't be able to (meaningfully) attend because of the unfortunate time in Australia when the meeting is scheduled. However, as script coordinator, I'll check the meeting log afterwards and add any comments to the repo, in addition to those received over the last week or so. 

Once I've digested it all and made changes, I'll reach out to the commenting individuals to see if there is any additional feedback on the new version.

## plowsof | 2023-01-30T21:37:26+00:00
Logs 
```
16:00:18 <plowsof11> Meeting time https://github.com/monero-project/meta/issues/785

16:00:21 <plowsof11> Greetings, hi

16:00:41 <Siren[m]> Ohai

16:00:53 <MSvB[m]> Hello.

16:02:20 <plowsof11> linking the news sites/letters while we wait a bit (Monero Moon has been active recently
and is making an appearance) [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-
xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero
Moon](https://www.themoneromoon.com/)

16:03:30 <hinto[m]> hello

16:05:10 <plowsof11> can jump to community highlights, anyone want to share something cool theyve been doing
or noticed?

16:05:46 <Siren[m]> Small update about Monero ATM: We would like to thank everyone who donated to the [ATM
project](https://atm.monero.is/). We're 57% funded! There hasn't been much progress this week because I'm busy
programming for Monerokon.

16:05:47 <blankpage[m]> Hello

16:06:25 <Siren[m]> Siren[m]: Other people are busy exploring NixOS builds and random stuff

16:06:42 <blankpage[m]> Revuo seems pretty low effort compared to the other news sources

16:06:47 <plowsof11> an open source, off-the-shelf parts DIY ATM to buy monero with cash

16:07:24 <plowsof11> the p2poool hardfork test on testnet was a success so everything is on track, well done
sech1 https://github.com/SChernykh/p2pool/issues/224

16:08:06 <hinto[m]> i forked plowsofs code to make a daily updated list of ZMQ-enabled monero nodes:
https://github.com/hinto-janaiyo/monero-nodes

16:08:39 <hinto[m]> these will be replacing the current nodes used in gupax, hopefully solving a lot p2pool
connection related issues

16:08:43 <plowsof11> i've also posted a bounty to hopefully support the developer who helps get  blake2b
merged into seraphis. without this, there will be no randomx mining in it, so its kind of important C++
BLAKE2b Dev Challenge [ Seraphis ] [new bounty
posted](https://bounties.monero.social/posts/75/0-348m-blake2b-c-dev-challenge-seraphis)

16:09:58 <plowsof11> [Haveno bounties](https://github.com/haveno-
dex/haveno/issues?q=is%3Aopen+is%3Aissue+label%3A%F0%9F%92%B0bounty) , woodser has been very busy on the back
end. wowario recently made a pull request to add wownero to haveno.

16:11:05 <Rucknium[m]> I wrote this:
https://www.reddit.com/r/Monero/comments/10gapp9/centralized_mining_pools_are_delaying_monero/

16:11:27 <Rucknium[m]> Already at least 3 mining pools started confirming transactions faster.

16:12:41 <plowsof11> wonderful, great to hear, up to ~1 minute faster for a transaction to get 1 conf if every
mining pool updates 👍️

16:13:13 <plowsof11> a few CCS proposers who might not be able to make it have given some updates on what
theyve been up to also

16:13:32 <plowsof11> dmslegend has taken note of feedback already given and put them into issues here
(focussing on video 1) https://gitlab.com/monero-videos/monero-adoption-animated-videos/-/issues

16:14:04 <plowsof11> here is the Script 1 that's being being addressed first https://gitlab.com/monero-
videos/monero-adoption-animated-
videos/-/blob/main/Video%201%20Script%3A%20Why%20Use%20Monero%20for%20Commerce%3F.md

16:14:12 <plowsof11> savandra has uploaded a sneak peak of some images / ideas for feedback theyve worked on
this week https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/308#note_20552

16:14:19 <savandra[m]> Hey guys, here are the new 3D concepts for the vids
https://www.reddit.com/r/Monero/comments/10nfjb7/new_animated_video_update_on_the_new_3d_concepts/

16:14:22 <savandra[m]> oh sorry

16:14:28 <plowsof11> ah hello savandra

16:15:06 <plowsof11> no problem

16:15:37 <savandra[m]> thank you for bringing up the matrix, hope the new concepts look more appealing! they
will be easily scalable to cover complex and long topics in the future

16:15:55 <plowsof11> my suggestion was to focus on script 1 / video 1 and i am so far satisfied with these
efforts to address our concerns, and will be following up to see any further progress / make sure we're being
kept up to date

16:16:21 <savandra[m]> looking forward to the feedback from the community :)

16:16:25 <savandra[m]> plowsof11: sure

16:18:18 <monerobull[m]1> Hello

16:18:50 <Siren[m]> savandra[m]: they look awesome!

16:19:06 <anhdres[m]> Hi there

16:19:09 <Siren[m]> I love that one with the ball dispenser (?)

16:19:39 <savandra[m]> Siren[m]: yeah, central autority concept with cctv cameras

16:19:45 <savandra[m]> s/autority/authority/

16:19:56 <Siren[m]> that's honestly very creative

16:20:00 <Siren[m]> fits so well

16:20:10 <monerobull[m]1> The new images are cool

16:20:37 <plowsof11> yes, i am relieved to see the script coordinator / animator working

16:21:09 <Rucknium[m]> Another update from me: Artic Mine has given me initial feedback on my OSPEAD
estimation procedure draft and approved the general direction. That's now three green lights out of three, so
we are go for launch.

16:21:09 <plowsof11> very creative indeed

16:22:07 <plowsof11> Molly IM [update](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/252#note_20549) valldrac has shown me the git history of the repo and i can confirm
that regular work has been going on in the molly-monero sdk repo.

16:22:07 <plowsof11> i've suggested that they try to 'show' us how its going with e,g, screenshots/recordings
so we know the project is still alive, which it is

16:22:17 <anhdres[m]> savandra: just saw the 3D concepts, very cool, like them

16:23:43 <plowsof11> thanks for the update valldrac

16:24:33 <plowsof11> out of 3 projects/persons who ive asked for updates, savandra/dmslegend  - and valldrac
have impressed me. only nothing from yet endor00

16:25:46 <plowsof11> ill chase that up. i think we can go on to the ccs proposals now

16:26:25 <plowsof11> [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/366)

16:27:39 <monerobull[m]1> Hm

16:28:11 <plowsof11> lovera has edited the proposal after each request by the community / attended all the
prior meetings. it now contains the transparency section which discloses the 5 videos from cake / no youtube
monetisation or other will be on the community videos. donators can see the full picture now

16:28:45 <ofrnxmr[m]> 👀 im late

16:28:56 <monerobull[m]1> Looks like it has community support and the guy incorporated all request people had

16:30:31 <anhdres[m]> I commented in the isssue, I don't see a problem with Lovera proposal, his videos are
usually very clear and he's knowledgeable. There is not an excess of spanish material, really. I'll leave it
to the community to step up and fund it, but the CCS should be approved IMHO.

16:30:33 <ofrnxmr[m]> Lovera @btclovera:matrix.org: thank you for the transparency

16:30:53 <plowsof11> time to merge this one then?

16:31:27 <Siren[m]> Honestly it's better outreach than the movie

16:31:40 <ofrnxmr[m]> I vote yes

16:31:42 <monerobull[m]1> I vote yes

16:31:46 <Siren[m]> also better price/value, so I'm gonna say yes too

16:31:46 <Stnby[m]> And a whole 15XMR less

16:32:03 <Stnby[m]> Absoultely good deal

16:32:20 <plowsof11> yes

16:32:26 <monerobull[m]1> 15?

16:32:49 <ofrnxmr[m]> Movie is 25k* usd 150xmr or so

16:32:50 <ofrnxmr[m]> So 140xmr less

16:32:56 <Stnby[m]> Ohh right

16:33:22 <Stnby[m]> Well then even better

16:33:31 <Stnby[m]> * even better deal

16:33:31 <plowsof11> Lovera wil be merged asap thanks for votes and patience

16:33:44 <plowsof11> [Help an independent film featuring Monero get to the Oscars™!

16:33:44 <plowsof11> ](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371)

16:34:01 <monerobull[m]1> Only if we get a community version

16:34:02 <Siren[m]> ( ͡° ͜ʖ ͡°)

16:34:16 <anhdres[m]> I think we should be able to watch the film to judge the amount and kind of Monero
exposure

16:34:26 <Stnby[m]> > <@plowsof:matrix.org> [Help an independent film featuring Monero get to the Oscars™!

16:34:26 <Stnby[m]> > ](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371)

16:34:26 <Stnby[m]> Sell your kidneys if you want 150XMR. Not worth even if the movie is CC

16:34:30 <monerobull[m]1> That NEEDS to be clarified before we can even fund it based on the CCS rules

16:34:40 <Stnby[m]> Absolutely NO

16:34:42 <Siren[m]> I don't care about any awards, it needs to be free and open

16:35:06 <Stnby[m]> He does not deserve a cent more than Lovera @btclovera:matrix.org

16:35:47 <plowsof11> so we can see 15% of the movie (public) which i read is planned . the license issue is
still lingering , but the proposer is shifting toward applying the liense to "only the marketing material"

16:36:09 <Siren[m]> and if it cannot be open and he cares more about qualifying for awards, he should go find
funding somewhere else

16:36:10 <Stnby[m]> Not worth 150XMR anyway

16:36:19 <Stnby[m]> A single youtube video is longer lmao

16:36:25 <Siren[m]> I also think that it's not worth 150 XMR

16:36:49 <monerobull[m]1> plowsof11: Only the marketing material? So this is a marketing proposal again all of
a sudden

16:37:02 <Stnby[m]> Just a fat NO

16:37:16 <plowsof11> yes thats the new pivot

16:37:29 <ofrnxmr[m]> No

16:37:30 * Siren[m] uploaded an image: (877KiB) <
https://libera.ems.host/_matrix/media/v3/download/kernal.eu/siQWTVzkMcYpVxTiueuvTBbH/image.png >

16:37:39 <Stnby[m]> No one cares about his bizantine M coin 1sec shot

16:37:39 <ofrnxmr[m]> I vote hard no

16:37:52 <plowsof11> the proposers comment to summarise where they are at now
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371#note_20542

16:37:52 <Siren[m]> Siren[m]: not good enough to find out about Monero

16:38:21 <Siren[m]> but maybe for learning about byzatine empire and drugs

16:38:58 <ofrnxmr[m]> jwinterm @jwinterm:libera.chat: jwinterm @jwinterm:magicgrants.org:

16:39:09 <monerobull[m]1> I could have _maybe_ considered if it was to "support the art"

16:39:19 <ofrnxmr[m]> The ccs is not for the movie, but for the marketing to get to the Oscars

16:39:19 <ofrnxmr[m]> So I wont vote for you, since that wasnt what was discussed

16:39:23 <plowsof11> if we take a look at the bitcoin miami proposal - one of the core team fluffypony had
issue with 'dash hosting a strip club party' so this seems to be important how monero is perceived

16:39:32 <monerobull[m]1> But as just a marketing thing its basically worthless

16:39:46 <Stnby[m]> monerobull[m]1: You should make a proposal for 150 XMR we can cover every single sqm of
Lithuania in Monero ads

16:39:56 <ofrnxmr[m]> Marketing a movie that we cant watch until after commitiing a donation? No

16:39:57 <Siren[m]> I honestly find it problematic that he didn't ask the dead child's family for consent

16:40:04 <ofrnxmr[m]> Might as well sponsor Netflix

16:40:06 <jwinterm[m]> I vote that it is ok to go to funding if marketing materials are permissively licensed

16:40:16 <ofrnxmr[m]> Ill contact Netflix and see if they want us to donate to their TV show

16:40:39 <ofrnxmr[m]> jwinterm @jwinterm:magicgrants.org:  thank you for update 👍

16:40:50 <Siren[m]> Siren[m]: and he's dodging this question too

16:40:55 <monerobull[m]1> ofrnxmr[m]: "This scene sponsored by the Monero community"

16:41:05 <ofrnxmr[m]> Yeah, saying "thats his problem "

16:41:11 <Stnby[m]> DRM sponsored by Monero CCS

16:41:11 <anhdres[m]> We need to see the film, that's my opinion. Maybe it's great. But we cannot make a
decision based on words alone.

16:41:19 <ofrnxmr[m]> Hard no.

16:41:23 <plowsof11> have you not seen it anhdres?

16:41:29 <anhdres[m]> nope

16:41:31 <jwinterm[m]> anhdres[m]: I think this is also reasonable request

16:41:34 <jwinterm[m]> I have seen it

16:41:38 <ofrnxmr[m]> anhdres @anhdres:matrix.org:  you must pay to view

16:41:40 <anhdres[m]> I thought it wasn't available

16:41:41 <Stnby[m]> Can someone drop a link to the movie?

16:41:49 <plowsof11> ehhh its a spanish film, you'd be the first person on the list

16:41:50 <jwinterm[m]> geonic shared it with me privately

16:41:59 <ofrnxmr[m]> ofrnxmr[m]: And delete after viewing

16:42:09 <Stnby[m]> It has to be on the proposal page

16:42:21 <ofrnxmr[m]> But it cant be, or voids the point of the ccs

16:42:21 <plowsof11> anhdres you can contact geonoic for a link

16:42:23 <anhdres[m]> will check, I had no idea it was possible to watch it

16:42:30 <Siren[m]> it's an invalid proposal

16:42:31 <anhdres[m]> will do

16:42:31 <ofrnxmr[m]> plowsof11: Nah, thats sus

16:42:58 <Stnby[m]> How many dislikes does it have to collect to be closed?

16:43:09 <ofrnxmr[m]> 100

16:43:18 <anhdres[m]> in another life I went to film school haha

16:43:26 <plowsof11> geonic* currently it was breaking the rules, but now its shifted into "marketing
materials"

16:43:40 <Siren[m]> it's also mega weird that he's already done with the movie and will release regardless,
he's only here for marketing but provides little to no value for us

16:43:40 <ofrnxmr[m]> (Sarcasm. We all know they will merge this)

16:43:40 <plowsof11> xD

16:43:54 <ofrnxmr[m]> I wont ask for a copy.

16:43:57 <Stnby[m]> plowsof11: When did we spend 150XMR on 1 second marketing?

16:44:40 <ofrnxmr[m]> If I cannot come to the ccs and VIEW it, I can only vote no

16:44:40 <monerobull[m]1> I swear to God if the gf pays to this

16:44:40 <ofrnxmr[m]> So, no

16:44:40 <Siren[m]> you know that you can get a monero themed hot air balloon for 150 xmr right???

16:44:40 <Siren[m]> what the fuck

16:44:40 <Siren[m]> nobody even watches the end credits

16:44:40 <ofrnxmr[m]> You can get Netflix placement for cheaper

16:44:42 <ofrnxmr[m]> And actual name dropping

16:44:56 <Stnby[m]> Can I open a proposal where I ask for CCS to buy me a hot air baloon. We will give it away
to the hot air baloon company in Vilnius

16:44:56 <Siren[m]> yes that was much better marketing

16:44:59 <ofrnxmr[m]> Can watch Netflix trailers too

16:45:13 <Stnby[m]> Stnby[m]: With a big ass getmonero ad

16:45:19 <Siren[m]> because the netflix show said something in the lines of "in Monero. It is untraceable
currency."

16:45:26 <monerobull[m]1> ofrnxmr[m]: With a explanation instead of portraied like a physical coin

16:45:32 <Siren[m]> YES

16:45:33 <ofrnxmr[m]> Stnby[m]: No

16:45:37 <Rucknium[m]> Zcash funded a skydiver

16:45:38 <ofrnxmr[m]> Were doing sgp's yacht next

16:45:50 <monerobull[m]1> Rucknium[m]: Ok but that was cool

16:45:56 <monerobull[m]1> Like their hit song, ZCash anthem

16:46:11 <monerobull[m]1> WHICH IS PERMISSIVELY LICENSED CAN YOU BELIEVE IT

16:46:11 <Stnby[m]> ofrnxmr[m]: Those dont cost 150XMR

16:46:48 <ofrnxmr[m]> Go big or go home

16:46:50 <plowsof11> if this 'situation' is not remedied then it feels like we're in a deadlock / no consensus
with possibly 'rules being broken' - i would then ask core to decide if necessary (like the bitcoin miami
proposal) 😟

16:47:11 <Stnby[m]> Hot air baloon costs 30-70k Eur + VAT. Whos into it?

16:47:13 <ofrnxmr[m]> Uh

16:47:15 <Rucknium[m]> https://grants.zfnd.org/proposals/1830470619-proposal-to-fund-zcash-skydives

16:47:21 <anhdres[m]> I'm still trying to get any of the argentinean fintech that sell crypto for fiat and
stuff like that to accept Monero

16:47:22 <ofrnxmr[m]> There is 1?2 yes votes from "not my friends"

16:47:28 <ofrnxmr[m]> And the rest from friends and alts

16:47:40 <Stnby[m]> Stnby[m]: https://ballooning.lt/reklama-ant-oro-baliono/

16:47:42 <anhdres[m]> then the second step is to post guerilla posters and stuff

16:48:07 <ofrnxmr[m]> Lets reopen Lebanon cxs

16:48:09 <anhdres[m]> but otherwise makes no sense because it's kinda annoying yo buy monero here, unless pure
p2p

16:48:13 <monerobull[m]1> anhdres[m]: I can provide those

16:48:16 <jwinterm[m]> 570 xmr on chinese marketing on one forum https://forum.getmonero.org/22/completed-
tasks/87757/funding-for-a-monero-subforum-on-the-largest-chinese-btc-forum-8btc

16:48:21 <ofrnxmr[m]> Monero doesnt win an Oscar. Geonic does

16:48:38 <monerobull[m]1> jwinterm[m]: How much was xmr worth back then

16:48:49 <Siren[m]> I think he'll win a lawsuit from the family before oscars

16:48:53 <sgp[m]> Rucknium[m]: Honestly $3300 is a good value if the videos actually look cool

16:48:55 <jwinterm[m]> monerobull[m]1: I think that was $25k?

16:48:57 <Siren[m]>  * I think he'll be awarded a lawsuit from the family before oscars

16:49:15 <jwinterm[m]> 170.000 chinese Yuan, around 570 XMR

16:49:18 <monerobull[m]1> The Chinese thing probably got more xmr adoption than this

16:49:38 <jwinterm[m]> monerobull[m]1: it was a total scam, I think this is a lot more value tbh

16:49:42 <Siren[m]> sgp: off-topic but has your team looked into Maxima Lithuania cards yet?

16:50:00 <plowsof11> ok with 10 minutes left, we have a new ccs proposal posted today

16:50:06 <Siren[m]> * Maxima Lithuania (geradovana.lt) cards yet?

16:50:08 <monerobull[m]1> Throwing in failed proposals as a reason to fund this is not the great move you
think it is

16:50:27 <sgp[m]> Siren[m]: We probably can't add unless they have a real API. People don't like when we plug
in stuff they they don't know about. Bad for partnerships long term :(

16:50:40 <plowsof11> selsta (part-time) 3 months dev work https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/372

16:50:40 <ofrnxmr[m]> jwinterm[m]: We arent doing scams anymore

16:50:40 <ofrnxmr[m]> Not even small ones

16:50:47 <jwinterm[m]> monero on a sail boat sail https://forum.getmonero.org/8/funding-required/87627/get-a-
massive-monero-logo-on-a-sail-in-the-bermuda-one-two-yacht-race

16:50:53 <ofrnxmr[m]> Selsta to funding

16:50:55 <jwinterm[m]> appears to have been funded?

16:51:04 <ajs_[m]> selsta +1

16:51:04 <monerobull[m]1> monerobull[m]1: jwinterm @jwinterm:magicgrants.org:

16:51:08 <ofrnxmr[m]> jwinterm @jwinterm:magicgrants.org:  monero isnt even mentioned in the movie

16:51:11 <monerobull[m]1> Selsta +1

16:51:12 <plowsof11> +1 for selsta

16:51:27 <ofrnxmr[m]> Move to funding right away

16:51:33 <jwinterm[m]> monerobull[m]1: I am just pointing out there have been "marketing" things funded in
past

16:51:35 <monerobull[m]1> Let's set a record from proposal to merge kek

16:51:37 <Rucknium[m]> +1 for selsta

16:51:54 <monerobull[m]1> jwinterm[m]: And they all turned out like shit

16:52:05 <selsta> <3

16:52:09 <jwinterm[m]> so did lots of other CCS things lol

16:52:09 <sgp[m]> +1 selsta

16:52:23 <ofrnxmr[m]> jwinterm @jwinterm:magicgrants.org:  new year, new standards

16:52:57 <ofrnxmr[m]> I havent seen the movie and wont beg or share my address to see it. If it cant be
shared, it cant be voted on

16:53:06 <plowsof11> we have another open proposal - comit swaps improvement - 6 thumbs up 4 down - but the
sentiment in all the meetings has been to close

16:53:21 <ofrnxmr[m]> Does he expect everyone to contact him directly? Thats not how ccs works

16:53:28 <monerobull[m]1> I have an announcement to make before we leave. First ever Monerochan merch more
elaborate than a mug or t-shirt:  https://monerosupplies.com/product/monerochan-standee/

16:53:43 <plowsof11> leito has asked if they should close the proposal https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/355#note_20532

16:53:49 <nioc> <ofrnxmr[m]>  monero isnt even mentioned in the movie <<>> not a fact

16:54:09 <plowsof11> monero is mentioned 14 times in the movie

16:54:13 <monerobull[m]1> That doesn't count

16:54:14 <plowsof11> (i did not count)

16:54:21 <Siren[m]> monero isn't mentioned in any of the dialogues

16:54:34 <Siren[m]> but in songs playing in the strip club, correct me if I'm wrong

16:54:42 <nioc> you are wrong

16:54:45 <Stnby[m]> monerobull[m]1: expensive :(

16:54:47 <Siren[m]> and you only could pay attention to that because you know what monero is

16:54:51 <monerobull[m]1> Siren[m]: While Booba and cocaine

16:55:10 <Siren[m]> nioc: and your correction is? where is it in the dialogue?

16:55:10 <jwinterm[m]> ofrnxmr[m]: I'm not sure I 100% agree that he needs to show the movie to fundraise for
marketing. In the vast majority of CCS the applicant has nothing to show at the proposal stage, and things are
delivered as milestones, right?

16:55:16 <jwinterm[m]> I think he should, but not sure it's totally necessary

16:55:49 <nioc> Siren[m]: when the coin was first shown

16:55:54 <monerobull[m]1> No company pays for ads this way

16:55:58 <nioc> have you seen the movie?

16:56:02 <monerobull[m]1> With the ad already done but they can't see it

16:56:03 <Siren[m]> nioc: does he say "Monero"?

16:56:13 <monerobull[m]1> No

16:56:13 <ofrnxmr[m]> nioc: A background song isnt a mention

16:56:18 <Stnby[m]> nioc: can you post it, I have not seen it

16:56:22 <ofrnxmr[m]> Its not in a script

16:56:22 <plowsof11> nioc which character says Monero? did i miss it?

16:56:25 <nioc> as I recall yes,  Have you seen the movie?

16:56:39 <Stnby[m]> hes asking for XMR to view it which is against the rules

16:56:46 <Siren[m]> nioc, send me it for free

16:57:00 <nioc> I can't

16:57:04 <Siren[m]> prove it

16:57:06 <nioc> link is gone

16:57:17 <Stnby[m]> proposal should be gone too

16:57:40 <Siren[m]> cyrptobro movie I swear

16:57:46 <Siren[m]> s/cyrptobro/cryptobro/

16:57:50 <nioc> Siren[m]: you are declaring things about something that you haven't see, that is my only point

16:58:09 <nioc> plowsof11 probably has a better memory

16:58:10 <ofrnxmr[m]> Everybody want Elon to "say" Monero.

16:58:10 <ofrnxmr[m]> Has tweeted things like "is it fungible though?" Much larger audience and more direct
than the movie

16:58:34 <monerobull[m]1> > <@ofrnxmr:monero.social> Everybody want Elon to "say" Monero.

16:58:34 <monerobull[m]1> >

16:58:34 <monerobull[m]1> > Has tweeted things like "is it fungible though?" Much larger audience and more
direct than the movie

16:58:34 <monerobull[m]1> Elon tweeted "CryptoNote"

16:58:35 <ofrnxmr[m]> Why memory?

16:58:47 <ofrnxmr[m]> monerobull @monerobull:matrix.org:  also the fungible line

16:59:12 <sgp[m]> I think all points have been made on this CCS proposals and core needs to decide what to do
with it

16:59:14 <plowsof11> nioc im struggling to remember anyone actually saying the term monero (other than the
song) i would hope to be corrected if wrong, but my memory cant remember that

16:59:21 <sgp[m]> s/proposals/proposal/

16:59:40 <hinto[m]> <plowsof11> "leito has asked if they should..." <- i agree with close for now, re-open a
more organized ccs after showing work

16:59:41 <Siren[m]> nioc: Yes I have not seen it and I will not pay for it but the director himself says that
it's not in dialogue https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371#note_20475

16:59:49 <plowsof11> thanks hinto

16:59:56 <Siren[m]> also plowsof and monerobull and others saw it

17:00:04 <Siren[m]> and they did not hear monero in a dialogue

17:00:13 <Siren[m]> I trust them, yes

17:00:41 <Stnby[m]> 150XMR for a single word, would still be lmao

17:00:42 <Siren[m]> If you're saying that you heard it, you should post a timestamp or a clip

17:00:46 <monerobull[m]1> I have a question and want your opinion before i embarrass myself with a ccs
proposal

17:00:46 <plowsof11> now im scared if ive been misleading everyone , but i genuinely did not hear it

17:00:47 <Siren[m]> otherwise I don't believe you

17:01:11 <Stnby[m]> Just close lol

17:01:17 <Stnby[m]> * close lol, its a scam

17:01:25 <Siren[m]> if even the people whose ears are conditioned to heard the word "monero" missed it, nobody
will fucking notice it

17:01:39 <nioc> Siren[m]: thx, must be the voices in my head

17:01:57 <plowsof11> the movie itself is high "oscar quality" (yes, i read the oscar rules ( from top to
bottom))

17:02:07 <Stnby[m]> doubt it

17:02:39 <Stnby[m]> what oscar will he get if it will end up on the 1337x.to the second it gets merged

17:02:42 <plowsof11> they have a requirement for the type of camera/film used and it meets the specs etc for a
short live action film

17:03:04 <nioc> so is selsta merged yet?

17:03:20 <selsta> nioc: i just opened it lol

17:04:09 <plowsof11> seems we've just went over time , thank you all for attending , AOB? there is an events
meeting in #monero-events:monero.social in 2 hours

17:04:12 <nioc> I just upvoted, can be merged now

17:04:37 <plowsof11> oh wait, i was trying to resolve a ccs proposal with 0.2xmr in limbo

17:04:48 <plowsof11> we need to say that it is abandonned first https://github.com/plowsof/ccs-wip-
list/issues/2

17:04:53 <plowsof11> thats all

17:04:59 <ofrnxmr[m]> Donate to alpharabius

17:05:08 <monerobull[m]1> Kek

17:05:14 <hinto[m]> checking once again: has plowsof gotten paid yet?

17:05:39 <ofrnxmr[m]> We need confirmation plowsof

17:05:40 <plowsof11> not ready for moneys, i have alot of testing for jberman to do, and lacking in site work

17:05:46 <MSvB[m]> Good meeting everyone and great moderation plowsof @plowsof:libera.chat, dankon.

17:05:48 <ofrnxmr[m]> We need CONFIRMSTION, not excuses

17:05:56 <dimmed6843[m]> https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/371#note_20542

17:05:56 <dimmed6843[m]> This is bad ROI. Does our target audience even care about Oscars?

17:06:04 <Siren[m]> no, we don't care

17:06:04 <ofrnxmr[m]> How many payments have you had?

17:06:30 <plowsof11> i have also not resolved anything yet, 1 payment , i have no problems

17:06:46 <ofrnxmr[m]> Your term is 3 months

17:06:50 <ofrnxmr[m]> That only leaves a few days :P

17:06:52 <nioc> the CCS is just motivation for plowsof11 he is not actually getting paid

17:07:10 <Siren[m]> plowsof ccs is expiring?

17:07:20 <ofrnxmr[m]> ^^^^^^^

17:07:24 <ofrnxmr[m]> Id believe it

17:07:30 <plowsof11> no hours roll over after each period is claimed , so the beatings shall be renewed

17:07:31 <monerobull[m]1> Carrot on a stick

17:08:00 <plowsof11> <3

17:08:03 <monerobull[m]1> Can we discuss the German translation

17:08:10 <monerobull[m]1> Merge it

17:08:12 <ofrnxmr[m]> Lets

17:08:20 <ofrnxmr[m]> Agreed. Merge

17:08:29 <plowsof11> yes ercicione will merge as soon as he gains access to the weblate

17:08:29 <Stnby[m]> Merge!

17:08:39 <monerobull[m]1> And donate funds to GF if we don't hear from the guy within a year

17:08:41 <blankpage[m]> <monerobull[m]1> "I have a question and want..." <- What was this?

17:08:58 <plowsof11> i do not want to perhaps waste time discussing the next steps until "its closed" i do not
like to deal with fantasy

17:09:06 <monerobull[m]1> Translation is done, sitting only partially reviewed on weblate

17:09:33 <Siren[m]> plowsof11: I just low how translations were essentially dead because nobody realized the
translation coordinator was AFK

17:09:35 <plowsof11> per your feedback monerobull and another (if they wish to name themsleve) it will be
merged

17:09:38 <Siren[m]> s/low/love/

17:09:50 <plowsof11> so thank you for pushing it forward after a year

17:09:58 <Siren[m]> Siren[m]: meanwhile someone was raging at me for asking if I can submit a PR for some
langs

17:10:39 <Stnby[m]> Can we elect some lang coordinator some time in the future?

17:10:44 <monerobull[m]1> I've spent like 3 hours reviewing it and while it's not perfect, we can just merge
it, better than leaving the video subtitles on YouTube the way they are right now

17:10:47 <plowsof11> the german translation can be found in these issues, ive attempted to pick the issues
that we can resolve together https://github.com/plowsof/ccs-wip-list/issues

17:11:01 <monerobull[m]1> They are only German for 2 minutes and the go to English

17:11:01 <Siren[m]> Stnby[m]: can we simply not have one?

17:11:10 <Siren[m]> let weblate or some shit merge based on votes

17:11:31 <plowsof11> (realistically)

17:11:39 <plowsof11> ercicione has a language coordinator in training called michaelizer but this is yet to be
confirmed, there is a 'history' there im not fully aware of

17:11:39 <Siren[m]> as those lang coordinators don't care nor help with anything

17:11:40 <Siren[m]> other than locking themselves out

17:11:45 <ofrnxmr[m]> plowsof @plowsof:matrix.org:  what is the point of 6 months vs 3 months if it can be
extended arbitrarily

17:12:04 <ofrnxmr[m]> Claim your milestones and open a new ccs.

17:12:06 <Siren[m]> how in the hell didn't ercicione notice that other one being AFK for so long?

17:12:07 <Stnby[m]> voting would not work, If I translated something in Lithuanian. I am the only one in this
chat :DDD

17:12:13 <ofrnxmr[m]> If you want to do it for free, lower your price..

17:12:26 <plowsof11> my own failings have extended it, ive promised hours on testing/site (my gui
contirbutions are ok though)

17:12:50 <Siren[m]> Siren[m]: thanks to them you will not have turkish/lithuanian/azerbaijani translations

17:12:52 <plowsof11> soon(tm)

17:13:09 <ofrnxmr[m]> Low closes out his ccs after the months are up

17:13:10 <ofrnxmr[m]> Koe*

17:13:12 <ofrnxmr[m]> And opens a new one

17:13:31 <ofrnxmr[m]> What youre doing is just getting screwed into the 6 month deal. Unacceptable

17:13:50 <plowsof11> motivation to pull myself out of it, when i have worked the hours promised sir

17:14:14 <blankpage[m]> Research like Koe's always has less concrete deliverables, so it makes sense to do it
on X months basis

17:14:16 <Siren[m]> plowsof11: not really https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/348#what

17:14:24 <plowsof11> i have been busy trying to get a custom fee of 420.69 xmr on testnet for example

17:14:40 <Siren[m]> they need to pay you

17:14:40 <ofrnxmr[m]> ^^^^

17:15:40 <Siren[m]> plowsof11: that's not in your proposal

17:15:40 <ofrnxmr[m]> Consensus says pay plowsof regardless of what HE thinks

17:15:44 <Siren[m]> ask them for payment

17:15:55 <ofrnxmr[m]> ofrnxmr[m]: Opposite of mj

17:16:10 <plowsof11> thank you for the support, i would feel comfortable to get something resolved and finish
off a few things asap

17:16:11 <plowsof11> lol

17:17:19 <Siren[m]> plowsof11: if it's not about coordinating or providing feedback, please don't wait

17:18:23 <plowsof11> i ave learned all the memes in -community also

17:18:59 <monerobull[m]1> I doubt that

17:19:12 <monerobull[m]1> ALL the memes?

17:19:16 <Stnby[m]> Core release the funds to plowsof please. Thanks sars.

17:19:24 <ofrnxmr[m]> luigi1111:

17:19:36 <ofrnxmr[m]> I second Stnby:  statement. Release the funds

17:19:40 <monerobull[m]1> Plowsof just doesn't want to redeem

17:19:59 <Stnby[m]> Maybe he is threatened by them, you never know

17:20:22 <Siren[m]> I would like to submit a proposal (150 XMR) for conducting the monero sleep experiment on
plowsof. We will keep him awake for the duration of the proposal.

17:20:23 <ofrnxmr[m]> Who is he proving himself to? Not us.

17:20:52 <Lovera[m]> Thanks guys for your comments! A little be later to the meeting sorry! Hi everyone

17:20:57 <ofrnxmr[m]> We all (I think) agree that he should be paid

17:21:02 <selsta> +1

17:21:08 <ceetee[m]> +1

17:21:10 <plowsof11> lovera your proposal will be merged asap

17:21:48 <Lovera[m]> plowsof11: Actually I’m reading all comments ! Thank you for your support

17:24:26 <eudaimon36[m]> +1 most certainly

17:26:48 <ofrnxmr[m]> Hinto, stnby, selsta, eudaimon, Ceetee, siren and myself:

17:26:48 <ofrnxmr[m]> pay plowsof

17:27:17 <plowsof11> 5 of my alts would say that

17:27:25 <eudaimon36[m]> lol

17:27:40 <ofrnxmr[m]> golden0:  can you chime in

17:27:54 <plowsof11> how isnt he banned

17:28:04 <nioc> I have already conducted a successful sleep experiment on plowsof11 resulting in an improved
version

17:28:09 <ofrnxmr[m]> Because he was nice

17:28:10 <ofrnxmr[m]> He never left DM either

17:28:16 <ofrnxmr[m]> OMG why

17:28:27 <plowsof11> he harassed us via PM

17:28:28 <plowsof11> lol

17:28:49 <plowsof11> can not forgive the emotional trauma he has caused me


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

endors update for visibility @mj-xmr ( an update on profitability.py / endors ccs milestones will be requested again for the next meeting in 2 weeks ) 
```
Sorry, wasn't home this weekend. Haven't made any progress so far unfortunately, since I'm still dealing with the
 same shit that's slowing me down - hoping that changes soon. I'm actually working right now on adding support for
 multiple nodes in the configuration, so that the software doesn't stop if the node used goes down (like the supportxmr
 node that the CI used for testing stuff)

```

# Action History
- Created by: plowsof | 2023-01-22T12:31:45+00:00
- Closed at: 2023-01-30T21:37:28+00:00
