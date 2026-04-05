---
title: hwloc issue
source_url: https://github.com/xmrig/xmrig/issues/1159
author: xday3
assignees: []
labels:
- question
created_at: '2019-09-03T23:20:09+00:00'
updated_at: '2021-08-06T19:17:43+00:00'
type: issue
status: closed
closed_at: '2019-09-13T16:27:57+00:00'
---

# Original Description
I tried to compile xmrig static - cmake .. -DUV_LIBRARY=/usr/local/lib/libuv.a -DBUILD_STATIC=-ON

 * ABOUT        XMRig/3.1.1 gcc/5.4.0
 * LIBS         libuv/1.31.1-dev hwloc/1.11.2
 * CPU          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (1) x64 AES
                L2:0.0 MB L3:0.0 MB 2C/2T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      104.140.201.42:80:3333 algo cn/r
 * COMMANDS     hashrate, pause, resume
[2019-09-03 19:17:03.169] use pool 104.140.201.42:80  104.140.201.42
[2019-09-03 19:17:03.169] new job from 104.140.201.42:80 diff 10000 algo cn/r height 1915339

The problem what I got is, when I am using my miner to another machine I got this error:
./xmrig-notls: error while loading shared libraries: libhwloc.so.5: cannot open shared object file: No such file or directory

Can anyone know how can I fix it?




# Discussion History
## xday3 | 2019-09-04T00:52:46+00:00
Any update :)

## trasherdk | 2019-09-04T00:53:43+00:00
You need to compile a static libhwloc from source.

## xmrig | 2019-09-04T00:58:11+00:00
You have 2 options:
1. Use own hwloc build https://github.com/xmrig/xmrig/issues/1099#issuecomment-518089405 (better option)
2. Disable it `-DWITH_HWLOC=OFF`

Please note hwloc may not work well in virtual environment, zero cache detected `L2:0.0 MB L3:0.0`
Thank you.

## trasherdk | 2019-09-04T01:03:14+00:00
@xmrig VirtualBox 6.0.10 guest, running Slackware 14.2
```
 * ABOUT        XMRig/3.1.0 gcc/5.5.0
 * LIBS         libuv/1.23.2 OpenSSL/1.0.2s hwloc/1.11.0
 * CPU          Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz (1) x64 AES
                L2:1.0 MB L3:32.0 MB 4C/4T NUMA:1
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      localhost:8000 algo cn/r
 * COMMANDS     hashrate, pause, resume
[2019-09-04 02:59:47.865] use pool localhost:8000  127.0.0.1
[2019-09-04 02:59:47.868] new job from localhost:8000 diff 1000 algo cn/r height 1291897
[2019-09-04 02:59:47.868]  cpu  use profile  cn  (4 threads) scratchpad 2048 KB
[2019-09-04 02:59:48.745]  cpu  READY threads 4(4) huge pages 4/4 100% memory 8192 KB (876 ms)
[2019-09-04 02:59:52.876] accepted (1/0) diff 1000 (98 ms)
[2019-09-04 03:00:03.363] accepted (2/0) diff 1000 (169 ms)
[2019-09-04 03:00:09.688] accepted (3/0) diff 1000 (190 ms)
[2019-09-04 03:00:10.983] Ctrl+C received, exiting
[2019-09-04 03:00:11.025]  cpu  stopped (41 ms)
```
Looks OK to me :)


## kio3i0j9024vkoenio | 2019-09-04T03:09:37+00:00
LIBS libuv/1.23.2 OpenSSL/1.0.2s hwloc/1.11.0

You will get terrible hash rates with hwloc v1.11.0.

You need at least V2.0.4

```
wget https://download.open-mpi.org/release/hwloc/v2.0/hwloc-2.0.4.tar.gz
tar xvzf hwloc-2.0.4.tar.gz

cd hwloc-2.0.4

sudo apt install autoconf
sudo apt install libtool-bin

Note that GNU autoconf >=2.63, automake >=1.11 and Libtool >=2.2.6 are required when building from a Git clone.

autoconf -V
automake --version
libtool --version

./configure

make
sudo make install
```

## xday3 | 2019-09-04T13:34:01+00:00
Thank you very much for your helps, finally I compiled my miner fully static with hwloc 2.0 and libuv.


## RizkiRama99 | 2019-10-25T14:41:57+00:00
This is the way https://junglecrypto.blogspot.com/2019/10/how-to-fix-hwloc-issue-when-running.html

## zrayburn | 2020-07-22T00:20:50+00:00
This can also be fixed using the apt package manager.
`sudo apt install hwloc`
I don't know if this library is present in other package managers but it worked for me.

## TheColetrain | 2021-05-20T16:56:31+00:00
`sudo apt install hwloc` is a winner

# Action History
- Created by: xday3 | 2019-09-03T23:20:09+00:00
- Closed at: 2019-09-13T16:27:57+00:00
