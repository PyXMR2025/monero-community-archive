---
title: 'Monero Community Workgroup Meeting: Saturday 22nd July 2023 @ 15:00 UTC'
source_url: https://github.com/monero-project/meta/issues/864
author: plowsof
assignees: []
labels: []
created_at: '2023-07-14T00:17:15+00:00'
updated_at: '2023-08-18T19:17:41+00:00'
type: issue
status: closed
closed_at: '2023-08-18T19:17:41+00:00'
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
News: [Monero Observer](https://www.monero.observer/) (On vacation) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/) (Last issue Jan)    
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [recanman bitejo rewrite and expansion proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/395)    changed / revisit
  b. [Glitter Finance Cross-Chain Privacy Infrastructure with Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/396)    Close
  c. [Serving Defcon 31 (2023)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/397)    Close
  d. [XMR Business Wallet Development](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/398)    Close
  e. [Continued Feather Wallet development (3 months)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/400)    merge 
  f. [j-berman full-time 3 months (part 5)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/401) merge / wait for some MRL/Seraphis Migration/Dev feedback
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

[Previous meeting including logs](https://github.com/monero-project/meta/issues/857)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2023-07-22T18:47:19+00:00
Logs 
```
15:00:11 <plowsof11> meeting time https://github.com/monero-project/meta/issues/864

15:00:30 <plowsof> Greetings

15:01:17 <Rucknium[m]> Hi

15:01:21 <plowsof> matrix is playing up for me but the IRC bridge is working thankfully

15:02:08 <hbs[m]> 👋

15:02:58 <blankpage[m]> Hello

15:03:07 <plowsof> lets share some community highlights while people come in 3. Community highlights

15:03:33 <plowsof> the new / final bulletproofs++ paper is here https://libera.monerologs.net/monero-research-
lab/20230720#c268352. The first auditors, CypherStack, will provide an update some time in August (because the
paper is now different / complete, i can only assume the scope of the audit may require changes / cost
adjustments. The MRL team can discuss this

15:03:33 <plowsof> after CS provide feedback of the final paper).

15:05:25 <recanman[m]> Hello

15:05:32 <plowsof> https://libera.monerologs.net/monero-community/20230710#c267159 "Buy and sell information
on the owner of any blockchain wallet address—anonymously, via smart contract." Lovera has tested it out for
us. No support for Monero (transparent blockchains only)

15:06:11 <blankpage[m]> I wonder if you could poison the system by selling fake info 🤔

15:06:19 <tobtoht[m]> Hi

15:06:32 <plowsof> after reaching out to several auditors/cryptography researchers for adding security proofs
to the Seraphis paper(s), the initial feedback has been 'can we arrange a call' whereas for the bp++ audit,
which the MRL was able to provide feedback on an actual scope of work, a quote for time / cost was easily
obtaininable for comparison, i've recommended

15:06:32 <plowsof> the same to be done for the Seraphis papers to remove alot of friction from the process.
jberman and koe will collaborate in creating a more detailed scope

15:08:11 <plowsof11> blankpage[m]: a pretty graph goes a long way

15:08:26 <msvb-lab> Hello, sorry late.

15:08:51 <plowsof> hello

15:09:25 <plowsof> just sharing some highlights of the past 2 weeks if anyone wants to share something

15:10:10 <blankpage[m]> To confirm, there are some funds raised and allocated for bp++++++ audit (but the
eventual cost is unknown) whereas the audits for seraphis are essentially unknown and unfunded at this point?

15:10:32 <plowsof11> [Revuo Monero](https://revuo-xmr.com/) - [The Monero
Standard](https://localmonero.co/the-monero-standard)  have been 2 active newsletters during this period and
the author of revuo, rottenwheel has joined this channel

15:10:39 <recanman[m]> Does anyone know when escapethe3RA will be back to write the Monero observer?

15:11:12 <plowsof11> blankpage yes - the bp++ audit funds where for an earlier version of the paper

15:11:16 <recanman[m]> s/observer/Observer/

15:11:30 <plowsof11> currently trying to obtain quotes for seraphis work

15:12:00 <Rucknium[m]> blankpage: BP++ now has security proofs. Those security proofs need to be checked to
make sure there is no flaw in them. Seraphis is lacking security proofs. Those need to be written. Then those
proofs need to be checked.

15:12:03 <plowsof11> no updates from escape3RA about return date

15:12:53 <Rucknium[m]> The original BP++ paper had a vulnerability in it, too. (According to ACK-J)

15:14:02 <blankpage[m]> Is there a post about that somewhere Rucknium? The vulnerability

15:14:53 <plowsof> in the papers changelog "Fixed soundness vulnerability in range proofs that required the
introduction of new challenge

15:14:53 <plowsof> variable δ to the arithmetic circuit protocol."

15:15:10 <plowsof> i do not know what this means

15:15:54 <Rucknium[m]> blankpage: https://libera.monerologs.net/monero-research-lab/20230720#c268403

15:16:59 <plowsof> shall we move on to the CCS proposals?

15:17:32 <recanman[m]> Looks like

15:17:37 <plowsof> first impressions of the new bp++ paper from cypherstack coming in august*

15:18:14 <plowsof11> 4. [CCS updates](https://ccs.getmonero.org/)

15:18:24 <plowsof11>   a. [recanman bitejo rewrite and expansion proposal](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/395)

15:18:43 <recanman[m]> I thought about making a separate CCS for the jobs, but I am confident that I can
finish it in one CCS.

15:19:10 <recanman[m]> I've already been working on it for fun (I am going to make it, but much slower if it
doesn't get funded), and things have been going well.

15:19:59 <plowsof11> proposal has not changed since 3 weeks. it will stay on the ideas page and rot away as it
stands right now imo

15:20:11 <recanman[m]> I don't feel that any changes are necessary.

15:20:58 <blankpage[m]> I will restate my opinion that I am not against such proposals but I would not donate
because it requires network effects etc. to be successful rather than being a technical problem

15:21:46 <ofrnxmr[m]> Greetings #late

15:21:47 <Rucknium[m]> If you get something successful running, then maybe apply to CCS for
maintenance/expansion

15:22:15 <recanman[m]> Since it would be a hobby project, it would take a year at minimum.

15:22:40 <blankpage[m]> Most successful monero market website is a janky ugly mess but people will go wherever
the people are

15:22:56 <recanman[m]> I'm planning to promote it with LocalMonero

15:23:18 <plowsof11> has localmonero promoted bitejo?

15:23:35 <recanman[m]> No, they have not

15:24:00 <recanman[m]> I don't think the original creator of Bitejo ever contacted them.

15:24:51 <ofrnxmr[m]> I had suggested removing the jobs portion of the ccs (- name: Month 4 (Begin jobs
service backend) (80 hours) funds: 15 XMR done: status: unfinished - name: Month 5 (Finish jobs service
backend) (80 hours) funds: 10 XMR ) -25xmr

15:25:14 <recanman[m]> Could you remind me of the reasoning for that?

15:25:59 <ofrnxmr[m]> brings it to 30 xmr for work, 15 for maintenance and hosting etc

15:26:09 <ofrnxmr[m]> New ccs later for the jobs part

15:26:22 <plowsof11> the proposal does not require changes according to recanman, which has received many
suggestions during that time. if people would like more time to make a decision on merge/close (or willing to
vote now) please say/do so

15:26:46 <ofrnxmr[m]> 30xmr for current stuff

15:26:46 <ofrnxmr[m]> 25 for jobs

15:26:46 <ofrnxmr[m]> 15 for maintenance

15:26:46 <ofrnxmr[m]> cut the jobs stuff for now

15:28:58 <recanman[m]> I am about to make the changes

15:29:13 <plowsof11> i would vote close on its current form, but do not want to deter recanman from coming
back with something more appealing

15:29:46 <plowsof11> discuss it again next meeting and move on?

15:29:57 <recanman[m]> ofrnxmr[m]: > <@ofrnxmr:monero.social> 30xmr for current stuff... (full message at
<https://libera.ems.host/_matrix/media/v3/download/libera.chat/db6b5a574163f572a558b826bf5df01a59e7632a>)

15:30:03 <recanman[m]> Total 45 XMR for four months of work

15:30:13 <ofrnxmr[m]> Close in current form, but since making changes, wait 2 weeks and revisit i think

15:31:16 <ofrnxmr[m]> recanman:  thanks. we'llsee before the next meeting if anyone has anything else to
suggest.

15:31:17 <plowsof11> lets revisit next time and discuss more in the interim

15:31:46 <recanman[m]> By next meeting, I won't be able to commit the four months.

15:32:03 <plowsof11> would anyone like to revisit any of the previous proposals that where voted for being
closed

15:32:05 <ofrnxmr[m]> Thats ok

15:32:19 <plowsof11>   b. [Glitter Finance Cross-Chain Privacy Infrastructure with
Monero](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/396)    Close

15:32:19 <plowsof11>   c. [Serving Defcon 31 (2023)](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/397)    Close

15:32:19 <plowsof11>   d. [XMR Business Wallet Development](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/398)    Close

15:33:21 <recanman[m]> I say close them all

15:33:28 <ofrnxmr[m]> recanman[m]: You can begin work anytime and bill later.

15:33:28 <ofrnxmr[m]> should probably change your milestones description from "month1, 2 etc" to "as work is
completed".

15:33:45 <blankpage[m]> Nah close the three proposals

15:33:52 <ofrnxmr[m]> B. Close

15:33:52 <ofrnxmr[m]> C. Close

15:33:52 <ofrnxmr[m]> D. Close

15:34:24 <ofrnxmr[m]> Unless glittrr wants to sponsor us

15:35:34 <plowsof11> thanks to everyone who is leaving feedback here and also on the gitlab

15:35:37 <ofrnxmr[m]> * sponsor us /s

15:36:29 <plowsof11> moving on then..

15:36:49 <plowsof11> e. [Continued Feather Wallet development (3 months)](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/400)

15:37:19 <plowsof11> tobtoht listed some items on the todo list today https://libera.monerologs.net/monero-
community/20230722#c268628

15:37:21 <recanman[m]> I don't use Feather Wallet personally, but I've seen it and it is pretty great

15:37:22 <recanman[m]> +merge

15:38:01 <blankpage[m]> Merge feather always 🪶

15:38:07 <plowsof11> the background sync with view keys only pull request from jberman is also up for review.
an update was provided here (with links to the associated bounty) https://github.com/monero-
project/monero/pull/8619#issuecomment-1632951461 - its nice to see feather wants to integrate it asap

15:38:47 <ofrnxmr[m]> I like that feather wants to

15:39:38 <ofrnxmr[m]> But unless the fixes make it back upstream in less than a year 😅 TOBBY! Haha

15:39:51 <ofrnxmr[m]> (referring to proxy leak and dns leak, polyseed etc)

15:40:42 <rbrunner> (Comment from a lurker: I am reviewing that background sync PR right now.)

15:40:50 <tobtoht[m]> That DNS leak happened to be an accidental fix, I wasn't aware of it.

15:41:29 <tobtoht[m]> rbrunner: I will review it too (not accepting the bounty)

15:42:00 <plowsof11> tobtoht has been handling tech support / bug reports / sharing updates in
#feather:monero.social

15:42:00 <Rucknium[m]> rbrunner: Could you explain background sync simply? What makes it different from the
way sync happens now?

15:42:49 <ofrnxmr[m]> View keys

15:43:04 <rbrunner> "Background" in this case means "While you don't have the wallet open in the app".

15:43:27 <rbrunner> It's kept open in the background, in a pretty secure way, and collects info about
incomming transactions.

15:43:44 <nioc> also on IRC OFTC network #feather

15:43:45 <rbrunner> If you "open" the wallet again in the app, it will be synced "officially" withing seconds.

15:44:13 <ofrnxmr[m]> So wallet can keep syncing in background without having spend keys in memory (?)

15:44:13 <ofrnxmr[m]> am i remembering wrong?

15:44:18 <plowsof11> afaiu but injb (im not jberman) - the wallet will re-scan all the inputs received using
the spend key to double check if they are realchange

15:44:36 <plowsof11> that where found during background view key scanning

15:44:40 <rbrunner> Yes, that's the "magic" that this PR implements - the spend secret key is NOT around

15:45:00 <Rucknium[m]> Does this use the change "heuristic" to recognize spent txs?

15:45:23 <plowsof11> +merge for tobtoht. thanks for the #feather room nioc (i keep joining the empty #monero-
feather lol

15:45:44 <rbrunner> No, it just collects all rings where any of your outputs occur. Later, with the spend
secret available again, it sorts things out

15:45:58 <Rucknium[m]> since the view key cannot directly recognize spent funds.

15:46:02 <ofrnxmr[m]> +1 Merge btw

15:46:48 <Rucknium[m]> +1 merge on Feather continued development

15:47:07 <plowsof11> injb and i think no heuristics are needed because the spend key verifies if theyre change
/ real

15:47:17 <plowsof11> after the fact

15:47:27 <plowsof11> pls confirm

15:47:30 <ofrnxmr[m]> 0xffc:  joining us?

15:47:43 <rbrunner> Yes, no heuristics are involved

15:47:44 <ofrnxmr[m]> (that was a ping)

15:48:22 <Rucknium[m]> Does it assume that the user doesn't have a second wallet that is spending funds?

15:49:04 <rbrunner> No, that's no problem: If you collect *all* rings where any of your outputs occur, you
catch such spendings

15:49:15 <Rucknium[m]> Does it check every tx that uses a given output to see if it's....

15:49:36 <Rucknium[m]> I see. Check all rings that use the output. Makes sense

15:50:14 <Rucknium[m]> You check those rings with the spend key when your load it. Since there are only a few
of those txs, it's a quick check. Right?

15:50:24 <rbrunner> Exactly.

15:50:25 <Lovera[m]> <plowsof11> "[Revuo Monero](https://revuo-xmr..." <- Welcome? 😅

15:50:32 <ofrnxmr[m]> https://github.com/m2049r/xmrwallet/issues/785#issuecomment-1079569991 Rucknium:

15:50:32 <Rucknium[m]> Very nice :)

15:50:48 <ofrnxmr[m]> Some early discussion is here

15:51:23 <Lovera[m]> I’m late but my vote merges for feather 🚀

15:51:23 <plowsof11> hello!

15:52:11 <Lovera[m]> B, C and D for me Close

15:52:31 <Lovera[m]> <plowsof11> "  b. [Glitter Finance Cross-..." <- > <@plowsof:matrix.org>   b. [Glitter
Finance Cross-Chain Privacy Infrastructure with Monero](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/396)    Close

15:52:31 <Lovera[m]> >   c. [Serving Defcon 31 (2023)](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/397)    Close

15:52:31 <Lovera[m]> >   d. [XMR Business Wallet Development](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/398)    Close

15:52:31 <Lovera[m]> Here

15:53:00 <plowsof11> positive / merge sentiment for feather 🪶

15:53:18 <plowsof11> moving on...

15:53:20 <tobtoht[m]> Thanks all ♥️

15:53:58 <plowsof11>   f. [j-berman full-time 3 months (part 5)](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/401)

15:54:02 <tobtoht[m]> +1 berman

15:54:48 <Rucknium[m]> I've raised doubts about whether it's a good idea to code a protocol that has no
security proofs yet: https://libera.monerologs.net/monero-research-lab/20230705#c263993

15:55:07 <Rucknium[m]> If the community wants to go ahead with it, that's fine.

15:55:17 <ofrnxmr[m]> +1

15:55:24 <Rucknium[m]> It could be wasted effort

15:55:26 <Lovera[m]> We need Dev work seraphis and all this stuff so +1  merge berman

15:55:37 <recanman[m]> +merge

15:56:53 <plowsof11> perhaps adding in hours to collab with koe to create a detailed spec for auditors /
cryptographers to obtain quotes from people easier could be added (i dont know how long this would take)

15:57:00 <ofrnxmr[m]> Rucknium:  do you suggest we try to get proofs done asap?

15:57:11 <Rucknium[m]> ofrnxmr: Yes

15:57:12 <hbs[m]> isn't it a little early to work on including FCMP in the wallet lib?

15:57:32 <Rucknium[m]> hbs: IMHO, yes

15:58:34 <rbrunner> It needs to be tested thouroughly, and I am not sure building tests around it would be
much faster than plugging it into the library for testing ...

15:58:40 <Rucknium[m]> We don't know how we would get the security proofs for Curve Trees done. AFAIK,
kayabaNerve is knocking on some doors to see who could work on it

15:58:40 <plowsof11> ideally these things can be discussed in MRL/no wallet left behind meetings also

15:59:43 <Rucknium[m]> rbrunner: What's "it"?

15:59:59 <rbrunner> The FCMP code

16:00:53 <ofrnxmr[m]> Im still +1 merge berman. Id rather not derail any momentum theyve created. Even if work
doesnt pan out, maybe we'll find out before seraphis is even ready :P

16:02:32 <plowsof11> so jberman merge / get feedback from MRL/no wallet left behind

16:03:21 <nioc> Merge jberman

16:03:22 <rbrunner> Sounds good to me

16:03:42 <nioc> Also, merge jberman

16:04:01 <ofrnxmr[m]> i think merge before next meeting

16:04:02 <ofrnxmr[m]> If no negative feedback from mrl/NWLB/dev

16:04:35 <plowsof11> AOB

16:05:36 <ofrnxmr[m]> Im assume kayabanerve:  would say merge

16:05:41 <plowsof11> msvb-lab shared in events that there will be a meeting in 1 hour

16:05:41 <ofrnxmr[m]> Anything else on the agenda?

16:05:50 <plowsof11> no

16:06:48 <ofrnxmr[m]> monerokon is doing a lot of restructuring

16:07:35 <plowsof11> #monero-translations:monero.social recently pushed a bunch of french translations to
-site (yes, we still have passionate volunteers creating/reviewing translations 🙏)

16:07:47 <ofrnxmr[m]> So if involved with monerokon, or want tl be, pay attention to Monero Events  because
planning is already underway

16:09:19 <plowsof11> "Finance Committee" to address concerns over reimbursement issue iirc , and other
things.. creating a none profit to not have to rely on Digital Renegades for things / become independant

16:11:14 <plowsof11> seems like we've came to an end, thank you all for joining and enjoy the rest of your
weekend 👍️


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued:

```
16:11:51 <msvb-lab> Good meeting and dankon everyone.
16:13:34 <ofrnxmr[m]> ah. One last note
16:14:12 <ofrnxmr[m]> Libera rooms will work differrnt with matrix soon. Youll need to join the matrix rooms
16:14:22 <ofrnxmr[m]> For example... (full message at <https://libera.ems.host/_matrix/media/v3/download/libera.chat/33fc535610d1939252b53ae89295588ee2921bb5>)
16:15:15 <ofrnxmr[m]> If you are joining from matrix and are in Libera.Chat #p2pool-log etc. I would recommend to move onto these (as they are plumbed and working already) before the cutoff date of portalled room https://libera.chat/news/matrix-deportalling
16:24:15 <datahoarder[m]> Thanks for mentioning, was going to do the same here but was waiting for meeting to be over :)
16:27:18 <tobtoht[m]> <ofrnxmr[m]> "But unless the fixes make it..." <- Yeah, I recently became aware that Monerujo is using a wallet_api extension for their pocketchange feature that I wrote for Feather eons ago and realized I could have saved them some time had that been available in core, so I think you're right to point this out and I will give upstreaming stuff higher priority going forward.
```

# Action History
- Created by: plowsof | 2023-07-14T00:17:15+00:00
- Closed at: 2023-08-18T19:17:41+00:00
