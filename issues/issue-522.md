---
title: Move the Monero project to a self-hosted git, preferably gitea or gogs
source_url: https://github.com/monero-project/meta/issues/522
author: sanderfoobar
assignees: []
labels: []
created_at: '2020-10-26T12:56:20+00:00'
updated_at: '2021-06-30T15:51:15+00:00'
type: issue
status: closed
closed_at: '2020-10-26T17:20:20+00:00'
---

# Original Description
Some downsides of staying on Github:

- low barrier to submit issues/PRs (quality control)
- low bandwidth throughput while cloning repositories
- Tor usage discouraged
- Outages/500's
- less control over the platform/ecosystem as a whole
- rate limited APIs

Comparison with other FOSS projects:

- Tor - https://gitweb.torproject.org/tor.git & https://gitlab.torproject.org/tpo
- Whonix - https://gitlab.com/whonix/Whonix.git
- Tails - https://gitlab.tails.boum.org/

Reminder: https://torrentfreak.com/riaa-takes-down-popular-open-source-youtube-dl-software-201024/

Anyway, this topic has come up every few months for the past 2/3 years, and I've seen the following arguments pop up _against_ Gitea:

#### Gitea can't do X

Gitea/Gogs have everything imaginable for modern software development and in addition is adequately performant. It is simply high quality software™, used by many businesses all over the world. 

Gitea/gogs have less features than Gitlab. You may comment about them, but do ask yourself if they are really needed for day to day development operations within Monero. I'd say we can do without just fine, given the benefits.

### Gitea/Gogs don't have that "network effect"

Yet many FOSS projects use self-hosted Git instances and they do fine in terms of development. This in no way has an impact on meaningful development. If anything, it's a plus - because developers have more freedom in *how* they contribute.

### Gitea/Gogs is not properly maintained

This is false.

### TL;DR

Consider moving to Gitea or Gogs.

# Discussion History
## 00-matt | 2020-10-26T13:24:09+00:00
[sourcehut](https://sourcehut.org/) seems to be getting pretty good now, but sadly it's hosted in the US and there isn't much support for self hosting it.

Also Phabricator is another option for self hosting, unsure about deploying it but it's great to use. (Along with all of the other Phacility tools).

## sanderfoobar | 2020-10-26T15:28:28+00:00
I did not know sourcehut. Looks nice :+1: 

## erciccione | 2020-10-26T15:50:07+00:00
I highly suggest to everyone who wish to contribute to the discussion to read #236 first.

I have some questions about Gitea, i don't know Gogs but the questions apply to it as well.

1. Is Gitea stable and vetted enough to host a very sensitive project like Monero? How long has it been around?
2. I remember when Gitea was mentioned on IRC, somebody stated there are often breaking changes, since Gitea is still in high development. Is that still the case?
3. What features would be lost compared to GitHub? and what features would be gained?
4. Is there the possibility that self-hosting would cause the same problems with the CDN that we had with gitlab? like broken SSH support.
5. Would be possible to use tools such netlify's preview?
6. How would it work for buildbots? Would it be like Gitlab where we had to host our own runners?

## scottAnselmo | 2020-10-26T16:10:20+00:00
Would likely want to bring in @Snipa22 to the conversation. This issue has now been highlighted in -dev. If memory serves there were some quality of life / Travis CI issues that made using GitLab non-viable that would need to be looked at? On the note of Phabricator, it's worth noting that KDE is moving off of it (to GitLab). Not advocating for GitLab, just noting that one of the major FOSS projects is leaving Phabricator.

This issue is plenty relevant though given the recent removal of youtube-dl

## moneromooo-monero | 2020-10-26T16:13:24+00:00
> Is there the possibility that self-hosting would cause the same problems with the CDN that we had with gitlab? like broken SSH support.

This was not due to Gitlab, this was due to me not wanting to configure anything to do with cloudflare (since the server this ran on was using cloudflare). This would be the case with gitea also.

## sanderfoobar | 2020-10-26T17:20:20+00:00
- Flexibility/hackability
- Gitea supports CI/CD just fine
- This results in a better developer experience
- Not hosted by Microsoft

Disappointing IRC conversation in `-dev`.

## erciccione | 2020-10-26T17:22:32+00:00
The full logs of the conversation in `#monero-dev` about this issue:

```
Oct 26 16:09:04 <xmrscott[m]>	FYI since dsc is bringing it up, conversation about using something other than GitHub/GitLab: https://github.com/monero-project/meta/issues/522
Oct 26 16:09:16 <xmrscott[m]>	Snipa:  ^
Oct 26 16:10:05 <hyc>	I'm in favor of anything that isn't github...
Oct 26 16:11:11 *	peach34 has quit (Remote host closed the connection)
Oct 26 16:11:18 <xmrscott[m]>	Yes, I mean the youtube-dl scandal probably speaks a great deal to folk here
Oct 26 16:11:29 <selsta>	I'm tired of this conversation :P
Oct 26 16:11:31 *	peach30 (56126737@cpc113418-maid7-2-0-cust822.20-1.cable.virginm.net) has joined
Oct 26 16:11:57 <Snipa>	Self-hosted is great, but then you're at the mercy of the upstream provider still.
Oct 26 16:12:03 <Snipa>	Who's at the mercy of their upstream ISP.
Oct 26 16:12:06 <Snipa>	Etc.
Oct 26 16:12:10 <selsta>	We use both Github Actions / Travis CI which both don’t get supported by Gitlab / Gitea
Oct 26 16:12:10 *	pyu has quit (Remote host closed the connection)
Oct 26 16:12:28 <Snipa>	If you want to make the statement "Get out of the US", then you need to start by finding a non-US datacenter provider that matches your requirements.
Oct 26 16:12:59 <Snipa>	Tbh, it's pretty trivial to require GA/TCI into GL CI/CD.
Oct 26 16:13:23 <Snipa>	I use GL CI/CD on a daily basis for work, and it's pretty much "if you can write a shell script, you can stuff it into gitlab-ci"
Oct 26 16:13:25 <hyc>	re: CDN breaking ssh - do we actually need a CDN to frontend the repo?
Oct 26 16:13:30 <selsta>	gitlab does not support enabling CI for all users
Oct 26 16:13:37 <selsta>	we tried this already with the sites repo
Oct 26 16:13:45 <Snipa>	Sure it does?
Oct 26 16:13:52 <Snipa>	The issue is disabling it for some users.
Oct 26 16:13:52 <Snipa>	:P
Oct 26 16:14:01 <hyc>	why does ssh work with github - they use no CDN?
Oct 26 16:14:11 <Snipa>	They intercept and reroute the traffic at the CDN.
Oct 26 16:14:24 <Snipa>	Like a sensible company would do, if they talked to their CDN provider.
Oct 26 16:14:42 <Snipa>	Generally though, I just use a second SSH address, and tell gitlab to use the SSH address when displaying it.
Oct 26 16:14:48 <hyc>	which means ssh could be overloaded by high volume
Oct 26 16:15:09 <Snipa>	Usually.  Generally, you'd block SSH for anyone except who's got access to push.
Oct 26 16:15:19 <Snipa>	As you should be pulling either packages or over HTTPS.
Oct 26 16:15:26 <Snipa>	Both of which get cached at the CDN layer.
Oct 26 16:15:46 <moneromooo>	The ssh thing could have been done, but required me to configure cloudflare stuff, and I'm not touching it because they're either a TLA in disguise, or pwned by many of those. Either way, they should be dropped by anyone who cares.
Oct 26 16:16:07 <moneromooo>	ssh worked well with the actual IP. IT was just blocked by cloudflare.
Oct 26 16:17:15 <hyc>	so, do we just forego cloudflare, setup our own squid proxy or whatever if we need to put a cache in front?
Oct 26 16:17:35 *	xmrscott has quit (Quit: Leaving)
Oct 26 16:17:47 <Snipa>	Tbh, in my eyes, the argument is kind of absurd.  Moving off GH would be nice, but we've also very happily integrated into GH.
Oct 26 16:18:19 <Snipa>	If there's a serious want to move away from GH, move issues/bug reporting first, and figure out if there's going to be someone to run that infrastructure.
Oct 26 16:18:34 <Snipa>	Step 1 is to de-couple, not look for a full blown replacement.
Oct 26 16:18:53 <hyc>	good point, that can be a major pain. we migrated openldap from our old tracker to bugzilla recently
Oct 26 16:19:08 <hyc>	and exported and re-imported all of our old bug DB, so nothing was lost
Oct 26 16:19:15 <hyc>	otherwise it would have been a non-starter
Oct 26 16:19:36 <moneromooo>	IIRC github had (maybe still does for now) an exporter for non repo data.
Oct 26 16:20:07 <Snipa>	I mean to selsta's point:  We've got CI/CD to worry about, both of which are stated not to work with the fastest drop in solution (Self-hosted gitlab).  Which means that we need to be concerned with: MR's, Tickets/Bug Reports, CI/CD systems.
Oct 26 16:20:28 <moneromooo>	So someone who cares about htose should probably keep an eye on that, keep an update export for the time MS goes evil (which, historically, they will).
Oct 26 16:20:46 <Snipa>	All of which need to be de-linked from the way we work with GH if this is going to go forwards, because the other solutions are just going to end up with: Well, we've integrated with X, and now we're dependant on X.
Oct 26 16:20:55 <Snipa>	Because that's /really/ the point of this arguement I suspect.
Oct 26 16:21:14 <Snipa>	MS always goes evil.  Remember.  Embrace.  Extend.  Extinguish.
Oct 26 16:21:16 *	moneromooo gives voice to ErCiccione[irc]
Oct 26 16:21:28 <ErCiccione[irc]>	thanks moo
Oct 26 16:21:34 <ErCiccione[irc]>	We needed a paid plan to have CI working for all users on gitlab. Otherwise each user needed their own runner. And each users would have counted as member of the project, and we had to pay a plus for each member. I'm going by memory
Oct 26 16:21:40 <selsta>	We already have full regular backup of our repos
Oct 26 16:21:54 <Snipa>	Gitlab also has full licenses available for open source projects.
Oct 26 16:22:07 <Snipa>	Which I know I pointed out last time, and someone was going to look into.
Oct 26 16:22:15 <selsta>	(repos + metadata)
Oct 26 16:22:27 <Snipa>	Also, as we'd want to self-host, why the hell does it matter, as you tie your runners to your self-hosted instance.
Oct 26 16:22:29 <hyc>	Yes, openldap is on a full license, free.
Oct 26 16:22:41 <Snipa>	Because gitlab is still functionally centralized like GH if you use the cloud version.
Oct 26 16:22:44 <ErCiccione[irc]>	yeah, i remember that snipa. no idea if somebody did look into that?
Oct 26 16:22:44 <hyc>	it still requires annual renewal, but it's free.
Oct 26 16:22:48 <selsta>	Who will pay for the self hosted CI?
Oct 26 16:22:53 <selsta>	Who will set it up? I will not
Oct 26 16:23:10 <Snipa>	Tbh, someone's got to pay for all of this crap if we move off GH.
Oct 26 16:23:12 <ErCiccione[irc]>	iirc rehrar said was going to contact them at the time. Rehrar am i correct?
Oct 26 16:23:24 <Snipa>	Besides, like I said, with a self-hosted GL instance, the issue is moot.
Oct 26 16:23:38 <Snipa>	Your self-hosted runners tied to a self-hosted GL instance will work for all users properly configured.
Oct 26 16:23:54 <selsta>	I really don’t like that we tried moving to Gitlab, it was kinda meh and now we are discussing this again lol
Oct 26 16:24:10 <ErCiccione[irc]>	To be fair, the issue is not about moving to gitlab, but to gitea
Oct 26 16:24:15 <Snipa>	All answers are meh.
Oct 26 16:24:19 <moneromooo>	We still have the gitlab instance from pony. Still running.
Oct 26 16:24:21 <Snipa>	Because we're tied to github.
Oct 26 16:24:25 <moneromooo>	There's this cloudflare thing still though :P
Oct 26 16:24:32 *	kayabaNerve (~kayabaNer@unaffiliated/kayabanerve) has joined
Oct 26 16:24:32 <Snipa>	Until we de-link from github and sort through it, it's not going to be solved.
Oct 26 16:25:15 <hyc>	selsta: we can resolve this conversation now, or wait until M$ has a reason to takedown the project
Oct 26 16:25:57 <selsta>	we have https://www.backhub.co
Oct 26 16:26:26 <selsta>	in the unlikely case that monero repo gets taken down we can import it to a different place
Oct 26 16:26:28 <hyc>	accessible only to core team?
Oct 26 16:27:03 <hyc>	in the event that the repo is taken down, we will need to setup in a different place with quite some urgency
Oct 26 16:27:14 <hyc>	whereas right now we can take our time and investigate the best options
Oct 26 16:27:22 <Snipa>	Functionally, GH to self-hosted GL, without being behind CF is the /fastest/ option.
Oct 26 16:27:40 <rehrar>	nobody liked our GL though
Oct 26 16:27:48 <selsta>	pushing the repo to a different place is trivial
Oct 26 16:27:50 <rehrar>	ErCiccione[irc]: this I don't recall but it's very possible it got lost in my mix
Oct 26 16:28:01 <selsta>	the issues / pr history is a bit more work but nothing unsolvable
Oct 26 16:28:03 <Snipa>	Yes, but the infrastructure around it is not.
Oct 26 16:28:39 <Snipa>	Which is the point I've made above.  If this is a serious discussion to be had, it's time to start looking at what exists around GH that needs to be moved to a self-hosted service.
Oct 26 16:28:47 <Snipa>	And work out who the hell is going to maintain those services long-term.
Oct 26 16:29:55 <Snipa>	To your point: Travis CI is owned by a US conglomorate.
Oct 26 16:30:00 <Snipa>	So that needs to be removed as well.
Oct 26 16:30:20 <Snipa>	Purchased last year by Idera, which is a B2B parent company based out of Houston Texas.
Oct 26 16:30:29 <ErCiccione[irc]>	Any opinion about Gitea? The issue mention moving specifically to that
Oct 26 16:30:58 <Snipa>	Tbh, if we're going to make the move, my preference would be to stop using large, combined software packages.
Oct 26 16:31:04 <Snipa>	And suck it up, use multiple smaller systems.
Oct 26 16:31:45 <Snipa>	Ticketing/issue management belongs in it's own system.  CI/CD should be split apart and only depend on the ability to pull in from an upstream repo, etc.
Oct 26 16:31:50 *	rj_ (~x@modemcable218.189-57-74.mc.videotron.ca) has joined
Oct 26 16:32:05 <selsta>	Snipa: we want to run CI on every PR
Oct 26 16:32:12 <hyc>	... /me muses on using NNTP as backend for bug tracker
Oct 26 16:32:15 <Snipa>	Cool, Gitlab literlaly supports that natively.
Oct 26 16:32:28 <selsta>	Self hosted runners?
Oct 26 16:32:28 *	rj_ has quit (Client Quit)
Oct 26 16:32:30 <Snipa>	Yes.
Oct 26 16:32:46 <Snipa>	Because when you PR to the upstream, you tie the runner to the upstream.
Oct 26 16:32:53 <Snipa>	ANd it doesn't care any more that the child is pulling it in.
Oct 26 16:33:04 <ErCiccione[irc]>	i remember that being problematic at the time
Oct 26 16:33:04 <Snipa>	But you do that on self-hosted, or you don't avoid the core problems listed in the ticket.
Oct 26 16:33:14 <ErCiccione[irc]>	and was one of the main reasons for moving away
Oct 26 16:33:20 <moneromooo>	hyc: you mean, LMDB having a bug would be news ? :P
Oct 26 16:33:33 <hyc>	:P
Oct 26 16:33:33 <ErCiccione[irc]>	We tested it quite a lot, so i'm sure it was a problem at the time
Oct 26 16:33:59 <Snipa>	Naturally, and I use gitlab in that fashion on a daily basis, so I know it works fairly decently for that.
Oct 26 16:34:12 <Snipa>	But again, I'd suggest moving away from the large combined package.
Oct 26 16:35:32 <luigi1111>	losing github in the future be an inconvenience. why would we go through a similar inconvenience now for a hypothetical?
Oct 26 16:35:48 <selsta>	right
Oct 26 16:36:07 *	rj_ (~x@modemcable218.189-57-74.mc.videotron.ca) has joined
Oct 26 16:36:10 <rehrar>	to be a pure FOSS project bro
Oct 26 16:36:18 <Snipa>	Planning around it is not the /worst/ thing.
Oct 26 16:36:30 <Snipa>	Executing on it poorly is a horrid idea.
Oct 26 16:36:48 <rehrar>	and no, fireice spies, I don't mean ethnically pure. You nuts.
Oct 26 16:37:06 <Snipa>	Github certianly is a poor single point of failure, and the more that we opt to integrate with it, the more dependant we become on it.
Oct 26 16:38:13 <Snipa>	Functionally, I don't see why we wouldn't go the kernel.org route if we /really/ wanted to go down this stream.
Oct 26 16:38:54 <Snipa>	Where the master repos are behind some super light weight system, everything else is done through sensible patches and patch management structures, most likely /not/ email knowing us, but something along those lines.
Oct 26 16:39:20 <selsta>	why make everything more inconvenient now just because maybe sometime in the future github could take down monero repo?
Oct 26 16:39:35 <selsta>	and even for this case we have backhub like I said so no data is at risk
Oct 26 16:39:38 <ErCiccione[irc]>	Accessibility should be taken in consideration. A lot of our contributors barely know how to use git.
Oct 26 16:39:46 <Snipa>	Again, not saying we should, but planning should be a consideration.
Oct 26 16:39:50 <rehrar>	one of the main reasons we wanted to stay in github is the 'discovery' factor. Everyone is on there. It's THE social media for devs nowadays.
Oct 26 16:39:59 <Snipa>	Disaster planning is part of running a business for a reason.
Oct 26 16:40:03 <hyc>	ErCiccione[irc]: eh? if they don't know how to use git, they have to learn
Oct 26 16:40:30 <rehrar>	although, realistically, how many people have contributed to Monero based on this discovery factor?
Oct 26 16:40:36 <rehrar>	I don't think we have any way of knowing.
Oct 26 16:41:08 <ErCiccione[irc]>	hyc: sure, but then you have to keep in consideration the drop of contributors, especially for the website. Github's UI is very convenient from that point of view, but gitlab's is good as well
Oct 26 16:41:38 <ErCiccione[irc]>	rehrar: i got some contributors to my GUI guide repository only by participating to the hactoberfest
Oct 26 16:41:46 <ErCiccione[irc]>	talking about last year or the one before
Oct 26 16:42:09 <binaryFate>	In my view anyone can step up and plan and execute on contingency plans. Even different people could propose/architect different solutions and get the infra ready already if they want to. Especially since we're discussing threat modelling and response, decentralization is key.
Oct 26 16:42:21 <Snipa>	^ It's git.
Oct 26 16:42:37 <moneromooo>	Maybe the website would not be banned if the safety protecting software were to be taken down.
Oct 26 16:42:42 <binaryFate>	For instance, core team is managing the backhub thing and paying for with donations. But anyone could also do their backup anywhere on their own, adding to resilience.
Oct 26 16:43:07 *	peach30 has quit (Remote host closed the connection)
Oct 26 16:44:01 *	fluffypony gives voice to dethos ferretinjapan investanto kasperaitis
Oct 26 16:44:01 *	fluffypony gives voice to kayabaNerve kl_ luke-jr rj_
Oct 26 16:44:02 *	fluffypony gives voice to spoke0 TheoStorm tobtoht
Oct 26 16:44:30 <Inge->	and it might not be a bad thing if someone does so .. quietly :D
Oct 26 16:44:40 <hyc>	good point
Oct 26 16:45:07 <hyc>	but just having a backup of github repo + issue tracker is one thing
Oct 26 16:45:24 <hyc>	having an operational replacement if github shuts us down is another
Oct 26 16:45:40 <rehrar>	ultimately, I'm still for moving to something off github. Gitlab was kinda clunky. I've used Gogs before, and I know Gitea is just souped up Gogs, so I'd be down for either.
Oct 26 16:46:16 <rehrar>	but we'd need manpower and infra runners. Two things I'd not exactly say we're in excess of atm
Oct 26 16:46:28 <selsta>	gitea does not even use gitea for their repo yet
Oct 26 16:46:32 <ErCiccione[irc]>	hyc i think the only thing missing from the replacement would be the various CI. The rest would be ready to work (talking about the existing self hosted gitlab)
Oct 26 16:47:15 <selsta>	and setting up CI replacement is not crucial fo operations
Oct 26 16:47:20 <selsta>	for
Oct 26 16:49:44 <rehrar>	I know it sucks to have conversations like this over and over, but the world seems to be becoming increasingly hostile towards 'wrong-think'
Oct 26 16:50:07 <rehrar>	and I think it is prudent to come back to conversations like these as this gets worse
Oct 26 16:50:10 <rehrar>	which I suspect it will
Oct 26 16:50:36 <fluffypony>	well the thing is that we already have DR ready
Oct 26 16:50:45 <binaryFate>	IMO it's good to prepare alternatives, but I don't see why move away already. Agree with luigi1111 it's just inflicting inconvenience to ourselves. It's a way for the project to self-censor itself out of vague fear before someone needs to actively censor.
Oct 26 16:50:47 <rehrar>	if moving away is a pro-con analysis, and even if right now the cons outweigh the pros and so we don't move, the pros of moving may one day outweigh the cons, even just as the balance is tipped further and further by hostile takedowns
Oct 26 16:51:07 <selsta>	rehrar: we have plans in case github takes us down
Oct 26 16:51:43 <rehrar>	yes, but the github getting taken down is only one of the pros of moving. dsc outlined others, such as Tor contribution
Oct 26 16:51:44 <fluffypony>	I don't think we need to move, we tried that already and it didn't work - if we're FORCED to move that's different and we have multiple contingencies in place
Oct 26 16:52:17 <fluffypony>	rehrar: yes but the handful of additional pros don't outweigh the cons
Oct 26 16:52:26 <fluffypony>	ErCiccione has a whole write-up on the issues
Oct 26 16:52:35 <moneromooo>	Right. The moon base is almost in place.
Oct 26 16:52:36 <rehrar>	at present, I think I agree
Oct 26 16:52:44 <fluffypony>	and it wasn't JUST because of GitLab, it was other things
Oct 26 16:52:50 <ErCiccione[irc]>	rehrar: Github works with Tor afaik. not reliably, but it works
Oct 26 16:53:34 <asymptotically>	yes github works fine thru tor, both the webui and git+ssh push/pull
Oct 26 16:55:40 <hyc>	if you guys are satisfied that no changes need to be made at this time, fine with me
Oct 26 16:56:19 <hyc>	summarize these points in the issue and close it...
```

## fluffypony | 2020-10-27T06:01:36+00:00
@xmrdsc FWIW I was the one that pushed for self-hosted GitLab after the MS buy-out. I really, really tried to make it work, but in practice this is harder than expected.

## sanderfoobar | 2020-10-28T19:58:03+00:00
From experience I know gitea/gogs is easy to host and maintain. That said, I understand if for now the most pragmatic thing would be to stay on Github, as a switch has implications on core team resources, CI/CD. After this issue, gitea will at least be on people's radar so perhaps in the future gitea will be a consideration when there's a push towards an alternative git platform. Best I can do :- )

## selsta | 2020-10-29T03:00:49+00:00
Having tried both Gitlab and gitea, gitea definitely has the nicer interface and feels less bloated. If we at some point for whatever reason switch away from Github I would prefer it over Gitlab. Also it is fully FOSS compared to Gitlab being open core.

# Action History
- Created by: sanderfoobar | 2020-10-26T12:56:20+00:00
- Closed at: 2020-10-26T17:20:20+00:00
