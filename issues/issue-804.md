---
title: 'Monero Community Workgroup Meeting: Saturday 11th March 2023 @ 16:00 UTC '
source_url: https://github.com/monero-project/meta/issues/804
author: plowsof
assignees: []
labels: []
created_at: '2023-03-02T22:49:07+00:00'
updated_at: '2023-03-13T09:53:29+00:00'
type: issue
status: closed
closed_at: '2023-03-13T09:53:29+00:00'
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
- [v0.18.2.0 released](https://www.getmonero.org/2023/02/26/monero-0.18.2.0-released.html)
- [General Fund transparency report March 2023](https://www.reddit.com/r/Monero/comments/11fslu9/monero_general_fund_transparency_report_march_2023/)
- Our sponsors Forked Networking have a great deal for purchasing many ip addresses https://www.forked.net/
- [XMRstarter](https://xmrstarter.com/) allowing free fundraising campaigns
- [Cake Wallet 4.6.0 + monero.com update: Tor Only Mode & more](reddit.com/r/Monero/comments/11l8cie/updates_cake_wallet_460_and_monerocom_130_tor/)
- MyNero re-brands to MySu + updates (pay-to-many) - https://mysu.dev/
- Rucknium confirms [Monero Transaction Confirmations Are Now 60 Seconds Faster Thanks to HashVault, MoneroOcean, SupportXMR, and Nanopool](https://www.reddit.com/r/Monero/comments/11nu4aj/monero_transaction_confirmations_are_now_60/)
- Guarda wallet has fixed Monero support https://guarda.com/
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/) - Animated video series [Video one Final?](https://www.yewtu.be/watch?v=XJ6p-7GTMdo)

  b. [Standalone AcceptXMR](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/374)    
  c. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/375)    
  d. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377)   
  e. [escapethe3RA Monero Observer maintenance (Spring 2023)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/378)    

delayed:
-   a. [Draft Bulletproofs++ Peer Review](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358)    

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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/798)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-03-12T00:33:16+00:00
Logs 
```
16:00:03 <plowsof11> Meeting time https://github.com/monero-project/meta/issues/804

16:00:15 <plowsof11> Greetings. hi

16:00:30 <Rucknium[m]> Hi

16:00:35 <BusyBoredom[m]> Hi

16:00:36 <ofrnxmr[m]> Greetings

16:00:45 <gnuteardrops[m]> Hi.

16:00:57 <paradexical[m]> Hello!

16:01:48 <hinto[m]> hello

16:02:00 <ofrnxmr[m]> Gnutesrdrops is the designer of our hard fork logo ♥️. Thank you and hello

16:02:58 <plowsof11> hi there, since the last meeting weve seen [v0.18.2.0
released](https://www.getmonero.org/2023/02/26/monero-0.18.2.0-released.html), and the [General Fund
transparency report for March
2023](https://www.reddit.com/r/Monero/comments/11fslu9/monero_general_fund_transparency_report_march_2023/).
Lets talk about some other community highlights!

16:03:29 <plowsof11> i see Rucknium released some research recently

16:03:36 <ofrnxmr[m]> P2pool hard fork coming soon. 18.2.0 and p2pool 3.0+ are required!

16:04:28 <plowsof11> the latest Monero GUI + hintos GUPAX are ready and waiting 🚀

16:04:52 <Rucknium[m]> Yes. 60 second faster transaction confirmations after pools changed their
configurations on my suggestion:
https://www.reddit.com/r/Monero/comments/11nu4aj/monero_transaction_confirmations_are_now_60/

16:05:01 <plowsof11> earlier today i stumbled upon a reproducible windows installer for p2pool
https://github.com/WeebDataHoarder/p2pool-nsis (from DataHoarder) - its 2 years old but ive not heard about it
until now

16:05:27 <plowsof11> Thanks Rucknium and all those that contributed

16:05:34 <DataHoarder> produced it for a xmrvsbeast incentive

16:06:11 <plowsof11> nice work DataHoarder

16:06:37 <DataHoarder> send questions this way, but I haven't had time to add nicer things to it, works
otherwise. it is a powershell script to plug things together, plus installer

16:06:56 <hinto[m]> Rucknium: i was wondering, are those diagrams directly produced from the code?

16:07:10 <Rucknium[m]> Yes

16:07:30 <plowsof11> i will test it out today DataHoarder

16:08:09 <Rucknium[m]> Here: https://github.com/Rucknium/misc-research/tree/main/Monero-TX-Confirm-Delay

16:08:09 <Rucknium[m]> I need to give it a readme and a license

16:08:27 <plowsof11> some mobile wallet news: [Cake Wallet 4.6.0 + monero.com update: Tor Only Mode &
more](reddit.com/r/Monero/comments/11l8cie/updates_cake_wallet_460_and_monerocom_130_tor/) and MyNero re-
brands to MySu + updates (pay-to-many) - https://mysu.dev/ (from pokst)

16:08:44 <Rucknium[m]> The Dec-Jan data is here: https://rucknium.me/data/ . I need to post the more recent
data still

16:09:32 <plowsof11> fundraising alternatives: [XMRstarter](https://xmrstarter.com/) allowing free fundraising
campaigns (free as in free beer)

16:09:55 <Rucknium[m]> hinto: If you say you want to reproduce the graphs, that gives me an incentive to
create the README :)

16:10:35 <plowsof11> aand i hope we are all sitting down for this next highlights. Guarda wallet has fixed
Monero support https://guarda.com/

16:10:48 <hinto[m]> do you have any experience with gnuplot? i have tons of data i'd like in graphs and was
considering between that, R and python

16:11:47 <ofrnxmr[m]> Protonwallet.org is a new wallet being promoted on r/darknet

16:11:47 <ofrnxmr[m]> Id beware of it.

16:11:59 <Rucknium[m]> hinto: No experience with gnuplot. If you want pointers on R plots, I would be happy to
give them

16:13:06 <plowsof11> a kind botnet has been solo mining for us also

16:13:51 <plowsof11> solo miners update their block templates the quickest , thank you

16:14:13 <ofrnxmr[m]> There is also a very nice sponsor of ours..

16:14:22 <plowsof11> i wonder if this would have any effect on Ruckniums research , if they are indeed solo
mining

16:14:58 <Rucknium[m]> In the graphs, any solo miners would be included in the "other" category

16:15:02 <plowsof11> ah yes , thanks for reminding us ofrnxmr : a message from our sponsors Our sponsors
Forked Networking have a great deal for purchasing many ip addresses https://www.forked.net/

16:15:13 <ofrnxmr[m]> They are using xmr 6.18 so...hop

16:15:14 <ofrnxmr[m]> Nope

16:15:14 <ofrnxmr[m]> s/xmr/xmrig/

16:15:18 <plowsof11> ah ok

16:15:49 <hinto[m]> Rucknium: i was leaning towards R after seeing how nice the charts were

16:16:26 <hinto[m]> C syntax is also familiar :D

16:16:30 <Rucknium[m]> It uses ggplot ("Grammar of Graphics"). I also use base R plot for some things

16:16:31 <ofrnxmr[m]> The Tldr on forked - there are 750+ Sybil node ips that were are from fork

16:17:06 <ofrnxmr[m]> About $1500 to purchase 256ips for a year

16:17:10 <Rucknium[m]> You can find other R plots on my blog posts: https://rucknium.me/

16:18:09 <plowsof11> seems like we can move onto the ccs merge list, mainly acceptxmr, unless we have some
more things to talk about

16:18:17 <hinto[m]> i'll be copying your code if you don't mind

16:18:23 <ofrnxmr[m]> Just wanted to plug cake quickly

16:18:50 <plowsof11> stackwallet has coin control for bch and ltc wut

16:18:51 <ofrnxmr[m]> Cakes latest update has a new feature that forces exchanges and fiat api calls over
onions

16:19:00 <ofrnxmr[m]> plowsof11: Also has a new monero theme

16:19:33 <ofrnxmr[m]> Alright. Acceptxmr

16:19:44 <plowsof11>   b. [Standalone AcceptXMR](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/374)

16:19:59 <ofrnxmr[m]> Im ofrnxmr. Busyboredom, do you acceptxmr?

16:20:24 <BusyBoredom[m]> Yep, I acceptxmr

16:20:44 <plowsof11> has recently been changed to include an extended maintenance amount as per community
feedback. reminder than merging this will officially close xmrsale / and fund acceptxmr with the remaining
funds

16:20:53 <ofrnxmr[m]> What is the balance of xmrsale?

16:20:56 <ofrnxmr[m]> Refresher

16:21:11 <plowsof11> 30 XMR abandoned

16:21:16 <plowsof11> for 1 year

16:21:18 <Rucknium[m]> hinto: Some animated graphs at the bottom :) https://rucknium.me/html/spent-output-age-
btc-bch-ltc-doge.html .Interactive R charts (using plotly) Data is slightly wrong. "beta" is in the URL:
https://beta.redteam.cash/

16:21:35 <Rucknium[m]> Sure you can copy the code

16:22:03 <plowsof11> so those funds are going to be re-purposed to fund something 'similar , but better'

16:22:26 <ofrnxmr[m]> 30xmr from xmr sale is redistributed into

16:22:26 <ofrnxmr[m]> 14+10 milestones

16:22:26 <ofrnxmr[m]> 6 for maintenance

16:22:26 <ofrnxmr[m]> + 14xmr from community remainder of maintenance

16:23:02 <BusyBoredom[m]> Yep exactly

16:23:05 <plowsof11> those htat have thumbed up the proposal already, does your opinion remain the same after
the changes above?

16:23:28 <ofrnxmr[m]> Merge

16:23:37 <plowsof11> any one have any questions? or would like to voice the vote on merging or not?

16:23:44 <Rucknium[m]> My thumbs up stays

16:25:05 <plowsof11> i think luigi1111 should do the needful

16:25:55 <hinto[m]> +1 merge

16:25:57 <ofrnxmr[m]> (The footnote is that busy said they need to finish 0.12 or something first), so ccs
milestone 1 depends on that as well👍

16:26:24 <plowsof11> the more unpaid work the better, love to see it

16:26:31 <plowsof11> xD

16:27:35 <plowsof11> anyone just seeing this for the first time is more than welcome to voice their vote but i
think we can move on , should be merged

16:27:59 <ofrnxmr[m]> Let it go to funding

16:28:00 <plowsof11> c. [Computational work for OSPEAD parameterization](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/375)

16:28:34 <plowsof11> Rucknium: there was a test, and you where happy with it (even though it looks like
isthmus was the one who completed the test? from the commits)

16:29:02 <plowsof11> we are waiting for isthmus to make a final response

16:29:05 <ofrnxmr[m]> Mj claims to be in competition still lol?

16:29:08 <Rucknium[m]> See isthmus's latest comment. We've gotten into detailed discussions. E.g. which
specific lines of R code need to be converted in C++ and what would be required to do it.

16:29:09 <ofrnxmr[m]> > My case is still open, mainly due to the fact, that there was no deadline for
organizing the funds. I'm still waiting for @sgp 's reply to our official letter from the 23st January, so
almost a month now, before I'm forced to go all in with external help.

16:30:09 <ofrnxmr[m]> > I’ll update the proposal accordingly and add another comment. (I’ll also circle back
and answer the questions from above comments)

16:30:09 <ofrnxmr[m]> Is this the latest comment?

16:30:15 <Rucknium[m]> plowsof: The R test workflow package was uploaded as one commit. For example, I wrote
the skeleton of the package, but the commits don't indicate that.

16:30:19 <plowsof11> so its progressing along nicely , thank you for providing a test for them to complete

16:30:58 <ofrnxmr[m]> Sounds good. Im ok with waiting.

16:32:02 <plowsof11> yep not much to say

16:32:04 <Rucknium[m]> The C++ that Geometry Labs wrote is in the /src/ directory in the repo. Tests are in
/tests/

16:32:06 <Rucknium[m]> The README is descriptive

16:32:17 <plowsof11> just hope that isthmus is more active

16:33:13 <plowsof11> the research appears to be fundamental to the monero project, would you agree Rucknium?

16:35:02 <Rucknium[m]> A good decoy selection algorithm is critical for protecting Monero user privacy. I have
quotes from several sources saying so in the introduction of
https://github.com/Rucknium/OSPEAD/blob/main/OSPEAD-Fully-Specified-Estimation-Plan-PUBLIC.pdf

16:35:03 <Rucknium[m]> I would agree that's it's fundamental to the Monero Project.

16:35:32 <plowsof11> thank you

16:36:11 <plowsof11> thanks for being here (on behalf of isthmus lol)

16:37:25 <plowsof11> ok lets move on

16:37:33 <plowsof11>   d. [dangerousfreedom - wallet development 2](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/377)

16:37:47 <plowsof11> is new / awaiting mrl / -dev feedback

16:37:51 <Rucknium[m]> The importance of this has been recognized as early as January 2015 (see the PDF
above). This is the first feasible procedure to directly estimate the real spend distribution (and therefore
get a good mimicking decoy selection algorithm) with fully anonymized Monero transaction data.

16:38:09 <plowsof11> ah sorry, thanks^

16:38:21 <ofrnxmr[m]> One question I have, is this possible to run on more recent data?

16:39:24 <Rucknium[m]> ofrnxmr: Me? Yes. It will be run on the most recent data possible. I know the proposal
says up to Oct 2022, but that was assuming a particular timeline of events/review pace, etc

16:40:12 <Rucknium[m]> The "dry run" in my OSPEAD repo on GitHub is on old data because it is a dry run.

16:40:28 <ofrnxmr[m]> Oh, perfect.

16:42:44 <ofrnxmr[m]> Im not sure what to make of dangerousfreedoms ccs - is this dev or dev/research?

16:43:19 <plowsof11> reg the dangerous freedom proposal - theyve had a performance review from koe of the
previous ones, and ive left a 'not so positive' comment (from a none-technical / logistics stand point

16:43:57 <ofrnxmr[m]> Too bad koe isnt in here. vtnerd:

16:44:11 <Rucknium[m]> It looks like there has been disagreement between koe and dangerousfreedom on specific
things. That's pretty normal. I hope they are communicating as they go on. koe is not dangerousfreedom's boss.
But they have to find a way to work together.

16:44:48 <dangerousfreedom> It would be good if koe could better clarify his points as I didnt understand
either.

16:45:23 <dangerousfreedom> ofrnxmr[m]: My work would be restricted to the wallet development

16:45:26 <Rucknium[m]> What I mean is that whatever their disagreements, dangerousfreedom and koe shouldn't go
down paths without communicating and then have to throw away work.

16:45:37 <dangerousfreedom> There is not much research now

16:45:38 <ofrnxmr[m]> ^ thats my worry

16:45:47 <ofrnxmr[m]> (@ruck)

16:45:48 <plowsof11> i will make sure to ask for some more feedback at the next "no wallet left behind
meeting"

16:45:59 <ofrnxmr[m]> Monday?

16:46:28 <plowsof11> yep, Monday, 2023-03-13, 18:00 UTC

16:46:36 <plowsof11> in #no-wallet-left-behind:monero.social

16:47:00 <Rucknium[m]> NoWalletLeftBehind meetings should be resolving issues. That's what they are there for.
if DF cannot attend them due to scheduling conflicts, then maybe the time should be moved.

16:48:05 <selsta> I think the problem was with the wallet dev side of things, this was produced from over 300h
funded work: https://github.com/UkoeHB/monero/compare/seraphis_lib...DangerousFreedom1984:seraphis_lib:prototy
pe_wall3_d1?expand=1

16:48:24 <selsta> there were good things (jamtis-checksum related code) but a lot of the wallet3 code was
simply copied from wallet2, this is the wrong approach

16:49:21 <plowsof11> reg scheduling , i wasn't aware (ive seen many updates from Df during meetings)

16:49:30 <dangerousfreedom> Not really. I spent much more hours in the knowledge proofs than the wallet
development

16:49:42 <Rucknium[m]> Something is not working in the NoWalletLeftBehind meetings if the overall approach
isn't being decided there

16:49:59 <dangerousfreedom> I thought it would be easier but it wont in the end

16:50:00 <selsta> dangerousfreedom: according to your ccs you spent 100xmr on wallet dev work, out of 120

16:50:01 <dangerousfreedom> It was 3/5 knowledge proofs and 2/5 wallet

16:50:10 <selsta> that's how I came to the hours

16:50:30 <dangerousfreedom> Yes. That was what was planned but that was not what happened

16:50:38 <plowsof11> the meetings decide purse / wallet / enote / output - if you have an active ccs you need
to communicate with the creator / developer of seraphis for how you can help them

16:50:50 <ofrnxmr[m]> Rucknium[m]: The group is named "no wallet left behind" but its somehow ..hijacked..
development of everything seraphis

16:51:35 <dangerousfreedom> I thought it would be easier in the beginning but in the end was not. But the
result was a better framework than what we have currently.

16:52:57 <ofrnxmr[m]> I think some of these seraphis conversations should move to -dev, am I wrong for
thinking that way?

16:54:14 <plowsof11> is there a scheduling issue?

16:56:28 <plowsof11> its a new idea and needs discussion, thank you for those who have shared input so far

16:56:59 <plowsof11> we also have   e. [escapethe3RA Monero Observer maintenance (Spring
2023)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/378)

16:57:11 <ofrnxmr[m]> 3 months flies!

16:57:27 <ofrnxmr[m]> (Only 1 month in plowsof time)

16:58:01 <gnuteardrops[m]> +1

16:58:10 <ofrnxmr[m]> Oi, I want plowsof to close out his ccs asap. Been 6(?) Months

16:58:16 <ofrnxmr[m]> +1 to observer

16:58:29 <plowsof11> ive just placed a thumbs up on observer +1

16:58:33 <ofrnxmr[m]> Merge it. Lots of events coming up

16:59:06 <Rucknium[m]> +1 observer

16:59:44 <Rucknium[m]> I have one small item from MAGIC

16:59:52 <hinto[m]> plowsof was merged: Oct 6th, 2022

17:00:15 <ofrnxmr[m]> 5 months 👀

17:00:56 <hinto[m]> should be closed and opened again

17:00:59 <Rucknium[m]> Someone submitted a proposal to Magic for about 2,500 USD equivalent to integrate
Monero into this + 12 months of maintenance. We wanted to get community feedback on it. They have built a
draft for Zcash (maybe other coins too): https://app.alphaday.com/b/e7267b7268d4da17bcc146cf9efb05d4

17:01:14 <hinto[m]> and compensated for overtime

17:01:14 <ofrnxmr[m]> hinto[m]: Do we have to do it for him?

17:01:37 <Rucknium[m]> I guess it would be a more polished https://themonero.dance/

17:01:51 <hinto[m]> all up to plowsof himself

17:02:01 <ofrnxmr[m]> : luigi1111w: luigi1111:  do the thing

17:02:01 <ofrnxmr[m]> Observer

17:02:01 <ofrnxmr[m]> Acceptxmr

17:02:01 <ofrnxmr[m]> Close out plowsof

17:03:21 <gnuteardrops[m]> If any community project needs me let me know.

17:04:21 <plowsof11> this meeting shall conclude my 3 months of ccs coordination 🥹 its been a journey.
mistakes where made and lessons have been learned (threat of legal action only twice). thank you to everyone
who has helped me / had positive things to say. overall my goal has been to leave a positive impact on this
community and 'help'. hopefully i  can continue to do the same moving forward. this was the first ccs /
strange role kind of, so i

17:04:21 <plowsof11> assume there will be changes made / areas where i should focus on more / improve on etc.

17:04:21 <ofrnxmr[m]> gnuteardrops: yes we do

17:05:13 <blankpage[m]> gnuteardrops there is some debate about Monerokon graphics in #monero-
events:monero.social

17:05:31 <escapethe3ra[m]> good job plowsof

17:06:06 <ofrnxmr[m]> blankpage[m]: And a meeting there in 1hr to settle it

17:06:10 <hinto[m]> Rucknium: seems strange that payment is needed for integration

17:06:41 <hinto[m]> wouldn't it behoove a "crypto" dashboard site like this to include everything they can?

17:06:49 <ofrnxmr[m]> I like monerobull's / izamenace graphana

17:06:55 <blankpage[m]> Rucknium I'm not 100% clear on the remit of MAGIC but paying for integration into a
dashboard doesn't seem like critical work for the monero project

17:07:40 <Rucknium[m]> It's not critical, but it's pretty cheap. MAGIC has funded only two things in the past
year.

17:07:51 <monerobull[m]> What

17:07:52 <monerobull[m]> Is there a meeting today

17:07:55 <monerobull[m]> I thought there was one last week

17:07:56 <Rucknium[m]> If you don't want it, that feedback will go back to the committee

17:08:17 <blankpage[m]> Congrats plowsof @plowsof:matrix.org you've excelled in the role

17:08:24 <ofrnxmr[m]> <monerobull[m]> "Screenshot 2022-08-17 133004.png" <- ^

17:08:38 <ofrnxmr[m]> Re dashboard

17:08:49 <plowsof11> i have almost resolved ONE issue, its a great day

17:09:17 <ofrnxmr[m]> Damn, we missed out on the juicy issues today.

17:09:43 <ofrnxmr[m]> I think those animated videos should be halted / cancelled or otherwise

17:09:43 <plowsof11> thanks blankpage

17:10:11 <dani-g5x[m]1> What version of Monero gui should I use?

17:10:20 <hinto[m]> ah i've caught up with the animated video discussion

17:10:24 <plowsof11> we ran over time, but yes, there are at least several people unhappy with the animated
videos ccs

17:10:26 <ofrnxmr[m]> dani-g5x[m]1: V0.18.2.0

17:10:37 <ofrnxmr[m]> Download from getmonero.org

17:10:37 <hinto[m]> to be honest i'm a little disappointed

17:10:39 <blankpage[m]> The eyeball meatball was a raging red flag

17:11:00 <dani-g5x[m]1> ofrnxmr[m]: Great, that's what I use (self compiled in Gentoo obviously  :D)

17:11:05 <plowsof11> after nearly many months ^

17:11:12 <ofrnxmr[m]> hinto[m]: Quality quoted at 1k/hr. A year later we get an eye in a cage

17:11:16 <plowsof11> nearly/many? was it almost a year

17:11:22 <ofrnxmr[m]> Now stumbling through scripts and AI voices

17:11:27 <plowsof11> 1k/minute

17:11:39 <ofrnxmr[m]> Correction ^^

17:11:51 <plowsof11> 1k/hour? slave labour??

17:12:48 <hinto[m]> i (maybe unfairly) expected videos similar to the previous ones

17:13:16 <plowsof11> thanks for sharing your feelings hinto, you and i where very positive about this ccs in
the beginning (judging by the comment left on it)

17:13:16 <hinto[m]> on the other hand, withholding payment seems harsh

17:13:41 <dani-g5x[m]1> dani-g5x[m]1: Nobody care

17:14:03 <blankpage[m]> Idk whether people agree but I genuinely like the old simple animations on getmonero.
The 3D backgrounds are noisy

17:14:05 <plowsof11> dani-g5x , thank you for stuggling with our terrible docs to self compile on gentoo

17:14:08 <ofrnxmr[m]> Im not talking about withholding payment 🙏 hinto @hinto.janaiyo:matrix.org:

17:14:26 <ofrnxmr[m]> I would like to pay them in full for video 1 and stop before they go make even more of
this

17:14:50 <dani-g5x[m]1> plowsof11: It was just adding the overlay, ```emerge monero-gui```

17:14:57 <blankpage[m]> Seems fair

17:14:58 <ofrnxmr[m]> Or, they need to finish video 1 acceptable before moving in to video 2 milestone

17:15:38 <plowsof11> dani-g5x if anything is missing (emerge monero-gui?) to allow self compiling an issue /
or pull request on github would be appreciated

17:16:44 <dani-g5x[m]1> plowsof11: What do you mean by "anything is missing"? Portage (Gentoo's package
manager) solves the dependencies and set the compiler flags for me.

17:17:01 <plowsof11> ah no worries then 👍️

17:17:20 <ofrnxmr[m]> dani-g5x:  all is working well?

17:18:08 <dani-g5x[m]1> ofrnxmr[m]: Guess so, alao the monero package was installed and I have an openrc
service for monerod, I don't have that enabled as default should I?

17:18:32 <dani-g5x[m]1> But yeah the GUI wallet works good

17:18:44 <plowsof11> reg animated videos: lets be honest - if they where to re-apply for funding (after being
paid for video 1) how would their ccs go?

17:18:57 <plowsof11> merged?

17:19:51 <hinto[m]> i think the updated animation is good but yes the timescale has been pretty stretched

17:20:09 <hinto[m]> original estimation was 1 video per month and its been 11 months since merge

17:20:23 <plowsof11> the compromise for video 1, which ive asked for , is to release the raw files. (without
subtitles / audio) just the animations

17:20:37 <ofrnxmr[m]> And they are either rushed or they are incapable of writing scripts or voicing them

17:20:46 <ofrnxmr[m]> Rushing*

17:21:24 <Lovera[m]> <ofrnxmr[m]> "Or, they need to finish video..." <- +1

17:21:51 <ofrnxmr[m]> Lovera @btclovera:matrix.org:  that being said, its been 11 months

17:22:29 <plowsof11> before making the proposal, savandra (living in ukraine) was not aware of what was to
happen. so this + energy cuts has played a role in their performance (lack of)

17:22:49 <ofrnxmr[m]> I understand.  But after 11 months the eye video?

17:23:00 <ofrnxmr[m]> And dsm writes scripts from Ukraine?

17:23:32 <ofrnxmr[m]> 11 months and couldnt find a voice actor in a country that isnt at war?

17:23:32 <ofrnxmr[m]> Or close the ccs and say "busy. At war. Ill be back later"

17:23:42 <ofrnxmr[m]> And then come back with the eye video? Loo

17:23:56 <plowsof11> after threat of ccs closure - they produced video 1 and started doing leg work ,
obtaining feedback for script 1

17:24:06 <plowsof11> (hiring outside help)

17:24:21 <hinto[m]> i'm ok with letting this ccs extend indefinitely, as long as they can finish and get paid

17:24:34 <Lovera[m]> plowsof11: This is understandable. We could then simply pause everything and continue
later. So everything is clear

17:24:37 <plowsof11> at this point im not sure who is doing the animations. i know some guy on reddit gave
them an ai voice over (which they are trying to pass off as being human)

17:24:37 <Siren[m]> I like how the video looks currently. I think you guys should cut them some slack.

17:25:00 <dani-g5x[m]1> I have another question: these are the ebuild where I donwloaded monero and monero-
gui: https://bpa.st/2TWTO https://bpa.st/43WPA do you guys think they don't have anything sus in there

17:25:23 <monerobull[m]> Siren[m]: This is 630$ per minute

17:25:33 <monerobull[m]> Or a little less now

17:25:36 <Lovera[m]> Siren[m]: The video looks good. I think so too. But I think there are some mistakes.
Errors that shouldn't be there for the price demanded no?

17:25:51 <Siren[m]> There shouldn't be any errors

17:25:59 <ofrnxmr[m]> The quoted price is higher than a professional studio

17:26:08 <Siren[m]> I don't think you should close it but 630$ per minute is way too much

17:26:10 <dani-g5x[m]1> dani-g5x[m]1: plowsof:

17:26:18 <Siren[m]> Siren[m]: You shouldn't have offered that in the first place

17:26:31 <Siren[m]> What is this Pixar?

17:26:35 <ofrnxmr[m]> dani-g5x:  come over to #monero-support:monero.social  or #monero:monero.social

17:26:38 <plowsof11> dani-g5x: are you seriously that impatient, i seen the message

17:26:52 <ofrnxmr[m]> Siren[m]: They asked for 1000/min

17:27:00 <ofrnxmr[m]> Got merged a year ago in scamming times

17:27:29 <ofrnxmr[m]> The ccs has 100+ donations (seemingly fake microdonations to pump the number)

17:27:51 <dani-g5x[m]1> plowsof11: Sorry

17:27:52 <dani-g5x[m]1> ofrnxmr[m]: Oh 👍

17:27:53 <ofrnxmr[m]> I can tell you I didnt vote for it and never would have voted for such a ridiculous ccs

17:28:29 <Siren[m]> Bruh next time you're approving CCS proposals for media consider checking how much other
people are offering

17:28:30 <Siren[m]> That is indeed insane

17:28:46 <monerobull[m]> Axe it

17:28:56 <monerobull[m]> No more scam videos

17:29:09 <Siren[m]> Siren[m]: Go employ CCS treasurer lmao

17:29:10 <ofrnxmr[m]> It was opened in questionable faith, and the quality of the product does not match what
was even closed to expencted

17:29:24 <Siren[m]> Siren[m]: Plowsof coordinates and this person should evaluate the price

17:29:30 <monerobull[m]> ofrnxmr[m]: 🪓

17:29:30 <ofrnxmr[m]> As this ccs is literally pieces, I want to pay them for video 1, and not continue the
relationship

17:29:42 <ofrnxmr[m]> CCS proposers are free to quit, we should be free to fire them

17:30:03 <monerobull[m]> Yes

17:30:05 <monerobull[m]> Axe

17:30:14 <monerobull[m]> Pay the first one

17:30:17 <monerobull[m]> Them 🪓

17:30:21 <plowsof11> Siren this is a great point, at no point did i think 'hey, lets obtain a quote from
elsewhere' - i based my opinions off the previous work, fun/cool/informative 2d videos that big youtubers had
used and lazily thought 'yes'

17:30:24 <monerobull[m]> * Then 🪓

17:32:14 <plowsof11> e.g. bulletproofs++ peer review, multiple companies where contacted and prices/time
frames where obtained / compared

17:32:14 <monerobull[m]> Because we don't make marketing videos

17:32:18 <ofrnxmr[m]> https://www.wired.co.uk/article/corporate-memphis-design-tech

17:32:29 <ofrnxmr[m]> The first one was cookie cutter shit anyway

17:32:41 <plowsof11> i wasnt a ccs coordinator back then also so pls forgiv

17:32:48 <ofrnxmr[m]> And "block reward is 0.3xmr" in the first ones lol

17:32:52 <monerobull[m]> Plowsof don't worry

17:32:55 <monerobull[m]> We got scammed

17:33:21 <monerobull[m]> There is no discussion to be had here

17:33:33 <monerobull[m]> Pay the first video out, cancel the rest

17:34:34 <Mister[m]> What is the problem guys? Not following the discussion really but I'm open to
finish/create any video/promotional work for free

17:34:47 <ofrnxmr[m]> #monero-events:monero.social

17:34:54 <ofrnxmr[m]> There will be a bounty of 3500 given away there in the next 25 minutes or so

17:35:02 <Siren[m]> ofrnxmr[m]: ??

17:35:10 <luigi1112> merge some things?

17:35:12 <Siren[m]> What in the hell

17:35:21 <ofrnxmr[m]> Mister:  for logos, artwork etc

17:35:25 <ofrnxmr[m]> luigi1112: Yes sirrrrr

17:35:30 <Lovera[m]> I’m not sure we can cancel after funding… Maybe we can pause it waiting properly video

17:35:38 <monerobull[m]> Lovera[m]: Of course we can

17:35:41 <plowsof11> Mister context: Animated video series [Video one
Final?](https://www.yewtu.be/watch?v=XJ6p-7GTMdo)

17:36:14 <Siren[m]> We can ask them to send project files, HQ render as well of the video

17:36:15 <plowsof11> thats my real voice

17:36:15 <luigi1112> 374

17:36:18 <luigi1112> 378?

17:36:18 <Siren[m]> Siren[m]: And close it

17:36:43 <Siren[m]> Siren[m]: Someone else can work with those

17:36:44 <plowsof11> merge...

17:36:46 <ofrnxmr[m]> And 378

17:37:05 <plowsof11> ye 374

17:37:35 <plowsof11> and 378 is observer yep

17:37:42 <hinto[m]> +1 for 374 & 378

17:37:49 <ofrnxmr[m]> And then plowsof will close out his CCS, please make sure he does so before he goes home
tonight. Thanks luigi1112:

17:38:09 <Mister[m]> plowsof11: The animation looks good in my opinion but also very corporate instead of
educative. Anyways, what is the problem? Is the animator not continuing?

17:38:27 <ofrnxmr[m]> After merging 374, you can move xmrsale's 30xmr directly to 374 (leaving a balance of 14
to raise)

17:38:33 <monerobull[m]> Compare it to the videos on getmonero

17:38:41 <monerobull[m]> Mister[m]: This is way worse

17:38:45 <plowsof11> the animator/script writer are wanting to continue as normal*

17:38:54 <monerobull[m]> And they tried to sell their ai voiced video like it was spoken by a human

17:39:02 <luigi1112> done, done. Good work team.

17:39:27 <Mister[m]> monerobull[m]: Yeah that is basically a scam then

17:39:35 <plowsof11> thanks luigi1112

17:39:37 <Lovera[m]> And where is this people? We need that they will here to discvuse this things

17:39:40 <plowsof11> n1oc sir?

17:39:59 <ofrnxmr[m]> Its obviously a scam, quoted 1k/minute? Lolz

17:40:21 <ofrnxmr[m]> Lovera[m]: dsmlegend:  savandra:

17:40:31 <hinto[m]> plowsof: i have to leave, finish meeting soon?

17:40:44 <Lovera[m]> Close it.., moving forward

17:40:57 <plowsof11> ah yes meeting over , sorry hinto, thank you all for attending

17:40:59 <ofrnxmr[m]> <dsmlegend[m]> "I guess we could've added "..." <- ^

17:41:16 <plowsof11> you're not allowed to leave though because theres a monerokon meeting in 20 mins

17:41:22 <ofrnxmr[m]> > <@dsmlegend:matrix.org> ofrnxmr works hard to cultivate the appearance that he cares
deeply about accurate and complete information, yet somehow neglected to mention some context. We already
changed from 'fixed' to 'flat' fee on Rucknium's suggestion. Also added the onscreen disclaimer 'exact fee
will vary depending on network congestion and other factors', which is a quote directly taken from getmonero.
Additionally, there is a

17:41:22 <ofrnxmr[m]> link in the description to a page explaining how fees are calculated.

17:41:22 <ofrnxmr[m]> > I'd be more than happy for you to join our discussion room if you'd like to pitch in
suggestions/corrections for the next video(s) 🙂

17:41:22 <ofrnxmr[m]> ^

17:41:45 <luigi1112> plowsof11 nice try, you're not allowed to leave regardless

17:41:54 <Mister[m]> monerobull[m]: The animation looks like some sort of Blender template by the way

17:41:56 <ofrnxmr[m]> He's not going anywhere, dont worry

17:42:14 <ofrnxmr[m]> Mister[m]: Because it is

17:42:41 <Lovera[m]> Nobody ask, but my February report is in gitlab and Reddit

17:42:42 <monerobull[m]> Mister[m]: They also outsourced it...

17:42:43 <Lovera[m]> https://www.reddit.com/r/Monero/comments/11l691p/ccs_lovera_february_monthly_report/?utm_
source=share&utm_medium=ios_app&utm_name=iossmf

17:43:25 <ofrnxmr[m]> Do you do tiktok lives etc?

17:43:34 <n1oc> escapethe3RA Monero Observer maintenance (Spring 2023) has moved to funding!
https://ccs.getmonero.org/proposals/escapethe3ra-monero-observer-maintenance-spring-2023.html

17:43:51 <monerobull[m]> Fund

17:44:02 <n1oc> Standalone AcceptXMR has moved to funding! https://ccs.getmonero.org/proposals/busyboredom-
standalone-acceptxmr.html

17:44:08 <Lovera[m]> ofrnxmr[m]: TikTok live no… but I can 😎 live are important to grow the community

17:44:33 <ofrnxmr[m]> Live's, ive noticed, get a lot of real people asking real questions

17:44:49 <ofrnxmr[m]> One thing we fuck up on moneromeet - YouTube commenters.  We never reply lolllol

17:45:03 <ofrnxmr[m]> We should be reading the comments and answering people

17:45:13 <plowsof11> BusyBoredom: thank you GLHF. escapethe3ra heres to another 3 months of monero.observer,
cheers!


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-03-02T22:49:07+00:00
- Closed at: 2023-03-13T09:53:29+00:00
