---
title: Remove Travis CI build
source_url: https://github.com/monero-project/monero/issues/5828
author: hyperreality
assignees: []
labels: []
created_at: '2019-08-20T06:52:22+00:00'
updated_at: '2019-11-06T14:49:26+00:00'
type: issue
status: closed
closed_at: '2019-11-06T14:49:26+00:00'
---

# Original Description
As a new contributor to this project, I think it's bad practice that the CI builds are failing on every commit. This means that people get accustomed to false positive failing builds, and then miss genuine compilation problems. One example right now is https://github.com/monero-project/monero/pull/5827, which many of the buildbots had already flagged but got ignored.

It seems to me that the buildbot builds normally work, but Travis CI is failing every time, and has always been failing since it got added in #4420. IMO it looks like Travis is unmaintained and we should disable it until somebody puts in the effort to fix it. I am quite happy look at fixing the flaky buildbot builds, so we can get those green ticks again :)

# Discussion History
## hyperreality | 2019-08-20T06:53:36+00:00
To be clear, this issue is for getting opinions, I'm happy to submit the PR for this eventually.

## xiphon | 2019-08-20T10:24:00+00:00
>  Travis CI is failing every time, and has always been failing since it got added

That's completely incorrect. See the builds history https://travis-ci.org/monero-project/monero/builds, i.e. [PR #5583 build](https://travis-ci.org/monero-project/monero/builds/540174624), or [PR #5552 build](https://travis-ci.org/monero-project/monero/builds/544905256), and [another successful build](https://travis-ci.org/monero-project/monero/builds/545776451), and so on.

Just the Travis build is broken right now and has to be fixed. Introducing it took @TheCharlatan and others quite a good amount of work that we shouldn't drop for no reason.





## hyperreality | 2019-08-20T10:42:07+00:00
@xiphon My bad, I took a sampling of commits over the past year and the Travis build had failed on all of them, I apologize for extrapolating inaccurately from that.

I'm not suggesting that anyone's work get dropped, simply that Travis should be disabled from running automatically until it is fixed. I provided what I think is a good reason for that in the first comment, which is that code recently got merged which breaks compilations for old versions of Boost. That issue was identified by the CI build but presumably ignored because the signal to noise ratio coming from it is too low currently.

## xiphon | 2019-08-20T11:10:40+00:00
>  I took a sampling of commits over the past year and the Travis build had failed on all of them

No

<details>
  <summary>Successful Travis builds over the past year</summary>

```diff
+ #3016 v0.14.1.0 Merge pull request #5638 passed 29a505d 2 months ago
+ #3015 master Merge pull request #5641 passed 6335509 2 months ago
+ #3012 release-v0.14 Merge pull request #5638 passed 29a505d 2 months ago
+ #3002 release-v0.14 Merge pull request #5633 passed 3395de2 2 months ago
+ #3001 master Merge pull request #5632 passed 7b3df89 2 months ago
+ #2999 master Merge pull request #5552 passed a22bb54 2 months ago
+ #2929 release-v0.14 Merge pull request #5584 passed 256f8d8 3 months ago
+ #2921 master Merge pull request #5583 passed 51766d0 3 months ago
+ #2919 master Merge pull request #5571 passed 7e417dd 3 months ago
+ #2834 release-v0.14 Merge pull request #5548 passed 5fbfa8a 3 months ago
+ #2833 master Merge pull request #5548 passed 5fbfa8a 3 months ago
+ #2825 master Merge pull request #5539 passed e8487fa 3 months ago
+ #2824 master Merge pull request #5535 passed 5e80b3c 3 months ago
+ #2822 master Merge pull request #5538 passed 1607419 3 months ago
+ #2817 master Merge pull request #5512 passed 266f68b 3 months ago
+ #1553 master Merge pull request #4864 passed c93c638 8 months ago
+ #1466 master Merge pull request #4927 passed 6bc0c7e 8 months ago
+ #1453 master Merge pull request #4840 passed 5123749 8 months ago
+ #1408 master Merge pull request #4879 passed 7e957c1 9 months ago
+ #1387 master Merge pull request #4862 passed eba668c 9 months ago
+ #1329 master Merge pull request #4821 passed 58ce16d 9 months ago
+ #1242 master Merge pull request #4781 passed 84dd674 9 months ago
+ #1226 master Merge pull request #4820 passed d850e05 9 months ago
+ #1198 master Merge pull request #4236 passed 1910aab 9 months ago
+ #1183 master Merge pull request #4842 passed d0c4123 9 months ago
+ #1172 master Merge pull request #4847 passed 2312aac 9 months ago
+ #1131 master Merge pull request #4814 passed 8534f71 10 months ago
+ #1130 master Merge pull request #4818 passed 3c83e3a 10 months ago
+ #1121 master Merge pull request #4809 passed a9e03eb 10 months ago
+ #1120 master Merge pull request #4713 passed 2aabaea 10 months ago
+ #1105 master Merge pull request #4729 passed b789f7e 10 months ago
+ #1104 master Merge pull request #4728 passed 1667d41 10 months ago
+ #1095 master Merge pull request #4760 passed 4c621b1 10 months ago
+ #1092 master Merge pull request #4797 passed 6148726 10 months ago
+ #1077 master Merge pull request #4702 passed 7e2483e 10 months ago
+ #1064 master Merge pull request #4736 passed 22da14b 10 months ago
+ #918 release-v0.13 Merge pull request #4716 passed ab6c17c 10 months ago
+ #881 v0.13.0.4 Merge pull request #4705 passed 29073f6 10 months ago
+ #880 release-v0.13 Merge pull request #4705 passed 29073f6 10 months ago
+ #879 master Merge pull request #4697 passed 1e74586 10 months ago
+ #874 master Merge pull request #4640 passed af7caf7 10 months ago
+ #865 v0.13.0.4 Merge pull request #4699 passed bf38d75 10 months ago
+ #864 master Merge pull request #4699 passed bf38d75 10 months ago
+ #863 release-v0.13 Merge pull request #4698 passed d6da74a 10 months ago
+ #844 release-v0.13 Merge pull request #4670 passed 4ad6b66 10 months ago
+ #834 master Merge pull request #4524 passed 2287fb9 10 months ago
+ #765 master Merge pull request #4610 passed 5c85da5 10 months ago
+ #762 release-v0.13 Merge pull request #4603 passed 5638b07 10 months ago
+ #758 release-v0.13 Merge pull request #4622 passed ccc7e3a 10 months ago
+ #757 master Merge pull request #4621 passed e0a1d45 10 months ago
+ #746 master Merge pull request #4572 passed 636153b 10 months ago
+ #732 v0.13.0.3 Merge pull request #4598 passed e9fde8a 10 months ago
+ #731 release-v0.13 Merge pull request #4598 passed e9fde8a 10 months ago
+ #727 release-v0.13 Merge pull request #4596 passed b66c523 10 months ago
+ #703 master Merge pull request #4549 passed ae5ca0b 10 months ago
+ #630 v0.13.0.2 Merge pull request #4544 passed 77ef8c1 10 months ago
+ #628 release-v0.13 Merge pull request #4544 passed 77ef8c1 10 months ago
+ #627 master Merge pull request #4543 passed 77e1ebf 10 months ago
+ #622 release-v0.13 Merge pull request #4540 passed 1b9e686 10 months ago
+ #621 master Merge pull request #4540 passed c23b6f8 10 months ago
+ #599 master Merge pull request #4532 passed 3115511 11 months ago
+ #598 release-v0.13 Merge pull request #4530 passed 4b609de 11 months ago
+ #597 master Merge pull request #4530 passed d6dbb66 11 months ago
+ #571 master Merge pull request #4514 passed 3f2bfe8 11 months ago
+ #559 release-v0.13 Merge pull request #4036 passed 84cc3b9 11 months ago
+ #558 master Merge pull request #4036 passed e19652d 11 months ago
+ #553 master Merge pull request #4509 passed 533d31d 11 months ago
+ #551 master Merge pull request #4506 passed 9da6d29 11 months ago
+ #541 release-v0.13 Merge pull request #4472 passed b26ab0b 11 months ago
+ #538 master Merge pull request #4472 passed 79d46c4 11 months ago
+ #508 v0.13.0.2-RC2 Merge pull request #4485 passed 735a33e 11 months ago
+ #507 release-v0.13 Merge pull request #4485 passed 735a33e 11 months ago
+ #506 master Merge pull request #4485 passed 215651c 11 months ago
```
</details>

## erciccione | 2019-08-21T12:29:10+00:00
@hyperreality A PR fixing Travis would be appreciated. I disagree about the removal.

## xiphon | 2019-08-23T01:56:21+00:00
https://github.com/monero-project/monero/pull/5844

## hyperreality | 2019-08-26T23:58:48+00:00
#5858

## xiphon | 2019-09-15T11:36:33+00:00
Master is all green now. https://travis-ci.org/monero-project/monero/builds/585039052 

## t-h-e-chief | 2019-11-01T00:48:24+00:00
@hyperreality Are we good to close this ticket now?

## hyperreality | 2019-11-06T14:49:26+00:00
@t-h-e-chief Yes I will close this. The master builds are still failing but it looks like the buildbot CI is the area that needs attention now.

# Action History
- Created by: hyperreality | 2019-08-20T06:52:22+00:00
- Closed at: 2019-11-06T14:49:26+00:00
