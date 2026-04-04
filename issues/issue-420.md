---
title: Deprecate BuildBot?
source_url: https://github.com/monero-project/meta/issues/420
author: fluffypony
assignees: []
labels: []
created_at: '2019-12-18T13:30:11+00:00'
updated_at: '2020-03-09T21:42:53+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:42:53+00:00'
---

# Original Description
We've used BuildBot for a long time, but the Mac and ARM servers + VM boxes are expensive. There are also environmental issues which cause builds to fail (despite the PR being fine) often enough that people have started ignoring BuildBot results.

With Gitian being stable for the CLI, and getting close to completion on the GUI, pigeons and I would like to start taking the BuildBots down and deprecating them, starting with the CLI ones. This meta issue exists to take input from everyone as to whether this is a good idea or not.

# Discussion History
## moneromooo-monero | 2019-12-18T13:33:45+00:00
I wanted buildbots years ago. In practice, I tuned them out because they just pinged you for (most of the time) irrelevant stuff. So great in theory, but not in practice unfortunately. So no objection here.

## erciccione | 2019-12-18T14:52:16+00:00
I totally agree. Also, we have other tools we can use, like GitHub actions and Gitlab CI structure. Both can be contributed to by the community (Which is not the case for the buildbots).

## vtnerd | 2019-12-18T15:13:17+00:00
One giant benefit of continually building is getting quicker feedback if a platform is failing. It could be a rush during release time if a replacement process isn't in place.

Boost (used to?) has a test matrix where volunteers from the community setup a unique environment to compile + run tests and report back to a web interface. The testing is only done against commits and not against each PR - which reduces load considerably. Our commits are "batched" too, so they only need to run once a week (or less) after a group of commits. I should be able to obtain the code (probably Python) for both the server and the builds that ran this matrix. It generated static html files IIRC.

If Gitian is doing cross-compiles, then these systems don't have to be lock-down secure for release building, they only need to sanity checking periodically (with a rush during the lead-up to release).

## fluffypony | 2019-12-18T15:39:09+00:00
@vtnerd to be clear, I'm not saying we mustn't have CI, I'm saying that it can use cross-compilation via Jenkins or whatever rather than native builds via BuildBot.

## vtnerd | 2019-12-18T15:49:24+00:00
The cross-compile will do most of what we need. It will be difficult (impossible?) to get those CI systems to run arm64 unit tests + core tests for instance. That's where the test matrix would fill the gap. Its pretty rare to find a bug specific to one platform at least. 

## hyc | 2019-12-18T16:29:51+00:00
Could run arm64 tests via qemu if necessary. Emulation is slow but might be good enough for periodic test purposes.

## xiphon | 2019-12-18T17:04:07+00:00
Just `osx-10.11` buildslave is needed for Monero GUI releases, we don't have any other environment to build the GUI for MacOS at the moment.

## Snipa22 | 2019-12-19T04:31:52+00:00
Gitlab-CI's structure is quite nice for most things, I've used it extensively in professional and personal structures.  If it's just a function of cost for some of the more obscure servers, I'm more than happy to help shoulder the load for these going forwards, as long as they're somewhat within reason.

## selsta | 2019-12-30T18:18:08+00:00
For the CLI repository: https://github.com/monero-project/monero/pull/6270

## selsta | 2020-03-09T21:42:53+00:00
Buildbot has been taken offline. @danrmiller please keep the osx-10.12 VM alive for macOS GUI builds.

# Action History
- Created by: fluffypony | 2019-12-18T13:30:11+00:00
- Closed at: 2020-03-09T21:42:53+00:00
