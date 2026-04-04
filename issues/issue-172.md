---
title: 'Buildbot: Win32: No space left on device'
source_url: https://github.com/monero-project/meta/issues/172
author: anonimal
assignees: []
labels: []
created_at: '2018-02-01T01:58:53+00:00'
updated_at: '2018-02-01T14:01:13+00:00'
type: issue
status: closed
closed_at: '2018-02-01T14:01:13+00:00'
---

# Original Description
`C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/bin/ld.exe: final link failed: No space left on devicemake[3]: Leaving directory '/home/buildbot/slave/kovri-all-win32/build/build'`

https://build.getmonero.org/builders/kovri-all-win32/builds/786/steps/compile%20tests/logs/stdio

# Discussion History
## danrmiller | 2018-02-01T03:12:41+00:00
OK fixed, thanks.

# Action History
- Created by: anonimal | 2018-02-01T01:58:53+00:00
- Closed at: 2018-02-01T14:01:13+00:00
