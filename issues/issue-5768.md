---
title: android build
source_url: https://github.com/monero-project/monero/issues/5768
author: Fapt4ov
assignees: []
labels: []
created_at: '2019-07-21T22:46:37+00:00'
updated_at: '2019-08-19T07:11:33+00:00'
type: issue
status: closed
closed_at: '2019-08-19T07:11:33+00:00'
---

# Original Description
hi

build for android failed on iconv

i followed the guide nothing special

docker build -f android.dockerfile -t monero .


"cconfigure: error: in `/opt/android/libiconv-1.15':
onfigure: error: in `/opt/android/libiconv-1.15':
configure: error: C compiler cannot create executables"

there is no other error mesage only

"WARNING: using cross tools not prefixed with host triplet"

i change version to 1.16 but same error.

# Discussion History
## hyperreality | 2019-08-19T01:19:18+00:00
The issue is that libiconv is trying to link against libtinfo5, which does not exist on Debian Buster by default. Since Debian stable was upgraded from Stretch->Buster a month ago, it appears that libtinfo6 is now the default installed version. However libtinfo5 is still available in the repos.

I have added it and tested that the Android build now works in the referenced commit.

## Fapt4ov | 2019-08-19T07:11:33+00:00
HELLO!

Very good.

Issue solved.

# Action History
- Created by: Fapt4ov | 2019-07-21T22:46:37+00:00
- Closed at: 2019-08-19T07:11:33+00:00
