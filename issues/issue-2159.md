---
title: monero-wallet-gui.app/Contents/MacOS/monerod (which was built for Mac OS X
  10.12) crash
source_url: https://github.com/monero-project/monero-gui/issues/2159
author: Afron-Lysias
assignees: []
labels:
- resolved
created_at: '2019-05-04T00:19:13+00:00'
updated_at: '2019-05-05T06:54:36+00:00'
type: issue
status: closed
closed_at: '2019-05-05T06:54:36+00:00'
---

# Original Description
`Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BREAKPOINT (SIGTRAP)
Exception Codes:       0x0000000000000002, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Application Specific Information:
crashed on child side of fork pre-exec

Dyld Error Message:
  Symbol not found: _clock_gettime
  Referenced from: /Users/USER/*/monero-wallet-gui.app/Contents/MacOS/monerod (which was built for Mac OS X 10.12)
  Expected in: /usr/lib/libSystem.B.dylib
`

# Discussion History
## sanderfoobar | 2019-05-04T00:36:48+00:00
10.12 builds are not backward compatible (`clock_gettime()` was added in 10.12 - someone correct me if I'm wrong). El Capitan is EOL since August 2018.

Whether or not we're going to support 10.11 ill leave to the build team. Qt 5.9 is capable of it, I know that much.

## selsta | 2019-05-05T01:12:58+00:00
+resolved with using a macOS 10.11 build.

## dEBRUYNE-1 | 2019-05-05T06:51:06+00:00
+resolved

# Action History
- Created by: Afron-Lysias | 2019-05-04T00:19:13+00:00
- Closed at: 2019-05-05T06:54:36+00:00
