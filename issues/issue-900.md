---
title: 'Monero Community Workgroup Meeting: Saturday 30th September 2023 @ 15:00 UTC'
source_url: https://github.com/monero-project/meta/issues/900
author: plowsof
assignees: []
labels: []
created_at: '2023-09-25T11:28:40+00:00'
updated_at: '2023-10-04T13:48:57+00:00'
type: issue
status: closed
closed_at: '2023-10-04T13:48:57+00:00'
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
    - Recent bounty @ https://bounties.monero.social/ [Nostr client for Monero](https://bounties.monero.social/posts/94/8-520m-nostr-client-for-monero) Tips OR Zaps?.
    - [Nerostr: a Nostr paid relay, but with Monero (new version)](https://monero.town/post/648493) - pluja of kycnot.me
    - silverpill shares [Mitra update](https://codeberg.org/silverpill/mitra/releases/tag/v1.36.0) cross-server Monero payments on a federated social network. A [bounty](https://bounties.monero.social/posts/22/1-850m-monero-tip-bot-for-mastodon-pleroma) would add a tipping feature to it, any support appreciated!
    - anhdres has started a new (mainly) spanish-speaking podcast. Cafe Nero https://linktr.ee/cafemonero https://www.yewtu.be/watch?v=CDlQGCVJ8DE
    - Bitmain X5 images released [img dot ur](https://imgur.com/a/S03VsWf) - [r*ddit thread](https://www.reddit.com/r/Monero/comments/16txlhq/bitmains_x5_has_been_cracked_open_here_is_whats/) 
    - [Istanbul meetup sponsored by localmonero.co](https://www.reddit.com/r/Monero/comments/16q4k21/istanbul_meetup_sponsored_by_localmoneroco/) Siren and Stnby to attend to present Monero ATM's next milestones (what after pizza box) and also Metronero.
    - [Upcoming Jamtis Dynamic View Tag Design Discussion/Poll](https://www.reddit.com/r/Monero/comments/16uxj28/upcoming_jamtis_dynamic_view_tag_design/) - jeffro256
    - [Monero non-standard fee research](https://github.com/Rucknium/misc-research/tree/main/Monero-Nonstandard-Fees) - Rucknium
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard) - [Monero Moon](https://www.themoneromoon.com/)    
5. [CCS updates](https://ccs.getmonero.org/)   | [Limite update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371#note_22460) - geonic | [Animated explainer video update](https://www.yewtu.be/watch?v=vjn9l3hG4ME) - vosto emisio
  a. [recanman to take over Monero integrations pt. 3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/402) Merged
  b. [Add retroactive funding proposal for FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)  Merging soon because  'if not funded in x months - i receive what was raised and consider it as being paid in full' was added
  c. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/406)   Merged 
  d. [Selfhosted tor gitea instance of monero source](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/408)    
  e. [dangerousfreedom - wallet work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409)    
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
     - [Response to a Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE
COUNCIL on the legal tender of euro banknotes and coins](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/13429-Clarifying-the-legal-tender-status-of-euro-banknotes-and-coins/F3436571_en)    
     - the search for a g**gledocs alternative continues. next candidate: https://www.getoutline.com/ Dan/123bob123     
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
    https://github.com/monero-project/meta/issues/899 
9. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/893)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-10-02T12:00:18+00:00
Logs 
```
15:00:06 <plowsof> Meeting time https://github.com/monero-project/meta/issues/900

15:00:21 <plowsof> Greetings, hi

15:00:38 <m-relay> <r​ecanman:agoradesk.com> Hello

15:00:41 <m-relay> <o​frnxmr:monero.social> Gmorning

15:00:44 <m-relay> <v​ostoemisio:matrix.org> Hey

15:01:00 <m-relay> <1​23bob123:matrix.org> ^

15:01:48 <m-relay> <m​ichael:monero.social> Hello.

15:02:38 <m-relay> <p​lowsof:matrix.org> summer, is over! hope everyone is happy and well, lets discuss some
community highlights while we all arrive

15:03:21 <m-relay> <r​ucknium:monero.social> Hi

15:04:41 <m-relay> <1​23bob123:matrix.org> Fruit basket?

15:04:55 <m-relay> <p​lowsof:matrix.org> https://bounties.monero.social/ has seen some activity lately, mainly
around the nostr client for Monero https://bounties.monero.social/posts/94 ,, i wonder if pluja would be up to
the task (spoiler: he is busy atm) but also shared an update on one of his nostr related projects [Nerostr: a
Nostr paid relay, but with Monero (new version)](https://monero.town/post/648493)

15:05:33 <m-relay> <p​lowsof:matrix.org> Ruckniums recent research about fee abnormalities (briefly discussed
yesterday) https://libera.monerologs.net/monero-community/20230929#c284802

15:06:21 <m-relay> <p​lowsof:matrix.org> would an explainer at https://rucknium.me/ be beneficial?

15:06:22 <m-relay> <p​lowsof:matrix.org> blog*

15:07:08 <m-relay> <r​ucknium:monero.social> I might do that.

15:08:21 <m-relay> <p​lowsof:matrix.org> Bitmain x5 miner seems to have been a disaster, overheating / dusty.
it also can not mine anything other than Monero ( always keep an eye on the #monero-pow:monero.social,
interesting stuff discussed there)

15:08:40 <m-relay> <p​lowsof:matrix.org> Bitmain X5 images released [img dot ur](https://imgur.com/a/S03VsWf)
- [r*ddit
thread](https://www.reddit.com/r/Monero/comments/16txlhq/bitmains_x5_has_been_cracked_open_here_is_whats/)

15:09:17 <m-relay> <p​lowsof:matrix.org> [Upcoming Jamtis Dynamic View Tag Design
Discussion/Poll](https://www.reddit.com/r/Monero/comments/16uxj28/upcoming_jamtis_dynamic_view_tag_design/) -
jeffro256

15:09:30 <m-relay> <o​frnxmr:monero.social> Not even wownero?!

15:09:48 <m-relay> <p​lowsof:matrix.org> this r*ddit thread required some propaganda for "pro dynamic
viewtags" - thankfully tevador rose to the occasion and rbrunner gladly relayed the messages

15:10:13 <m-relay> <p​lowsof:matrix.org> MAYBE townforge gold !

15:10:21 <m-relay> <p​olar9669:matrix.org> Nope, only xmr and they might release firmware/sw update

15:10:40 <m-relay> <1​23bob123:matrix.org> Firmware fixes smoke?

15:11:00 <m-relay> <r​ecanman:agoradesk.com> Yes, but it would have to bring hashrate down

15:11:18 <m-relay> <r​ecanman:agoradesk.com> Yes, but it would have to bring hashrate down, it would have to
monitor temperatures if it doesn

15:11:24 <m-relay> <r​ecanman:agoradesk.com> Yes, but it would have to bring hashrate down, it would have to
monitor temperatures if it doesn't already

15:11:35 <m-relay> <r​ecanman:agoradesk.com> Yes, but it would have to bring hashrate down, it would have to
monitor temperatures if it doesn't already and bring down clock speed

15:11:47 <m-relay> <1​23bob123:matrix.org> Sounds efficient

15:12:01 <m-relay> <o​frnxmr:monero.social> (Sidenote: careful/avoid with edits. The log get messy)

15:12:14 <m-relay> <p​lowsof:matrix.org> spanish speaking persons out there - anhdres has you covered with a
new Cafe Nero podcast (links and into video here) Cafe Nero https://linktr.ee/cafemonero
https://www.yewtu.be/watch?v=CDlQGCVJ8DE

15:12:46 <m-relay> <p​luja:matrix.org> Hey, indeed I was taking a look at how this could be done yesterday and
I might give it a shot soon, but I can't promise anything yet... :)

15:12:54 <m-relay> <o​frnxmr:monero.social> We need a list of podcasts coming our of community

15:13:30 <m-relay> <p​lowsof:matrix.org> pluja of (kycnot.me, whishper.net, blogo.site, the new nerostr,
awesome-privacy...) :slau

15:13:35 <m-relay> <1​23bob123:matrix.org> Directory ?

15:13:41 <m-relay> <p​lowsof:matrix.org> 🫡

15:14:23 <m-relay> <o​frnxmr:monero.social> Stack wallet has stack cast etc

15:14:46 <m-relay> <1​23bob123:matrix.org> Google chromecast?

15:15:02 <m-relay> <o​frnxmr:monero.social> Thats -policy (had to)

15:15:19 <m-relay> <p​lowsof:matrix.org> and silverpill , with Mitra ,  answered(answering) questions about it
in #monero-community-dev:monero.social [Mitra
update](https://codeberg.org/silverpill/mitra/releases/tag/v1.36.0)

15:16:00 <m-relay> <p​lowsof:matrix.org> active newsletters we have [Revuo Monero](https://revuo-xmr.com/) -
[The Monero Standard](https://localmonero.co/the-monero-standard)

15:17:04 <m-relay> <p​lowsof:matrix.org> anything else we would like to mention?

15:18:23 <m-relay> <p​lowsof:matrix.org> ah yes, bp++ new price of 32k as its a greatly expanded paper (need
to get the ball rolling on that asap)

15:18:25 <m-relay> <o​frnxmr:monero.social> The meetup

15:18:44 <m-relay> <1​23bob123:matrix.org> Cheap

15:18:56 <m-relay> <p​lowsof:matrix.org> oh ofcourse, Siren and Stnby attending it. [Istanbul meetup sponsored
by
localmonero.co](https://www.reddit.com/r/Monero/comments/16q4k21/istanbul_meetup_sponsored_by_localmoneroco/)
Siren and Stnby to attend to present Monero ATM's next milestones (what after pizza box) and also Metronero.

15:19:11 <m-relay> <o​frnxmr:monero.social> Istanbul meetup sponsored by localmonero.co Siren and Stnby to
attend to present Monero ATM's next milestones (what after pizza box) and also Metronero.

15:19:18 <m-relay> <p​lowsof:matrix.org> 2nd of October

15:19:46 <m-relay> <1​23bob123:matrix.org> Alt exposed

15:20:24 <m-relay> <p​lowsof:matrix.org> aaaand new release / tag iminent .. either today tomorrow or soon(tm)

15:20:32 <m-relay> <p​lowsof:matrix.org> imminent

15:21:10 <m-relay> <p​lowsof:matrix.org> right, shall we move on to the ccs updates. i see vostoemisio is
here!

15:21:52 <m-relay> <p​lowsof:matrix.org> i hear you released a video or something

15:22:10 <m-relay> <v​ostoemisio:matrix.org> hehe, we released it yesterday, over 5k views already on X

15:22:28 <m-relay> <v​ostoemisio:matrix.org> https://youtu.be/vjn9l3hG4ME?si=b5n6WWwnxlTRHtSM

15:23:11 <m-relay> <v​ostoemisio:matrix.org> Great feedback so far, if anyone have any input or ideas for
improvement please let me know

15:23:20 <m-relay> <p​lowsof:matrix.org> nice work 👍️ , seems to have completed your open CCS
https://ccs.getmonero.org/proposals/VOSTOEMISIO-TailEmission-Concept-Video.html 🫡 (pending the open source of
the files and such)

15:24:16 <m-relay> <v​ostoemisio:matrix.org> We've already cleaned up the source files, I can upload them
later today

15:24:19 <m-relay> <o​frnxmr:monero.social> I haven't watched yet 🙈

15:25:45 <m-relay> <r​ucknium:monero.social> "miners would be forced to raise tx fees". I don't agree with
this statement. Miners don't set fees. See Theorem 1 of "Monopoly without a Monopolist"

15:26:19 <m-relay> <r​ucknium:monero.social> Thanks, Vosto

15:26:22 <m-relay> <p​lowsof:matrix.org> pending the reception of this then, we could circle back round and
tackle the older proposal https://ccs.getmonero.org/proposals/savandra-videos-for-monero.html (a discussion
for another day/meeting) e.g. savandra vs vosto to resume/take over - or repurpose funds toward another
animated proposal

15:27:38 <m-relay> <p​lowsof:matrix.org> checking my calandar, there should be an oscar nominated movie
[Limite update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/371#note_22460) -
geonic

15:28:08 <m-relay> <o​frnxmr:monero.social> Voice message.ogg

15:28:36 <m-relay> <o​frnxmr:monero.social> Accident ^

15:29:18 <m-relay> <1​23bob123:matrix.org> I dont like the  comment about the community in the update

15:29:23 <m-relay> <1​23bob123:matrix.org> Need stay on topic with update

15:29:23 <m-relay> <o​frnxmr:monero.social> Same.

15:30:25 <m-relay> <o​frnxmr:monero.social> > On a not so grateful note, I'd like to add that since opening
this proposal, I've been on the receiving end of a campaign of harassment, abuse, libel and doxxing --
threatened and actual -- by a group of vindictive downvoters, some of whom are in this thread. These purported
"community members" are actively working against the wishes of the donors who supported the proposal. I
v<clipped message>

15:30:25 <m-relay> <o​frnxmr:monero.social> iew this behavior as a long-term threat to the CCS and hope some
remedial action is taken.

15:30:59 <m-relay> <1​23bob123:matrix.org> Not warranted tbh

15:32:04 <m-relay> <1​23bob123:matrix.org> Heres my update, show me the money

15:32:30 <m-relay> <o​frnxmr:monero.social> Also called for banning of people who scrutinize in progress ccs
proposals.

15:33:03 <m-relay> <p​lowsof:matrix.org> i dont think geonic is here atm , we can jump into the bans issue
later on

15:33:51 <m-relay> <o​frnxmr:monero.social> id just like to make nite

15:33:59 <m-relay> <o​frnxmr:monero.social> Note, or clarify

15:34:36 <m-relay> <p​lowsof:matrix.org> thanks ! nowww recapping the random merges on a tuesday

15:34:50 <m-relay> <o​frnxmr:monero.social> That in progress ccs proposals arent "do whatever you want"
periods.. youre expected to deliver, or keep us updated etc, no?

15:34:52 <m-relay> <p​lowsof:matrix.org> a. [recanman to take over Monero integrations pt.
3](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/402) Merged - GLHF

15:35:09 <m-relay> <r​ecanman:agoradesk.com> Thank you. It's going well so far. I'll send a progress update
soon.

15:35:35 <m-relay> <o​frnxmr:monero.social> Purgatory ccs are all technically "in progress"

15:35:39 <m-relay> <p​lowsof:matrix.org> do you feel confident about the 2nd milestone,, the gateway work?

15:36:08 <m-relay> <r​ecanman:agoradesk.com> I've looked into it, and it is not too hard.

15:36:33 <m-relay> <p​lowsof:matrix.org> recanmann to completed one of the oldest purgatory / in progress ccs'

15:36:42 <m-relay> <r​ecanman:agoradesk.com> I haven't worked with wordpress too much, but it shouldn't be too
hard to set it up locally and play around with it

15:36:54 <m-relay> <1​23bob123:matrix.org> Was created on a scroll

15:37:04 <m-relay> <1​23bob123:matrix.org> Its that old

15:37:19 <m-relay> <p​lowsof:matrix.org> i have no new updates to present for any of the others btw sadly ..
(haveno back end / not ccs related is moving at a nice pace with updates)

15:37:58 <m-relay> <1​23bob123:matrix.org> Sdk ?

15:38:10 <m-relay> <p​lowsof:matrix.org> keep us updated with your progress recanmann 🙏

15:38:56 <m-relay> <p​lowsof:matrix.org> valldrac: is active / probably has updates to share yes (molly itself
is being updated with new features such as multi device support etc)

15:39:18 <m-relay> <1​23bob123:matrix.org> And edit message

15:39:22 <m-relay> <o​frnxmr:monero.social> Multidevice support is a signal feature, no?

15:39:25 <m-relay> <1​23bob123:matrix.org> Winrar *

15:39:26 <m-relay> <o​frnxmr:monero.social> That too

15:39:37 <m-relay> <p​lowsof:matrix.org> it was recently just added to molly

15:39:54 <m-relay> <r​ecanman:agoradesk.com> I don't think so, but I've never used signal

15:39:59 <m-relay> <p​lowsof:matrix.org> moving on with the tuesday night merge list:

15:40:04 <m-relay> <p​lowsof:matrix.org> b. [Add retroactive funding proposal for
FCMPs](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/403)  Merging soon because
'if not funded in x months - i receive what was raised and consider it as being paid in full' was added

15:40:14 <m-relay> <p​lowsof:matrix.org> kayabanever has added that, so it will be merged soon(tm)

15:40:29 <m-relay> <p​lowsof:matrix.org> he added a period of 2 months

15:41:38 <m-relay> <p​lowsof:matrix.org> c. [Create Educational Content in
Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/406)   Merged for funding @
https://ccs.getmonero.org/funding-required/

15:42:23 <m-relay> <p​lowsof:matrix.org> GL Lovera 🙏

15:42:24 <m-relay> <o​frnxmr:monero.social> Sounds good 2 me

15:42:42 <m-relay> <1​23bob123:matrix.org> Yep

15:43:05 <m-relay> <p​lowsof:matrix.org> d. [Selfhosted tor gitea instance of monero
source](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/408)

15:43:05 <m-relay> <p​lowsof:matrix.org> has added a comment https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/408#note_22516

15:43:12 <m-relay> <p​lowsof:matrix.org> 4rkal has been hosting the instance already since posting the
proposal

15:43:28 <m-relay> <r​ecanman:agoradesk.com> I don't think it should be funded IMO

15:44:06 <m-relay> <r​ecanman:agoradesk.com> There are already thousands of decentralized mirrors - that is
called git

15:44:09 <m-relay> <p​lowsof:matrix.org> perhaps he could address the concerns i raised in my comment, i
personally don't see it as being useful

15:45:00 <m-relay> <r​ucknium:monero.social> Possibly useful things: Practical PGP-based web of trust,
checking how many commits to the monero repo are signed (is it all?), researching ways to make sure no commits
are missing.

15:45:35 <m-relay> <1​23bob123:matrix.org> Someone needs to get monero off proprietary software

15:45:47 <m-relay> <r​ecanman:agoradesk.com> Pretty much impossible

15:45:52 <m-relay> <r​ecanman:agoradesk.com> For the majority of users

15:45:59 <m-relay> <p​lowsof:matrix.org> we have hashes up to a certain point/state i guess they could be...
signed

15:46:50 <m-relay> <1​23bob123:matrix.org> So the og proposal was started because of tornado cash and github
deleting devs

15:47:53 <m-relay> <p​lowsof:matrix.org> if your opinion of this ccs is negative - could it be changed to an
updoot? if yes, do you have any suggestions to change it? if no then please vote to close . i do commend 4rkal
for the honest milestone/payout structure and hosting it already

15:48:07 <m-relay> <r​ecanman:agoradesk.com> I vote to close

15:48:32 <m-relay> <r​ecanman:agoradesk.com> I vote to close. It's a nice idea but impractical in practice -
we are putting trust in a person for hosting the decentralized mirror

15:48:38 <m-relay> <r​ecanman:agoradesk.com> I vote to close. It's a nice idea but impractical in practice -
we are putting trust in a (random) person for hosting the decentralized mirror

15:48:52 <m-relay> <p​lowsof:matrix.org> 4rkal also received a double bounties payout - and refunded the money
to all involved , so he's an honest person (long story dont ask)

15:48:54 <m-relay> <r​ecanman:agoradesk.com> And the notion of git being decentralized already...

15:48:55 <m-relay> <4​rkal:matrix.org> If it was up to me I would have moved all monero repos off GitHub. Not
a good idea to have a privacy project on GitHub. I do understand that for some reason it has been decided to
host them on GitHub. So what I'm proposing is a way to interact with the code (view clone etc) in a Foss
censorship resistant manor. I do understand the concerns about trust and am open to suggestions.

15:49:28 <m-relay> <o​frnxmr:monero.social> There was a long discussion about moving away from github

15:49:36 <m-relay> <o​frnxmr:monero.social> Should read that first

15:49:45 <m-relay> <1​23bob123:matrix.org> Tldr

15:49:48 <m-relay> <r​ecanman:agoradesk.com> ^

15:50:57 <m-relay> <r​ucknium:monero.social> This isn't the "long discussion", but some info on "backups":
https://libera.monerologs.net/monero-dev/20220809#c131094

15:51:31 <m-relay> <p​lowsof:matrix.org> thanks Rucknium

15:51:52 <m-relay> <o​frnxmr:monero.social> https://github.com/monero-project/meta/issues/236

15:52:18 <m-relay> <p​lowsof:matrix.org> thanks ofrnxmr, 4rkal can read and respond to suggestions following
this meeting.  with 8 minutes left (with another proposal and a hot topic to cover)

15:52:44 <m-relay> <p​lowsof:matrix.org> e. [dangerousfreedom - wallet
work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409)

15:53:25 <m-relay> <1​23bob123:matrix.org> Say github rm -rf monero there is a backup/mirror?

15:53:37 <m-relay> <p​lowsof:matrix.org> previous ccs completed / payout requested (i assume waiting for a
review of sorts / 'we're pleased' from the workgroup rbrunner .. and then to handle the new one

15:53:50 <m-relay> <r​ecanman:agoradesk.com> https://git.wownero.com/monero-project/monero

15:55:30 <m-relay> <r​ecanman:agoradesk.com> Unrelated note, https://lbsrc.getmonero.org is down

15:55:30 <m-relay> <p​lowsof:matrix.org> previous ccs update rbrunner https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/377#note_22413

15:55:54 <m-relay> <r​ecanman:agoradesk.com> I say merge, his work is very much needed.

15:56:16 <m-relay> <1​23bob123:matrix.org> Cloudflare

15:56:38 <m-relay> <o​frnxmr:monero.social> And -dev

15:56:40 <m-relay> <r​ecanman:agoradesk.com> Especially with the seraphis wallet PoC

15:57:38 <m-relay> <p​lowsof:matrix.org> thanks for the report, moving quickly on, a policy update - [Response
to a Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE

15:57:38 <m-relay> <p​lowsof:matrix.org> COUNCIL on the legal tender of euro banknotes and
coins](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/13429-Clarifying-the-legal-
tender-status-of-euro-banknotes-and-coins/F3436571_en)   #monero-policy:monero.social ,,, Dan r/dark (Is not
the man & Braxman Tomsparks Advocate ) has also been working on degoogling things for them so they can produce
the a<clipped message>

15:57:38 <m-relay> <p​lowsof:matrix.org> bove types of papers using e.g. onlyoffice

15:58:13 <m-relay> <1​23bob123:matrix.org> Yest

15:58:19 <m-relay> <p​lowsof:matrix.org> finally, bans,     https://github.com/monero-project/meta/issues/899

15:58:26 <m-relay> <1​23bob123:matrix.org> Waiting on midi too test

15:58:38 <m-relay> <r​ecanman:agoradesk.com> This will be an interesting topic to discuss

15:58:43 <m-relay> <p​lowsof:matrix.org> Matrix/IRC Lack of proper moderation^

15:59:13 <m-relay> <1​23bob123:matrix.org> I think my post says enough

15:59:16 <m-relay> <p​lowsof:matrix.org> now, 2 or 3 days ago the situation came to a head , and people skept
on it, and it seems to be civil now? is my understanding correct?

15:59:31 <m-relay> <1​23bob123:matrix.org> Think so

15:59:32 <m-relay> <o​frnxmr:monero.social> When it comes to moderation vs administration, i find a lot of
mods to be opportunistic.

16:00:13 <m-relay> <1​23bob123:matrix.org> But it come to me making an issue doe something to be done

16:00:17 <m-relay> <1​23bob123:matrix.org> But it come to me making an issue for something to be done

16:00:52 <m-relay> <1​23bob123:matrix.org> Beside plowsof there isnt consistent mods in rooms

16:00:58 <m-relay> <o​frnxmr:monero.social> Its been a thing for a long time. Mostly from those with the most
power

16:01:33 <m-relay> <1​23bob123:matrix.org> And then banning in reso room :/

16:01:34 <m-relay> <o​frnxmr:monero.social> They don't participate, and but happily jump on the banhammer if
someone they dont like speaks up

16:02:09 <m-relay> <o​frnxmr:monero.social> Example from months ago "does anybody mind if i ban endogenic?"
From an admin that doesnt even attend meetings or reply to developers DM's

16:02:16 <m-relay> <p​lowsof:matrix.org> i ban kitty without warning / unban apologise - then do nothing other
times

16:02:48 <m-relay> <o​frnxmr:monero.social> Imo admins should admin. Mods should mod

16:03:02 <m-relay> <o​frnxmr:monero.social> Admins shouldnt moderate groups they arent even active in

16:03:45 <m-relay> <o​frnxmr:monero.social> And most of all, mods should put their username in the ban reason
when using banhammer

16:04:16 <m-relay> <1​23bob123:matrix.org> Or ban from gui

16:04:27 <m-relay> <1​23bob123:matrix.org> That shows names

16:05:04 <m-relay> <o​frnxmr:monero.social> we have plenty of admin issues (bad history settings in maby
rooms, no logging setup, no bridges) etc

16:05:33 <m-relay> <1​23bob123:matrix.org> Thats the other thing why isnt resolutions logged?

16:05:55 <m-relay> <o​frnxmr:monero.social> Because charuto "said no bridges allowed"

16:06:20 <m-relay> <1​23bob123:matrix.org> So no logs and no history

16:06:30 <m-relay> <o​frnxmr:monero.social> So, also it means no irc users allowed

16:06:41 <m-relay> <1​23bob123:matrix.org> Yep

16:07:13 <m-relay> <1​23bob123:matrix.org> Youd think other mods would attend this meeting

16:07:14 <m-relay> <p​lowsof:matrix.org> this topic is open ended/on-going , i think we can end the meeting
soon/here after going over a bit

16:07:32 <m-relay> <o​frnxmr:monero.social> yes sir. Can end meeting

16:07:49 <m-relay> <1​23bob123:matrix.org> Sleepy time

16:07:56 <m-relay> <o​frnxmr:monero.social> Point here: we need to select admins and their duties, mods and
their duties, and change them when necessary

16:08:10 <m-relay> <o​frnxmr:monero.social> We have some rooms admin by dead accounts

16:08:23 <plowsof> thanks all for attending ^ nioc has or has not renamed to something else


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2023-09-25T11:28:40+00:00
- Closed at: 2023-10-04T13:48:57+00:00
