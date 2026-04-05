---
title: '[ISSUE] SIGBUS, Bus Error On Ryzen'
source_url: https://github.com/xmrig/xmrig/issues/3311
author: Ayan-Nalawade
assignees: []
labels: []
created_at: '2023-08-01T23:14:21+00:00'
updated_at: '2024-03-10T14:31:17+00:00'
type: issue
status: closed
closed_at: '2024-03-10T14:31:17+00:00'
---

# Original Description
**Describe the bug**
When I try to execute it crashes with a Bus Error (core dumped)

**To Reproduce**
I have done the following from the other GitHub comment @xmrig  made [Here](https://github.com/xmrig/xmrig/issues/446#:~:text=Change%20this%20line,output.%0AThank%20you.):
(Copy and paste):

"Change this line to:

`set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -fno-exceptions -fno-rtti -Wno-missing-braces")`
The difference is added -g.

Then rebuild, after that run gdb ./xmrig, enter command r.
If miner crashed, enter command bt and show output.
Thank you."

Compiled with `cmake ..  -DWITH_HWLOC=OFF` and `make`, though after running `gdb ./xmrig` I got:
```
Starting program: /notebooks/xmrig/build/xmrig 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[2023-08-01 23:08:36.466] unable to open "/notebooks/xmrig/build/config.json".
[2023-08-01 23:08:36.466] unable to open "/root/.xmrig.json".
[2023-08-01 23:08:36.466] unable to open "/root/.config/xmrig.json".
[2023-08-01 23:08:36.466] no valid configuration found, try https://xmrig.com/wizard
[Inferior 1 (process 12345) exited with code 02]
```
so I created a config.json (I don't know what the other files mean "/root/.config/xmrig.json" && "/root/.xmrig.json"":
In config.json:
```
{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "coin": null,
            "algo": null,
            "url": "gulf.moneroocean.stream:10128",
            "user": "<MY WALLET ADDRESS>",
            "pass": "x",
            "tls": false,
            "keepalive": true,
            "nicehash": false
        }
    ]
}
```

after doing that and running with` gdb ./xmrig`:
```
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04.1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...
(No debugging symbols found in ./xmrig)
(gdb) r
Starting program: /notebooks/xmrig/build/xmrig 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
 * ABOUT        XMRig/6.20.0 gcc/9.4.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f 
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7742 64-Core Processor (1) 64-bit AES VM
                threads:52
 * MEMORY       9.8/102.3 GB (10%)
                DIMM 0: 16 GB RAM @ 0 MHz DIMM 0
                DIMM 1: 16 GB RAM @ 0 MHz DIMM 1
                DIMM 2: 16 GB RAM @ 0 MHz DIMM 2
                DIMM 3: 16 GB RAM @ 0 MHz DIMM 3
                DIMM 4: 16 GB RAM @ 0 MHz DIMM 4
                DIMM 5: 16 GB RAM @ 0 MHz DIMM 5
                DIMM 6: 8 GB RAM @ 0 MHz DIMM 6
 * MOTHERBOARD  OpenStack Foundation - OpenStack Nova
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[New Thread 0x7ffff78c9700 (LWP 10870)]
 * OPENCL       disabled
 * CUDA         disabled
[New Thread 0x7ffff70c8700 (LWP 10871)]
[New Thread 0x7ffff68c7700 (LWP 10872)]
[New Thread 0x7ffff60c6700 (LWP 10873)]
[New Thread 0x7ffff58c5700 (LWP 10874)]
[2023-08-01 23:00:04.563]  net      use pool gulf.moneroocean.stream:10128  44.196.193.227
[2023-08-01 23:00:04.563]  net      new job from gulf.moneroocean.stream:10128 diff 90515 algo rx/0 height 46025
[2023-08-01 23:00:04.563]  cpu      use argon2 implementation AVX2
[Detaching after vfork from child process 10875]
[2023-08-01 23:00:04.565]  msr      msr kernel module is not available
[2023-08-01 23:00:04.565]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2023-08-01 23:00:04.565]  randomx  init dataset algo rx/0 (52 threads) seed cd55b2233804d4da...
[2023-08-01 23:00:04.565]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)

Thread 2 "xmrig" received signal SIGBUS, Bus error.
[Switching to Thread 0x7ffff78c9700 (LWP 10870)]
0x00005555558a40e5 in xmrig_ar2_fill_first_blocks ()
```
then I ran `backtrace`:
```
#0  0x00005555558a40e5 in xmrig_ar2_fill_first_blocks ()
#1  0x00005555558a4275 in xmrig_ar2_initialize ()
#2  0x00005555558a0dd0 in argon2_ctx_mem ()
#3  0x0000555555869bc4 in randomx::initCache(randomx_cache*, void const*, unsigned long) ()
#4  0x0000555555869c2d in randomx::initCacheCompile(randomx_cache*, void const*, unsigned long) ()
#5  0x0000555555871847 in xmrig::RxCache::init(std::vector<unsigned char, std::allocator<unsigned char> > const&) ()
#6  0x0000555555874b62 in xmrig::RxDataset::init(std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, int) ()
#7  0x000055555587125c in xmrig::RxBasicStorage::init(xmrig::RxSeed const&, unsigned int, bool, bool, xmrig::RxConfig::Mode, int) ()
#8  0x00005555558758e8 in xmrig::RxQueue::backgroundInit() ()
#9  0x00005555559947b4 in ?? ()
#10 0x00007ffff7c3e609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#11 0x00007ffff7a0e133 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```
for further information `info registers` gives me:
```
rax            0x0                 0
rbx            0x7ffff78c8630      140737346569776
rcx            0x7fff56000000      140734636228608
rdx            0x7fff56000000      140734636228608
rsi            0x40                64
rdi            0x7ffff78c85a0      140737346569632
rbp            0x7ffff78c8b60      0x7ffff78c8b60
rsp            0x7ffff78c8630      0x7ffff78c8630
r8             0xbeb9eb464ad28ae8  -4703469648676222232
r9             0xa733aeebee6eb990  -6398578317222561392
r10            0xacc43e6527b58f33  -5997600199571828941
r11            0x7ffff78c84c0      140737346569408
r12            0x7ffff78c8640      140737346569792
r13            0x0                 0
r14            0x7ffff78c8af0      140737346570992
r15            0x7ffff78c8a70      140737346570864
rip            0x5555558a40e5      0x5555558a40e5 <xmrig_ar2_fill_first_blocks+149>
eflags         0x10202             [ IF RF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0
```
and `disassemble` returns:
```
   0x00005555558a4050 <+0>:     endbr64 
   0x00005555558a4054 <+4>:     push   %r15
   0x00005555558a4056 <+6>:     push   %r14
   0x00005555558a4058 <+8>:     push   %r13
   0x00005555558a405a <+10>:    push   %r12
   0x00005555558a405c <+12>:    push   %rbx
   0x00005555558a405d <+13>:    sub    $0x410,%rsp
   0x00005555558a4064 <+20>:    mov    0x1c(%rsi),%edx
   0x00005555558a4067 <+23>:    mov    %fs:0x28,%rax
   0x00005555558a4070 <+32>:    mov    %rax,0x408(%rsp)
   0x00005555558a4078 <+40>:    xor    %eax,%eax
   0x00005555558a407a <+42>:    test   %edx,%edx
   0x00005555558a407c <+44>:    je     0x5555558a4163 <xmrig_ar2_fill_first_blocks+275>
   0x00005555558a4082 <+50>:    mov    %rdi,%r15
   0x00005555558a4085 <+53>:    mov    %rsi,%r14
   0x00005555558a4088 <+56>:    xor    %r13d,%r13d
   0x00005555558a408b <+59>:    mov    %rsp,%rbx
   0x00005555558a408e <+62>:    lea    0x10(%rsp),%r12
   0x00005555558a4093 <+67>:    mov    %r13d,0x44(%r15)
   0x00005555558a4097 <+71>:    mov    $0x48,%ecx
   0x00005555558a409c <+76>:    mov    %r15,%rdx
   0x00005555558a409f <+79>:    mov    %rbx,%rdi
   0x00005555558a40a2 <+82>:    movl   $0x0,0x40(%r15)
   0x00005555558a40aa <+90>:    mov    $0x400,%esi
   0x00005555558a40af <+95>:    callq  0x5555558a7360 <xmrig_ar2_blake2b_long>
   0x00005555558a40b4 <+100>:   mov    %r13d,%eax
   0x00005555558a40b7 <+103>:   imul   0x18(%r14),%eax

```


# Discussion History
# Action History
- Created by: Ayan-Nalawade | 2023-08-01T23:14:21+00:00
- Closed at: 2024-03-10T14:31:17+00:00
