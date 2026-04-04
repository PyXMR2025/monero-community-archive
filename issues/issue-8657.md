---
title: SIGSEGV on MacBook M1
source_url: https://github.com/monero-project/monero/issues/8657
author: vorot93
assignees: []
labels:
- arm
- mac
created_at: '2022-11-29T22:43:45+00:00'
updated_at: '2023-12-10T17:22:36+00:00'
type: issue
status: closed
closed_at: '2023-12-10T17:22:36+00:00'
---

# Original Description
Crashes around the same block and on restart:

```
2022-11-29 22:36:51.443	I Sync data returned a new top block candidate: 2719724 -> 2766694 [Your node is 46970 blocks (2.1 months) behind]
2022-11-29 22:36:51.443	I SYNCHRONIZATION started
fish: Job 1, './build/Darwin/release-v0.18/re…' terminated by signal SIGSEGV (Address boundary error)
```

# Discussion History
## selsta | 2022-11-29T22:47:24+00:00
There's an issue with the latest macOS version that we didn't figure out yet.

Workaround is to use an older SDK

```diff
diff --git a/Makefile b/Makefile
index a07ac77a1..10e3cde27 100644
--- a/Makefile
+++ b/Makefile
@@ -100,7 +100,7 @@ release-test:
 
 release-all:
 	mkdir -p $(builddir)/release
-	cd $(builddir)/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release $(topdir) && $(MAKE)
+	cd $(builddir)/release && cmake -D CMAKE_OSX_SYSROOT=~/dev/MacOSX12.3.sdk/ -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Release $(topdir) && $(MAKE)
 
 release-static:
 	mkdir -p $(builddir)/release
```

You can download the older SDK from here: https://github.com/phracker/MacOSX-SDKs/releases/tag/11.3

Alternatively you can disable RandomX JIT with: `MONERO_RANDOMX_UMASK=8` env var.

## smathy | 2023-01-30T20:59:21+00:00
Just throwing in some keywords to help anyone else searching (and missing) with segfault or segmentation fault.  Thanks for your help in the chat @selsta 

## selsta | 2023-10-19T16:48:18+00:00
We found the issue, a fix will be included in the next release: https://github.com/tevador/RandomX/pull/281

## philipmw | 2023-12-10T17:07:01+00:00
I can confirm that the the latest git rev works on my Macbook Air M1, whereas the latest release (0.18.3.1) was consistently crashing with a segmentation fault.

# Action History
- Created by: vorot93 | 2022-11-29T22:43:45+00:00
- Closed at: 2023-12-10T17:22:36+00:00
