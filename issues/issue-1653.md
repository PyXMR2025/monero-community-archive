---
title: Compilation of 32-bit static binaries fails.
source_url: https://github.com/monero-project/monero/issues/1653
author: WE1SLkZPUi5GVU4K
assignees: []
labels: []
created_at: '2017-01-30T11:26:42+00:00'
updated_at: '2017-10-03T10:06:22+00:00'
type: issue
status: closed
closed_at: '2017-10-03T10:06:22+00:00'
---

# Original Description
I'm trying to compile static 32-bit binaries on arch using `make release-static-32` and get the following error:

```
[ 86%] Linking CXX static library ../../lib/libwallet.a
make[3]: Leaving directory '/builing/monero/build/release'
[ 86%] Built target wallet
make[3]: Entering directory '/builing/monero/build/release'
Scanning dependencies of target wallet_rpc_server
make[3]: Leaving directory '/builing/monero/build/release'
make[3]: Entering directory '/builing/monero/build/release'
[ 87%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 88%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/lib/gcc/i686-pc-linux-gnu/6.3.1/../../../libboost_program_options.a(variables_map.o): In function `boost::program_options::abstract_variables_map::abstract_variables_map()':
(.text+0x181): undefined reference to `vtable for boost::program_options::abstract_variables_map'
/usr/lib/gcc/i686-pc-linux-gnu/6.3.1/../../../libboost_program_options.a(variables_map.o): In function `boost::program_options::abstract_variables_map::abstract_variables_map(boost::program_options::abstract_variables_map const*)':
(.text+0x1b1): undefined reference to `vtable for boost::program_options::abstract_variables_map'
collect2: error: ld returned 1 exit status
make[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:132: bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/builing/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1303: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/builing/monero/build/release'
make[1]: *** [Makefile:139: all] Error 2
make[1]: Leaving directory '/builing/monero/build/release'
make: *** [Makefile:89: release-static-32] Error 2
```

The same happens for 64-bit static as well.

# Discussion History
## iDunk5400 | 2017-01-30T14:34:40+00:00
Try adding `-D USE_LTO=OFF` define to the cmake line of `release-static-32` target in the Makefile (and/or `release-static-64`).

## ghost | 2017-01-30T14:34:41+00:00
What OS, compiler, processor?

## WE1SLkZPUi5GVU4K | 2017-01-30T15:40:07+00:00
Adding `-D USE_LTO=OFF` to the cmake command made it work, thanks!

I've been trying compile on both 32-bit and 64-bit machines on Arch Linux. Always got the same reuslt. GCC version used is 6.3.1. For what it's worth, I'm not the only one with this problem. mWo12 on [reddit](https://www.reddit.com/r/Monero/comments/5qtdbq/submittingbroadcasting_transfer_without_daemon/) also wasn't able to build static binaries on arch.


## ghost | 2017-01-30T15:59:41+00:00
@iDunk5400 @moneromooo-monero Should this be submitted as a PR to core? Or maybe as an extra flag if the system detects ARCH Linux?

## iDunk5400 | 2017-01-30T16:08:17+00:00
I have always had this problem building static monero on Ubuntu. Disabling LTO always solved it for me. Apparently, not everyone seems to have this problem with static builds.

## ghost | 2017-01-31T02:39:27+00:00
What's the potential harm in disabling this for all static Linux builds?

## moneromooo-monero | 2017-08-08T11:01:49+00:00
Slight performance degradation I guess. I doubt it'd be a lot, but that's speculation.

## moneromooo-monero | 2017-10-03T09:58:21+00:00
Looks like LTO now defaults to false.

+resolved

# Action History
- Created by: WE1SLkZPUi5GVU4K | 2017-01-30T11:26:42+00:00
- Closed at: 2017-10-03T10:06:22+00:00
