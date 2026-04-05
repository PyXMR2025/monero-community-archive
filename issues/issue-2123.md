---
title: 'Error : regex_error'
source_url: https://github.com/xmrig/xmrig/issues/2123
author: xguya
assignees: []
labels:
- bug
created_at: '2021-02-21T22:46:43+00:00'
updated_at: '2021-04-12T14:11:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:11:15+00:00'
---

# Original Description
**Describe the bug**
when I run ./xmrig  I get this error: what():  regex_error

**To Reproduce**
yum install -y git make cmake gcc gcc-c++ libstdc++-static libuv-static hwloc-devel openssl-devel
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake ..
make -j$(nproc) 

**Required data**
Error: 
./xmrig 
 * ABOUT        XMRig/6.9.0 gcc/4.8.5
 * LIBS         libuv/1.40.0 OpenSSL/1.0.2k hwloc/1.11.8
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       15.2/15.5 GB (98%)
terminate called after throwing an instance of 'std::regex_error'
  what():  regex_error

OS - CentOS Linux release 7.9.2009 (Core) 
Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz
NO GPU 

Default config.json (added just my ewallet)
 


# Discussion History
## xguya | 2021-02-21T23:17:27+00:00
solved with: Static, CPU only https://xmrig.com/download

## guoshuaifeng | 2021-02-27T01:55:37+00:00
But i need to build from source,How to solve it ?

## xmrig | 2021-02-27T07:02:00+00:00
gcc 4.8 has bad incomplete c++ regex support as a temporary solution you can disable DMI support by using `-DWITH_DMI=OFF` CMake option.
Thank you.

## xmrig | 2021-02-27T08:30:47+00:00
Fixed in dev branch.

# Action History
- Created by: xguya | 2021-02-21T22:46:43+00:00
- Closed at: 2021-04-12T14:11:15+00:00
