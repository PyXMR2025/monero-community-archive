---
title: Compiling monero V0.12 Static Ubuntu  x86_64 and i can't fix this error
source_url: https://github.com/monero-project/monero/issues/3501
author: italocoin-project
assignees: []
labels:
- invalid
created_at: '2018-03-27T10:06:35+00:00'
updated_at: '2018-03-27T23:40:46+00:00'
type: issue
status: closed
closed_at: '2018-03-27T23:40:46+00:00'
---

# Original Description
keep in mind, i compiled boost and ssl with -fPIC flag, but this error won't go away, any ideas?

```
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libtinfo.a(lib_termcap.o): relocation R_X86_64_32 against `_nc_globals' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libtinfo.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/simplewallet/CMakeFiles/simplewallet.dir/build.make:135: recipe for target 'bin/monero-wallet-cli' failed
make[3]: *** [bin/monero-wallet-cli] Error 1
make[3]: Leaving directory '/root/monero/build/release'
```

# Discussion History
## moneromooo-monero | 2018-03-27T10:18:49+00:00
That message is clearly about libtinfo.a, not boost nor ssl.
It's used by readline, so you can disable readline (-D USE_READLINE=OFF to cmake) or build libtinfo with -fPIC. 

## italocoin-project | 2018-03-27T10:20:22+00:00
Whats readline used for?

## CamilleScholtz | 2018-03-27T19:47:37+00:00
Input editing

## moneromooo-monero | 2018-03-27T23:25:06+00:00
+invalid

# Action History
- Created by: italocoin-project | 2018-03-27T10:06:35+00:00
- Closed at: 2018-03-27T23:40:46+00:00
