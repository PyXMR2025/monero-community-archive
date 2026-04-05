---
title: make not working on linux
source_url: https://github.com/xmrig/xmrig/issues/3106
author: Feuerwerko
assignees: []
labels: []
created_at: '2022-08-09T09:13:21+00:00'
updated_at: '2024-12-26T20:25:51+00:00'
type: issue
status: closed
closed_at: '2024-12-26T20:25:51+00:00'
---

# Original Description
Im trying to install xmrig on a raspberry PI running PI-OS lite, and when i try to install xmrig using the commands
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build 
cd xmrig/build
cmake ..
everything works but as soon as I use the command
make
it gives out:

pi@raspberrypi:~/data/xmrig/build $ make
[  2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:82: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:240: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:103: all] Error 2

somewhere i saw that you should run make with -j4 at the end but then the list just becomes way longer:

pi@raspberrypi:~/data/xmrig/build $ make -j4
Scanning dependencies of target ethash
Scanning dependencies of target argon2
Scanning dependencies of target ghostrider
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:82: src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:95: src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:213: src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:82: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:95: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o] Error 1
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:108: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:186: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
[  1%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o
[  2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o
cc: error: unrecognized command-line option ‘-maes’
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:95: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_bmw.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:82: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_blake.c.o] Error 1
[  2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o
[  2%] Building C object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:108: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_cubehash.c.o] Error 1
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:121: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/sph_echo.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:240: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
make: *** [Makefile:103: all] Error 2

Also i tried all methods with sudo but that doesnt change anything.

Ive looked around everywhere and i cant find anyone having the same issue. So I couldnt find a fix too.


# Discussion History
## Feuerwerko | 2022-08-09T09:21:36+00:00
Ive also tried running cmake with -DWITH_GHOSTRIDER=OFF but then it says
pi@raspberrypi:~/data/xmrig/build $ make
Scanning dependencies of target argon2
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:82: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:164: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
make: *** [Makefile:103: all] Error 2

## SChernykh | 2022-08-09T10:40:43+00:00
32-bit ARM is not supported, you need to install 64-bit PI OS.

## Feuerwerko | 2022-08-10T07:14:30+00:00
oh okay

## fplata | 2023-02-02T00:40:24+00:00
Dear, I have the same problem, were you able to solve it, I will be attentive to your comments

# Action History
- Created by: Feuerwerko | 2022-08-09T09:13:21+00:00
- Closed at: 2024-12-26T20:25:51+00:00
