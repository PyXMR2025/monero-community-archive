---
title: Building in OBS fails in openSUSE with CMake GCrypt error
source_url: https://github.com/monero-project/monero-gui/issues/3213
author: nopeinomicon
assignees: []
labels: []
created_at: '2020-11-05T11:03:51+00:00'
updated_at: '2020-11-08T09:39:12+00:00'
type: issue
status: closed
closed_at: '2020-11-08T03:54:04+00:00'
---

# Original Description
I'm attempting to package this project in the SUSE Open Build Service, but the build process is failing with an error regarding the GCrypt library
```
...
[    7s] -- Configuring done
[    7s] CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
[    7s] Please set them or make sure they are set and tested correctly in the CMake files:
[    7s] GCRYPT_LIBRARY
[    7s]     linked by target "openpgp" in directory /home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/src/openpgp
[    7s] 
[    8s] -- Generating done
[    8s] CMake Generate step failed.  Build files cannot be regenerated correctly.
[    8s] make: *** [Makefile:37: release] Error 1
[    8s] error: Bad exit status from /var/tmp/rpm-tmp.bo4RHh (%build)
```
I am using the source for version 0.17.1.1 pulled from git (meaning I have all the needed parts of the repository). I am building using an RPM spec file with which I replicated the Linux build instructions as much as I was able to. This is copied to the following text file:
[monero-gui.txt](https://github.com/monero-project/monero-gui/files/5493855/monero-gui.txt)


# Discussion History
## xiphon | 2020-11-05T12:07:52+00:00
https://github.com/monero-project/monero-gui#on-linux

## nopeinomicon | 2020-11-05T23:00:17+00:00
I'm aware of the readme section, and I followed it quite closely making the spec file to build.

## selsta | 2020-11-05T23:03:27+00:00
Does it clone recursively?

## nopeinomicon | 2020-11-05T23:06:34+00:00
Yes, I checked that for sure.

## nopeinomicon | 2020-11-05T23:10:55+00:00
It seems manually setting the location of the GCrypt library is a workaround for that error from some testing, though I am still failing the build probably due to missing Qt5 dependencies (since I'm basically guessing as to what package names translate over to openSUSE's package manager haha)

## nopeinomicon | 2020-11-05T23:27:59+00:00
```
...
[   77s] cd /home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build/monero/src/wallet && /usr/bin/c++ -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_SHARED_LIBS -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_HIDAPI -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/external/rapidjson/include -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/external/easylogging++ -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/src -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/contrib/epee/include -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/external -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/external/supercop/include -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build/monero/generated_include -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build/monero/translations -I/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/external/db_drivers/liblmdb -I/usr/include/hidapi -O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto -DNDEBUG -pthread -maes -march=x86-64 -fno-strict-aliasing -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -fno-strict-aliasing -ftemplate-depth=900 -O2 -g -DNDEBUG -o CMakeFiles/obj_wallet.dir/wallet_rpc_payments.cpp.o -c /home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/monero/src/wallet/wallet_rpc_payments.cpp
[   81s] [ 73%] Linking CXX static library libepee.a
[   81s] cd /home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build/monero/contrib/epee/src && /usr/bin/cmake -P CMakeFiles/epee.dir/cmake_clean_target.cmake
[   81s] cd /home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build/monero/contrib/epee/src && /usr/bin/cmake -E cmake_link_script CMakeFiles/epee.dir/link.txt --verbose=1
[   81s] /usr/bin/ar qc libepee.a CMakeFiles/epee.dir/byte_slice.cpp.o CMakeFiles/epee.dir/byte_stream.cpp.o CMakeFiles/epee.dir/hex.cpp.o CMakeFiles/epee.dir/abstract_http_client.cpp.o CMakeFiles/epee.dir/http_auth.cpp.o CMakeFiles/epee.dir/mlog.cpp.o CMakeFiles/epee.dir/net_helper.cpp.o CMakeFiles/epee.dir/net_utils_base.cpp.o CMakeFiles/epee.dir/string_tools.cpp.o CMakeFiles/epee.dir/wipeable_string.cpp.o CMakeFiles/epee.dir/levin_base.cpp.o CMakeFiles/epee.dir/memwipe.c.o CMakeFiles/epee.dir/connection_basic.cpp.o CMakeFiles/epee.dir/network_throttle.cpp.o CMakeFiles/epee.dir/network_throttle-detail.cpp.o CMakeFiles/epee.dir/mlocker.cpp.o CMakeFiles/epee.dir/buffer.cpp.o CMakeFiles/epee.dir/net_ssl.cpp.o CMakeFiles/epee.dir/int-util.cpp.o
[   81s] /usr/bin/ranlib libepee.a
[   81s] make[2]: Leaving directory '/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build'
[   81s] [ 73%] Built target epee
[   90s] make[2]: Leaving directory '/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build'
[   90s] [ 73%] Built target obj_wallet_api
[   99s] make[2]: Leaving directory '/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build'
[   99s] [ 73%] Built target obj_wallet
[  100s] make[2]: Leaving directory '/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build'
[  100s] [ 73%] Built target obj_rpc
[  100s] make[1]: Leaving directory '/home/abuild/rpmbuild/BUILD/monero-gui-0.17.1.1/build'
[  100s] make: *** [Makefile:152: all] Error 2
[  100s] error: Bad exit status from /var/tmp/rpm-tmp.fflqxf (%build)
```

After some tweaking seems like the extra workaround was not necessary. Just building using the make command now, but the build still fails with the log above. If you need a more complete log I will provide.

## xiphon | 2020-11-06T03:00:09+00:00
>  If you need a more complete log I will provide.

Yep, please do.

## nopeinomicon | 2020-11-06T03:41:04+00:00
[build.log](https://github.com/monero-project/monero-gui/files/5498878/build.log)
Full log from the build

## xiphon | 2020-11-06T12:44:37+00:00
> It seems manually setting the location of the GCrypt library is a workaround for that error from some testing

Nope, it should automatically find it. According to the logs attached `libgcrypt` library is missing.

## xiphon | 2020-11-06T13:13:06+00:00
Reproduced. Will have a look

## xiphon | 2020-11-06T19:28:51+00:00
>  Reproduced. Will have a look

The only error is missing `libsodium-devel` package in attached `monero-gui.txt`.

Monero GUI builds fine using `opensuse/leap` docker image.

## nopeinomicon | 2020-11-07T06:29:40+00:00
Hmmm. I added libsodium-devel to the .spec file but the same build error still occurs. I also tested with Leap to see if that makes a difference and it does not.

## xiphon | 2020-11-07T12:44:40+00:00
Provide all the commands you execute to reproduce the issue on `opensuse/leap` OS.

## nopeinomicon | 2020-11-07T18:53:09+00:00
I am using the command `osc build openSUSE_Leap_15.2` to trigger the build process based on the spec file. However, within the spec file I only use the `make` command to build.

## xiphon | 2020-11-07T20:38:59+00:00
Alright, i even had to create `https://build.opensuse.org/` account just to verify that Monero GUI builds fine using OBS on `openSUSE_Leap_15.2`.

https://build.opensuse.org/package/show/home:xiphon/monero-gui


## nopeinomicon | 2020-11-07T21:47:49+00:00
Ah wow. Thanks for that. It's probably a local machine issue then, but I'll test it with your specfile when I get home from work.

## nopeinomicon | 2020-11-08T03:54:04+00:00
Hmm, finished testing out with your spec file and mine, seems like it's totally a client-side issue. The package works on OBS. How strange lol. Might have to bug the OBS people about that now. Anyway, thanks a lot, I'll close this!

## nopeinomicon | 2020-11-08T09:39:12+00:00
I found that doing a clean build (as in doing the `--clean` option for OBS and also using `make clean`) fixes the issue I was having. Thanks again for your help!

# Action History
- Created by: nopeinomicon | 2020-11-05T11:03:51+00:00
- Closed at: 2020-11-08T03:54:04+00:00
