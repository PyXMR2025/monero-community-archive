---
title: '"xmring" namespace can''t be stripped on linux builds'
source_url: https://github.com/xmrig/xmrig/issues/2008
author: Frago9876543210
assignees: []
labels: []
created_at: '2020-12-25T17:34:00+00:00'
updated_at: '2021-04-12T14:26:16+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:26:16+00:00'
---

# Original Description
**Describe the bug**
On Linux builds symbols can't be stripped correctly. Binary file always contain ton of symbols. It is likely that this is due to abusing `static` keyword. This may affect the detection of the miner. E.g. just `cat xmrig-notls | grep -a xmrig` command can detect it or `strings`.

**To Reproduce**
Flags unlikely have anything to do with the issue
```bash
sudo apt install -y git build-essential cmake automake libtool autoconf
git clone --depth=1 https://github.com/xmrig/xmrig.git && cd xmrig
mkdir -p build && cd scripts
./build_deps.sh && cd ../build
cmake .. \
	-DWITH_CN_LITE=OFF \
	-DWITH_CN_HEAVY=OFF \
	-DWITH_CN_PICO=OFF \
	-DWITH_ARGON2=OFF \
	-DWITH_ASTROBWT=OFF \
	-DWITH_KAWPOW=OFF \
	-DWITH_HTTP=OFF \
	-DWITH_TLS=OFF \
	-DWITH_EMBEDDED_CONFIG=ON \
	-DWITH_OPENCL=OFF \
	-DWITH_CUDA=OFF \
	-DWITH_BENCHMARK=OFF \
	-DXMRIG_DEPS=scripts/deps
make -j$(nproc)

readelf -Ws xmrig-notls
```

```
   442: 0000000000126c40    29 FUNC    GLOBAL DEFAULT   14 _ZN5xmrig18SinglePoolStrategy17onVerifyAlgorithmEPKNS_7IClientERKNS_9AlgorithmEPb
   443: 000000000028aac0   251 FUNC    WEAK   DEFAULT   14 _ZNSt17moneypunct_bynameIwLb1EEC1ERKSsm
   444: 00000000002df9b0    91 FUNC    WEAK   DEFAULT   14 _ZNKSt10moneypunctIcLb1EE10neg_formatEv
   445: 00000000002b2e50   249 FUNC    WEAK   DEFAULT   14 _ZNSt7__cxx1115numpunct_bynameIwEC1EPKcm
   446: 0000000000595280    32 OBJECT  GLOBAL DEFAULT   28 _ZN7randomx7MacroOp6Add_riE
   447: 000000000057ecc8    40 OBJECT  WEAK   DEFAULT   24 _ZTVN5xmrig7FileLogE
   448: 000000000029a470    37 FUNC    WEAK   DEFAULT   14 _ZNSt7__cxx1114collate_bynameIcED1Ev
   449: 00000000002c1380     4 FUNC    WEAK   DEFAULT   14 _ZNSt15basic_streambufIcSt11char_traitsIcEE6setbufEPcl
   450: 00000000001d4830    58 FUNC    GLOBAL DEFAULT   14 _ZN5xmrig10MemoryPoolD0Ev
   451: 00000000002d06f0    23 FUNC    WEAK   DEFAULT   14 _ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEEC2Ev
   452: 00000000001faf16     0 NOTYPE  GLOBAL DEFAULT   14 CryptonightR_instruction100
   453: 00000000001faf19     0 NOTYPE  GLOBAL DEFAULT   14 CryptonightR_instruction101
   454: 00000000002de530    19 FUNC    WEAK   DEFAULT   14 _ZNSt8time_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEED1Ev
   455: 00000000001f2460    57 FUNC    GLOBAL DEFAULT   14 _ZN7randomx14JitCompilerX869h_ISWAP_RERKNS_11InstructionE
   456: 00000000001faf1b     0 NOTYPE  GLOBAL DEFAULT   14 CryptonightR_instruction102
   457: 0000000000153e50    47 FUNC    GLOBAL DEFAULT   14 _ZThn8_N5xmrig7Network17onVerifyAlgorithmEPNS_9IStrategyEPKNS_7IClientERKNS_9AlgorithmEPb
   458: 0000000000162c00     6 FUNC    GLOBAL DEFAULT   14 _ZN5xmrig13VirtualMemory20isHugepagesAvailableEv
```

```bash
#before using strip
$ du --bytes xmrig-notls
3719592	xmrig-notls

#trying to strip
$ strip --strip-all xmrig-notls

#after using strip
$ du --bytes xmrig-notls
3719592	xmrig-notls
```
Binary file size has not changed in this example.

**Expected behavior**
Symbols can be stripped using `strip --strip-all xmrig-notls` that can complicate the detection of the miner (**and also reduce binary size for releases**)

**Required data**
 - OS: Ubuntu 18.04 LTS


# Discussion History
## Spudz76 | 2020-12-25T18:08:42+00:00
Or if you're a hacker you could pack it with an exepacker and be done.
Not a very good script kiddie, get skillz.

## Frago9876543210 | 2020-12-25T18:14:32+00:00
@Spudz76 packer can reduce hashrate

## Spudz76 | 2020-12-25T18:33:29+00:00
Then run your own strip somewhere in your rootkitter script, hacker.  Will not be supported upstream as the only reason for it is unauthorized mining detection avoidance.  Thanks for the tip though.

AWWW my stolen hashrate is lower than maxxxxxx.  wow

# Action History
- Created by: Frago9876543210 | 2020-12-25T17:34:00+00:00
- Closed at: 2021-04-12T14:26:16+00:00
