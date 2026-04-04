---
title: Can't compile static release-v0.13 at Ubuntu 18.04
source_url: https://github.com/monero-project/monero/issues/4593
author: bmnc-team
assignees: []
labels: []
created_at: '2018-10-15T03:36:07+00:00'
updated_at: '2018-10-21T03:08:09+00:00'
type: issue
status: closed
closed_at: '2018-10-21T03:08:09+00:00'
---

# Original Description
Command: make release-static
OS: Ubuntu 18.04 x64
Errors:
[ 96%] Linking CXX executable ../../bin/monerod
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::init(char const*, bool, bool)':
(.text+0x24d): undefined reference to `NORM_INSTANCE_INVALID'
(.text+0x265): undefined reference to `NormCreateSession'
(.text+0x26c): undefined reference to `NORM_SESSION_INVALID'
(.text+0x281): undefined reference to `NormIsUnicastAddress'
(.text+0x29a): undefined reference to `NormSetTTL'
(.text+0x2b2): undefined reference to `NormSetRxPortReuse'
(.text+0x2c3): undefined reference to `NormSetLoopback'
(.text+0x2d7): undefined reference to `NormSetMulticastInterface'
(.text+0x31e): undefined reference to `NormSetDefaultUnicastNack'
(.text+0x334): undefined reference to `NormSetDefaultSyncPolicy'
(.text+0x345): undefined reference to `NormStartReceiver'
(.text+0x360): undefined reference to `NormGetRandomSessionId'
(.text+0x385): undefined reference to `NormStartSender'
(.text+0x39f): undefined reference to `NormSetCongestionControl'
(.text+0x3c2): undefined reference to `NormStreamOpen'
(.text+0x3c9): undefined reference to `NORM_OBJECT_INVALID'
(.text+0x3f3): undefined reference to `NormDestroyInstance'
(.text+0x3fa): undefined reference to `NORM_SESSION_INVALID'
(.text+0x408): undefined reference to `NORM_INSTANCE_INVALID'
(.text+0x42a): undefined reference to `NORM_NODE_ANY'
(.text+0x447): undefined reference to `NormCreateInstance'
(.text+0x44e): undefined reference to `NORM_INSTANCE_INVALID'
(.text+0x498): undefined reference to `NormDestroyInstance'
(.text+0x49f): undefined reference to `NORM_INSTANCE_INVALID'
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::send_data()':
(.text+0x851): undefined reference to `NormStreamWrite'
(.text+0x912): undefined reference to `NormStreamFlush'
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::plug(zmq::io_thread_t*, zmq::session_base_t*)':
(.text+0xb20): undefined reference to `NormGetDescriptor'
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::recv_data(void const*)':
(.text+0x11d4): undefined reference to `NORM_OBJECT_INVALID'
(.text+0x11e1): undefined reference to `NormObjectGetType'
(.text+0x11f2): undefined reference to `NormObjectGetUserData'
(.text+0x1267): undefined reference to `NormStreamSeekMsgStart'
(.text+0x1288): undefined reference to `NormStreamRead'
(.text+0x12da): undefined reference to `NormStreamRead'
(.text+0x17ae): undefined reference to `NormObjectGetUserData'
(.text+0x184b): undefined reference to `NormObjectSetUserData'
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::restart_input()':
(.text+0x19a4): undefined reference to `NORM_OBJECT_INVALID'
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::in_event()':
(.text+0x19f8): undefined reference to `NormGetNextEvent'
(.text+0x1aa6): undefined reference to `NormObjectGetUserData'
(.text+0x1b4e): undefined reference to `NormNodeDelete'
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::shutdown()':
(.text+0x1c49): undefined reference to `NORM_SESSION_INVALID'
(.text+0x1c53): undefined reference to `NormDestroySession'
(.text+0x1c68): undefined reference to `NORM_INSTANCE_INVALID'
(.text+0x1c72): undefined reference to `NormStopInstance'
(.text+0x1c7e): undefined reference to `NormDestroyInstance'
(.text+0x1c91): undefined reference to `NormStopReceiver'
(.text+0x1cd5): undefined reference to `NormStopSender'
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libzmq.a(src_libzmq_la-norm_engine.o): In function `zmq::norm_engine_t::norm_engine_t(zmq::io_thread_t*, zmq::options_t const&)':
(.text+0x26bb): undefined reference to `NORM_INSTANCE_INVALID'
(.text+0x26e3): undefined reference to `NORM_SESSION_INVALID'
(.text+0x26f6): undefined reference to `NORM_OBJECT_INVALID'
collect2: error: ld returned 1 exit status
src/daemon/CMakeFiles/daemon.dir/build.make:289: recipe for target 'bin/monerod' failed
make[3]: *** [bin/monerod] Error 1
make[3]: Leaving directory '/root/monero/build/Linux/release-v0.13/release'
CMakeFiles/Makefile2:3019: recipe for target 'src/daemon/CMakeFiles/daemon.dir/all' failed
make[2]: *** [src/daemon/CMakeFiles/daemon.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/root/monero/build/Linux/release-v0.13/release'
[ 96%] Built target obj_wallet
make[2]: Leaving directory '/root/monero/build/Linux/release-v0.13/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/Linux/release-v0.13/release'
Makefile:89: recipe for target 'release-static' failed
make: *** [release-static] Error 2

# Discussion History
## moneromooo-monero | 2018-10-15T09:13:19+00:00
Check you have libzmq >= 3.0.0, that you don't have more than one libzmq around (or that you're using just one), make sure you make a build from scratch if you changed libzmq stuff recently.

## iDunk5400 | 2018-10-15T09:56:07+00:00
`sudo apt install libnorm-dev libpgm-dev`

## bmnc-team | 2018-10-15T10:23:51+00:00
> `sudo apt install libnorm-dev libpgm-dev`

Thank you! it's work now.

## bmnc-team | 2018-10-15T10:26:11+00:00
> Check you have libzmq >= 3.0.0, that you don't have more than one libzmq around (or that you're using just one), make sure you make a build from scratch if you changed libzmq stuff recently.

My libzmq it's ok, and libnorm-dev help me to finish my compile, maybe you can add this package to README.md :) Thank you!

## moneromooo-monero | 2018-10-15T13:01:47+00:00
https://github.com/monero-project/monero/pull/4597

## bmnc-team | 2018-10-17T07:51:30+00:00
> #4597

Thank you!
I finished my compile, but is doesn't output a static library of norm.

## moneromooo-monero | 2018-10-17T09:37:52+00:00
You compiled libnorm ? Check its docs and/or configure --help or similar to see how to make a static lib if you need one.


# Action History
- Created by: bmnc-team | 2018-10-15T03:36:07+00:00
- Closed at: 2018-10-21T03:08:09+00:00
