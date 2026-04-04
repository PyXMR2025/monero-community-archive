---
title: p2p functional test failure
source_url: https://github.com/monero-project/monero/issues/9755
author: selsta
assignees: []
labels:
- tests
created_at: '2025-01-29T20:27:39+00:00'
updated_at: '2025-02-13T17:26:56+00:00'
type: issue
status: closed
closed_at: '2025-02-13T17:26:55+00:00'
---

# Original Description
https://github.com/monero-project/monero/actions/runs/12969219043/job/36173269466?pr=9723#step:11:1380

```
[TEST STARTED] p2p
Resetting blockchain
Creating wallet
Generating 80 blocks
Testing P2P reorg
Testing P2P tx propagation
Traceback (most recent call last):
  File "/home/runner/work/monero/monero/tests/functional_tests/p2p.py", line 187, in <module>
    P2PTest().run_test()
  File "/home/runner/work/monero/monero/tests/functional_tests/p2p.py", line 46, in run_test
    self.test_p2p_tx_propagation()
  File "/home/runner/work/monero/monero/tests/functional_tests/p2p.py", line 182, in test_p2p_tx_propagation
    assert len(res.tx_hashes) == 1
  File "/home/runner/work/monero/monero/utils/python-rpc/framework/rpc.py", line 50, in __getattr__
    return self[key]
KeyError: 'tx_hashes'
[TEST FAILED] p2p
```

Before we can put out v0.18.4.0 we have investigate this to make sure this is not a regression with recent merges. The test failure does not show up consistently.

# Discussion History
## selsta | 2025-01-29T20:28:29+00:00
@vtnerd could this be related to https://github.com/monero-project/monero/pull/9459?

## vtnerd | 2025-01-29T23:42:46+00:00
A quick question before I dig deeper: have you seen this on the `release-v0.18` branch or just the `master` branch? The linked CI build was for `master` so I'm testing against that for now.

## selsta | 2025-01-30T07:55:45+00:00
It did not trigger on `release-v0.18` yet. It generally only triggered once so far, seems to be a rare bug.

## vtnerd | 2025-01-31T10:57:04+00:00
I haven't gotten this to trigger locally, so I have no daemon logs to investigate. And I don't see a way to download the daemon logs from Github.

My best guess is that this is a timing bug in the test itself. The sleep timeout is 5 seconds, but the fluff (incoming) timer for transactions is typically going to be in the 3-7.25 second range. The counter argument is that it seems like the test should fail more frequently if this were the culprit.

I don't have any other theories as to the cause at the moment. #9459 definitely seems unrelated, unless there was a p2p connection loss + reconnect just before `test_p2p_tx_propagation` ran. Otherwise, if #9459 were responsible, there should've been an error earlier in the test functions.

## selsta | 2025-01-31T17:08:33+00:00
Thank you for looking into it. If we can't reproduce it locally and if doesn't show up again on CI then not sure if we can do anything else.

## iamamyth | 2025-01-31T21:04:26+00:00
I think the test can be improved quite a bit to avoid such spurious failures.

## iamamyth | 2025-02-01T05:12:56+00:00
See https://github.com/monero-project/monero/pull/9762

## iamamyth | 2025-02-10T17:54:31+00:00
I did a bit of archaeology: Roughly three weeks ago, the transfer functional_tests started failing (first PR I could find failing the test suite is https://github.com/monero-project/monero/pull/9491). Here are two sample runs with failures:
https://github.com/monero-project/monero/actions/runs/12850111386/job/35829685047
https://github.com/monero-project/monero/actions/runs/12918481913/job/36027874548 

A week after that, the tx propagation test starts failing (first two failed runs I can find):
https://github.com/monero-project/monero/actions/runs/12974105844/job/36183872821
https://github.com/monero-project/monero/actions/runs/12974245275/job/36184138495

I also note that around Jan 1, this test (unit_tests.node_server.race_condition) started to break:
https://github.com/monero-project/monero/actions/runs/12641109688/job/35228444178
https://github.com/monero-project/monero/actions/runs/12572716509/job/35045312830

@tobtoht Do you know if the transfer test failure had to do with a broken commit, which was subsequently patched, or if it was just another badly written test? Because the observation that multiple timing-sensitive tests, which previously passed, started failing around the same time, leads me to think that perhaps GitHub simply changed the runner environment (or the various build changes impacted it, or both) enough to expose the flaws in these tests, which had been relying on coincidence/timing in a specific environment.

## selsta | 2025-02-10T17:58:15+00:00
`unit_tests.node_server.race_condition` has been failing for years. `transfer` started failing due to https://github.com/monero-project/monero/pull/9389, which was fixed in https://github.com/monero-project/monero/pull/9720.

## iamamyth | 2025-02-10T19:20:45+00:00
> unit_tests.node_server.race_condition has been failing for years

I don't doubt it (added in this PR from 2021, https://github.com/monero-project/monero/pull/7873/files), but the logs on GitHub actions only go back about three months, so I can't say the p2p test (added in 2020, if I recall) has been any better or worse behaved than this unit test.

## selsta | 2025-02-10T19:23:30+00:00
`p2p` test definitely only started 3 weeks ago. I will try to see if it is easily reproducible by looping the test inside Github Action, if yes it should be possible to figure out the culprit by reverting recent merges that could be related.

## iamamyth | 2025-02-10T21:57:42+00:00
This would be a prototypical candidate for `git bisect`, but the build takes so long that it might take quite some time to find the culprit.

## iamamyth | 2025-02-11T04:13:39+00:00
Findings so far: The transaction propagation piece by itself works fine; it's the combination with `test_p2p_reorg` that causes the failure. In particular, if I just comment out the `test_p2p_reorg` call, the suite succeeds no matter how many iterations I run (tried up to 120), whereas it fails pretty quickly (happened on the first iteration) with the reorg included.

## selsta | 2025-02-11T18:16:51+00:00
@vtnerd @iamamyth I investigated the issue by running it in a loop on Github Actions. #9459 introduced it and #9762 fixes it. Now the question is why does a low level network code change cause this behaviour?

-------

Master branch, failed: https://github.com/selsta/monero/actions/runs/13269225338/job/37044415465
Master branch with #9762, success: https://github.com/selsta/monero/actions/runs/13267695803/job/37039228400
Master branch with #9459 reverted, success: https://github.com/selsta/monero/actions/runs/13266293083/job/37034497456

## iamamyth | 2025-02-11T19:45:01+00:00
Your conclusions match my own. 7e766e13c3790856fee440dcf8d47dab0bed5ea6 (aka https://github.com/monero-project/monero/pull/9459) introduced the problem. Taking into account the finding that `test_p2p_reorg` must be called in order to surface the behavior hints at a direction to explore: The reorg test generates a lot of traffic, both in the rpc and p2p, and a lot of rpc connections. The end of the test requires that both of the daemons of interest in the tx propagation test have agreed to the same top block in the chain. But, the daemons' networking state persists into the propagation test, meaning the networking limiter may impose a delay that slows tx propagation. I don't know enough about the context for the original patch to establish the exact cause, nor do I have time to spend on the question.

## selsta | 2025-02-11T19:54:30+00:00
So the plausible theory is that the incorrect throttling code caused daemon operations to slow down, which in turn meant that waiting for the maximum delay happened unintentionally. After the throttling code got fixed, there was a chance that the random delay was longer than daemon operations took, which caused the sporadic test failure. Still not sure why it happened only on CI and not locally, maybe simply because it's slower hardware.

## iamamyth | 2025-02-11T20:00:14+00:00
As for https://github.com/monero-project/monero/pull/9762, I think the patch still makes sense, but, once the cause of the slowdown has been established, I'll revisit the appropriate timeout, as a more strict value may help catch rate limiting bugs, but, if it's too strict, it becomes a source of test noise.

## iamamyth | 2025-02-11T20:09:17+00:00
I cannot narrow down the hypothesis any more than I already have, but I will just note that these tests, structurally, generate a ton of interference: For example, the end of the reorg test waits 10s in each pooling loop iteration to confirm the two daemons have synchronized. So, a slight timing change has potentially very large consequences with respect to rate limiting, because a +10s wait of course impacts the rate limiting state in the next test. And the entire "functional test" suite shares one daemon and has pathological behaviors like "connection per request" and "sleep for some preset amount and hope that's enough". In a sense, it does an OK job of surfacing bugs because it's a networking nightmare, but it gives very little direction about the nature of the bugs (e.g. test suite 2 could be failing because its predecessor did something, so good luck finding the cause).

## vtnerd | 2025-02-11T22:14:46+00:00
I agree, the code prior to #9459 unintentionally rate limited RPC. This could've caused a slight down in processing times that made the tests work. There isn't really an explanation otherwise, unless UB was triggered before and/or after the PR.

## selsta | 2025-02-13T17:26:55+00:00
Closing as the likely explanation has been found and a fix for p2p test exists.

# Action History
- Created by: selsta | 2025-01-29T20:27:39+00:00
- Closed at: 2025-02-13T17:26:55+00:00
