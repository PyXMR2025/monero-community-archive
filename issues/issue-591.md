---
title: Compiling error on Arch
source_url: https://github.com/xmrig/xmrig/issues/591
author: ghost
assignees: []
labels: []
created_at: '2018-04-29T08:56:04+00:00'
updated_at: '2018-05-07T03:58:04+00:00'
type: issue
status: closed
closed_at: '2018-04-30T11:48:42+00:00'
---

# Original Description
Having difficulties compiling on Arch Linux
I tried to compile with gcc-6 just in case:
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=/usr/bin/gcc-6 -DCMAKE_CXX_COMPILER=/usr/bin/g++-6
all libs are found:
> -- The C compiler identification is GNU 6.4.1
> -- The CXX compiler identification is GNU 6.4.1
> -- Check for working C compiler: /usr/bin/gcc-6
> -- Check for working C compiler: /usr/bin/gcc-6 -- works
> -- Detecting C compiler ABI info
> -- Detecting C compiler ABI info - done
> -- Detecting C compile features
> -- Detecting C compile features - done
> -- Check for working CXX compiler: /usr/bin/g++-6
> -- Check for working CXX compiler: /usr/bin/g++-6 -- works
> -- Detecting CXX compiler ABI info
> -- Detecting CXX compiler ABI info - done
> -- Detecting CXX compile features
> -- Detecting CXX compile features - done
> -- Found UV: /usr/lib/libuv.so  
> -- Looking for syslog.h
> -- Looking for syslog.h - found
> -- Configuring done
> -- Generating done
> -- Build files have been written to:...

But when I do make it gives me 
> ld: cannot find -luv
> make[2]: *** [CMakeFiles/xmrig.dir/build.make:1111: xmrig] Error 1
> make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
> make: *** [Makefile:84: all] Error 2

and a bunch of garbage on top of that.

# Discussion History
## kpcyrd | 2018-04-29T18:08:19+00:00
```
pacman -S libuv
```

## ghost | 2018-04-29T19:16:42+00:00
I did that of course. libuv-1.20.2-1 installed.
also 
> -- Found UV: /usr/lib/libuv.so

shows that it found it. but when I do which libuv I get this:

> which: no libuv in (/usr/local/sbin:/usr/local/bin:/usr/bin:/opt/cuda/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/home/arch/scripts:/home/arch/scripts)

## donovansolms | 2018-04-30T11:09:29+00:00
I'm also on Arch but can't replicate your issue. `which libuv` also shows not found as yours, but I can compile just fine. My cmake output is identical to yours.

I previously set my environment up for xmr-stak by installing the following
 `sudo pacman -S --needed base-devel hwloc openssl cmake libmicrohttpd`
Not sure if that might help in this case

## ghost | 2018-04-30T11:48:42+00:00
It compiles without -DCMAKE_BUILD_TYPE=Release

## k0ste | 2018-05-07T03:58:04+00:00
[aur/xmrig](https://aur.archlinux.org/packages/xmrig/)

# Action History
- Created by: ghost | 2018-04-29T08:56:04+00:00
- Closed at: 2018-04-30T11:48:42+00:00
