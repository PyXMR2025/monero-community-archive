---
title: 'regression: seg fault after upgrading from v2.13.1 to v2.14.0'
source_url: https://github.com/xmrig/xmrig/issues/975
author: csquaredphd
assignees: []
labels:
- bug
created_at: '2019-03-07T02:41:00+00:00'
updated_at: '2019-03-19T02:51:43+00:00'
type: issue
status: closed
closed_at: '2019-03-19T02:51:43+00:00'
---

# Original Description
After upgrading to v2.14.0 without changing anything else, the program crashes immediately.  The same setup works fine with v2.13.1.  Running on Ubuntu 16.04.

```
$ ./xmrig -c config_1T_double.json
 * ABOUT        XMRig/2.14.0 gcc/5.4.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1a microhttpd/0.9.62 
 * CPU          Intel(R) Core(TM) i5-7600K CPU @ 3.80GHz (1) x64 AES AVX2
 * CPU L2/L3    1.0 MB/6.0 MB
 * THREADS      1, cryptonight, donate=1%
 * ASSEMBLY     auto:intel
 * POOL #1      ca.minexmr.com:6666 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-03-06 21:18:12] use pool ca.minexmr.com:6666 TLSv1.2 158.69.25.77 
[2019-03-06 21:18:12] new job from ca.minexmr.com:6666 diff 35000 algo cn/2 height 1786123
Segmentation fault (core dumped)
```

Disassembly:

```
 => 0x5b6210 <cnv2_rwz_double_mainloop_asm+400>:	movdqu (%r8),%xmm11
    0x5b6215 <cnv2_rwz_double_mainloop_asm+405>:	punpcklqdq %xmm0,%xmm5
    0x5b6219 <cnv2_rwz_double_mainloop_asm+409>:	lea    (%rdx,%r13,1),%r9
    0x5b621d <cnv2_rwz_double_mainloop_asm+413>:	movdqu (%r9),%xmm15
    0x5b6222 <cnv2_rwz_double_mainloop_asm+418>:	nopw   %cs:0x0(%rax,%rax,1)
    0x5b622c <cnv2_rwz_double_mainloop_asm+428>:	nopw   %cs:0x0(%rax,%rax,1)
    0x5b6236 <cnv2_rwz_double_mainloop_asm+438>:	nopw   %cs:0x0(%rax,%rax,1)
    0x5b6240 <cnv2_rwz_double_mainloop_asm+448>:	movdqu %xmm15,%xmm9
    0x5b6245 <cnv2_rwz_double_mainloop_asm+453>:	mov    %edx,%eax
    0x5b6247 <cnv2_rwz_double_mainloop_asm+455>:	mov    %edx,%ebx
    0x5b6249 <cnv2_rwz_double_mainloop_asm+457>:	xor    $0x10,%eax
    0x5b624c <cnv2_rwz_double_mainloop_asm+460>:	xor    $0x20,%ebx
    0x5b624f <cnv2_rwz_double_mainloop_asm+463>:	xor    $0x30,%edx
    0x5b6252 <cnv2_rwz_double_mainloop_asm+466>:	movq   %r11,%xmm0
    0x5b6257 <cnv2_rwz_double_mainloop_asm+471>:	movq   %r10,%xmm2
    0x5b625c <cnv2_rwz_double_mainloop_asm+476>:	punpcklqdq %xmm0,%xmm2
```

Here is my thread config:
```
    "threads": [
        {
            "low_power_mode": 2,
            "affine_to_cpu": false,
            "asm": true
        }
```

It runs fine on v2.14.0 if I change "low_power_mode" to either 1 or 3.


# Discussion History
## xmrig | 2019-03-07T07:55:39+00:00
Fixed in master branch, v2.14.1 will be released soon.
Thank you.

## xmrig | 2019-03-07T08:40:25+00:00
Done https://github.com/xmrig/xmrig/releases/tag/v2.14.1

## DeadManWalkingTO | 2019-03-07T14:15:47+00:00
Solved!

## csquaredphd | 2019-03-12T02:04:44+00:00
Yes, resolved for me in v2.14.1.  Thanks!

## DeadManWalkingTO | 2019-03-19T02:06:07+00:00
I think this issue can be closed.
Thank you!

# Action History
- Created by: csquaredphd | 2019-03-07T02:41:00+00:00
- Closed at: 2019-03-19T02:51:43+00:00
