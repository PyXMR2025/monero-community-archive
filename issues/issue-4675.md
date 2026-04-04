---
title: Dockerfile seems to be broken
source_url: https://github.com/monero-project/monero/issues/4675
author: korjavin
assignees: []
labels: []
created_at: '2018-10-20T16:01:56+00:00'
updated_at: '2018-10-25T12:46:41+00:00'
type: issue
status: closed
closed_at: '2018-10-25T10:09:03+00:00'
---

# Original Description
I tried to build node by docker build by it has ended with:
`
Step 33/41 : RUN set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi
 ---> Running in cbd0b24e0045
+ git submodule init
+ git submodule update
+ rm -rf build
+ [ -z  ]
+ nproc
+ make -j2 release-static
make: *** No rule to make target 'release-static'.  Stop.
The command '/bin/sh -c set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi' returned a non-zero code: 2
Exited with code 2

`

# Discussion History
## moneromooo-monero | 2018-10-25T10:03:56+00:00
https://github.com/monero-project/monero/pull/4591

+resolved


## korjavin | 2018-10-25T12:46:41+00:00
Nope, it doesn't help.
I already had this git submodule in my Dockerfile.

There is the full log of building in circle-ci
[build_9_step_104_container_0.txt](https://github.com/monero-project/monero/files/2514903/build_9_step_104_container_0.txt)


# Action History
- Created by: korjavin | 2018-10-20T16:01:56+00:00
- Closed at: 2018-10-25T10:09:03+00:00
