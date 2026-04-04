---
title: Build broken on OSX
source_url: https://github.com/monero-project/monero/issues/3706
author: hashbender
assignees: []
labels: []
created_at: '2018-04-25T20:56:11+00:00'
updated_at: '2018-04-28T15:02:37+00:00'
type: issue
status: closed
closed_at: '2018-04-28T15:02:37+00:00'
---

# Original Description
I've merged https://github.com/monero-project/monero/pull/3667 into my local build to get unblocked there, but I'm still broken. 

```
[  2%] Built target generate_translations_header
[  6%] Built target libminiupnpc-static
[  7%] Built target lmdb
[  8%] Built target easylogging
[ 12%] Built target epee
[ 13%] Built target genversion
[ 14%] Built target obj_version
[ 14%] Built target version
[ 21%] Built target obj_cncrypto
[ 22%] Built target cncrypto
[ 25%] Built target obj_common
[ 25%] Linking CXX shared library libcommon.dylib
Undefined symbols for architecture x86_64:
  "boost::chrono::steady_clock::now()", referenced from:
      void boost::this_thread::sleep_for<long long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long long, boost::ratio<1l, 1000l> > const&) in download.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [src/common/libcommon.dylib] Error 1
make[1]: *** [src/common/CMakeFiles/common.dir/all] Error 2
make: *** [all] Error 2
```

# Discussion History
## gene-telligent | 2018-04-25T23:58:26+00:00
You're using Boost 1.67 right? Did you build it yourself or install it through Homebrew?

## hashbender | 2018-04-26T00:08:44+00:00
Yes, boost 1.67.  Installed via Homebrew.  It seems to be related to running cmake -DBUILD_SHARED_LIBS=1 . 

I deleted and re-built from scratch and was able to successfully build, but trying to build the shared libs broke everything irreparably. 

## gene-telligent | 2018-04-26T04:13:13+00:00
Could you let me know if applying the change in the pull request I just made fixes the issue?

# Action History
- Created by: hashbender | 2018-04-25T20:56:11+00:00
- Closed at: 2018-04-28T15:02:37+00:00
