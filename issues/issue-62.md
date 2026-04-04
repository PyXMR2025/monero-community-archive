---
title: Repo improvements
source_url: https://github.com/monero-project/monero-gui/issues/62
author: anonimal
assignees: []
labels:
- resolved
created_at: '2016-10-15T09:52:48+00:00'
updated_at: '2019-12-11T00:45:37+00:00'
type: issue
status: closed
closed_at: '2019-12-11T00:45:37+00:00'
---

# Original Description
I know we are _all_ pressed for time but I think the organization of this repo could use a little more work:
1. ~~build instructions are out of date (one apparently only needs only run `build.sh`)~~
2. we desperately need a CMake recipe (we don't need all these build scripts)
3. ~~we should consider using a git submodule for the `monero` repo~~
4. ~~these scripts shouldn't be commandeering all of my cpu cores~~ Thanks @moneromooo-monero #106 

These are just a few issues off the top of my head. I look forward to contributing to monero-core so if these issues aren't resolved by then, I'll be happy to make fixes.


# Discussion History
## moneromooo-monero | 2016-11-06T12:41:40+00:00
The most trivial of these is fixed :D https://github.com/monero-project/monero-core/pull/106


## ghost | 2017-03-29T04:01:47+00:00
@anonimal Can this issue be closed?

## anonimal | 2017-03-29T06:16:11+00:00
@xmr-eric step 2 is unresolved. I would advise to keep this issue open until that is addressed.

## sedited | 2019-09-29T18:51:41+00:00
Pull Request for cmake is open: https://github.com/monero-project/monero-gui/pull/2404

## selsta | 2019-12-11T00:40:42+00:00
#2404 is now merged.

+resolved

# Action History
- Created by: anonimal | 2016-10-15T09:52:48+00:00
- Closed at: 2019-12-11T00:45:37+00:00
