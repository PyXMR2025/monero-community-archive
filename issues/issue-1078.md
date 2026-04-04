---
title: Build Error in Ubuntu 16LTS
source_url: https://github.com/monero-project/monero-gui/issues/1078
author: escoire
assignees: []
labels:
- resolved
created_at: '2018-01-15T10:51:16+00:00'
updated_at: '2018-03-30T01:09:18+00:00'
type: issue
status: closed
closed_at: '2018-03-30T01:09:18+00:00'
---

# Original Description
I am receiving the below failure when running 'make' on monero on Ubuntu 16 LTS. This looks like the same issue reported in #1067. Patch referenced https://github.com/monero-project/monero/pull/3061 is already applied.

```
[ 62%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: ../../external/unbound/libunbound.a(libunbound.c.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
../../external/unbound/libunbound.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:130: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1

```

# Discussion History
## milargos | 2018-02-12T08:54:16+00:00
I am running Ubuntu 16.04 LTS and working without an issue.
Make sure you have all the dependencies:  

1. Run `sudo apt-get update && sudo apt-get upgrade`
2. `sudo apt install build-essential cmake libboost-all-dev libzmq3-dev miniupnpc libunbound-dev graphviz doxygen libunwind8-dev pkg-config libssl-dev libreadline-dev `
3. `sudo apt install qtbase5-dev qt5-default qtdeclarative5-dev qml-module-qtquick-controls qml-module-qtquick-xmllistmodel qttools5-dev-tools qml-module-qtquick-dialogs qml-module-qt-labs-settings libqt5qml-graphicaleffects`
4. Clean previous build `rm -rf monero build`
5. Compile `./build.sh`

## sanderfoobar | 2018-03-30T00:24:14+00:00
I believe this issue was fixed in https://github.com/monero-project/monero/issues/3296

Closing this for now, however, please re-open when you believe it is still present.

## sanderfoobar | 2018-03-30T00:24:34+00:00
+resolved

# Action History
- Created by: escoire | 2018-01-15T10:51:16+00:00
- Closed at: 2018-03-30T01:09:18+00:00
