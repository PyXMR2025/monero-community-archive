---
title: 'Error : regex_error'
source_url: https://github.com/xmrig/xmrig/issues/2134
author: guoshuaifeng
assignees: []
labels:
- bug
- duplicate
created_at: '2021-02-27T01:58:06+00:00'
updated_at: '2021-02-27T07:02:53+00:00'
type: issue
status: closed
closed_at: '2021-02-27T07:02:53+00:00'
---

# Original Description
I have the same error like this:
https://github.com/xmrig/xmrig/issues/2123

Describe the bug
when I run ./xmrig I get this error: what(): regex_error

To Reproduce
yum install -y git make cmake gcc gcc-c++ libstdc++-static libuv-static hwloc-devel openssl-devel
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake ..
make -j$(nproc)

Required data
Error:
./xmrig

ABOUT XMRig/6.9.0 gcc/4.8.5
LIBS libuv/1.40.0 OpenSSL/1.0.2k hwloc/1.11.8
HUGE PAGES supported
1GB PAGES unavailable
CPU Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz (1) 64-bit AES
L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
MEMORY 15.2/15.5 GB (98%)
terminate called after throwing an instance of 'std::regex_error'
what(): regex_error
OS - CentOS Linux release 7.9.2009 (Core)
Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz
NO GPU

Default config.json (added just my ewallet)

But i need to build from source,How to solve it ?

# Discussion History
# Action History
- Created by: guoshuaifeng | 2021-02-27T01:58:06+00:00
- Closed at: 2021-02-27T07:02:53+00:00
