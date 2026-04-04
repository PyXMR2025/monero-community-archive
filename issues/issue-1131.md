---
title: 'Build fail : Segmentation fault (core dumped) /usr/bin/ld [...]'
source_url: https://github.com/monero-project/monero/issues/1131
author: ghost
assignees: []
labels: []
created_at: '2016-09-25T08:40:04+00:00'
updated_at: '2017-10-08T12:12:19+00:00'
type: issue
status: closed
closed_at: '2017-10-08T12:12:19+00:00'
---

# Original Description
Build env : raspberry pi / arch linux

make[3]: Entering directory '/home/alarm/tmp/monero-0.10.0/build/release'
[ 50%] Generating testnet_blocks.o
/bin/sh: line 1: 8895 Segmentation fault (core dumped) /usr/bin/ld -r -b binary -o /home/alarm/tmp/monero-0.10.0/build/release/src/blocks/testnet_blocks.o testnet_blocks.dat
make[3]: **\* [src/blocks/CMakeFiles/blocks.dir/build.make:66: src/blocks/testnet_blocks.o] Error 139

... too bad, I realy want to have a full node running.

Rgds


# Discussion History
## anonimal | 2016-09-25T12:26:37+00:00
@lotusfred have you tried cloning/building against current master?

Referencing https://aur.archlinux.org/packages/monero/


## ghost | 2016-09-25T13:50:22+00:00
Which RPi?


## ghost | 2016-09-25T15:01:45+00:00
@anonimal : Yes I first try to use sources from AUR (and got the seg fault) then I try with "git clone https://github.com/monero-project/monero.git" and got the same error 
By the way I first post my question on https://aur.archlinux.org/packages/monero/ (nikname fredchamp)
@NanoAkron : I try to build on a RPI-2B


## ghost | 2016-10-28T19:46:10+00:00
Please try #1269


## radfish | 2016-11-18T23:06:54+00:00
See #974. Try Invoking cmake with: `-DCMAKE_LINKER=/usr/bin/ld.gold`


## diederikdehaas | 2016-12-21T19:32:09+00:00
I had a problem that very much seems to be related to `ld` vs `ld.gold` too on my Debian Sid amd64 system (haven't tried yet on my RPi's).

I tried to build monero-core and one of the first steps is run `./get_libwallet_api.sh`, which builds part of monero and that failed on the following line:
`ld -r -b binary -o /home/diederik/dev/crypto/monero-project/monero/build/release/src/blocks/testnet_blocks.o testnet_blocks.dat`

But it did succeed when I manually executed:
`ld.gold -r -b binary -o /home/diederik/dev/crypto/monero-project/monero/build/release/src/blocks/testnet_blocks.o testnet_blocks.dat`

A couple of days later the `binutils` package, which provides both `ld` and `ld.gold`, got updated from version `2.27.51.20161201-1` to `2.27.51.20161220-1` and then it did succeed with `ld`.
However, I didn't manage to reproduce the problem on my Debian Strech amd64 system and I also hadn't saved the build log :-/

Another thing to keep in mind is the version of openssl-dev used, 1.0 or 1.1, see https://github.com/monero-project/monero/issues/1411 for details. 
Also note that openssl 1.1 isn't yet supported by the Qt project.

So it may be useful to investigate which versions of various libraries are in use.

## radfish | 2017-09-25T02:41:14+00:00
The linking now succeeds on Arch on armv7h with binutils 2.29.0 (probably also with earlier versions too), where it used to fail. So, this is probably ok to close. See #974.

## moneromooo-monero | 2017-10-08T12:11:19+00:00
This was a bug in binutils, now fixed, so I'll mark this as resolved, even though we didn't change anything.

+resolved


# Action History
- Created by: ghost | 2016-09-25T08:40:04+00:00
- Closed at: 2017-10-08T12:12:19+00:00
