---
title: 'Complie Error: operand type mismatch for `vaesenc'''
source_url: https://github.com/xmrig/xmrig/issues/3081
author: evasive-stillness
assignees: []
labels: []
created_at: '2022-07-02T20:14:13+00:00'
updated_at: '2022-07-03T17:29:57+00:00'
type: issue
status: closed
closed_at: '2022-07-03T17:29:57+00:00'
---

# Original Description
When compiling xmrig using gcc 12.1, I'm getting this error:

```
…
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
/tmp/ccm3BGFb.s: Assembler messages:
/tmp/ccm3BGFb.s:388: Error: operand type mismatch for `vaesenc'
…
/tmp/ccm3BGFb.s:1269: Error: operand type mismatch for `vaesenc'
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/CryptoNight_x86_vaes.cpp.o] Error 1
…
```

I've tried gcc 10.2 as well, but same result.

OS: RHEL Server 7.9 (Maipo)
Kernel: Linux 3.10.0-1160.66.1.el7.x86_64
cmake: 3.18.4
gcc: 12.1.0
libtool: 2.4.6

I'm using the advanced build instructions found [here](https://xmrig.com/docs/miner/build/centos7). I've build this on other systems successfully, but it's just not compiling on this one system for some reason.


# Discussion History
## SChernykh | 2022-07-03T09:58:33+00:00
I've tested compilation with GCC 12 on Windows (MSYS2) and Ubuntu 22 and it works fine. It looks like you have incompatible `gas` (GNU Assembler) version which doesn't support VAES instructions properly.

## evasive-stillness | 2022-07-03T17:29:57+00:00
That was it! Using the latest version of [binutils](https://www.gnu.org/software/binutils/) (2.38) solved the problem. I was using 2.27.

Thank you!

# Action History
- Created by: evasive-stillness | 2022-07-02T20:14:13+00:00
- Closed at: 2022-07-03T17:29:57+00:00
