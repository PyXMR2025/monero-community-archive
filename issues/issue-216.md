---
title: support ARMv7?
source_url: https://github.com/xmrig/xmrig/issues/216
author: gennadicho
assignees: []
labels:
- enhancement
- arm
created_at: '2017-11-22T08:40:38+00:00'
updated_at: '2020-05-27T13:37:36+00:00'
type: issue
status: closed
closed_at: '2017-11-26T20:23:41+00:00'
---

# Original Description
Hi. Will there be support armv7? old phones, cubieboards, and other things.

# Discussion History
## semeion | 2017-11-22T18:00:54+00:00
I tried to compile on a raspberry pi 3 B and got an error, could be nice have xmrig running on my RPi3 but i have no idea if it is possible.

```
$ make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make:63: src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:123: src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```


## gennadicho | 2017-11-22T23:45:36+00:00
@semeion you not switch to the arm branch. Look "-maes" gcc flags? You try to compile x86 sources. Try git fetch origin arm ; git checkout arm on xmrig directory.

## gennadicho | 2017-11-22T23:51:23+00:00
@semeion but another problem is xmrig not support armv7, you can find this info in roadmap(only aarch64 aka armv8)

## xmrig | 2017-11-23T14:35:07+00:00
I got idea where I can get some ARMv7 hardware, I will check it tomorrow, hopefully only cmake changes required, until CPU supports NEON extensions.
But as I know hardware AES supported only in ARMv8.

## gennadicho | 2017-11-23T14:49:46+00:00
@xmrig, nice, thanks! You may buy random china android phone, and set up debian chroot on this :-) if you can not find armv7 hardware - i have many of them, and may to get you ssh to one of this "machine". But my phone is bit a slow and have bad internet connection. 

## gennadicho | 2017-11-23T14:55:43+00:00
@xmrig Yep, AES only on ARMv8. :( 

/proc/cpuinfo from one my phone:
`root@localhost:~# cat /proc/cpuinfo 
Processor       : ARMv7 Processor rev 5 (v7l)
processor       : 0
model name      : ARMv7 Processor rev 5 (v7l)
BogoMIPS        : 2413.36
Features        : swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt 
CPU implementer : 0x41
CPU architecture: 7
CPU variant     : 0x0
CPU part        : 0xc07
CPU revision    : 5

processor       : 1
model name      : ARMv7 Processor rev 5 (v7l)
BogoMIPS        : 2413.36
Features        : swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt 
CPU implementer : 0x41
CPU architecture: 7
CPU variant     : 0x0
CPU part        : 0xc07
CPU revision    : 5

processor       : 2
model name      : ARMv7 Processor rev 5 (v7l)
BogoMIPS        : 2413.36
Features        : swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt 
CPU implementer : 0x41
CPU architecture: 7
CPU variant     : 0x0
CPU part        : 0xc07
CPU revision    : 5

processor       : 3
model name      : ARMv7 Processor rev 5 (v7l)
BogoMIPS        : 2413.36
Features        : swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt 
CPU implementer : 0x41
CPU architecture: 7
CPU variant     : 0x0
CPU part        : 0xc07
CPU revision    : 5

Hardware        : sc8830
Revision        : 0000
Serial          : 0000000000000000
`

## gennadicho | 2017-11-24T16:30:29+00:00
I make many dumb editing in code, only CryptoNight.cpp not compile :(

> In file included from /tmp/xmrig/src/crypto/CryptoNight_arm64.h:33:0,
                 from /tmp/xmrig/src/crypto/CryptoNight.cpp:27:
/tmp/xmrig/src/crypto/soft_aes.h: In function ‘__m128i soft_aeskeygenassist(__m128i)’:
/tmp/xmrig/src/crypto/soft_aes.h:122:37: error: there are no arguments to ‘_rotr’ that depend on a template parameter, so a declaration of ‘_rotr’ must be available [-fpermissive]
     return _mm_set_epi32(_rotr(X3, 8) ^ rcon, X3, _rotr(X1, 8) ^ rcon, X1);
                                     ^
/tmp/xmrig/src/crypto/soft_aes.h:122:37: note: (if you use ‘-fpermissive’, G++ will accept your code, but allowing the use of an undeclared name is deprecated)
/tmp/xmrig/src/crypto/soft_aes.h:122:62: error: there are no arguments to ‘_rotr’ that depend on a template parameter, so a declaration of ‘_rotr’ must be available [-fpermissive]
     return _mm_set_epi32(_rotr(X3, 8) ^ rcon, X3, _rotr(X1, 8) ^ rcon, X1);
                                                              ^
In file included from /tmp/xmrig/src/crypto/CryptoNight.cpp:27:0:
/tmp/xmrig/src/crypto/CryptoNight_arm64.h: In function ‘__m128i _mm_set_epi64x(uint64_t, uint64_t)’:
/tmp/xmrig/src/crypto/CryptoNight_arm64.h:71:55: note: use -flax-vector-conversions to permit conversions between vectors with differing element types or numbers of subparts
     return vcombine_u64(vcreate_u64(b), vcreate_u64(a));
                                                       ^
/tmp/xmrig/src/crypto/CryptoNight_arm64.h:71:55: error: cannot convert ‘uint64x2_t {aka __vector(2) __builtin_neon_udi}’ to ‘__m128i {aka __vector(4) __builtin_neon_si}’ in return
/tmp/xmrig/src/crypto/CryptoNight_arm64.h: In function ‘uint64_t _mm_cvtsi128_si64(__m128i)’:
/tmp/xmrig/src/crypto/CryptoNight_arm64.h:78:31: error: cannot convert ‘__m128i {aka __vector(4) __builtin_neon_si}’ to ‘uint64x2_t {aka __vector(2) __builtin_neon_udi}’ for argument ‘1’ to ‘uint64_t vgetq_lane_u6
4(uint64x2_t, int)’
     return vgetq_lane_u64(a, 0);


## xmrig | 2017-11-26T19:31:53+00:00
I added ARMv7 support. It slow, need emulate 64 bit multiplication (same as 32bit x86) and AES as well.
Thank you.

## gennadicho | 2017-11-26T20:03:50+00:00
@xmrig big-big thanks! Ha-ha. I try it today :-)

## gennadicho | 2017-11-26T20:23:41+00:00
nice, everything works. :) thanks again

## demian2g | 2017-12-17T14:01:09+00:00
Does anybody have compiled armv7 version? Trying to make on OrangePi (rasp-like) - only errors. Thanks

## semeion | 2017-12-17T14:18:12+00:00
@demian2g yes i did. it is working fine.

I am using Raspberry pi 3B with ArchLinux ARM 32bits, to compile i used:

CFLAGS="-march=armv7-a -mfloat-abi=hard -mfpu=vfpv3-d16 -O2 -pipe -fstack-protector-strong -fno-plt" CXXFLAGS="-march=armv7-a -mfloat-abi=hard -mfpu=vfpv3-d16 -O2 -pipe -fstack-protector-strong -fno-plt" cmake .. -DWITH_HTTPD=OFF && make VERBOSE=1


## demian2g | 2017-12-17T15:41:19+00:00
@semeion thanks, but still MHD_LIBRARY (ADVANCED) error. I'm using OrangePi Plus 2 with Ubuntu Vivid and not sure that have correctly installed all compilers and libraries. Just wanted to see how much h/s can it generate

## semeion | 2017-12-18T01:36:53+00:00
I have no idea how to help you. I never used Ubuntu and/or OrangePi.

## SergeyStaroletov | 2017-12-19T12:34:29+00:00
@demian2g  just delete all the files in directory and rerun the compilation again. hashrate on rpi3 is 6h/s max :)))

## jgillich | 2017-12-23T20:00:47+00:00
My hashrate on a RPi3 is ~7.4 (running Fedora aarch64).

## SergeyStaroletov | 2017-12-23T20:20:42+00:00
@jgillich Can it use something like -x64 -AES-NI extensions in aarch64 mode? 

## jgillich | 2017-12-23T20:22:50+00:00
I don't think so, I have to use `--av 3` because it segfaults otherwise. Haven't really figured out why though.

## supercodechen | 2018-01-05T06:36:31+00:00
I have build successful on armv7l ,application could get job,but the rate is n/a H/s,I try to change config,like av : 4;algo : cyptonight-lite; But the rate is still n/a H/s，So, I need your help,@xmring

## supercodechen | 2018-01-05T06:39:33+00:00
oh~ps: when I change av to 2，the application return a err:"cryptonight-lite" hash self-test failed.

## supercodechen | 2018-01-05T09:00:20+00:00
@xmrig 

## rainmo | 2018-01-17T09:32:51+00:00
@semeion Hi, buddy. I met same problem when i complied xmrig used in RPI-3B-centos.  can u tell me how to use "cmake .. && make". Thanks.

## jgrabenstein | 2018-02-05T03:27:46+00:00
I’m able to get 9.3h/s on raspbian/cpuminer-multi with my pi 3. Heard aarch64 and xmrig was supposed to be faster but from the above comments that doesn’t seem to be the case. Anyone else achieve better? (Different compiliarion flags etc...)

## gennadicho | 2018-02-05T12:27:41+00:00
@rainmo what the problem? Paste some logs

## gennadicho | 2018-02-05T12:29:01+00:00
@jgrabenstein off course aarch64 with huge pages faster. I have phone wileyfox spark, cpuminer-multi = 9-10h/s, xmrig = 15-20 h/s

## jgrabenstein | 2018-02-05T16:57:48+00:00
@gennadicho thanks for confirming. Above comments made me apprehensive to try. Have 2 more boards coming tomorrow will give aarch64/xmrig a shot. 

## ghost | 2018-03-08T05:05:28+00:00
The instructions for building on Ubuntu work for my build, but I'd like to try tuning for my architecture by setting different values for CFLAGS and CXXFLAGS...  Is this possible?

## xmrig | 2018-03-08T05:09:33+00:00
https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L17 for gcc, separated for v8/v7
https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L58 for clang, also separated.
Thank you.

## ghost | 2018-03-08T05:39:06+00:00
I guess i should have mentioned that I'm new to linux and cmake... So, I see the various flags from the *.cmake files above, but I'm not clear on how they are applied at build-time.  Where in the build process can I see which flags are applied and also set my own?

Also, thanks for the quick reply!  I love the project!

## xmrig | 2018-03-08T06:01:33+00:00
You need change `CMAKE_C_FLAGS` and `CMAKE_CXX_FLAGS` and run `make`.
To determinate what line need change need know what compiler you use: gcc/clang and CPU arch: ARMv8/ARMv7.
Thank you.

## SlastikhinNikita | 2019-03-11T19:09:45+00:00
Can I download build releases somewhere? 

## James-yaoshenglong | 2020-05-27T13:37:35+00:00
I clone the source code from GitHub and compile and make it on a raspberry pi 4B with a pi os and it shows the below errors，I can not solve it .
It wellly run through the compile stage and in the link stage it shows these errors

collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3029: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Action History
- Created by: gennadicho | 2017-11-22T08:40:38+00:00
- Closed at: 2017-11-26T20:23:41+00:00
