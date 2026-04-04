---
title: Mattermost Migration
source_url: https://github.com/monero-project/meta/issues/81
author: serhack
assignees: []
labels:
- proposal
- in progress
created_at: '2017-06-18T19:44:40+00:00'
updated_at: '2018-03-06T13:25:19+00:00'
type: issue
status: closed
closed_at: '2018-03-06T13:25:13+00:00'
---

# Original Description
Hello,
I am a web developer and sysadmin. I'm managing about 2 servers and 3 vps for my clients. I installed some applications like gitlab and mattermost.

We are a large community and large community need a great web app in order to share every opinion, idea about monero and kovri projects.

Slack needs too much money, we are 462 users in slack; with telegram and irc gateway we can reach +1000 users.

Mattermost will be a nice alternative, I can setup it without problems. We need a vps like this https://my.hostus.us/cart.php?a=confproduct&i=0

- 6GB RAM
- 6GB vSwap
- 4 vCPU Cores (Fair Share)
- 150GB Disk Space
- 5TB Bandwidth
- 1Gbps Port (Fair Share)
- 1 x IPv4 Address
- 6 x IPv6 Addresses
- OpenVZ / Breeze Control Panel

Please share your idea, suggestions 

# Discussion History
## anonimal | 2017-06-19T17:10:06+00:00
I like the idea of mattermost but have not used it myself. @LivingInformation?

## medusadigital | 2017-07-06T21:17:17+00:00
@issue-helper label:question 

## anonimal | 2017-07-10T21:10:50+00:00
@medusadigital this is actually a proposal, not a question.

@issue-helper label:proposal

## danrmiller | 2017-07-10T21:14:53+00:00
@anonimal I'll add you to the bot ACL for the meta repo to help test the label bot. "Proposal" is not a currently supported tag either.

## danrmiller | 2017-07-22T00:06:41+00:00
-question

## erciccione | 2017-08-01T00:18:50+00:00
Totally agree with this. An open source alternative is necessary, but why not riot? Mattermost is more slack-alike but we already have a channel on matrix with an irc relay and i think we can move it on a private server. I never used Mattermost, what are the potential benefits over riot?

## psine | 2017-08-14T21:34:29+00:00
I agree that we could use a better communication platform, but how about a Discourse forum?  It is a forum, not chat / messaging, but I personally find forums more useful for most purposes.  It is open source and by far the slickest forum platform I've seen, much better than Reddit, imo.  In fact, it is the forum used by MatterMost itself:

https://forum.mattermost.org/


## danrmiller | 2017-09-20T18:01:55+00:00
+in progress

## SamsungGalaxyPlayer | 2017-09-26T03:32:53+00:00
https://taiga.getmonero.org/project/sgp-mattermost-migration/kanban

## michaesc | 2017-11-18T12:34:33+00:00
It seems that all pull requests referenced by this bug report have been merged and the main idea of Mattermost integration has been implemented.

Good work, folks. Should we close this bug report now?

## erciccione | 2017-11-18T12:51:33+00:00
@michaesc I would consider the migration complete once we completely got rid of slack in favour of MatterMost.

## rehrar | 2017-11-18T16:49:50+00:00
Unfortunately I don't foresee the Slack will ever be 100% replaced. There are people that prefer it and will not switch over. The goal is for workgroups to use MM instead of Slack, so all planning, work, and implementation can at least be somewhat private (i.e. we control the data).

With that in mind, I think it safe to say that this issue is indeed complete for the time being. 

## erciccione | 2017-11-18T17:24:29+00:00
>Unfortunately I don't foresee the Slack will ever be 100% replaced. There are people that prefer it and will not switch over

Fair enough, but we should at least discourage to use it

## rehrar | 2018-03-05T22:13:43+00:00
@serhack can we close this issue? :)

## serhack | 2018-03-06T13:25:13+00:00
Sure @rehrar ! For everyone: the mattermost instance is https://mattermost.getmonero.org 

# Action History
- Created by: serhack | 2017-06-18T19:44:40+00:00
- Closed at: 2018-03-06T13:25:13+00:00
