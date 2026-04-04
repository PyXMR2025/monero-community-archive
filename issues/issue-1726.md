---
title: Build on Ubuntu 18.04.1 LTS does not work
source_url: https://github.com/monero-project/monero-gui/issues/1726
author: buricl
assignees: []
labels:
- resolved
created_at: '2018-11-05T22:25:44+00:00'
updated_at: '2018-11-06T20:00:31+00:00'
type: issue
status: closed
closed_at: '2018-11-06T20:00:31+00:00'
---

# Original Description
I followed all steps from README.md and eventually ended up with linking error:

```
/home/lubor/repos/monero-gui/monero/lib/libwallet_merged.a(wallet2.cpp.o): In function `tools::wallet2::register_devices()':
wallet2.cpp:(.text+0x64c1): undefined reference to `hw::trezor::register_all()'
collect2: error: ld returned 1 exit status
Makefile:295: recipe for target 'release/bin/monero-wallet-gui' failed
```
Full build log is attached. Aren't we missing linking to libdevice_trezor.a?

[build.log](https://github.com/monero-project/monero-gui/files/2550820/build.log)

Furthermore, I get no such file or directory error

```
Installing libunbound...
./get_libwallet_api.sh: line 240: pushd: /home/lubor/repos/monero-gui/monero/build/release/external/unbound: No such file or directory
```
My build is using system libunbound and therefore this bit in get_libwallet_api.sh should not be performed.

# Discussion History
## buricl | 2018-11-05T23:41:19+00:00
Already opened pull request which fixes this problem

## sanderfoobar | 2018-11-06T00:41:10+00:00
Thanks.

## dEBRUYNE-1 | 2018-11-06T19:54:49+00:00
+resolved

# Action History
- Created by: buricl | 2018-11-05T22:25:44+00:00
- Closed at: 2018-11-06T20:00:31+00:00
