---
title: 'Monero Community Workgroup Meeting: Saturday 15th April 2023 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/824
author: plowsof
assignees: []
labels: []
created_at: '2023-04-10T14:25:15+00:00'
updated_at: '2023-04-18T02:12:27+00:00'
type: issue
status: closed
closed_at: '2023-04-18T02:12:27+00:00'
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
    - [Monero v0.18.2.2](https://www.getmonero.org/2023/04/04/monero-0.18.2.2-released.html) released! 
    - [Rucknium](https://rucknium.me/) reports that: "The P2Pool network upgrade on March 18 reduced the coinbase share of outputs from about 18% to about 9%"  [Empiracle privacy impact of Mordinals](https://www.reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/)
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377)    Consensus last meeting = MRL/Dev to decide 
  b. [Add maintaining-flatpak-package.md](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381)    Consensus last meeting = Positive votes , Waiting to make a more informed comment 
  c. [v1docq47 - monerokon 2022 (part 2) and monerotopia 2023 voiceover and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/382)  - Consensus last meeting = Merge
  d. [Oceanus ERP Software for Small Businesses](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/383)    Consensus last meeting = Integrate into an existing solution / Waiting to make a more informed comment
  e. [koe seraphis ongoing support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/384)    Consensus last meeting = Merge
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup https://github.com/monero-project/meta/issues/825
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
    - Monerooutreach dead? some funding available for revival? https://github.com/plowsof/ccs-wip-list/issues/4
    - Whonix monero-gui apt repository.
    BusyBoredom:
    >[22:13](https://libera.monerologs.net/monero/20230409#c234614)BusyBoredom[m]
Anyone know why whonix removed monero-gui from their default installation? [Whonix/anon-meta-packages b38990f](https://github.com/Whonix/anon-meta-packages/commit/b38990fff7200661bfc8ad8d90d308bbc1546feb)
    >[22:14](https://libera.monerologs.net/monero/20230409#c234615)BusyBoredom[m]
The monero-gui repo on their github is gone too. Is there a replacement coming?
    >[22:19](https://libera.monerologs.net/monero/20230409#c234616)BusyBoredom[m]
Ah I found it, they're recommending flatpack now: [forums.dds6qkxpwdeubwucdiaord2xgbbe…-for-virtualbox-point-release/16469](http://forums.dds6qkxpwdeubwucdiaord2xgbbeyds25rbsgr73tbfpqpt4a6vjwsyd.onion/t/whonix-16-0-9-8-for-virtualbox-point-release/16469)
   - [ANN] MajesticBank: you can now earn XMR or your favourite currency just by testing our software, exchange, atomic swaps and similar things. more info in the telegram group https://t.me/majestictesters
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/819)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-04-18T01:59:32+00:00
Logs 
```
11:20:03 <plowsof11> Meeting at 16:00utc here https://github.com/monero-project/meta/issues/824 , and then a
Monerokon meeting at 17:00utc in #monero-events:monero.social https://github.com/monero-
project/meta/issues/821

12:40:55 <plowsof11> thats in 3 hours and 20 mins 😵

12:56:11 <ofrnxmr[m]> Events gotta do something about their meeting time

12:57:33 <ofrnxmr[m]> 2hrs back to back is killer. Any reason ther moved theirs back an hr?

13:02:30 <nioc> daylight savings time

13:03:33 <nioc> so what do people do with all the light you save up during the year?

13:04:36 <ofrnxmr[m]> make lemonade, id think

13:07:07 <ofrnxmr[m]> I could prabably check a newsletter, but do you know if all meeting adjusted for DST?

13:11:03 <nioc> shrug

13:48:17 <plowsof11> MRL @ 17:00 utc still (as 1 utc will always == 1 utc)

13:48:51 <plowsof11> seraphis still @ 18:00utc

13:53:09 <plowsof11> a +9,+0.1,+0.00681 to the general fund today, based

14:00:16 <plowsof11> can we not just merge dangerous freedom, koe, v1do, flatpak and link everyone to
Ruckniums recent stats and call it a day

14:05:51 <ofrnxmr[m]> ajs_ @ajs_:matrix.org:  are yall willing to move your meeting back to 1800utc? (Not
tiday but future ones?)

14:06:09 <ofrnxmr[m]> Seems most other meetings didnt adjust

14:07:03 <ofrnxmr[m]> (Thats a topic for event meeting)

14:12:09 <plowsof11> more detailed stats of flatpak installs from flathub
https://klausenbusk.github.io/flathub-
stats/#ref=org.getmonero.Monero&interval=infinity&downloadType=installs%2Bupdates

14:17:45 <ofrnxmr[m]> Huge volume around HF

14:18:10 <ofrnxmr[m]> And steady growing

14:19:02 <ofrnxmr[m]> And quite a bit more in 2023

14:19:48 <ofrnxmr[m]> ATH!

14:19:57 <ofrnxmr[m]> 1351 old 1353 new

14:20:31 <ofrnxmr[m]> NGU games that i enjoy

14:20:55 <plowsof11> ah, they are installs and updates (can toggle between)

14:24:09 <ofrnxmr[m]> I broke my cookies (?) now it wont load

14:24:37 <ofrnxmr[m]> S'ok. I dudnt see s***, so we can merge it.

15:04:49 <nioc> so we are moving meeting back an hour starting next meeting?

15:04:55 <nioc> ( ͡° ͜ʖ ͡°)

15:06:01 <nioc> conflict will last for only a few more meetings

15:07:18 <nioc> <plowsof11> can we not just merge dangerous freedom, koe, v1do, flatpak and link everyone to
Ruckniums recent stats and call it a day <<>> sounds good to me

15:08:29 <nioc> lucky for me that I was able to get out of a 2.5hr meeting on Wed  o_0

15:24:49 <plowsof11> next meeting at 15:00utc has 3 votes, okay

15:26:30 <plowsof11> nioc that means you have 2.5hours + 1 in the tank :D

16:00:02 <plowsof11> Meeting time https://github.com/monero-project/meta/issues/824

16:00:11 <plowsof11> greetings, hello

16:00:12 <msvb-lab> Hello.

16:00:22 <michaelizer[m]> hello

16:00:38 <ofrnxmr[m]> Hello

16:00:49 <Lovera[m]> Hi everyone

16:01:07 <plowsof11> lets see how quickly we can end this before the events meeting xD Hi Lovera, nice update
you posted recently!

16:01:10 <plowsof11> News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-
xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero
Moon](https://www.themoneromoon.com/)

16:01:54 <Lovera[m]> plowsof11: Thanks 🙏🏻

16:02:38 <plowsof11> Ruckniums latest report reg mordinals, for your reading pleasure
https://www.reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/

16:02:38 <v1docq47[m]> Hello!

16:03:30 <plowsof11> lets breeze through the ccs merge list and swing back to open discussion at the end

16:03:47 <plowsof11>   a. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/377)    Consensus last meeting = MRL/Dev to decide

16:03:47 <Lovera[m]> Very nice report !!

16:04:08 <plowsof11> no blockers , approvement from seraphis dev / group coordinator , merge

16:04:23 <hinto[m]> hello

16:05:07 <hbs[m]> hello

16:06:03 <plowsof11> asking amount of 31 xmr too

16:06:03 <cmiv> greetings everyone

16:06:11 <Lovera[m]> That is… let’s MRL decide what to do with that

16:06:25 <plowsof11> moving on

16:06:31 <plowsof11>   c. [v1docq47 - monerokon 2022 (part 2) and monerotopia 2023 voiceover and working on
xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/382)  - Consensus last
meeting = Merge

16:07:06 <plowsof11> any issues with merging?

16:07:32 <v1docq47[m]> I will be happy to answer questions

16:07:42 <ofrnxmr[m]> not from me. Merge

16:07:46 <Lovera[m]> Merge!

16:08:04 <plowsof11> is there a RU community on IRC/matrix or only telegram?

16:08:33 <v1docq47[m]> telegram + matrix bridge

16:09:05 <plowsof11> what is the matrix channel if i may ask, to have it handy

16:09:57 <plowsof11> (i noticed i went from a - c there)

16:10:29 <v1docq47[m]> https://riot.im/app/#/room/#xmr.ru:matrix.org

16:11:10 <plowsof11> thanks v1docq47[m] will note that down. thnx for your contributions over the years and
future

16:11:39 <plowsof11> so merging, moving on?

16:12:02 <v1docq47[m]> i just do what i love :)

16:12:44 <plowsof11>   b. [Add maintaining-flatpak-package.md](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/381)    Consensus last meeting = Positive votes , Waiting to make a more informed
comment

16:13:47 <plowsof11> stats of happy flatpak monero-gui enjoyers https://klausenbusk.github.io/flathub-
stats/#ref=org.getmonero.Monero&interval=infinity&downloadType=installs%2Bupdates

16:14:26 <plowsof11> BigmenPixel: thanks for the support over the entire time frame

16:14:45 <ofrnxmr[m]> Im good with merging for simply continues support and better path thn current

16:16:21 <plowsof11> just a small logistics issue of getting luigi the token for the gui repo

16:16:30 <plowsof11> then milestone 1 will be completed asap

16:16:38 <plowsof11> merging

16:16:42 <ofrnxmr[m]> yeah np looks good

16:17:05 <plowsof11>   d. [Oceanus ERP Software for Small Businesses](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/383)    Consensus last meeting = Integrate into an existing solution /
Waiting to make a more informed comment

16:17:47 <ofrnxmr[m]> I havent kept up with this one

16:17:50 <plowsof11> no comment ~ feedback so far isnt good + i doubt it will improve unless they dont come
back with the feedback

16:18:13 <plowsof11> will let proposer make a comment

16:18:24 <plowsof11> until then , moving on

16:18:32 <ofrnxmr[m]> 2 more wwks0

16:18:44 <cmiv> I proposed this merge request.  Consensus seems to be to make a plugin for the Odoo python ERP
instead.

16:18:59 <plowsof11> ah sorry, hello cmiv

16:19:00 <cmiv> If so, I'll close it and go back to the drawing board.

16:19:20 <plowsof11> seems like a good idea (but dont do luigis job for him)

16:19:39 <cmiv> Either integrate with Odoo or make a web app interface for Moneropay API.

16:20:24 <plowsof11> #moneropay:kernal.eu team have been active recently btw , and the AcceptXMR ccs is on-
going

16:22:32 <ofrnxmr[m]> plowsof11: I thins sarcasm. Probably yes close it voluntarily

16:23:43 <plowsof11> i would say integrating into an existing solution will have more success, thank you for
taking the feedback onboard cmiv

16:24:06 <plowsof11> lets move on

16:24:27 <plowsof11>   e. [koe seraphis ongoing support](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/384)    Consensus last meeting = Merge

16:25:10 <Lovera[m]> Yeah merge

16:25:20 <ofrnxmr[m]> +1

16:27:29 <plowsof11> moving on

16:27:57 <plowsof11> is everyone sure for not merging the monerotopia p2p idea
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/380

16:28:09 <plowsof11> jut double checking

16:28:24 <ceetee[m]> 🚮

16:28:29 <ofrnxmr[m]> The proposer is eben mord childdish in my dms

16:29:41 <plowsof11> any DM's from proposers after giving feedback (negative or pushing for positive) let us
all know , otherwise i will ask chatgpt to make a diss track about it , cus i dont like to hear about it

16:30:16 <nioc> wasn't that already dismissed?

16:30:26 <ofrnxmr[m]> i dont mind

16:30:32 <ofrnxmr[m]> Issue was the fool wanted to act like a fool when his proposal was still open

16:30:33 <plowsof11> yes , by "father time"

16:30:42 <plowsof11> it just gives me a chance to quickly mention     - Monerooutreach dead? some funding
available for revival? https://github.com/plowsof/ccs-wip-list/issues/4

16:31:00 <plowsof11> we can look into this for the next meeting(s)

16:31:04 <ofrnxmr[m]> monero outreach - as in ^ whatever that is, rip

16:31:13 <ofrnxmr[m]> Monero outreach is far from dead though

16:31:35 <ofrnxmr[m]> We just paid to spread a movie actoss usa

16:31:48 <michaelizer[m]> I see lh1008: is in it, maybe ask him if he knows anything

16:32:05 <plowsof11> thanks michaelizer ❤️

16:32:24 <ofrnxmr[m]> Plenty of proposals woukd fall unser outreach, such as the moneotopia one from a few
minutes ago

16:32:59 <ofrnxmr[m]> But that 36 xmr, yacht fund it with the 242

16:33:11 <nioc> Cat gets 10%

16:33:29 <ofrnxmr[m]> Sorry, 33xmr then

16:34:06 <ofrnxmr[m]> But yes, i think that proposal is long dead. Close it

16:34:46 <plowsof11> i also just want to throw some 'brewing' possible ideas that are coming: molly dev to
finish / maintain wallet-sdk: needs to be put on the ideas so we can discuss everything in one place. and i
was messaged by someone who is interested in making some animated videos (maybe a slightly different idea) for
e.g. 1 milestone of the animated videos proposal.... as a test. but, hasn't yet had time to announce.

16:35:24 <plowsof11> bulletproofs++ author got me on read, 14th was the target for a paper update, lets see
what monday is like

16:35:46 <plowsof11> ANN from majesticbank :   "you can now earn XMR or your favourite currency just by
testing our software, exchange, atomic swaps and similar things. more info in the telegram group
https://t.me/majestictesters"

16:36:55 <plowsof11> mymonero said sorry, twice now : https://nitter.it/MyMonero/status/1646906169364021250

16:37:09 <plowsof11> pls forgiv?

16:37:44 <ofrnxmr[m]> Forgive but dont forget. I credit them with the retraction, even if it was initially
retracted in bad taste

16:38:05 <hinto[m]> speaking of possible ideas, is an alternative monerod frontend something that is needed?

16:38:39 <plowsof11> btw rino is trying to give money away on tweeter competition thing for april
https://twitter.com/RINOwallet

16:39:01 <hinto[m]> i've been wanting to create a more daemon focused gui for a while, something like a
control panel

16:39:03 <plowsof11> alternative to

16:39:14 <ofrnxmr[m]> theres a new swap service. Does anybody remember what its called?

16:39:21 <plowsof11> a running stats page? or different

16:39:35 <plowsof11> trocadoriogo

16:39:39 <hinto[m]> alternative to monero-gui

16:39:59 <ofrnxmr[m]> plowsof11: Thats it

16:40:20 <plowsof11> trocador.app and img

16:40:47 <ofrnxmr[m]> Anyway, majestics new swap service works like trocador (according to majestic = unsafe),
and uses js and cloudflare

16:40:47 <ofrnxmr[m]> Shrug.

16:40:55 <plowsof11> https://intercambio.app/

16:41:15 <ofrnxmr[m]> ^ this is the service

16:42:09 <plowsof11> hinto that seems interesting, i believe tobtoht also has a similar goal on their todo
list

16:42:10 <BusyBoredom[m]> Hinto, id post in Monero Community Dev cause I remember seeing someone post there
about an existing monerod web UI a while back.

16:42:13 <plowsof11> or at least to add local node management

16:42:35 <hinto[m]> i would have thought so

16:42:38 <hinto[m]> many wallet implementations, only 1 daemon

16:42:43 <ofrnxmr[m]> hinto @hinto.janaiyo:matrix.org:  going a but off topic but i dont think i2p-zero should
be removed from getmonero.org

16:43:30 <ofrnxmr[m]> I noticed you approved pr, but i2pzero 1. Works and 2. Could / should be replaced if it
was to be removed

16:43:40 <ofrnxmr[m]> Bitcoin still recommends i2p-zero

16:44:15 <ofrnxmr[m]> (replaced with i2pd instructions)

16:44:24 <ofrnxmr[m]> This is all regsrding the website workfgroup

16:44:43 <plowsof11> definitely needs to be replaced, and not just removed (wait for the replacement first,
better than nothing)

16:45:21 <hinto[m]> i was under the assumption ip2d had taken over as the canonical i2p impl

16:45:54 <plowsof11> i think we can end the meeting there , to allow those who want to attend the events
meeting to get hydrated , thanks all for attending

16:45:54 <ofrnxmr[m]> If so. Replace , not remove

16:46:13 <ofrnxmr[m]> plowsof11: wait wait

16:46:25 <ofrnxmr[m]> Feel free to go if you need to

16:46:43 <ofrnxmr[m]> but there are a few website knitiatives that need attention

16:46:55 <hinto[m]> ofrnxmr[m]: sounds good

16:47:00 <hinto[m]> not sure if i can change the review status

16:47:40 <ofrnxmr[m]> 1. Deleting m'onero outreach

16:47:40 <ofrnxmr[m]> 2. Addind no wallet left behind workgroup

16:47:41 <ofrnxmr[m]> 3...x somerhing i forgot

16:48:39 <ofrnxmr[m]> Both of these were decided without any consult, same as i2pzero

16:49:13 <ofrnxmr[m]> I dont agree with removing outreach

16:49:13 <ofrnxmr[m]> and i dont agree with a "wallet" workgroup.

16:49:13 <ofrnxmr[m]> a seraphis or a "monero-next" workgroup, ok, but not a wallet one

16:49:52 <ofrnxmr[m]> Workgroups arent meant to be short lived. If so, they fall under other workgroups

16:50:00 <plowsof11> we need a -website group meeting 😆

16:50:05 <ofrnxmr[m]> And all of this is -dev

16:50:12 <ofrnxmr[m]> plowsof11: This is it

16:50:31 <plowsof11> back to back to back, the next meeting will be at 15:00UTC

16:50:39 <plowsof11> now you know why

16:50:52 <ofrnxmr[m]> But yeah. Thats all i have to say. Please keep up with -website

16:51:19 <plowsof11> thanks, yes we also have another ongoing site issue about "what wallets to display"

16:51:25 <ofrnxmr[m]> So to confirm: our next meeting will be 1hr earlier

16:51:26 <plowsof11> and the requirements for being listed

16:52:01 <ofrnxmr[m]> Yes yes, that was the other one.

16:52:01 <ofrnxmr[m]> Thank you

16:52:45 <ofrnxmr[m]> Ok thanks everyone listening. See you next time

16:53:30 <v1docq47[m]> Thank for meeting

16:53:38 <Lovera[m]> 👍🏼👍🏼

16:53:45 <plowsof11> there will be a merge bomb coming shortly , please prepare youself

16:54:27 <msvb-lab> Good meeting and great moderation plowsof11, dankon very much.

16:55:01 <plowsof11> thnx msvb-lab

16:55:59 <plowsof11> if n1oc does not report to the community room on the hour, he's getting fired

17:00:17 <n1oc> v1docq47 - monerokon 2022 (part 2) and monerotopia 2023 voice over and working on xmr.ru has
moved to funding! https://ccs.getmonero.org/proposals/v1docq47-monerokon-part-2-and-monerotopia-2023-voice-
over-and-working-on-xmr.ru.html

17:00:45 <n1oc> koe: Seraphis Ongoing Support has moved to funding!
https://ccs.getmonero.org/proposals/seraphis-ongoing-support.html

17:01:13 <n1oc> Maintaining Flatpak package has moved to funding!
https://ccs.getmonero.org/proposals/maintaining-flatpak-package.html

17:01:41 <n1oc> dangerousfreedom - wallet development 2 has moved to funding!
https://ccs.getmonero.org/proposals/df-wallet-development-2.html

17:02:09 <plowsof11> thanks nioc, didnt doubt you a second

17:03:45 <nioc> :)

17:19:03 <plowsof11> reg the -site talk above: here is the PR to "clarify mobile and light wallets section"
https://github.com/monero-project/monero-site/pull/2145/files in essence, reduce the liability of the
getmonero maintainers / core for listing wallets there, and opening the door for listing 'more wallets' - can
share your feedback ideally in #monero-website:matrix.org #monero-site or on the GH issue itself

17:21:46 <ofrnxmr[m]> <n1oc> "v1docq47 - monerokon 2022 (part..." <- Isnt this outreach too

17:33:47 <ofrnxmr[m]> Prs that need oversight... (full message at
<https://libera.ems.host/_matrix/media/v3/download/libera.chat/5e33bf5a6809427da2572e63b845aadae80d87a4>)

20:34:56 <plowsof11> dangerousfreedom: ajs has a question reg your presentatoin, (if it could be in a workshop
format) pls get in touch thanks


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-04-10T14:25:15+00:00
- Closed at: 2023-04-18T02:12:27+00:00
