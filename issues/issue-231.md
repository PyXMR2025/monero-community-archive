---
title: Xcode not set up properly
source_url: https://github.com/monero-project/monero-gui/issues/231
author: rpcjacobs
assignees: []
labels: []
created_at: '2016-12-01T02:06:43+00:00'
updated_at: '2016-12-20T18:19:08+00:00'
type: issue
status: closed
closed_at: '2016-12-20T18:19:08+00:00'
---

# Original Description
Was trying to build the GUI, but kept running into;

`Project ERROR: Xcode not set up properly. You may need to confirm the license agreement by running /usr/bin/xcodebuild.`

As i thought the problem was with my xcode(-upgrade) or the suggested license issue, tried the suggested fix, to no avail. Eventually i completely removed xcode and did a full xcode re-install, without success. Finally made sure `brew` was running properly (`brew doctor`) and that the dependencies where correct, which they where, but still couldn't get passed the error.

In the end i have resolved the issue, by changing a Qt-file,

`$HOME/Qt/5.7/clang_64/mkspecs/features/mac/default_pre.prf`

replacing;
`isEmpty($$list($$system("/usr/bin/xcrun -find xcrun 2>/dev/null")))`

with;
`isEmpty($$list($$system("/usr/bin/xcrun -find xcodebuild 2>/dev/null")))`

as per; http://stackoverflow.com/a/35098040/1683164

Hopefully it can help others, with the same issue. Might also be a good addition to the install-guide.

# Discussion History
## dternyak | 2016-12-01T06:30:52+00:00
Can confirm this fix is required on macOs 10.11 and 10.12

## Jaqueeee | 2016-12-04T19:30:28+00:00
Thanks. Added this to readme in #241

## dternyak | 2016-12-05T00:33:46+00:00
@Jaqueeee You mean https://github.com/monero-project/monero-core/pull/241

## Jaqueeee | 2016-12-05T06:37:31+00:00
@dternyak Thanks. Updated. 

# Action History
- Created by: rpcjacobs | 2016-12-01T02:06:43+00:00
- Closed at: 2016-12-20T18:19:08+00:00
