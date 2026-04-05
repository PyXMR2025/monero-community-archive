---
title: static building erorr?
source_url: https://github.com/xmrig/xmrig/issues/2450
author: stream1990
assignees: []
labels: []
created_at: '2021-06-20T01:34:03+00:00'
updated_at: '2021-06-20T23:50:56+00:00'
type: issue
status: closed
closed_at: '2021-06-20T23:50:46+00:00'
---

# Original Description
`1. sudo dnf install -y epel-release
2. sudo yum config-manager --set-enabled PowerTools
3. sudo dnf install -y git make cmake gcc gcc-c++ libstdc++-static automake libtool autoconf
4. git clone https://github.com/xmrig/xmrig.git
5. mkdir xmrig/build
6. cd xmrig/scripts && ./build_deps.sh && cd ../build
7. cmake .. -DXMRIG_DEPS=scripts/deps
8. make -j$(nproc)`

but it can not build static?

[root@xx build]# ldd xmrig
        linux-vdso.so.1 (0x00007fff147ee000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f8605c6c000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f8605a68000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f8605860000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f86054de000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f8605119000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f8605e8c000)



and run error in other server



/lib64/libm.so.6: version `GLIBC_2.15' not found
/lib64/libc.so.6: version `GLIBC_2.17' not found
/lib64/libc.so.6: version `GLIBC_2.14' not found
/lib64/libc.so.6: version `GLIBC_2.25' not found




# Discussion History
## Spudz76 | 2021-06-20T16:08:22+00:00
You have to add `-DBUILD_STATIC=ON` in order to........... build static.

Otherwise it's dynamic linked always.

## stream1990 | 2021-06-20T23:50:56+00:00
thank you

# Action History
- Created by: stream1990 | 2021-06-20T01:34:03+00:00
- Closed at: 2021-06-20T23:50:46+00:00
