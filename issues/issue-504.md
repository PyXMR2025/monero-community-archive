---
title: V2.5 V2.5.2 V2.6 Failed to compile gcc v7.3 CentOS
source_url: https://github.com/xmrig/xmrig/issues/504
author: tanwaarpornthip
assignees: []
labels: []
created_at: '2018-04-05T17:34:47+00:00'
updated_at: '2018-11-05T13:20:12+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:20:12+00:00'
---

# Original Description
CentOS 6.9
gcc v7.3
cmake v3.11
libuv v1.9.1


cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/local/lib/libuv.a

```
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: /usr/local/bin/gcc
-- Check for working C compiler: /usr/local/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/local/bin/g++
-- Check for working CXX compiler: /usr/local/bin/g++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /usr/local/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found MHD: /usr/local/lib/libmicrohttpd.so
-- Configuring done
-- Generating done
-- Build files have been written to: /home/user/src/xmrig-2.5.2/build
```
make

```
[Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
In file included from /home/user/src/xmrig-2.5.2/src/api/ApiState.h:28:0,
                 from /home/user/src/xmrig-2.5.2/src/api/Api.cpp:28:
/home/user/src/xmrig-2.5.2/src/api/NetworkState.h:28:10: fatal error: array: No such file or directory
 #include <array>
          ^~~~~~~
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2](url)
```

# Discussion History
## JustHoldit | 2018-04-06T20:33:04+00:00
Upgrade your version of libuv to version 1.18. This should fix the problem.

## tanwaarpornthip | 2018-04-07T06:22:28+00:00
@JustHoldit I updated libuv to 1.20. Still get the same error. Any suggestions? Here's the setup now

CentOS 6.9
gcc v7.3
cmake v3.11
libuv v1.20



## JustHoldit | 2018-04-08T03:51:35+00:00
I dunno. I just compiled successfully on CentOS 7 and open SUSE Leap 42.3.

Send the results of:   uname -a
and
rpm -qa | grep gcc

## tanwaarpornthip | 2018-04-08T08:31:24+00:00
uname -a

`Linux somedoma.in 2.6.32-696.10.1.el6.x86_64 #1 SMP Tue Aug 22 18:51:35 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux`

rpm -qa | grep gcc (Note that the gcc version here is not the version I used to compile. As you can see from cmake result, gcc used is in /usr/local/bin. It's newer than the system-wide version"

```
libgcc-4.4.7-18.el6_9.2.x86_64
mpitests_openmpi_gcc-3.2-923.x86_64
mpitests_mvapich_gcc-3.2-923.x86_64
gcc-gfortran-4.4.7-18.el6_9.2.x86_64
devtoolset-2-gcc-c++-4.8.2-15.el6.x86_64
gcc-4.4.7-18.el6_9.2.x86_64
libgcc-4.4.7-18.el6_9.2.i686
mvapich_gcc-1.2.0-3635.x86_64
gcc-c++-4.4.7-18.el6_9.2.x86_64
openmpi_gcc-1.4.3-1.x86_64
devtoolset-2-gcc-4.8.2-15.el6.x86_64
```
gcc --version
```
gcc (GCC) 7.3.0
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

environment variables
```
HOSTNAME=somedoma.in
TERM=xterm
SHELL=/bin/bash
ECLIPSE_HOME=/opt/eclipse
HISTSIZE=1000
JASPERINC=/usr/include/jasper
SGE_CELL=default
SGE_ARCH=lx26-amd64
MPICH_PROCESS_GROUP=no
QTDIR=/usr/lib64/qt-3.3
QTINC=/usr/lib64/qt-3.3/include
ROCKSROOT=/opt/rocks/share/devel
SSH_TTY=/dev/pts/1
ANT_HOME=/opt/rocks
USER=XXX
LD_LIBRARY_PATH=/share/apps/lib64:/share/apps/lib:/opt/gridengine/lib/lx26-amd64:/opt/openmpi/lib
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lz=01;31:*.xz=01;31:*.bz2=01;31:*.tbz=01;31:*.tbz2=01;31:*.bz=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.rar=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:
ROCKS_ROOT=/opt/rocks
MAVEN_HOME=/opt/maven
MAIL=/var/spool/mail/XXX
PATH=/opt/openmpi/bin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/eclipse:/opt/ganglia/bin:/opt/ganglia/sbin:/opt/bin:/usr/java/latest/bin:/opt/maven/bin:/opt/rocks/bin:/opt/rocks/sbin:/opt/gridengine/bin/lx26-amd64:/home/XXX/bin
JASPERLIB=/usr/lib64
PWD=/home/XXX
_LMFILES_=/usr/share/Modules/modulefiles/rocks-openmpi
JAVA_HOME=/usr/java/latest
SGE_EXECD_PORT=537
LANG=en_US.iso885915
SGE_QMASTER_PORT=536
MODULEPATH=/usr/share/Modules/modulefiles:/etc/modulefiles
SGE_ROOT=/opt/gridengine
LOADEDMODULES=rocks-openmpi
CXX=/usr/local/bin/g++
SSH_ASKPASS=/usr/libexec/openssh/gnome-ssh-askpass
HISTCONTROL=ignoredups
SHLVL=1
HOME=/home/XXX
ROLLSROOT=/opt/rocks/share/devel/src/roll
MPIHOME=/opt/openmpi
LOGNAME=XXX
QTLIB=/usr/lib64/qt-3.3/lib
CVS_RSH=ssh
LC_CTYPE=UTF-8
MODULESHOME=/usr/share/Modules
LESSOPEN=||/usr/bin/lesspipe.sh %s
CC=/usr/local/bin/gcc
G_BROKEN_FILENAMES=1
BASH_FUNC_module()=() {  eval `/usr/bin/modulecmd bash $*`
}
_=/bin/env
```

## NmxMilk | 2018-04-10T08:46:28+00:00
The message is indicating thar the include file "array" cannot be found.
Either it is missing on your system or the include path is somehow wrong.

Use make VERBOSE=1 to check the include options used.

You should find your include file in:
/usr/local/include/c++/7.3.0/array
and as it says :
/** @file include/array
 *  This is a Standard C++ Library header.
 */

# Action History
- Created by: tanwaarpornthip | 2018-04-05T17:34:47+00:00
- Closed at: 2018-11-05T13:20:12+00:00
