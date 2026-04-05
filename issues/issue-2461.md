---
title: Assertion '!empty()' failed
source_url: https://github.com/xmrig/xmrig/issues/2461
author: LegoLivesMatter
assignees: []
labels: []
created_at: '2021-06-28T10:39:33+00:00'
updated_at: '2022-07-06T14:19:32+00:00'
type: issue
status: closed
closed_at: '2022-07-06T14:19:32+00:00'
---

# Original Description
**Describe the bug**
When trying to run an XMRig benchmark with the `--submit` option, some assertion fails and XMRig aborts:

```
/usr/include/c++/11.1.0/bits/basic_string.h:1101: std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::front() [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference = char&]: Assertion '!empty()' failed.
```

**To Reproduce**
Run XMRig with `doas xmrig --bench=1M --submit`
(replace doas with sudo if needed)

**Expected behavior**
Benchmark runs normally and submits results once complete.

**Required data**
 - Miner log as text or screenshot
 ```
  * ABOUT        XMRig/6.12.2 gcc/11.1.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-4720HQ CPU @ 2.60GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       7.0/7.7 GB (92%)
                DIMM_A0: 4 GB DDR3 @ 1600 MHz 8KTF51264HZ-1G9N1
                ChannelA-DIMM1: <empty>
                DIMM_B0: 4 GB DDR3 @ 1600 MHz M471B5173EB0-YK0
                ChannelB-DIMM1: <empty>
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - X550JX
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-06-28 12:35:43.205]  bench    start benchmark hashes 1M algo rx/0
[2021-06-28 12:35:43.205]  cpu      use argon2 implementation AVX2
[2021-06-28 12:35:43.205]  msr      register values for "intel" preset have been set successfully (0 ms)
[2021-06-28 12:35:43.205]  randomx  init dataset algo rx/0 (8 threads) seed 0000000000000000...
[2021-06-28 12:35:43.343]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (138 ms)
[2021-06-28 12:35:47.457]  randomx  dataset ready (4114 ms)
[2021-06-28 12:35:47.458]  cpu      use profile  rx  (3 threads) scratchpad 2048 KB
[2021-06-28 12:35:47.460]  cpu      READY threads 3/3 (3) huge pages 100% 3/3 memory 6144 KB (2 ms)
[2021-06-28 12:35:47.674]  bench    seed c32d7e546d612065f6bc56f820093d990ecff257d3a4fdd0f5784e731df6026a
/usr/include/c++/11.1.0/bits/basic_string.h:1101: std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::front() [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference = char&]: Assertion '!empty()' failed.
Aborted
 ```
 - Config file or command line (without wallets)
 `xmrig --bench=1M --submit`
 - OS: Artix GNU/Linux

**Additional context**
None.


# Discussion History
## Spudz76 | 2021-06-28T19:12:12+00:00
Probably bleeding edge gcc 11 bugs

I wouldn't use newer than 10.2 for much of anything until gcc 12 is out :)

# Action History
- Created by: LegoLivesMatter | 2021-06-28T10:39:33+00:00
- Closed at: 2022-07-06T14:19:32+00:00
