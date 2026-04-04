---
title: Linux 64 bit distribution is actually 32 bit
source_url: https://github.com/monero-project/monero/issues/1024
author: avnr
assignees: []
labels: []
created_at: '2016-08-31T13:04:21+00:00'
updated_at: '2016-09-01T08:27:54+00:00'
type: issue
status: closed
closed_at: '2016-09-01T08:27:54+00:00'
---

# Original Description
The binaries in monero.linux.x64.v0-9-4-0.tar.bz2 are actually 32 bit. Got me stuck on an LMDB bug specific to 32 bit, see https://monero.stackexchange.com/questions/1410/blockchain-import-fails-transaction-has-too-many-dirty-pages-transaction-too


# Discussion History
## fluffypony | 2016-09-01T08:27:54+00:00
That's definitely incorrect -

```
ric@spagni-primary:~/tmp# ./bitmonerod --version
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.4.0-release)
ric@spagni-primary:~/tmp# file bitmonerod
bitmonerod: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=e870a624d3f110cef7ed91e46018110accaea11c, not stripped
```

You can confirm this using the "file" command on your copy of Linux.


# Action History
- Created by: avnr | 2016-08-31T13:04:21+00:00
- Closed at: 2016-09-01T08:27:54+00:00
