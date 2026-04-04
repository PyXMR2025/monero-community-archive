---
title: Do the docker builds for Android actually work?
source_url: https://github.com/monero-project/monero/issues/6564
author: trurebel
assignees: []
labels: []
created_at: '2020-05-19T15:16:58+00:00'
updated_at: '2021-10-06T03:20:53+00:00'
type: issue
status: closed
closed_at: '2021-10-06T03:20:44+00:00'
---

# Original Description
I have MacOS docker and decided to try out the two (32 and 64 bit) docker build scripts, my internet is wobbly so I cannot be 100% I am not to blame, but certainly the 32 bit build fails with something that looks like a bug, though I cannot guess where that comes from.

`Step 43/43 : RUN cd /src     && CMAKE_INCLUDE_PATH="${PREFIX}/include"        CMAKE_LIBRARY_PATH="${PREFIX}/lib"        ANDROID_STANDALONE_TOOLCHAIN_PATH=${TOOLCHAIN_DIR}        USE_SINGLE_BUILDDIR=1        PATH=${HOST_PATH} make release-static-android-armv7 -j${NPROC}
 ---> Running in 32f7228b917f
make: *** No rule to make target 'release-static-android-armv7'.  Stop.`

Got the equivalent message on 64 bit

`Step 43/43 : RUN cd /src     && CMAKE_INCLUDE_PATH="${PREFIX}/include"        CMAKE_LIBRARY_PATH="${PREFIX}/lib"        ANDROID_STANDALONE_TOOLCHAIN_PATH=${TOOLCHAIN_DIR}        USE_SINGLE_BUILDDIR=1        PATH=${HOST_PATH} make release-static-android-armv8 -j${NPROC}
 ---> Running in 10efcd626111
make: *** No rule to make target 'release-static-android-armv8'.  Stop.
The command '/bin/sh -c cd /src     && CMAKE_INCLUDE_PATH="${PREFIX}/include"        CMAKE_LIBRARY_PATH="${PREFIX}/lib"        ANDROID_STANDALONE_TOOLCHAIN_PATH=${TOOLCHAIN_DIR}        USE_SINGLE_BUILDDIR=1        PATH=${HOST_PATH} make release-static-android-armv8 -j${NPROC}' returned a non-zero code: 2`

# Discussion History
## moneromooo-monero | 2020-05-19T15:25:15+00:00
release-static-android-armv7 and release-static-android-armv8 are valid targets, so it looks like it's not seeing the right Makefile. 


## ghost | 2020-10-04T20:44:36+00:00
#3039 3039

## selsta | 2021-10-06T03:20:44+00:00
Use `gitian` to create Android binaries.

# Action History
- Created by: trurebel | 2020-05-19T15:16:58+00:00
- Closed at: 2021-10-06T03:20:44+00:00
