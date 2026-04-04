---
title: Problem launching on Mac OS 10.14
source_url: https://github.com/monero-project/monero/issues/4625
author: xjmzx
assignees: []
labels: []
created_at: '2018-10-16T16:58:27+00:00'
updated_at: '2018-10-17T11:24:58+00:00'
type: issue
status: closed
closed_at: '2018-10-17T11:24:58+00:00'
---

# Original Description
Not sure whether caused by my installation procedure/system config or not.

- Downloaded the Mac 64bit gui binary 0.13.0.3 from downloads.getmonero.org 
- Checked the hash with GPG, looked good
- Replaced 0.12.3.0 with 0.13.0.3, clicked on the icon,
- OS tells me it's from unknown developer, OK that
- Then I get the error message below
- Tried on another computer running same OS version, get same results

<img width="1000" alt="screen shot 2018-10-16 at 11 31 17 pm" src="https://user-images.githubusercontent.com/1854925/47033542-b28b0900-d1a7-11e8-83fc-31563d04180a.png">

Process:               monero-wallet-gui [18722]
Path:                  /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
Identifier:            org.monero-project.monero-wallet-gui
Version:               0
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           monero-wallet-gui [18722]
User ID:               501

Date/Time:             2018-10-16 23:41:34.849 +0800
OS Version:            Mac OS X 10.14 (18A391)
Report Version:        12
Anonymous UUID:        E9530545-D3DA-E16D-E3CC-311EEDDF23D1

Sleep/Wake UUID:       8C4299FC-31E4-48A4-A8AF-B8A7E26201B8

Time Awake Since Boot: 120000 seconds
Time Since Wake:       23000 seconds

System Integrity Protection: enabled

Crashed Thread:        0

Exception Type:        EXC_CRASH (SIGABRT)
Exception Codes:       0x0000000000000000, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Termination Reason:    DYLD, [0x1] Library missing

Application Specific Information:
dyld: launch, loading dependent libraries

Dyld Error Message:
  Library not loaded: /usr/local/Cellar/openssl/1.0.2p/lib/libcrypto.1.0.0.dylib
  Referenced from: /Applications/monero-wallet-gui.app/Contents/Frameworks/libssl.1.0.0.dylib
  Reason: image not found

Binary Images:
       0x10c562000 -        0x10d14cff7 +org.monero-project.monero-wallet-gui (0) <DFDAF7C7-D396-394D-8B55-B386732697D9> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
       0x10d42a000 -        0x10d44cfff +libboost_serialization.dylib (0) <D3FEF731-E4CA-3FC3-A81C-81CB3F1A0E36> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_serialization.dylib
       0x10d464000 -        0x10d466fff +libhidapi.0.dylib (0) <A92130E2-B1F9-3F09-BE63-5386E4E9E252> /Applications/monero-wallet-gui.app/Contents/Frameworks/libhidapi.0.dylib
       0x10d46a000 -        0x10d478ff7 +libboost_thread-mt.dylib (0) <BA83C2D2-121D-3A6E-96CC-7362A6506427> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_thread-mt.dylib
       0x10d482000 -        0x10d484ffb +libboost_system.dylib (0) <8B938A2C-19B8-30B1-AE57-151E0400B505> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_system.dylib
       0x10d488000 -        0x10d48cfff +libboost_date_time.dylib (0) <9AE20BF4-E80D-3926-B61D-10A4F1E05A8D> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_date_time.dylib
       0x10d492000 -        0x10d4a0fff +libboost_filesystem.dylib (0) <272BF481-AF42-3FA2-B44D-828CF0B6F389> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_filesystem.dylib
       0x10d4a9000 -        0x10d548ff7 +libboost_regex.dylib (0) <D217762D-01CE-3F59-8497-AF919AAF1F91> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_regex.dylib
       0x10d57f000 -        0x10d582fff +libboost_chrono.dylib (0) <ED1F1F32-C901-3F63-B0B5-6BC17159833B> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_chrono.dylib
       0x10d586000 -        0x10d5b6fff +libboost_program_options.dylib (0) <22371C2D-A294-3545-801D-2EB35CC8D452> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_program_options.dylib
       0x10d5d3000 -        0x10d611fff +libssl.1.0.0.dylib (0) <4B800524-7AEB-3A76-A740-D6B70BE34554> /Applications/monero-wallet-gui.app/Contents/Frameworks/libssl.1.0.0.dylib
       0x10d62c000 -        0x10d667fef +libsodium.23.dylib (0) <C54406B9-C97D-39C7-B338-39C5E9C3D88B> /Applications/monero-wallet-gui.app/Contents/Frameworks/libsodium.23.dylib
       0x10d674000 -        0x10d7e8af7 +libcrypto.1.0.0.dylib (0) <81EE9FE4-56AD-333A-B447-C768F4A3A2F2> /Applications/monero-wallet-gui.app/Contents/Frameworks/libcrypto.1.0.0.dylib
       0x10d84f000 -        0x10db29fff +org.qt-project.QtQuick (5.7 - 5.7.0) <BE62D424-7627-3AC4-8ACD-31A68917E82F> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQuick.framework/Versions/5/QtQuick
       0x10dc02000 -        0x10df22fff +org.qt-project.QtQml (5.7 - 5.7.0) <C4665372-720D-3E1B-9878-49BFDD01DBF1> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQml.framework/Versions/5/QtQml
       0x10dfbc000 -        0x10e0c0ff7 +org.qt-project.QtNetwork (5.7 - 5.7.0) <B40B02F2-BD1A-3593-831A-6E9C83FA1D61> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtNetwork.framework/Versions/5/QtNetwork
       0x10e100000 -        0x10e614ff7 +org.qt-project.QtCore (5.7 - 5.7.0) <5F2F454C-CEE8-3E59-A3B7-94F51F5B9F96> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore
       0x10e6c2000 -        0x10eb22ff7 +org.qt-project.QtGui (5.7 - 5.7.0) <A41CBDE5-2955-3A57-BAE9-69001B210588> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtGui.framework/Versions/5/QtGui
       0x10ec13000 -        0x10f10cff7 +org.qt-project.QtWidgets (5.7 - 5.7.0) <9029D91F-7F7E-3DE0-BD66-FC91DD8112C3> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets
       0x10f267000 -        0x10f269ffb +libboost_system-mt.dylib (0) <463BE2E2-1649-3260-B284-90E5796FE04D> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_system-mt.dylib
       0x115e7e000 -        0x115efc6a7  dyld (625.13) <D6387150-2FB8-3066-868D-72E1B1C43982> /usr/lib/dyld
    0x7fff4a37a000 -     0x7fff4a37efff  com.apple.agl (3.3.2 - AGL-3.3.2) <81130C05-30AD-3BDA-BB9C-72ADDD5FAA2C> /System/Library/Frameworks/AGL.framework/Versions/A/AGL
    0x7fff4e418000 -     0x7fff4e867fff  com.apple.CoreFoundation (6.9 - 1555.10) <4A4C87BC-4C8E-392A-ABEE-824D4074C485> /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
    0x7fff505c9000 -     0x7fff505cefff  com.apple.DiskArbitration (2.7 - 2.7) <C53C1905-9BCF-3AE8-8BB3-C8A2C7DB7D25> /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
    0x7fff50e8a000 -     0x7fff50f1bfff  com.apple.framework.IOKit (2.0.2 - 1483.201.1) <DA4ED91F-2CC9-3CFD-9200-9D5D31EEE4F3> /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
    0x7fff58567000 -     0x7fff58576ff3  com.apple.opengl (17.0.37 - 17.0.37) <FA76EAA6-D035-3444-87F5-DD95446D651D> /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
    0x7fff58737000 -     0x7fff58741ff3  com.apple.pcsc (8.0 - 1) <221F377F-F384-3AE2-8FA2-230C5CEA4A7A> /System/Library/Frameworks/PCSC.framework/Versions/A/PCSC
    0x7fff785ab000 -     0x7fff785acff7  libDiagnosticMessagesClient.dylib (107) <C542CB3C-AA44-3D7F-B88C-79CC31B481AB> /usr/lib/libDiagnosticMessagesClient.dylib
    0x7fff7895d000 -     0x7fff7895effb  libSystem.B.dylib (1252.200.5) <D5133811-9D66-3DEB-9521-0A67347C9A54> /usr/lib/libSystem.B.dylib
    0x7fff78b98000 -     0x7fff78ba8ff3  libbsm.0.dylib (39.200.18) <5E5098D0-F7B2-32A1-8038-E709F6718D4E> /usr/lib/libbsm.0.dylib
    0x7fff78bb8000 -     0x7fff78c0fff7  libc++.1.dylib (400.9.4) <D4AB366F-48A9-3C7D-91BD-41198F69DD57> /usr/lib/libc++.1.dylib
    0x7fff78c10000 -     0x7fff78c25fff  libc++abi.dylib (400.17) <BA948A32-9024-3E55-98D4-18E31F6AED25> /usr/lib/libc++abi.dylib
    0x7fff79718000 -     0x7fff79718fff  libenergytrace.dylib (17.200.1) <D62ED169-B91C-3CCB-ADF5-E66AE4007B51> /usr/lib/libenergytrace.dylib
    0x7fff79873000 -     0x7fff79ad6ffb  libicucore.A.dylib (62107.0.1) <EAE6FC43-3AD2-3A53-9F7A-4E5E5F66D006> /usr/lib/libicucore.A.dylib
    0x7fff7a404000 -     0x7fff7ab8afe7  libobjc.A.dylib (750) <2E868147-8818-359E-8CD7-A8B80665928F> /usr/lib/libobjc.A.dylib
    0x7fff7b2e7000 -     0x7fff7b2f9ffb  libz.1.dylib (70.200.4) <99A3D725-8388-38B4-B66C-5E9006E6F072> /usr/lib/libz.1.dylib
    0x7fff7b36a000 -     0x7fff7b36eff3  libcache.dylib (81) <FE21A7E9-DBEB-33AC-836B-785AD036ACF4> /usr/lib/system/libcache.dylib
    0x7fff7b36f000 -     0x7fff7b379ff3  libcommonCrypto.dylib (60118.200.6) <78093D4F-91DB-35C8-981A-13375778B2E7> /usr/lib/system/libcommonCrypto.dylib
    0x7fff7b37a000 -     0x7fff7b381fff  libcompiler_rt.dylib (63.4) <A4D9CF37-D076-3CE9-95F1-DA89DA1601B6> /usr/lib/system/libcompiler_rt.dylib
    0x7fff7b382000 -     0x7fff7b38bff3  libcopyfile.dylib (146.200.3) <4BCDADBF-79F5-3829-B47D-64DA0D44BCBF> /usr/lib/system/libcopyfile.dylib
    0x7fff7b38c000 -     0x7fff7b410fff  libcorecrypto.dylib (602.200.50) <7AEC5B72-0B92-37E8-808B-6732DB714139> /usr/lib/system/libcorecrypto.dylib
    0x7fff7b496000 -     0x7fff7b4d0ff7  libdispatch.dylib (1008.200.78) <B8962879-AD55-3CF0-9B0A-5F1D57D1E14B> /usr/lib/system/libdispatch.dylib
    0x7fff7b4d1000 -     0x7fff7b500fff  libdyld.dylib (625.13) <4B16C209-83D4-3817-9B62-C2F7FFB23755> /usr/lib/system/libdyld.dylib
    0x7fff7b501000 -     0x7fff7b501ffb  libkeymgr.dylib (30) <A73AA788-C35C-3284-BFCA-95B1BBDF0CF3> /usr/lib/system/libkeymgr.dylib
    0x7fff7b502000 -     0x7fff7b50eff7  libkxld.dylib (4903.201.2) <EAF1CF8D-3843-33BE-8126-30994685B8F0> /usr/lib/system/libkxld.dylib
    0x7fff7b50f000 -     0x7fff7b50fff7  liblaunch.dylib (1336.201.2) <43E6698E-155E-3EAE-BAFF-CA5FCB35325C> /usr/lib/system/liblaunch.dylib
    0x7fff7b510000 -     0x7fff7b515fff  libmacho.dylib (917) <17BF7038-9C70-3EE1-9E96-3AE10D49669E> /usr/lib/system/libmacho.dylib
    0x7fff7b516000 -     0x7fff7b518ff3  libquarantine.dylib (86.200.11) <C70DA995-0D6E-302C-A15E-F7F03A3857B4> /usr/lib/system/libquarantine.dylib
    0x7fff7b519000 -     0x7fff7b51aff3  libremovefile.dylib (45.200.2) <D74A307B-3DC7-3992-B16C-DACB8207BE13> /usr/lib/system/libremovefile.dylib
    0x7fff7b51b000 -     0x7fff7b532ff3  libsystem_asl.dylib (356.200.4) <EC9D8AD4-E5CB-3765-804A-9E1E9DC045D2> /usr/lib/system/libsystem_asl.dylib
    0x7fff7b533000 -     0x7fff7b533fff  libsystem_blocks.dylib (73) <26419398-C30C-30F1-B656-A92AFA9560F6> /usr/lib/system/libsystem_blocks.dylib
    0x7fff7b534000 -     0x7fff7b5bcfff  libsystem_c.dylib (1272.200.26) <3DEEE96E-6DF6-35AD-8654-D69AC26B907B> /usr/lib/system/libsystem_c.dylib
    0x7fff7b5bd000 -     0x7fff7b5c0ff7  libsystem_configuration.dylib (963.200.27) <02CC3996-B34E-333C-8806-AE2699D34424> /usr/lib/system/libsystem_configuration.dylib
    0x7fff7b5c1000 -     0x7fff7b5c4ff7  libsystem_coreservices.dylib (66) <254B6849-2C8F-302C-8616-B8324A11AB30> /usr/lib/system/libsystem_coreservices.dylib
    0x7fff7b5c5000 -     0x7fff7b5cbffb  libsystem_darwin.dylib (1272.200.26) <974E9EF7-DE72-34B7-B056-0A81C10DF8EB> /usr/lib/system/libsystem_darwin.dylib
    0x7fff7b5cc000 -     0x7fff7b5d2ff7  libsystem_dnssd.dylib (878.200.35) <FFC665AA-B257-35AD-BD8B-32FD42C2EEC1> /usr/lib/system/libsystem_dnssd.dylib
    0x7fff7b5d3000 -     0x7fff7b61fff3  libsystem_info.dylib (517.200.9) <0707C387-D7DE-372E-8FF1-3DE5C91932D6> /usr/lib/system/libsystem_info.dylib
    0x7fff7b620000 -     0x7fff7b647ff7  libsystem_kernel.dylib (4903.201.2) <45FAA4C0-D553-34FD-ADF8-884886AE0D2A> /usr/lib/system/libsystem_kernel.dylib
    0x7fff7b648000 -     0x7fff7b693ff7  libsystem_m.dylib (3158.200.7) <43D1796B-954F-37D6-B1AC-9D80DF0655A2> /usr/lib/system/libsystem_m.dylib
    0x7fff7b694000 -     0x7fff7b6b8ff7  libsystem_malloc.dylib (166.200.60) <846F6898-117C-3427-A8FB-3772FFC2410B> /usr/lib/system/libsystem_malloc.dylib
    0x7fff7b6b9000 -     0x7fff7b6c4ffb  libsystem_networkextension.dylib (767.200.40) <F84D5474-4DC1-3E1A-AE00-8CE9593278B4> /usr/lib/system/libsystem_networkextension.dylib
    0x7fff7b6c5000 -     0x7fff7b6ccfff  libsystem_notify.dylib (172.200.21) <BCCB222F-DC64-3954-A836-DCCE6659CA5A> /usr/lib/system/libsystem_notify.dylib
    0x7fff7b6cd000 -     0x7fff7b6d6fef  libsystem_platform.dylib (177.200.16) <B75B04AD-69FE-3ADE-84D2-C17972FC8F49> /usr/lib/system/libsystem_platform.dylib
    0x7fff7b6d7000 -     0x7fff7b6e1fff  libsystem_pthread.dylib (330.201.1) <87A6B136-E423-3B6D-A58A-137F392D7D9D> /usr/lib/system/libsystem_pthread.dylib
    0x7fff7b6e2000 -     0x7fff7b6e5ff7  libsystem_sandbox.dylib (851.201.1) <FBA7E09B-F10F-3424-90EA-B4999B7FB461> /usr/lib/system/libsystem_sandbox.dylib
    0x7fff7b6e6000 -     0x7fff7b6e8ff7  libsystem_secinit.dylib (30.200.13) <CBEAB62B-F0A0-342F-9878-CADC14A3CB0D> /usr/lib/system/libsystem_secinit.dylib
    0x7fff7b6e9000 -     0x7fff7b6f0ff7  libsystem_symptoms.dylib (820.207.88) <B6E22FA8-0F7B-36FD-9D99-284056D3CB47> /usr/lib/system/libsystem_symptoms.dylib
    0x7fff7b6f1000 -     0x7fff7b706ff7  libsystem_trace.dylib (906.200.86) <7983ED77-18B5-39A5-BE19-AE4F2832ADEA> /usr/lib/system/libsystem_trace.dylib
    0x7fff7b708000 -     0x7fff7b70dffb  libunwind.dylib (35.4) <41222EF6-2233-3CF4-947A-15D48CB8C030> /usr/lib/system/libunwind.dylib
    0x7fff7b70e000 -     0x7fff7b73efff  libxpc.dylib (1336.201.2) <0A8747D1-33AA-37E1-B97A-BA9B95FE4E8C> /usr/lib/system/libxpc.dylib

Model: MacBookPro14,1, BootROM MBP141.0178.B00, 2 processors, Intel Core i5, 2.3 GHz, 8 GB, SMC 2.43f6
Graphics: Intel Iris Plus Graphics 640, Intel Iris Plus Graphics 640, Built-In
Memory Module: BANK 0/DIMM0, 4 GB, LPDDR3, 2133 MHz, 0x802C, 0x4D5435324C3531324D3332443250462D3039
Memory Module: BANK 1/DIMM0, 4 GB, LPDDR3, 2133 MHz, 0x802C, 0x4D5435324C3531324D3332443250462D3039
AirPort: spairport_wireless_card_type_airport_extreme (0x14E4, 0x170), Broadcom BCM43xx 1.0 (7.77.61.1 AirPortDriverBrcmNIC-1305.2)
Bluetooth: Version 6.0.8f6, 3 services, 18 devices, 1 incoming serial ports
Network Service: Wi-Fi, AirPort, en0
USB Device: USB 3.0 Bus
USB Device: Rugged Mini USB3
Thunderbolt Bus: MacBook Pro, Apple Inc., 37.1


# Discussion History
## moneromooo-monero | 2018-10-16T17:26:28+00:00
Looks like you're missing openssl. Install openssl.

## dEBRUYNE-1 | 2018-10-16T18:46:20+00:00
Temporary solution can be found here:

https://monero.stackexchange.com/questions/10364/gui-v0-13-0-3-does-not-start-on-mac-os-x-monero-wallet-gui-cannot-be-opened-bec

## xjmzx | 2018-10-17T09:02:15+00:00
Thanks. Problem solved!
Maybe it would be good to mention this on the download link page, until there is a workaround.

## moneromooo-monero | 2018-10-17T10:13:44+00:00
OpenSSL is in the README list of deps already.

## dEBRUYNE-1 | 2018-10-17T11:23:23+00:00
+resolved

# Action History
- Created by: xjmzx | 2018-10-16T16:58:27+00:00
- Closed at: 2018-10-17T11:24:58+00:00
