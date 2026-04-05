---
title: _clock_gettime not available in OSX 10.11.x
source_url: https://github.com/xmrig/xmrig/issues/172
author: atomize
assignees: []
labels: []
created_at: '2017-10-24T21:09:46+00:00'
updated_at: '2017-10-26T00:15:52+00:00'
type: issue
status: closed
closed_at: '2017-10-26T00:15:52+00:00'
---

# Original Description
Trying to run latest release xmrig-2.4.2 on OSX 10.11.6 I receive the runtime error:

dyld: Symbol not found: _clock_gettime
Expected in: /usr/lib/libSystem.B.dylib


Any fix for this?

# Discussion History
## xmrig | 2017-10-25T10:36:11+00:00
Please check version available via Homebrew http://www.brewformulas.org/Xmrig 2.4.1 at this moment.
Thank you.

## atomize | 2017-10-26T00:15:30+00:00
Works! Thx <3!

# Action History
- Created by: atomize | 2017-10-24T21:09:46+00:00
- Closed at: 2017-10-26T00:15:52+00:00
