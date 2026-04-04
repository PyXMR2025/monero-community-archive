---
title: 'Monero Tech Meeting #112 - Monday, 2025-03-17, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1172
author: rbrunner7
assignees: []
labels: []
created_at: '2025-03-14T18:21:35+00:00'
updated_at: '2025-03-17T18:53:38+00:00'
type: issue
status: closed
closed_at: '2025-03-17T18:53:37+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1168).

# Discussion History
## rbrunner7 | 2025-03-17T18:53:37+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1172
<s​needlewoods> hello
<s​yntheticbird> HELLO
<s​yntheticbird> sorry caps
<s​pirobel:kernal.eu> hai
<j​berman> *waves*
<r​brunner7> Ok, gentle ping to jeffro256 , maybe he will be able to join
<r​brunner7> Anyway, what is there to report from last week?
<j​effro256> Howdy
<j​berman> me: implemented batch FCMP++ verification, continuing to iron out FCMP++ txs via CLI/RPC, working through failing RPC tests, and reviewing PR 9844
<jeffro256> +1
<j​berman> jeffro256: also proposed a rule change to the FCMP++ contest to allow pre-compiled tables in the contest: https://github.com/j-berman/fcmp-plus-plus-optimization-competition/pull/7
<j​berman> I support the change. I think if a table takes a long time to build, but it's reasonably sized and can be pre-built, then I think we would want contestants to explore such an optimization
<j​berman> I believe kayabanerve  would have an opinion on that change, so hoping to give a chance for discussion
<j​effro256> In this unit test (https://github.com/seraphis-migration/monero/commit/b47389aa45cc99890e33b384727264c48d4f71f8#diff-7663dc0707e146176c989ec2c5ff21f030fedb61451997e53a7de6daa8dd1227R1362), I setup two accounts, Alice and Bob, generate a FCMP curve tree with Carrot outputs to Alice, she does input selection, creates SA/L and FCMP proofs, then constructs and serializes a tx to Bob, who deserializes it and scans it. I also check v17 tx validation rules on that tx. So basically as close as an end-to-end unit test can get w/o involving live network code
<jberman> +1
<rucknium> +1
<sneedlewoods> +1
<j​berman> Oh, also, I'm now developing off @jeffro256's latest over here: https://github.com/seraphis-migration/monero/pull/18
<j​effro256> Also studying a bug with #9135 involving pruned syncing. I proposed a fix, but I want to double-check that it's secure
<r​brunner7> jeffro256: Really sounds like progress!
<r​brunner7> At first gut feeling, I don't see a problem either with that table/caches rule change. In a "yeah, why not?" kind of way.
<s​needlewoods> me: made some progress, fixed an issue I had with password wiping and elaborated and cleaned up notes I'll add when making a PR
<r​brunner7> SNeedlewoods: So it will work, that wiping, finally?
<s​needlewoods> I think so, it's just a little tedious to find the right places, e.g. when I used `wipePassword()` after a call to `storeAsync()` it actually cleared the password before the async call, so now I'm trying to make sure to use `wipePassword()` inside async calls that require a password and that no password is needed afterwards, else you'd have to type it twice
<r​brunner7> Splendid. Perseverance pays.
<s​needlewoods> I feel the compiler is not giving many errors when compiling qt, even in cases that should be obvious, so I have to do a lot more testing than usual
<r​brunner7> Is there any news about the cryptographical / theoretical problems that kaya brought up in the last meeting? It all sounded, well, mildly worrying to this noob ...
<r​brunner7> As in "do we have to change fundamental things this late in the game?"
<j​berman> seems like tree build time is likely to increase which is ok (and will need to drop the key image migration code, which is actually pretty nice imo), and in exchange we'd get a more conservative protocol
<j​effro256> A tree building slowdown of up to 2x
<r​brunner7> Because that migration won't be needed?
<j​berman> right
<r​brunner7> Would that have been a migration over all existing transactions?
<j​berman> yes
<r​brunner7> Oh ...
<r​brunner7> Interesting. News to me, but may have been clear to people with closer knowledge for a long time of course
<j​berman> Section B.g in this PR for reference: https://github.com/monero-project/monero/pull/9436
<k​ayabanerve> That change breaks embedded device support and is a lazy optimization. It shouldn't be included.
<r​brunner7> I see
<k​ayabanerve> Sorry, the optimization contest rule change.
<j​effro256> How does it break embedded device support ?
<j​berman> What size embedded device are you looking at keeping support for?
<k​ayabanerve> You have to mandate table usage per conditional to maintain support for embedded devices. This requires people do two sets of code. I'm not concerned about that, I'm just noting it isn't represented in the current rules that any tables be optional.
<k​ayabanerve> jeffro256: Having a MB table in RAM? Secure elements give you KB.
<j​effro256> Well the rules already allowed "caches" built at runtime. It doesn't matter if it's compile-time or run-time, RAM usage is RAM usage
<k​ayabanerve> Also, I'm unsure where any tables can be introduced. The divisor code is variable to the point. It can't be tabled, even if someone had a table algorithm for it, unless you make it variable time. The same holds true for the elliptic curve code unless you start pushing the definitions of variable/constant time.
<k​ayabanerve> It's feasible to create a 1MB table ahead of time. It generally isn't at runtime to be competitive.
<k​ayabanerve> So under my lack of speculation for where to include a table, that's an argument to allow this rule change as it shouldn't matter anyways.
<j​effro256> RandomX code makes a 2GB table ahead of time. 1MB can definitely be competitive depending on the application
<k​ayabanerve> I don't support it. I don't believe it benefits the code and I believe it risks support for embedded devices. It's not up to me.
<k​ayabanerve> jeffro256: Your example is literally ahead of time so it isn't really revelant.
<r​brunner7> Well, the best outcome of the contest might be that somebody "thinks outside the box" and delivers something clever and creative. Which might include tables that nobody can imagine right now?
<k​ayabanerve> It'd be the 256 MB light mode you'd want to compare to?
<k​ayabanerve> And then I'll point out such a table mandated by the hash algorithm is distinct from a table in the sense we're discussing today, where not mandated
<k​ayabanerve> rbrunner7: My concern is we get submissions not eligible on certain devices and we have to argue about whether to disqualify on that basis.
<k​ayabanerve> The rule against tables prohibits a lot of behavior which would be ineligible on those devices.
<r​brunner7> kayabanerve: Yes, I see, but on the other hand we don't rule anything about RAM usage yet, as somebody else already pointed out
<j​berman> What if we just limit the allowed pre-compiled table size to 1 KB
<k​ayabanerve> It isn't perfect, see jeffro256 identifying you can still ad-hoc table, but ad-hoc tables are only going to be of size limited by runtime which means they won't exceed the operations mandated by a single operation.
<j​effro256> I don't understand. Compile-time tables for cryptographic operations can be made ahead of time too ? For example: https://github.com/monero-project/monero/blob/f90a267fa34bad095d7e8ba72ee78f2a63f37df6/src/crypto/crypto-ops-data.c#L42
<r​brunner7> We could argue back and forth what is "a table" and what not ...
<k​ayabanerve> The point of tables is to do a larger amount of work ahead of time to minimize time during.
<k​ayabanerve> Ad-hoc tables do the exact amount of work at time to minimize time during.
<k​ayabanerve> The two just have very distinct design goals, and again, this pleasant runtime bound.
<k​ayabanerve> jberman @jberman: That is 8-10 points.
<j​berman> I guess 1 KB wouldn't be enough looking at that table
<k​ayabanerve> That is an incredibly tiny table.
<r​brunner7> Lol
<k​ayabanerve> For reference, in work I'm currently doing, I make 6 MB tables.
<k​ayabanerve> That gives me ~10x in my current work.
<k​ayabanerve> jeffro256: You cited a 2GB ahead of time table and said 1MB can be competitive.
<k​ayabanerve> I said a 2GB ahead of time table doesn't justify a 1MB ad-hoc table.
<k​ayabanerve> AoT tables != ad-hoc tables
<r​brunner7> When I brainstormed about what to do when two submissions are exactly the same speed, jberman told me that there is flexibility built into the judgement process that will be able to deal with surprises coming up. Maybe we should not worry about tables with the same line of argument?
<k​ayabanerve> That table is 256 points and has a memory footprint of 32KB btw.
<j​effro256> NGL I think trying to do FCMPs in memory-constrained hardware devices is pointless anyways. Either A) a hot wallet scans, stores enotes, and passes paths, or B) the HW device does all the functions on-board. In case A, spend privacy is already gone in the hot wallet is compromised so there's no point. In case B, you can't do it by definition since you're memory-constrained
<k​ayabanerve> I didn't say to do FCMPs on constrained devices. I said these libs should work even on constrained devices. That is my opinion.
<k​ayabanerve> To argue these libs shouldn't be usable on embedded devices is a further argument.
<k​ayabanerve> Y'all do whatever. It's your contest.
<r​brunner7> I think if we are serious about that use on constrained devices, not any table are the enemy, but high RAM use in any which way, no?
<r​brunner7> Which may be very hard to specify
<r​brunner7> Alright, as this contest discussion seems to have run its course, do we have anything else to discuss today?
<j​effro256> Tbf I didn't say it did justify a 1MB ad-hoc table, I was talking about ahead-of-time tables. The contest rules state "tables" without any additional qualifiers, so it would be worth clarifying if there's confusion.
<j​effro256> When I read the rules, I assumed *any* tables
<s​pirobel:kernal.eu> when is the rust implementation of carrot coming? :D
<r​brunner7> Yeah, when is Carrot season? Summer, right? :)
<r​brunner7> Ok, seems that I can close the meeting. Thanks everybody for attending, read you again next week!
<j​effro256> Soon ™
<j​berman> Tables may help in the context which we intend for these libs to be used, they also may not, but it seems sensible we'd want contestants to have the ability to explore optimizations that may significantly benefit the FCMP++ integration that would be easy to review
<j​berman> It would be nice to have kayabanerve  on board for this since we hope kayaba would eventually help review code merged into the lib
<s​needlewoods> thanks everyone
<j​berman> kayabanerve:  if you hold the opinion that you would not allow pre-compiled tables into the code in any way maybe with flags? (to maintain support for all embedded devices), then I think that's worth us weighing here, but otherwise seems like it's an ok rule to allow a reasonbly sized pre-compiled table
````


# Action History
- Created by: rbrunner7 | 2025-03-14T18:21:35+00:00
- Closed at: 2025-03-17T18:53:37+00:00
