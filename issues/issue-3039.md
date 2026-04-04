---
title: 'Dockerfile returning ''make: *** No rule to make target ''release-static''.  Stop.'''
source_url: https://github.com/monero-project/monero/issues/3039
author: allexlima
assignees: []
labels: []
created_at: '2017-12-31T16:17:43+00:00'
updated_at: '2020-10-04T20:43:11+00:00'
type: issue
status: closed
closed_at: '2018-01-01T17:19:24+00:00'
---

# Original Description
Hi, 

When I try building the [dockerfile](https://github.com/monero-project/monero/blob/master/Dockerfile), I get the following error:

```bash
$ docker build -t monero-alone .
Sending build context to Docker daemon  3.072kB
Step 1/14 : FROM ubuntu:16.04 as builder
 ---> 00fd29ccc6f1
Step 2/14 : RUN apt-get update &&     apt-get --no-install-recommends --yes install         ca-certificates         cmake         g++         libboost1.58-all-dev         libssl-dev         libzmq3-dev         libreadline-dev         libsodium-dev         make         pkg-config         graphviz         doxygen         git
 ---> Using cache
 ---> 2972a74e2ff1
Step 3/14 : WORKDIR /src
 ---> Using cache
 ---> 8002585c60cf
Step 4/14 : COPY . .
 ---> Using cache
 ---> aaaefc2d8326
Step 5/14 : ARG NPROC
 ---> Using cache
 ---> 63b20d47afc3
Step 6/14 : RUN rm -rf build &&     if [ -z "$NPROC" ];then make -j$(nproc) release-static;else make -j$NPROC release-static;fi
 ---> Running in 96a3fdc888ea
make: *** No rule to make target 'release-static'.  Stop.

```

Is it any problem with the dockerfile?

# Discussion History
## moneromooo-monero | 2017-12-31T17:35:34+00:00
The Makefile has a release-static target, so it's not using the right makefile. Can you tell which one it's trying to use (ie, add a call to pwd before calling make) ?

## MoroccanMalinois | 2017-12-31T17:43:14+00:00
fwiw, i just tried to rebuild the image and it works fine. 

@allexlima Did you clone the repo or just took the dockerfile ? 

## allexlima | 2018-01-01T16:15:38+00:00
@moneromooo-monero I tried to add `pwd`  before `rm -rf build && \` (line 26) in the Dockerfile, but it didn't return anything :/

@MoroccanMalinois I just took the dockerfile from the repo 

## allexlima | 2018-01-01T17:19:01+00:00
update: I tried cloning the repo and then build the dockerfile and now it worked =)

## ealexhaywood | 2018-07-18T15:37:22+00:00
In my particular case, the Makefile was being ignored in the `.dockerignore` file.  Drove me nuts before I realized thats what it was

## ghost | 2020-10-04T20:43:11+00:00
So I ran into this same problem saying `make: *** No rule to make target 'release-static-android-armv8'. Stop`  on android64.Dockerfile and I changed the last part to be

```
ADD . /src
RUN cd /src \
    && pwd \
    && ls /src \
    && CMAKE_INCLUDE_PATH="${PREFIX}/include" \
       CMAKE_LIBRARY_PATH="${PREFIX}/lib" \
       ANDROID_STANDALONE_TOOLCHAIN_PATH=${TOOLCHAIN_DIR} \
       USE_SINGLE_BUILDDIR=1 \
       PATH=${HOST_PATH} make release-static-android-armv8 -j${NPROC}
```

and I found out that it was copying my files from utils/build-scripts/ into src/

so my src/ directory looked like 

android64.Dockerfile
android32.Dockerfile
windows.bat

when it was supposed to be copying my repository. 

I fixed this by running docker from the root directory monero/ instead of monero/utils/build-scripts/ so that ADD . / actually adds the src code to the docker blahhhhh

# Action History
- Created by: allexlima | 2017-12-31T16:17:43+00:00
- Closed at: 2018-01-01T17:19:24+00:00
