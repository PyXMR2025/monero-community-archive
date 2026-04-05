---
title: Not compatible stratum
source_url: https://github.com/xmrig/xmrig/issues/147
author: sammy007
assignees: []
labels:
- bug
created_at: '2017-10-10T05:03:49+00:00'
updated_at: '2017-10-15T04:27:47+00:00'
type: issue
status: closed
closed_at: '2017-10-15T04:27:46+00:00'
---

# Original Description
> xmrig checks jobid in setId() method of the class JobID which must be at least 4 bytes long to pass the check.

https://github.com/sammy007/monero-stratum/issues/60#issuecomment-335088449

Such requirement is incorrect.

```c
diff -ur xmrig_orig/src/net/JobId.h xmrig/src/net/JobId.h
--- xmrig_orig/src/net/JobId.h	2017-10-09 03:22:24.733266554 -0400
+++ xmrig/src/net/JobId.h	2017-10-09 03:23:04.392712944 -0400
@@ -63,7 +63,7 @@
         }
 
         const size_t size = strlen(id);
-        if (size < 4 || size >= sizeof(m_data)) {
+        if (size >= sizeof(m_data)) {
             return false;
         }
 
```

# Discussion History
## xmrig | 2017-10-10T13:36:44+00:00
I fixed it. Please don't close this issue I will install your monero-stratum to verify all works fine in other places.
Thank you.

## sammy007 | 2017-10-10T14:46:22+00:00
Very nice, thank you.

## 2010phenix | 2017-10-11T13:11:18+00:00
Xmrig, maybe we have this bug and in old, written on C (classic) miner?

## xmrig | 2017-10-11T16:01:44+00:00
@2010phenix good catch. I check it now, classic miner unaffected.
Also this bug was in proxy too, after update, miners behind proxy will be unaffected.
I will make bugfix release in 1-2 days.
Thank you.


## xmrig | 2017-10-15T04:27:46+00:00
v2.4.1 with the fix released.

# Action History
- Created by: sammy007 | 2017-10-10T05:03:49+00:00
- Closed at: 2017-10-15T04:27:46+00:00
