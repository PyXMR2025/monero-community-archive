---
title: Build issues on Raspberry Pi 3b+ running 64bit OS
source_url: https://github.com/xmrig/xmrig/issues/960
author: grahamreeds
assignees: []
labels:
- arm
created_at: '2019-02-28T17:19:21+00:00'
updated_at: '2019-08-02T13:18:03+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:18:03+00:00'
---

# Original Description
I am compiling on a Raspberry Pi 3b+ running a 64 bit version of raspbian (https://github.com/Crazyhead90/pi64/releases/tag/2018-04-17).

I have also built gcc-8.1.0 from scratch (https://solarianprogrammer.com/2017/12/07/raspberry-pi-raspbian-compiling-gcc/).

These and a some light overclocking has got me from 5.2H/s to 9.3H/s. :-)

The latest version of 2.13.1 has some compilation issues.

It may be due to my weird home brew system but I can't use `-static-libgcc -static-libstdc++` instead having to use `-lgcc -lstdc++`.

Also the detection routine for the AES on ARM is flawed (or CMakes is).  The Raspberry Pi definitely doesn't have AES in hardware. 

`gcc-8.1.0 -mcpu=native -march=native -Q --help=target` gives `-march` as `armv8-a+crc+simd`.

I replaced the `set` with "`-march=armv8-a -mtune=cortex-a53 -mfpu=neon-fp-armv8`".

Obviously this is Pi3-centric but thought it might help.



# Discussion History
## xmrig | 2019-03-01T16:54:58+00:00
For recent versions AES detection should be work correctly in compile and runtime phase.
If compiler not support `-march=armv8-a+crypto` will be used `-march=armv8-a` https://github.com/xmrig/xmrig/blob/master/cmake/cpu.cmake#L37

Thanks for information about `-static-libgcc -static-libstdc++`, need think what better do with it.

## cheltamel | 2019-06-27T09:54:16+00:00
grahamreeds: what overclocking did you do? Interested in getting a better hashrate out of my RPI 3b+

## grahamreeds | 2019-06-27T13:33:10+00:00
TL;DR
Install 64bit Raspbian.
Install GCC 8.x
Overclock Ram.

This is a post I started for my website and never finished.  Part 4 is
about getting opencl port working and requires a lot more work to organise
my notes and actually processing hashes.  Also I moved to 64bit Raspbian so
ignore the Gentoo install - using 64bit gives a 20% speed increase.  Before
the change in algorithm I was getting 9.3H/s

0. Preface

I have had a play with mining on a Raspberry Pi and thought I would do
a more formal thing.

I have been compiled gcc, modifed source (not difficult for me as I am
a dev for a living but not really contributed to other OS projects)
and mined part of a coin.

But it has been very piece meal.

So I thought I would roll it back to the start.

Since running 4 cores a 100% generates a lot of heat, I am using a
Raspberry Pi3b+ which has better thermal management and running in a
GeeekPi Armour case - which is essentially a clamshell heatsink and
fan.  The most highest temp I have seen that board run is 42'C.

So let's start again. First we need an OS. We will start with
Rasbian-lite which is a 32bit OS and later we will try Gentoo64 which
is one of few decent 64bit OS which hasn't fallen off the radar in the
last few years.

Gentoo is a bit heavyweight so as starter I will remove most of the
heavy features we don't want or need (LibreOffice, browsers, etc.).

1. 32 bit - gcc6.3.0
Building the client is exactly as it describes in the wiki for xmrig.
You first install the usual suspects (git, build-essentials, cmake,
etc) and then send it on it's merry way.
Eventually once done, a Pi3b+ with a HSF produces just 5.2H/s.  There
has to be a quicker way.

There is but it involves a bit of jumping through hoops.  The
instructions also mentions you can get a good speed up by just
rebuilding using a new version of gcc due to the better vectorisation
that those versions bring. But Raspbian is based on Debian and they
prefer reliability over being on the cutting edge and bleeding.

2. 32 bit - gcc8.1.0
So we need a new version.  The easiest, but not possibly the quickest,
is to build it yourself. There is a very good writeup on Solarian
Programmer though I deviated from his instructions by overclocking the
SD Card reader.  Even so it took a lot longer than his 5 hours.  Mine
took in excess of 8 (it was still going when I left for work the
following day and completed some time after).  However once done you
can compile and - oh noes! - it won't compile.  There is an issue that
requires you to add a single line to cmake/flags.cmake and that is:

'''
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fno-exceptions
-fno-rtti -Wno-class-memaccess")

    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -s")

    set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")



    if (XMRIG_ARMv8)

'''

This gives us boost to 6.5H/s - a good 25% increase over the one
compiled in 6.3.0

3. v8 mode
The Raspberry Pi is armv8.  However in 32bits it is reported as v7.
Is there speed ups to be had in simply changing the compile time
options?  Appears there is.

'''
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=armv8-a+crypto
-flax-vector-conversions")

    elseif (XMRIG_ARMv7)

        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mtune=cortex-a53
-mfloat-abi=hard -mfpu=neon-fp-armv8")

	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mtune=cortex-a53
-mfloat-abi=hard -mfpu=neon-fp-armv8 -flax-vector-conversions")

    else()

        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -maes")

'''
This gives us an additional 4% boost to 6.8H/s

3. Overclocking
A simple way to get a speed increase is overclocking. Memory speed is
more important than core speed.
So just a simple overclock of the ram to 500 and the core to 1500
takes us to 7.3H/s




On Thu, 27 Jun 2019, 10:54 cheltamel, <notifications@github.com> wrote:

> grahamreeds: what overclocking did you do? Interested in getting a better
> hashrate out of my RPI 3b+
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/960?email_source=notifications&email_token=ABGL3HFGJZXNAAG2W6MC3V3P4SE5PA5CNFSM4G25JTYKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODYWTHXY#issuecomment-506278879>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ABGL3HDGCEAL7NB2VDBPDATP4SE5PANCNFSM4G25JTYA>
> .
>


# Action History
- Created by: grahamreeds | 2019-02-28T17:19:21+00:00
- Closed at: 2019-08-02T13:18:03+00:00
