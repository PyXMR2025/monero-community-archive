---
title: External unbound is preferred over vendored unbound submodule
source_url: https://github.com/monero-project/monero/issues/3822
author: ilovezfs
assignees: []
labels: []
created_at: '2018-05-17T13:11:52+00:00'
updated_at: '2018-05-20T04:24:32+00:00'
type: issue
status: closed
closed_at: '2018-05-20T04:24:32+00:00'
---

# Original Description
Tested with both 0.12.0.0 and HEAD @ 4b728d7

If `unbound` happens to already be installed, we get
```
==> Summary
🍺  /usr/local/Cellar/monero/HEAD-4b728d7_2: 24 files, 55.4MB, built in 2 minutes 58 seconds
iMac-TMP:~ joe$ brew linkage monero
System libraries:
  /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
  /System/Library/Frameworks/PCSC.framework/Versions/A/PCSC
  /usr/lib/libSystem.B.dylib
  /usr/lib/libc++.1.dylib
Homebrew libraries:
  /usr/local/opt/boost/lib/libboost_chrono-mt.dylib (boost)
  /usr/local/opt/boost/lib/libboost_date_time-mt.dylib (boost)
  /usr/local/opt/boost/lib/libboost_filesystem-mt.dylib (boost)
  /usr/local/opt/boost/lib/libboost_program_options-mt.dylib (boost)
  /usr/local/opt/boost/lib/libboost_regex-mt.dylib (boost)
  /usr/local/opt/boost/lib/libboost_serialization-mt.dylib (boost)
  /usr/local/opt/boost/lib/libboost_system-mt.dylib (boost)
  /usr/local/opt/boost/lib/libboost_thread-mt.dylib (boost)
  /usr/local/opt/openssl/lib/libcrypto.1.0.0.dylib (openssl)
  /usr/local/opt/openssl/lib/libssl.1.0.0.dylib (openssl)
  /usr/local/opt/readline/lib/libreadline.7.dylib (readline)
  /usr/local/opt/unbound/lib/libunbound.2.dylib (unbound)
  /usr/local/opt/zeromq/lib/libzmq.5.dylib (zeromq)
Undeclared dependencies with linkage:
  unbound
```
and the submodule is not used. This happens regardless of whether I pass `-DINSTALL_VENDORED_LIBUNBOUND=ON`

Full log: https://gist.github.com/ilovezfs/a2007ba66311afe6da9f3cd31c9014a2

CC @jtgrassie 

# Discussion History
## moneromooo-monero | 2018-05-17T15:04:30+00:00
AFAIK this is the intent.

## ilovezfs | 2018-05-17T15:06:28+00:00
Hmm OK. @jtgrassie was saying that we should use the submodule in Homebrew, but I'll put it back to using the formula then.

## ilovezfs | 2018-05-17T15:11:16+00:00
@moneromooo-monero https://github.com/Homebrew/homebrew-core/pull/27977 for your review

## jtgrassie | 2018-05-17T15:36:32+00:00
I was saying use the monero submodule of unbound which I thought was correct (instead of using external unbound because the submodule is modified).

## ilovezfs | 2018-05-20T04:24:32+00:00
I'm closing this since @moneromooo-monero indicates the preference for the externally installed unbound over the submodule is intentional.

# Action History
- Created by: ilovezfs | 2018-05-17T13:11:52+00:00
- Closed at: 2018-05-20T04:24:32+00:00
