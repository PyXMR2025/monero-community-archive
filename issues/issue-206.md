---
title: Mac OSX error
source_url: https://github.com/xmrig/xmrig/issues/206
author: d3gan
assignees: []
labels: []
created_at: '2017-11-18T08:02:03+00:00'
updated_at: '2017-11-27T00:08:32+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:08:32+00:00'
---

# Original Description
Mac OSX error
Mac OSX 10.11.6

dyld: lazy symbol binding failed: Symbol not found: _clock_gettime
  Referenced from: /Users/asd/Downloads/xmrig-2.4.2 2/xmrig (which was built for Mac OS X 10.12)
  Expected in: /usr/lib/libSystem.B.dylib

dyld: Symbol not found: _clock_gettime
  Referenced from: /Users/asd/Downloads/xmrig-2.4.2 2/xmrig (which was built for Mac OS X 10.12)
  Expected in: /usr/lib/libSystem.B.dylib

# Discussion History
## xmrig | 2017-11-18T11:17:16+00:00
For macOS please use [Homebrew](http://www.brewformulas.org/Xmrig) to install.
Thank you.

## d3gan | 2017-11-18T12:29:24+00:00
thank you.

# Action History
- Created by: d3gan | 2017-11-18T08:02:03+00:00
- Closed at: 2017-11-27T00:08:32+00:00
