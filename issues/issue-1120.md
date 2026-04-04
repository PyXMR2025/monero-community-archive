---
title: Cannot build on Mac OS - 'sys/vmmeter.h' file not found
source_url: https://github.com/monero-project/monero-gui/issues/1120
author: samsondav
assignees: []
labels:
- invalid
created_at: '2018-02-18T08:12:03+00:00'
updated_at: '2018-12-18T16:00:37+00:00'
type: issue
status: closed
closed_at: '2018-12-18T16:00:37+00:00'
---

# Original Description
I get the following error trying to build on Mac OS High Sierra (10.13.3)

```
monero-gui/monero/external/unbound/compat/getentropy_osx.c:47:10: fatal error: 'sys/vmmeter.h' file not found
```

Any ideas? I've installed all the dependencies listed in the README.

# Discussion History
## sanderfoobar | 2018-03-30T00:11:35+00:00
Could you try again using latest master?

## sanderfoobar | 2018-12-18T15:57:57+00:00
+invalid

# Action History
- Created by: samsondav | 2018-02-18T08:12:03+00:00
- Closed at: 2018-12-18T16:00:37+00:00
