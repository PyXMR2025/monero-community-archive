---
title: Setting MONERO_WALLET_CRYPTO_LIBRARY to `cn`?
source_url: https://github.com/monero-project/monero/issues/6774
author: moneroexamples
assignees: []
labels: []
created_at: '2020-08-23T07:23:00+00:00'
updated_at: '2020-08-25T03:53:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
By default `MONERO_WALLET_CRYPTO_LIBRARY` is `auto`. 

Is there a way to set it  to `cn` when building monero. Something along the lines of setting up `USE_SINGLE_BUILDDIR`:

```
USE_SINGLE_BUILDDIR=1 make
```

But when I try to execute analoging command for `MONERO_WALLET_CRYPTO_LIBRARY`:

```
MONERO_WALLET_CRYPTO_LIBRARY=cn make 
```

the `MONERO_WALLET_CRYPTO_LIBRARY` will be `auto` regardless.






# Discussion History
## selsta | 2020-08-23T13:29:31+00:00
As a workaround you can change the Makefile to include -DMONERO_WALLET_CRYPTO_LIBRARY=cn

## iDunk5400 | 2020-08-23T17:43:29+00:00
Something like this would do what you want (the top bit, the rest is just cosmetics).
```diff
diff --git a/src/crypto/wallet/CMakeLists.txt b/src/crypto/wallet/CMakeLists.txt
index 4ed986dce..985dc1180 100644
--- a/src/crypto/wallet/CMakeLists.txt
+++ b/src/crypto/wallet/CMakeLists.txt
@@ -29,7 +29,12 @@
 #
 # Possibly user defined values.
 #
-set(MONERO_WALLET_CRYPTO_LIBRARY "auto" CACHE STRING "Select a wallet crypto library")
+if("$ENV{MONERO_WALLET_CRYPTO_LIBRARY}" STREQUAL "cn")
+  set(MONERO_WALLET_CRYPTO_LIBRARY "cn" CACHE STRING "Internal crypto library for wallet selected by user")
+  message(STATUS "Wallet crypto is using cn crypto backend, internal crypto library for wallet selected by user")
+else()
+  set(MONERO_WALLET_CRYPTO_LIBRARY "auto" CACHE STRING "Select a wallet crypto library")
+endif()

 #
 # If the user specified "auto", detect best library defaulting to internal.
@@ -37,10 +42,10 @@ set(MONERO_WALLET_CRYPTO_LIBRARY "auto" CACHE STRING "Select a wallet crypto lib
 if (${MONERO_WALLET_CRYPTO_LIBRARY} STREQUAL "auto")
    monero_crypto_autodetect(AVAILABLE BEST)
   if (DEFINED BEST)
-    message("Wallet crypto is using ${BEST} backend")
+    message(STATUS "Wallet crypto is using ${BEST} backend")
     set(MONERO_WALLET_CRYPTO_LIBRARY ${BEST})
   else ()
-    message("Defaulting to internal crypto library for wallet")
+    message(STATUS "Defaulting to internal crypto library for wallet")
     set(MONERO_WALLET_CRYPTO_LIBRARY "cn")
   endif ()
 endif ()
diff --git a/tests/CMakeLists.txt b/tests/CMakeLists.txt
index c601b93ed..e42ee6a48 100644
--- a/tests/CMakeLists.txt
+++ b/tests/CMakeLists.txt
@@ -129,7 +129,7 @@ if (${MONERO_WALLET_CRYPTO_BENCH} STREQUAL "auto")
   if (DEFINED AVAILABLE)
     list(APPEND MONERO_WALLET_CRYPTO_BENCH ${AVAILABLE})
   endif ()
-  message("Wallet crypto bench is using ${MONERO_WALLET_CRYPTO_BENCH}")
+  message(STATUS "Wallet crypto bench is using ${MONERO_WALLET_CRYPTO_BENCH}")
 endif ()

 list(REMOVE_DUPLICATES MONERO_WALLET_CRYPTO_BENCH)
```

## moneroexamples | 2020-08-24T02:36:41+00:00
@iDunk5400 

Thank you it works well. Is there a chance for this patch to be PRed?  

## vtnerd | 2020-08-24T14:46:59+00:00
I don't understand why a change to an environment variable is necessary when the other options are done via standard cmake option ?

## iDunk5400 | 2020-08-24T17:51:26+00:00
There are many ways to do what @moneroexamples requested. Editing the Makefile and adding the cmake define and having to stash/pop every time master is pulled, creating a local branch and having to rebase to master every time master is pulled, etc...
Having the option to prepend the desired cmake define value to `make` is probably the easiest. I don't know why this particular case is useful, as it's giving away free performance. Maybe if we/you knew what the problem is, there could be a better solution.

I can PR later if you are OK with it.

## moneroexamples | 2020-08-25T02:44:52+00:00
@vtnerd 

I think it would be good to use `make` for that to keep it in line with `USE_SINGLE_BUILDDIR` option.To setting of `USE_SINGLE_BUILDDIR` is done using `make` without needing to "manually" set it up with  `cmake`. 

@iDunk5400 

The issue I have now, and maybe others as well in the future, is that  projects that are base of monero are dependent now on the optimized library. For example, the monero explorer does not compile as it requires new libraries. I can make it work by using `MONERO_WALLET_CRYPTO_LIBRARY=cn` as explained in the following issue: 

https://github.com/moneroexamples/onion-monero-blockchain-explorer/issues/215

But for consistency reasons I think it would be good to set it using `make` as well and be able to do the following:

```
USE_SINGLE_BUILDDIR=1 MONERO_WALLET_CRYPTO_LIBRARY=cn make
```




## vtnerd | 2020-08-25T03:53:34+00:00
I would argue that those linker errors are the result of `device` being a dependency on a number of things incorrectly. Its difficult to undo now though.

# Action History
- Created by: moneroexamples | 2020-08-23T07:23:00+00:00
