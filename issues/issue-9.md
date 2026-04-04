---
title: Onion/Garlic sites for hosted services and build/testing machines
source_url: https://github.com/monero-project/meta/issues/9
author: anonimal
assignees: []
labels: []
created_at: '2016-11-12T06:38:12+00:00'
updated_at: '2023-12-18T15:59:23+00:00'
type: issue
status: closed
closed_at: '2023-12-18T15:59:23+00:00'
---

# Original Description
I believe that @fluffypony mentioned at some point *something* along these lines - but I'd like to see for certain where we stand and what the plan was exactly (I do like the idea very much :+1:).

Referencing https://github.com/monero-project/kovri/issues/46 and https://github.com/monero-project/kovri/issues/90.

# Discussion History
## danrmiller | 2016-11-13T02:40:27+00:00
We have i2p and tor services pointed to the buildbot web interface and the gitlab mirror, but I was holding off adding the rewrite rules to the web server until we get everything on a new box. But I can go ahead and do that and we'll just move everything later.

But this is the first I heard about i2p/tor access to the build and test machines, but I don't see why we can't set that up for the contributors who already access these machines.


## anonimal | 2016-11-13T04:58:38+00:00
Re: build machines, an onion service would greatly reduce the knowledge-set of exits; which I think would be a good thing. Unless anyone else plans to use an I2P tunnel, I will personally stick to an onion service because speed and flexibility is more of a priority than security for me (in terms of keeping up with the builds and run-time testing) but I support any decision that's made.


## anonimal | 2016-12-02T22:46:29+00:00
All build machines (except windows) are now accessible via onion service. Thank you @danrmiller !!! 🎉 👍 😂

Note: buildbot login now has fixed rewrite rules so i2p login is possible. Another thanks to @danrmiller.

## danrmiller | 2016-12-05T03:35:05+00:00
I've got the windows machines and arm testing machines ready for you

## anonimal | 2016-12-06T03:38:14+00:00
Windows and ARM onions are working 😂 This resolves the build/test portion. @danrmiller  is this issue resolved?

## danrmiller | 2016-12-06T03:44:49+00:00
Yes, resolved.

## anonimal | 2016-12-11T21:16:49+00:00
I'm reopening until monero-project/kovri#46 and monero-project/kovri#90 are *both* resolved. monero-project/kovri#46 may take a long while to resolve though, just FYI.

## anonimal | 2016-12-11T21:18:14+00:00
@danrmiller I'll rename the issue once it's down to resolving monero-project/kovri#46 and the Monero website.

## anonimal | 2016-12-12T14:27:33+00:00
@danrmiller http://monero-repo.i2p redirects to https://monero-repo.i2p/users/sign_in (failed browser expectations ensue).

## danrmiller | 2016-12-13T16:58:19+00:00
Sign-ins won't be enabled on this read-only mirror, if you want to browse use 
http://monero-repo.i2p/monero-project

I'll fix it so via i2p http://monero-repo.i2p/ goes to http://monero-repo.i2p/monero-project/ or something and let you know, but can't look at it today.

## anonimal | 2016-12-13T17:27:45+00:00
Ok, thanks. I didn't think to login, I was mostly complaining about the https redirect but this can work too.

I'm trying to git over http but the site appears offline. Can you please give me a ping when it's back online?

## danrmiller | 2016-12-13T20:30:53+00:00
OK I restarted i2p and it seems back. This was the error:
CRIT  [uterWatchdog] 2p.router.tasks.RouterWatchdog: Router appears hung, or there is severe network congestion.  Watchdog starts barking!

One day we'll use kovri.

## anonimal | 2016-12-13T23:19:49+00:00
That java I2P error is not uncommon and is usually just a temporary issue. We actually *can* use kovri now but I won't push to use it.

I'm now getting `500` and `504` responses when trying to git over http. The site looks offline again after the first `500`.

## danrmiller | 2017-02-02T03:54:34+00:00
I left you some messages on IRC. The i2p link is slow; something times out along the way, I've tried adjusting load balancer http buffer sizes and various other things time out. Maybe we'll change the tunnel and use ssh for git instead, and I'll try a few other things.

## danrmiller | 2023-12-18T15:56:17+00:00
We no longer use this buildot system for years, this can be closed 

# Action History
- Created by: anonimal | 2016-11-12T06:38:12+00:00
- Closed at: 2023-12-18T15:59:23+00:00
