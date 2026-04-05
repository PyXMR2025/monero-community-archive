---
title: '[BUG] break by uv__fs_done'
source_url: https://github.com/xmrig/xmrig/issues/2800
author: ftitreefly
assignees: []
labels:
- bug
created_at: '2021-12-07T15:08:13+00:00'
updated_at: '2025-06-16T20:26:38+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:26:38+00:00'
---

# Original Description
[2021-12-07 18:51:41.677]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-12-07 18:51:41.677]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2021-12-07 18:51:41.677]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)
**Assertion failed: (uv__has_active_reqs(req->loop)), function uv__fs_done, file src/unix/fs.c, line 1666.**
[1]    13963 abort      sudo ./xmrig -c config-rap.json

# Discussion History
## ghost | 2022-01-04T17:58:54+00:00
Looks like same (or similar) here:
User is running a self-built xmrig in Kubernetes non-privileged container.

```
 * ABOUT        XMRig/6.16.2-mo2 gcc/9.3.1
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 3900X 12-Core Processor (0) 64-bit AES
                L2:0.0 MB L3:0.0 MB 0C/24T NUMA:1
 * MEMORY       0.1/1.0 GB (6%)
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      gulf.moneroocean.stream:10512 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
```

## pod A

```
[2022-01-04 15:48:37.538]  miner    speed 10s/60s/15m 3611.8 2811.6 1582.5 H/s max 4608.0 H/s avg 1390.5 H/s
[2022-01-04 15:48:47.023]  net      new job from gulf.moneroocean.stream:10512 diff 40837 algo ghostrider height 220368
[2022-01-04 15:48:47.024]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2022-01-04 15:48:47.024]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2022-01-04 15:48:47.024]  cpu      GhostRider algo 3: cn/dark (512 KB)
[2022-01-04 15:48:58.843]  net      new job from gulf.moneroocean.stream:10512 diff 40837 algo ghostrider height 220369
[2022-01-04 15:48:58.844]  cpu      GhostRider algo 1: cn/fast (2 MB)
xmrig: src/unix/fs.c:1720: uv__fs_done: Assertion `((req->loop)->active_reqs.count > 0)' failed.
[2022-01-04 15:48:58.844]  cpu      GhostRider algo 2: cn/lite (1 MB)
[2022-01-04 15:48:58.844]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)
```

## pod B

```
[2022-01-04 13:58:59.321]  miner    speed 10s/60s/15m 690.7 691.0 1320.4 H/s max 5038.4 H/s avg 1480.1 H/s
[2022-01-04 13:59:59.433]  miner    speed 10s/60s/15m 695.2 695.3 1304.0 H/s max 5038.4 H/s avg 1452.8 H/s
[2022-01-04 14:00:00.042]  cpu      accepted (1148/0) diff 38166 (420 ms)
[2022-01-04 14:00:36.933]  cpu      accepted (1149/0) diff 38166 (531 ms)
[2022-01-04 14:00:49.742]  cpu      accepted (1150/0) diff 38166 (421 ms)
[2022-01-04 14:00:59.548]  miner    speed 10s/60s/15m 695.0 694.3 1287.7 H/s max 5038.4 H/s avg 1427.2 H/s
[2022-01-04 14:01:02.269]  net      new job from gulf.moneroocean.stream:10512 diff 37640 algo ghostrider height 220314
[2022-01-04 14:01:02.270]  cpu      GhostRider algo 1: cn/lite (1 MB)
xmrig: src/unix/fs.c:1720: uv__fs_done: Assertion `((req->loop)->active_reqs.count > 0)' failed.
[2022-01-04 14:01:02.270]  cpu      GhostRider algo 2: cn/dark-lite (256 KB)
[2022-01-04 14:01:02.270]  cpu      GhostRider algo 3: cn/dark (512 KB)
```

## koitsu | 2023-07-27T22:37:30+00:00
Seen this same problem on Ghostrider (for the first time!)

```
[2023-07-27 04:29:16.649]  miner    speed 10s/60s/15m 235.7 184.3 209.6 H/s max 795.0 H/s avg 163.8 H/s
[2023-07-27 04:29:24.055]  net      new job from ghostrider.mine.zergpool.com:15354 diff 16384 algo ghostrider height 56678
[2023-07-27 04:29:57.268]  net      new job from ghostrider.mine.zergpool.com:15354 diff 16384 algo ghostrider height 56679
[2023-07-27 04:29:57.286]  cpu      GhostRider algo 1: cn/turtle-lite (128 KB)
[2023-07-27 04:29:57.286]  cpu      GhostRider algo 2: cn/dark (512 KB)
[2023-07-27 04:29:57.286]  cpu      GhostRider algo 3: cn/turtle (256 KB)
xmrig: src/unix/fs.c:1773: uv__fs_done: Assertion `uv__has_active_reqs(req->loop)' failed.
Aborted
```

XMRig details if you need it.  Host is running Ubuntu 20.04.6 LTS (focal); no containers, just straight bare metal.

```
 * ABOUT        XMRig/6.20.0 gcc/9.4.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz (1) 64-bit AES
                L2:0.5 MB L3:4.0 MB 2C/4T NUMA:1
 * MEMORY       0.7/15.4 GB (5%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+ssl://ghostrider.mine.zergpool.com:15354 algo ghostrider
 * POOL #2      stratum+ssl://us-west.flockpool.com:5555 algo ghostrider
 * POOL #3      stratum+ssl://rx-us.unmineable.com:443 algo rx/0
 * POOL #4      stratum+ssl://rx-us.unmineable.com:443 algo rx/0
 * POOL #5      stratum+ssl://us.arqma.herominers.com:1143 algo rx/arq
 * POOL #6      stratum+ssl://pool.hashvault.pro:443 algo cn/half
 * POOL #7      stratum+ssl://us.qrl.herominers.com:1166 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
```
Please note only the first pool (POOL 1) is enabled.  All others are disabled.

## koitsu | 2023-12-28T01:53:24+00:00
I've now seen this (intermittently) for several months, always the same line of code / assertion.

@SChernykh Is there anything we can do to help fix this?  I'm happy to try dev/debug builds if needed.


## SChernykh | 2023-12-28T07:32:40+00:00
Did you enable logging to a file in config.json?

## koitsu | 2023-12-28T09:56:48+00:00
> Did you enable logging to a file in config.json?

No; I currently run XMRig under GNU screen.  Did you want me to use `log-file` to write things to a file?  What about `verbose`?

## SChernykh | 2023-12-28T11:08:56+00:00
No, I was just wondering if it was related because `uv__fs_done` is a file operation. I'll try to reproduce this bug without log-file.

## koitsu | 2023-12-28T11:36:59+00:00
Thanks.  For me this issue happens randomly -- sometimes takes hours, sometimes days/weeks.  If there was a version of XMRig "focal" (and libuv) built with debug symbols that I could run, I'd launch XMRig under gdb and wait until the issue happened.  But as it stands I literally cannot determine what the cause of this is.

libuv code in question is https://github.com/libuv/libuv/blob/v1.44.2/src/unix/fs.c#L1769-L1781 but it's too abstracted and too deep to determine what exactly in XMRig invoked this function.

If you need my config.json it's below; xmrig itself not invoked with any flags.
```
{
    "autosave": false,
    "watch": false,
    "dmi": false,
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "cpu": {
        "enabled": true,
        "priority": null,
        "asm": true,
        "argon2": [0, 1],
        "cn/half": [0, 1],
        "cn-heavy/xhv": [0, 1],
        "rx": [0, 1],
        "rx/wow": [0, 1],
        "ghostrider": [[8, 0], [8, 1]]
    },
    "randomx": {
        "1gb-pages": true
    },
    "pools": [
        {
            "enabled": true,
            "sni": true,
            "algo": "gr",
            "url": "stratum+ssl://ghostrider.mine.zergpool.com:15354",
            "user": "XXX",
            "pass": "XXX"
        },
        {
            "enabled": false,
            "sni": true,
            "algo": "gr",
            "url": "stratum+ssl://us-west.flockpool.com:5555",
            "user": "XXX",
            "pass": "XXX"
        },
        {
            "enabled": false,
            "sni": true,
            "algo": "rx/0",
            "url": "stratum+ssl://rx-us.unmineable.com:443",
            "user": "XXX",
            "pass": "XXX"
        },
        {
            "enabled": false,
            "sni": true,
            "algo": "rx/0",
            "url": "stratum+ssl://rx-us.unmineable.com:443",
            "user": "XXX",
            "pass": "XXX"
        }
    ]
}
```


## koitsu | 2024-02-26T20:37:16+00:00
I go through this multiple times a week on my Linux-based rig running Ubuntu 20.04.6 LTS (focal) on x64.

Because this is SIGABRT (abort() induced by an assert), it is not possible to use a simple shell script to auto-restart XMRig; the process tree is killed and you are left dead in the water (i.e. `while true; do sudo xmrig ...; sleep 5; done` will never hit the `sleep`).

This is a very nasty bug that I wish I could help debug.  I honestly would have run this through gdb and strace by now if XMRig was built with debug symbols and libuv debugging was enabled, but because there are no instructions on building XMRig + its dependencies, I can't do the work to make that happen.

My going theory is that `src/unix/fs.c` in libuv **may** be used for certain kinds of file descriptor I/O, despite the filename.  But it is a theory and not supported by hard evidence.

## SChernykh | 2024-02-26T20:47:10+00:00
> there are no instructions on building XMRig + its dependencies

There are: https://xmrig.com/docs/miner/build/ubuntu

## koitsu | 2024-02-27T07:20:22+00:00
> > there are no instructions on building XMRig + its dependencies
> 
> There are: https://xmrig.com/docs/miner/build/ubuntu

Thanks -- was not aware of this document!  I'm making progress on this (building binary via Docker to make my life easier).  Will report back when I have more info.

## koitsu | 2024-02-27T09:54:29+00:00
Managed to a debug binary built after a bit of hacking up various files.  Used Docker to do the build so the environment was 100% clean (source image via `FROM ubuntu:focal`):
```
$ ls -l /tmp/xmrig-20240227T011328
-rwxr-xr-x 1 jdc users 55111232 Feb 27 01:18 /tmp/xmrig-20240227T011328
$ /tmp/xmrig-20240227T011328 --version
XMRig 6.21.1
 built on Feb 27 2024 with GCC 9.4.0
 features: 64-bit AES

libuv/1.44.2
OpenSSL/1.1.1s
hwloc/2.9.0
$ file /tmp/xmrig-20240227T011328
/tmp/xmrig-20240227T011328: ELF 64-bit LSB pie executable, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1c53e668dad93e21b10c6ea8eb70c0f26e3dba88, for GNU/Linux 3.2.0, with debug_info, not stripped
$ objdump -x /tmp/xmrig-20240227T011328 | grep fs_done
00000000007749eb l     F .text  00000000000000b2              uv__fs_done
```
I'll work on getting this into place and see what happens.  What I suspect is that `uv__fs_done()`, despite living in libuv `fs.c`, is actually used for anything relating to file descriptor events, which would include sockets.  But I am not sure as I'm not libuv-savvy.

My hope is to run this under gdb and then get a full backtrace.  It's clear people HAVE managed to get backtraces on SIGABRT before, so we'll see.

## koitsu | 2024-02-27T22:11:11+00:00
Well that didn't take long.  However, this is in different code, so I think this may be a different problem.  @SChernykh Let me know if you want me to file a separate bug on this one (although it blocks me from analysing the libuv problem).  I can provide `bt full` output if needed too, but I suspect it may contain sensitive info (wallet addresses etc.).

The way this binary was built required two changes:

1. `scripts/build.uv.sh` modified to forced CFLAGS to ensure no optimisation and full debugging:
```
-./configure --disable-shared
+CFLAGS="-ggdb -g3 -O0" ./configure --disable-shared
```
2. Use of `cmake .. -DXMRIG_DEPS=scripts/deps -DCMAKE_BUILD_TYPE=Debug` to ensure nothing in CMake built this as a "release".
  * Note: libuv 1.44.2 contains a bug in their autogen.sh shell script where they used `==` as the comparison operator instead of `=`.  This was fixed in 1.45.0.
* Actual fix: https://github.com/libuv/libuv/commit/c880de3004ac31fde42129ff069a58d67013b8bd
* Comparison: https://github.com/libuv/libuv/compare/v1.44.2...v1.45.0
You can see this bug if you pay close attention to the libuv build process -- note the test operator failing:
```
...
  1150K .......... .......... .......... .......... .......... 54.8M
  1200K .......... .......... .......... .......... .......... 6.97M
  1250K .......... .......... ........                         14.2M=0.2s

2024-02-27 07:01:06 (7.13 MB/s) - 'v1.44.2.tar.gz' saved [1309062]

autogen.sh: 20: [: dev: unexpected operator
+ libtoolize --copy --force
libtoolize: putting auxiliary files in '.'.
libtoolize: copying file './ltmain.sh'
...
```

Anyway, here's the backtrace:

```
[2024-02-27 05:32:36.518]  net      new job from ghostrider.mine.zergpool.com:15354 diff 16384 algo ghostrider height 122863
[2024-02-27 05:32:50.778]  net      dev donate started
xmrig-20240227T011328: /root/xmrig/src/3rdparty/rapidjson/document.h:1231: rapidjson::GenericValue<Encoding, Allocator>& rapidjson::GenericValue<Encoding, Allocator>::operator[](const rapidjson::GenericValue<Encoding, SourceAllocator>&) [with SourceAllocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>]: Assertion `false' failed.

Thread 1 "xmrig-20240227T" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7c7a859 in __GI_abort () at abort.c:79
#2  0x00007ffff7c7a729 in __assert_fail_base (fmt=0x7ffff7e10588 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=0x555555e71586 "false",
    file=0x555555e70ed8 "/root/xmrig/src/3rdparty/rapidjson/document.h", line=1231, function=<optimized out>) at assert.c:92
#3  0x00007ffff7c8bfd6 in __GI___assert_fail (assertion=0x555555e71586 "false", file=0x555555e70ed8 "/root/xmrig/src/3rdparty/rapidjson/document.h", line=1231,
    function=0x555555e71430 "rapidjson::GenericValue<Encoding, Allocator>& rapidjson::GenericValue<Encoding, Allocator>::operator[](const rapidjson::GenericValue<Encoding, SourceAllocator>&) [with SourceAllocator = rapidjson::Mem"...) at assert.c:101
#4  0x00005555559030c0 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> > (this=0x55555629d338, name=...) at /root/xmrig/src/3rdparty/rapidjson/document.h:1231
#5  0x0000555555902367 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<char const> (this=0x55555629d338,
    name=0x555555e76373 "job") at /root/xmrig/src/3rdparty/rapidjson/document.h:1211
#6  0x000055555591a189 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<char const> (this=0x55555629d338,
    name=0x555555e76373 "job") at /root/xmrig/src/3rdparty/rapidjson/document.h:1214
#7  0x00005555559154df in xmrig::Client::parseResponse (this=0x555556238790, id=1, result=..., error=...) at /root/xmrig/src/base/net/stratum/Client.cpp:847
#8  0x0000555555914d77 in xmrig::Client::parse (this=0x555556238790, line=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", len=123)
    at /root/xmrig/src/base/net/stratum/Client.cpp:730
#9  0x000055555591658f in xmrig::Client::onLine (this=0x555556238790, line=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=123)
    at /root/xmrig/src/base/net/stratum/Client.h:81
#10 0x00005555559360fd in xmrig::LineReader::getline (this=0x555556238c38, data=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=124)
    at /root/xmrig/src/base/net/tools/LineReader.cpp:92
#11 0x0000555555935f0c in xmrig::LineReader::parse (this=0x555556238c38, data=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=124)
    at /root/xmrig/src/base/net/tools/LineReader.cpp:43
#12 0x0000555555b4ecc3 in xmrig::Client::Tls::read (this=0x555556256240, data=0x7ffff53b8038 "\027\003\003", size=146) at /root/xmrig/src/base/net/stratum/Tls.cpp:134
#13 0x00005555559157d3 in xmrig::Client::read (this=0x555556238790, nread=146, buf=0x7fffffffb0e0) at /root/xmrig/src/base/net/stratum/Client.cpp:905
#14 0x0000555555915cef in xmrig::Client::onRead (stream=0x7fffe8009cc0, nread=146, buf=0x7fffffffb0e0) at /root/xmrig/src/base/net/stratum/Client.cpp:1056
#15 0x0000555555cd4d4c in uv__read (stream=0x7fffe8009cc0) at src/unix/stream.c:1201
#16 0x0000555555cd5052 in uv__stream_io (loop=0x55555616cd80 <default_loop_struct>, w=0x7fffe8009d48, events=1) at src/unix/stream.c:1270
#17 0x0000555555ce01ea in uv__io_poll (loop=0x55555616cd80 <default_loop_struct>, timeout=232) at src/unix/epoll.c:374
#18 0x0000555555cc3643 in uv_run (loop=0x55555616cd80 <default_loop_struct>, mode=UV_RUN_DEFAULT) at src/unix/core.c:406
#19 0x0000555555a08cb5 in xmrig::App::exec (this=0x7fffffffe4d0) at /root/xmrig/src/App.cpp:90
#20 0x0000555555a228df in main (argc=3, argv=0x7fffffffe628) at /root/xmrig/src/xmrig.cpp:36
(gdb)
```

## koitsu | 2024-02-27T22:35:26+00:00
BTW, for the above backtrace: it looks to me like some server is returning mangled (partial) JSON and causes rapidjson to barf with an abort(), OR, that some part of the I/O handling has a bug and is getting a short read.  I suspect it's the former, with the JSON blob being returned as:
```
{"id"
```
And nothing more.

We can tell that at frame 11 the size/length of the buffer is 124, and at frame 9 the size/length is 123 (that's fine, probably a newline removed or relates to a trailing NULL or the like).

Let's examine data in frame 8, and then the internal XMRig structures in frame 13 to see what server XMRig was talking to (hard to tell from the XMRig output because it was doing a dev donation at the same time):
```
(gdb) f 8
#8  0x0000555555914d77 in xmrig::Client::parse (this=0x555556238790, line=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", len=123)
    at /root/xmrig/src/base/net/stratum/Client.cpp:730
730     in /root/xmrig/src/base/net/stratum/Client.cpp
(gdb) p line
$1 = 0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id"
(gdb) f 13
#13 0x00005555559157d3 in xmrig::Client::read (this=0x555556238790, nread=146, buf=0x7fffffffb0e0) at /root/xmrig/src/base/net/stratum/Client.cpp:905
905     in /root/xmrig/src/base/net/stratum/Client.cpp
(gdb) p this->m_ip
$2 = {m_data = 0x555556256e80 "199.247.27.41", m_size = 13}
(gdb) p this->m_sendBuf
$3 = {<std::_Vector_base<char, std::allocator<char> >> = {
    _M_impl = {<std::allocator<char>> = {<__gnu_cxx::new_allocator<char>> = {<No data fields>}, <No data fields>}, <std::_Vector_base<char, std::allocator<char> >::_Vector_impl_data> = {
        _M_start = 0x5555561f9670 "{\"id\":1,\"jsonrpc\":\"2.0\",\"method\":\"login\",\"params\":{\"login\":\"6eac04ac520eeb0caf8bf2dc27e59be7339e2cd823ff71da26d8afd9422f00f8\",\"pass\":\"x\",\"agent\":\"XMRig/6.21.1 (Linux x86_64) libuv/1.44.2 gcc/9.4.0\",\"a"..., _M_finish = 0x5555561f9a70 "", _M_end_of_storage = 0x5555561f9a70 ""}, <No data fields>}}, <No data fields>}
```
```
$ host ghostrider.mine.zergpool.com
ghostrider.mine.zergpool.com has address 103.249.70.7
$ host donate.v2.xmrig.com
donate.v2.xmrig.com has address 178.128.242.134
donate.v2.xmrig.com has address 199.247.27.41
```
And here we see it's not Zergpool which is doing this, it's the XMRig dev donation server.

I cannot do packet captures to analyse the payload either because TLS is being used.  (I can disable TLS for Zergpool of course, but I cannot for this dev donation server).

## SChernykh | 2024-02-27T22:41:57+00:00
https://github.com/xmrig/xmrig/pull/3431 should fix the direct reason of this crash callstack. Accessing the non-existent `job` object in release could probably result in some random crash in uv__fs_done later.

## koitsu | 2024-02-27T22:52:14+00:00
> #3431 should fix the direct reason of this crash callstack. Accessing the non-existent `job` object in release could probably result in some random crash in uv__fs_done later.

I don't think this will fix the problem?  The call stack clearly shows `xmrig::Client::parseResponse()` involved here, not `xmrig::Client::parseLogin()`.  `xmrig::Client::parseLogin()` calls `setRpcId(Json::getString(result, "id"))` which means the JSON parser is invoked and trying to parse out something that it can't because the JSON blob read into the in-memory buffer is bad/incorrect.

What needs to be done here is proper error handling in the JSON parser.  An assert/abort() should not EVER kick in when bogus JSON is returned from a server, unless rapidjson does not have a way to validate JSON (if it doesn't, then that library is junk).

## koitsu | 2024-02-27T22:53:38+00:00
https://rapidjson.org/group___r_a_p_i_d_j_s_o_n___e_r_r_o_r_s.html needs to be implemented all over the place, specifically use of `rapidjson::ParseResult()`


## koitsu | 2024-02-27T23:17:27+00:00
@SChernykh If you really think this is the problem, I can build a new binary with #3431 in place (just a simple `git pull` for me) and let things run again.  Let me know.

## SChernykh | 2024-02-27T23:52:15+00:00
> The call stack clearly shows xmrig::Client::parseResponse() involved here, not xmrig::Client::parseLogin()

`parseLogin` is called right before the crashing line of code, and I added a check for `job`, so it won't crash anymore. As for the real reason of this crash, I still don't know.

## koitsu | 2024-02-28T01:11:23+00:00
Thanks.  I've built a binary based off https://github.com/SChernykh/xmrig/commit/b49197f8088fa594e4e9a1794f3f189b1d782b47  (your fork, branch dev, that commit) and am testing it now.

## koitsu | 2024-02-28T05:28:31+00:00
I can confirm https://github.com/SChernykh/xmrig/commit/b49197f8088fa594e4e9a1794f3f189b1d782b47 **does not** fix the problem.  This time the behaviour was seen against 178.128.242.134.

It may be that this is a libuv bug of some sort.  I will try upgrading libuv (adjusting build.uv.sh) to use libuv 1.45.0 or newe and see if I can reproduce the problem there.  Some of the fixes/info in https://github.com/libuv/libuv/releases implies there may be bugs that were fixed in newer versions, so it's worth a try.

```
$ ./xmrig-20240227T170234 --version
XMRig 6.21.2-dev
 built on Feb 28 2024 with GCC 9.4.0
 features: 64-bit AES

libuv/1.44.2
OpenSSL/1.1.1s
hwloc/2.9.0

$ sudo -- gdb -ex run --args ./xmrig-20240227T170234 --log-file ./xmrig.log
...
[2024-02-27 20:48:22.791]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)
[2024-02-27 20:48:27.588]  miner    speed 10s/60s/15m 511.5 439.2 185.4 H/s max 779.9 H/s avg 142.7 H/s
[2024-02-27 20:48:27.880]  cpu      accepted (108/2) diff 16384 (203 ms)
[2024-02-27 20:49:00.831]  net      dev donate started
xmrig-20240227T170234: /root/xmrig/src/3rdparty/rapidjson/document.h:1231: rapidjson::GenericValue<Encoding, Allocator>& rapidjson::GenericValue<Encoding, Allocator>::operator[](const rapidjson::GenericValue<Encoding, SourceAllocator>&) [with SourceAllocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>]: Assertion `false' failed.

Thread 1 "xmrig-20240227T" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7c7a859 in __GI_abort () at abort.c:79
#2  0x00007ffff7c7a729 in __assert_fail_base (fmt=0x7ffff7e10588 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=0x555555e71586 "false",
    file=0x555555e70ed8 "/root/xmrig/src/3rdparty/rapidjson/document.h", line=1231, function=<optimized out>) at assert.c:92
#3  0x00007ffff7c8bfd6 in __GI___assert_fail (assertion=0x555555e71586 "false", file=0x555555e70ed8 "/root/xmrig/src/3rdparty/rapidjson/document.h", line=1231,
    function=0x555555e71430 "rapidjson::GenericValue<Encoding, Allocator>& rapidjson::GenericValue<Encoding, Allocator>::operator[](const rapidjson::GenericValue<Encoding, SourceAllocator>&) [with SourceAllocator = rapidjson::Mem"...) at assert.c:101
#4  0x00005555559030ae in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> > (this=0x5555562a8ee8, name=...) at /root/xmrig/src/3rdparty/rapidjson/document.h:1231
#5  0x0000555555902355 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<char const> (this=0x5555562a8ee8,
    name=0x555555e76383 "job") at /root/xmrig/src/3rdparty/rapidjson/document.h:1211
#6  0x000055555591a1a1 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<char const> (this=0x5555562a8ee8,
    name=0x555555e76383 "job") at /root/xmrig/src/3rdparty/rapidjson/document.h:1214
#7  0x00005555559154f7 in xmrig::Client::parseResponse (this=0x555556238790, id=1, result=..., error=...) at /root/xmrig/src/base/net/stratum/Client.cpp:852
#8  0x0000555555914d8f in xmrig::Client::parse (this=0x555556238790, line=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", len=123)
    at /root/xmrig/src/base/net/stratum/Client.cpp:735
#9  0x00005555559165a7 in xmrig::Client::onLine (this=0x555556238790, line=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=123)
    at /root/xmrig/src/base/net/stratum/Client.h:81
#10 0x0000555555936115 in xmrig::LineReader::getline (this=0x555556238c38, data=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=124)
    at /root/xmrig/src/base/net/tools/LineReader.cpp:92
#11 0x0000555555935f24 in xmrig::LineReader::parse (this=0x555556238c38, data=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=124)
    at /root/xmrig/src/base/net/tools/LineReader.cpp:43
#12 0x0000555555b4ed03 in xmrig::Client::Tls::read (this=0x555556261000, data=0x7ffff53b8038 "\027\003\003", size=146) at /root/xmrig/src/base/net/stratum/Tls.cpp:134
#13 0x00005555559157eb in xmrig::Client::read (this=0x555556238790, nread=146, buf=0x7fffffffb0e0) at /root/xmrig/src/base/net/stratum/Client.cpp:910
#14 0x0000555555915d07 in xmrig::Client::onRead (stream=0x7fffe80095d0, nread=146, buf=0x7fffffffb0e0) at /root/xmrig/src/base/net/stratum/Client.cpp:1061
#15 0x0000555555cd4d8c in uv__read (stream=0x7fffe80095d0) at src/unix/stream.c:1201
#16 0x0000555555cd5092 in uv__stream_io (loop=0x55555616cd80 <default_loop_struct>, w=0x7fffe8009658, events=1) at src/unix/stream.c:1270
#17 0x0000555555ce022a in uv__io_poll (loop=0x55555616cd80 <default_loop_struct>, timeout=369) at src/unix/epoll.c:374
#18 0x0000555555cc3683 in uv_run (loop=0x55555616cd80 <default_loop_struct>, mode=UV_RUN_DEFAULT) at src/unix/core.c:406
#19 0x0000555555a08ccd in xmrig::App::exec (this=0x7fffffffe4d0) at /root/xmrig/src/App.cpp:90
#20 0x0000555555a228f7 in main (argc=3, argv=0x7fffffffe628) at /root/xmrig/src/xmrig.cpp:36
(gdb) f 8
#8  0x0000555555914d8f in xmrig::Client::parse (this=0x555556238790, line=0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", len=123)
    at /root/xmrig/src/base/net/stratum/Client.cpp:735
735     /root/xmrig/src/base/net/stratum/Client.cpp: No such file or directory.
(gdb) p line
$1 = 0x55555615c700 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id"
(gdb) f 13
#13 0x00005555559157eb in xmrig::Client::read (this=0x555556238790, nread=146, buf=0x7fffffffb0e0) at /root/xmrig/src/base/net/stratum/Client.cpp:910
910     in /root/xmrig/src/base/net/stratum/Client.cpp
(gdb) p this->m_ip
$2 = {m_data = 0x55555625dbf0 "178.128.242.134", m_size = 15}
(gdb) p this->m_sendBuf
$3 = {<std::_Vector_base<char, std::allocator<char> >> = {
    _M_impl = {<std::allocator<char>> = {<__gnu_cxx::new_allocator<char>> = {<No data fields>}, <No data fields>}, <std::_Vector_base<char, std::allocator<char> >::_Vector_impl_data> = {
        _M_start = 0x5555561f9670 "{\"id\":1,\"jsonrpc\":\"2.0\",\"method\":\"login\",\"params\":{\"login\":\"6eac04ac520eeb0caf8bf2dc27e59be7339e2cd823ff71da26d8afd9422f00f8\",\"pass\":\"x\",\"agent\":\"XMRig/6.21.2-dev (Linux x86_64) libuv/1.44.2 gcc/9.4.0"..., _M_finish = 0x5555561f9a70 "", _M_end_of_storage = 0x5555561f9a70 ""}, <No data fields>}}, <No data fields>}
(gdb)
```



## SChernykh | 2024-02-28T08:14:48+00:00
This is weird, that assert shouldn't trigger. XMRig does check for JSON parsing errors on the path to `Client::parseResponse`, and it does check for `job` existence now. Can you build XMRig with `-DWITH_DEBUG_LOG=ON` in cmake command line? It will show all communication with the stratum server.

## koitsu | 2024-02-28T08:40:28+00:00
I suspect there is very buggy code somewhere when used alongside `-O0`.  Anyway, binary with libuv 1.48.0 had the same issue / same crash.  I will add `-DWITH_DEBUG_LOG=on`.

Addendum: regarding original bug report (re: crash in libuv fs.c): this might be used due to me launching XMRig with `sudo -- ./xmrig --log-file ./xmrig.log` (note the `--log-file`), however unsure if XMRig's logging functions use libuv or something native.

## koitsu | 2024-02-28T08:52:26+00:00
Built (also using libuv 1.48.0) and now running.  Quite a useful compile-time feature :)

## koitsu | 2024-02-28T21:01:30+00:00
Reproduced.  Looks like what comes across the wire is indeed proper JSON.  Because I'm not familiar with the XMRig code nor rapidjson, it's hard for me to tell exactly where the issue is.  Let me know what frame/variables you might find of interest, or if you want a core dump (I think I can get that in this scenario with gdb).

```
[2024-02-28 04:43:19.714]  net      new job from ghostrider.mine.zergpool.com:15354 diff 16384 algo ghostrider height 123538
[2024-02-28 04:43:26.560] [donate.ssl.xmrig.com:443] state: "unconnected" -> "host-lookup"
[2024-02-28 04:43:26.569] [donate.ssl.xmrig.com:443] state: "host-lookup" -> "connecting"
[2024-02-28 04:43:26.710] [donate.ssl.xmrig.com:443] state: "connecting" -> "connected"
[2024-02-28 04:43:26.710] [donate.ssl.xmrig.com:443] TLS send     (293 bytes)
[2024-02-28 04:43:26.855] [donate.ssl.xmrig.com:443] TLS received (1448 bytes)
[2024-02-28 04:43:26.855] [donate.ssl.xmrig.com:443] TLS received (3116 bytes)
[2024-02-28 04:43:26.856] [donate.ssl.xmrig.com:443] send (543 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"6eac04ac520eeb0caf8bf2dc27e59be7339e2cd823ff71da26d8afd9422f00f8","pass":"x","agent":"XMRig/6.21.1 (Linux x86_64) libuv/1.48.0 gcc/9.4.0","algo":["ghostrider","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/keva","argon2/chukwa","argon2/chukwav2","argon2/ninja","cn/1"],"diff":16384,"height":123538}}"
[2024-02-28 04:43:26.856] [donate.ssl.xmrig.com:443] TLS send     (645 bytes)
[2024-02-28 04:43:26.998] [donate.ssl.xmrig.com:443] TLS received (478 bytes)
[2024-02-28 04:43:27.047] [donate.ssl.xmrig.com:443] TLS received (146 bytes)
[2024-02-28 04:43:27.047] [donate.ssl.xmrig.com:443] received (123 bytes): "{"id":1,"error":null,"result":{"id":"7357a618047dec68","algo":"ghostrider","extra_nonce":"ffb58baa","extra_nonce2_size":4}}"
[2024-02-28 04:43:27.047] [donate.ssl.xmrig.com:443] extra nonce set to ffb58baa
[2024-02-28 04:43:27.047]  net      dev donate started
xmrig-20240228T004215: /root/xmrig/src/3rdparty/rapidjson/document.h:1231: rapidjson::GenericValue<Encoding, Allocator>& rapidjson::GenericValue<Encoding, Allocator>::operator[](const rapidjson::GenericValue<Encoding, SourceAllocator>&) [with SourceAllocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; Encoding = rapidjson::UTF8<>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>]: Assertion `false' failed.

Thread 1 "xmrig-20240228T" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7c7a859 in __GI_abort () at abort.c:79
#2  0x00007ffff7c7a729 in __assert_fail_base (fmt=0x7ffff7e10588 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=0x555555e76586 "false",
    file=0x555555e75ed8 "/root/xmrig/src/3rdparty/rapidjson/document.h", line=1231, function=<optimized out>) at assert.c:92
#3  0x00007ffff7c8bfd6 in __GI___assert_fail (assertion=0x555555e76586 "false", file=0x555555e75ed8 "/root/xmrig/src/3rdparty/rapidjson/document.h", line=1231,
    function=0x555555e76430 "rapidjson::GenericValue<Encoding, Allocator>& rapidjson::GenericValue<Encoding, Allocator>::operator[](const rapidjson::GenericValue<Encoding, SourceAllocator>&) [with SourceAllocator = rapidjson::Mem"...) at assert.c:101
#4  0x0000555555904100 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> > (this=0x5555562a78f8, name=...) at /root/xmrig/src/3rdparty/rapidjson/document.h:1231
#5  0x00005555559033a7 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<char const> (this=0x5555562a78f8,
    name=0x555555e7b428 "job") at /root/xmrig/src/3rdparty/rapidjson/document.h:1211
#6  0x000055555591b3f3 in rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::operator[]<char const> (this=0x5555562a78f8,
    name=0x555555e7b428 "job") at /root/xmrig/src/3rdparty/rapidjson/document.h:1214
#7  0x0000555555916681 in xmrig::Client::parseResponse (this=0x55555623f930, id=1, result=..., error=...) at /root/xmrig/src/base/net/stratum/Client.cpp:847
#8  0x0000555555915f19 in xmrig::Client::parse (this=0x55555623f930, line=0x555556163740 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", len=123)
    at /root/xmrig/src/base/net/stratum/Client.cpp:730
#9  0x00005555559177cd in xmrig::Client::onLine (this=0x55555623f930, line=0x555556163740 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=123)
    at /root/xmrig/src/base/net/stratum/Client.h:81
#10 0x00005555559375bd in xmrig::LineReader::getline (this=0x55555623fdd8, data=0x555556163740 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=124)
    at /root/xmrig/src/base/net/tools/LineReader.cpp:92
#11 0x00005555559373cc in xmrig::LineReader::parse (this=0x55555623fdd8, data=0x555556163740 <xmrig::Client::Tls::read(char const*, unsigned long)::buf> "{\"id", size=124)
    at /root/xmrig/src/base/net/tools/LineReader.cpp:43
#12 0x0000555555b50883 in xmrig::Client::Tls::read (this=0x555556245080, data=0x7ffff53b8038 "\027\003\003", size=146) at /root/xmrig/src/base/net/stratum/Tls.cpp:134
#13 0x00005555559169a5 in xmrig::Client::read (this=0x55555623f930, nread=146, buf=0x7fffffffa4c0) at /root/xmrig/src/base/net/stratum/Client.cpp:905
#14 0x0000555555916f2d in xmrig::Client::onRead (stream=0x7fffe8006b30, nread=146, buf=0x7fffffffa4c0) at /root/xmrig/src/base/net/stratum/Client.cpp:1056
#15 0x0000555555cd7770 in uv__read (stream=0x7fffe8006b30) at src/unix/stream.c:1143
#16 0x0000555555cd7a5c in uv__stream_io (loop=0x555556173dc0 <default_loop_struct>, w=0x7fffe8006bb8, events=1) at src/unix/stream.c:1203
#17 0x0000555555ce19f8 in uv__io_poll (loop=0x555556173dc0 <default_loop_struct>, timeout=188) at src/unix/linux.c:1528
#18 0x0000555555cc5a67 in uv_run (loop=0x555556173dc0 <default_loop_struct>, mode=UV_RUN_DEFAULT) at src/unix/core.c:448
#19 0x0000555555a0a85b in xmrig::App::exec (this=0x7fffffffe4d0) at /root/xmrig/src/App.cpp:90
#20 0x0000555555a24485 in main (argc=3, argv=0x7fffffffe628) at /root/xmrig/src/xmrig.cpp:36
(gdb)
```

## SChernykh | 2024-02-28T22:08:40+00:00
This callstack is the old code, not the one in https://github.com/SChernykh/xmrig/commit/b49197f8088fa594e4e9a1794f3f189b1d782b47
Can you try with that one?

And yes, the donation server sent a login response without `job` object:
```
{"id":1,"error":null,"result":{"id":"7357a618047dec68","algo":"ghostrider","extra_nonce":"ffb58baa","extra_nonce2_size":4}}
```
which is wrong

## xmrig | 2024-02-29T02:51:04+00:00
After a bit of investigation I found bug: if build with `-DWITH_KAWPOW=OFF` for donation used wrong stratum client and it expected `job` field, but previous PR #3431 should hide this bug and assertion should never happen.

Donations use `AutoClient` that client chose between `EthStratumClient` and generic `Client` in runtime based on login response, since GhostRider and KawPow use another stratum protocol.
Thank you.

## koitsu | 2024-02-29T15:58:14+00:00
Stratum/protocol differences make perfect sense.  I always wondered how the dev donation thing worked in the first place, now I have a better idea.  Thanks for digging in with me!

I'll build https://github.com/xmrig/xmrig/commit/64913e3163d98887ab1902eaf9834a3acd3e3d2f (xmrig repo, branch dev) and try it out + provide feedback here.

## koitsu | 2024-02-29T16:18:46+00:00
Built and running.  Your build instructions got updated so I'll include what's used in this build:
* Repo: https://github.com/xmrig/xmrig.git
* Branch: `dev`
* Commit tip: https://github.com/xmrig/xmrig/commit/64913e3163d98887ab1902eaf9834a3acd3e3d2f
* Compile details:
  - `cmake .. -DXMRIG_DEPS=scripts/deps -DCMAKE_BUILD_TYPE=Debug -DWITH_DEBUG_LOG=on`
  - `scripts/build.uv.sh` modified in two ways:
    - `UV_VERSION="1.48.0"`
    - `CFLAGS="-ggdb -g3 -O0" ./configure --disable-shared`
```
$ ./xmrig-20240229T080338 --version
XMRig 6.21.2-dev
 built on Feb 29 2024 with GCC 9.4.0
 features: 64-bit AES

libuv/1.48.0
OpenSSL/1.1.1s
hwloc/2.9.0
```

## koitsu | 2024-03-01T20:10:18+00:00
Still running good so far -- lots of dev donation start/ends working well.  So I think that bug -- still unsure if it's related to this ticket or not -- is fixed.  For now, going to keep letting the debug build run under gdb to see if the uv__fs_done bug kicks in or not.

## koitsu | 2024-03-03T23:25:56+00:00
OK, it seems the src/unix/fs.c crash is still there (i.e. above issue I reported was actually a separate problem).  Finally got a crash in fs.c today.

Since I'm not well-versed in libuv structures, I'm just generally poking around.  @SChernykh I'll keep this gdb session up, so please advise me on what frames and variables/structs you might be interested in.  If you'd like me to open a libuv GitHub Issue on this (to get some additional help), let me know and I'll do it.

```
[2024-03-02 12:03:10.126]  net      new job from ghostrider.mine.zergpool.com:15354 diff 16384 algo ghostrider height 211533
[2024-03-02 12:03:10.131]  cpu      GhostRider algo 1: cn/turtle-lite (128 KB)
[2024-03-02 12:03:10.131]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2024-03-02 12:03:10.131]  cpu      GhostRider algo 3: cn/dark (512 KB)
xmrig-20240229T080338: src/unix/fs.c:1622: uv__fs_done: Assertion `uv__has_active_reqs(req->loop)' failed.

Thread 1 "xmrig-20240229T" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7c7a859 in __GI_abort () at abort.c:79
#2  0x00007ffff7c7a729 in __assert_fail_base (fmt=0x7ffff7e10588 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=0x555555f6b450 "uv__has_active_reqs(req->loop)",
    file=0x555555f6b43c "src/unix/fs.c", line=1622, function=<optimized out>) at assert.c:92
#3  0x00007ffff7c8bfd6 in __GI___assert_fail (assertion=0x555555f6b450 "uv__has_active_reqs(req->loop)", file=0x555555f6b43c "src/unix/fs.c", line=1622,
    function=0x555555f6b4a0 <__PRETTY_FUNCTION__.9896> "uv__fs_done") at assert.c:101
#4  0x0000555555cc9f2a in uv__fs_done (w=0x7fffe8004780, status=0) at src/unix/fs.c:1622
#5  0x0000555555cbe511 in uv__work_done (handle=0x555556172e70 <default_loop_struct+176>) at src/threadpool.c:329
#6  0x0000555555cc3a9f in uv__async_io (loop=0x555556172dc0 <default_loop_struct>, w=0x555556172f88 <default_loop_struct+456>, events=1) at src/unix/async.c:176
#7  0x0000555555ce09b8 in uv__io_poll (loop=0x555556172dc0 <default_loop_struct>, timeout=259) at src/unix/linux.c:1528
#8  0x0000555555cc4a27 in uv_run (loop=0x555556172dc0 <default_loop_struct>, mode=UV_RUN_DEFAULT) at src/unix/core.c:448
#9  0x0000555555a09849 in xmrig::App::exec (this=0x7fffffffe4d0) at /root/xmrig/src/App.cpp:90
#10 0x0000555555a23473 in main (argc=3, argv=0x7fffffffe628) at /root/xmrig/src/xmrig.cpp:36
(gdb) f 4
#4  0x0000555555cc9f2a in uv__fs_done (w=0x7fffe8004780, status=0) at src/unix/fs.c:1622
1622    in src/unix/fs.c
(gdb) p req
$1 = (uv_fs_t *) 0x7fffe8004630
(gdb) p *req
$2 = {data = 0x7fffe8006ed0, type = UV_FS, reserved = {0x3330332e38333a30, 0x74617274735b205d, 0x2f3a6c73732b6d75, 0x697274736f68672f, 0x656e696d2e726564, 0x6f6f706772657a2e},
  fs_type = UV_FS_WRITE, loop = 0x555556172dc0 <default_loop_struct>, cb = 0x5555558f973c <xmrig::fsWriteCallback(uv_fs_t*)>, result = 72, ptr = 0x0, path = 0x0, statbuf = {
    st_dev = 3328760707660607602, st_mode = 7526752396642099760, st_nlink = 7956010210498339951, st_uid = 7881991435412008553, st_gid = 8241992085136372841,
    st_rdev = 8152178580738239841, st_ino = 7525639748157060474, st_size = 7813033309939135080, st_blksize = 3995660921692696673, st_blocks = 8314040110914692462,
    st_flags = 8607841704012623971, st_gen = 3474869271659291240, st_atim = {tv_sec = 3472328236030113337, tv_nsec = 2462380686627057712}, st_mtim = {tv_sec = 3559359069731239222,
      tv_nsec = 4048789048530185250}, st_ctim = {tv_sec = 730283928549799472, tv_nsec = 385}, st_birthtim = {tv_sec = 140737085702640, tv_nsec = 140737085702640}}, new_path = 0x0,
  file = 11, flags = 0, mode = 0, nbufs = 0, bufs = 0x0, off = 16813819, uid = 0, gid = 0, atime = 2.2690014191823832e-318, mtime = 6.8003195493589174e-320, work_req = {work = 0x0,
    done = 0x555555cc9edb <uv__fs_done>, loop = 0x555556172dc0 <default_loop_struct>, wq = {next = 0x7fffffffa1f0, prev = 0x7fffffffa1f0}}, bufsml = {{
      base = 0x7fffe8006ed0 "[2024-03-02 12:03:10.131]  cpu      GhostRider algo 3: cn/dark (512 KB)\nU", len = 72}, {base = 0x0, len = 0}, {base = 0x0, len = 0}, {base = 0x0,
      len = 0}}}
(gdb) p req->loop
$3 = (uv_loop_t *) 0x555556172dc0 <default_loop_struct>
(gdb) p *req->loop
$4 = {data = 0x0, active_handles = 11, handle_queue = {next = 0x555556173048 <default_loop_struct+648>, prev = 0x7fffe8006b10}, active_reqs = {unused = 0x0, count = 0},
  internal_fields = 0x55555622c650, stop_flag = 0, flags = 0, backend_fd = 3, pending_queue = {next = 0x555556172e08 <default_loop_struct+72>,
    prev = 0x555556172e08 <default_loop_struct+72>}, watcher_queue = {next = 0x555556172e18 <default_loop_struct+88>, prev = 0x555556172e18 <default_loop_struct+88>},
  watchers = 0x5555562480f0, nwatchers = 30, nfds = 6, wq = {next = 0x555556172e38 <default_loop_struct+120>, prev = 0x555556172e38 <default_loop_struct+120>}, wq_mutex = {__data = {
      __lock = 0, __count = 0, __owner = 0, __nusers = 0, __kind = 0, __spins = 0, __elision = 0, __list = {__prev = 0x0, __next = 0x0}}, __size = '\000' <repeats 39 times>,
    __align = 0}, wq_async = {data = 0x0, loop = 0x555556172dc0 <default_loop_struct>, type = UV_ASYNC, close_cb = 0x0, handle_queue = {next = 0x55555622c5d0,
      prev = 0x555556173048 <default_loop_struct+648>}, u = {fd = 0, reserved = {0x0, 0x0, 0x0, 0x0}}, next_closing = 0x0, flags = 20, async_cb = 0x555555cbe440 <uv__work_done>,
    queue = {next = 0x555556172f70 <default_loop_struct+432>, prev = 0x555556172f70 <default_loop_struct+432>}, pending = 0}, cloexec_lock = {__data = {__readers = 0, __writers = 0,
      __wrphase_futex = 0, __writers_futex = 0, __pad3 = 0, __pad4 = 0, __cur_writer = 0, __shared = 0, __rwelision = 0 '\000', __pad1 = "\000\000\000\000\000\000", __pad2 = 0,
      __flags = 0}, __size = '\000' <repeats 55 times>, __align = 0}, closing_handles = 0x0, process_handles = {next = 0x555556172f30 <default_loop_struct+368>,
    prev = 0x555556172f30 <default_loop_struct+368>}, prepare_handles = {next = 0x555556172f40 <default_loop_struct+384>, prev = 0x555556172f40 <default_loop_struct+384>},
  check_handles = {next = 0x555556172f50 <default_loop_struct+400>, prev = 0x555556172f50 <default_loop_struct+400>}, idle_handles = {next = 0x555556172f60 <default_loop_struct+416>,
    prev = 0x555556172f60 <default_loop_struct+416>}, async_handles = {next = 0x555556172ed8 <default_loop_struct+280>, prev = 0x555556172ed8 <default_loop_struct+280>},
  async_unused = 0x0, async_io_watcher = {cb = 0x555555cc38d6 <uv__async_io>, pending_queue = {next = 0x555556172f90 <default_loop_struct+464>,
      prev = 0x555556172f90 <default_loop_struct+464>}, watcher_queue = {next = 0x555556172fa0 <default_loop_struct+480>, prev = 0x555556172fa0 <default_loop_struct+480>},
    pevents = 1, events = 1, fd = 8}, async_wfd = -1, timer_heap = {min = 0x5555562483e8, nelts = 3}, timer_counter = 559477, time = 465644812, signal_pipefd = {6, 7},
  signal_io_watcher = {cb = 0x555555cd4374 <uv__signal_event>, pending_queue = {next = 0x555556172ff8 <default_loop_struct+568>, prev = 0x555556172ff8 <default_loop_struct+568>},
    watcher_queue = {next = 0x555556173008 <default_loop_struct+584>, prev = 0x555556173008 <default_loop_struct+584>}, pevents = 1, events = 1, fd = 6}, child_watcher = {data = 0x0,
    loop = 0x555556172dc0 <default_loop_struct>, type = UV_SIGNAL, close_cb = 0x0, handle_queue = {next = 0x555556172e90 <default_loop_struct+208>,
      prev = 0x555556172dd0 <default_loop_struct+16>}, u = {fd = 0, reserved = {0x0, 0x0, 0x0, 0x0}}, next_closing = 0x0, flags = 16, signal_cb = 0x0, signum = 0, tree_entry = {
      rbe_left = 0x0, rbe_right = 0x0, rbe_parent = 0x0, rbe_color = 0}, caught_signals = 0, dispatched_signals = 0}, emfile_fd = 10, inotify_read_watcher = {cb = 0x0,
    pending_queue = {next = 0x0, prev = 0x0}, watcher_queue = {next = 0x0, prev = 0x0}, pevents = 0, events = 0, fd = 0}, inotify_watchers = 0x0, inotify_fd = -1}
(gdb) p req->loop->active_reqs
$5 = {unused = 0x0, count = 0}
```

## koitsu | 2024-03-03T23:33:59+00:00
I forgot about `set print pretty on` in gdb, ha. :)  Bit easier on the eyes now.  I suspect fs.c is being induced because I use `--log-file ./xmrig.log` in my XMRig invocation.  Here is that proof (see file descriptor 11):

```
(gdb) set print pretty on
(gdb) p *req
$24 = {
  data = 0x7fffe8006ed0,
  type = UV_FS,
...
  fs_type = UV_FS_WRITE,
...
  result = 72,
...
  file = 11,
...
(gdb) info proc
process 12995
cmdline = '/home/jdc/xmrig/xmrig-20240229T080338 --log-file ./xmrig.log'
cwd = '/home/jdc/xmrig'
exe = '/home/jdc/xmrig/xmrig-20240229T080338'
(gdb) shell lsof -p 12995
COMMAND     PID USER   FD      TYPE DEVICE SIZE/OFF     NODE NAME
...
xmrig-202 12995 root   11w      REG  259,2 16813819 25952280 /home/jdc/xmrig/xmrig.log
```

## koitsu | 2024-03-03T23:43:17+00:00
The only thing I see that might be the cause -- but I am literally grasping at straws here, so this may not be a problem at all:

```
(gdb) ptype req
type = struct uv_fs_s {
    void *data;
...
(gdb) x/s req->data
0x7fffe8006ed0: "[2024-03-02 12:03:10.131]  cpu      GhostRider algo 3: cn/dark (512 KB)\nU"
```
Not sure if the `U` on the end of the string is a problem or not.  The newline/0x0a is the 72nd character, and we did get back a result of 72 (I assume that's write length).  Given that I don't know how libuv works, maybe it's trying to do something with the remaining `U`+0x00 bytes?  Or is this just because I'm treating the bufffer as a C string?  I'll treating the length of the buffer as 74 bytes just to see what we get:
```
(gdb) x/74c req->data
0x7fffe8006ed0: 91 '['  50 '2'  48 '0'  50 '2'  52 '4'  45 '-'  48 '0'  51 '3'
0x7fffe8006ed8: 45 '-'  48 '0'  50 '2'  32 ' '  49 '1'  50 '2'  58 ':'  48 '0'
0x7fffe8006ee0: 51 '3'  58 ':'  49 '1'  48 '0'  46 '.'  49 '1'  51 '3'  49 '1'
0x7fffe8006ee8: 93 ']'  32 ' '  32 ' '  99 'c'  112 'p' 117 'u' 32 ' '  32 ' '
0x7fffe8006ef0: 32 ' '  32 ' '  32 ' '  32 ' '  71 'G'  104 'h' 111 'o' 115 's'
0x7fffe8006ef8: 116 't' 82 'R'  105 'i' 100 'd' 101 'e' 114 'r' 32 ' '  97 'a'
0x7fffe8006f00: 108 'l' 103 'g' 111 'o' 32 ' '  51 '3'  58 ':'  32 ' '  99 'c'
0x7fffe8006f08: 110 'n' 47 '/'  100 'd' 97 'a'  114 'r' 107 'k' 32 ' '  40 '('
0x7fffe8006f10: 53 '5'  49 '1'  50 '2'  32 ' '  75 'K'  66 'B'  41 ')'  10 '\n'
0x7fffe8006f18: 85 'U'  0 '\000'
```
In the actual xmrig.log file itself, the last byte we have is newline/0x0a.  So maybe this isn't the cause.

## SChernykh | 2024-03-04T00:28:21+00:00
It can happen if XMRig uses some of libuv handles from multiple threads (libuv event loop is not thread safe). If you still have it open, can you get call stacks for all threads?

## koitsu | 2024-03-04T00:44:10+00:00
Sure thing.  And yeah, I'm keeping this gdb session open until you have something else for me to look at or new code to try somewhere.  We'll figure this out :)

```
(gdb) thread apply all bt

Thread 12 (Thread 0x7fffed5ff700 (LWP 13015)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7fffe4002f44) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x7fffe4002ef0, cond=0x7fffe4002f18) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x7fffe4002f18, mutex=0x7fffe4002ef0) at pthread_cond_wait.c:647
#3  0x0000555555cd962f in uv_cond_wait (cond=0x7fffe4002f18, mutex=0x7fffe4002ef0) at src/unix/thread.c:814
#4  0x0000555555d41bb4 in xmrig::ghostrider::HelperThread::run (this=0x7fffe4002ef0) at /root/xmrig/src/crypto/ghostrider/ghostrider.cpp:257
#5  0x0000555555d42505 in std::__invoke_impl<void, void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> (__f=@0x7fffe40031b0: (void (xmrig::ghostrider::HelperThread::*)(struct xmrig::ghostrider::HelperThread * const)) 0x555555d41aee <xmrig::ghostrider::HelperThread::run()>, __t=@0x7fffe40031a8: 0x7fffe4002ef0) at /usr/include/c++/9/bits/invoke.h:73
#6  0x0000555555d4241f in std::__invoke<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> (__fn=@0x7fffe40031b0: (void (xmrig::ghostrider::HelperThread::*)(struct xmrig::ghostrider::HelperThread * const)) 0x555555d41aee <xmrig::ghostrider::HelperThread::run()>) at /usr/include/c++/9/bits/invoke.h:95
#7  0x0000555555d4236f in std::thread::_Invoker<std::tuple<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> >::_M_invoke<0ul, 1ul> (this=0x7fffe40031a8) at /usr/include/c++/9/thread:244
#8  0x0000555555d42311 in std::thread::_Invoker<std::tuple<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> >::operator() (this=0x7fffe40031a8) at /usr/include/c++/9/thread:251
#9  0x0000555555d422e2 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> > >::_M_run (this=0x7fffe40031a0) at /usr/include/c++/9/thread:195
#10 0x0000555555e3b774 in execute_native_thread_routine ()
#11 0x00007ffff7fa7609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#12 0x00007ffff7d77353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 11 (Thread 0x7fffeefff700 (LWP 13014)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7fffe8002f74) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x7fffe8002f20, cond=0x7fffe8002f48) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x7fffe8002f48, mutex=0x7fffe8002f20) at pthread_cond_wait.c:647
#3  0x0000555555cd962f in uv_cond_wait (cond=0x7fffe8002f48, mutex=0x7fffe8002f20) at src/unix/thread.c:814
#4  0x0000555555d41bb4 in xmrig::ghostrider::HelperThread::run (this=0x7fffe8002f20) at /root/xmrig/src/crypto/ghostrider/ghostrider.cpp:257
#5  0x0000555555d42505 in std::__invoke_impl<void, void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> (__f=@0x7fffe80031e0: (void (xmrig::ghostrider::HelperThread::*)(struct xmrig::ghostrider::HelperThread * const)) 0x555555d41aee <xmrig::ghostrider::HelperThread::run()>, __t=@0x7fffe80031d8: 0x7fffe8002f20) at /usr/include/c++/9/bits/invoke.h:73
#6  0x0000555555d4241f in std::__invoke<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> (__fn=@0x7fffe80031e0: (void (xmrig::ghostrider::HelperThread::*)(struct xmrig::ghostrider::HelperThread * const)) 0x555555d41aee <xmrig::ghostrider::HelperThread::run()>) at /usr/include/c++/9/bits/invoke.h:95
#7  0x0000555555d4236f in std::thread::_Invoker<std::tuple<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> >::_M_invoke<0ul, 1ul> (this=0x7fffe80031d8) at /usr/include/c++/9/thread:244
#8  0x0000555555d42311 in std::thread::_Invoker<std::tuple<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> >::operator() (this=0x7fffe80031d8) at /usr/include/c++/9/thread:251
#9  0x0000555555d422e2 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (xmrig::ghostrider::HelperThread::*)(), xmrig::ghostrider::HelperThread*> > >::_M_run (this=0x7fffe80031d0) at /usr/include/c++/9/thread:195
#10 0x0000555555e3b774 in execute_native_thread_routine ()
#11 0x00007ffff7fa7609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#12 0x00007ffff7d77353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 10 (Thread 0x7ffff4b9a700 (LWP 13013)):
#0  0x00007ffff7c4d0f4 in ?? ()
#1  0x00007ffff4b99fc0 in ?? ()
#2  0x00007fffe4002ef0 in ?? ()
#3  0x0000000000000050 in ?? ()
#4  0x0000000000000000 in ?? ()

Thread 9 (Thread 0x7ffff53b7700 (LWP 13012)):
#0  0x00007ffff7c4d090 in ?? ()
#1  0x00007ffff53b6fc0 in ?? ()
#2  0x00007fffe8002f20 in ?? ()
--Type <RET> for more, q to quit, c to continue without paging--
#3  0x0000000000000050 in ?? ()
#4  0x0000000000000000 in ?? ()

Thread 6 (Thread 0x7ffff5c31700 (LWP 13003)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x555556202ee8) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x555556202ef0, cond=0x555556202ec0) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x555556202ec0, mutex=0x555556202ef0) at pthread_cond_wait.c:647
#3  0x0000555555dc52f0 in std::condition_variable::wait(std::unique_lock<std::mutex>&) ()
#4  0x0000555555b38564 in std::condition_variable::wait<xmrig::RxQueue::backgroundInit()::<lambda()> >(std::unique_lock<std::mutex> &, xmrig::RxQueue::<lambda()>) (this=0x555556202ec0, __lock=..., __p=...) at /usr/include/c++/9/condition_variable:101
#5  0x0000555555b38192 in xmrig::RxQueue::backgroundInit (this=0x555556202e80) at /root/xmrig/src/crypto/rx/RxQueue.cpp:129
#6  0x0000555555b3ac43 in std::__invoke_impl<void, void (xmrig::RxQueue::*)(), xmrig::RxQueue*> (__f=@0x555556248210: (void (xmrig::RxQueue::*)(class xmrig::RxQueue * const)) 0x555555b38104 <xmrig::RxQueue::backgroundInit()>, __t=@0x555556248208: 0x555556202e80) at /usr/include/c++/9/bits/invoke.h:73
#7  0x0000555555b3ab5d in std::__invoke<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> (__fn=@0x555556248210: (void (xmrig::RxQueue::*)(class xmrig::RxQueue * const)) 0x555555b38104 <xmrig::RxQueue::backgroundInit()>) at /usr/include/c++/9/bits/invoke.h:95
#8  0x0000555555b3aaad in std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> >::_M_invoke<0ul, 1ul> (this=0x555556248208) at /usr/include/c++/9/thread:244
#9  0x0000555555b3aa4f in std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> >::operator() (this=0x555556248208) at /usr/include/c++/9/thread:251
#10 0x0000555555b3aa20 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (xmrig::RxQueue::*)(), xmrig::RxQueue*> > >::_M_run (this=0x555556248200) at /usr/include/c++/9/thread:195
#11 0x0000555555e3b774 in execute_native_thread_routine ()
#12 0x00007ffff7fa7609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#13 0x00007ffff7d77353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 5 (Thread 0x7ffff6432700 (LWP 13002)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x555556172d08 <cond+40>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x555556172d20 <mutex>, cond=0x555556172ce0 <cond>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at pthread_cond_wait.c:647
#3  0x0000555555cd962f in uv_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at src/unix/thread.c:814
#4  0x0000555555cbdccd in worker (arg=0x0) at src/threadpool.c:76
#5  0x00007ffff7fa7609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff7d77353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 4 (Thread 0x7ffff6c33700 (LWP 13001)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x555556172d0c <cond+44>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x555556172d20 <mutex>, cond=0x555556172ce0 <cond>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at pthread_cond_wait.c:647
#3  0x0000555555cd962f in uv_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at src/unix/thread.c:814
#4  0x0000555555cbdccd in worker (arg=0x0) at src/threadpool.c:76
#5  0x00007ffff7fa7609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff7d77353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 3 (Thread 0x7ffff7434700 (LWP 13000)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x555556172d0c <cond+44>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x555556172d20 <mutex>, cond=0x555556172ce0 <cond>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at pthread_cond_wait.c:647
#3  0x0000555555cd962f in uv_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at src/unix/thread.c:814
#4  0x0000555555cbdccd in worker (arg=0x0) at src/threadpool.c:76
#5  0x00007ffff7fa7609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff7d77353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 2 (Thread 0x7ffff7c35700 (LWP 12999)):
#0  futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x555556172d0c <cond+44>) at ../sysdeps/nptl/futex-internal.h:183
#1  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x555556172d20 <mutex>, cond=0x555556172ce0 <cond>) at pthread_cond_wait.c:508
#2  __pthread_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at pthread_cond_wait.c:647
--Type <RET> for more, q to quit, c to continue without paging--
#3  0x0000555555cd962f in uv_cond_wait (cond=0x555556172ce0 <cond>, mutex=0x555556172d20 <mutex>) at src/unix/thread.c:814
#4  0x0000555555cbdccd in worker (arg=0x0) at src/threadpool.c:76
#5  0x00007ffff7fa7609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#6  0x00007ffff7d77353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 1 (Thread 0x7ffff7c56f40 (LWP 12995)):
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7c7a859 in __GI_abort () at abort.c:79
#2  0x00007ffff7c7a729 in __assert_fail_base (fmt=0x7ffff7e10588 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=0x555555f6b450 "uv__has_active_reqs(req->loop)", file=0x555555f6b43c "src/unix/fs.c", line=1622, function=<optimized out>) at assert.c:92
#3  0x00007ffff7c8bfd6 in __GI___assert_fail (assertion=0x555555f6b450 "uv__has_active_reqs(req->loop)", file=0x555555f6b43c "src/unix/fs.c", line=1622, function=0x555555f6b4a0 <__PRETTY_FUNCTION__.9896> "uv__fs_done") at assert.c:101
#4  0x0000555555cc9f2a in uv__fs_done (w=0x7fffe8004780, status=0) at src/unix/fs.c:1622
#5  0x0000555555cbe511 in uv__work_done (handle=0x555556172e70 <default_loop_struct+176>) at src/threadpool.c:329
#6  0x0000555555cc3a9f in uv__async_io (loop=0x555556172dc0 <default_loop_struct>, w=0x555556172f88 <default_loop_struct+456>, events=1) at src/unix/async.c:176
#7  0x0000555555ce09b8 in uv__io_poll (loop=0x555556172dc0 <default_loop_struct>, timeout=259) at src/unix/linux.c:1528
#8  0x0000555555cc4a27 in uv_run (loop=0x555556172dc0 <default_loop_struct>, mode=UV_RUN_DEFAULT) at src/unix/core.c:448
#9  0x0000555555a09849 in xmrig::App::exec (this=0x7fffffffe4d0) at /root/xmrig/src/App.cpp:90
#10 0x0000555555a23473 in main (argc=3, argv=0x7fffffffe628) at /root/xmrig/src/xmrig.cpp:36
```

## SChernykh | 2024-03-04T07:40:18+00:00
I think I know why it crashes. I'll prepare a fix today.

The problem is that log can be written from any thread, but uv_default_loop() runs in the main thread. Any functions that use it must also be called only from the main thread because libuv loops are not thread-safe.

## SChernykh | 2024-03-04T07:46:46+00:00
Can you test #3436 ?

## koitsu | 2024-03-04T08:15:05+00:00
You bet!  Your explanation makes perfect sense given libuv's design (I did some reading); mutex lock around the operation is definitely right.  Thanks a ton!

I'll start this build and get it running shortly.  Be aware sometimes it takes several days for this problem to kick in, so you might not hear from me for a while if things are good :)

## SChernykh | 2024-03-04T08:30:29+00:00
The mutex is there only to safely pass data (`m_buffers`) between threads. The actual fix is that `uv_fs_write(uv_default_loop(), ...` is now called in the async call back which is always called from the default uv loop (=main thread).

## koitsu | 2024-03-14T09:37:55+00:00
So far the build with this fix has been running for 10 days and hasn't seen a single crash.  I think it's safe to merge #3436 .

Thanks for fixing this @SChernykh !

## koitsu | 2024-03-24T00:11:11+00:00
I think we can resolve this one.  As always, thanks a ton @SChernykh !

# Action History
- Created by: ftitreefly | 2021-12-07T15:08:13+00:00
- Closed at: 2025-06-16T20:26:38+00:00
