---
title: 'Kovri: buildbot and/or backend is not linking openssl statically for win build'
source_url: https://github.com/monero-project/meta/issues/154
author: anonimal
assignees: []
labels: []
created_at: '2017-12-24T18:08:11+00:00'
updated_at: '2018-01-24T14:50:43+00:00'
type: issue
status: closed
closed_at: '2018-01-24T14:50:43+00:00'
---

# Original Description
As detailed in https://github.com/monero-project/kovri/issues/711, we now have 3 confirmations that buildbot or something backend-related is preventing the windows static build from statically linking openssl.

# Discussion History
## anonimal | 2017-12-25T00:55:41+00:00
On successful build machine:

`/C/msys64/mingw64/lib/libssl.a /C/msys64/mingw64/lib/libcrypto.a`

On [buildbot](https://build.getmonero.org/builders/kovri-static-win64/builds/362/steps/compile/logs/stdio):

`/C/msys64/mingw64/lib/libssl.dll.a /C/msys64/mingw64/lib/libcrypto.dll.a`

@danrmiller how was openssl built on the build machine?

## danrmiller | 2018-01-24T05:12:03+00:00
/C/msys64/mingw64/lib/libssl.dll.a and /C/msys64/mingw64/lib/libcrypto.dll.a don't belong to the packages according to pacman -Qo, so I moved them away and ran a new build:

https://build.getmonero.org/builders/kovri-static-win64/builds/388


## anonimal | 2018-01-24T14:50:42+00:00
Resolved! Thank you @danrmiller

# Action History
- Created by: anonimal | 2017-12-24T18:08:11+00:00
- Closed at: 2018-01-24T14:50:43+00:00
