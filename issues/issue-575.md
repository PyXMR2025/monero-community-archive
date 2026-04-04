---
title: Move all IRC channels to Libera.chat
source_url: https://github.com/monero-project/meta/issues/575
author: fluffypony
assignees: []
labels: []
created_at: '2021-05-25T15:49:04+00:00'
updated_at: '2022-07-20T23:26:06+00:00'
type: issue
status: closed
closed_at: '2022-07-20T23:26:06+00:00'
---

# Original Description
For those who haven't been paying attention, all of the Freenode staff have left due to [Freenode ownership changing hands](https://www.kline.sh), and starting to monetise their user data. Those staff have setup a new IRC network, [Libera Chat](https://libera.chat). Loads of major projects have already moved (including CentOS, Ubuntu, Grafana, Fosdem, the Python Software Foundation, Wikimedia, Wikipedia, Curl, CouchDB).

We've already been given the Monero namespace on Libera, so we can claim #monero- channels where they don't have an existing owner (or where the existing owner is different to the owner on Freenode). We had the same privilege on Freenode, so we're grateful that they've set this up for us. More importantly, we have a great relationship with the Libera staff, and no relationship with the new Freenode staff - to that end, my IRC bouncer was k-lined, which means both myself and @moneromooo-monero were off IRC for a bit - I'm still trying to get them to remove the k-line so I can reconnect.

For users of the various bridges (Matrix, Slack, MatterMost, Discord) this change will be invisible to you, so you don't need to worry about it at all.

As to why we are sticking with IRC: there is a long, deep relationship between IRC and open-source projects. Many of the contributors to Monero's codebase live in a command-line world, and are comfortable with IRC clients. It would be unthinkable for us to try force them to either use a GUI, or learn an entirely new text-based Matrix client. IRC as a foundational link between all these services is also really useful.

The only major thing missing from Libera right now is a native Tor server. They are working on their Tor infrastructure, and in the interim we can make a plan for any contributors who want to use IRC over Tor (eg. by letting them use my bouncer). We have also considered moving to OFTC, but the general consensus seems to be to stick to the network where we already have a relationship with the staff, and where we can help them grow.

For this thread, I would love to hear any *objections* to moving to Libera. Please don't post suggestions about dropping IRC altogether, as mentioned above that is not on the cards right now. Feel free to indicate your specific support for this, too, if so inclined.

# Discussion History
## jtgrassie | 2021-05-25T15:52:57+00:00
Fully support.

## rbrunner7 | 2021-05-25T15:57:30+00:00
Support.

A little off-topic maybe, but for this transition, assuming it will go ahead, can we do (or should we do) something to prevent bad actors creating well-known user names and register them?

## 00-matt | 2021-05-25T16:02:02+00:00
> can we do (or should we do) something to prevent bad actors creating well-known user names and register them?

A bot went through and tried to register a bunch of nicks that it saw on Freenode on Libera. If the bot (or anyone else) is squatting your name you can ask nicely in `#libera` for them to drop the existing registration so that you can re-register it.

## serhack | 2021-05-25T16:07:09+00:00
Full support. 

## cirocosta | 2021-05-25T16:15:23+00:00
👍 

## dEBRUYNE-1 | 2021-05-25T17:03:30+00:00
Has my support!

## SChernykh | 2021-05-25T17:20:40+00:00
+1

## ArticMine | 2021-05-25T17:32:32+00:00
I fully support this move. 

From a technical point of view, It will be necessary to fully inform the community and provide necessary instructions for the transition for those who are not using a bridge. 

## SamsungGalaxyPlayer | 2021-05-25T17:51:14+00:00
100% behind transitioning, while still recommending that most people use Matrix directly because it's easier to moderate. Element is the most common app, but there are many others (including CLI apps).

https://forum.monero.space/d/83-join-the-monero-core-team-matrix-server

## AncientSion | 2021-05-25T18:18:26+00:00
Will this effect the Monero-Discord and the various bridges ?

## FreeBitcoins-com | 2021-05-25T18:26:03+00:00
Support.

## fluffypony | 2021-05-25T18:44:58+00:00
> Will this effect the Monero-Discord and the various bridges ?

I specifically mentioned the bridges in the post:) They're unaffected by this, the bridges will just be updated to point to Libera instead of Freenode.

## marvin8 | 2021-05-25T20:01:02+00:00
Fully Support.

## geonic1 | 2021-05-26T00:09:44+00:00
Do eet.

The “old” Freenode admins (jess in particular) have been super helpful in mitigating the spam attacks we’ve experienced. Let’s keep that relationship.

## reesericci | 2021-05-26T01:22:06+00:00
+1

## PuppyLover101 | 2021-05-26T06:32:08+00:00
Supported

## somerandompiggo | 2021-05-26T12:10:05+00:00
Definitely. Fully support.

## hyc | 2021-05-26T13:18:18+00:00
Full support. The freenode admins seized the OpenLDAP Project channels and removed my op and voice privs. At this point they're no better than pirates. The sooner we're out of there the better.

## fluffypony | 2021-05-26T15:17:37+00:00
Alright, looks like we're moving, see everyone on Libera :)

## selsta | 2021-05-27T19:37:16+00:00
Connecting via Tor is now possible: https://libera.chat/guides/connect#accessing-liberachat-via-tor

Appears that only Matrix bridge is missing before we can switch.

## erciccione | 2021-05-28T09:37:14+00:00
There are some issues on matrix side at the moment. Better wait until the problems are solved: 

https://github.com/matrix-org/matrix-appservice-irc/issues/1323
https://github.com/matrix-org/matrix-appservice-irc/issues/1324 (for general tracking of the status of the bridge)

## erciccione | 2021-05-30T06:42:23+00:00
Can somebody clarify the status of the migration? There has been no coordination at all and looks like room admins and bots operators are all doing whatever they think it's best. My rooms are still not migrated, but the merge bots are migrated to libera and some monero rooms now relay on libera and others do not.

## fluffypony | 2021-05-30T14:21:26+00:00
@dEBRUYNE-1 is writing a blog post, once that's live then we can put that in all the channel topics and maybe put a bot in all the channels to let people know we've moved. Matrix and other bridges are in the process of shifting over.

## scottAnselmo | 2021-05-30T23:29:58+00:00
> Can somebody clarify the status of the migration?

rehrar seems to be the person leading the charge, at least in terms of getting ChanOps as needed on Libera side to handshake the bridges. FWIW, the list of Matrix rooms on Monero.social that have/had a freenode equivalent sorted by people count desc

monero-dev
monero-community
monero-research-lab
monero-space
monero-support
monero-research-lounge
monero-italia
monero-mrw
monero-site
monero-memes
monero-markets
monero-events
monero-gui
monero-swap
monero-translations
monero-outreach
monero-policy
monero-pow
monero-offtopic
monero-pools
monero-pt

Other:

mastering-monero
haveno
haveno-dev

## erciccione | 2021-06-01T08:20:30+00:00
FYI the status of the matrix bridge is tracked here: https://github.com/matrix-org/matrix-appservice-irc/issues/1324

I would wait for the bridge to be ready before we start the migration.

>  list of Matrix rooms on Monero.social

@sanecito you forgot `#monero`

## erciccione | 2021-06-05T13:03:49+00:00
> monero-dev
monero-community
monero-research-lab
monero-space
monero-support
monero-research-lounge
monero-italia
monero-mrw
monero-site
monero-memes
monero-markets
monero-events
monero-gui
monero-swap
monero-translations
monero-outreach
monero-policy
monero-pow
monero-offtopic
monero-pools
monero-pt

Most of these rooms are currently broken on matrix and has been like this for some time. In some of these rooms (i haven't tested them all) Matrix users don't see IRC messages if they are not sent by OPs. The MRL channels are completely broken on both IRC and matrix (voice only channels but nobody has voice). I've been pinging people everywhere but without success, hopefully here the problem will be more visible and somebody will work on fixing it. Most of these rooms appear empty, but i know there have been discussions.

## selsta | 2021-06-05T13:05:27+00:00
#monero-markets matrix bridge moved successfully to Libera without issues.

What is stopping the other channels from moving at this point?

> The MRL channels are completely broken on both IRC and matrix (voice only channels but nobody has voice).

MRL channels work fine on Libera, only matrix bridge missing.

## erciccione | 2021-06-05T13:19:50+00:00
> What is stopping the other channels from moving at this point?

-markets and -pools migrated on their own initiative, but as i pointed out multiple times, the matrix bridge is not ready and matrix devs suggest to not use it yet. The bridge is unstable and it's creating issues, which in some cases are not reversible (https://github.com/monero-project/meta/issues/575#issuecomment-850290217).

The absence of coordination and people acting on their own is causing all kind of problems, including matrix users being completely isolated.

> MRL channels work fine on Libera, only matrix bridge missing.

So there are active MRL channels on libera? My feeling is that part of the community already migrated to Libera (even if the migration hasn't been officialized yet https://github.com/monero-project/meta/issues/575#issuecomment-851008222) and part is still on freenode, but the bridges are stable only on freenode (except those migrated by personal initiative of the matrix admin of those rooms). Also, there has been no communication of any type about the fact that these channels are now active on libera but not on freenode.

If a migration is planned, should be also coordinated. Matrix users are isolated and are probably not aware of it and freenode users haven't been communicated that some channels are now not active on libera but not on freenode, because they silently migrated.

This is chaos.

## selsta | 2021-06-13T18:02:52+00:00
Freenode banned all IRCCloud users permanently. I'm only on Libera now and also moved the `xmr-pr` bot.

Until the bridge moves Matrix users can connect to Libera manually using this guide: https://kparal.wordpress.com/2021/06/01/connecting-to-libera-chat-through-matrix/

## fluffypony | 2021-06-13T22:47:27+00:00
Ok so next steps are:

1. @dEBRUYNE-1 is working on a blog post
2. Put the blog post in the channel topics on Freenode
3. (optional) have a bot that auto-kicks anyone who joins after 5 mins?

The question is whether we do 2 and/or 3 before or after the Matrix bridge issues are fixed.

## scottAnselmo | 2021-06-13T23:31:13+00:00
I would suggest all three happen after at least -dev, -community, and monero... maybe -MRL and -gui are all bridge migrated to Libera on Matrix to avoid disruption by Freenode operators. Freenode has shown they're all for punishing FOSS projects before they can migrate, and while Monero's migration has been featured in major news outlets like Vice, a formal blog post is likely to invite more eyes, potentially Freenode's this time around.

The Matrix bridge for Libera is supposed to be released this Monday, so should be fine to wait another ~24 hours: https://matrix.org/blog/2021/06/11/this-week-in-matrix-2021-06-11#liberachat-irc-bridge-work-continues



## scottAnselmo | 2021-06-14T16:34:32+00:00
"Hi folks, the bridge is effectively live now and we're not going to monitor this thread for bug reports. We'd instead ask you interact via either the #libera-matrix:libera.chat Matrix room or create a new issue on this repo for us to triage."

https://github.com/matrix-org/matrix-appservice-irc/issues/1324#issuecomment-860694474

## HoverHalver | 2021-07-23T06:06:56+00:00
Not everybody seems to appreciate matrix
https://www.hackea.org/notas/matrix.html
(comes from #monero-markets)

## erciccione | 2021-10-31T08:54:00+00:00
Writing here because hopefully it will get attention:

There are problems with the matrix server or the IRC bridge. Users have been reporting for quite some time that some of their messages are not relayed to IRC (or the other way round). Nobody has done anything yet, but the complains are almost daily. I left the chatroom of matrix moderators (and i don't have intention to join it again), so i'm writing here to try to draw some attention to the issue.

Furthermore, the #monero room on matrix and IRC are not communicating. At the moment there are 2 monero rooms on two different platforms that don't communicate with each other.

Whomever is taking care of the migration and the matrix server need to step up and soon. Only who has access to the server's config can do something or even get an idea of what the problem is.

Problems to the Monero infrastructure are frequent and are usually slowly processed if recognized at all. Usually we have to hope that a good soul will spend their time pinging people until the problem is solved.

**I propose once again to the core team to hire somebody dedicated to take care of the infrastructure of Monero**. Voluntary help is not enough anymore and has been causing delays and problems for a long time (for example, some changes to the backend i requested long time ago are still not completed, regardless my continuous pings and requests for updates: https://github.com/monero-project/monero-site/issues/903 https://github.com/monero-project/monero-site/issues/1085).

## scottAnselmo | 2021-10-31T16:50:34+00:00
> Whomever is taking care of the migration and the matrix server need to step up and soon. Only who has access to the server's config can do something or even get an idea of what the problem is.

You don't need to be a home server instance admin to know as root cause has been discussed on -community a great deal. pigeons has stated multiple times on -community the #monero issue of no bridge is due to the arbitrary 100+ person exception request Matrix Support requires which pigeons has followed up on multiple times. I suggest kindly pinging pigeons on -community to see if they can follow up once again with Matrix Support and maybe this time Matrix Support will act.

pigeons, sgp, Seth, and myself have been diligent in working w/ Matrix Support to resolve bugs in -dev and elsewhere. Per above thread Matrix Support owns the bridge and has said for any bugs w/ the app service bridge they own should be raised in #libera-matrix:libera.chat. Alternatively, you can ping the relevant Monero room admins for rooms still seeing odd bridge issues and I'm sure they could raise Matrix Support if you don't want to.

## danrmiller | 2021-11-01T21:35:19+00:00
I last received notification 14 Oct from Matrix Support that #monero-gui and #monero-pools plumbing was working properly. If this is not the case please provide me details. 

That left these rooms remaining in the "not-working" category, which they said would be addressed 15 Oct, but I haven't had confirmation or followed up on them. I will check into them now:

#monero-space to !dNHEplVyfwtUhqDdKF:matrix.org
#monero-swap to !towEEjZCMEMNYZFhlS:monero.social
#monero to !psOvWRiQkyosOPKvaO:matrix.org
#monero-hardware to !HoCZRUWeTZDNBfUcDr:matrix.org

## SamsungGalaxyPlayer | 2021-11-03T21:22:06+00:00
@erciccione the only thing we can do beyond what we have been doing is host our own IRC bridge infrastructure. I don't think anyone is willing to step up to do that. Besides that, the issue does not lay at the hands of the migration team. Matrix has limits on the room size to bridge, so unless we wanted to kick a bunch of people, we can't proceed.

## Cactii1 | 2022-07-20T23:24:18+00:00
I think this issue can be marked as closed.

# Action History
- Created by: fluffypony | 2021-05-25T15:49:04+00:00
- Closed at: 2022-07-20T23:26:06+00:00
