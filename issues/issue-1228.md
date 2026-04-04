---
title: Build fails with undefined references (PCSC related)
source_url: https://github.com/monero-project/monero-gui/issues/1228
author: rnhmjoj
assignees: []
labels: []
created_at: '2018-03-31T09:08:28+00:00'
updated_at: '2018-04-03T10:08:57+00:00'
type: issue
status: closed
closed_at: '2018-04-03T10:08:57+00:00'
---

# Original Description
I'm trying to build (package expression [here](https://gist.github.com/0bc7f1b5f719bf43ffa09508802bf049)) monero-gui 959c2fcc32d515f90cb39933689a37418197a095 and getting these:

```
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(miner.cpp.o): In function `cryptonote::miner::background_worker_thread()':
(.text+0x3786): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(miner.cpp.o): In function `cryptonote::miner::background_worker_thread()':
(.text+0x4144): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(miner.cpp.o): In function `epee::misc_utils::sleep_no_w(long)':
(.text._ZN4epee10misc_utils10sleep_no_wEl[_ZN4epee10misc_utils10sleep_no_wEl]+0x2bb): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::release()':
(.text+0x1e01): undefined reference to `SCardReleaseContext'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::disconnect()':
(.text+0x23b1): undefined reference to `SCardDisconnect'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::exchange(unsigned int, unsigned int)':
(.text+0x2bba): undefined reference to `g_rgSCardT0Pci'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::exchange(unsigned int, unsigned int)':
(.text+0x2bdc): undefined reference to `SCardTransmit'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::exchange(unsigned int, unsigned int)':
(.text+0x303a): undefined reference to `pcsc_stringify_error'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::exchange(unsigned int, unsigned int)':
(.text+0x30b5): undefined reference to `pcsc_stringify_error'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::init()':
(.text+0x4e9e): undefined reference to `SCardEstablishContext'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::init()':
(.text+0x4f66): undefined reference to `pcsc_stringify_error'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::init()':
(.text+0x51d8): undefined reference to `pcsc_stringify_error'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x593a): undefined reference to `SCardListReaders'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x5a63): undefined reference to `pcsc_stringify_error'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x5b24): undefined reference to `pcsc_stringify_error'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x5ff8): undefined reference to `SCardFreeMemory'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x61a6): undefined reference to `SCardDisconnect'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x64e3): undefined reference to `SCardConnect'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x660e): undefined reference to `SCardStatus'
/nix/store/i1x32q3s6ny0z2jmglmsmnnylzpzlfcx-monero-0.12.0.0/lib/libwallet_merged.a(device_ledger.cpp.o): In function `hw::ledger::device_ledger::connect()':
(.text+0x6903): undefined reference to `SCardFreeMemory'
collect2: error: ld returned 1 exit status
```

The same errors were reported here https://github.com/monero-project/monero-gui/issues/1066#issuecomment-377511652.

Any idea what am I missing?


# Discussion History
## rnhmjoj | 2018-03-31T09:45:00+00:00
I could build it with this
```patch
diff --git a/monero-wallet-gui.pro b/monero-wallet-gui.pro
index 50d3e0e..9857fc9 100644
--- a/monero-wallet-gui.pro
+++ b/monero-wallet-gui.pro
@@ -4,7 +4,9 @@ QT += qml quick widgets
 
 WALLET_ROOT=$$PWD/monero
 
-CONFIG += c++11
+CONFIG += c++11 link_pkgconfig
+PKGCONFIG += libpcsclite
+
 QMAKE_CXXFLAGS += -fPIC -fstack-protector
 QMAKE_LFLAGS += -fstack-protector
 
```

## iDunk5400 | 2018-03-31T14:29:09+00:00
The problem with this approach is if libpcsclite dev package is not installed, qmake fails like this:
```
Project ERROR: libpcsclite development package not found
Command exited with non-zero status 3
```
I tried to fix it on Linux in #1231, but that also didn't work if libpcsclite library was not installed. I probably messed up the env var check.

## iDunk5400 | 2018-03-31T17:43:40+00:00
This seems to work
```
diff --git a/monero-wallet-gui.pro b/monero-wallet-gui.pro
index 50d3e0e..eff2083 100644
--- a/monero-wallet-gui.pro
+++ b/monero-wallet-gui.pro
@@ -4,7 +4,10 @@ QT += qml quick widgets

 WALLET_ROOT=$$PWD/monero

-CONFIG += c++11
+CONFIG += c++11 link_pkgconfig
+packagesExist(libpcsclite) {
+    PKGCONFIG += libpcsclite
+}
 QMAKE_CXXFLAGS += -fPIC -fstack-protector
 QMAKE_LFLAGS += -fstack-protector

```


## rnhmjoj | 2018-03-31T17:49:28+00:00
Thanks, I'm trying it right now.

## iDunk5400 | 2018-03-31T19:36:13+00:00
#1236

## rnhmjoj | 2018-03-31T20:19:24+00:00
@iDunk5400 thank you

# Action History
- Created by: rnhmjoj | 2018-03-31T09:08:28+00:00
- Closed at: 2018-04-03T10:08:57+00:00
