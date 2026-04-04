---
title: 'Seraphis wallet workgroup meeting #15 - Monday, 2023-03-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/806
author: rbrunner7
assignees: []
labels: []
created_at: '2023-03-03T20:20:19+00:00'
updated_at: '2023-03-10T16:55:51+00:00'
type: issue
status: closed
closed_at: '2023-03-10T16:55:50+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #802

I propose to put this question on the agenda: [Dealing with two very different transaction classes](https://github.com/seraphis-migration/wallet3/issues/7)

# Discussion History
## rbrunner7 | 2023-03-06T18:42:17+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/806
<ghostway[m]> Hello
<one-horse-wagon[> Hello.
<Rucknium[m]> Hi
<UkoeHB> Hi
<SerHack> Hi
<jberman[m]> hello
<rbrunner7[m]> The subject that I proposed in the meeting meta issue for today, that transaction class story, takes a bit longer to prepare than anticipated. Let's move that one week, in any case.
<rbrunner7[m]> So what is there to report from the week that was?
<shalit[m]> Hello
<rbrunner7[m]> For people that don't watch this room constantly, here again two new issues that I wrote during the week:
<rbrunner7[m]> https://github.com/seraphis-migration/wallet3/issues/48
<rbrunner7[m]> https://github.com/seraphis-migration/wallet3/issues/49
<rbrunner7[m]> The first is an attempt at a technical compromise, a reaction that it looks we have to keep around wallet2 code for longer after all
<rbrunner7[m]> And the second a first tiny step towards the "top-level" wallet API
<rbrunner7[m]> So ... if not much else to report, anybody wanting to discuss something specific today?
<jberman[m]> Update: I realized that the multithreaded scanner I implemented using the Seraphis lib pointing to a daemon wasn't scanning coinbase outputs. I updated it and re-ran benchmarks, which were still clocking in ~5-10% faster than wallet2. I also recreated and tested scanning every tx version and was able to pick up spends and receives of all of tx types including pre-RCT
<rbrunner7[m]> Really nice. I guess the current code did not yet go through many round of optimizations, the speedup may be "just" the result of a good architecture and clean code?
<UkoeHB> it's pretty well optimized, I doubt there is much room to improve other than using non-blocking network calls
<UkoeHB> I don't think we should try to create 'one API' for Monero. We should do multiple APIs that are each compositions of shared API subsets.
<jberman[m]> the most significant structural difference is submitting per tx "scans" into the thread pool (i.e. a batch of crypto ops are done within a single task submitted to the threadpool on a per tx basis), rather than submitting more granular crypto ops into the threadpool piecemeal. there are other strucutural differences like that, but I believe that's the most significant one
<rbrunner7[m]> Ok. After you complete this, do you already know what's next? I think you mentioned once, but I don't have it ready ...
<UkoeHB> complete this referring to?
<rbrunner7[m]> To jberman , his next planned work on a part of the wallet
<jberman[m]> Reorg handling is next on my "hardening the scanner" list
<rbrunner7[m]> Ah, complete meaning these scanning tests
<jberman[m]> Last week I also mentioned looking into updating the wallet2 scanner using the above scanner because we'd have to re-use wallet2 components for tx creation anyway. I like your  proposed alternative to instead re-use wallet2 "in a box": https://github.com/seraphis-migration/wallet3/issues/48
<rbrunner7[m]> Could it be a possible thing that somebody could try on its own? Independently from other concurrent work?
<jberman[m]> I think that alternative is a smoother upgrade path. should be easier to implement, easier to review, easier to shed wallet2 when the time comes
<rbrunner7[m]> (Still looking for ways to parallelize, if need should arise)
<rbrunner7[m]> Hmmm, maybe hard until we have something to embed that in ...
<jberman[m]> preliminary thought: because we'd want to populate wallet2 containers from what's kept in the wallet3 containers, would probably make sense to tackle the wallet3 containers first. I believe dangerousfreedom[m] may have been working toward this with their "Transaction history component". There's also UkoeHB 's mock enote stores, which are labeled "mock"
<rbrunner7[m]> Right. Makes sense.
<rbrunner7[m]> I hope he can get some input for his design work on that history component. I saw that currently wallet2 probably stores less that would really be good.
<rbrunner7[m]> (Input from my issue that I linked, documenting the query methods of wallet2)
<rbrunner7[m]> For example, I think you can't easily query anymore which was the tx that spent a particular enote.
<rbrunner7[m]> If it's spent, of course
<rbrunner7[m]> About "switching the curve" we may get an update in 2 days. Funny that suddenly we had two new cryptographers showing up in the MRL IRC channel, as it looks eager to help working.
<rbrunner7[m]> Fate favors the brave, or something like that :)
<ghostway[m]> rbrunner7[m]: MRL?
<rbrunner7[m]> Monero Research Lab
<ghostway[m]> Oh ok
<rbrunner7[m]> The cryptographer density never was higher :)
<rbrunner7[m]> But that's kind of gossip. Anything else here, more technical?
<rbrunner7[m]> If not, we can call it for today.
<rbrunner7[m]> Thanks everybody for participating!
````


# Action History
- Created by: rbrunner7 | 2023-03-03T20:20:19+00:00
- Closed at: 2023-03-10T16:55:50+00:00
