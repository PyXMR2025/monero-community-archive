---
title: crypto::random32_unbiased is both biased and can return 0
source_url: https://github.com/monero-project/monero/issues/7061
author: jagerman
assignees: []
labels: []
created_at: '2020-12-03T16:16:12+00:00'
updated_at: '2020-12-10T21:37:54+00:00'
type: issue
status: closed
closed_at: '2020-12-10T21:37:54+00:00'
---

# Original Description
#4097 rewrote random scalar generation with the objective of removing the slight bias of doing `random % L`; as originally written in the PR it was fine, but then 7434df1cc6e96b5d98ea6e3ec095eaae4ac9a95c updated the code to supposedly prevent it from returning 0, but in the process reintroduced the bias and didn't actually prevent it from returning 0.

- `while (!sc_isnonzero(bytes) && !less32(bytes, limit));` is logically saying (in 32-byte integer math): `while (value == 0 && value >= limit)` which is clearly never satisfied.  Thus this loop can never actually loop, and this code ends up simply doing `random mod L`.

- However even if that is fixed (to `while (!(sc_isnonzero(bytes) && less32(bytes, limit)))`), the `sc_reduce32` call will reduce any generated non-negative integral multiple of L to 0, which isn't supposed to happen.

# Discussion History
## moneromooo-monero | 2020-12-03T16:27:08+00:00
Nice find.
I think this fixes it:
```
diff --git a/src/crypto/crypto.cpp b/src/crypto/crypto.cpp
index 4cfe83d54..19fb2e65b 100644
--- a/src/crypto/crypto.cpp
+++ b/src/crypto/crypto.cpp
@@ -128,8 +128,8 @@ namespace crypto {
     do
     {
       generate_random_bytes_thread_safe(32, bytes);
-    } while (!sc_isnonzero(bytes) && !less32(bytes, limit)); // should be good about 15/16 of the time
-    sc_reduce32(bytes);
+      sc_reduce32(bytes);
+    } while (!sc_isnonzero(bytes) || !less32(bytes, limit)); // should be good about 15/16 of the time
   }
   /* generate a random 32-byte (256-bit) integer and copy it to res */
   static inline void random_scalar(ec_scalar &res) {
```
Testing now.

## moneromooo-monero | 2020-12-03T17:00:46+00:00
https://github.com/monero-project/monero/pull/7062

Thanks

# Action History
- Created by: jagerman | 2020-12-03T16:16:12+00:00
- Closed at: 2020-12-10T21:37:54+00:00
