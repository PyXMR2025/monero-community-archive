---
title: Debian Testing build => free() invalid pointer
source_url: https://github.com/xmrig/xmrig/issues/3428
author: YannChemin
assignees: []
labels: []
created_at: '2024-02-25T10:00:35+00:00'
updated_at: '2025-06-16T19:46:54+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:46:54+00:00'
---

# Original Description
**Describe the bug**
compiling from git clone now, on a updated Debian testing today. When running the xmrig, it says "free(): invalid pointer Aborted"

**To Reproduce**

1. sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. cmake ..
5. make -j$(nproc)
6. ./xmrig -c theconf4xmrig.json 

**Expected behavior**
xmrig to launch
The binary version (latest download) works perfectly on the computer.

**Required data**
- terminal says: 

> free(): invalid pointer
> Aborted

 - Config file or command line (without wallets)
 - OS: Debian Testing updated today
 

**Additional context**

theconf4xmrig.json

~~~json
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": 1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5],
        "cn": [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
        "cn-heavy": [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
        "cn-lite": [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
        "cn-pico": [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5]],
        "cn/upx2": [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5]],
        "ghostrider": [[8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5]],
        "rx": [0, 1, 2, 3, 4, 5],
        "rx/wow": [0, 1, 2, 3, 4, 5],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [{
            "algo": "cn/r",
            "coin": null,
            "url": "xmrpool.eu:9999",
            "user": "XXXXX",
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
~~~


# Discussion History
## SChernykh | 2024-02-25T16:19:15+00:00
It might be something wrong with your dependencies. Try to build using advanced build instructions, it will create the same binary as in official releases.

## YannChemin | 2024-02-25T18:58:18+00:00
I removed the previously used xmrig git directory and used these steps:

1. sudo apt-get install git build-essential cmake automake libtool autoconf
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/scripts
4. ./build_deps.sh && cd ../build
5. cmake .. -DXMRIG_DEPS=scripts/deps
6. make -j$(nproc)

The result is the same:

~~~shell
free(): invalid pointer
Aborted
~~~

## SChernykh | 2024-02-26T08:30:57+00:00
Is it the full output in the terminal? Nothing else? Also, can you run it under gdb and get a call stack?
Run `gdb --args ./xmrig` then in console type `run` and when it crashes type `bt`

## YannChemin | 2024-02-26T08:36:36+00:00
~~~gdb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7fffee9ff6c0 (LWP 6016)]
[New Thread 0x7fffee1fe6c0 (LWP 6017)]
free(): invalid pointer
[Thread 0x7fffee1fe6c0 (LWP 6017) exited]

Thread 1 "xmrig" received signal SIGABRT, Aborted.
__pthread_kill_implementation (threadid=<optimized out>, signo=signo@entry=6, no_tid=no_tid@entry=0)
    at ./nptl/pthread_kill.c:44
44	./nptl/pthread_kill.c: No such file or directory.
(gdb) bt
#0  __pthread_kill_implementation (threadid=<optimized out>, signo=signo@entry=6, no_tid=no_tid@entry=0)
    at ./nptl/pthread_kill.c:44
#1  0x00007ffff7d611cf in __pthread_kill_internal (signo=6, threadid=<optimized out>) at ./nptl/pthread_kill.c:78
#2  0x00007ffff7d13472 in __GI_raise (sig=sig@entry=6) at ../sysdeps/posix/raise.c:26
#3  0x00007ffff7cfd4b2 in __GI_abort () at ./stdlib/abort.c:79
#4  0x00007ffff7cfe1ed in __libc_message (fmt=fmt@entry=0x7ffff7e7078c "%s\n") at ../sysdeps/posix/libc_fatal.c:150
#5  0x00007ffff7d6aae5 in malloc_printerr (str=str@entry=0x7ffff7e6e22c "free(): invalid pointer")
    at ./malloc/malloc.c:5658
#6  0x00007ffff7d6c864 in _int_free (av=<optimized out>, p=<optimized out>, have_lock=have_lock@entry=0)
    at ./malloc/malloc.c:4432
#7  0x00007ffff7d6f1df in __GI___libc_free (mem=<optimized out>) at ./malloc/malloc.c:3367
#8  0x00007ffff7c06ea0 in ?? () from /opt/rocm-6.0.1/lib/libamdocl64.so
#9  0x00007ffff7c1035d in ?? () from /opt/rocm-6.0.1/lib/libamdocl64.so
#10 0x00007ffff7bce525 in ?? () from /opt/rocm-6.0.1/lib/libamdocl64.so
#11 0x00007ffff7bfe43e in ?? () from /opt/rocm-6.0.1/lib/libamdocl64.so
#12 0x00007ffff7ba91b5 in ?? () from /opt/rocm-6.0.1/lib/libamdocl64.so
#13 0x00007ffff7d642d7 in __pthread_once_slow (once_control=0x7ffff7cc96a0, init_routine=0x7fffeeadd8d0 <__once_proxy>)
    at ./nptl/pthread_once.c:116
#14 0x00007ffff7baa23f in clIcdGetPlatformIDsKHR () from /opt/rocm-6.0.1/lib/libamdocl64.so
#15 0x00007ffff7f9c565 in ?? () from /opt/rocm-6.0.1/lib/libOpenCL.so
#16 0x00007ffff7f9e937 in ?? () from /opt/rocm-6.0.1/lib/libOpenCL.so
#17 0x00007ffff7d642d7 in __pthread_once_slow (once_control=0x7ffff7fa2100, init_routine=0x7ffff7f9e7a0)
    at ./nptl/pthread_once.c:116
#18 0x00007ffff7f9cbc6 in clGetPlatformIDs () from /opt/rocm-6.0.1/lib/libOpenCL.so
#19 0x00005555557e8ea8 in xmrig::OclLib::getPlatformIDs() ()
#20 0x00005555557e994b in xmrig::OclPlatform::get() ()
#21 0x00005555557d2ac9 in xmrig::OclConfig::platform() const ()
#22 0x00005555557d4c06 in xmrig::OclConfig::generate() ()
#23 0x000055555580689c in xmrig::Config::read(xmrig::IJsonReader const&, char const*) ()
#24 0x0000555555717a98 in xmrig::Base::Base(xmrig::Process*) ()
#25 0x0000555555814489 in xmrig::Controller::Controller(xmrig::Process*) ()
#26 0x0000555555805bce in xmrig::App::App(xmrig::Process*) ()
#27 0x00005555556dcf31 in main ()

~~~

## YannChemin | 2024-02-26T09:08:36+00:00
After changing opencl to false in .xmrig.conf, then it worked

## SChernykh | 2024-02-26T09:14:37+00:00
```
#18 0x00007ffff7f9cbc6 in clGetPlatformIDs () from /opt/rocm-6.0.1/lib/libOpenCL.so
#19 0x00005555557e8ea8 in xmrig::OclLib::getPlatformIDs() ()
```
XMRig just calls `clGetPlatformIDs` here, and then it crashes deep inside `libamdocl64.so` which is not a part of XMRig. Maybe (maybe) your OpenCL headers are incompatible with .so libraries you have there, which is why you have issues when compiling XMRig locally.

# Action History
- Created by: YannChemin | 2024-02-25T10:00:35+00:00
- Closed at: 2025-06-16T19:46:54+00:00
