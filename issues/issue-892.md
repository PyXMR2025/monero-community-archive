---
title: AES-NI not detected correctly
source_url: https://github.com/xmrig/xmrig/issues/892
author: mbehrsf
assignees: []
labels: []
created_at: '2018-12-08T02:20:07+00:00'
updated_at: '2018-12-08T02:37:32+00:00'
type: issue
status: closed
closed_at: '2018-12-08T02:25:42+00:00'
---

# Original Description
Hi there!
I have a Xeon E3-1230 CPU here, running xmrig built on debian 9. According to https://ark.intel.com/products/52271/Intel-Xeon-Processor-E3-1230-8M-Cache-3-20-GHz- , the CPU should support AES-NI. However, when I start xmrig, it shows that AES is disabled and Assembly is set to none:

 * ABOUT        XMRig/2.8.3 gcc/6.3.0
 * LIBS         libuv/1.9.1 OpenSSL/1.1.0j 
 * CPU          Intel(R) Xeon(R) CPU E31230 @ 3.20GHz (1) x64 -AES
 * CPU L2/L3    1.0 MB/8.0 MB
 * THREADS      4, cryptonight, av=1, donate=5%
 * ASSEMBLY     auto:none
 * POOL #1      <REMOVED> variant auto
 * COMMANDS     hashrate, pause, resume

The hashrate is <100 H/s.

I tried forcing AES with --av=1 and --av=2, but I get an "Illegal instructions" error. An identical setup is working fine with AES and assembly on Xeon E3-1230 V2 CPU that I have here.

# Discussion History
## mbehrsf | 2018-12-08T02:37:32+00:00
sorry, it seems AES-NI was disabled in the BIOS settings

# Action History
- Created by: mbehrsf | 2018-12-08T02:20:07+00:00
- Closed at: 2018-12-08T02:25:42+00:00
