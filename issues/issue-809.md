---
title: 'Error: refresh failed: unexpected error: boost::thread_resource_error: Resource
  temporarily unavailable.'
source_url: https://github.com/monero-project/monero/issues/809
author: AJIekceu4
assignees: []
labels: []
created_at: '2016-04-16T18:08:43+00:00'
updated_at: '2016-12-15T18:14:55+00:00'
type: issue
status: closed
closed_at: '2016-12-15T18:14:55+00:00'
---

# Original Description
Wallet file (key) created 10.12.2014.
After upgrading simplewallet from 0.9.1 to 0.9.4.0-1c66fe0 i trying to resync via rpc from remote node and got this error every 400...2500 blocks:
`Error: refresh failed: unexpected error: boost::thread_resource_error: Resource temporarily unavailable. Blocks received: 1464`

From simplewallet side:
tcpflow -i wlan1 -c port 13666

> 188.166.061.194.13666-192.168.001.040.34074: Nfn :.p="qA&zaz]I_B7oDL&ujK0p6c]`nMx$Sqd/[KtTM.bQaAz9_RGSG#VoAf-oqD^-!G^aJN0DY^eS_Vl`block
> %/,~\omr-"..Ba+aX,D<pKl[CMGR+SH]Vm%Q*^
> xvvC3ke0block>RFK;(!z>]CQj@7(O y,(
> %kH5~Pp@H1+"f^HH_$12P
> N,D2itaZVm)9-O8Q&VF0+(YTj2%_T":^P?>!=BB
> h}) Yu>'|@et_Z2'>-`1xey!qmm9S.~Cv:rB>{BPF!`cQLs6tX.IwQEblock
> VX_b;`ja_Yl^glL3hNhkfxL
> /#Q@8B>MOyv-H`8QU -SarRz-IW
> 58.C
> }cle5EJ~R5P-sK6!^K+t=yY7block.001.040.34074: lb% ;|I[l;oa
> # >3Cp:jsx,?K^F0\M}t30x-[k#W&)c^4J&'"+NM@\pKqVUsm8/!jikz"q:m
> 
> 4fcurrent_height/start_height[@status
> OK

From bitmonero side (v0.9.4.0-abea280):
tcpflow -i eth0 -c port 13666

> %kH5~Pp@H1+"f^HH_$12P
> N,D2itaZVm)9-O8Q&VF0+(YTj2%_T":^P?>!=BB
> h}) Yu>'|@et_Z2'>-`1xey!qmm9S.~Cv:rB>{BPF!`cQLs6tX.IwQEblock
> VX_b;`ja_Yl^glL3hNhkfxL
> /#Q@8B>MOyv-H`8QU -SarRz-IW
> 58.C
> }cle5EJ~R5P-sK6!^K+t=yY7block.232.108.34074: lb% ;|I[l;oa
> # >3Cp:jsx,?K^F0\M}t30x-[k#W&)c^4J&'"+NM@\pKqVUsm8/!jikz"q:m
> 
> 4fcurrent_height/start_height[@status
> OK
> 188.166.061.194.13666-110.168.232.108.34258: HTTP/1.1 200 Ok
> Server: Epee-based
> Content-Length: 44
> Content-Type: application/json
> Last-Modified: Sat, 16 Apr 2016 17:22:43 GMT
> Accept-Ranges: bytes

I try another public node (node.moneroclub.com:8880) and got the same error.
I use libboost 1.58 and 1.60 - problem exist.

Kali Linux (linux-headers-4.4.0-kali1-amd64)

```
cat /proc/sys/kernel/threads-max
77378
```

```
ulimit -s
8192
```


# Discussion History
## AJIekceu4 | 2016-04-16T18:43:22+00:00
After start simplewallet with log_level 4:

```
2016-Apr-17 01:41:39.070365 ERROR /root/15.04.2016/bitmonero/src/wallet/wallet2.cpp:830 pull_blocks failed, try_count=3
2016-Apr-17 01:41:39.070717 ERROR /root/15.04.2016/bitmonero/src/simplewallet/simplewallet.cpp:1806 unexpected error: boost::thread_resource_error: Resource temporarily unavailable
2016-Apr-17 01:41:39.070750 Error: refresh failed: unexpected error: boost::thread_resource_error: Resource temporarily unavailable. Blocks received: 2777
```

Full log:
https://www.dropbox.com/s/me9hdrm4cm42nzp/simplewallet_with_bug.log?dl=0


## moneromooo-monero | 2016-04-17T10:02:47+00:00
When this happens:
gdb /path/to/simplewallet `pidof simplewallet`
thread apply all bt


## AJIekceu4 | 2016-04-17T14:05:57+00:00
pidof simplewallet
27138
gdb /root/monero/simplewallet 27138
GNU gdb (Debian 7.10-1+b1) 7.10
Copyright (C) 2015 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later http://gnu.org/licenses/gpl.html
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
http://www.gnu.org/software/gdb/bugs/.
Find the GDB manual and other documentation resources online at:
http://www.gnu.org/software/gdb/documentation/.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /root/monero/simplewallet...done.
Attaching to program: /root/monero/simplewallet, process 27138
Reading symbols from /lib/x86_64-linux-gnu/librt.so.1...Reading symbols from /usr/lib/debug/.build-id/72/759f03f2a2ebca1aecb17b10f3c0ae735ca6e5.debug...done.
done.
Reading symbols from /usr/lib/x86_64-linux-gnu/libunbound.so.2...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_date_time.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_program_options.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_serialization.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_filesystem.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_regex.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_chrono.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_system.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/local/lib/libboost_thread.so.1.60.0...(no debugging symbols found)...done.
Reading symbols from /usr/lib/x86_64-linux-gnu/libstdc++.so.6...(no debugging symbols found)...done.
Reading symbols from /lib/x86_64-linux-gnu/libm.so.6...Reading symbols from /usr/lib/debug/.build-id/b1/6024064374c71ba2d7a6bf25c3c0a2c394f4fb.debug...done.
done.
Reading symbols from /lib/x86_64-linux-gnu/libgcc_s.so.1...(no debugging symbols found)...done.
Reading symbols from /lib/x86_64-linux-gnu/libpthread.so.0...Reading symbols from /usr/lib/debug/.build-id/6e/07318079b168ccc1b4aaf05620aa9ae483ff67.debug...done.
done.
[New LWP 27139]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Reading symbols from /lib/x86_64-linux-gnu/libc.so.6...Reading symbols from /usr/lib/debug/.build-id/4e/edb9af5134e5682b672a7bbccc5884a8569815.debug...done.
done.
Reading symbols from /usr/lib/x86_64-linux-gnu/libssl.so.1.0.2...(no debugging symbols found)...done.
Reading symbols from /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.2...(no debugging symbols found)...done.
Reading symbols from /usr/lib/x86_64-linux-gnu/libicudata.so.55...(no debugging symbols found)...done.
Reading symbols from /usr/lib/x86_64-linux-gnu/libicui18n.so.55...(no debugging symbols found)...done.
Reading symbols from /usr/lib/x86_64-linux-gnu/libicuuc.so.55...(no debugging symbols found)...done.
Reading symbols from /lib64/ld-linux-x86-64.so.2...Reading symbols from /usr/lib/debug/.build-id/fb/2f658b000c9c478337bc1dab4f7605edbfbdca.debug...done.
done.
Reading symbols from /lib/x86_64-linux-gnu/libdl.so.2...Reading symbols from /usr/lib/debug/.build-id/0b/376e85e5b2693beb4f67e335bc7dbef8b7b03b.debug...done.
done.
Reading symbols from /lib/x86_64-linux-gnu/libnss_files.so.2...Reading symbols from /usr/lib/debug/.build-id/d7/fea9cc97150c468890f1815f47e2409faecf86.debug...done.
done.
Reading symbols from /lib/x86_64-linux-gnu/libnss_mdns4_minimal.so.2...(no debugging symbols found)...done.
Reading symbols from /lib/x86_64-linux-gnu/libnss_dns.so.2...Reading symbols from /usr/lib/debug/.build-id/2a/fb53c75885a0cf4e739f43bce9d4bb3e452faf.debug...done.
done.
Reading symbols from /lib/x86_64-linux-gnu/libresolv.so.2...Reading symbols from /usr/lib/debug/.build-id/97/4dd9b8b5b98a72ca82447af126f186dca3359e.debug...done.
done.
pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
185 ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S: No such file or directory.
(gdb) thread apply all bt

Thread 2 (Thread 0x7f418650f700 (LWP 27139)):
#0  0x00007f418916ec03 in select () at ../sysdeps/unix/syscall-template.S:84
#1  0x000000000053f196 in epee::async_stdin_reader::reader_thread_func() ()
#2  0x00007f4189ef03bd in thread_proxy () from /usr/local/lib/libboost_thread.so.1.60.0
#3  0x00007f4189438454 in start_thread (arg=0x7f418650f700) at pthread_create.c:334
#4  0x00007f4189175edd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 1 (Thread 0x7f418b7a4740 (LWP 27138)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00000000004a7f0b in cryptonote::simple_wallet::run() ()
#2  0x000000000048a146 in main ()
(gdb) 


## AJIekceu4 | 2016-04-17T19:20:59+00:00
i found that this error on my system is ONLY after command "refresh".
if i start wallet and do nothing - then wallet sync (but i did't see any sync progress like 1000/1027842).
if i type "refresh" i saw "starting refresh" and see progress, but after time i get this error.


## luigi1111 | 2016-12-15T17:45:36+00:00
@moneromooo-monero @AJIekceu4 What's the status of this?

## AJIekceu4 | 2016-12-15T18:14:55+00:00
Hello. I never seen this problem again in new versions of monero. So i close this issue.

# Action History
- Created by: AJIekceu4 | 2016-04-16T18:08:43+00:00
- Closed at: 2016-12-15T18:14:55+00:00
