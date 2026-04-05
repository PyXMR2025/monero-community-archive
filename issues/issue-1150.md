---
title: Error compiling by clang in freebsd 11
source_url: https://github.com/xmrig/xmrig/issues/1150
author: Prostoname1
assignees: []
labels:
- bug
created_at: '2019-08-30T06:40:27+00:00'
updated_at: '2019-10-02T08:01:37+00:00'
type: issue
status: closed
closed_at: '2019-10-02T04:48:47+00:00'
---

# Original Description
[ 11%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
/usr/home/andrey/1/xmrig/src/3rdparty/argon2/lib/argon2.c:91:52: error: use of undeclared identifier 'ARGON2_FLAG_GENKAT'
    instance.print_internals = !!(context->flags & ARGON2_FLAG_GENKAT);
                                                                         ^
1 error generated.
*** Error code 1

Stop.
make[2]: stopped in /usr/home/andrey/1/xmrig/build
*** Error code 1

Stop.
make[1]: stopped in /usr/home/andrey/1/xmrig/build
*** Error code 1

Stop.



Gcc9 compile without any errors.

# Discussion History
## xmrig | 2019-08-30T07:49:40+00:00
If you don't need Argon2 support you can disable it by `-DWITH_ARGON2=OFF`, otherwise probably wrong header used, I will check it later.
Thank you.

## OlegKotcar | 2019-09-23T09:02:36+00:00
Xmrig V. 3.1.3 on FreeBSD 12 has the same problem.

## lisergey | 2019-09-23T09:17:17+00:00
why don't you just compile it from ports?
/usr/ports/net-p2p/xmrig

## OlegKotcar | 2019-09-23T22:46:45+00:00
I was tried to compile from ports, but the same error appears.

пн, 23 сент. 2019 г., 17:17 lisergey <notifications@github.com>:

> why don't you just compile it from ports?
> /usr/ports/net-p2p/xmrig
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1150?email_source=notifications&email_token=ACHQYZE4TXF4NE3VHM5SYWTQLCCS5A5CNFSM4ISJ2QAKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOD7KICMA#issuecomment-534020400>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ACHQYZES3XBDAMLDAVSFCCDQLCCS5ANCNFSM4ISJ2QAA>
> .
>


## OlegKotcar | 2019-09-30T01:29:08+00:00
In version 3.2.0
appears new one error
"    instance.print_internals = !!(context->flags & ARGON2_FLAG_GENKAT);
                                                                           ^
1 error generated.
ninja: build stopped: subcommand failed.
"

## lisergey | 2019-09-30T08:10:15+00:00
that's really strange.
I've just successfully upgraded xmrig from ports on 11.3-RELEASE-p3 GENERIC  amd64
```
# pkg inf -q | grep -E "ninja|xmrig"
ninja-1.9.0,2
xmrig-3.2.0
```
try to reinstall ninja & cmake, run `make clean && make cleandir` twice in /usr/src, and `make delete-old`, and freebsd-update to latest patches.

## lisergey | 2019-09-30T08:15:43+00:00
> Xmrig V. 3.1.3 on FreeBSD 12 has the same problem.

I have several FreeBSD 12 machines, where I've tried to compile xmrig-3.1.3 from ports.
That's really strange, but it did successfully on most and stopped with errors on two.
They should be identical by means of updates, libs, /usr/src, but conclusion is they are not. 
These hidden difference is villain and causing the compile error, not the code.

## xmrig | 2019-09-30T09:50:38+00:00
Maybe some another argon2 package installed with `argon2.h` header? potentially it can make conflict.

## lisergey | 2019-09-30T11:09:09+00:00
> Maybe some another argon2 package installed with `argon2.h` header? potentially it can make conflict.

seems it does. 
There is installed `/usr/ports/security/libargon2` as a dependency for php72 where compile fails.
So maybe to adapt cmake files to pick the right one?

## OlegKotcar | 2019-09-30T12:22:31+00:00
pkg info -q | grep ninja
ninja-1.9.0,2

portsnap fetch update - OK
/usr/ports/security/libargon2 make reinstall clean - OK
/usr/ports/devel/ninja make distclean - OK
/usr/ports/devel/ninja make reinstall clean - 
===>  Building for ninja-1.9.0,2
bootstrapping ninja...
warning: A compatible version of re2c (>= 0.11.3) was not found; changes to src/*.in.cc will not affect your build.
Installing ninja-1.9.0,2... - OK
/usr/ports/net-p2p/xmrig make install clean - The same error:
2: error: use of undeclared identifier 'ARGON2_FLAG_GENKAT'
    instance.print_internals = !!(context->flags & ARGON2_FLAG_GENKAT);
                                                   ^
1 error generated.
ninja: build stopped: subcommand failed.
*** Error code 1

Stop.
make[1]: stopped in /usr/ports/net-p2p/xmrig
*** Error code 1




## OlegKotcar | 2019-09-30T12:42:30+00:00
freebsd-update fetch
freebsd-update install - Installing updates... done.
Nothing has changed...

## OlegKotcar | 2019-09-30T12:46:17+00:00
> 
> Maybe some another argon2 package installed with `argon2.h` header? potentially it can make conflict.

Which program can installed  another `argon2.h` ?

## xmrig | 2019-09-30T18:24:42+00:00
@lisergey yep this is it, fixed in evo branch.
Thank you.

## xmrig | 2019-10-02T04:48:47+00:00
https://github.com/xmrig/xmrig/releases/tag/v4.2.1-beta

## OlegKotcar | 2019-10-02T08:01:36+00:00
> 
> 
> https://github.com/xmrig/xmrig/releases/tag/v4.2.1-beta

Thanks!  v4.2.1-beta compiled without error.

# Action History
- Created by: Prostoname1 | 2019-08-30T06:40:27+00:00
- Closed at: 2019-10-02T04:48:47+00:00
