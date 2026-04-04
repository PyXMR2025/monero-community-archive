---
title: 'Dev Meeting July 19th, 17:00 UTC: Network upgrade'
source_url: https://github.com/monero-project/meta/issues/485
author: erciccione
assignees: []
labels: []
created_at: '2020-07-11T17:27:57+00:00'
updated_at: '2020-07-29T12:27:10+00:00'
type: issue
status: closed
closed_at: '2020-07-20T13:45:56+00:00'
---

# Original Description
## Location

[Freenode](https://webchat.freenode.net/) | [Mattermost](https://mattermost.getmonero.org/) | [Matrix](https://matrix.to/#/!VDQXWJoFsesLtbGdTT:matrix.org?via=matrix.org)

 #monero-dev

## Date and Time

July 19th, 2020, 17:00 UTC

Use the [timezone converter](https://www.timeanddate.com/worldclock/converter.html?iso=20200719T170000&p1=tz_gmt&p2=tz_et&p3=28&p4=111&p5=49&p6=179&p7=70&p8=224&p9=48) to see when the meeting is for you.

## Proposed Meeting Items

The main point of this meeting is to discuss the upcoming network upgrade.

1. Set date of the network upgrade and discussion about what should be included
2. Status of CLSAG and related audits
3. Preparation of a checklist and division of duties between volunteers
4. Possible and actual blockers and their status

Feel free to propose additional items and to suggest edits of the ones listed above.

# Discussion History
## SamsungGalaxyPlayer | 2020-07-13T16:55:21+00:00
Logs from #monero-dev

```
[2020-07-10 10:26:07] <sarang> Are there any other major changes planned for the next network upgrade?
[2020-07-10 10:26:19] <sarang> No CLSAG code changes are needed as a result of the security audit
[2020-07-10 10:31:50] <moneromooo> I want to change the unlock time, I've been meaning to do this for years really.
[2020-07-10 10:32:14] <moneromooo> But someone's prodded me about it not long ago, so I might get to it :)
[2020-07-10 10:32:46] <moneromooo> Can't think of anything else atm.
[2020-07-10 10:33:20] <moneromooo> (just straightening stuff, technically a consensus change, but nothing wil change in practice)
[2020-07-10 10:33:46] <moneromooo> I think I had something else I wanted for a fork but I can't find anything in my list.
[2020-07-10 10:34:19] <sarang> No CLSAG-related changes from the audit, right?
[2020-07-10 10:34:19] <moneromooo> Ah, there was the "pre-divie key image by 8" thing... :)
[2020-07-10 10:34:35] <sarang> They had only two informational suggestions that are not security-related
[2020-07-10 10:34:36] <moneromooo> Not that I know of. But you'd know better than me here.
[2020-07-10 10:34:50] <moneromooo> Right, and nothing consensus related anyway.
[2020-07-10 10:34:54] <sarang> I didn't think they were necessary, and the type change thing would likely introduce more risk
[2020-07-10 10:35:50] <sarang> I do like the key image idea, but I understand that it was contentious
[2020-07-10 10:35:51] <fluffypony> moneromooo: make it shorter or longer?
[2020-07-10 10:35:56] <fluffypony> (unlock time)
[2020-07-10 10:36:08] <moneromooo> No functional change.
[2020-07-10 10:36:17] <moneromooo> Actually.
[2020-07-10 10:36:55] <moneromooo> It's currently stored as a full 64 bit unsigned IIRC. But coinbase txes check it's exactly 60.
[2020-07-10 10:37:10] <moneromooo> Might be worth removing it for coinbase, and hardcoding 60.
[2020-07-10 10:37:14] <moneromooo> Saves... 4 bytes ?
[2020-07-10 10:37:43] <moneromooo> I was going to say delta for all, but then it depends on when it is mined, which might be unwanted,
[2020-07-10 10:37:56] <sarang> every byte counts
[2020-07-10 10:38:07] <moneromooo> Delta also prevents stupid things like an unlock time < current height.
[2020-07-10 10:38:14] <sarang> I also want a cooler name for CLSAG, but I fear that ship has long sailed
[2020-07-10 10:38:37] <moneromooo> ZLSAG.
[2020-07-10 10:38:42] <moneromooo> Everything is better with a Z.
[2020-07-10 10:38:51] <moneromooo> Almost sounds the same.
[2020-07-10 10:39:00] <sarang> %s/C/Z/g
[2020-07-10 10:39:03] <sarang> done
[2020-07-10 10:39:11] <sarang> what could do wrong
[2020-07-10 10:39:35] <moneromooo> RingZT.
[2020-07-10 10:39:40] <dsc_> Nein!
[2020-07-10 10:40:41] <Isthmus> Delta from height of the youngest ring member perhaps?
[2020-07-10 10:41:00] <moneromooo> Interesting idea.
[2020-07-10 10:46:07] <moneromooo> Ah, maybe moving tx key / nonce outside extra and kill extra, since sgp mentioned people were gonna use extra for customer data.
[2020-07-10 10:46:33] <moneromooo> I'm coming round to the idea that the pros/cons are really not that good.
[2020-07-10 10:46:57] <sgp_> I believe those plans fell through fwiw, though of course anyone can use it for any reason at any time
[2020-07-10 10:47:49] <moneromooo> Or replacing with a fixed size (non consensus enforced) encrypted chunk.
[2020-07-10 10:48:15] <moneromooo> If the fixed size is high enough, we could also calculate entropy and consensus enforce high enough :D
[2020-07-10 10:48:23] <sgp_> tradeoff between bloat and sticking out
[2020-07-10 10:48:29] <moneromooo> OK, bad idea probably.
[2020-07-10 10:49:13] <sgp_> if we want to remove tx_extra, we need to aggressively ask for comment now
[2020-07-10 10:49:31] <sgp_> we don't know if we would be breaking anything
[2020-07-10 10:50:39] <moneromooo> Should be simple enough to list all txes that have unknown extra payload. AFAIK only minergate has its own thing.
[2020-07-10 10:51:19] <moneromooo> Then we get to ponder, if there's unknown stuff, does it add or remove incentive to break it :)
[2020-07-10 10:51:46] <Isthmus> !RemindMe 1 week
[2020-07-10 10:51:54] — Isthmus heads to the data mines
[2020-07-10 10:52:59] <sgp_> I still see this as something we need to super clearly announce ahead of time since we are potentially breaking.... who knows what lol
[2020-07-10 10:53:21] <Isthmus> Yea, let's set removal for 2022 or something. Better late than never, especially where transaction linkability is involved.
[2020-07-10 10:53:45] <Isthmus> @mooo replacing with enforced fixed-size encrypted would also get an upvote from me
[2020-07-10 10:54:18] <sarang> What good real-world use cases would that have, that couldn't be addressed with encrypted pID?
[2020-07-10 10:54:29] <moneromooo> I have a patch somewhere that does mostly that, but has a quantized set of allowed sizes.
[2020-07-10 10:54:45] <sarang> downvote for quantization / optional sizes
[2020-07-10 10:54:54] <moneromooo> Coloured coins maybe. Can that be encrypted ?
[2020-07-10 10:54:58] <sarang> IMO it should be all or nothing (and I'd prefer nothing, since pID exist)
[2020-07-10 10:55:05] <moneromooo> One single size is a special case of quantized :)
[2020-07-10 10:55:10] <sarang> Oh, multiple assets for outputs? Yes
[2020-07-10 10:55:22] <sarang> There are a couple of ways to do it
[2020-07-10 10:56:10] <moneromooo> What I wanted to have is encrypted data where you can stuff json for the recipient. Then recipient/sender agree on a set of fields they want to exchnge.
[2020-07-10 10:56:34] <moneromooo> That said, it's kinda a solution is search of a problem maybe.
[2020-07-10 10:57:24] <sarang> Even if nothing else makes it besides CLSAG, that's still a huge improvement
[2020-07-10 10:57:30] <sarang> 25% smaller, 20% faster
[2020-07-10 10:57:50] <sarang> better security model
[2020-07-10 10:57:54] <sarang> audited signature code
[2020-07-10 10:58:09] <sgp_> I'm still pushing for coinbase-only sings but no one else seems interested in those
[2020-07-10 10:58:13] <sgp_> *rings
[2020-07-10 10:58:47] <sarang> I marginally like the idea
[2020-07-10 10:59:25] <moneromooo> I can't help but feel that it's what someone who wanted to deanonymize solo miners would do.
[2020-07-10 10:59:49] <sarang> sgp_: can you read through the blog post draft I posted to -community about CLSAG?
[2020-07-10 11:00:00] <sgp_> yeah one sec
[2020-07-10 11:00:22] <sarang> no rush
[2020-07-10 11:00:24] <sgp_> I know we love solo miners, but think of all the other users too...
[2020-07-10 11:00:27] <sarang> can't post it for a while anyway
[2020-07-10 11:00:53] <moneromooo> Because we don't. Obviously.
[2020-07-10 11:01:22] <sgp_> it's just one of those things where if we ask the solo miners for a small favor, then everyone else is much better off
[2020-07-10 11:03:57] <hyc> I really don't see the threat
[2020-07-10 11:05:05] <sgp_> hyc: which threat?
[2020-07-10 11:05:11] <hyc> singling out coinbase outputs into separate rings kind of destroys their anonymity set
[2020-07-10 11:05:23] <luigi1111w> I see benefit of having coinbase inputs not part of normal rings
[2020-07-10 11:05:36] <luigi1111w> but ~no benefit of having their own rings
[2020-07-10 11:05:36] <hyc> letting them be randomly selected in normal rings keeps them ... random
[2020-07-10 11:06:01] <moneromooo> OK, I said I'd trust MRL if they gave the ok to it, I'd also trust luigi1111w.
[2020-07-10 11:06:04] <sgp_> luigi1111w: how could we enforce that behavior by consensus?
[2020-07-10 11:06:29] <hyc> luigi1111: I don't understand. if they're not part of normal rings, and don't have their own rings, then how can they be spent at atll?
[2020-07-10 11:06:34] <luigi1111w> 0 rings
[2020-07-10 11:06:41] <luigi1111w> why have rings at all if they publish their txs
[2020-07-10 11:06:45] <hyc> ah
[2020-07-10 11:06:50] <sgp_> oh so you mean make coinbase spends have no decoys
[2020-07-10 11:06:54] <luigi1111w> just theater that wastes space
[2020-07-10 11:07:11] <sgp_> that's the reality really, yeah
[2020-07-10 11:07:43] <sgp_> I'm mostly in favor of keeping the ringsize 3 for coinbase, since the cost is tiny and the benefits could be larger than the tiny cost
[2020-07-10 11:08:08] <sarang> From a graph analysis perspective, any removal of coinbase from standard rings moves heuristics effectively one hop
[2020-07-10 11:08:19] <sarang> Which can be marginally beneficial
[2020-07-10 11:08:25] <sarang> Hence I marginally support the idea overall
[2020-07-10 11:08:41] <sgp_> imo those benefits are downplayed
[2020-07-10 11:09:33] <Isthmus> @sarang good point, RE encrypted memo field = ePID. Probably not necessary to have both, could just expand ePID length to desired data payload size
[2020-07-10 11:10:05] <hyc> whatever fixed size you choose will always be "not big enough"
[2020-07-10 11:10:10] <sgp_> luigi1111w: what are your thoughts about c_ringsize 3?
[2020-07-10 11:10:20] <sarang> Isthmus: I think it really comes down to whether it's optimal to have enough space for arbitrary data, or enough for a reasonable side-channel identifier (like pID is now)
[2020-07-10 11:10:32] <luigi1111w> seems pointless
[2020-07-10 11:11:54] <luigi1111w> the chances of not having "poisoned" inputs is pretty small at 3, surely
[2020-07-10 11:12:02] <luigi1111w> so the size isn't large, but the benefit is ~zero
[2020-07-10 11:12:07] — Isthmus is just making a technical note and not commenting on whether or not it's something we should do
[2020-07-10 11:13:04] <sgp_> I think the unpredictability helps reduce the effectiveness of mass surveillance, not really something to be relied upon for individual protection if that makes sense
[2020-07-10 11:13:46] <sgp_> makes things like associating outputs by timing of spends more difficult, for example
[2020-07-10 11:14:35] <sgp_> I'm not strongly in favor of this, but I think the benefits are greater than the cost
[2020-07-10 11:20:59] <UkoeHB_> Isthmus: did you ever submit a PR for fixed coin base amounts?
[2020-07-10 11:22:23] <Isthmus> Oops, forgot to put that in. Probably have time for that on Saturday.
[2020-07-10 11:22:50] <sarang> ?
[2020-07-10 12:19:02] <sgp_> this is not a consensus change, but thoughts on https://github.com/monero-project/monero/issues/5222?
[2020-07-10 12:19:24] <sgp_> I edited it to show that it applies to all public wallets, not just public mining pools
```

## erciccione | 2020-07-20T13:45:56+00:00
If somebody has the logs, please post them on monero-site

## erciccione | 2020-07-29T12:27:10+00:00
Logs: https://web.getmonero.org/2020/07/19/monero-dev-meeting.html

# Action History
- Created by: erciccione | 2020-07-11T17:27:57+00:00
- Closed at: 2020-07-20T13:45:56+00:00
