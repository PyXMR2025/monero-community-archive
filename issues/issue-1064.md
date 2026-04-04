---
title: plugin needed to handle lto object following latest pulls
source_url: https://github.com/monero-project/monero/issues/1064
author: ghost
assignees: []
labels: []
created_at: '2016-09-10T16:28:56+00:00'
updated_at: '2016-09-15T13:18:32+00:00'
type: issue
status: closed
closed_at: '2016-09-15T13:18:32+00:00'
---

# Original Description
Hi @radfish and @fluffypony, I've just pulled down the latest merges and started to build on my system but it's starting to fail here:

```
[  9%] Linking CXX static library libotshell_utils.a
/usr/bin/ar: CMakeFiles/otshell_utils.dir/windows_stream.cpp.o: plugin needed to handle lto object
/usr/bin/ar: CMakeFiles/otshell_utils.dir/runoptions.cpp.o: plugin needed to handle lto object
/usr/bin/ar: CMakeFiles/otshell_utils.dir/utils.cpp.o: plugin needed to handle lto object
/usr/bin/ar: CMakeFiles/otshell_utils.dir/ccolor.cpp.o: plugin needed to handle lto object
/usr/bin/ranlib: windows_stream.cpp.o: plugin needed to handle lto object
/usr/bin/ranlib: runoptions.cpp.o: plugin needed to handle lto object
/usr/bin/ranlib: utils.cpp.o: plugin needed to handle lto object
/usr/bin/ranlib: ccolor.cpp.o: plugin needed to handle lot object
```

This error with /ar and /ranlib appears throughout the rest of the compile with the following libraries:

`libcrypto.a`,  `libcommon.a`, `libringct.a`, `libblocks.a`, `libblockchain_db.a`, `libcryptonote_core.a`, `libcryptonote_protocol.a`, `librpc.a`, `libwallet.a`, `libp2p.a`

And then compilation finally fails when trying to link monero-wallet-cli

I found this if it helps? https://stackoverflow.com/questions/39236917/using-gccs-link-time-optimization-with-static-linked-libraries

Which makes me wonder whether PR #1047 possibly introduced this breaking change?


# Discussion History
## ghost | 2016-09-11T15:47:47+00:00
Fixed by #1065, will close when merged


# Action History
- Created by: ghost | 2016-09-10T16:28:56+00:00
- Closed at: 2016-09-15T13:18:32+00:00
