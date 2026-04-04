---
title: 'OpenSuSE 42.2: crash when using bundled libs, works fine with system libs'
source_url: https://github.com/monero-project/monero-gui/issues/333
author: villabacho
assignees: []
labels: []
created_at: '2016-12-22T16:59:49+00:00'
updated_at: '2017-04-01T20:43:16+00:00'
type: issue
status: closed
closed_at: '2017-04-01T20:43:16+00:00'
---

# Original Description
The Monero Core GUI Beta 1 crashed on my OpenSuSE 42.2 system when using the bundled libraries. When using system libraries instead, except for libicudata.so.55, libicui18n.so.55, and libicuuc.so.55 (which I didn't get from the OpenSuSE default repositories), it works fine.

# Discussion History
## villabacho | 2016-12-22T17:13:08+00:00
I should add that the crash with the bundled libs already happens during startup. Even gdb crashed when having the bundled libs in my LD_LIBRARY_PATH, so I guess it happens already when loading/initializing one of the libraries.

## peronero | 2016-12-22T19:59:33+00:00
Issue exists on Tumbleweed as well.

## ghost | 2017-03-29T03:48:37+00:00
@villabacho Can this issue be closed?

## peronero | 2017-03-29T15:53:14+00:00
Was resolved on Tumbleweed.

## villabacho | 2017-04-01T20:41:42+00:00
@xmr-eric yes, that happened wit beta 1. beta 2 runs fine for me.

# Action History
- Created by: villabacho | 2016-12-22T16:59:49+00:00
- Closed at: 2017-04-01T20:43:16+00:00
