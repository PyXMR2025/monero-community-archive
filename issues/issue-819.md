---
title: 'Monero Community Workgroup Meeting: Saturday 08th April 2023 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/819
author: plowsof
assignees: []
labels: []
created_at: '2023-03-29T19:27:25+00:00'
updated_at: '2023-04-10T15:01:01+00:00'
type: issue
status: closed
closed_at: '2023-04-10T15:01:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Because the 8th falls on a holiday weekend, I'll hold a 2nd meeting on the 15th.

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
- New Monero release v0.18.2.2 tagged / released soon.
- Rucknium 2023-03-29 reg ordinals on Monero:
> The mint rate has seemed to slow down over the past 48 hours. As of about 24 hours ago, total number of Mordinal txs were 24,222. Sum of Mordinal tx sizes was 202 Megabytes. Total fees to mint Mordinals was 4.05 XMR.    
> 2023-04-04 Updated Mordinals volume data: https://gist.github.com/Rucknium/67cc9efdf7e43a40c52417611b322d43
- Moneros new release to limit tx_extra delayed. sech1 discovered a potential network split with the patch and provided a bug fix moments later (and another serious bug that could prevent windows users from syncing [#8811](https://github.com/monero-project/monero/pull/8811). jeffro built upon this pull request [#8831](https://github.com/monero-project/monero/pull/8813) which will be merged. Release coming toward the end of this week.    
- BP++ peer review on hold as author aims to have a new version out for April 14th which will include security proofs (thus slightly changing the scope/price. [CypherStack](https://cypherstack.com/) are performing the initial review.
- Jeffro256 working on 'avoid using coinbase outputs as decoys' https://github.com/monero-project/monero/pull/8815
- hinto improves his cpu-only vanity address generator from 5 million guesses a second to over 70 million https://github.com/hinto-janai/monero-vanity#comparison
- 92.221xmr donation to the general fund https://nitter.monero.fail/WatchFund/status/1642419180124135425
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    

5. [CCS updates](https://ccs.getmonero.org/)    
  a. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377)    
  b. [Add maintaining-flatpak-package.md](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/381) -BigmenPixel working through tech. difficulties / on hold.   
  c. [v1docq47 - monerokon 2022 (part 2) and monerotopia 2023 voiceover and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/382)    
  d. [Oceanus ERP Software for Small Businesses](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/383)    
  e. [koe seraphis ongoing support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/384)    
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/810)  
- Close animated videos as "completed" - pay savandra 9xmr 
- Close [P2P Publisher - Monerotopia Mexico City](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/380)  

Meeting logs will be posted here afterwards.  

# Discussion History
## johnr365 | 2023-03-30T13:42:23+00:00
Thanks for the details on the minting of Mordinals. So at the current XMR price of ~$160, that's $648 for the 202 MB. Or $3.21 per MB / ~$3,287 per GB added to the Blockchain.


## plowsof | 2023-04-04T17:15:10+00:00
@johnr365  Rucknium shared some new data - showing that ordinals have dropped over the past 48 hours. someone shared that the fees have been increased in a new update to the mordinals client, and that the front end of the their website will not display any mordinal below a certain fee.

## plowsof | 2023-04-10T14:13:26+00:00
Logs 
```
16:00:12 <plowsof11> time for the 3rd meeting today https://github.com/monero-project/meta/issues/819 ok
thanks ofrnxmr

16:00:21 <plowsof11> hello everyone

16:00:55 <ofrnxmr[m]> grumpy hello

16:01:10 <ceetee[m]> hello

16:01:32 <Lovera[m]> Hello 👋🏻

16:01:56 <ofrnxmr[m]> happy holidays evrryone

16:02:26 <ofrnxmr[m]> glsd you could dedicare your lives, unlike the traitor. lets get this started

16:02:30 <plowsof11> so the next release of Monero which limits tx extra is ready, thank you to those that
have done the gitian hashes thing and made pull requests here: https://github.com/monero-
project/gitian.sigs/pulls the maintainer TheCharlatan is on holiday so cant merge anything atm. Core team are
aware, when binaryfate is available he can push selstas release notes/announcement to getmonero / update the
downloads page

16:03:16 <ofrnxmr[m]> would be nice if people can run it and report back if any issues at all

16:03:23 <hinto[m]> hello

16:04:01 <plowsof11> in my peer list atm , i see 18 public rpc nodes that have updated

16:04:14 <ofrnxmr[m]> what?? should be 19 now

16:04:52 <plowsof11> i have limited outreach, maybe it will see yours soon, thanks

16:05:17 <ofrnxmr[m]> im always connected to you 😈

16:05:40 <plowsof11> so the mordinal devs have nerfed their front end page. if you dont use their updates
software (and pay a high fee) your morbinal wont be displayed

16:06:07 <ofrnxmr[m]> TBD release of fork that adds functionality back

16:06:53 <Lovera[m]> Excellent 💪🏻

16:07:07 <plowsof11> Rucknium of rucknium.me shared the latest stats (showing a dramatic decrease of mordinals
on the blockchain... its basically over before we even had a chance to get the limited tx extra update out
2023-04-04 Updated Mordinals volume data: https://gist.github.com/Rucknium/67cc9efdf7e43a40c52417611b322d43 )

16:07:44 <ofrnxmr[m]> over >> taking a break >> trust me, i promise

16:07:56 <ofrnxmr[m]> wait til payday

16:08:10 <ofrnxmr[m]> 4xmr isa lot of money yknoe

16:08:41 <Lovera[m]> Monero is not for NFTs… that was just a “Temporary trend “

16:08:51 <ofrnxmr[m]> but yeah. "they turned it off" fornow

16:09:11 <Lovera[m]> But it’s good to have ready solutions.

16:09:20 <ofrnxmr[m]> was never a trend, has always been an exploitabke exploit

16:09:36 <ofrnxmr[m]> just someone pissing all over your blockchain saying"i can"

16:09:37 <plowsof11> https://github.com/monero-project/monero/pull/8815 Jeffros pull request here is an
attempt to remove privacy concerns of using bogus coinbase decoys (or only using coinbase decoys when spending
those) - needs review / data to see the implications of this

16:09:51 <ofrnxmr[m]> im also running this on mainnet

16:10:06 <GorillaQuest[m]> all my homies dislike coinbase

16:10:18 <ofrnxmr[m]> and im not seeing any issues. you need to use the updated wallet as well

16:10:32 <ofrnxmr[m]> imo its a big uograde over the ststus quo

16:10:49 <ofrnxmr[m]> jeffro256:  ty for looking into this

16:11:08 <Lovera[m]> plowsof11: Niceee

16:11:28 <plowsof11> it should help increase the effective ring size of a monero transaction (a chart can be
found in this comment from Rucknium) https://github.com/monero-project/research-
lab/issues/109#issuecomment-1387504724

16:11:29 <ofrnxmr[m]> basicsllt my rings are 90+% 2 outs now

16:12:26 <plowsof11> we're closer to 15 than we where after the p2pool hardfork.. hopefully this improves it
further

16:12:51 <ofrnxmr[m]> much much closer ❤

16:13:14 <ofrnxmr[m]> chainalysis punching air

16:14:20 <plowsof11> - 92.221xmr donation to the general fund
https://nitter.monero.fail/WatchFund/status/1642419180124135425 😮 AOB?

16:15:06 <ofrnxmr[m]> always nice to see someone that cares

16:15:07 <plowsof11> ah new release will be deployed on Monday*

16:15:17 <ofrnxmr[m]> nice

16:15:19 <nioc> \o/

16:15:24 <ofrnxmr[m]> new release doesnt inckude jeffros pr

16:15:37 <ofrnxmr[m]> i wish it did 😆

16:16:00 <nioc> relax, we went from ring size of 7 > 11 > 16

16:16:03 <Lovera[m]> ofrnxmr[m]: Need review

16:16:29 <ofrnxmr[m]> nioc: went from effective 7 to 7 to 10

16:16:32 <plowsof11> iirc it needs statistical analysis to be performed on over 100k transactions using the
patch xD

16:16:33 <Lovera[m]> nioc: Slow but safe

16:16:45 <ofrnxmr[m]> plowsof11: not reallt

16:16:54 <ofrnxmr[m]> maybe to prove how much better

16:17:01 <ofrnxmr[m]> not to prove that is IS better

16:17:15 <plowsof11> we tried to release a chainsplit last week, lets take it slow

16:17:18 <ofrnxmr[m]> Lovera[m]: unsafe

16:17:39 <ofrnxmr[m]> ring size bumos were akways a response to inadewuacies

16:18:02 <ofrnxmr[m]> plowsof11: hey, i tested it on testnet #not

16:18:14 <nioc> we should change from esperanto to ofrnxmr

16:18:26 <plowsof11> bumps / inadequacies (cant even type inadqequ.. with a keyboard)

16:19:17 <plowsof11> can jump into the CCS ideas unless we've missed something 🤔

16:19:26 <ofrnxmr[m]> first

16:19:34 <ofrnxmr[m]> bp++ 14th still?

16:19:51 <plowsof11> yep, no further updates there

16:20:00 <ofrnxmr[m]> that ccs might move before we come back? or not sure

16:20:10 <ofrnxmr[m]> ok

16:20:32 <plowsof11> that was the self imposed target, i have not much faith

16:20:53 <ofrnxmr[m]> ok thanks

16:21:02 <ofrnxmr[m]> new ccs ideas?

16:21:27 <plowsof11> will just go through the list starting with:

16:21:39 <plowsof11>   a. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/377)

16:22:26 <nioc> seems that people are satisfied with the changes

16:22:33 <plowsof11> DF is away for april , the original proposal was changed after issues where raised, now
koe gave it the thumbs up (ive deferred my vote to him) and has been discussed in a 'no wallet left behind'
meeting

16:22:43 <ofrnxmr[m]> no wallet /mrl should decide on thr scope and acceptance

16:23:20 <nioc> both koe and rbrunner now approve

16:23:25 <ofrnxmr[m]> lm voting: merge as soon as relevant parties ok it

16:24:35 <Lovera[m]> ofrnxmr[m]: Agree

16:24:43 <plowsof11> i vote , tell mrl we're merging it (so people are pushed into feedback if they disagree)

16:24:55 <plowsof11> then merge it during the week xD

16:25:08 <ofrnxmr[m]> no need for further approval from us imo.

16:25:14 <plowsof11> okay

16:25:15 <ofrnxmr[m]> its up to them

16:25:42 <plowsof11> agree

16:25:46 <plowsof11> b. [Add maintaining-flatpak-package.md](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/381)

16:26:15 <MajesticBank> hm this one is important

16:26:16 <ofrnxmr[m]> few flatpak issues

16:26:16 <ofrnxmr[m]> the build steps are basicallt centralized not on our repo

16:26:27 <ofrnxmr[m]> better than current behavior, so still a go ahead

16:26:55 <nioc> please add rule that the proposer doesn't up or down vote their proposal or the comments on it

16:26:56 <plowsof11> theres some back and forth in the comments there, as i was unsure about what milestone
one would actually get us. BigmenPixel  has improved the workflow build and explained to me that , the monero-
gui repo , will build and push flatpak files directly to flathub.

16:26:58 <ofrnxmr[m]> but id like to look into the possibility of hosting our own flatpak repo with
reproducible builds

16:27:08 <ofrnxmr[m]> nioc: no

16:27:09 <MajesticBank> wait for proof of concept + cryptographic assurances ?

16:27:17 <ofrnxmr[m]> i like seeing the weirdos that do it

16:27:23 <nioc> :)

16:27:41 <plowsof11> the artifacts / hashes we see here flatpak hashes https://github.com/BigmenPixel0/monero-
gui/actions/runs/4643408350 will appear on your machine, when installing monero-gui through flatpak (they will
be seen on the official monero-gui repo)

16:28:00 <MajesticBank> nioc: there are few ccs rule need changing but it's complex process I guess

16:28:12 <ofrnxmr[m]> i think some research is needed on the hosting of our own repo

16:28:48 <MajesticBank> why actions are not run from monero-project github ?

16:29:08 <plowsof11> there will be no

16:29:14 <plowsof11> uhm this repo https://github.com/flathub/org.getmonero.Monero will no longer exist (so im
told)

16:29:15 <ofrnxmr[m]> flathub, at a deeper look, seems to be a good but not ideal option

16:29:32 <ofrnxmr[m]> MajesticBank: flathub rules i guess

16:29:34 <plowsof11> monero-gui repo will push directly to flathub (and hashes can be confirmed)

16:29:39 <MajesticBank> pay the guy for his code / scripts / actions anyway

16:29:44 <monerobull[m]> is there a meeting here

16:29:46 <ofrnxmr[m]> 5 years of people rewuesting reproducible buikds

16:30:19 <plowsof11> i have only found this information out 1 hour ago, so i need to be certain myself whats
going on

16:30:25 <ofrnxmr[m]> monerobull[m]: nope. were just trying to enjoy the holiday but thersles some sort of
gathering here

16:30:31 <ofrnxmr[m]> plowsof told me thrre was lunch

16:30:45 <ofrnxmr[m]> i think he lied

16:31:47 <ofrnxmr[m]> ill stry to help look into the flatpak stuff as well, but imo rstes chsnge (up) if it
involves deploying our own repo

16:31:58 <MajesticBank> i think this distribution needs to be really tight and verified, so let's wait on this
one

16:32:26 <MajesticBank> i still would donate if someone can continue debian repo, apt-get install monero was
amazing

16:32:27 <plowsof11> yeah, i only wrapped my bran around the process an hour ago

16:32:33 <plowsof11> brain*

16:32:56 <ofrnxmr[m]> gui is already in flsthub though, so current situstion is no better

16:33:34 <ofrnxmr[m]> but yes, i agree but i do think there might be another or s different first milestone in
the final ccs

16:33:39 <MajesticBank> i saw flatpak is California based company, not sure are there any privacy implications
there

16:34:06 <plowsof11> monero-gui repo runs a workflow, and spits out artifacts (app.flatpak files) - these same
files are pushed to flathub - which we install through flatpak - we can compare hashes shown on the monero-gui
workflow run - so there is no doubt (ONLY if github collude with flathub)

16:34:08 <hinto[m]> MajesticBank: agree

16:34:20 <hinto[m]> it would affect all downstream distros as well

16:34:22 <hinto[m]> e.g ubuntu mint

16:34:32 <plowsof11> bigmenpixel has been maintaining flatpak monero-gui for 2 years~ now

16:35:17 <plowsof11> and finding out 'wtf is happening with the debian/whonix maintainer' is on the todo list

16:35:27 <MajesticBank> we might not see monero wallet in whonix / qubeos without debian repo, other distros
affected too

16:35:29 <ofrnxmr[m]> i was thinking maybe shorten the ccs to 3 months, with a new ccs for the repo later

16:36:25 <MajesticBank> and there might be a deal with another privacy coin, so need to consider wider picture
on this one

16:36:43 <MajesticBank> *might* *possible* *future*

16:36:56 <plowsof11> at the moment - users can confirm hashes that are @ monero-gui repo , so at least we have
that

16:37:26 <plowsof11> there will be another meeting next saturday, so we can investigate further

16:38:16 <ofrnxmr[m]> so the plan to do xyz_ might be a wate of time. can just keep maintaining as is an then
do the repo (?)

16:38:23 <ofrnxmr[m]> thoughts for next week

16:39:02 <plowsof11> i just know that "verified" status on flathub is a myth/placebo - "verified" for the
monero community is something else, that im trying to ascertain

16:39:26 <ofrnxmr[m]> yeah, blue twitter check

16:39:35 <plowsof11> BigmenPixel: has responded to my questions / been busy setting milestone one up for a
while now, so thank you

16:40:02 <MajesticBank> verified is when you have plowsof police that download package every minute and check
the hashes from 3 different servers

16:40:05 <ofrnxmr[m]> we'll figure it out

16:40:09 <ofrnxmr[m]> whats next?

16:40:28 <plowsof11> next saturday discuss it again 15th with more info/questions in between. also whats going
on with debian

16:40:41 <plowsof11> yes a script to DL and confirm is possible / raise alarm

16:41:00 <ofrnxmr[m]> i mean, next on meeting agenda :P

16:41:22 <plowsof11>   c. [v1docq47 - monerokon 2022 (part 2) and monerotopia 2023 voiceover and working on
xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/382)

16:42:06 <ofrnxmr[m]> no further feedback from russia, i say merge

16:42:18 <plowsof11> the last time v1do put a proposal up - we delayed it for weeks to get feedback, then put
it to funding. he;s been doing this for years, and i already see some positive feedback coming in. not sure
why we would delay now

16:42:31 <ofrnxmr[m]> yeah, merge it

16:42:55 <plowsof11> merge from me also

16:42:58 <ofrnxmr[m]> its a proposak that is repeatedly funded by, i assume, russians

16:43:43 <ofrnxmr[m]> even if they dont comt o #conmunity and make me use a translator, someone is supporting
the work consistentky

16:43:56 <MajesticBank> there is not much feedback from the community tho

16:44:06 <ofrnxmr[m]> were not russian

16:44:22 <ofrnxmr[m]> i csnt tell you anything abiut the quality of output

16:44:29 <MajesticBank> can anyone else comment? I need to get into loop on this one, was thinking it's 18 utc
today

16:44:41 <plowsof11> XD

16:45:09 <ofrnxmr[m]> consensus merge?

16:45:11 <plowsof11> v1do wont start work until start of May? hasnt finished his current ccs

16:45:27 <ofrnxmr[m]> 0 abstain

16:45:27 <ofrnxmr[m]> 1 close

16:45:27 <ofrnxmr[m]> 2 merge

16:45:29 <ofrnxmr[m]> 2

16:45:48 <BusyBoredom[m]> Merge

16:46:58 <plowsof11> 3 - the meeting didnt happen as its a holiday , lets come back next week xD

16:47:07 <ofrnxmr[m]> plowsof11: yep, but he doesnt get paid til may either. no reason to wait to raise funds

16:47:12 <MajesticBank> option 3 wait ?

16:47:17 <ofrnxmr[m]> plowsof11: merge it smh lol

16:47:36 <ofrnxmr[m]> wait for what, russians?

16:47:43 <ofrnxmr[m]> like waiting for mj tk be honest

16:47:47 <ofrnxmr[m]> theyve never ckme before

16:47:51 <plowsof11> wait for me to make a sock account and say thanks

16:48:06 <MajesticBank> I know someone from xmr.ru, will invite him here

16:48:11 <ofrnxmr[m]> i need time to downvote with socks

16:48:16 <MajesticBank> he is owner of monero.net I think

16:48:49 <michaelizer[m]> Is there another channel apart from #xmr.ru:matrix.org ?

16:49:15 <michaelizer[m]> It seems kinda dead even though it has +1000 members

16:49:20 <MajesticBank> they are very active on telegram

16:49:28 <plowsof11> i will follow that up majesticbank (for some extra feedback) - its just a song and dance
before merging it

16:50:01 <plowsof11> yeah they have a ru telegram

16:50:15 <michaelizer[m]> MajesticBank: I thought it was the same, do you have the link to that one by any
chance?

16:50:22 <MajesticBank> https://t.me/xmr_ru_news

16:50:22 <ofrnxmr[m]> i wonder how hard is is for vdo to be 9 russian alts

16:50:43 <michaelizer[m]> Thank you

16:50:56 <ofrnxmr[m]> its not animated videos, nor a meth drinking movie

16:50:56 <MajesticBank> they have active weekly news, there is link to channel in description

16:51:08 <plowsof11> https://web.telegram.org/k/#@XMR_RU also?

16:51:39 <MajesticBank> when I read comments on the proposal, last two, they are too fishy, nothing else

16:52:11 <plowsof11> yeah just make like, 4 ish more sock accounts and say thanks then we can merge

16:52:12 <ofrnxmr[m]> who's funding them? not anybody we know

16:52:23 <michaelizer[m]> plowsof11: Thanks, lol I saw lovera commenting in Russian 🔥

16:52:23 <ofrnxmr[m]> waste if time trying to block it

16:52:45 <ofrnxmr[m]> until someone shoes up with proof, the ccs is as good as its always been

16:52:53 <plowsof11> luigi is slow so we can block it inadvertently until next saturday

16:53:16 <ofrnxmr[m]> im just saying im wasting my tkme voting yes 3 times

16:53:39 <ofrnxmr[m]> like, just fkn merge kt

16:53:40 <Lovera[m]> plowsof11: Sorry, we are about v1docs? Proposal?

16:53:44 <plowsof11> yess

16:53:46 <ofrnxmr[m]> meth movies grt merged on a casual tuesdag

16:54:07 <plowsof11> lovera says yes for the third time today also

16:54:09 <Lovera[m]> I think merge…

16:54:33 <ofrnxmr[m]> ty lovera 👍

16:54:52 <plowsof11> this meeting consensus is merge moving on

16:54:56 <ofrnxmr[m]> rent free, no thanjs

16:54:58 <Lovera[m]> michaelizer[m]: Yeah!! Sometimes I check their community 🙂

16:55:10 <plowsof11> sadly i have no idea what this is   d. [Oceanus ERP Software for Small
Businesses](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/383)

16:55:26 <plowsof11> hinto: and BusyBoredom have left some feedback on the ERP proposal

16:55:42 <ofrnxmr[m]> er.. same, i didnt even look at that one yet

16:55:48 <plowsof11> its not something we can just have a quick look at , and ive not devoted much time into
researching it

16:56:22 <ofrnxmr[m]> Siren:

16:56:25 <plowsof11> will definitely do that before next saturday, but, my initial impression from the
feedback is "cant ya just use an existing thing and add monero to it instead of using your custom made thing"

16:56:36 <MajesticBank> bump for next week ?

16:56:41 <plowsof11> ye

16:56:56 <ofrnxmr[m]> it uses moneropay?

16:56:57 <ofrnxmr[m]> but costs more than moneropay ccs?

16:57:16 <ofrnxmr[m]> yes. bump for nxt week

16:57:18 <Lovera[m]> ofrnxmr[m]: Mmmm

16:57:29 <plowsof11> " Moneropay API or the AcceptXMR library "

16:57:59 <ofrnxmr[m]> thats just as bad

16:58:08 <ofrnxmr[m]> acceptxmr was 44xmr

16:58:22 <plowsof11> its not "sexy" to promote .. needs a long study, but my initial impression is "nah" but i
dont think im fully informed

16:58:41 <ofrnxmr[m]> im again, not commenting on the proposal thus week.

16:58:46 <plowsof11> yep

16:58:52 <ofrnxmr[m]> need to actually look first

16:59:00 <MajesticBank> let's not be gatekeepers, but a shapers, maybe this can be POS solution for shops /
restaurants

16:59:07 <MajesticBank> different interface w/e

16:59:26 <ofrnxmr[m]> we'll look into it and see

16:59:31 <plowsof11> will follow up with the proposer ye

16:59:35 <BusyBoredom[m]> I think it would be much cheaper and more beneficial to integrate monero into an
existing ERP like odoo.

16:59:59 <plowsof11> nice feedback, lets end on   e. [koe seraphis ongoing
support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/384)

17:00:08 <plowsof11> no idea, but i say merge

17:00:21 <ofrnxmr[m]> i vote close

17:00:27 <ofrnxmr[m]> jk.

17:00:42 <plowsof11> i read the title and im voting merge

17:01:13 <plowsof11> koe will be holding a (hopefully) monerokon talk about "Build a demo for a secure and
efficient escrowed market using Monero 2-of-3 multisig with the seraphis library."

17:01:16 <MajesticBank> this sounds interesting

17:01:17 <MajesticBank> Build a demo for a secure and efficient escrowed market using Monero 2-of-3 multisig
with the seraphis library.

17:01:19 <plowsof11> which is funded by this ccs

17:01:25 <MajesticBank> yep

17:01:34 <Lovera[m]> MajesticBank: Amazing

17:01:43 <ofrnxmr[m]> merge it

17:01:54 <plowsof11> the #monero-events:monero.social team are yet to confirm his talk but he has submitted
the proposal

17:01:54 <Lovera[m]> ofrnxmr[m]: +1

17:01:56 <ofrnxmr[m]> koe is essential to other ccs

17:02:24 <BusyBoredom[m]> ERPs are not like payment gateways where businesses add new ones periodically.
Businesses generally use only one ERP, and that ERP becomes very core to their day-to-day functioning. It's
not customer-facing, it's business management software.

17:03:07 <ofrnxmr[m]> they shoukd come to communitt dev and expkain why

17:03:14 <MajesticBank> On the point of monero payment gateway, I think it's waste of time making monero
specific gateway, but rather approach different vendors to add monero into existing solutions

17:03:18 <plowsof11> thank you BusyBoredom for the vital feedback

17:03:24 <MajesticBank> like blockonomics and such

17:03:26 <ofrnxmr[m]> meeting done? ty bye everyone

17:04:11 <Lovera[m]> Can I continue with my whiskey 🥃?

17:04:29 <michaelizer[m]> Lovera[m]: It's semana santa ffs

17:04:56 <Lovera[m]> By the way, today I take out the last video for tomorrow or the day after tomorrow to
give my report

17:05:07 <Lovera[m]> michaelizer[m]: Yeah!!! 🥃🙏🏻

17:05:11 <plowsof11> yep meeting over! thanks for joining, happy weekend everyone sorry for dragging you here!
MajesticBank yes a monero specific gateway does lack appeal to alot of merchants who want to accept every
payment method under the sun

17:05:37 <MajesticBank> Lovera[m]: nice !!!

17:05:54 <plowsof11> they still have their place though. nice one Lovera !

17:06:24 <MajesticBank> https://www.blockonomics.co/, non custodial payment gateway, should be working with
monero easy, crazy amount of vendors are using this one

17:10:00 <plowsof11> what about https://bitcartcc.com/ which has monero support

17:10:30 <plowsof11> multi coin / non custodial but ive never used it


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-03-29T19:27:25+00:00
- Closed at: 2023-04-10T15:01:01+00:00
