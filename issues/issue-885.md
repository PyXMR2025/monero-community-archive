---
title: 'Seraphis wallet workgroup meeting #34 - Monday, 2023-08-28, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/885
author: rbrunner7
assignees: []
labels: []
created_at: '2023-08-26T05:18:59+00:00'
updated_at: '2023-08-28T18:32:45+00:00'
type: issue
status: closed
closed_at: '2023-08-28T18:32:45+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/881

# Discussion History
## rbrunner7 | 2023-08-28T18:32:45+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/885
<d​angerousfreedom> Hello
<Rucknium> waves
<v​alldrac> Hi
<j​berman> hello
<r​brunner7> So, what is there to report from last week?
<d​angerousfreedom> From my side, I finished the legacy_proofs in the way I think that makes more sense (injecting node connection and wallet_keys/cache data) and wrote [this](https://github.com/seraphis-migration/wallet3/issues/55) comment.
<d​angerousfreedom> I have a question regarding that. How do I replace a node connection for unit_tests in legacy? I want to test my legacy_knowledge_proofs [here](https://github.com/DangerousFreedom1984/seraphis_lib/blob/legacy_proofs_with_jeffro_api/tests/unit_tests/sp_wallet_legacy_proofs.cpp) (they are working) but the tests will fail if the node is not on (which is expected in the real world of <clipped 
<d​angerousfreedom> course). Is there any solution? Maybe not let it at the unit_tests folder but somewhere else where a node is required? Maybe remove the node part of it for testing (if possible)? Maybe not test the whole proof like it is done today?
<v​alldrac> Nothing from my side. Just busy with the Android SDK, having fun with wallet2 and transaction history
<r​brunner7> Not sure, but isn't Python code used if it's question to start a daemon and such? Some code from jberman to test background sync does that.
<r​brunner7> Or you inject a "pseudo daemon" in the first place ...
<g​hostway> Hello
<g​hostway> For some reason I've been hogging the key container thing for a while, probably I should just pr
<g​hostway> I'll send jeffro256 my implementation of the migration thingy detailed on jamtis' page
<r​brunner7> For some reason? :) Maybe just PR what you have, yes.
<d​angerousfreedom> I will look to that. Thanks
<d​angerousfreedom> Is there something like a pseudo daemon for legacy? Like there is in seraphis?
<r​brunner7> Not sure, but I never stumbled over one.
<r​brunner7> Maybe would be useful anyway?
<d​angerousfreedom> Ok. I will try to find alternatives to test the whole proofs.
<j​berman> the legacy python functional_tests start up regtest daemons from python code and use those in all the tests (`functional_tests_rpc.py`)
<d​angerousfreedom> Oh, okay, I was wondering that. So can I add transactions to a regtest daemon?
<d​angerousfreedom> I will try...
<j​berman> I think we're pretty far away from getting to that point with the seraphis code. the regtest daemon is basically a fully functioning daemon that adds txs to the db and has consensus with other regtest daemons
<d​angerousfreedom> Yeah sure, I mentioned a mock version.
<j​berman> the core_tests are probably closer, they let you construct txs and manual blocks all in c++, but they're also testing consensus
<d​angerousfreedom> Good to know, thanks. I will just adapt the proofs I created on stagenet to regtest
<r​brunner7> It seems the discussion about jeffro256 's proposed Jamtis view tag refinements is still ongoing. Probably nothing to discuss right today, much less with jeffro256 not here right now. Maybe in Wednesday's MRL meeting.
<r​brunner7> Anything else to discuss?
<g​hostway> Btw I've contacted koe about the task of optimizing the enote store, if that matters
<d​angerousfreedom> For next meeting or before I want to have a demonstrator of how looking at enotes could look like. I will demonstrate the path 'show my enotes' -> make a transaction -> 'show my enotes' -> make a knowledge_proof proving that I sent my legacy enotes to a seraphis address.
<d​angerousfreedom> What needs to be done?
<g​hostway> That sounds really cool, I tried doing that some time back but got bored....
<g​hostway> I don't know, on the task he said you (I in that case) should contact him
<r​brunner7> dangerousfreedom: I don't fully understand what you mean, but will gladly look at any demonstrator :)
<g​hostway> He's doing what you suggested I beleieve
<j​berman> dangerousfreedom: idea: instead of `get_spend_proof_legacy` taking in an http client as a param, it could take in a lambda that makes a request for the tx from the daemon, and then you can inject a mock request and response into that and have full control over it in your tests, rather than get a daemon involved
<d​angerousfreedom> Haha okay. Discussion for next week :p
<j​berman> Sort of similar to how I pass in a lambda here and abstract away the http client/daemon connection from the scanner: https://github.com/j-berman/monero/blob/0562fa8590389472539a5fb20054d70fe5c33565/src/blockchain_utilities/blockchain_scanner.cpp#L215-L241
<r​brunner7> Just a crazy idea: Did anybody already try something like "pair programming" when producing Monero code, in this particular case jberman and dangerousfreedom building tests for those proofs together?
<r​brunner7> Never did it myself
<r​brunner7> I mean pair programming in general, just heard about it
<d​angerousfreedom> I'm not sure if I fully understood. I want to have final functions in my cpp file and use a unit_test to just test these functions. I dont know how it would be different from the problem that I need to contact a node. I will see more carefully later. Thank you
<d​angerousfreedom> I will contact you later if I get into trouble (I guess this is pair programming ? :p)
<r​brunner7> Alright, seems the meeting has taken its course. Thanks for attending everybody, read you again in 1 week at the latest.
````

# Action History
- Created by: rbrunner7 | 2023-08-26T05:18:59+00:00
- Closed at: 2023-08-28T18:32:45+00:00
