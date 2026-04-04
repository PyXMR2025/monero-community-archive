---
title: Meeting about the mining subreddit and the quality of the Monero chats
source_url: https://github.com/monero-project/meta/issues/433
author: erciccione
assignees: []
labels: []
created_at: '2020-01-25T10:35:53+00:00'
updated_at: '2020-01-27T16:04:18+00:00'
type: issue
status: closed
closed_at: '2020-01-27T16:04:18+00:00'
---

# Original Description
**Location**
[Freenode](https://kiwiirc.com/nextclient/#irc://irc.freenode.net/#monero-community) | [Mattermost](https://mattermost.getmonero.org/monero/channels/monero-community) | [Matrix](https://matrix.to/#/!ecCZkSsvFtDOcBBQha:matrix.org?via=matrix.org&via=ru-matrix.org&via=matrix.kiwifarms.net) | Irc2P

`#monero-community`

**Time**

26 January 18:00 UTC (After dev meeting)

**Meeting items**

- The subreddit */r/moneromining* is run by an individual who: (i) Use the subreddit for their own private goals, without listening to the feedback of moderators (ii) Published racist content and refused to take it down, insulting anyone who criticized them. The subreddit is one of the most recognized and active, but it's a tickling bomb and we should find an alternative as soon as possible. (For reference: https://repo.getmonero.org/monero-project/monero-site/merge_requests/1195)
- Some monero chats are getting out of control in terms of quality of the content. Discussion on how to create a more welcoming environment for newcomers and keep conversations on topic.

# Discussion History
## Cactii1 | 2020-01-26T17:55:20+00:00
Which Monero chats are getting out of control?

## erciccione | 2020-01-26T19:34:28+00:00
logs:

```
Jan 26 19:00:09 <ErCiccione>	alright here we are
Jan 26 19:00:16 <asymptotically>	merry meetingmas
Jan 26 19:00:36 <ErCiccione>	Thanks everybody for being here to discuss this unpleasant subject. The agenda is here: https://github.com/monero-project/meta/issues/433 and the points in discussion are two:
Jan 26 19:00:50 <ErCiccione>	- Moving away from /r/moneromining after the recent events (see description of this PR: https://repo.getmonero.org/monero-project/monero-site/merge_requests/1195)
Jan 26 19:00:58 <ErCiccione>	- Discussion about the quality of the Monero chats, some of which are lightly moderated and higly off topic
Jan 26 19:01:13 <ErCiccione>	Before we start i have to point out that when i called out the racist description in #Monero-pools, which i erroneously considered the official chat of /r/moneromining (My misunderstanding was caused by the fact that the chat was near the word 'official' in the top of the page when seen from the old reddit. The issue has been fixed since)
Jan 26 19:01:29 <ErCiccione>	i was fiercley attacked by some of the active people in the chat, especially by a single person: rottensox, who defended the racist chat description, doubled down using racist slang and repeatedly insulted me. That behaviour was disgusting and i think it needs to be called out.
Jan 26 19:01:42 <ErCiccione>	I hope this incident will make the community more vigilant and sensitive about the subject and that this meeting will help to set some guidelines to avoid the rise of a similar problem.
Jan 26 19:01:55 <asymptotically>	i don't think #monero-pools ever had a racist topic. there's a site somewhere that has a full history of all the topics that have been set
Jan 26 19:02:04 <Mochi101>	Sounds legit.
Jan 26 19:02:13 <M5M400>	ErCiccione: you're mixing things up. the "racist" description was on a reddit chat, not #monero-pools
Jan 26 19:02:29 <ErCiccione>	sorry guys, my mistake. I meant /r/moneromining
Jan 26 19:03:00 <ErCiccione>	Now, let's start with point one:
Jan 26 19:03:18 <ErCiccione>	1) Moving away from /r/moneromining
Jan 26 19:03:36 <Mochi101>	ErCiccione, can you give an example of the racist slang? Or do we just have to take your word for it?
Jan 26 19:04:07 <sgp_>	Mochi101: someone was banned from this channel temporarily for offensive language
Jan 26 19:04:15 <ErCiccione>	Mochi101: "welcome to the SJW-riddled world in which anything you say can be considered natzi!!!" "we are demons!!!! we killed (((them)))."
Jan 26 19:04:16 <sgp_>	The point of this meeting isn't to document it
Jan 26 19:04:32 <ErCiccione>	those are just a couple, logs are public on monero-pools
Jan 26 19:04:53 <Mochi101>	So the three parentheses is the racist thing?
Jan 26 19:05:07 <sgp_>	Mochi101: yes especially in this case
Jan 26 19:05:14 <sgp_>	Let's not play dumb
Jan 26 19:05:39 <Mochi101>	Actually I've never heard about the 3 ( until like a week ago.
Jan 26 19:05:43 <hyc>	fwiw all of these culturla references went over my head
Jan 26 19:06:07 <Mochi101>	So if the "SJWs" want to keep moving the goal posts...
Jan 26 19:06:37 <sgp_>	In any case we don't need to have that discussion here about what Mochi101 knows about racist statements
Jan 26 19:07:11 <ErCiccione>	so, about /r/moneromining
Jan 26 19:07:11 <M5M400>	we should however discuss that this: https://github.com/monero-project/meta/issues/433 is not accurate
Jan 26 19:07:11 <sgp_>	Topic is moving away from the subreddit
Jan 26 19:07:24 <M5M400>	because this is basically the argument for the proposed move
Jan 26 19:07:39 <sgp_>	Lead mod is impossible to work with
Jan 26 19:07:44 <hyc>	Have we actually, explicitly stated that "racism = bad" here? I'm taking it as a given, but maybe not everyone is on the same page
Jan 26 19:07:55 <sgp_>	And is using the subreddit to advance their "anti-snowflake" agenda
Jan 26 19:08:00 <M5M400>	sgp_: I'd say challenging, but not impossible
Jan 26 19:08:02 *	rbrunner (~rbrunner@31-12-138-91-cust-static.fcom.ch) has joined
Jan 26 19:08:22 <sgp_>	M5M400: what action has taken out of compromise at all?
Jan 26 19:08:29 <asymptotically>	was usrn ever a part of the community? i've only been here for a couple of years but i have never seen him around
Jan 26 19:08:36 <M5M400>	sgp_: he has taken it down.
Jan 26 19:08:48 <M5M400>	upon request from me
Jan 26 19:08:59 <gweentea>	I can confirm racist and homophobic remarks on monero related irc channels. Theres also some nazistic remarks and cryptic chat with it. That's all I can say.
Jan 26 19:09:02 <sgp_>	asymptotically: he was to a small extent early on
Jan 26 19:09:29 <sgp_>	M5M400: I think that's a really low bar
Jan 26 19:09:33 <needmonero90>	Same.
Jan 26 19:09:48 <needmonero90>	He has demonstrated a distinct lack of leadership qualities
Jan 26 19:09:54 <M5M400>	sgp_: i have to agree that it bothers me that he is not willing to give up the control over the channel
Jan 26 19:10:06 <sgp_>	For example I was removed for removing a BCH post in r/cryptocurrency
Jan 26 19:10:13 <hyc>	irc channel? or subreddit? is he in charge of both?
Jan 26 19:10:16 <needmonero90>	Usrn being head mod of any part of our ecosystem is a liability.
Jan 26 19:10:19 <M5M400>	so for me it's basically a decision between dealing with it vs. rebuilding a community
Jan 26 19:10:21 <sgp_>	Just the sub for now hyc
Jan 26 19:10:23 <asymptotically>	hyc: just subreddit
Jan 26 19:10:46 <hyc>	I agree, from my interactions with him, I view him as a liability
Jan 26 19:10:54 <sgp_>	I think this meeting was brought about since it is a huge liability now
Jan 26 19:10:56 <Mochi101>	Going to have a hard time rebuilding.
Jan 26 19:11:04 <M5M400>	^this
Jan 26 19:11:05 <sgp_>	Not just could be
Jan 26 19:11:09 <needmonero90>	And it will not get easier to fix in the future
Jan 26 19:11:11 <sgp_>	It IS a liability
Jan 26 19:11:22 <sgp_>	With already-seen negative impacts
Jan 26 19:11:33 <needmonero90>	This needs to be dealt with before the ecosystem gets any bigger
Jan 26 19:11:47 <needmonero90>	Having it happen after the CPU mining fork is unfortunate
Jan 26 19:11:47 <Mochi101>	So what needmonero90 and sgp_ are saying is that you want centralized control over some parts of the community?
Jan 26 19:11:48 <M5M400>	i'm kinda having a deja-vu needmonero90 ;)
Jan 26 19:11:52 <needmonero90>	That would have made it way easier
Jan 26 19:12:26 <needmonero90>	M5M400: I've already argued this point once, and you overrode it. It's coming up again. I very much hope it doesn't happen a third time.
Jan 26 19:12:32 <sgp_>	Mochi101: haha no way
Jan 26 19:12:34 <Mochi101>	and you're willing to underhandedly make a request to reddit admins to take that control?
Jan 26 19:12:43 <needmonero90>	Wut
Jan 26 19:12:53 <sgp_>	Mochi101: Reddit admins aren't responsive but I would if they were responsive
Jan 26 19:12:59 <needmonero90>	Where on earth are you getting that from
Jan 26 19:13:17 <hyc>	some degree of control is useful, yes. if we as a community have a policy of "no racism" and a moderator - a person in a position of leadership - isn't abiding by that policy
Jan 26 19:13:27 <M5M400>	needmonero90: let's factor in that this chat topic was set before the first incident with deopping sgp_
Jan 26 19:13:29 <hyc>	then we need a means to take action
Jan 26 19:13:33 <sgp_>	Right, it's about accountability not "control"
Jan 26 19:13:35 <M5M400>	just nobody noticed
Jan 26 19:13:50 <needmonero90>	He reverted it multiple times afterwards
Jan 26 19:13:57 <M5M400>	he reverted it ONCE
Jan 26 19:14:06 <needmonero90>	Still, that occurred after.
Jan 26 19:14:09 <M5M400>	(yes, once is too often still
Jan 26 19:14:10 <sgp_>	That alone is total bullshit
Jan 26 19:14:11 <selsta>	no one noticed because it requires the new design
Jan 26 19:14:25 <M5M400>	and because noone uses that chat
Jan 26 19:14:47 <M5M400>	I'm inclined to disable it
Jan 26 19:15:09 <rehrar>	Mochi101, he can retain control, but then we just won't link to it from official core team sources.
Jan 26 19:15:22 <hyc>	anyway, being moderator of a forum or channel that is part of a larger community doesn't mean you can use it to advance your own personal agenda.
Jan 26 19:15:24 <sgp_>	Exactly, which bring us back to theain topic
Jan 26 19:15:26 <Mochi101>	Was there a specific complaint about the "bergbau macht frei" thing from someone?
Jan 26 19:15:29 <hyc>	that's not why the community entrusts you with that role.
Jan 26 19:15:37 <rehrar>	This isn't being silenced and not centralization. People can do racist things in their racist places, but we don't have to send people there. That simple. :)
Jan 26 19:15:46 <sgp_>	How should we move over to something else
Jan 26 19:16:01 <sgp_>	needmonero90 is squatting on a similarly named subreddit
Jan 26 19:16:17 <needmonero90>	Inb4 I have dreams of centralized control and won't give it up
Jan 26 19:16:28 <sgp_>	Haha nice
Jan 26 19:16:32 <Mochi101>	It's possible
Jan 26 19:16:33 <ErCiccione>	So going back to the topic, how are we going to act? New subreddit?
Jan 26 19:16:37 <M5M400>	needmonero90: gib control
Jan 26 19:16:40 <M5M400>	:D
Jan 26 19:16:52 <needmonero90>	If this plays out, you're top of my list m5m
Jan 26 19:16:54 <hyc>	yeah, new subreddit sounds good. drop all references to the old one
Jan 26 19:16:57 <needmonero90>	Easy transition
Jan 26 19:16:57 <M5M400>	<3
Jan 26 19:17:00 <gingeropolous>	yeah, new subreddit
Jan 26 19:17:01 <ErCiccione>	i think that's the best option. Revuilding the community will be a pain, but it's necessary
Jan 26 19:17:04 <sgp_>	I think it's obvious we need a new subreddit if the lead mod isn't removed from the current sub
Jan 26 19:17:25 <M5M400>	I'm still against that, but if y'all think that's what needs to be done, be my guest
Jan 26 19:17:34 <kinghat>	sounds like a good way to go about it
Jan 26 19:17:39 <hyc>	we are forking away. community will make up their own minds which chain to follow.
Jan 26 19:18:16 <Mochi101>	I put .1 xmr on r/moneromining
Jan 26 19:18:23 <kinghat>	M5M400: what are your reasons for being against that?
Jan 26 19:18:44 <M5M400>	kinghat: haven't changed. I think it throws us back a couple of years in community building
Jan 26 19:19:01 <M5M400>	official monero mining subreddit: 10 members. GOTTA JOIN!
Jan 26 19:19:21 <M5M400>	not sure how you guys go about chosing the right sub, but I usually go with the crowded ones
Jan 26 19:19:29 <gingeropolous>	well, get usrn to step down.
Jan 26 19:19:31 <Mochi101>	You'll never build that up... People are not following likes to Reddit off of getmonero.org and the likes to find that subreddit
Jan 26 19:19:47 <asymptotically>	i don't think that the sub is particularly active anyway
Jan 26 19:19:48 <M5M400>	gingeropolous: I can certainly pitch it to him but I doubt I'll succeed
Jan 26 19:19:52 <sgp_>	Mochi101: risk we need to take
Jan 26 19:19:58 <sgp_>	It's not a huge sub
Jan 26 19:20:09 <kinghat>	M5M400: fair reasoning.
Jan 26 19:20:18 <hyc>	and we can do a few announcements in various social media channels
Jan 26 19:20:43 <M5M400>	fireice is going to have his fun with this either way
Jan 26 19:20:45 *	TheoStorm (~TheoStorm@78-22-87-51.access.telenet.be) has joined
Jan 26 19:20:48 <kinghat>	what if usrn handed the sub over but was still in a mod role?
Jan 26 19:20:59 <M5M400>	kinghat: he won't
Jan 26 19:20:59 <sgp_>	Yes but we're making the right choice
Jan 26 19:21:19 <sgp_>	New sub
Jan 26 19:21:29 <sgp_>	needmonero90: what's the new sub again?
Jan 26 19:21:30 <ErCiccione>	So, the vast majority of the people here agree with moving away. Where? /r/monerominer? currently registered by neemonero90
Jan 26 19:21:34 <rehrar>	I don't want him in a mod role either. :P
Jan 26 19:21:43 <ErCiccione>	rehrar: +1
Jan 26 19:21:45 <M5M400>	honestly, I'm not particularly fond of the current sub. it's utterly boring and I only mod it because someone has to
Jan 26 19:22:01 <hyc>	lol. it's probably good that it's boring.
Jan 26 19:22:02 <Mochi101>	So tell me how "consensus" happened here.
Jan 26 19:22:09 <gingeropolous>	yeah i don't frequent the mining sub either
Jan 26 19:22:09 <Mochi101>	I mean, for the community.
Jan 26 19:22:11 <sgp_>	Mochi101: off-topic
Jan 26 19:22:16 <Mochi101>	fuck you it's off topic
Jan 26 19:22:17 <kinghat>	is it not an option to leave things the way they are, and if he does clearly out of line this again we move to the new sub?
Jan 26 19:22:33 <ErCiccione>	Mochi101: no insults or you can just leave the meeting
Jan 26 19:22:36 *	sgp_ has kicked Mochi101 from #monero-community (being an ass)
Jan 26 19:22:45 <rehrar>	Mocho101 the same way it happens for many things with Monero. People of reputation showed up to a publicly announced meeting and talked about things.
Jan 26 19:22:48 <ErCiccione>	thanks sgp_
Jan 26 19:22:49 <rehrar>	Oh he got kicked.
Jan 26 19:22:59 *	Mochi101 (~Mochi101@unaffiliated/mochi101) has joined
Jan 26 19:23:09 <Mochi101>	because you're acting like a dictator
Jan 26 19:23:18 <rehrar>	11:22 AM <BA1719• rehrar> Mocho101 the same way it happens for many things with Monero. People of reputation showed up to a publicly announced meeting and talked about things.
Jan 26 19:23:20 <Mochi101>	How did we arrice at consenzsus?
Jan 26 19:23:31 <hyc>	I'mnot hearing a lot of dissent.
Jan 26 19:23:35 <rehrar>	And then it's shown to core and they are the final deciders of what is shown on their infrastructure.
Jan 26 19:23:46 <ErCiccione>	Mochi101: please behave decently or leave the meeting
Jan 26 19:23:52 <sgp_>	Mochi101: it's not a consensus of literally everyone. It's consensus of a group of people here to take an action
Jan 26 19:23:52 <rehrar>	If people want to be involved in the process they can come to these meetings. :)
Jan 26 19:23:57 <M5M400>	hyc: I am not in favor, but seem to be the minority
Jan 26 19:23:58 <needmonero90>	In this case, it's a consensus that encompasses the people who have control over various sidebars and wikis in our ecosystem.
Jan 26 19:23:59 <sgp_>	But next topic
Jan 26 19:24:19 <rehrar>	Hold up.
Jan 26 19:24:21 <hyc>	M5M400: you agree though that usrn is difficult to work with?
Jan 26 19:24:27 <M5M400>	I do
Jan 26 19:24:34 <hyc>	ok
Jan 26 19:24:38 <rehrar>	It needs to be noted that nobody is stopping the old sub from still existing and we're not taking it down in any way. We aren't silencing anybody.
Jan 26 19:24:50 <rehrar>	We are just choosing not to associate with it.
Jan 26 19:24:55 <gingeropolous>	let the record show!
Jan 26 19:24:59 <rehrar>	The claims of dictatorship are honestly moronic.
Jan 26 19:25:09 <rehrar>	We aren't forcing anyone to do anything.
Jan 26 19:25:10 <Mochi101>	No they're not.
Jan 26 19:25:13 <sgp_>	Right, it's more accurately worried people removing support and affiliation
Jan 26 19:25:14 <M5M400>	needmonero90: ErCiccione: did reporting the sub bear any fruits?
Jan 26 19:25:27 <sgp_>	Nope
Jan 26 19:25:31 <kinghat>	im more in favor of giving the sub another chance, only because its so easy, from a tech standpoint, to move to a different sub we are squatting on.
Jan 26 19:25:42 <rehrar>	In the same way that forking off of Monero because you don't agree, and Monero core not linking to your fork is not dictatorship.
Jan 26 19:25:51 <hyc>	kinghat: I think many chanves have already come and gone
Jan 26 19:26:01 <ErCiccione>	I strongly disagree we should keep pointing people to that subreddit because "it's easier"
Jan 26 19:26:30 <ErCiccione>	we have to make the right decision, not the easier
Jan 26 19:26:54 <hyc>	+1
Jan 26 19:27:04 <M5M400>	seems minds have been made up then
Jan 26 19:27:05 <gingeropolous>	+infinity
Jan 26 19:27:11 <rbrunner>	+1 (for the loose consensus)
Jan 26 19:27:15 <hyc>	By the way, usrn could have chosen to attend this meeting too, yes?
Jan 26 19:27:22 <kinghat>	i said its easy to switch. i mean if nothing controversial comes out of that sub again the premature move to another one seems kind of meh.
Jan 26 19:27:27 <rehrar>	hyc it's in the meta repo
Jan 26 19:27:29 <gingeropolous>	no, only people with super cool internet connections can get on IRC
Jan 26 19:27:36 <rehrar>	Though we really need a better system.
Jan 26 19:27:45 <rehrar>	Because using GitHub for meeting is the most sucky thing.
Jan 26 19:27:48 <rehrar>	But that's another topic.
Jan 26 19:27:51 <M5M400>	hyc: maybe if you made a thread about it on r/moneropools. don't think he's very active outside of this
Jan 26 19:28:03 <needmonero90>	Seems like a great head mod
Jan 26 19:28:12 <M5M400>	I wouldn't be here if the link wasn't shared 5 minutes before the meeting on #monero-pools
Jan 26 19:28:16 <sgp_>	We will link the new sub in the old one :)
Jan 26 19:28:31 <gingeropolous>	brilliant.
Jan 26 19:28:39 <rbrunner>	With takedown in 3 .. 2 .. 1
Jan 26 19:28:41 <M5M400>	sgp_: haha. I bet 0.1 xmr he won't delete it
Jan 26 19:28:49 <M5M400>	any takers?
Jan 26 19:28:49 <hyc>	will see how much of a laissez-faire mod he is then
Jan 26 19:28:54 <sgp_>	Haha
Jan 26 19:28:59 <M5M400>	I'll pin it, even
Jan 26 19:28:59 <needmonero90>	He has a temper, I wouldn't be surprised if he removed.
Jan 26 19:29:01 <ErCiccione>	ok so, the subreddit we migrate to will be /r/monerominer?
Jan 26 19:29:04 <needmonero90>	And also power fantasies
Jan 26 19:29:19 <M5M400>	"master of the universe" flair...
Jan 26 19:29:20 <ErCiccione>	and all links to /r/moneromining will be removed from core-managed platforms
Jan 26 19:29:26 <hyc>	yeah /r/monerominer sounds fine, it's already ready to go
Jan 26 19:29:36 <sgp_>	Yup and yup
Jan 26 19:29:38 <ErCiccione>	and hopefully /r/monero as well
Jan 26 19:29:46 <rehrar>	K. Next.
Jan 26 19:29:48 <gingeropolous>	nah
Jan 26 19:29:51 <needmonero90>	Ginger and I are here
Jan 26 19:29:55 <needmonero90>	And I think in agreement
Jan 26 19:30:00 <needmonero90>	Which is two of the three active mods
Jan 26 19:30:09 <needmonero90>	I think /r/Monero is covered
Jan 26 19:30:12 <ErCiccione>	Good. Next point:
Jan 26 19:30:18 <ErCiccione>	2) Quality of the Monero chats
Jan 26 19:30:30 <gingeropolous>	ruh roh
Jan 26 19:30:38 <ErCiccione>	After the issue mentioned above, the problem of some "wild" Monero chatrooms rised again, especially #monero-pools #monero-market and in minor part #monero. It's important that all 'Monero-' channels reflect the welcoming spirit our community is renown for. I know binaryfate in particular wanted to speak about the subject, so if he is here, please go ahead :)
Jan 26 19:31:09 <ErCiccione>	haven't read him here yet, so, let's give him a couple of minutes
Jan 26 19:31:59 <hyc>	I've seen some pretty questionable stuff in -markets. since we've treated is a trollbox I usually ignore it
Jan 26 19:32:16 <M5M400>	never been on there so can't say
Jan 26 19:32:19 <hyc>	but sometimes the hookers'n'lambo talk gets way too sexist
Jan 26 19:32:34 <needmonero90>	If a channel is officially designated designated for support, I think off topic chatter should be light
Jan 26 19:32:59 <hyc>	I can't really think of any problems in #monero itself
Jan 26 19:33:06 <needmonero90>	Monero is fine
Jan 26 19:33:14 <rbrunner>	Would say so also
Jan 26 19:33:22 <rehrar>	Once again, please not that core team has control over all 'monero-' channels on IRC.
Jan 26 19:33:26 <M5M400>	don't hang out there either. it's boring :)
Jan 26 19:33:28 <needmonero90>	Pools has cleaned up too
Jan 26 19:33:39 <rehrar>	If anyone wants to make #miningonmonero, they can do so, and it will be outside of core control.
Jan 26 19:33:39 <needmonero90>	Mostly afaik
Jan 26 19:34:07 <kinghat>	gl finding people to police all of this. do we just start shutting it all down?
Jan 26 19:34:10 <ErCiccione>	rehrar: all chats eith monero- can be taken over anytime by the core team
Jan 26 19:34:10 <hyc>	probably should make a #monero-miner to correspond to the subreddit
Jan 26 19:34:13 <sgp_>	I think for IRC the main points are making sure they're on topic and non-offensive. And making sure mods enforce this. I'm not volunteering to do this fwiw
Jan 26 19:34:21 <Mochi101>	Freenode will give Monero core preference if the channel name has the word monero it it though rehrar
Jan 26 19:34:21 <ErCiccione>	that was freenode's decision after they cleaned up -pools AFAIK
Jan 26 19:34:57 <M5M400>	sgp_: if you wanna target civilized off-topic too, I'm out as mod there
Jan 26 19:35:10 <ErCiccione>	i agree with sgp_. I know that some mods in -pools got powers, but they are not really active, so maybe we need more active mods there?
Jan 26 19:35:18 *	TheoStorm has quit (Quit: Leaving)
Jan 26 19:35:21 <Mochi101>	Precisely why I relinquished my powers.
Jan 26 19:35:25 <rehrar>	Mochi101: XMR then?
Jan 26 19:35:54 <Mochi101>	Maybe
Jan 26 19:36:26 <rehrar>	Fwiw I think this enforcement of high quality talk is a terrible idea.
Jan 26 19:36:30 <ErCiccione>	i would have really liked an input from the core team on this point, but we should take a stance about what is acceptable and what is not in the monero- channels
Jan 26 19:36:46 <asymptotically>	ErCiccione: freenode policy already covers a lot of things
Jan 26 19:36:50 <rehrar>	In times like meetings, yes, let there be high quality talk.
Jan 26 19:36:58 <rehrar>	In other times, let the community be a community.
Jan 26 19:37:07 <ErCiccione>	asymptotically: that policy is not enforced, that's the problem
Jan 26 19:37:09 <kinghat>	rehrar: agree. i also think its not possible.
Jan 26 19:37:13 <hyc>	yeah, you have to have room for banter and actual socializing
Jan 26 19:37:20 <rehrar>	We laugh, have fun, mourn, make jokes, etc.
Jan 26 19:37:32 <asymptotically>	ErCiccione: it is in pools. there's even freenode staff there to make sure :)
Jan 26 19:37:35 <Mochi101>	ErCiccione, there are 2 freenode cops in the channel pretty much all the time.
Jan 26 19:37:53 <rehrar>	Otherwise we become a stick-in-the-mud group that nobody wants to be around (including me :P)
Jan 26 19:38:03 <cohcho>	What are nicknames of freenode cops?
Jan 26 19:38:03 <monerobux>	cohcho: 2020-01-26 - 12:28:36 <Anonlancer> tell cohcho retarget-ratio change works like a charm, I reduced the start difficulty to 5000 without any issue
Jan 26 19:38:05 <M5M400>	I even kick when I see some stupidly grouped parantheses
Jan 26 19:38:06 <sgp_>	Roughly on topic is fine
Jan 26 19:38:08 <rbrunner>	Is pools such a magnet for bad things?
Jan 26 19:38:29 <ErCiccione>	There shouldn;t be freenode mods there to enforce the rules guys, that's the issue
Jan 26 19:38:32 <gweentea>	yeah, which is weird. there are freenode opers on those channels yet racist and sexist talk are still rampant.
Jan 26 19:38:35 <Mochi101>	Fuchs is one
Jan 26 19:38:55 <gingeropolous>	i mean, #monero-pools could continue doings its thing, and a new miner help chatroom can be started. THe only reason #monero-pools gets the noobs is because its the default IRC room for the pool software
Jan 26 19:39:13 <ErCiccione>	The freenode team intervenes only in extreme situatons, we should really avoid to get there. That's the point
Jan 26 19:39:13 <gingeropolous>	that would require getting... 2 pool admins to change the defaults
Jan 26 19:39:25 <M5M400>	ErCiccione: haven't seen them having to enforce anything since \x
Jan 26 19:39:30 <gingeropolous>	because... decentralized (lol)
Jan 26 19:39:51 <ErCiccione>	M5M400: exactly, that's what i mean with extreme situations, we shouldn't get there
Jan 26 19:40:09 <hyc>	still we should adhere to certain ideals. Being a permissionless money kinda says we value being non-discriminatory.
Jan 26 19:40:19 <ErCiccione>	That's why if pools can be a bit slight, is fine for me, but it's important to have mods which enforces freenode rules strictly
Jan 26 19:40:20 <M5M400>	but we can get there anytime in an open chatroom... not sure how to avoid?
Jan 26 19:40:28 <hyc>	so allowing racist/sexist/whatever would be hypocritical
Jan 26 19:40:42 <ErCiccione>	#which means no sexists, racists discussions or other stuff of that kind
Jan 26 19:40:46 <Mochi101>	Your certain ideals may be different than others.
Jan 26 19:41:05 <gingeropolous>	well there are other places on the internet
Jan 26 19:41:06 <ErCiccione>	nobody is talking about ideals here Mochi101
Jan 26 19:41:10 <hyc>	Mochi101: if you don't believe in permissionless money then Monero isn't for you
Jan 26 19:41:26 <Mochi101>	"hyc> still we should adhere to certain ideals."
Jan 26 19:41:37 <ErCiccione>	if you want to have sexist/racist discussions, monero- channels are not the place for you
Jan 26 19:41:47 <Mochi101>	'scuse me?
Jan 26 19:41:47 <rehrar>	Once again, we are discussing all core te stewarded areas.
Jan 26 19:41:50 <rehrar>	Team*
Jan 26 19:41:58 <ErCiccione>	ideals =/= ideology
Jan 26 19:42:00 <kinghat>	everyone wants these chats policed but nobody here wants to do it 🤷‍♂️
Jan 26 19:42:13 <rehrar>	kinghat: this is also true. :D
Jan 26 19:42:13 <gingeropolous>	just get a bot to do it
Jan 26 19:42:18 <needmonero90>	I got removed from my position as mod when I dared enforce.
Jan 26 19:42:21 <needmonero90>	so.
Jan 26 19:42:22 <ErCiccione>	kinghat: that's actually part of the problem
Jan 26 19:42:28 <needmonero90>	Thats not exactly true kinghat.
Jan 26 19:42:38 <rehrar>	Oof needmoney90 coming in with the facts
Jan 26 19:42:43 <M5M400>	kinghat: I'm willing to do it, but to my own moral compass. and I have a very high tolerance for bullshit and sarcasm/cynism...
Jan 26 19:42:44 <kinghat>	for the record i dont want to do it.
Jan 26 19:42:48 <kinghat>	lubs needmonero90.
Jan 26 19:43:20 <kinghat>	M5M400: youre obv not good enough then.
Jan 26 19:43:28 <needmonero90>	m5m big bad
Jan 26 19:43:28 <kinghat>	😁
Jan 26 19:43:37 <rehrar>	M5M400: I'd trust you. I think that's what's needed for a looser group. High tolerance, but then moderating vitrolic and destructive behavior.
Jan 26 19:43:55 <sgp_>	No that's the status quo
Jan 26 19:44:03 <M5M400>	it is.
Jan 26 19:44:09 <rehrar>	Indeed.
Jan 26 19:44:13 <Mochi101>	We're not loosers rehrar, be nice.
Jan 26 19:44:15 <Mochi101>	;)
Jan 26 19:44:26 <rehrar>	:P loose not lose
Jan 26 19:44:31 <needmonero90>	m5m is already active on the mining subreddits, and receptive to community consensus (even if it goes against his personal opinion) from what I can tell
Jan 26 19:44:47 <needmonero90>	Which is ideally what we want
Jan 26 19:45:06 <rehrar>	I completely understand that M5M400 would let things through that others might not.
Jan 26 19:45:13 <ErCiccione>	we need somebody to at least enforce freenode rules. M5M400 if you are fine with letting racism and sexism pass because in your opinion is sarcasm, you are indeed not fitting for the role
Jan 26 19:45:14 <needmonero90>	he also doesnt seem to have dreams of power, seeing as he keeps wanting to keep the old sub with the dictatorial leader
Jan 26 19:45:27 <needmonero90>	sigh
Jan 26 19:45:31 <M5M400>	power is pain
Jan 26 19:45:42 <rehrar>	Perhaps a slightly tighter control is necessary, but moving to a choking grip wouldn't be beneficial imo.
Jan 26 19:45:43 <needmonero90>	shh, not so loud or we'll never get new mods
Jan 26 19:45:57 <kinghat>	so in light of nobody stepping up to police the coms, do we shut them down? what are the options here?
Jan 26 19:46:00 <M5M400>	ErCiccione: if I spot intended racism, I step in.
Jan 26 19:46:25 <sgp_>	We need the threshold to be more restrictive
Jan 26 19:46:29 <ErCiccione>	rehrar: i think enforcing freenode's rules is very far from being a "chocking grip"
Jan 26 19:46:33 <M5M400>	hard to distinguish where the jokes end and the real racism starts though
Jan 26 19:46:33 <sgp_>	Other mods can help with that
Jan 26 19:46:56 <Mochi101>	What other mods?
Jan 26 19:47:03 <ErCiccione>	M5M400: THat "intended" is not really reasurign. So i can be racist if right after i say i'm joking? (which is often the case)
Jan 26 19:47:04 <needmonero90>	just make race/religion/politics out of bounds, potentially.
Jan 26 19:47:05 <rehrar>	Erciccione not everyone here is in agreement with what constitutes racism or sexism.
Jan 26 19:47:05 <Mochi101>	binaryFate has to be there to mod
Jan 26 19:47:22 <Mochi101>	hedgemoon has to be there to mod
Jan 26 19:47:31 <rehrar>	I, for one, don't play the identity politics game, but I still try not to be discriminatory in my speech and actions.
Jan 26 19:47:35 <Mochi101>	hegemoOn sorry
Jan 26 19:48:01 <asymptotically>	rehrar: me too. try not to be offensive, and try not to be offended :D
Jan 26 19:48:07 <rehrar>	Indeed.
Jan 26 19:48:11 <Mochi101>	so all -pools has is asymptotically and M5M400
Jan 26 19:48:23 <M5M400>	because you took the easy way out Mochi101 :P
Jan 26 19:48:32 <rehrar>	And the hand of justice that is falling here seems to stem from a left leaning view of racism and sexism.
Jan 26 19:48:41 <rehrar>	Which, if that is what is wanted, that can be discussdd
Jan 26 19:48:45 <rehrar>	But it must be defined.
Jan 26 19:48:51 <sgp_>	No it doesn't
Jan 26 19:48:58 <rehrar>	We can't assume that everyone has the same idea as what constitutes these subjects.
Jan 26 19:49:02 <dsc_>	+1
Jan 26 19:49:09 <sgp_>	Not everyone has the same view
Jan 26 19:49:10 <Mochi101>	++ rehrar
Jan 26 19:49:34 <gingeropolous>	.define racism
Jan 26 19:49:35 <monerobux>	racism — noun: 1. Belief in distinct human races, and that they have different inherent attributes or abilities, and generally that some are superior and others inferior, 2. The policy, practice or (e.g. government or political) program of promoting this belief and promoting the dominance of on[...]
Jan 26 19:49:35 <rehrar>	If we want a uniform policy, that's fine. But making sure "nobody feels offended ever" is a losing game.
Jan 26 19:49:41 <sgp_>	But we need higher standards to make the room welcoming
Jan 26 19:49:43 <gingeropolous>	.define sexism
Jan 26 19:49:43 <monerobux>	sexism — noun: 1. The belief that people of one sex or gender are inherently superior to people of the other sex or gender, 2. Different treatment or discrimination based on a difference of sex or gender
Jan 26 19:50:11 <Mochi101>	I've neer seen sexism in -pools if that's how it's defined
Jan 26 19:50:17 <rehrar>	sgp_, and this is what I'm asking. What constitutes a higher standard? It can't be nebulous?
Jan 26 19:50:26 <rehrar>	How do we measure whether the standard is met?
Jan 26 19:50:33 <ErCiccione>	now we have the definitions. If somebody is being one of those (jokingly or not) should be moderated. Sounds easy to me
Jan 26 19:50:49 <sgp_>	rehrar: we remove racist and offensive stuff in r/cc
Jan 26 19:50:57 <sgp_>	We don't have defined standards
Jan 26 19:50:57 <kinghat>	kind of think we are putting the cart before the horse here. we can decided the rules after we appoint the responsible ops.
Jan 26 19:50:59 <kinghat>	everyone in favor of making needmonero90 and M5M400 mods of the entire monero irc network say aye!
Jan 26 19:51:05 <sgp_>	If something is confusing, we discuss it
Jan 26 19:51:09 <sgp_>	It's not that hard
Jan 26 19:51:17 <rehrar>	Incorrect.
Jan 26 19:51:17 <kinghat>	🙌
Jan 26 19:51:28 <gingeropolous>	kinghat, bots i tell yah!
Jan 26 19:51:29 <rehrar>	The moderator that moderates has their internal definitions that they use as a standard.
Jan 26 19:51:44 <sgp_>	rehrar: yeah that's why communication is important
Jan 26 19:51:48 <rehrar>	They are still applying a standard. You might remove something that another mod might not.
Jan 26 19:51:58 <rehrar>	But they're not going to make a fuss about you removing it.
Jan 26 19:52:10 <needmonero90>	I don't want to moderate the network. Moderation is work, I don't get paid to do this shit
Jan 26 19:52:12 <gingeropolous>	im sure there's a machine learning algo out there
Jan 26 19:52:23 <asymptotically>	gingeropolous: google have a nice one i think
Jan 26 19:52:25 <rehrar>	So the same is applied here with the moderation of pools. If M5M400 is the mod, he will use his definitions.
Jan 26 19:52:29 <needmonero90>	Im doing my part to pitch in.
Jan 26 19:52:35 <rehrar>	If those aren't sufficient, then step up and moderate.
Jan 26 19:52:48 <sgp_>	This discussion about standards seems more philosophical than actionable
Jan 26 19:52:53 <kinghat>	didnt MS's bot get really racist, really fast?
Jan 26 19:52:54 <ErCiccione>	agreed
Jan 26 19:53:08 <Mochi101>	and that's the problem sgp_
Jan 26 19:53:11 <rehrar>	If you're not willing to step up and moderate with your definitions, then I don't know what to tell you.
Jan 26 19:53:16 <ErCiccione>	we can discuss for hours about what a standard is, but we have to be practical
Jan 26 19:53:39 <sgp_>	I agree the big issue is that we don't have anyone who really wants to do this
Jan 26 19:53:45 <M5M400>	the way I see it: regulars are often mean to each other. but noone is ever mean to the random noob seeking help - at least if said noob is not totally ignorant to the help already provided
Jan 26 19:53:47 <kinghat>	ya im not sure why we are talking about how to police if there are no police 🤷‍♂️
Jan 26 19:53:48 <rehrar>	ErCiccione: cool, the be practical and moderate the room.
Jan 26 19:53:53 <needmonero90>	sgp_: Again, I *was* willing
Jan 26 19:54:12 <rehrar>	*then
Jan 26 19:54:23 <sgp_>	needmonero90: sorry, I took your joke as your actual opinion
Jan 26 19:54:25 <needmonero90>	I intervened as a mod, and got removed.
Jan 26 19:54:27 <M5M400>	or, more precisely: when rotten tells mochi to suck his dick, there's no victim.
Jan 26 19:54:48 <Mochi101>	needmonero90, everyone would have been banned within a week using your standards of modding
Jan 26 19:54:49 <rottensox>	lol.
Jan 26 19:54:57 <gingeropolous>	well, M5M400 , that leads me to the idea that the hanging out should be in a different room not monero related. I mean, #monero-pools was where I landed 4 years ago
Jan 26 19:55:00 <gingeropolous>	maybe 5 at this point
Jan 26 19:55:05 <sgp_>	M5M400: ideally not, but there are sometimes statements that discourage others from participating. We need to be understanding of that
Jan 26 19:55:10 <gingeropolous>	hell, I think fluffypony was the one that responded to whatever I posted
Jan 26 19:55:25 <rehrar>	I think that is a good standard imo. Was there a victim? It's practical.
Jan 26 19:55:32 <M5M400>	gingeropolous: disagree. because the people in there are knowledgeable and helpful to n00bs
Jan 26 19:55:47 <rehrar>	If someone says "hey, that hurt me. Stop." Then this crime has a victim. The behavior needs to stop.
Jan 26 19:55:49 <gingeropolous>	i had the room up for a while. I don't know what I woulda thought of things if I got to witness some of the ..... banter.... that is on there now
Jan 26 19:55:51 <M5M400>	if they have their everyday trashtalk elsewhere, they wouldn't see noobs needing help
Jan 26 19:55:57 <ErCiccione>	rehrar: that's simplicistic
Jan 26 19:56:20 <gingeropolous>	i dunno. my IRC client indicates when there's room activity
Jan 26 19:56:23 <asymptotically>	gingeropolous: https://www.perspectiveapi.com/#/home AI irc mods coming soon :D
Jan 26 19:56:24 <needmonero90>	It *is* possible to have a 1-way relay from pools into a trashtalk channel
Jan 26 19:56:28 <needmonero90>	so they can see the people who need help
Jan 26 19:56:42 <kinghat>	im only speaking for myself here but id say 99% of my experience with the xmr community has be pleasant. i cant really think of a non pleasant experience ive had. i think that says something.
Jan 26 19:56:53 <gingeropolous>	shit its 6 years ago
Jan 26 19:56:56 <rehrar>	Erciccione: We'd rather invent victims then?
Jan 26 19:56:58 <ErCiccione>	Btw therse are freenode rules, which should be enforced: https://freenode.net/policies
Jan 26 19:57:17 <M5M400>	I am aware of these rules
Jan 26 19:57:25 <asymptotically>	they are linked in the monero pools rules
Jan 26 19:57:26 <ErCiccione>	rehrar: i was talking about you proposing me to be practical and moderate the room
Jan 26 19:57:38 <Mochi101>	Again, there is a freenode IRCOP in the channel pretty much all the time.
Jan 26 19:57:56 <Mochi101>	* [Fuchs] (fuchs@freenode/staff/Fuchs): Christian
Jan 26 19:58:12 <rottensox>	why not have a #monero-ops in which all ops are present and people can join to voice their complaints about certain characters? copying and pasting the text lines that allegedly have violated freenode policies or otherwise 'civilized' behaviour?
Jan 26 19:58:37 <rottensox>	doesn't advocate for anyone to step up, just puts the ops in a single place for people to jump in and voice themselves.
Jan 26 19:58:37 <ErCiccione>	Please stop assuming that everything is fine because there is a freenode op in the channel. They don;t intervene if not for extreme cases. I said this before, the point i s to avoid to get there
Jan 26 19:58:39 <Mochi101>	I volunteer to be a mod in #monero-ops
Jan 26 19:59:21 <asymptotically>	ErCiccione: he's quite active and chats often
Jan 26 19:59:35 <gingeropolous>	then again, i was also on bitcointalk at that point in time.... so, I kinda knew that this space is just full of...... spicy ppl
Jan 26 19:59:50 <ErCiccione>	asymptotically: active as banning people or calling for moderation?
Jan 26 20:00:05 <M5M400>	no, because it's not nessecary
Jan 26 20:00:19 <M5M400>	that's Mochi101's point.
Jan 26 20:00:29 <rehrar>	I think a "tribunal" of sorts in terms of an ops channel might be beneficial.
Jan 26 20:00:36 <Mochi101>	I'm sure he won't mind... Here's an opinion on how a Freenod OP thinks the channel is doing: <Fuchs> rougher than most of our other channels, but fine :)
Jan 26 20:00:43 <ErCiccione>	anyway again: we should have the mods in the chat to moderate it, not freenode mods. Isn't it clear that if they are there is because they FEEL that chat is not moderated enough by the urrent mods?
Jan 26 20:01:36 <rehrar>	ErCiccione: the question is not whether freenode is ok with it. It never was (in this meeting). The question is whether we want to change it for the optics of Monero.
Jan 26 20:01:49 <rehrar>	And if it should change for people coming to Monero to have a good experience.
Jan 26 20:02:25 <rehrar>	Mochi101: just gave an example of how Freenode says what's going on currently dicey, but fine.
Jan 26 20:02:39 <ErCiccione>	agreed and the fact that there are freenode mods in some monero chat should warrant people of the fact that they need better moderation by the mods of that channe;
Jan 26 20:02:40 <M5M400>	sounds like what you want is a helpdesk style system with 1on1 chats with certified, friendly support agents
Jan 26 20:02:51 <Mochi101>	How much does that pay?
Jan 26 20:02:54 <gingeropolous>	yeah. thats a good restatement of things rehrar
Jan 26 20:03:00 <Mochi101>	If the price is right I'm in.
Jan 26 20:03:05 <gingeropolous>	yah know, they have open source helpdesk thingies
Jan 26 20:03:15 <M5M400>	inb4 Mochi101 checkout.php scam
Jan 26 20:03:19 <Mochi101>	lol
Jan 26 20:03:31 <Mochi101>	That was a joke, not a scam.
Jan 26 20:03:33 <gingeropolous>	u get 1 moneropoints for every guest u help
Jan 26 20:03:44 <hyc>	sorry can't stay thru the conclusion, gotta go
Jan 26 20:03:50 <M5M400>	Mochi101: so was my statement
Jan 26 20:04:29 <Mochi101>	I know that, not everybody here knows that they were both jokes though. So it's good we pointed out that they were both jokes for clarity.
Jan 26 20:04:48 <M5M400>	oh look, toxic sarcasm
Jan 26 20:04:54 <M5M400>	ok, back to topic
Jan 26 20:05:34 <gingeropolous>	well to be honest, its a joke sure, but its also not a bad idea. I mean, how great would it be to have that sort of system on getmonero.org for example?
Jan 26 20:05:42 <ErCiccione>	Anyway, this meeting has been going for one hour and feels like we are going in circle with this last point. We can close the meeting, but feel free to keep the discussion going
Jan 26 20:06:00 <needmonero90>	we need a decision on /r/moneromining, if one hasnt been made yet.
Jan 26 20:06:09 <rehrar>	It has been stated numerous times that pool has cleaned up their act somewhat. Given that, the issue is that some people went into the rougher parts of Monero town and we're appalled that it was rougher.
Jan 26 20:06:16 <rehrar>	needmoney90 switch to new sub
Jan 26 20:06:18 <ErCiccione>	needmonero: it was made, we are migrating to /r/monerominer
Jan 26 20:06:22 <rehrar>	That was the decision
Jan 26 20:06:23 <needmonero90>	alright.
Jan 26 20:06:27 <rehrar>	Were*
Jan 26 20:06:30 <needmonero90>	Just making crystal clear before the meeting ends.
Jan 26 20:06:59 <ErCiccione>	rehrar: has been brought up many times, even during this meeting, that sexist and recists terminology are still used in some monero- chats
Jan 26 20:07:16 <ErCiccione>	they happened unmoderated on pools and i brought some examples at the beginning of this meeting
Jan 26 20:07:36 <Mochi101>	Great meeting people. Sorry about the swearing that got me kicked. Can't just shut people down all the time with a quick "That's off topic" all the time though.
```

# Action History
- Created by: erciccione | 2020-01-25T10:35:53+00:00
- Closed at: 2020-01-27T16:04:18+00:00
