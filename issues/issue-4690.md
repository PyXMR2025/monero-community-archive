---
title: 'Building on Docker with BUILD_SHARED_LIBS=ON: error: dereferencing pointer
  to incomplete type ''EVP_MD_CTX {aka struct evp_md_ctx_st}'''
source_url: https://github.com/monero-project/monero/issues/4690
author: whidrasl
assignees: []
labels: []
created_at: '2018-10-22T10:32:26+00:00'
updated_at: '2022-04-08T15:46:40+00:00'
type: issue
status: closed
closed_at: '2022-04-08T15:46:39+00:00'
---

# Original Description
Hi! I'm trying to build v0.13.0.2 (also tried release-v0.13 and master) with shared libs using Dockerfile (with added `git submodule init && git submodule update`) with changed make command:
```
mkdir -p build/release
cd build/release
cmake -D CMAKE_BUILD_TYPE=release -D ARCH="x86-64" -D BUILD_64=ON -D BUILD_SHARED_LIBS=ON ../..
make -j$(nproc)
```
and got such error:

```
/src/external/unbound/validator/val_secalgo.c: In function 'verify_canonrrset':
/src/external/unbound/validator/val_secalgo.c:665:35: error: dereferencing pointer to incomplete type 'EVP_MD_CTX {aka struct evp_md_ctx_st}'
  ctx = (EVP_MD_CTX*)malloc(sizeof(*ctx));
                                   ^
/src/external/unbound/validator/val_secalgo.c:681:3: warning: implicit declaration of function 'EVP_MD_CTX_cleanup' [-Wimplicit-function-declaration]
   EVP_MD_CTX_cleanup(ctx);
   ^
```

If I replace BUILD_SHARED_LIBS=ON to STATIC=ON then it successfuly built, but I need shared libraries (for sammy007/monero-stratum).

Also I've noticed that calling `openssl version` in Docker container crashes with Segmentation fault even in STATIC build.

Thank you.

# Discussion History
## whidrasl | 2018-10-22T12:17:53+00:00
There is some lines that I've got at compiling monero: (do you need all logs?)
```
-- Found OpenSSL: /usr/local/openssl-1.1.0h/libcrypto.a (found version "1.1.0h")  
-- Using OpenSSL include dir at /usr/local/openssl-1.1.0h/include
```

apt-get install curl ca-certificates and so one installs some ssl libraries:
```
# apt list --installed | grep ssl
libssl1.0.0/xenial-updates,xenial-security,now 1.0.2g-1ubuntu4.13 amd64 [installed,automatic]
openssl/xenial-updates,xenial-security,now 1.0.2g-1ubuntu4.13 amd64 [installed,automatic]
```
If I manually remove them by `dpkg -r --force-depends openssl libssl1.0.0` before making monero, I've got next error:
```
cmake: error while loading shared libraries: libssl.so.1.0.0: cannot open shared object file: No such file or directory
```

I don't know whether this library is needed by cmake itself or for linking monero (I suppose that by cmake itself)

## iDunk5400 | 2018-10-22T14:06:09+00:00
Try adding  `-D INSTALL_VENDORED_LIBUNBOUND=ON` to your cmake line.

## iDunk5400 | 2018-10-22T14:11:21+00:00
Actually... see if you have libunbound dev package installed (libunbound-dev in Ubuntu). If you do, uninstall it, make clean and try again.

## iDunk5400 | 2018-10-22T14:14:22+00:00
Nvm, ignore. I see that you get the error when building libunbound. You seem to be missing a commit then.

## iDunk5400 | 2018-10-22T14:17:54+00:00
Ah, you have (selfbuilt?) OpenSSL in /usr/local. Can't help you there.

## iDunk5400 | 2018-10-22T14:47:32+00:00
Maybe [this](https://github.com/monero-project/monero/blob/master/Dockerfile#L59) is the cause of your error.

## whidrasl | 2018-10-22T14:49:03+00:00
@iDunk5400, Thanks for idea:
Totally I've left only this projects for building from source in Dockerfile:

> libzmq
cppzmq
libsodium

(not compiling: cmake, boost, openssl, readline)

All other packages I've installed with apt and it compiled succesfully

## whidrasl | 2018-10-22T14:53:55+00:00
> Maybe [this](https://github.com/monero-project/monero/blob/master/Dockerfile#L59) is the cause of your error.

I don't think so, because other projects has the same "no-shared" and "static", and also with this parameters (but with previous openssl version, for example) it worked with v0.12.*.* monero version

## iDunk5400 | 2018-10-22T15:20:04+00:00
I think you will need all of them. Did you change [this](https://github.com/monero-project/monero/blob/master/Dockerfile#L121-L122) ?

## whidrasl | 2018-10-22T15:37:07+00:00
> I think you will need all of them. Did you change [this](https://github.com/monero-project/monero/blob/master/Dockerfile#L121-L122) ?

Yes, I've changed this lines to lines in my upper post. And I don't remove cmake, boost, openssl, readline: I install most of them with apt instead of compiling them.

## iDunk5400 | 2018-10-22T16:09:01+00:00
Well, all I can add is make sure `git -C external/unbound/ log --oneline -1` returns `7f23967 Merge pull request #11`.

## SomethingGettingWrong | 2018-11-17T18:52:23+00:00
Expierienced this problem when compiling another coin. The fix was in an unbound update I believe


## guybrush | 2019-03-21T16:09:27+00:00
I am running into the same problem. Since the docker-image took quite some time to build I pushed it to the hub: https://hub.docker.com/r/guybrush/monero-builder (dockerfile: https://gist.github.com/guybrush/c9b9f7422f02a2bd8f3d35c62ecdde81).

## selsta | 2022-04-08T15:46:39+00:00
We removed unbound as a submodule.

# Action History
- Created by: whidrasl | 2018-10-22T10:32:26+00:00
- Closed at: 2022-04-08T15:46:39+00:00
