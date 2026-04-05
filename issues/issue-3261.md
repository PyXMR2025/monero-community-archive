---
title: error compilation make libstdc++
source_url: https://github.com/xmrig/xmrig/issues/3261
author: afl45
assignees: []
labels: []
created_at: '2023-04-22T16:29:53+00:00'
updated_at: '2025-06-18T22:34:31+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:34:31+00:00'
---

# Original Description
Hi monero comunity,
Today I have a problem for compiling xmrig with command make.
I have an error message telling me that there is a problem with the libstdc++ package.
I try to install the lib and it's done but still the same error message.
Can somebody help me please. Here is a screenshot of my error message

`[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o
[100%] Linking CXX executable xmrig
/usr/bin/ld : ne peut pas trouver -lstdc++ : Aucun fichier ou dossier de ce type
collect2: erreur: ld a retourné le statut de sortie 1
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3854 : xmrig] Erreur 1
make[1]: *** [CMakeFiles/Makefile2:182 : CMakeFiles/xmrig.dir/all] Erreur 2
make: *** [Makefile:91 : all] Erreur 2
[afl_xmr_hp_pm@pc-130 build]$ 
`

# Discussion History
## Spudz76 | 2023-04-22T21:51:03+00:00
Generally there is a runtime package and a "dev" or "devel" package, you need both.  Which Linux distro?

## afl45 | 2023-04-23T08:13:05+00:00
> Generally there is a runtime package and a "dev" or "devel" package, you need both. Which Linux distro?

i am on fedora 37, ok i will look at the dev and devel package history. thanks

## Walid233 | 2023-04-23T10:56:31+00:00
نعم أنا مشرك أحاول اسحب لكن بدون جدوه ارجو انا تخبرني ماهي المشكله

في الأحد، 23 أفريل 2023 11:13 ص afl45 ***@***.***> كتب:

> Generally there is a runtime package and a "dev" or "devel" package, you
> need both. Which Linux distro?
>
> i am on fedora 37, ok i will look at the dev and devel package history.
> thanks
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3261#issuecomment-1518989612>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A7HCYJP4MX6HOE3NB3C4U6DXCTQDHANCNFSM6AAAAAAXH5ZYGE>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## Walid233 | 2023-04-23T10:57:51+00:00
لا ادري ماهي المشكله اشراح لي اكثر عن الينكس

في السبت، 22 أفريل 2023 7:30 م afl45 ***@***.***> كتب:

> Hi monero comunity,
> Today I have a problem for compiling xmrig with command make.
> I have an error message telling me that there is a problem with the
> libstdc++ package.
> I try to install the lib and it's done but still the same error message.
> Can somebody help me please. Here is a screenshot of my error message
>
> [ 99%] Building CXX object
> CMakeFiles/xmrig.dir/src/base/net/https/HttpsServer.cpp.o [100%] Building
> CXX object CMakeFiles/xmrig.dir/src/crypto/common/Assembly.cpp.o [100%]
> Building CXX object
> CMakeFiles/xmrig.dir/src/crypto/cn/r/CryptonightR_gen.cpp.o [100%] Linking
> CXX executable xmrig /usr/bin/ld : ne peut pas trouver -lstdc++ : Aucun
> fichier ou dossier de ce type collect2: erreur: ld a retourné le statut de
> sortie 1 make[2]: *** [CMakeFiles/xmrig.dir/build.make:3854 : xmrig] Erreur
> 1 make[1]: *** [CMakeFiles/Makefile2:182 : CMakeFiles/xmrig.dir/all] Erreur
> 2 make: *** [Makefile:91 : all] Erreur 2 ***@***.*** build]$
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3261>, or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A7HCYJNDHFNNGAK65WWZWYTXCQBSHANCNFSM6AAAAAAXH5ZYGE>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## DeeDeeRanged | 2023-04-24T09:24:02+00:00
Also have a look which GCC version you are on.

# Action History
- Created by: afl45 | 2023-04-22T16:29:53+00:00
- Closed at: 2025-06-18T22:34:31+00:00
