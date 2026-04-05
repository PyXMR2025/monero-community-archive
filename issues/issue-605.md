---
title: 'Help cross compiling for PPC64 '
source_url: https://github.com/xmrig/xmrig/issues/605
author: asanchez500
assignees: []
labels: []
created_at: '2018-05-06T00:23:45+00:00'
updated_at: '2018-06-17T18:12:42+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:12:42+00:00'
---

# Original Description
I got cmake to work... Just havn't figured out this fatal error in make when cross compiling...  Im trying to cross compile for a PS3 to see if it can mine monero. Would compiling the older stak work at all? 

> root@debian:/home/asanchez500/xmrig# make --arch=PPC64
[ 13%] Built target cpuid
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
In file included from /home/asanchez500/xmrig/src/api/Api.cpp:27:0:
/home/asanchez500/xmrig/src/api/Api.h:28:16: fatal error: uv.h: No such file or directory
 #include <uv.h>
                ^
compilation terminated.
CMakeFiles/xmrig.dir/build.make:62: recipe for target 'CMakeFiles/xmrig.dir/src/api/Api.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2  > 




# Discussion History
## Balzhur | 2018-05-07T06:49:00+00:00
I would really appreciate if @xmrig added support for ppc64. 

For now you can use xmr-stak fork for Power. It's based on 2.3.0 version of xmr-stak, not latest version, but it works with CryptonightV7.
https://github.com/nioroso-x3/xmr-stak

PS: @xmrig if you decide to add ppc64 support - I can help with testing.

## asanchez500 | 2018-05-07T11:34:40+00:00
Im running fedora 9 on ppc64. Cmake has to be at 3.4 for it to compile apparently. Im on cmake 2.4. Ive tried cross compiling with no luck though. Do yoy know how to cross compile? Im willing to pay some one money to get this miner running.... 

Sent from Yahoo Mail on Android 
 
  On Sun, May 6, 2018 at 11:49 PM, Balzhur<notifications@github.com> wrote:   
I would really appreciate if @xmrig added support for ppc64.

For now you can use xmr-stak fork for Power. It's based on 2.3.0 version of xmr-stak, not latest version, but it works with CryptonightV7.
https://github.com/nioroso-x3/xmr-stak

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub, or mute the thread.
    


## asanchez500 | 2018-05-15T02:55:48+00:00
Yea I couldn't get Xmr-Stak to run at all as well. Some kind of dependency issue apparently Cmake isn't up to date. I will go ahead and look for the latest LINUX OS to load on PS3 but most distributions are old and no one seems to be developing for the PS3 anymore and PS4 is no longer supporting linux. I don't get why no one has bother with a PS3 cluster since it is very cheap processsing power for the time being. I mean very cheap. I hope others figure this out as well. I am going to go ahead and try porting XMR in assembly to PPC64 and see if I can get it to work. I will let you all know how my endeavor goes... 

# Action History
- Created by: asanchez500 | 2018-05-06T00:23:45+00:00
- Closed at: 2018-06-17T18:12:42+00:00
