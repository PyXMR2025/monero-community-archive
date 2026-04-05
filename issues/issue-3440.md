---
title: Getting error on raspberry pi 5
source_url: https://github.com/xmrig/xmrig/issues/3440
author: yashkathe
assignees: []
labels: []
created_at: '2024-03-11T05:09:13+00:00'
updated_at: '2024-03-11T21:27:19+00:00'
type: issue
status: closed
closed_at: '2024-03-11T21:27:19+00:00'
---

# Original Description
```
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
/home/yashkathe/xmrig/src/crypto/randomx/randomx.cpp: In member function ‘void RandomX_ConfigurationBase::Apply()’:
/home/yashkathe/xmrig/src/crypto/randomx/randomx.cpp:274:38: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                      ^~~~~~~~~~~~~~
/home/yashkathe/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/yashkathe/xmrig/src/crypto/randomx/randomx.cpp:291:9: note: in expansion of macro ‘INST_HANDLE’
  291 |         INST_HANDLE(IADD_RS, NULL);
      |         ^~~~~~~~~~~
/home/yashkathe/xmrig/src/crypto/randomx/randomx.cpp:274:76: error: ‘randomx::JitCompilerA64’ has not been declared
  274 | #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
      |                                                                            ^~~~~~~~~~~~~~
/home/yashkathe/xmrig/src/crypto/randomx/randomx.cpp:285:37: note: in expansion of macro ‘JIT_HANDLE’
  285 |         for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
      |                                     ^~~~~~~~~~
/home/yashkathe/xmrig/src/crypto/randomx/randomx.cpp:291:9: note: in expansion of macro ‘INST_HANDLE’
  291 |         INST_HANDLE(IADD_RS, NULL);

```

# Discussion History
## SChernykh | 2024-03-11T08:35:07+00:00
You're probably using 32-bit OS. You must compile XMRig in 64-bit.

## yashkathe | 2024-03-11T21:27:19+00:00
I tried to run it on Raspberry PI OS (64 bit) with desktop

But once I tried to install normal Raspberry pi OS without desktop it somehow worked
Thank You

# Action History
- Created by: yashkathe | 2024-03-11T05:09:13+00:00
- Closed at: 2024-03-11T21:27:19+00:00
