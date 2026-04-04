---
title: unbound, osx, ranlib warning
source_url: https://github.com/monero-project/monero/issues/2308
author: jtgrassie
assignees: []
labels:
- invalid
created_at: '2017-08-18T12:00:00+00:00'
updated_at: '2017-09-12T15:54:25+00:00'
type: issue
status: closed
closed_at: '2017-09-12T15:54:25+00:00'
---

# Original Description
```
[ 56%] Linking C static library libunbound.a
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ranlib: file: libunbound.a(checklocks.c.o) has no symbols
```

# Discussion History
## moneromooo-monero | 2017-09-10T12:28:38+00:00
This file seems to be empty if USE_THREAD_DEBUG is not defined, so that's fine.

## moneromooo-monero | 2017-09-12T15:43:24+00:00
Invalid seems a bit wrong for a report that's correct, but not actually a bug (or not something we want to fix), but looks like the closest we have.

+invalid

# Action History
- Created by: jtgrassie | 2017-08-18T12:00:00+00:00
- Closed at: 2017-09-12T15:54:25+00:00
