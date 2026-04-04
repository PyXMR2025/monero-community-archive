---
title: 'Problem with brew install on OSX: No such file or directory - ./build/release/src/bitmonerod'
source_url: https://github.com/monero-project/monero/issues/190
author: hems
assignees: []
labels: []
created_at: '2014-11-28T02:10:51+00:00'
updated_at: '2014-11-28T16:22:33+00:00'
type: issue
status: closed
closed_at: '2014-11-28T15:10:21+00:00'
---

# Original Description
After executing:
`brew install --HEAD bitmonero`

i  end up with that error:
`No such file or directory - ./build/release/src/bitmonerod`


# Discussion History
## sammy007 | 2014-11-28T04:28:09+00:00
Please report brew issues to https://github.com/sammy007/homebrew-cryptonight. Run with flag -v and open issue there with log. Also include your OS X version.


## sammy007 | 2014-11-28T06:12:30+00:00
Seems trunk has issues on OS X. Use: <code>brew install bitmonero --build-from-source</code> to install 0.8.8.4 version (last tagged version). You can bypass <code>--build-from-source</code> option in order to install precompiled (by me) binaries (Mavericks, Yosemite).


## sammy007 | 2014-11-28T15:05:36+00:00
I pushed <code>--HEAD</code> installation fix to my repo. Please close.


## fluffypony | 2014-11-28T15:10:21+00:00
Closed per @sammy007's fix


## hems | 2014-11-28T16:22:33+00:00
@sammy007 for the info, i'll communicate through you repo for now.


# Action History
- Created by: hems | 2014-11-28T02:10:51+00:00
- Closed at: 2014-11-28T15:10:21+00:00
