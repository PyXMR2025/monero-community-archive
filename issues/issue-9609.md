---
title: '[gentoo amd64] build.sh fails on boost'
source_url: https://github.com/monero-project/monero/issues/9609
author: x64x2
assignees: []
labels:
- invalid
created_at: '2024-12-10T09:15:15+00:00'
updated_at: '2025-02-18T13:05:28+00:00'
type: issue
status: closed
closed_at: '2025-02-18T13:05:28+00:00'
---

# Original Description
compiling monero  after fetch-params.sh results in this
$./xmrcutil/build.sh --disable-cpp -j6

`Building boost...
mkdir -p /home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/.
cd /home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/.; PATH=/home/user/work/dude/activity/monero_wallet/monero/depends/x86_64-unknown-linux-gnu/native/bin:/usr/local/bin:/usr/bin:/bin:/opt/bin:/usr/x86_64-pc-linux-gnu/gcc-bin/4.9.4:/usr/lib/llvm/5/bin:/usr/lib/llvm/4/bin:/usr/games/bin ./b2 -d2 -j2 -d1 --prefix=/home/user/work/dude/activity/monero_wallet/monero/depends/work/staging/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/home/user/work/dude/activity/monero_wallet/monero/depends/x86_64-unknown-linux-gnu --layout=tagged --build-type=complete --user-config=user-config.jam threading=multi link=static -sNO_BZIP2=1 -sNO_ZLIB=1 variant=release threadapi=pthread runtime-link=shared stage
/home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/build/feature.jam:494: in feature.validate-value-string from module feature
error: "none" is not a known value of feature
error: legal values: "off" "speed" "space"
/home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/build/property.jam:276: in validate1 from module property
/home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/build/property.jam:302: in property.validate from module property
/home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/tools/builtin.jam:381: in variant from module builtin
/usr/share/boost-build/site-config.jam:9: in modules.load from module site-config
/home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/build-system.jam:249: in load-config from module build-system
/home/user/work/dude/activity/monero_wa_llet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/build-system.jam:351: in load-configuration-files from module build-system
/home/user/work/dude/activity/monero_wa_llet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/build-system.jam:524: in load from module build-system
/home/user/work/dude/activity/monero_wa_llet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/kernel/modules.jam:295: in import from module modules
/home/user/work/dude/activity/monero_wa_llet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/tools/build/src/kernel/bootstrap.jam:139: in boost-build from module
/home/user/work/dude/activity/monero_wallet/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/boost-build.jam:17: in module scope from module

make: *** [funcs.mk:240: /home/user/work/dude/activity/monero_wallt/monero/depends/work/build/x86_64-unknown-linux-gnu/boost/1_62_0-2d69d505974/./.stamp_built] Error 1
make: uscita dalla directory "/home/user/work/dude/activity/monero_wallet/zcash/depends"

`

system's boost version: 1.62.0-r2

# Discussion History
## selsta | 2024-12-13T23:13:59+00:00
What is `xmrcutil`? I'm not aware what `build.sh` you are using or what project you are compiling.

# Action History
- Created by: x64x2 | 2024-12-10T09:15:15+00:00
- Closed at: 2025-02-18T13:05:28+00:00
