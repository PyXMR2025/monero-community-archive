---
title: 'Seraphis wallet workgroup meeting #21 - Monday, 2023-04-17, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/826
author: rbrunner7
assignees: []
labels: []
created_at: '2023-04-14T14:53:05+00:00'
updated_at: '2023-04-17T18:34:13+00:00'
type: issue
status: closed
closed_at: '2023-04-17T18:34:12+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #823 

I won't be around to run meetings for 3 weeks after this one. We can decide in the meeting whether there will be a pause, with the next meeting on May 15, or whether somebody else will run meetings during this time.

# Discussion History
## rbrunner7 | 2023-04-17T18:34:12+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/826
<ghostway[m]> Hello 
<jberman[m]> hello
<xmrack[m]> Hi
<rbrunner7[m]> Are we still in the long shadow of the Easter weekend? :)
<rbrunner7[m]> Matrix quite a bit slower than IRC today it seems, at least at my end ...
<jberman[m]> I'm on matrix and I see ghostway and xmrack  here
<rbrunner7[m]> Yup, about 1 minute later for me here on Matrix than on IRC. Well, well.
<rbrunner7[m]> Alright, let's start.
<rbrunner7[m]> First something about our formal meetings like this one: I will be away and won't be able to run meetings on April 24, May 1 and May 8. I will be back for a meeting on May 15.
<rbrunner7[m]> Seems to me that with development picking up speed only gradually a break in meetings won't hurt too much; people can always coordinate ad hoc. But if somebody volunteers to run these meetings, why not? :)
<rbrunner7[m]> Anything to report regarding progress?
<jberman[m]> Short version progress update: I got UkoeHB 's optimized scanner working in crude fashion, but noticed some unexpected bottlenecks that I'm still working through. I'm hoping to hammer it down and submit a PR within the next days but it may take a bit longer to iron it out fully
<rbrunner7[m]> Interesting
<ghostway[m]> Not exactly. Id like to talk with dangerousfreedom which is absent currently
<rbrunner7[m]> Right. Maybe 2 weeks more or so.
<rbrunner7[m]> Anything to discuss today in this wider round?
<ofrnxmr[m]> dangerousfreedom[m]:  has moved to funding https://ccs.getmonero.org/proposals/df-wallet-development-2.html
<rbrunner7[m]> Oh, good, thanks for the news.
<jberman[m]> (writing up a long-form update that I think will be interesting, 1 sec sorry)
<ofrnxmr[m]>  UkoeHB:  has as well https://ccs.getmonero.org/proposals/seraphis-ongoing-support.html
<rbrunner7[m]> Even better :)
<rbrunner7[m]> By the way, if something bad should happen to this room while I am away, beside me sgp_ (New Account: @sgp:magicgrants.org) is the second admin
<rbrunner7[m]> or maybe sgp_ (New Account: @sgp:magicgrants.org) not sure which one
<rbrunner7[m]> Same person of course
<ofrnxmr[m]> sgp:  this one should be active but all 3
<ofrnxmr[m]> Matrix, monero.social (which were needed for bridges) and magicgrants (current)
<jberman[m]> Long version update on my end: UkoeHB designed an optimized scanner here: https://gist.github.com/UkoeHB/4b3528a5c3a3134bd82d19a2bc6a8e87
<jberman[m]> I've taken that as a base and am working on pointing it to an actual daemon and observing the speed-up
<jberman[m]> The crux of the design is that the client queues 10 requests to scan chunks of the chain in parallel (e.g. blocks 2m - 2.01m, 2.01m - 2.02m, etc.), and is therefore continuously working while many network requests are pending
<jberman[m]> This is in contrast to wallet2 today (and in contrast to how I wrote this code: https://github.com/j-berman/monero-cpp/blob/c2c55f4386f33d7617c49c25d88183fc4f8b5d43/src/utils/monero_utils.cpp#L1215-L1316), where the client submits the "next" request for a chunk in parallel while it scans the "current" chunk
<jberman[m]> In theory, queuing network requests should smooth out latency bottlenecks, and should end up faster than needing to wait for 1 network request at a time which can randomly turn out pretty slow
<jberman[m]> I would think this approach is the optimal design for scanning over tor/i2p where packets take multiple hops through those networks, for example
<jberman[m]> With my current code now able to scan the chain from beginning to tip using koe's scanner, I noticed the queuing approach wasn't much faster, but I believe this is because of issues in my code that I'm still working through
<rbrunner7[m]> Hopefully the speedup is worth the larger complexity of the code. But sounds interesting.
<rbrunner7[m]> Is is in any way prepared for scanning on behalf of several open wallets at once?
<rbrunner7[m]> Or, better said, in parallel
<jberman[m]> it's written in better plug-and-play fashion, so I'd say there is an easier path to implement scanning multiple wallets at once than with wallet2 code, but no it's not written to scan multiple wallets at once
<Rucknium[m]> I have unintentionally stress tested monerod for data gathering. It can handle at least 32 RPC requests in its "queue".
<rbrunner7[m]> Ok, I think a reasonable way to implement this later, thanks to better modularization, is perfectly ok for the time being.
<ghostway[m]> I'd like to understand what you mean by modularization, just the general term. what do you mean by that exactly? 
<Rucknium[m]> When I try something like that with bitcoind and its code forks, I sometimes receive malformed data.
<rbrunner7[m]> 32 may still not be that much for a busy daemon used by many wallets as their remote daemon, but that's probably not yet the end of the line I would guess
<rbrunner7[m]> Not much specific. If we have separate, well defined classes instead of one big monolith that wallet2 is, things will be much better and much more flexible.
<rbrunner7[m]> And of course classes that do not depend on each other too much in hard-to-see and hard-to-understand ways.
<ghostway[m]> so the best course of action is to just to implement the classes bottom-up?
<ghostway[m]> this is very slow, lol
<rbrunner7[m]> Well, that's still my opinion so far, yes.
<rbrunner7[m]> Guessing some high-level structure that later may not hold and has to be modified again and again can be slow as well, so ...
<rbrunner7[m]> I think up to a point it's a question of personal preference of a dev, I for one like working bottom up. Especially for brand new things.
<ghostway[m]> makes sense
<rbrunner7[m]> Ok, if that's about it for today, thanks for attending, and read you again at May 15 at the latest.
<rbrunner7[m]> Don't finish the darn thing without me :)
````


# Action History
- Created by: rbrunner7 | 2023-04-14T14:53:05+00:00
- Closed at: 2023-04-17T18:34:12+00:00
