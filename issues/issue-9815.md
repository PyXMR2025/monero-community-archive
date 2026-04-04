---
title: Static Libs
source_url: https://github.com/monero-project/monero/issues/9815
author: batterhour
assignees: []
labels:
- question
created_at: '2025-02-23T19:49:39+00:00'
updated_at: '2025-02-24T21:58:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I want to deploy multiple Monero nodes (monerod) to support the network, but I'm encountering issues.

when i launched:

`sudo ./monerod`

I get the following error:

`./monerod: error while loading shared libraries: libboost_chrono.so.1.82.0: cannot open shared object file: No such file or directory`

Checking with:
ldd ./monerod
It returns an error:
`       linux-vdso.so.1 (0x00007fff2733c000)
        libboost_chrono.so.1.82.0 => not found
        libboost_filesystem.so.1.82.0 => not found
        libboost_program_options.so.1.82.0 => not found
        libreadline.so.8 => /lib/x86_64-linux-gnu/libreadline.so.8 (0x00007886c36b8000)
        libzmq.so.5 => /lib/x86_64-linux-gnu/libzmq.so.5 (0x00007886c295e000)
        libhidapi-libusb.so.0 => /lib/x86_64-linux-gnu/libhidapi-libusb.so.0 (0x00007886c36ab000)
        libsodium.so.23 => /lib/x86_64-linux-gnu/libsodium.so.23 (0x00007886c2907000)
        libunbound.so.8 => /lib/x86_64-linux-gnu/libunbound.so.8 (0x00007886c2806000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x00007886c275c000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x00007886c2200000)
        libboost_thread.so.1.82.0 => not found
        libboost_serialization.so.1.82.0 => not found
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007886c1e00000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007886c2117000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007886c272e000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007886c1a00000)
        /lib64/ld-linux-x86-64.so.2 (0x00007886c371c000)
        libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6 (0x00007886c20e3000)
        libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007886c2718000)
        libpgm-5.3.so.0 => /lib/x86_64-linux-gnu/libpgm-5.3.so.0 (0x00007886c2099000)
        libnorm.so.1 => /lib/x86_64-linux-gnu/libnorm.so.1 (0x00007886c1cf5000)
        libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x00007886c1ca1000)
        libusb-1.0.so.0 => /lib/x86_64-linux-gnu/libusb-1.0.so.0 (0x00007886c1c83000)
        libevent-2.1.so.7 => /lib/x86_64-linux-gnu/libevent-2.1.so.7 (0x00007886c1c31000)
        libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0 (0x00007886c208a000)
        libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x00007886c1937000)
        libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x00007886c190b000)
        libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x00007886c369d000)
        libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x00007886c1c24000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007886c18d8000)
        libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x00007886c2083000)
        libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x00007886c18c5000)
        libcap.so.2 => /lib/x86_64-linux-gnu/libcap.so.2 (0x00007886c1c17000)
`

This seems to be an issue with static and dynamic libraries. Does anyone know how to resolve it?
Here’s the full list of commands I used to install the required libraries and compile the binaries:

#!/bin/bash
sudo apt update -y && sudo apt upgrade -y
cd /
wget https://github.com/Kitware/CMake/releases/download/v4.0.0-rc1/cmake-4.0.0-rc1-linux-x86_64.sh
chmod +x cmake-4.0.0-rc1-linux-x86_64.sh
sudo bash ./cmake-4.0.0-rc1-linux-x86_64.sh --skip-license --prefix=/usr/local
export PATH=/usr/local/bin:$PATH
echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
cd /usr/local/src
sudo wget https://mirror.bazel.build/boostorg.jfrog.io/artifactory/main/release/1.82.0/source/boost_1_82_0.tar.gz
sudo tar -xvzf boost_1_82_0.tar.gz
cd boost_1_82_0
sudo apt update && sudo apt install -y build-essential pkg-config libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev liblzma-dev libreadline6-dev libexpat1-dev qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev libprotobuf-dev protobuf-compiler libudev-dev python3 ccache doxygen graphviz git curl autoconf libtool gperf
./bootstrap.sh --prefix=/usr/local
sudo ./b2 install --prefix=/usr/local --build-type=complete link=static runtime-link=static -j$(nproc)
ls /usr/local/lib | grep boost
export BOOST_ROOT="/usr/local/src/boost_1_82_0"
export BOOST_INCLUDEDIR="$BOOST_ROOT"
export BOOST_LIBRARYDIR="/usr/local/lib"
cd /
git clone https://github.com/monero-project/monero.git
cd /monero
git submodule init && git submodule update
cmake .
sudo make -j$(nproc)
cd bin
sudo ./monero --help

# Discussion History
## batterhour | 2025-02-23T19:55:07+00:00
P.S. I ran monerod on a new virtual machine

You will probably say that I should have installed it exactly the same way, but I tried and the result was not successful

## batterhour | 2025-02-24T06:00:55+00:00
...?

## selsta | 2025-02-24T12:38:18+00:00
We use the `depends` system for static binaries: https://github.com/monero-project/monero/?tab=readme-ov-file#cross-compiling

## batterhour | 2025-02-24T13:17:59+00:00
> Мы используем `depends`систему для статических двоичных файлов: https://github.com/monero-project/monero/?tab=readme-ov-file#cross-compiling

Is cmake 4.0.0 and boost 1.82 suitable?

## selsta | 2025-02-24T17:49:23+00:00
You can try `make release-static` instead of `make`.

## batterhour | 2025-02-24T19:31:34+00:00
> You can try `make release-static` instead of `make`.

Thank you, I created the binary files successfully, but the question is how can I compile them into .exe?
I tried, but there were one error, can you tell me how to do it correctly?:

cd /monero/contrib/depends
make HOST=x86_64-w64-mingw32 -j$(nproc)
cd /monero
mkdir build && cd build
cmake .. -DARCH=x86-64 -DCMAKE_SYSTEM_NAME=Windows \
    -DCMAKE_C_COMPILER=x86_64-w64-mingw32-gcc \
    -DCMAKE_CXX_COMPILER=x86_64-w64-mingw32-g++ \
    -DCMAKE_FIND_ROOT_PATH=/monero/contrib/depends/x86_64-w64-mingw32 \
    -DSTATIC=ON -DBUILD_SHARED_LIBS=OFF
make -j$(nproc)

## selsta | 2025-02-24T21:25:06+00:00
See this https://github.com/monero-project/monero/blob/master/.github/workflows/depends.yml#L104

## batterhour | 2025-02-24T21:42:45+00:00
> See this https://github.com/monero-project/monero/blob/master/.github/workflows/depends.yml#L104

make depends target=${{ matrix.toolchain.host }} -j${{env.MAKE_JOB_COUNT}} wait?

Please tell me the command, otherwise I don't understand much..

## selsta | 2025-02-24T21:58:38+00:00
Use this command to install dependencies

https://github.com/monero-project/monero/actions/runs/13504907018/job/37732133704#step:4:1

run the following two commands to `update-alternatives`

https://github.com/monero-project/monero/actions/runs/13504907018/job/37732133704#step:9:2

then use this command to build

https://github.com/monero-project/monero/actions/runs/13504907018/job/37732133704#step:11:5

# Action History
- Created by: batterhour | 2025-02-23T19:49:39+00:00
