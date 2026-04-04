---
title: 'Monero Community Workgroup Meeting: Saturday 14th October 2023 @ 15:00 UTC'
source_url: https://github.com/monero-project/meta/issues/906
author: plowsof
assignees: []
labels: []
created_at: '2023-10-06T10:03:10+00:00'
updated_at: '2023-10-21T13:41:22+00:00'
type: issue
status: closed
closed_at: '2023-10-21T13:41:22+00:00'
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
    - [PSA for p2pool miners using --socks5 and a 3rd party node](https://www.reddit.com/r/Monero/comments/1757ms3/psa_for_p2pool_miners_curls_cve202338545_can/)
    - [v0.18.3.1 released](https://www.getmonero.org/2023/10/07/monero-GUI-0.18.3.1-released.html). boog900 found/patched a bug as a direct result of their CCS ! [Pull request](https://github.com/monero-project/monero/pull/9013)
    - https://monero.observer/ is back / Welcome back!
    - Daily tx's peaked above 25k for the first time in 3 months [monerno.town](https://monero.town/post/699939)
    - [Chainalysis CEO may face jail time for defrauding investors?](https://libera.monerologs.net/monero-community/20231007#c287224) - MajesticBank shared
    - [Jit compiler for RISC-V](https://github.com/tevador/RandomX/pull/275) - tevador. This will increase RandomX performance on RISC-V cpu's. some volunteers including pauliouk and gingeropolous have purchased risc-v hardware to help testing.
    - [Privacy Advisory - exodus wallet users update](https://www.reddit.com/r/Monero/comments/176e1zr/privacy_advisory_exodus_desktop_users_update_to/) - Rucknium 
    - https://monerosuite.org/ - [hundehausen](https://nitter.net/hundehausen/status/1712612552016863434) via [lzamenaces'](https://github.com/lalanza808) work
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [Add retroactive funding proposal for FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)  waiting for merge  
  b. [dangerousfreedom - wallet work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409)    
  c. [XMR BTC Atomic Swaps Desktop GUI - Continued development for 6 months](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/411)    
  d. [Core Monero Concepts](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/412) 
  e. [escapethe3RA Monero Observer maintenance (2023 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/414)    
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
    - [CoinMarket caps' @Monero posts](https://www.reddit.com/r/Monero/comments/170x2fr/is_this_a_real_post_from_the_monero_team/) - [viks response](https://libera.monerologs.net/monero-community/20231006#c287047)
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2023-10-16T22:27:47+00:00
Logs 
```
15:00:09 <plowsof> Meeting time https://github.com/monero-project/meta/issues/906

15:00:25 <m-relay> <m​onerobull:matrix.org> Hello

15:00:33 <m-relay> <v​ostoemisio:matrix.org> 👋

15:00:48 <m-relay> <c​trej:matrix.org> hello

15:00:49 <plowsof> hello all

15:00:51 <m-relay> <o​frnxmr:monero.social> Hello

15:01:24 <m-relay> <s​needlewoods_xmr:matrix.org> hi

15:01:54 <plowsof> lets discuss some community highlights while people roll in

15:02:06 <m-relay> <p​lowsof:matrix.org> [v0.18.3.1 released](https://www.getmonero.org/2023/10/07/monero-
GUI-0.18.3.1-released.html). boog900 found/patched a bug as a direct result of their CCS ! in this [Pull
request](https://github.com/monero-project/monero/pull/9013)

15:02:56 <m-relay> <m​onerobull:matrix.org> Cool

15:03:38 <m-relay> <p​lowsof:matrix.org> when will the DNS servers be updated selsta? usually after about a
week right? im not seeing any problems reported so far

15:04:48 <m-relay> <p​lowsof:matrix.org> monerobull tested the latest haveno release and noticed a BSOD ,
leading to an update 🫡

15:05:03 <m-relay> <m​onerobull:matrix.org> Nah

15:05:06 <m-relay> <m​onerobull:matrix.org> Not really

15:05:39 <m-relay> <m​onerobull:matrix.org> I believe the haveno bug was because US and EU use commas and dots
differently

15:06:06 <m-relay> <m​onerobull:matrix.org> The BSOD was apparently from the last windows update and has been
fixed .... By me upgrading to win11 💀

15:06:21 <m-relay> <p​lowsof:matrix.org> thank you for testing

15:06:41 <m-relay> <p​lowsof:matrix.org> we also had some community members purchase hardware to help with
this RandomX PR: [Jit compiler for RISC-V](https://github.com/tevador/RandomX/pull/275) - tevador. This will
increase RandomX performance on RISC-V cpu's. some volunteers including pauliouk and gingeropolous have
purchased risc-v hardware to help testing.

15:06:55 <m-relay> <r​ecanman:agoradesk.com> Hello, apologies for being late

15:07:28 <m-relay> <m​onerobull:matrix.org> Didn't we recently plan to make riscv less efficient lol

15:07:32 <m-relay> <m​onerobull:matrix.org> (by proxy)

15:07:47 <m-relay> <r​ecanman:agoradesk.com> I think it was to require more memory

15:08:07 <m-relay> <m​onerobull:matrix.org> And special Ryzen instructions

15:08:12 <m-relay> <p​lowsof:matrix.org> this would be a PR for the "future" - a world where RISC-V cpu's are
widespread

15:08:38 <m-relay> <m​onerobull:matrix.org> Is this kit thing licensed in such a way that bitmain can't use it
in closed software?

15:08:50 <m-relay> <m​onerobull:matrix.org> Is this jit thing licensed in such a way that bitmain can't use it
in closed software?

15:09:28 <m-relay> <p​lowsof:matrix.org> im not sure about that, i can follow up any Q's about this in
#monero-pow or with sech1 if they know

15:09:43 <m-relay> <o​frnxmr:monero.social> Monero PoW

15:10:29 <sech1> It's BSD 3-clause, so they can use it

15:10:45 <sech1> But they already used XMRig with is GPLv3, and they didn't disclose the source code

15:10:46 <m-relay> <m​onerobull:matrix.org> :/

15:10:51 <sech1> So they don't give a damn about licenses

15:10:58 <m-relay> <p​lowsof:matrix.org> lol

15:11:09 <sech1> X5 miners uses modified XMRig inside

15:11:12 <sech1> It's GPLv3

15:11:18 <sech1> Where's the published source code?

15:11:19 <m-relay> <m​onerobull:matrix.org> Their miners are blowing up anyways and they don't pay their
employers so I doubt they made much money with xmr 🤷‍♂️

15:11:41 <m-relay> <p​lowsof:matrix.org> planned obsolescence is a feature

15:11:51 <m-relay> <o​frnxmr:monero.social> Lets sue

15:12:08 <m-relay> <o​frnxmr:monero.social> monerokin lawyers

15:12:31 <m-relay> <m​onerobull:matrix.org> Only if you have the next product lined up

15:12:35 <m-relay> <p​lowsof:matrix.org> we owe them 1k for sending empty emails already but thats another
issue for #monero-events:monero.social

15:12:36 <m-relay> <m​onerobull:matrix.org> Which I very much doubt

15:13:00 <m-relay> <p​lowsof:matrix.org> the next product is probably mining already

15:13:22 <m-relay> <m​onerobull:matrix.org> Nah no way they developed another one

15:13:31 <m-relay> <m​onerobull:matrix.org> This one was a big failure

15:14:09 <m-relay> <p​lowsof:matrix.org> AI needs cpu's so the future is even brighter for RandomX

15:14:26 <m-relay> <m​onerobull:matrix.org> Ai uses GPU or asics

15:15:13 <m-relay> <p​lowsof:matrix.org> or machine learning.. they like RISC-V

15:15:46 <m-relay> <c​trej:matrix.org> bitmain likely got the cpus far below retail price to make it
worthwhile for them. People speculated on engineering samples or similar non-retail silicon

15:16:11 <m-relay> <r​ecanman:agoradesk.com> There was like $10k of memory in there alone, right?

15:17:03 <m-relay> <c​trej:matrix.org> retail price for the specific modules they've used. I'd guess they used
whatever modules they were able to source for cheap

15:17:11 <m-relay> <p​lowsof:matrix.org> almost forgetting a special thanks to Rucknium for chasing those
none-standard fees [Privacy Advisory - exodus wallet users
update](https://www.reddit.com/r/Monero/comments/176e1zr/privacy_advisory_exodus_desktop_users_update_to/)

15:18:08 <m-relay> <p​lowsof:matrix.org> we have a full-house for the active newsletters this week  [Monero
Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero
Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)

15:18:59 <m-relay> <p​lowsof:matrix.org> are we missing anything obvious? we can move on to proposals then

15:19:12 <m-relay> <r​ecanman:agoradesk.com> This website includes them and some other things, it's pretty
nice: https://themonero.dance/

15:19:59 <m-relay> <r​ecanman:agoradesk.com> I'm not sure who maintains it but its pretty nice, there are a
couple of broken things though

15:20:14 <m-relay> <p​lowsof:matrix.org> yes alot of missing things, looks nice though

15:20:48 <m-relay> <p​lowsof:matrix.org> i pointed the general fund donation tweeter to the p2pool blockchain
explorer (exploremonero still dead)

15:22:01 <m-relay> <p​lowsof:matrix.org> lets move on to the proposals

15:22:04 <m-relay> <m​onerobull:matrix.org> I'd like to thank lza_menace: for the amazing new map for docker
monero node. It's so cool

15:22:47 <m-relay> <o​frnxmr:monero.social> Yes, ty lza_menace:

15:22:50 <m-relay> <c​trej:matrix.org> eww, monero.dance has google-analytics.com and gstatic.com javascript.
Whoever runs it: is that really necassary?

15:22:53 <m-relay> <p​lowsof:matrix.org> ah yes! 🗺️

15:23:06 <m-relay> <o​frnxmr:monero.social> dⱮartian:

15:23:14 <m-relay> <r​ecanman:agoradesk.com> I didn't notice that, I have it all blocked

15:23:15 <m-relay> <o​frnxmr:monero.social> dⱮartian:

15:23:20 <m-relay> <r​ecanman:agoradesk.com> Maybe someone should contact the above

15:23:21 <m-relay> <o​frnxmr:monero.social> Runs it

15:24:03 <m-relay> <p​lowsof:matrix.org> monerosuite.org is from hundehausen  (based on the work of lza_menace
too)

15:24:39 <m-relay> <r​ecanman:agoradesk.com> This looks pretty cool, if I can get it working I'll feature it
in my next issue of the Monero Standard

15:25:09 <m-relay> <m​onerobull:matrix.org> Is that like an all in one monero deployer?

15:25:09 <m-relay> <p​lowsof:matrix.org> feather wallet tagged a new release. they also need help to verify
hashes and such (20~GB of free disk space and time required) https://github.com/feather-
wallet/feather/tree/master/contrib/guix#building

15:25:24 <m-relay> <r​ecanman:agoradesk.com> Yes, so many configuration options

15:25:26 <m-relay> <p​lowsof:matrix.org> yes monerosuite is an all in one, similar to xmr.sh

15:25:48 <m-relay> <m​onerobull:matrix.org> Cool

15:25:59 <m-relay> <r​ecanman:agoradesk.com> Includes block explorer, reverse proxy, tor proxy, monitoring,
etc.

15:26:42 <m-relay> <o​frnxmr:monero.social> Tor stuff look weird

15:28:00 <m-relay> <p​lowsof:matrix.org> lets move onto the proposals unless

15:29:08 <m-relay> <p​lowsof:matrix.org> CCS proposals

15:29:08 <m-relay> <p​lowsof:matrix.org> we can skip a. [Add retroactive funding proposal for
FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)  waiting for merge.

15:29:11 <m-relay> <p​lowsof:matrix.org> and just make everyone waiting for a ccs payout / merges aware that
luigi1111 knows about it and will be handling everything soon(tm) - apologies for the delays

15:29:26 <m-relay> <o​frnxmr:monero.social> yup

15:30:09 <m-relay> <p​lowsof:matrix.org> b. [dangerousfreedom - wallet
work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409)

15:30:41 <m-relay> <m​onerobull:matrix.org> Voting merge

15:31:16 <m-relay> <p​lowsof:matrix.org> DF is waiting for code reviews from his previous CCS

15:31:52 <m-relay> <r​ecanman:agoradesk.com> Seraphis wallet migration is extremely necessary and DF has major
contributions

15:31:53 <m-relay> <r​ecanman:agoradesk.com> +merge

15:32:20 <m-relay> <m​onerobull:matrix.org> This is a problem in general right

15:33:04 <m-relay> <p​lowsof:matrix.org> indeed, rbrunner7 has provided some positive feedback

15:33:09 <m-relay> <m​onerobull:matrix.org> Can we hire someone like cypher stack if we can't find reviewers
otherwise

15:34:05 <m-relay> <o​frnxmr:monero.social> This

15:34:14 <m-relay> <o​frnxmr:monero.social> Daemon needed too lol

15:34:30 <m-relay> <o​frnxmr:monero.social> Seraphis needs proofs and audits

15:34:36 <m-relay> <o​frnxmr:monero.social> And DF needs reviews

15:34:45 <m-relay> <o​frnxmr:monero.social> Yes

15:35:15 <m-relay> <o​frnxmr:monero.social> -dev and/or mrl and/or nwlb need to sign off

15:35:39 <m-relay> <r​ecanman:agoradesk.com> You'

15:35:42 <m-relay> <p​lowsof:matrix.org> we have devs on the payroll who can use hours to review DFs work

15:35:43 <m-relay> <r​ecanman:agoradesk.com> You're right

15:36:22 <m-relay> <m​onerobull:matrix.org> Are those devs just sitting around doing nothing?

15:36:36 <m-relay> <m​onerobull:matrix.org> I'm pretty sure most work on very specific things

15:37:28 <m-relay> <m​onerobull:matrix.org> Delaying what they work on to review each other's work while we
have funds sitting idle is not very efficient

15:38:12 <m-relay> <p​lowsof:matrix.org> koe has had a quick look and said it all seems ok but not actually
reviewed it in depth

15:38:14 <m-relay> <m​onerobull:matrix.org> Unless there's direct benefits from wallet reviewers being
familiar with it in the future

15:39:02 <m-relay> <m​onerobull:matrix.org> But it would need to be related, no point in a wallet expert
reviewing p2p protocol when they don't plan to ever work with it

15:39:37 <m-relay> <p​lowsof:matrix.org> i defer all serpahis proposals to the NWLB/seraphis workgroup

15:39:41 <m-relay> <p​lowsof:matrix.org> thats my vote

15:40:37 <m-relay> <p​lowsof:matrix.org> hiring outside help from e.g. cypherstack is a good idea

15:40:37 <m-relay> <s​needlewoods_xmr:matrix.org> maybe we need monero-apprenticeship

15:40:49 <m-relay> <p​lowsof:matrix.org> we need experts

15:41:39 <selsta> plowsof: depends on core team availability

15:42:02 <selsta> but yes DNS will be updated after a week or so

15:42:15 <m-relay> <c​trej:matrix.org> specifics about dev work can be discussed in other groups, as long as
we take care that devs willing to work can work - and that they are not waiting on the ccs bureaucracy

15:42:20 <m-relay> <p​lowsof:matrix.org> thanks! (DNS tells clients there is an update available)

15:42:36 <m-relay> <c​trej:matrix.org> otherwise agreeing with this

15:43:33 <m-relay> <p​lowsof:matrix.org> i mean on a personal level - DF has attended a monerokon and done
other great work for the project - reducing delays is the priority here so he can get funding to continue

15:44:14 <m-relay> <m​onerobull:matrix.org> Can he already move forward even without the review?

15:46:28 <m-relay> <p​lowsof:matrix.org> there where some issues when the previous ccs was posted - which
required discussion and changes, can view it in the comments. (perhaps showing a lack of direction because
this is all new)

15:47:22 <m-relay> <p​lowsof:matrix.org> give him the tasks that we need and he'll do it

15:48:03 <m-relay> <p​lowsof:matrix.org> lets touch on the other proposals

15:48:04 <m-relay> <p​lowsof:matrix.org> c. [XMR BTC Atomic Swaps Desktop GUI - Continued development for 6
months](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/411)

15:48:04 <m-relay> <o​frnxmr:monero.social> close

15:48:27 <m-relay> <p​lowsof:matrix.org> binarybaron: hasnt had a chance to respond to my comment yet

15:49:13 <m-relay> <p​lowsof:matrix.org> this comment: https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/411#note_22562

15:50:13 <m-relay> <m​onerobull:matrix.org> The GUI looks good but it's built on a discontinued protocol

15:51:08 <m-relay> <m​onerobull:matrix.org> BasicSwapDex allows bidirectional monero swaps with BTC and LTC
now

15:51:50 <m-relay> <o​frnxmr:monero.social> UnstoppableSwap

15:52:23 <m-relay> <m​onerobull:matrix.org> I'd much rather have someone look into taking BasicSwapDex and
ripping out their smsg network and replace it with regular Tor connections

15:52:45 <m-relay> <m​onerobull:matrix.org> Or at least evaluate how feasible that would be

15:53:07 <m-relay> <o​frnxmr:monero.social> Or pokkst etc implement said features in other wallets

15:53:38 <m-relay> <m​onerobull:matrix.org> Yeaj

15:53:38 <m-relay> <m​onerobull:matrix.org> Saw a tweet today

15:53:41 <m-relay> <m​onerobull:matrix.org> Pokkst implementation looks promising

15:54:04 <m-relay> <m​onerobull:matrix.org> Is there any more info than his tweets?

15:54:05 <m-relay> <p​lowsof:matrix.org> pokkst made a PR to the COMIT repo....

15:54:14 <m-relay> <p​lowsof:matrix.org> is he also using the dead protocol?

15:54:27 <m-relay> <p​lowsof:matrix.org> perhaps then its not dead?

15:54:44 <m-relay> <p​lowsof:matrix.org> suspicious https://github.com/comit-network/xmr-btc-swap/pull/1447

15:54:58 <m-relay> <m​onerobull:matrix.org> Hm

15:55:05 <m-relay> <m​onerobull:matrix.org>
https://matrix.monero.social/_matrix/media/v1/download/matrix.org/jRrtPURCTbucKTNNvMPLvtSY

15:55:55 <m-relay> <m​onerobull:matrix.org> I want to know how the liquidity providing works

15:56:07 <m-relay> <p​lowsof:matrix.org> looks like the same setup as unstoppable swap

15:56:26 <m-relay> <p​lowsof:matrix.org> i think we can defer discussion after raising some questions here and
wait for binarybarons initial response

15:56:43 <m-relay> <p​lowsof:matrix.org> moving on

15:56:45 <m-relay> <p​lowsof:matrix.org> d. [Core Monero Concepts](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/412)

15:57:35 <m-relay> <p​lowsof:matrix.org> the previous video they made was _actually_ proudly shared on some
social media sites

15:58:08 <m-relay> <m​onerobull:matrix.org> Unlike the last animation proposal lol

15:58:16 <m-relay> <o​frnxmr:monero.social> My comments earlier are an extension of plowsof. Lower # of videos
to 2 + (my suggestion) and do video on importance of nodes etc and another on fungibility/adoption4merchants

15:59:17 <m-relay> <p​lowsof:matrix.org> we have 35 XMR from this proposal
https://ccs.getmonero.org/proposals/savandra-videos-for-monero.html . if this Core Monero Concepts is reduced
to 2 videos - then it could be almost entirely funded by those funds, and reduce the logisticcs issues with
trying to push 4 videos out in a short time span

15:59:34 <m-relay> <o​frnxmr:monero.social> Im ok with more videos following fwiw

16:00:39 <m-relay> <v​ostoemisio:matrix.org> When would this be decided and allocated? I discussed a bit with
xenu and we are open to shorten it to 2 videos to start if it makes sense. But if we could choose freely we
would like to keep it to 4 videos as the initial proposal, less administration

16:01:17 <m-relay> <v​ostoemisio:matrix.org> About the script and topics I refer to x3nu  to comment 👍️

16:01:37 <m-relay> <m​onerobull:matrix.org> Let vosto work without needing to deal with us again every few
weeks thankd

16:02:09 <m-relay> <p​lowsof:matrix.org> the hive mind will make it so. if reducing to 2 videos , then its
possible that the price is halfed and it goes to funding for 0.x XMR?

16:02:24 <m-relay> <c​trej:matrix.org> which comment?

16:02:39 <m-relay> <v​ostoemisio:matrix.org> this comment

16:02:40 <m-relay> <p​lowsof:matrix.org> and absorbs the savandra funds (thus closing that proposal for good)

16:02:41 <m-relay> <v​ostoemisio:matrix.org> this comment ceetee

16:02:48 <m-relay> <p​lowsof:matrix.org> similar path to AcceptXMR

16:03:06 <m-relay> <v​ostoemisio:matrix.org> this feedback, ceetee

16:03:56 <m-relay> <p​lowsof:matrix.org> currently this proposal is 72XMR - halving it to 2 videos makes 36
XMR meaning if people want it to be 2, we could fund it with the 35 XMR , and put it to funding with 1 XMR

16:04:13 <m-relay> <p​lowsof:matrix.org> bish bang bosh

16:04:16 <m-relay> <l​ordx3nu:matrix.org> the general idea is to have a full suite of videos discussing
intermediate topics about Monero. So for example the four topics in the proposal show this. We also have
future plans for videos as well to help with adoption and understanding: e.g. atomic swaps, seraphis. By doing
a buik order now we can focus on four topics that have a lot of merit and content  and I believe it
would<clipped message>

16:04:16 <m-relay> <l​ordx3nu:matrix.org>  benefit the community to have videos like this they can just link
to a noobie that will introduce them to these ideas.

16:04:50 <m-relay> <l​ordx3nu:matrix.org> and you guys have already seen the quality from the tail
emission/dynamic blockswize vid :_)

16:05:03 <m-relay> <l​ordx3nu:matrix.org> and you guys have already seen the quality from the tail
emission/dynamic blockswize vid :)

16:06:03 <m-relay> <s​needlewoods_xmr:matrix.org> yeah it  was visually appealing

16:06:28 <m-relay> <l​ordx3nu:matrix.org> if two videos is more convenient that works as well. we can again
show we are capable of producing quality to make future funding more valuable

16:06:45 <m-relay> <v​ostoemisio:matrix.org> If it's not a big deal for the community I'd prefer the current
proposal but like x3nu  says we are open to changing it

16:06:46 <m-relay> <o​frnxmr:monero.social> Seraphis and stomic swaps?

16:06:55 <m-relay> <p​lowsof:matrix.org> so we have several options here , move to funding as, move to funding
as is -= to the 35 XMR, half it and -= 35 so it requires 1 xmr to complete funding

16:07:18 <m-relay> <p​lowsof:matrix.org> if halfing people need to decide on what 2 vids they want

16:07:23 <m-relay> <c​trej:matrix.org> from the proposal:

16:07:23 <m-relay> <c​trej:matrix.org> >• Random X: Understanding the significance of ASIC resistance

16:07:23 <m-relay> <c​trej:matrix.org> >• Breaking down the how-to and the rationale for P2Pool.

16:07:24 <m-relay> <c​trej:matrix.org> >• Nodes: Why every Monero enthusiast should consider running one.

16:07:24 <m-relay> <c​trej:matrix.org> >• Fungibility: Explaining its essence in the context of Monero.

16:07:31 <m-relay> <p​lowsof:matrix.org> overall i am +1 for vost and xenu to produce more videos for us

16:07:45 <m-relay> <r​ecanman:agoradesk.com> As am IU

16:07:47 <m-relay> <r​ecanman:agoradesk.com> As am I

16:07:54 <m-relay> <o​frnxmr:monero.social> i am as well

16:07:59 <m-relay> <p​lowsof:matrix.org> some discussion to finalise what is going to happen is needed

16:08:03 <m-relay> <l​ordx3nu:matrix.org> that's not in this proposal, but we have future plans for that, yes.
we need to wait until more work is done on them though before spending time on it

16:08:05 <m-relay> <r​ecanman:agoradesk.com> RandomX and fungibility I think are good if halfing

16:08:11 <m-relay> <o​frnxmr:monero.social> But making videos that only last a few months is retarded

16:08:13 <m-relay> <m​onerobull:matrix.org> do we nee d a p2pool how-to? breaking it down sure but i believe
there are already good tutorials

16:08:28 <m-relay> <p​lowsof:matrix.org> i apologise for spelling halfing wrong and misleading you all.
halving *

16:08:30 <m-relay> <o​frnxmr:monero.social> Landscape forever changing on atomic awaps, seraphis, p2pool, even
fungibility

16:08:56 <m-relay> <v​ostoemisio:matrix.org> Keep proposal as is, redistribute funding to ours, 35/72 xmr in
the funding, that's optimal IMO

16:08:57 <m-relay> <r​ecanman:agoradesk.com> RandomX and fungibility I think are good if halving

16:09:11 <m-relay> <v​ostoemisio:matrix.org> 34 or 35, whatever was left in savandra's

16:09:15 <m-relay> <l​ordx3nu:matrix.org> well for fungibility that isn't really about technology but moreso
the characteristic of fungibility because monero isn't perfectly fungible

16:09:43 <m-relay> <l​ordx3nu:matrix.org> so we will have example of what we mean by that and benefits of
fungibility

16:10:02 <m-relay> <r​ecanman:agoradesk.com> I have to leave the meeting. Goodbye everyone and thank you
plowsof for moderation

16:10:15 <m-relay> <v​ostoemisio:matrix.org> x3nu: Is probably up to work on the scripts while we wait for the
second half funding, x3nu  ? No time would be wasted

16:10:18 <m-relay> <l​ordx3nu:matrix.org> atomic swaps and seraphis are indeed constantly changing. althought
seraphis I think would be ideal once it is finalized because this is the largest hardfork  in Monero's history

16:10:20 <m-relay> <o​frnxmr:monero.social> Right. So why makeba video on fungibikity when xmr is not yet
fungible?

16:10:26 <m-relay> <o​frnxmr:monero.social> Ita like making news reports on "whats to come"

16:10:31 <m-relay> <p​lowsof:matrix.org> recanman vote on the last one before you leave?

16:10:37 <m-relay> <p​lowsof:matrix.org> e. [escapethe3RA Monero Observer maintenance (2023
Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/414)

16:11:18 <m-relay> <o​frnxmr:monero.social> merge

16:11:25 <m-relay> <l​ordx3nu:matrix.org> it would be like making a video on privacy but monero isn't
perfectly private. it isn't an on or an off switch but an ideal that development for Monero aims for

16:11:25 <m-relay> <r​ecanman:agoradesk.com> +merge, Monero observer I look at all the time

16:11:26 <m-relay> <p​lowsof:matrix.org> monero.observer left our minds, but never our hearts and has been
back the past week pushing out content as usual

16:11:39 <m-relay> <o​frnxmr:monero.social> Didnt check price, bur merge if same as last

16:11:44 <m-relay> <p​lowsof:matrix.org> thanks for attending recanman

16:11:52 <m-relay> <p​lowsof:matrix.org> price is the same rates as the prev

16:11:53 <m-relay> <r​ecanman:agoradesk.com> I checked almost every day on whether monero.observer was back.
It's great. Goodbye

16:12:20 <m-relay> <m​onerobull:matrix.org> i suggest you to set up an rss reader instead

16:12:29 <m-relay> <o​frnxmr:monero.social> G2g too

16:12:33 <m-relay> <o​frnxmr:monero.social> back in a few

16:12:45 <m-relay> <m​onerobull:matrix.org>
https://matrix.monero.social/_matrix/media/v1/download/matrix.org/XvlSJVtviXKzgOWYRKVgYwjz

16:12:46 <m-relay> <m​onerobull:matrix.org> its so good

16:13:15 <m-relay> <l​ordx3nu:matrix.org> we think it would be a good idea to introduce the topic as part of
running a node because the question of "what can I do to help Monero" comes up a lot. it wouldn't be a literal
guide but a guide emphasizing the difference between centarlized pools and p2pool and why long term p2pool is
what we should aim for

16:13:29 <m-relay> <m​onerobull:matrix.org> yeah that is good

16:13:34 <plowsof> thanks all for attending, we can call an end to the meeting here. we have to come to a
decision on how to move forward with the core monero concepts proposal asap


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## rottenwheel | 2023-10-21T06:07:33+00:00
Test.

> **\<plowsof\>** Meeting time https://github.com/monero-project/meta/issues/906  
> **\<m​onerobull:matrix.org\>** Hello  
> **\<v​ostoemisio:matrix.org\>** 👋  
> **\<c​trej:matrix.org\>** hello  
> **\<plowsof\>** hello all  
> **\<o​frnxmr:monero.social\>** Hello  
> **\<s​needlewoods\_xmr:matrix.org\>** hi  
> **\<plowsof\>** lets discuss some community highlights while people roll in   
> **\<p​lowsof:matrix.org\>** [v0.18.3.1 released](https://www.getmonero.org/2023/10/07/monero-GUI-0.18.3.1-released.html). boog900 found/patched a bug as a direct result of their CCS ! in this [Pull request](https://github.com/monero-project/monero/pull/9013)  
> **\<m​onerobull:matrix.org\>** Cool  
> **\<p​lowsof:matrix.org\>** when will the DNS servers be updated selsta? usually after about a week right? im not seeing any problems reported so far  
> **\<p​lowsof:matrix.org\>** monerobull tested the latest haveno release and noticed a BSOD , leading to an update 🫡  
> **\<m​onerobull:matrix.org\>** Nah  
> **\<m​onerobull:matrix.org\>** Not really  
> **\<m​onerobull:matrix.org\>** I believe the haveno bug was because US and EU use commas and dots differently  
> **\<m​onerobull:matrix.org\>** The BSOD was apparently from the last windows update and has been fixed .... By me upgrading to win11 💀  
> **\<p​lowsof:matrix.org\>** thank you for testing  
> **\<p​lowsof:matrix.org\>** we also had some community members purchase hardware to help with this RandomX PR: [Jit compiler for RISC-V](https://github.com/tevador/RandomX/pull/275) - tevador. This will increase RandomX performance on RISC-V cpu's. some volunteers including pauliouk and gingeropolous have purchased risc-v hardware to help testing.  
> **\<r​ecanman:agoradesk.com\>** Hello, apologies for being late  
> **\<m​onerobull:matrix.org\>** Didn't we recently plan to make riscv less efficient lol  
> **\<m​onerobull:matrix.org\>** (by proxy)  
> **\<r​ecanman:agoradesk.com\>** I think it was to require more memory  
> **\<m​onerobull:matrix.org\>** And special Ryzen instructions  
> **\<p​lowsof:matrix.org\>** this would be a PR for the "future" - a world where RISC-V cpu's are widespread  
> **\<m​onerobull:matrix.org\>** Is this kit thing licensed in such a way that bitmain can't use it in closed software?  
> **\<m​onerobull:matrix.org\>** Is this jit thing licensed in such a way that bitmain can't use it in closed software?  
> **\<p​lowsof:matrix.org\>** im not sure about that, i can follow up any Q's about this in #monero-pow or with sech1 if they know  
> **\<o​frnxmr:monero.social\>** Monero PoW  
> **\<sech1\>** It's BSD 3-clause, so they can use it  
> **\<sech1\>** But they already used XMRig with is GPLv3, and they didn't disclose the source code  
> **\<m​onerobull:matrix.org\>** :/  
> **\<sech1\>** So they don't give a damn about licenses  
> **\<p​lowsof:matrix.org\>** lol  
> **\<sech1\>** X5 miners uses modified XMRig inside  
> **\<sech1\>** It's GPLv3  
> **\<sech1\>** Where's the published source code?  
> **\<m​onerobull:matrix.org\>** Their miners are blowing up anyways and they don't pay their employers so I doubt they made much money with xmr 🤷‍♂️  
> **\<p​lowsof:matrix.org\>** planned obsolescence is a feature  
> **\<o​frnxmr:monero.social\>** Lets sue  
> **\<o​frnxmr:monero.social\>** monerokin lawyers  
> **\<m​onerobull:matrix.org\>** Only if you have the next product lined up  
> **\<p​lowsof:matrix.org\>** we owe them 1k for sending empty emails already but thats another issue for #monero-events:monero.social  
> **\<m​onerobull:matrix.org\>** Which I very much doubt  
> **\<p​lowsof:matrix.org\>** the next product is probably mining already  
> **\<m​onerobull:matrix.org\>** Nah no way they developed another one  
> **\<m​onerobull:matrix.org\>** This one was a big failure  
> **\<p​lowsof:matrix.org\>** AI needs cpu's so the future is even brighter for RandomX  
> **\<m​onerobull:matrix.org\>** Ai uses GPU or asics  
> **\<p​lowsof:matrix.org\>** or machine learning.. they like RISC-V  
> **\<c​trej:matrix.org\>** bitmain likely got the cpus far below retail price to make it worthwhile for them. People speculated on engineering samples or similar non-retail silicon  
> **\<r​ecanman:agoradesk.com\>** There was like $10k of memory in there alone, right?  
> **\<c​trej:matrix.org\>** retail price for the specific modules they've used. I'd guess they used whatever modules they were able to source for cheap  
> **\<p​lowsof:matrix.org\>** almost forgetting a special thanks to Rucknium for chasing those none-standard fees [Privacy Advisory - exodus wallet users update](https://www.reddit.com/r/Monero/comments/176e1zr/privacy\_advisory\_exodus\_desktop\_users\_update\_to/)  
> **\<p​lowsof:matrix.org\>** we have a full-house for the active newsletters this week  [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)  
> **\<p​lowsof:matrix.org\>** are we missing anything obvious? we can move on to proposals then  
> **\<r​ecanman:agoradesk.com\>** This website includes them and some other things, it's pretty nice: https://themonero.dance/  
> **\<r​ecanman:agoradesk.com\>** I'm not sure who maintains it but its pretty nice, there are a couple of broken things though  
> **\<p​lowsof:matrix.org\>** yes alot of missing things, looks nice though  
> **\<p​lowsof:matrix.org\>** i pointed the general fund donation tweeter to the p2pool blockchain explorer (exploremonero still dead)  
> **\<p​lowsof:matrix.org\>** lets move on to the proposals  
> **\<m​onerobull:matrix.org\>** I'd like to thank lza\_menace: for the amazing new map for docker monero node. It's so cool  
> **\<o​frnxmr:monero.social\>** Yes, ty lza\_menace:  
> **\<c​trej:matrix.org\>** eww, monero.dance has google-analytics.com and gstatic.com javascript. Whoever runs it: is that really necassary?  
> **\<p​lowsof:matrix.org\>** ah yes! 🗺️  
> **\<o​frnxmr:monero.social\>** dⱮartian:  
> **\<r​ecanman:agoradesk.com\>** I didn't notice that, I have it all blocked  
> **\<o​frnxmr:monero.social\>** dⱮartian:  
> **\<r​ecanman:agoradesk.com\>** Maybe someone should contact the above  
> **\<o​frnxmr:monero.social\>** Runs it  
> **\<p​lowsof:matrix.org\>** monerosuite.org is from hundehausen  (based on the work of lza\_menace too)  
> **\<r​ecanman:agoradesk.com\>** This looks pretty cool, if I can get it working I'll feature it in my next issue of the Monero Standard  
> **\<m​onerobull:matrix.org\>** Is that like an all in one monero deployer?  
> **\<p​lowsof:matrix.org\>** feather wallet tagged a new release. they also need help to verify hashes and such (20~GB of free disk space and time required) https://github.com/feather-wallet/feather/tree/master/contrib/guix#building  
> **\<r​ecanman:agoradesk.com\>** Yes, so many configuration options  
> **\<p​lowsof:matrix.org\>** yes monerosuite is an all in one, similar to xmr.sh  
> **\<m​onerobull:matrix.org\>** Cool  
> **\<r​ecanman:agoradesk.com\>** Includes block explorer, reverse proxy, tor proxy, monitoring, etc.  
> **\<o​frnxmr:monero.social\>** Tor stuff look weird  
> **\<p​lowsof:matrix.org\>** lets move onto the proposals unless  
> **\<p​lowsof:matrix.org\>** CCS proposals  
> **\<p​lowsof:matrix.org\>** we can skip a. [Add retroactive funding proposal for FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge\_requests/403)  waiting for merge.  
> **\<p​lowsof:matrix.org\>** and just make everyone waiting for a ccs payout / merges aware that luigi1111 knows about it and will be handling everything soon(tm) - apologies for the delays  
> **\<o​frnxmr:monero.social\>** yup  
> **\<p​lowsof:matrix.org\>** b. [dangerousfreedom - wallet work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge\_requests/409)  
> **\<m​onerobull:matrix.org\>** Voting merge  
> **\<p​lowsof:matrix.org\>** DF is waiting for code reviews from his previous CCS  
> **\<r​ecanman:agoradesk.com\>** Seraphis wallet migration is extremely necessary and DF has major contributions  
> **\<r​ecanman:agoradesk.com\>** +merge  
> **\<m​onerobull:matrix.org\>** This is a problem in general right  
> **\<p​lowsof:matrix.org\>** indeed, rbrunner7 has provided some positive feedback  
> **\<m​onerobull:matrix.org\>** Can we hire someone like cypher stack if we can't find reviewers otherwise  
> **\<o​frnxmr:monero.social\>** This  
> **\<o​frnxmr:monero.social\>** Daemon needed too lol  
> **\<o​frnxmr:monero.social\>** Seraphis needs proofs and audits  
> **\<o​frnxmr:monero.social\>** And DF needs reviews  
> **\<o​frnxmr:monero.social\>** Yes  
> **\<o​frnxmr:monero.social\>** -dev and/or mrl and/or nwlb need to sign off  
> **\<r​ecanman:agoradesk.com\>** You'  
> **\<p​lowsof:matrix.org\>** we have devs on the payroll who can use hours to review DFs work  
> **\<r​ecanman:agoradesk.com\>** You're right  
> **\<m​onerobull:matrix.org\>** Are those devs just sitting around doing nothing?  
> **\<m​onerobull:matrix.org\>** I'm pretty sure most work on very specific things  
> **\<m​onerobull:matrix.org\>** Delaying what they work on to review each other's work while we have funds sitting idle is not very efficient  
> **\<p​lowsof:matrix.org\>** koe has had a quick look and said it all seems ok but not actually reviewed it in depth  
> **\<m​onerobull:matrix.org\>** Unless there's direct benefits from wallet reviewers being familiar with it in the future  
> **\<m​onerobull:matrix.org\>** But it would need to be related, no point in a wallet expert reviewing p2p protocol when they don't plan to ever work with it  
> **\<p​lowsof:matrix.org\>** i defer all serpahis proposals to the NWLB/seraphis workgroup  
> **\<p​lowsof:matrix.org\>** thats my vote  
> **\<p​lowsof:matrix.org\>** hiring outside help from e.g. cypherstack is a good idea  
> **\<s​needlewoods\_xmr:matrix.org\>** maybe we need monero-apprenticeship  
> **\<p​lowsof:matrix.org\>** we need experts  
> **\<selsta\>** plowsof: depends on core team availability  
> **\<selsta\>** but yes DNS will be updated after a week or so  
> **\<c​trej:matrix.org\>** specifics about dev work can be discussed in other groups, as long as we take care that devs willing to work can work - and that they are not waiting on the ccs bureaucracy  
> **\<p​lowsof:matrix.org\>** thanks! (DNS tells clients there is an update available)  
> **\<c​trej:matrix.org\>** otherwise agreeing with this  
> **\<p​lowsof:matrix.org\>** i mean on a personal level - DF has attended a monerokon and done other great work for the project - reducing delays is the priority here so he can get funding to continue  
> **\<m​onerobull:matrix.org\>** Can he already move forward even without the review?  
> **\<p​lowsof:matrix.org\>** there where some issues when the previous ccs was posted - which required discussion and changes, can view it in the comments. (perhaps showing a lack of direction because this is all new)  
> **\<p​lowsof:matrix.org\>** give him the tasks that we need and he'll do it  
> **\<p​lowsof:matrix.org\>** lets touch on the other proposals  
> **\<p​lowsof:matrix.org\>** c. [XMR BTC Atomic Swaps Desktop GUI - Continued development for 6 months](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge\_requests/411)  
> **\<o​frnxmr:monero.social\>** close  
> **\<p​lowsof:matrix.org\>** binarybaron: hasnt had a chance to respond to my comment yet  
> **\<p​lowsof:matrix.org\>** this comment: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge\_requests/411#note\_22562  
> **\<m​onerobull:matrix.org\>** The GUI looks good but it's built on a discontinued protocol  
> **\<m​onerobull:matrix.org\>** BasicSwapDex allows bidirectional monero swaps with BTC and LTC now  
> **\<o​frnxmr:monero.social\>** UnstoppableSwap  
> **\<m​onerobull:matrix.org\>** I'd much rather have someone look into taking BasicSwapDex and ripping out their smsg network and replace it with regular Tor connections  
> **\<m​onerobull:matrix.org\>** Or at least evaluate how feasible that would be  
> **\<o​frnxmr:monero.social\>** Or pokkst etc implement said features in other wallets  
> **\<m​onerobull:matrix.org\>** Yeaj  
> **\<m​onerobull:matrix.org\>** Saw a tweet today  
> **\<m​onerobull:matrix.org\>** Pokkst implementation looks promising  
> **\<m​onerobull:matrix.org\>** Is there any more info than his tweets?  
> **\<p​lowsof:matrix.org\>** pokkst made a PR to the COMIT repo....  
> **\<p​lowsof:matrix.org\>** is he also using the dead protocol?  
> **\<p​lowsof:matrix.org\>** perhaps then its not dead?  
> **\<p​lowsof:matrix.org\>** suspicious https://github.com/comit-network/xmr-btc-swap/pull/1447  
> **\<m​onerobull:matrix.org\>** Hm  
> **\<m​onerobull:matrix.org\>** https://matrix.monero.social/\_matrix/media/v1/download/matrix.org/jRrtPURCTbucKTNNvMPLvtSY  
> **\<m​onerobull:matrix.org\>** I want to know how the liquidity providing works  
> **\<p​lowsof:matrix.org\>** looks like the same setup as unstoppable swap  
> **\<p​lowsof:matrix.org\>** i think we can defer discussion after raising some questions here and wait for binarybarons initial response  
> **\<p​lowsof:matrix.org\>** moving on  
> **\<p​lowsof:matrix.org\>** d. [Core Monero Concepts](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge\_requests/412)  
> **\<p​lowsof:matrix.org\>** the previous video they made was \_actually\_ proudly shared on some social media sites  
> **\<m​onerobull:matrix.org\>** Unlike the last animation proposal lol  
> **\<o​frnxmr:monero.social\>** My comments earlier are an extension of plowsof. Lower # of videos to 2 + (my suggestion) and do video on importance of nodes etc and another on fungibility/adoption4merchants  
> **\<p​lowsof:matrix.org\>** we have 35 XMR from this proposal https://ccs.getmonero.org/proposals/savandra-videos-for-monero.html . if this Core Monero Concepts is reduced to 2 videos - then it could be almost entirely funded by those funds, and reduce the logisticcs issues with trying to push 4 videos out in a short time span  
> **\<o​frnxmr:monero.social\>** Im ok with more videos following fwiw  
> **\<v​ostoemisio:matrix.org\>** When would this be decided and allocated? I discussed a bit with xenu and we are open to shorten it to 2 videos to start if it makes sense. But if we could choose freely we would like to keep it to 4 videos as the initial proposal, less administration  
> **\<v​ostoemisio:matrix.org\>** About the script and topics I refer to x3nu  to comment 👍️  
> **\<m​onerobull:matrix.org\>** Let vosto work without needing to deal with us again every few weeks thankd  
> **\<p​lowsof:matrix.org\>** the hive mind will make it so. if reducing to 2 videos , then its possible that the price is halfed and it goes to funding for 0.x XMR?  
> **\<c​trej:matrix.org\>** which comment?  
> **\<v​ostoemisio:matrix.org\>** this comment  
> **\<p​lowsof:matrix.org\>** and absorbs the savandra funds (thus closing that proposal for good)  
> **\<v​ostoemisio:matrix.org\>** this comment ceetee  
> **\<p​lowsof:matrix.org\>** similar path to AcceptXMR  
> **\<v​ostoemisio:matrix.org\>** this feedback, ceetee  
> **\<p​lowsof:matrix.org\>** currently this proposal is 72XMR - halving it to 2 videos makes 36 XMR meaning if people want it to be 2, we could fund it with the 35 XMR , and put it to funding with 1 XMR  
> **\<p​lowsof:matrix.org\>** bish bang bosh  
> \<clipped message\>  
> **\<l​ordx3nu:matrix.org\>**  benefit the community to have videos like this they can just link to a noobie that will introduce them to these ideas.  
> **\<l​ordx3nu:matrix.org\>** and you guys have already seen the quality from the tail emission/dynamic blockswize vid :\_)  
> **\<l​ordx3nu:matrix.org\>** and you guys have already seen the quality from the tail emission/dynamic blockswize vid :)  
> **\<s​needlewoods\_xmr:matrix.org\>** yeah it  was visually appealing  
> **\<l​ordx3nu:matrix.org\>** if two videos is more convenient that works as well. we can again show we are capable of producing quality to make future funding more valuable  
> **\<v​ostoemisio:matrix.org\>** If it's not a big deal for the community I'd prefer the current proposal but like x3nu  says we are open to changing it  
> **\<o​frnxmr:monero.social\>** Seraphis and stomic swaps?  
> **\<p​lowsof:matrix.org\>** so we have several options here , move to funding as, move to funding as is -= to the 35 XMR, half it and -= 35 so it requires 1 xmr to complete funding  
> **\<p​lowsof:matrix.org\>** if halfing people need to decide on what 2 vids they want  
> **\<c​trej:matrix.org\>** from the proposal:  
> **\<c​trej:matrix.org\>** \>• Random X: Understanding the significance of ASIC resistance  
> **\<c​trej:matrix.org\>** \>• Breaking down the how-to and the rationale for P2Pool.  
> **\<c​trej:matrix.org\>** \>• Nodes: Why every Monero enthusiast should consider running one.  
> **\<c​trej:matrix.org\>** \>• Fungibility: Explaining its essence in the context of Monero.  
> **\<p​lowsof:matrix.org\>** overall i am +1 for vost and xenu to produce more videos for us  
> **\<r​ecanman:agoradesk.com\>** As am IU  
> **\<r​ecanman:agoradesk.com\>** As am I  
> **\<o​frnxmr:monero.social\>** i am as well  
> **\<p​lowsof:matrix.org\>** some discussion to finalise what is going to happen is needed  
> **\<l​ordx3nu:matrix.org\>** that's not in this proposal, but we have future plans for that, yes. we need to wait until more work is done on them though before spending time on it  
> **\<r​ecanman:agoradesk.com\>** RandomX and fungibility I think are good if halfing  
> **\<o​frnxmr:monero.social\>** But making videos that only last a few months is retarded  
> **\<m​onerobull:matrix.org\>** do we nee d a p2pool how-to? breaking it down sure but i believe there are already good tutorials  
> **\<p​lowsof:matrix.org\>** i apologise for spelling halfing wrong and misleading you all. halving \*  
> **\<o​frnxmr:monero.social\>** Landscape forever changing on atomic awaps, seraphis, p2pool, even fungibility  
> **\<v​ostoemisio:matrix.org\>** Keep proposal as is, redistribute funding to ours, 35/72 xmr in the funding, that's optimal IMO  
> **\<r​ecanman:agoradesk.com\>** RandomX and fungibility I think are good if halving  
> **\<v​ostoemisio:matrix.org\>** 34 or 35, whatever was left in savandra's  
> **\<l​ordx3nu:matrix.org\>** well for fungibility that isn't really about technology but moreso the characteristic of fungibility because monero isn't perfectly fungible  
> **\<l​ordx3nu:matrix.org\>** so we will have example of what we mean by that and benefits of fungibility  
> **\<r​ecanman:agoradesk.com\>** I have to leave the meeting. Goodbye everyone and thank you plowsof for moderation  
> **\<v​ostoemisio:matrix.org\>** x3nu: Is probably up to work on the scripts while we wait for the second half funding, x3nu  ? No time would be wasted  
> **\<l​ordx3nu:matrix.org\>** atomic swaps and seraphis are indeed constantly changing. althought seraphis I think would be ideal once it is finalized because this is the largest hardfork  in Monero's history  
> **\<o​frnxmr:monero.social\>** Right. So why makeba video on fungibikity when xmr is not yet fungible?  
> **\<o​frnxmr:monero.social\>** Ita like making news reports on "whats to come"  
> **\<p​lowsof:matrix.org\>** recanman vote on the last one before you leave?  
> **\<p​lowsof:matrix.org\>** e. [escapethe3RA Monero Observer maintenance (2023 Q4)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge\_requests/414)  
> **\<o​frnxmr:monero.social\>** merge  
> **\<l​ordx3nu:matrix.org\>** it would be like making a video on privacy but monero isn't perfectly private. it isn't an on or an off switch but an ideal that development for Monero aims for  
> **\<r​ecanman:agoradesk.com\>** +merge, Monero observer I look at all the time  
> **\<p​lowsof:matrix.org\>** monero.observer left our minds, but never our hearts and has been back the past week pushing out content as usual  
> **\<o​frnxmr:monero.social\>** Didnt check price, bur merge if same as last  
> **\<p​lowsof:matrix.org\>** thanks for attending recanman  
> **\<p​lowsof:matrix.org\>** price is the same rates as the prev  
> **\<r​ecanman:agoradesk.com\>** I checked almost every day on whether monero.observer was back. It's great. Goodbye  
> **\<m​onerobull:matrix.org\>** i suggest you to set up an rss reader instead  
> **\<o​frnxmr:monero.social\>** G2g too  
> **\<o​frnxmr:monero.social\>** back in a few  
> **\<m​onerobull:matrix.org\>** https://matrix.monero.social/\_matrix/media/v1/download/matrix.org/XvlSJVtviXKzgOWYRKVgYwjz  
> **\<m​onerobull:matrix.org\>** its so good  
> **\<l​ordx3nu:matrix.org\>** we think it would be a good idea to introduce the topic as part of running a node because the question of "what can I do to help Monero" comes up a lot. it wouldn't be a literal guide but a guide emphasizing the difference between centarlized pools and p2pool and why long term p2pool is what we should aim for  
> **\<m​onerobull:matrix.org\>** yeah that is good  
> **\<plowsof\>** thanks all for attending, we can call an end to the meeting here. we have to come to a decision on how to move forward with the core monero concepts proposal asap  

## rottenwheel | 2023-10-21T07:02:18+00:00
@plowsof Interesting. Compare both logs above. Also, for some reason the issue isn't getting closed after it posts the log. 

## plowsof | 2023-10-21T12:12:17+00:00
thanks! seems more readable on GH, please review https://github.com/plowsof/post-libera-meeting-logs/issues/2#issuecomment-1773770917

i stopped closing the issue when the logs get posted as it felt abrupt. closing when the next meeting is posted gives people time to see what happened

# Action History
- Created by: plowsof | 2023-10-06T10:03:10+00:00
- Closed at: 2023-10-21T13:41:22+00:00
