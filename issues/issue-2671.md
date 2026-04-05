---
title: 'Submitting a benchmark causes xmrig to fail '
source_url: https://github.com/xmrig/xmrig/issues/2671
author: paypur
assignees: []
labels:
- bug
created_at: '2021-11-03T20:33:28+00:00'
updated_at: '2025-06-04T18:26:20+00:00'
type: issue
status: closed
closed_at: '2025-06-04T18:26:19+00:00'
---

# Original Description
```
$ sudo xmrig --bench=1M --submit
 * ABOUT        XMRig/6.15.3 gcc/11.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       14.3/15.6 GB (92%)
                ChannelA-DIMM1: <empty>
                DIMM_A2: 8 GB DDR4 @ 3333 MHz F4-2666C18-8GTZR    
                ChannelB-DIMM1: <empty>
                DIMM_B2: 8 GB DDR4 @ 3333 MHz F4-2666C18-8GTZR    
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - ROG STRIX Z370-F GAMING
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL 1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-03 13:28:10.479]  bench    start benchmark hashes 1M algo rx/0
[2021-11-03 13:28:10.479]  cpu      use argon2 implementation AVX2
[2021-11-03 13:28:10.479]  msr      register values for "intel" preset have been set successfully (1 ms)
[2021-11-03 13:28:10.479]  randomx  init dataset algo rx/0 (12 threads) seed 0000000000000000...
[2021-11-03 13:28:10.557]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (77 ms)
[2021-11-03 13:28:12.451]  randomx  dataset ready (1895 ms)
[2021-11-03 13:28:12.451]  cpu      use profile  rx  (6 threads) scratchpad 2048 KB
[2021-11-03 13:28:12.454]  cpu      READY threads 6/6 (6) huge pages 100% 6/6 memory 12288 KB (3 ms)
/usr/include/c++/11.1.0/bits/basic_string.h:1101: std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::front() [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference = char&]: Assertion '!empty()' failed.
Aborted
```

# Discussion History
## Spudz76 | 2021-11-04T03:41:37+00:00
Can't seem to duplicate on gcc 11.2.0

May be localized to 11.1.0

## wereii | 2025-03-07T11:59:18+00:00
Somehow, still applies on an up to date Arch and _fresh_ gcc, also no difference between the pre-built package and self-built.

```
> xmrig --submit --bench=1M
 * ABOUT        XMRig/6.22.2 gcc/14.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.50.0 OpenSSL/3.4.1 hwloc/2.12.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          13th Gen Intel(R) Core(TM) i9-13900KF (1) 64-bit AES
                L2:32.0 MB L3:36.0 MB 24C/32T NUMA:1
 * MEMORY       4.8/62.6 GB (8%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2025-03-07 12:54:36.648]  bench    start benchmark hashes 1M algo rx/0
[2025-03-07 12:54:36.648]  cpu      use argon2 implementation AVX2
[2025-03-07 12:54:36.654]  msr      cannot read MSR 0x000001a4
[2025-03-07 12:54:36.654]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2025-03-07 12:54:36.654]  randomx  init dataset algo rx/0 (32 threads) seed 0000000000000000...
[2025-03-07 12:54:36.715]  randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (60 ms)
[2025-03-07 12:54:37.624]  randomx  dataset ready (909 ms)
[2025-03-07 12:54:37.624]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2025-03-07 12:54:37.639]  cpu      READY threads 32/32 (32) huge pages 100% 32/32 memory 65536 KB (15 ms)
/usr/include/c++/14.2.1/bits/basic_string.h:1328: std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::front() [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; reference = char&]: Assertion '!empty()' failed.
[1]    21650 IOT instruction (core dumped)  xmrig --submit --bench=1M
```




E: Nevermind, building and running the xmrig binary directly works so it is probably a problem with packaging.


## EXtremeExploit | 2025-04-16T19:26:37+00:00
Problem is not related to packaging, happens on both release and debug builds, either running xmrig with the path or just the name

This is the stack trace vscode throws when trying to do a benchmark:

![Image](https://github.com/user-attachments/assets/8cb1301d-5b07-4b24-ab3d-699697d0f8cd)

```
libc.so.6![Unknown/Just-In-Time compiled code] (Unknown Source:0)
libc.so.6!raise (Unknown Source:0)
libc.so.6!abort (Unknown Source:0)
libstdc++.so.6!std::__glibcxx_assert_fail(const char * file, const char * file@entry, int line, int line@entry, const char * function, const char * function@entry, const char * condition, const char * condition@entry) (/usr/src/debug/gcc/gcc/libstdc++-v3/src/c++11/assert_fail.cc:41)
libstdc++.so.6!std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::front(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > * const this) (/usr/src/debug/gcc/gcc-build/x86_64-pc-linux-gnu/libstdc++-v3/include/bits/basic_string.h:1328)
xmrig::HttpWriteBaton::HttpWriteBaton(xmrig::HttpWriteBaton * this, std::string && body, xmrig::HttpContext * ctx) (/home/pedro/dev/xmrig/src/base/net/http/HttpContext.cpp:49)
xmrig::HttpContext::write(xmrig::HttpContext * this, std::string && data, bool close) (/home/pedro/dev/xmrig/src/base/net/http/HttpContext.cpp:110)
xmrig::HttpsClient::flush(xmrig::HttpsClient * this, bool close) (/home/pedro/dev/xmrig/src/base/net/https/HttpsClient.cpp:197)
xmrig::HttpsClient::read(xmrig::HttpsClient * this, const char * data, size_t size) (/home/pedro/dev/xmrig/src/base/net/https/HttpsClient.cpp:103)
xmrig::HttpClient::onConnect(uv_connect_s*, int)::$_0::operator()(uv_stream_s*, long, uv_buf_t const*) const(const class {...} * this, uv_stream_t * tcp, ssize_t nread, const uv_buf_t * buf) (/home/pedro/dev/xmrig/src/base/net/http/HttpClient.cpp:155)
xmrig::HttpClient::onConnect(uv_connect_s*, int)::$_0::__invoke(uv_stream_s*, long, uv_buf_t const*)(uv_stream_t * tcp, ssize_t nread, const uv_buf_t * buf) (/home/pedro/dev/xmrig/src/base/net/http/HttpClient.cpp:150)
libuv.so.1![Unknown/Just-In-Time compiled code] (Unknown Source:0)
libuv.so.1!uv_run (Unknown Source:0)
xmrig::App::exec(xmrig::App * this) (/home/pedro/dev/xmrig/src/App.cpp:89)
main(int argc, char ** argv) (/home/pedro/dev/xmrig/src/xmrig.cpp:36)
```

Keep in mind this problem happens sometimes, but it happens most of the time and seems to be networking related
Also if it doesnt happen at the start, it also has a very high chance of happening at the end of the benchmark, making it so that you need to run the benchmark multiple times until you get lucky enough to not get the error twice

## SChernykh | 2025-04-17T08:33:11+00:00
https://github.com/xmrig/xmrig/pull/3652 should fix it.

## EXtremeExploit | 2025-04-18T13:24:17+00:00
Nope, still happens on the dev branch

```
libc.so.6![Unknown/Just-In-Time compiled code] (Unknown Source:0)
libc.so.6!raise (Unknown Source:0)
libc.so.6!abort (Unknown Source:0)
libstdc++.so.6!std::__glibcxx_assert_fail(const char * file, const char * file@entry, int line, int line@entry, const char * function, const char * function@entry, const char * condition, const char * condition@entry) (/usr/src/debug/gcc/gcc/libstdc++-v3/src/c++11/assert_fail.cc:41)
libstdc++.so.6!std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::front(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > * const this) (/usr/src/debug/gcc/gcc-build/x86_64-pc-linux-gnu/libstdc++-v3/include/bits/basic_string.h:1328)
xmrig::HttpWriteBaton::HttpWriteBaton(xmrig::HttpWriteBaton * this, std::string && body, xmrig::HttpContext * ctx) (/home/pedro/dev/xmrig/src/base/net/http/HttpContext.cpp:49)
xmrig::HttpContext::write(xmrig::HttpContext * this, std::string && data, bool close) (/home/pedro/dev/xmrig/src/base/net/http/HttpContext.cpp:110)
xmrig::HttpsClient::flush(xmrig::HttpsClient * this, bool close) (/home/pedro/dev/xmrig/src/base/net/https/HttpsClient.cpp:197)
xmrig::HttpsClient::read(xmrig::HttpsClient * this, const char * data, size_t size) (/home/pedro/dev/xmrig/src/base/net/https/HttpsClient.cpp:103)
xmrig::HttpClient::onConnect(uv_connect_s*, int)::$_0::operator()(uv_stream_s*, long, uv_buf_t const*) const(const class {...} * this, uv_stream_t * tcp, ssize_t nread, const uv_buf_t * buf) (/home/pedro/dev/xmrig/src/base/net/http/HttpClient.cpp:155)
xmrig::HttpClient::onConnect(uv_connect_s*, int)::$_0::__invoke(uv_stream_s*, long, uv_buf_t const*)(uv_stream_t * tcp, ssize_t nread, const uv_buf_t * buf) (/home/pedro/dev/xmrig/src/base/net/http/HttpClient.cpp:150)
libuv.so.1![Unknown/Just-In-Time compiled code] (Unknown Source:0)
libuv.so.1!uv_run (Unknown Source:0)
xmrig::App::exec(xmrig::App * this) (/home/pedro/dev/xmrig/src/App.cpp:89)
main(int argc, char ** argv) (/home/pedro/dev/xmrig/src/xmrig.cpp:36)
```

![Image](https://github.com/user-attachments/assets/bf24d781-05d7-4bad-bbd9-2f3a4a3602f1)

## SChernykh | 2025-04-18T13:31:39+00:00
```
xmrig::HttpsClient::flush(xmrig::HttpsClient * this, bool close) (/home/pedro/dev/xmrig/src/base/net/https/HttpsClient.cpp:197)
```
This is an old line number for `HttpContext::write` call. You need to do a fresh build, you're running the old code.

## EXtremeExploit | 2025-04-18T13:38:44+00:00
The problem seems to be fixed, but a new less frequent error now appears:
```
[2025-04-18 10:36:46.155]  bench    benchmark failed: "Failed to verify benchmark start time, might be due high network latency."
```

I cant find the logic for this string in the miner so i guess its an error returned by the server, if its completely unrelated to this you can close the issue, thanks

# Action History
- Created by: paypur | 2021-11-03T20:33:28+00:00
- Closed at: 2025-06-04T18:26:19+00:00
