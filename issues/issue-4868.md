---
title: Dockerfile is not working with git submodule init fatal
source_url: https://github.com/monero-project/monero/issues/4868
author: lcgogo
assignees: []
labels: []
created_at: '2018-11-19T11:20:54+00:00'
updated_at: '2018-11-19T11:43:16+00:00'
type: issue
status: closed
closed_at: '2018-11-19T11:43:16+00:00'
---

# Original Description
Step 39/50 : COPY . .
 ---> 28209aa52c8a
Step 40/50 : ENV USE_SINGLE_BUILDDIR=1
 ---> Running in 590ad11ee5b9
Removing intermediate container 590ad11ee5b9
 ---> 132ffe6e9314
Step 41/50 : ARG NPROC
 ---> Running in 442f6a838721
Removing intermediate container 442f6a838721
 ---> e00cb8614f69
Step 42/50 : RUN set -ex &&     git submodule init &&     git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi
 ---> Running in 62f5a2586f1c
+ git submodule init
fatal: Not a git repository (or any of the parent directories): .git
The command '/bin/sh -c set -ex &&     git submodule init &&     git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi' returned a non-zero code: 128

# Discussion History
## lcgogo | 2018-11-19T11:43:16+00:00
I think I need clone the source at first. I used to think use the only dockerfile to build.

# Action History
- Created by: lcgogo | 2018-11-19T11:20:54+00:00
- Closed at: 2018-11-19T11:43:16+00:00
