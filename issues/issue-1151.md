---
title: '[Windows] Can''t build RELEASE-STATIC Monero-GUI, only RELEASE'
source_url: https://github.com/monero-project/monero-gui/issues/1151
author: limnique
assignees: []
labels:
- invalid
created_at: '2018-03-04T12:47:37+00:00'
updated_at: '2018-04-05T20:00:58+00:00'
type: issue
status: closed
closed_at: '2018-04-05T20:00:58+00:00'
---

# Original Description
Hi guys! I can't build release-static monero-gui, only release. When I trying to build it by typing:
```
./build.sh release-static
```
I got this error:
```
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x2b6): undefined reference to `ub_ctx_delete'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x12d0): undefined reference to `ub_resolve'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x1379): undefined reference to `ub_resolve_free'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x13d0): undefined reference to `ub_resolve_free'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x2130): undefined reference to `ub_ctx_create'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x214e): undefined reference to `ub_ctx_set_fwd'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x2185): undefined reference to `ub_ctx_set_option'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x21c5): undefined reference to `ub_ctx_set_option'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x230c): undefined reference to `ub_ctx_create'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x2320): undefined reference to `ub_ctx_resolvconf'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x2332): undefined reference to `ub_ctx_hosts'
C:/msys64/mingw32/lib/wallet_merged.a(dns_utils.cpp.obj):dns_utils.cpp:(.text+0x2350): undefined reference to `ub_ctx_add_ta'
C:/msys64/mingw32/lib/wallet_merged.a(util.cpp.obj):util.cpp:(.text+0x25b1): undefined reference to `ub_ctx_create'
C:/msys64/mingw32/lib/wallet_merged.a(util.cpp.obj):util.cpp:(.text+0x25da): undefined reference to `ub_ctx_zone_add'
C:/msys64/mingw32/lib/wallet_merged.a(util.cpp.obj):util.cpp:(.text+0x25e6): undefined reference to `ub_ctx_async'
C:/msys64/mingw32/lib/wallet_merged.a(util.cpp.obj):util.cpp:(.text+0x25f3): undefined reference to `ub_ctx_delete'
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:203: release/bin/monero-wallet-gui.exe] Ошибка 1
make[1]: выход из каталога «/d/GitHub/monero-gui-wallet/build»
make: *** [Makefile:36: release] Ошибка 2
```
How I can fix this and finally make successful RELEASE-STATIC build?
Thank you!

# Discussion History
## limnique | 2018-03-05T20:03:32+00:00
Still can't do that, any help? Or maybe you have any random guess? I will try any solution :)

## sanderfoobar | 2018-04-04T06:16:58+00:00
There has been some changes as of late, could you perhaps try again using latest master? I also believe the build instructions [have been updated](https://github.com/monero-project/monero-gui/tree/master/installers/windows).

Also https://github.com/monero-project/monero-gui#on-windows

## sanderfoobar | 2018-04-05T18:33:26+00:00
Ill close this for now, feel free to re-open if issues persist.

## sanderfoobar | 2018-04-05T18:33:52+00:00
+invalid

# Action History
- Created by: limnique | 2018-03-04T12:47:37+00:00
- Closed at: 2018-04-05T20:00:58+00:00
