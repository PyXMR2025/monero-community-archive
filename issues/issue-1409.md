---
title: Passing CFLAGS to make
source_url: https://github.com/monero-project/monero/issues/1409
author: sammy007
assignees: []
labels: []
created_at: '2016-12-06T04:33:00+00:00'
updated_at: '2016-12-06T05:48:46+00:00'
type: issue
status: closed
closed_at: '2016-12-06T05:48:46+00:00'
---

# Original Description
I am linking from GO CGO with monero libcrypto.a and some other libraries, previously I used `CXXFLAGS="-fPIC" CFLAGS="-fPIC" make` to achieve that. But with `master` I see:

```
relocation R_X86_64_TPOFF32 against `hp_state' can not be used when making a shared object; recompile with -fPIC
```

Is it possible to recompile monero with `fPIC` somehow?

# Discussion History
## sammy007 | 2016-12-06T05:48:46+00:00
Well, closing for now, kinda sorted out.

# Action History
- Created by: sammy007 | 2016-12-06T04:33:00+00:00
- Closed at: 2016-12-06T05:48:46+00:00
