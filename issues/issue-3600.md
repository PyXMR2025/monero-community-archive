---
title: monero-wallet-gui are not running after upgrading to Linux 5.12.13
source_url: https://github.com/monero-project/monero-gui/issues/3600
author: vdrobysh
assignees: []
labels: []
created_at: '2021-06-30T17:08:39+00:00'
updated_at: '2021-07-06T15:50:13+00:00'
type: issue
status: closed
closed_at: '2021-07-06T15:50:13+00:00'
---

# Original Description
$ ./monero-wallet-gui 
./monero-wallet-gui: error while loading shared libraries: libicui18n.so.55: cannot open shared object file: No such file or directory

$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/monero-wallet-gui/libs/
sed: /opt/monero-wallet-gui/libs/libselinux.so.1: no version information available (required by sed)

$ ./monero-wallet-gui 
./monero-wallet-gui: symbol lookup error: /opt/monero-wallet-gui/libs/librt.so.1: undefined symbol: __clock_nanosleep, version GLIBC_PRIVATE
sed: /opt/monero-wallet-gui/libs/libselinux.so.1: no version information available (required by sed)

The Monero GUI's version is latest.

# Discussion History
## selsta | 2021-06-30T17:09:26+00:00
Which OS?

## vdrobysh | 2021-06-30T17:27:21+00:00
Fedora 34

The kernel is 5.12.13-300

## selsta | 2021-06-30T22:13:45+00:00
Is this self compiled? If yes you have to rebuild it.

## vdrobysh | 2021-07-01T05:31:47+00:00
qt5.15.2 is not working for rebuilding
[100%] Linking CXX executable ../bin/monero-wallet-gui
/usr/bin/ld: ../external/libquirc.a(decode.c.o): relocation R_X86_64_32S against symbol `quirc_version_db' can not be used when making a PIE object; recompile with -fPIE
/usr/bin/ld: ../external/libquirc.a(identify.c.o): relocation R_X86_64_32 against `.rodata' can not be used when making a PIE object; recompile with -fPIE
/usr/bin/ld: ../external/libquirc.a(quirc.c.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a PIE object; recompile with -fPIE
collect2: error: ld returned 1 exit status

I will try again after installing qt5.9.7.

## selsta | 2021-07-01T14:07:38+00:00
Try again with `Qt 5.15.2` and the following diff:

```
diff --git a/external/CMakeLists.txt b/external/CMakeLists.txt
index c99cd900..e711b635 100644
--- a/external/CMakeLists.txt
+++ b/external/CMakeLists.txt
@@ -4,4 +4,5 @@ add_library(quirc STATIC
     quirc/lib/quirc.c
     quirc/lib/version_db.c
 )
+set_target_properties(quirc PROPERTIES POSITION_INDEPENDENT_CODE ON)
 target_include_directories(quirc PUBLIC quirc/lib)
```

## vdrobysh | 2021-07-01T16:33:58+00:00
That worked! Thank you.

# Action History
- Created by: vdrobysh | 2021-06-30T17:08:39+00:00
- Closed at: 2021-07-06T15:50:13+00:00
