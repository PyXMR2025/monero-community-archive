---
title: Linux 32-bit builds no-worky
source_url: https://github.com/monero-project/monero/issues/103
author: fluffypony
assignees: []
labels: []
created_at: '2014-08-22T07:37:13+00:00'
updated_at: '2015-11-24T14:39:03+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:39:03+00:00'
---

# Original Description
@dbit34 couldn't compile on an Ubuntu 12.04 32-bit VirtualBox, got this error:

```
[ 37%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/difficulty.cpp.o
/home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp: In function ‘void cryptonote::mul(uint64_t, uint64_t, uint64_t&, uint64_t&)’:
/home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:59:22: error: expected unqualified-id before ‘__int128’
     typedef unsigned __int128 uint128_t;
                      ^
/home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:60:5: error: ‘uint128_t’ was not declared in this scope
     uint128_t res = (uint128_t) a * (uint128_t) b;
     ^
/home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:60:15: error: expected ‘;’ before ‘res’
     uint128_t res = (uint128_t) a * (uint128_t) b;
               ^
/home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:61:22: error: ‘res’ was not declared in this scope
     low = (uint64_t) res;
                      ^
make[3]: *** [src/CMakeFiles/cryptonote_core.dir/cryptonote_core/difficulty.cpp.o] Error 1
make[3]: Leaving directory `/home/david/Monero/bitmonero/build/release'
make[2]: *** [src/CMakeFiles/cryptonote_core.dir/all] Error 2
make[2]: Leaving directory `/home/david/Monero/bitmonero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/home/david/Monero/bitmonero/build/release'
make: *** [build-release] Error 2
```

If we're supporting 32-bit Windows builds we should support 32-bit Linux builds. VERY low priority.


# Discussion History
## tewinget | 2014-08-22T07:43:36+00:00
I remember that bit having ifdef stuff w.r.t. uint128_t.  Not sure _why_ it
doesn't play nice with 32-bit Linux, but a trivial workaround would be
applying those same ifdef to it.  That's assuming I'm remembering
correctly, which I'll leave as an exercise for the reader (I'm on my
mobile).
On Aug 22, 2014 3:37 AM, "Riccardo Spagni" notifications@github.com wrote:

> @dbit34 https://github.com/dbit34 couldn't compile on an Ubuntu 12.04
> 32-bit VirtualBox, got this error:
> 
> [ 37%] Building CXX object src/CMakeFiles/cryptonote_core.dir/cryptonote_core/difficulty.cpp.o
> /home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp: In function ‘void cryptonote::mul(uint64_t, uint64_t, uint64_t&, uint64_t&)’:
> /home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:59:22: error: expected unqualified-id before ‘__int128’
>      typedef unsigned __int128 uint128_t;
>                       ^
> /home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:60:5: error: ‘uint128_t’ was not declared in this scope
>      uint128_t res = (uint128_t) a \* (uint128_t) b;
>      ^
> /home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:60:15: error: expected ‘;’ before ‘res’
>      uint128_t res = (uint128_t) a \* (uint128_t) b;
>                ^
> /home/david/Monero/bitmonero/src/cryptonote_core/difficulty.cpp:61:22: error: ‘res’ was not declared in this scope
>      low = (uint64_t) res;
>                       ^
> make[3]: **\* [src/CMakeFiles/cryptonote_core.dir/cryptonote_core/difficulty.cpp.o] Error 1
> make[3]: Leaving directory `/home/david/Monero/bitmonero/build/release'
> make[2]: *** [src/CMakeFiles/cryptonote_core.dir/all] Error 2
> make[2]: Leaving directory`/home/david/Monero/bitmonero/build/release'
> make[1]: **\* [all] Error 2
> make[1]: Leaving directory `/home/david/Monero/bitmonero/build/release'
> make: **\* [build-release] Error 2
> 
> If we're supporting 32-bit Windows builds we should support 32-bit Linux
> builds. VERY low priority.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/103.


## iamsmooth | 2014-08-22T23:41:44+00:00
not supported by gcc, but apparently other people want it so maybe in the future...

https://gcc.gnu.org/bugzilla/show_bug.cgi?id=60846


## mikezackles | 2014-08-22T23:59:54+00:00
I _think_ there are already workarounds for this in the source that we can use.  For example, there are preprocessor switches surrounding the error quoted above that are already in use for MinGW, so this doesn't seem like a show-stopper to me.


## iamsmooth | 2014-08-23T00:03:38+00:00
I think you'd have to have your own 128 bit integer type, math functions, etc. That might be in the code somewhere, but I'm not sure. Does it actually WORK with MinGW on 32 bit? If so, then that should be easily fixable. If not then still fixable, but not not so easily.


## mikezackles | 2014-08-23T00:10:00+00:00
See https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/difficulty.cpp#L48-65

mul128 uses uint64_t

As for working on MinGW 32-bit, time will tell.


## mikezackles | 2014-08-23T00:11:59+00:00
https://github.com/monero-project/bitmonero/blob/master/src/common/int-util.h#L71-95


## iamsmooth | 2014-08-23T00:21:03+00:00
Oh, that looks like it should work. I thought I remembered seeing other places in the code that also use int128, but I just looked and there aren't any, so should be fairly straightforward.


## ghost | 2015-04-22T16:34:59+00:00
Will 32 bit linux be supported in the future?

```
Linux legs 2.6.32-042stab093.4 #1 SMP Mon Aug 11 18:47:39 MSK 2014 i686 i686 i686 GNU/Linux
```

```
/home/ihashfury/tmp/bitmonero/src/crypto/slow-hash.c:558:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     U64(b)[1] = U64(&state.k[16])[1] ^ U64(&state.k[48])[1];
     ^
/home/ihashfury/tmp/bitmonero/src/crypto/slow-hash.c:558:5: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
/home/ihashfury/tmp/bitmonero/src/crypto/slow-hash.c:573:16: error: incompatible types when assigning to type '__m128i' from type 'int'
             _c = _mm_aesenc_si128(_c, _a);
                ^
cc1: all warnings being treated as errors
make[3]: *** [src/crypto/CMakeFiles/crypto.dir/slow-hash.c.o] Error 1
make[3]: Leaving directory `/home/ihashfury/tmp/bitmonero/build/release'
make[2]: *** [src/crypto/CMakeFiles/crypto.dir/all] Error 2
make[2]: Leaving directory `/home/ihashfury/tmp/bitmonero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/home/ihashfury/tmp/bitmonero/build/release'
make: *** [release-all] Error 2
```


## fluffypony | 2015-04-22T16:36:51+00:00
@iPerky yes, we've been working on that and ARM for Linux, so definitely:)


## ghost | 2015-04-22T17:50:33+00:00
I have a full node syncing on archlinuxarm (cubox-i4) - builds and runs well - but takes ages to sync.

Just spun up 64bit VPS instead - should have two full nodes running soon


## fluffypony | 2015-11-24T14:39:03+00:00
Fixed


# Action History
- Created by: fluffypony | 2014-08-22T07:37:13+00:00
- Closed at: 2015-11-24T14:39:03+00:00
