---
title: ld error with boost 1.71.0
source_url: https://github.com/monero-project/monero-gui/issues/2395
author: zordon13
assignees: []
labels:
- resolved
created_at: '2019-09-22T07:43:33+00:00'
updated_at: '2019-11-25T12:18:41+00:00'
type: issue
status: closed
closed_at: '2019-11-25T12:18:41+00:00'
---

# Original Description
`/usr/lib/gcc/x86_64-pc-linux-gnu/9.2.0/../../../../x86_64-pc-linux-gnu/bin/ld: device_trezor_base.cpp:(.text._ZN5boost16re_detail_10700012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10700012perl_matcherIPKcSaINS_9sub_matchIS3_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x64a): undefined reference to `boost::re_detail_107000::put_mem_block(void*)'
`
dev-libs/boost 1.71.0
dev-util/boost-build 1.71.0

System uname: Linux-5.2.14-gentoo-x86_64-AMD_Ryzen_5_2600_Six-Core_Processor-with-gentoo-2.6
KiB Mem:    16410848 total,  11668952 free
KiB Swap:          0 total,         0 free
Timestamp of repository gentoo: Sun, 22 Sep 2019 07:00:01 +0000
Head commit of repository gentoo: cb680a5e45d6569f2bc6017a19f36f4d187f56a3
sh bash 5.0_p11
ld GNU ld (Gentoo 2.32 p2) 2.32.0
app-shells/bash:          5.0_p11::gentoo
dev-java/java-config:     2.2.0-r4::gentoo
dev-lang/perl:            5.30.0::gentoo
dev-lang/python:          2.7.16::gentoo, 3.6.9::gentoo, 3.7.4-r1::gentoo
dev-util/cmake:           3.15.3::gentoo
dev-util/pkgconfig:       0.29.2::gentoo
sys-apps/baselayout:      2.6-r1::gentoo
sys-apps/sandbox:         2.18::gentoo
sys-devel/autoconf:       2.13-r1::gentoo, 2.69-r4::gentoo
sys-devel/automake:       1.13.4-r2::gentoo, 1.15.1-r2::gentoo, 1.16.1-r1::gentoo
sys-devel/binutils:       2.30-r4::gentoo, 2.31.1-r4::gentoo, 2.32-r1::gentoo
sys-devel/gcc:            8.2.0-r6::gentoo, 8.3.0-r1::gentoo, 9.1.0-r1::gentoo, 9.2.0::gentoo
sys-devel/gcc-config:     2.1::gentoo
sys-devel/libtool:        2.4.6-r5::gentoo
sys-devel/make:           4.2.1-r4::gentoo
sys-kernel/linux-headers: 5.3::gentoo (virtual/os-headers)
sys-libs/glibc:           2.29-r5::gentoo


# Discussion History
## dEBRUYNE-1 | 2019-11-25T08:57:06+00:00
Can you check whether this issue is still present with the GUI v0.15.0.1 tag? 

## zordon13 | 2019-11-25T10:04:00+00:00
> Can you check whether this issue is still present with the GUI v0.15.0.1 tag?

build ok


## dEBRUYNE-1 | 2019-11-25T12:14:00+00:00
Going to mark this as resolved then.

## dEBRUYNE-1 | 2019-11-25T12:14:05+00:00
+resolved

# Action History
- Created by: zordon13 | 2019-09-22T07:43:33+00:00
- Closed at: 2019-11-25T12:18:41+00:00
