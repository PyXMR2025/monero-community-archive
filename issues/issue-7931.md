---
title: '`make depends target=aarch64-linux-gnu` fails'
source_url: https://github.com/monero-project/monero/issues/7931
author: rblaine95
assignees: []
labels: []
created_at: '2021-09-10T16:21:52+00:00'
updated_at: '2021-09-24T03:20:07+00:00'
type: issue
status: closed
closed_at: '2021-09-24T03:20:07+00:00'
---

# Original Description
Hi there

I'm trying to cross compile `v0.17.2.3` for `aarch-linux-gnu` on `Pop!_OS 21.04`

This is the error when trying to build:
```
$ git clone --recursive https://github.com/monero-project/monero.git -b v0.17.2.3
$ make -j9 depends target=aarch64-linux-gnu
[...]
cd contrib/depends && make HOST=aarch64-linux-gnu && cd ../.. && mkdir -p build/aarch64-linux-gnu/release
make[1]: Entering directory '/home/robbie/Documents/monero/contrib/depends'
Building unwind...
make[2]: Entering directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be'
Making all in src
make[3]: Entering directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be/src'
make  all-am
make[4]: Entering directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be/src'
make[4]: Nothing to be done for 'all-am'.
make[4]: Leaving directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be/src'
make[3]: Leaving directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be/src'
Making all in tests
make[3]: Entering directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be/tests'
/bin/bash ../libtool --tag=CC   --mode=link aarch64-linux-gnu-gcc  -pipe  -fexceptions -Wall -Wsign-compare  -L/home/robbie/Documents/monero/contrib/depends/aarch64-linux-gnu/lib -o Lperf-simple Lperf-simple.o ../src/libunwind.la
libtool: link: aarch64-linux-gnu-gcc -pipe -fexceptions -Wall -Wsign-compare -o Lperf-simple Lperf-simple.o  -L/home/robbie/Documents/monero/contrib/depends/aarch64-linux-gnu/lib ../src/.libs/libunwind.a -lc -lgcc_s
/usr/lib/gcc-cross/aarch64-linux-gnu/10/../../../../aarch64-linux-gnu/bin/ld: ../src/.libs/libunwind.a(dyn-info-list.o):(.bss+0x0): multiple definition of `_U_dyn_info_list'; ../src/.libs/libunwind.a(Linit.o):(.bss+0x0): first defined here
collect2: error: ld returned 1 exit status
make[3]: *** [Makefile:752: Lperf-simple] Error 1
make[3]: Leaving directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be/tests'
make[2]: *** [Makefile:480: all-recursive] Error 1
make[2]: Leaving directory '/home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be'
make[1]: *** [funcs.mk:261: /home/robbie/Documents/monero/contrib/depends/work/build/aarch64-linux-gnu/unwind/1.2-89d5f33f1be/./.stamp_built] Error 2
make[1]: Leaving directory '/home/robbie/Documents/monero/contrib/depends'
make: *** [Makefile:50: depends] Error 2
```

My system specs are as follows:
* Intel i7-6700HQ (4 core, 8 thread)
* 32GiB DDR3 Memory (not sure frequency, doubt it matters)

I installed the build dependencies like so:
```sh
$ sudo apt-get update
$ sudo apt-get dist-upgrade -y
$ sudo apt-get install -y build-essential \
    cmake pkg-config libboost-all-dev \
    libssl-dev libzmq3-dev libunbound-dev \
    libsodium-dev libunwind8-dev liblzma-dev \
    libreadline6-dev libldns-dev libexpat1-dev \
    doxygen graphviz libpgm-dev qttools5-dev-tools \
    libhidapi-dev libusb-1.0-0-dev libprotobuf-dev \
    protobuf-compiler libudev-dev git

$ sudo apt-get install -y libgtest-dev && \
  cd /usr/src/gtest && \
  sudo cmake . && \
  sudo make && \
  sudo mv lib/libg* /usr/lib/

$ sudo apt-get install -y \
    g++-arm-linux-gnueabihf g++-aarch64-linux-gnu \
    gperf
```
And python3 is my default set python
```sh
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```

Maybe I'm just missing something stupid.

# Discussion History
## selsta | 2021-09-11T05:23:04+00:00
Seems to be solved by updating the libunwind depends package version. Will submit a patch for it.

## selsta | 2021-09-11T19:22:45+00:00
#7933

## rblaine95 | 2021-09-11T19:58:45+00:00
Great, thank you @selsta, testing it out cherry-picked on the `v0.17.2.3` tag

# Action History
- Created by: rblaine95 | 2021-09-10T16:21:52+00:00
- Closed at: 2021-09-24T03:20:07+00:00
