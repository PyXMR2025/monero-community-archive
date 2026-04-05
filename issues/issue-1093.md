---
title: xmrig build make on ubuntu
source_url: https://github.com/xmrig/xmrig/issues/1093
author: akunredmi26
assignees: []
labels:
- question
- need feedback
created_at: '2019-08-01T08:26:39+00:00'
updated_at: '2020-02-09T10:40:13+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:40:13+00:00'
---

# Original Description
[  1%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
gcc-7: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make:63: src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:128: src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

please help me..

# Discussion History
## xmrig | 2019-08-02T11:19:26+00:00
Please provide more details, you try build for ARM device?
Thank you.

## Spudz76 | 2019-08-02T19:09:58+00:00
What does `gcc-7 -v` say about itself?  The `-maes` option has been accepted since almost forever (gcc-4.8?)  And yes, is it even `x86_64-linux-gnu` or some other platform.

gcc-7 (version `7.4.0-1ubuntu1~18.04.1`) works fine for me, though I generally use the gcc-9 from [PPA ubuntu-toolchain-r-test](https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test) mainly because then it's the same compiler version on all Ubuntu releases.

But lately have had best results with clang-9 so haven't really been using gcc other than to see if it still compiles occasionally (and if it got any faster than clang-9).  I run a lot of CPUs where there is no optimized ASM module so the compiler (and how it decides to optimize its resulting ASM) makes a much bigger difference.

gcc-4.9.3 is definitely broken since the RandomX rework that dropped the external lib, and clang-3.5.0 no longer works at the same breakage point (I think the new code has some C++17 and other weird tricks in it which break true C++11?)

## akunredmi26 | 2019-08-04T07:09:55+00:00
u0_a64@localhost
OS: Android 6.0.1 armv8l
Host: Amlogic HG680-P
Kernel: 3.14.29
Uptime: 18 mins
Packages: 72 (dpkg), 1 (pkg)
Shell: bash 5.0.7
Terminal: com.termux
CPU: (4) @ 1.512GHz
Memory: 977MiB / 1774MiB

and i install ubuntu from https://github.com/Neo-Oli/termux-ubuntu

root@localhost:~# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=19.04
DISTRIB_CODENAME=disco
DISTRIB_DESCRIPTION="Ubuntu 19.04"

## seanwhe | 2019-08-08T19:06:24+00:00
There is not much info to go on in your post so I will just assume you're on Ubuntu 18.0.4.2 LTS.

Here's my setup and solution.

~$ hostnamectl
   Static hostname: sean-work-wks
         Icon name: computer-desktop
           Chassis: desktop
        Machine ID: c4b916b14b1343f793d27e0150252bf3
           Boot ID: 4920a88b82844fd1b2e91cf482dfc051
  Operating System: Ubuntu 18.04.2 LTS
            Kernel: Linux 4.15.0-55-generic
      Architecture: x86-64

~$ uname -a
Linux sean-work-wks 4.15.0-55-generic #60-Ubuntu SMP Tue Jul 2 18:22:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

~$ sudo apt-cache policy gcc
gcc:
  Installed: 4:7.4.0-1ubuntu2.3
  Candidate: 4:7.4.0-1ubuntu2.3
  Version table:
 *** 4:7.4.0-1ubuntu2.3 500
        500 http://za.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages
        100 /var/lib/dpkg/status
     4:7.3.0-3ubuntu2 500
        500 http://za.archive.ubuntu.com/ubuntu bionic/main amd64 Packages

~$ sudo apt-cache policy g++
g++:
  Installed: 4:7.4.0-1ubuntu2.3
  Candidate: 4:7.4.0-1ubuntu2.3
  Version table:
 *** 4:7.4.0-1ubuntu2.3 500
        500 http://za.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages
        100 /var/lib/dpkg/status
     4:7.3.0-3ubuntu2 500
        500 http://za.archive.ubuntu.com/ubuntu bionic/main amd64 Packages

See my xmrig-bash-scripts for full steps I have taken to build, install and configure xmrig.
They are a bit blunt and lack finesse but I have run them on 30 hosts behind an xmrig-proxy 
and it works each time.

https://github.com/seanwhe/xmrig-bash-scripts/blob/master/depends.sh

https://github.com/seanwhe/xmrig-bash-scripts/blob/master/build.sh

https://github.com/seanwhe/xmrig-bash-scripts/blob/master/functions.sh

Hope this helps

# Action History
- Created by: akunredmi26 | 2019-08-01T08:26:39+00:00
- Closed at: 2020-02-09T10:40:13+00:00
