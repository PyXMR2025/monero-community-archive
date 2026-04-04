---
title: 'Monero does not compile: LTO version 5.1 instead of the expected 5.2'
source_url: https://github.com/monero-project/monero/issues/1865
author: moneroexamples
assignees: []
labels: []
created_at: '2017-03-13T05:54:19+00:00'
updated_at: '2017-03-13T10:35:46+00:00'
type: issue
status: closed
closed_at: '2017-03-13T10:35:46+00:00'
---

# Original Description
`v0.10.2.1-d4236689` does not compile.

```
lto1: fatal error: bytecode stream generated with LTO version 5.1 instead of the expected 5.2
compilation terminated.
lto-wrapper: fatal error: /usr/bin/c++ returned 1 exit status
compilation terminated.
/usr/bin/ld: error: lto-wrapper failed
collect2: error: ld returned 1 exit status
make[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:131: bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/home/mwo/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1291: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/home/mwo/monero/build/release'
make[1]: *** [Makefile:139: all] Error 2
make[1]: Leaving directory '/home/mwo/monero/build/release'
make: *** [Makefile:59: release-all] Error 2
```

You can workaround this issue:

```
cmake .  -DUSE_LTO=OFF
make
```


# Discussion History
## hyc | 2017-03-13T10:31:16+00:00
Sounds like you had leftover files from a previous compile, and then upgraded your build tools after that. You should do a make clean. 

## moneroexamples | 2017-03-13T10:35:46+00:00
its possible. there were some upgrades in manjaro befor that, but I havent looked what I was upgrading. but after reset of the pc later, it compiled fine. 

# Action History
- Created by: moneroexamples | 2017-03-13T05:54:19+00:00
- Closed at: 2017-03-13T10:35:46+00:00
