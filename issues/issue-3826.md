---
title: Fail to build on PPC64
source_url: https://github.com/monero-project/monero/issues/3826
author: hegjon
assignees: []
labels: []
created_at: '2018-05-17T21:50:04+00:00'
updated_at: '2022-04-08T14:48:35+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:48:35+00:00'
---

# Original Description
Seems like this is the cause:
```
cc1: error: unrecognized command line option '-maes'
cc1: error: unrecognized command line option '-march=native'
```

Full log: https://kojipkgs.fedoraproject.org//work/tasks/3387/27023387/build.log

# Discussion History
## nioroso-x3 | 2018-05-18T02:24:11+00:00
Are you on big endian or little endian?
Some months ago I managed to modify the CMakeLists.txt enough to get it to compile, but in big endian ppc64 there are just too many endiannes problems. 
The daemon is unable to connect to anything and the cli wallet creates invalid keys.

## hegjon | 2018-05-18T08:01:50+00:00
Big Endian.

CPU info:
```
Architecture:        ppc64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Big Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  1
Socket(s):           4
NUMA node(s):        1
Model:               2.1 (pvr 004b 0201)
Model name:          POWER8 (architected), altivec supported
Hypervisor vendor:   KVM
Virtualization type: para
L1d cache:           64K
L1i cache:           32K
NUMA node0 CPU(s):   0-3
```

## hegjon | 2018-05-18T08:05:25+00:00
> Some months ago I managed to modify the CMakeLists.txt enough to get it to compile, but in big endian ppc64 there are just too many endiannes problems.

Would it be possible to white list those platforms that support `-maes` instead of having a list of the known platforms that does not support the flag?

## hyc | 2018-05-18T08:06:29+00:00
Yeah I think there's far too much dependency on little-endian math scattered throughout the code. Feel free to track all occurrences down and submit patches to fix them.

## nioroso-x3 | 2018-05-19T22:12:21+00:00
I created a pull request for the modified CMakeLists.
It compiles fine in gentoo ppc64, and almost in macos leopard.
Any pointers on where little endian math is most used? Most of the crypto source files seem to handle endianness fine.

## hegjon | 2018-05-21T20:59:50+00:00
> I created a pull request for the modified CMakeLists.

Thanks.

Why is it needed to set the `-mcpu` flags?

## nioroso-x3 | 2018-05-22T14:01:05+00:00
> Why is it needed to set the -mcpu flags?

-mcpu=native for some reason fails with G5 or ppc970 gcc, so I just set it manually to the lowest common denominator, a G4 for 32 bit, G5 for 64 bit and Power8 for 64 bit little endian.

## jtgrassie | 2018-05-23T12:06:56+00:00
@nioroso-x3 
> Any pointers on where little endian math is most used? Most of the crypto source files seem to handle endianness fine.

See:
https://github.com/monero-project/monero/blob/master/src/crypto/crypto-ops.c

A lot of the math in there is LE dependent.

## jtgrassie | 2018-05-23T12:24:31+00:00
Also, the crypto implementations in the src/crypto directory are the x86 implementations, for example, chacha has a different implementation for PowerPC: https://cr.yp.to/chacha.html.

## moneromooo-monero | 2018-10-06T18:46:05+00:00
Is it any better nowadays ? That particular thing got fixed a while ago.

## nioroso-x3 | 2018-10-19T03:21:30+00:00
> Is it any better nowadays ? That particular thing got fixed a while ago.

Monero is endian agnostic now? I haven't booted my power mac in a while, so I havent tested anything.

## moneromooo-monero | 2018-10-19T10:33:18+00:00
Well, we won't know for sure until someone reports another problem :)

## nioroso-x3 | 2018-10-19T20:50:26+00:00
Just compiled latest git, monerod fails all handshakes and monero-wallet-cli creates invalid keys and is unable to open valid wallets.

## moneromooo-monero | 2018-10-19T21:53:35+00:00
Can you start with unit_tests please ?

## moneromooo-monero | 2018-10-19T21:53:59+00:00
And crypto tests. "make release-test" should run them all.

## nioroso-x3 | 2018-10-20T01:56:44+00:00
This is the output:
Running tests...                                                   
Test project /home/jribeiro/Development/monero/build/Linux/master/release
      Start  1: hash-target                                             
 1/15 Test  #1: hash-target ......................   Passed    0.51 sec
      Start  2: core_tests                                                 
 2/15 Test  #2: core_tests .......................***Exception: Other7354.57 sec
      Start  3: cncrypto                                             
 3/15 Test  #3: cncrypto .........................***Failed   52.76 sec
      Start  4: unit_tests                               
 4/15 Test  #4: unit_tests .......................***Exception: Other335.84 sec
      Start  5: difficulty                              
 5/15 Test  #5: difficulty .......................   Passed    0.23 sec    
      Start  6: hash-fast                                           
 6/15 Test  #6: hash-fast ........................   Passed    0.08 sec
      Start  7: hash-slow                                       
 7/15 Test  #7: hash-slow ........................***Failed    1.36 sec
      Start  8: hash-slow-1                             
 8/15 Test  #8: hash-slow-1 ......................***Failed    1.61 sec     
      Start  9: hash-slow-2                                  
 9/15 Test  #9: hash-slow-2 ......................***Failed    4.72 sec
      Start 10: hash-tree                                  
10/15 Test #10: hash-tree ........................   Passed    0.19 sec
      Start 11: hash-extra-blake                        
11/15 Test #11: hash-extra-blake .................   Passed    0.04 sec
      Start 12: hash-extra-groestl                             
12/15 Test #12: hash-extra-groestl ...............***Failed    0.75 sec
      Start 13: hash-extra-jh                                   
13/15 Test #13: hash-extra-jh ....................   Passed    0.03 sec
      Start 14: hash-extra-skein                         
14/15 Test #14: hash-extra-skein .................   Passed    0.04 sec                       
      Start 15: hash-variant2-int-sqrt                 
15/15 Test #15: hash-variant2-int-sqrt ...........***Exception: Other166.52 sec

47% tests passed, 8 tests failed out of 15

Total Test time (real) = 7919.46 sec

The following tests FAILED:
          2 - core_tests (OTHER_FAULT)
          3 - cncrypto (Failed)
          4 - unit_tests (OTHER_FAULT)
          7 - hash-slow (Failed)
          8 - hash-slow-1 (Failed)
          9 - hash-slow-2 (Failed)
         12 - hash-extra-groestl (Failed)
         15 - hash-variant2-int-sqrt (OTHER_FAULT)
Errors while running CTest

The exceptions are because I killed the tests that were taking too long.
Attached is the core_tests log.

[core_tests.log.gz](https://github.com/monero-project/monero/files/2497720/core_tests.log.gz)


## moneromooo-monero | 2018-10-20T09:31:57+00:00
Can you please run and attach the output of these two commands:

./build/Linux/master/release/tests/crypto/cncrypto-tests tests/crypto/tests.txt
./build/Linux/master/release/tests/unit_tests/unit_tests



## nioroso-x3 | 2018-10-20T17:55:33+00:00
Ok, done.
[unit_tests.log.gz](https://github.com/monero-project/monero/files/2498393/unit_tests.log.gz)
[cncrypt-tests.log.gz](https://github.com/monero-project/monero/files/2498394/cncrypt-tests.log.gz)



## moneromooo-monero | 2018-10-20T19:10:48+00:00
Are you running with commit hash aa1d321e5f207a69161ffb919453dfe7311b9e61 ?

## nioroso-x3 | 2018-10-20T19:18:37+00:00
The short HEAD outputs 5c85da5, I cloned the repo yesterday.


## moneromooo-monero | 2018-10-20T21:20:31+00:00
The main problem seems to be Keccak being wrong. Which is a shame since the last change to Keccak was to allegedly make it work on big endian architectures :)
That is used for the PRNG, which in turn makes most of the crypto tests fail.


## moneromooo-monero | 2018-10-20T21:27:58+00:00
As for the IP errors, this should fix it:

<pre>
diff --git a/contrib/epee/include/net/local_ip.h b/contrib/epee/include/net/local_ip.h
index 52c5855b9..90e6a07b0 100644
--- a/contrib/epee/include/net/local_ip.h
+++ b/contrib/epee/include/net/local_ip.h
@@ -27,6 +27,15 @@
 
 #pragma once
 
+namespace
+{
+  static inline uint32_t leip(uint32_t x)
+  {
+    x = ((x & 0x00ff00ff) << 8) | ((x & 0xff00ff00) >> 8);
+    return (x << 16) | (x >> 16);
+  }
+}
+
 namespace epee
 {
   namespace net_utils
@@ -34,6 +43,7 @@ namespace epee
     inline
     bool is_ip_local(uint32_t ip)
     {
+      ip = leip(ip);
       /*
       local ip area
       10.0.0.0 <97> 10.255.255.255 
@@ -57,6 +67,7 @@ namespace epee
     inline
     bool is_ip_loopback(uint32_t ip)
     {
+      ip = leip(ip);
       if( (ip | 0xffffff00) == 0xffffff7f)
         return true;
       //MAKE_IP
</pre>

## moneromooo-monero | 2018-10-20T21:46:16+00:00
This might fix the keccak part (edited, needs more parentheses):

<pre>
diff --git a/src/crypto/keccak.c b/src/crypto/keccak.c
index b5946036e..ee20adb2d 100644
--- a/src/crypto/keccak.c
+++ b/src/crypto/keccak.c
@@ -145,7 +145,7 @@ void keccak1600(const uint8_t *in, size_t inlen, uint8_t *md)
 #define IS_ALIGNED_64(p) (0 == (7 & ((const char*)(p) - (const char*)0)))
 #define KECCAK_PROCESS_BLOCK(st, block) { \
     for (int i_ = 0; i_ < KECCAK_WORDS; i_++){ \
-        ((st))[i_] ^= ((block))[i_]; \
+        ((st))[i_] ^= swap64le(((block))[i_]); \
     }; \
     keccakf(st, KECCAK_ROUNDS); }
 

</pre>

## moneromooo-monero | 2018-10-20T23:00:58+00:00
The IP stuff is wrong, the IPs should be in network byte order. If they're not, then somhting else is probably wrong.

## moneromooo-monero | 2018-10-20T23:07:40+00:00
Or maybe not. That will need thinking.

## nioroso-x3 | 2018-10-21T01:12:38+00:00
The patches didnt change much.

Test project /home/jribeiro/Development/monero/build/Linux/master/release                                                                                                                                          
      Start  1: hash-target                                                                                                                                                                                        
 1/15 Test  #1: hash-target ......................   Passed    0.42 sec                                                                                                                                            
      Start  2: core_tests                                                                                                                                                                                         
 2/15 Test  #2: core_tests .......................***Exception: Other5903.01 sec                                                                                                                                  
      Start  3: cncrypto                                                                                                                                                                                           
 3/15 Test  #3: cncrypto .........................***Failed   67.77 sec                                                                                                                                            
      Start  4: unit_tests                                                                                                                                                                                         
 4/15 Test  #4: unit_tests .......................***Failed  849.29 sec                                                                                                                                            
      Start  5: difficulty
 5/15 Test  #5: difficulty .......................   Passed    0.24 sec
      Start  6: hash-fast
 6/15 Test  #6: hash-fast ........................   Passed    0.08 sec
      Start  7: hash-slow
 7/15 Test  #7: hash-slow ........................***Failed    1.37 sec
      Start  8: hash-slow-1
 8/15 Test  #8: hash-slow-1 ......................***Failed    1.79 sec
      Start  9: hash-slow-2
 9/15 Test  #9: hash-slow-2 ......................***Failed    4.75 sec
      Start 10: hash-tree
10/15 Test #10: hash-tree ........................   Passed    0.03 sec
      Start 11: hash-extra-blake
11/15 Test #11: hash-extra-blake .................   Passed    0.04 sec
      Start 12: hash-extra-groestl
12/15 Test #12: hash-extra-groestl ...............***Failed    0.68 sec
      Start 13: hash-extra-jh
13/15 Test #13: hash-extra-jh ....................   Passed    0.03 sec
      Start 14: hash-extra-skein
14/15 Test #14: hash-extra-skein .................   Passed    0.04 sec
      Start 15: hash-variant2-int-sqrt
15/15 Test #15: hash-variant2-int-sqrt ...........   Passed  1178.90 sec

[cncrypto-tests.log.gz](https://github.com/monero-project/monero/files/2498703/cncrypto-tests.log.gz)
[unit_tests.log.gz](https://github.com/monero-project/monero/files/2498704/unit_tests.log.gz)


## moneromooo-monero | 2018-10-21T08:44:12+00:00
Well, you're going to have to debug it I'm afraid, or wait for someone else with big endian hardware to have a look. Since it was recently "fixed" for big endian, it should be mostly there already.


## nioroso-x3 | 2018-10-21T18:27:42+00:00
I have zero knowledge of how monero works, what should I look into first?
Get the functions of keccak.c to have the same output as little endian machines?

## moneromooo-monero | 2018-10-21T21:35:16+00:00
Since the (primary) culprit seems to be Keccak, you don't need to know how monero works, just how to build it. The Keccak output for a given input should indeed be identical on big and little endian archs. I suspect once Keccak's fixed, a lot of stuff will start working. We can then see what's next in line.
Thanks

## xiphon | 2018-10-22T06:52:46+00:00
@nioroso-x3 
Please apply the patch from attached PR, run the tests and provide the logs.

## nioroso-x3 | 2018-10-24T23:17:14+00:00
From the unit_test logs seems like keccak is fixed now.
[cncrypto-tests.log.gz](https://github.com/monero-project/monero/files/2512673/cncrypto-tests.log.gz)
[unit_tests.log.gz](https://github.com/monero-project/monero/files/2512674/unit_tests.log.gz)
[core_tests.log.gz](https://github.com/monero-project/monero/files/2512676/core_tests.log.gz)


Test project /home/jribeiro/Development/monero/build/Linux/master/release                                                                                                                  
      Start  1: hash-target                                                                                                                                                                
 1/15 Test  #1: hash-target ......................   Passed    0.31 sec                                                                                                                    
      Start  2: core_tests                                                                                                                                                                 
 2/15 Test  #2: core_tests .......................***Exception: Other3939.69 sec                                                                                                           
      Start  3: cncrypto                                                                                                                                                                   
 3/15 Test  #3: cncrypto .........................***Failed   57.74 sec                                                                                                                    
      Start  4: unit_tests                                                                                                                                                                 
 4/15 Test  #4: unit_tests .......................***Failed  811.43 sec                                                                                                                    
      Start  5: difficulty                                                                                                                                                                 
 5/15 Test  #5: difficulty .......................   Passed    0.24 sec                                                                                                                    
      Start  6: hash-fast                                                                                                                                                                  
 6/15 Test  #6: hash-fast ........................   Passed    0.06 sec                                                                                                                    
      Start  7: hash-slow                                                                                                                                                                  
 7/15 Test  #7: hash-slow ........................***Failed    1.36 sec                                                                                                                    
      Start  8: hash-slow-1                                                                                                                                                                
 8/15 Test  #8: hash-slow-1 ......................***Failed    1.65 sec                                                                                                                    
      Start  9: hash-slow-2                                                                                                                                                                
 9/15 Test  #9: hash-slow-2 ......................***Failed    4.86 sec                                                                                                                    
      Start 10: hash-tree                                                                                                                                                                  
10/15 Test #10: hash-tree ........................   Passed    0.19 sec                                                                                                                    
      Start 11: hash-extra-blake                                                                                                                                                           
11/15 Test #11: hash-extra-blake .................   Passed    0.04 sec                                                                                                                    
      Start 12: hash-extra-groestl                                                                                                                                                         
12/15 Test #12: hash-extra-groestl ...............***Failed    0.71 sec                                                                                                                    
      Start 13: hash-extra-jh                                                                                                                                                              
13/15 Test #13: hash-extra-jh ....................   Passed    0.03 sec                                                                                                                    
      Start 14: hash-extra-skein                                                                                                                                                           
14/15 Test #14: hash-extra-skein .................   Passed    0.03 sec                                                                                                                    
      Start 15: hash-variant2-int-sqrt                                                                                                                                                     
15/15 Test #15: hash-variant2-int-sqrt ...........   Passed  1314.93 sec                                                                                                                   
                                                                                                                                                                                           
53% tests passed, 7 tests failed out of 15                                                                                                                                                 
                                                                                                                                                                                           
Total Test time (real) = 6133.48 sec                                                                                                                                                       

The following tests FAILED:
          2 - core_tests (OTHER_FAULT)
          3 - cncrypto (Failed)
          4 - unit_tests (Failed)
          7 - hash-slow (Failed)
          8 - hash-slow-1 (Failed)
          9 - hash-slow-2 (Failed)
         12 - hash-extra-groestl (Failed)


## xiphon | 2018-10-24T23:44:53+00:00
Thanks, will ping you to test further big-endian patches on hardware if you don't mind

## xiphon | 2018-10-25T02:08:47+00:00
@nioroso-x3 updated #4689 with fixes for groestl. Please test the new version, 

## moneromooo-monero | 2018-10-25T09:17:21+00:00
That one might fix the mnemonics unit test:

<pre>
diff --git a/src/mnemonics/electrum-words.cpp b/src/mnemonics/electrum-words.cpp
index 3d6338856..ba2c8e120 100644
--- a/src/mnemonics/electrum-words.cpp
+++ b/src/mnemonics/electrum-words.cpp
@@ -335,7 +335,8 @@ namespace crypto
           return false;
         }
 
-        dst.append((const char*)&w[0], 4);  // copy 4 bytes to position
+        uint32_t w0 = SWAP32LE(*(const uint32_t*)&w[0]);
+        dst.append((const char*)&w0, 4);  // copy 4 bytes to position
         memwipe(w, sizeof(w));
       }
 
</pre>

## nioroso-x3 | 2018-10-25T17:46:38+00:00
Groestl and the mnemonics tests now pass.

Test project /home/jribeiro/Development/monero/build/Linux/master/release                                              
      Start  1: hash-target                                                                                            
 1/15 Test  #1: hash-target ......................   Passed    0.52 sec                                                
      Start  2: core_tests                                                                                             
 2/15 Test  #2: core_tests .......................***Exception: Other641.52 sec                                        
      Start  3: cncrypto                                                                                               
 3/15 Test  #3: cncrypto .........................***Failed   53.65 sec                                                
      Start  4: unit_tests
 4/15 Test  #4: unit_tests .......................***Failed  829.74 sec
      Start  5: difficulty
 5/15 Test  #5: difficulty .......................   Passed    0.06 sec
      Start  6: hash-fast
 6/15 Test  #6: hash-fast ........................   Passed    0.07 sec
      Start  7: hash-slow
 7/15 Test  #7: hash-slow ........................***Failed    1.39 sec
      Start  8: hash-slow-1
 8/15 Test  #8: hash-slow-1 ......................***Failed    1.66 sec
      Start  9: hash-slow-2
 9/15 Test  #9: hash-slow-2 ......................***Failed    4.89 sec
      Start 10: hash-tree
10/15 Test #10: hash-tree ........................   Passed    0.19 sec
      Start 11: hash-extra-blake
11/15 Test #11: hash-extra-blake .................   Passed    0.04 sec
      Start 12: hash-extra-groestl
12/15 Test #12: hash-extra-groestl ...............   Passed    0.06 sec
      Start 13: hash-extra-jh
13/15 Test #13: hash-extra-jh ....................   Passed    0.04 sec
      Start 14: hash-extra-skein
14/15 Test #14: hash-extra-skein .................   Passed    0.04 sec
      Start 15: hash-variant2-int-sqrt
15/15 Test #15: hash-variant2-int-sqrt ...........   Passed  1351.16 sec

[unit_tests.log.gz](https://github.com/monero-project/monero/files/2516127/unit_tests.log.gz)
[cncrypto-tests.log.gz](https://github.com/monero-project/monero/files/2516128/cncrypto-tests.log.gz)


## moneromooo-monero | 2018-10-25T20:41:24+00:00
That might fix the remainder of the RNG:

<pre>
diff --git a/src/crypto/hash.c b/src/crypto/hash.c
index 42f272e34..d8c549f19 100644
--- a/src/crypto/hash.c
+++ b/src/crypto/hash.c
@@ -36,7 +36,14 @@
 #include "keccak.h"
 
 void hash_permutation(union hash_state *state) {
+#if BYTE_ORDER == LITTLE_ENDIAN
   keccakf((uint64_t*)state, 24);
+#else
+  uint64_t le_state[24];
+  memcpy_swap64le(le_state, state, 24);
+  keccakf(le_state, 24);
+  memcpy_swap64le(state, le_state, 24);
+#endif
 }
 void hash_process(union hash_state *state, const uint8_t *buf, size_t count) {


## nioroso-x3 | 2018-10-26T00:22:28+00:00
Your patch to hash.c causes this error:
*** stack smashing detected ***: <unknown> terminated
Aborted


## moneromooo-monero | 2018-10-26T08:29:13+00:00
Oooh, the 24 is the number of rounds, my mistake.  Here's a fixed version:

<pre>
diff --git a/src/crypto/hash.c b/src/crypto/hash.c
index 42f272e34..43ce32957 100644
--- a/src/crypto/hash.c
+++ b/src/crypto/hash.c
@@ -36,7 +36,14 @@
 #include "keccak.h"
 
 void hash_permutation(union hash_state *state) {
+#if BYTE_ORDER == LITTLE_ENDIAN
   keccakf((uint64_t*)state, 24);
+#else
+  uint64_t le_state[25];
+  memcpy_swap64le(le_state, state, 25);
+  keccakf(le_state, 24);
+  memcpy_swap64le(state, le_state, 25);
+#endif
 }
 
 void hash_process(union hash_state *state, const uint8_t *buf, size_t count) {
</pre>


## nioroso-x3 | 2018-10-29T17:39:08+00:00
cncrypto tests now pass

      Start  1: hash-target
 1/15 Test  #1: hash-target ......................   Passed    0.50 sec
      Start  2: core_tests
 2/15 Test  #2: core_tests .......................***Exception: Other2284.95 sec
      Start  3: cncrypto
 3/15 Test  #3: cncrypto .........................   Passed   40.11 sec
      Start  4: unit_tests
 4/15 Test  #4: unit_tests .......................***Failed  815.90 sec
      Start  5: difficulty
 5/15 Test  #5: difficulty .......................   Passed    0.07 sec
      Start  6: hash-fast
 6/15 Test  #6: hash-fast ........................   Passed    0.07 sec
      Start  7: hash-slow
 7/15 Test  #7: hash-slow ........................***Failed    1.23 sec
      Start  8: hash-slow-1
 8/15 Test  #8: hash-slow-1 ......................***Failed    1.76 sec
      Start  9: hash-slow-2
 9/15 Test  #9: hash-slow-2 ......................***Failed    3.37 sec
      Start 10: hash-tree
10/15 Test #10: hash-tree ........................   Passed    0.04 sec
      Start 11: hash-extra-blake
11/15 Test #11: hash-extra-blake .................   Passed    0.04 sec
      Start 12: hash-extra-groestl
12/15 Test #12: hash-extra-groestl ...............   Passed    0.06 sec
      Start 13: hash-extra-jh
13/15 Test #13: hash-extra-jh ....................   Passed    0.04 sec
      Start 14: hash-extra-skein
14/15 Test #14: hash-extra-skein .................   Passed    0.04 sec
      Start 15: hash-variant2-int-sqrt
15/15 Test #15: hash-variant2-int-sqrt ...........   Passed  1240.98 sec

[unit_tests.log.gz](https://github.com/monero-project/monero/files/2526378/unit_tests.log.gz)
[core_tests.log.gz](https://github.com/monero-project/monero/files/2526379/core_tests.log.gz)
[cncrypto-tests.log.gz](https://github.com/monero-project/monero/files/2526380/cncrypto-tests.log.gz)


## xiphon | 2018-10-29T22:00:57+00:00
#4755

## nioroso-x3 | 2018-10-30T01:49:58+00:00
nvm, looks like its a WIP.

## moneromooo-monero | 2018-10-30T18:59:05+00:00
For the slow hash tests:

<pre>
diff --git a/src/crypto/slow-hash.c b/src/crypto/slow-hash.c
index 40cfb0461..ce716b652 100644
--- a/src/crypto/slow-hash.c
+++ b/src/crypto/slow-hash.c
@@ -109,8 +109,8 @@ extern int aesb_pseudo_round(const uint8_t *in, uint8_t *out, const uint8_t *exp
     memcpy(b + AES_BLOCK_SIZE, state.hs.b + 64, AES_BLOCK_SIZE); \
     xor64(b + AES_BLOCK_SIZE, state.hs.b + 80); \
     xor64(b + AES_BLOCK_SIZE + 8, state.hs.b + 88); \
-    division_result = state.hs.w[12]; \
-    sqrt_result = state.hs.w[13]; \
+    division_result = SWAP64LE(state.hs.w[12]); \
+    sqrt_result = SWAP64LE(state.hs.w[13]); \
   } while (0)
 
 #define VARIANT2_SHUFFLE_ADD_SSE2(base_ptr, offset) \
@@ -145,30 +145,31 @@ extern int aesb_pseudo_round(const uint8_t *in, uint8_t *out, const uint8_t *exp
     const uint64_t chunk1_old[2] = { chunk1[0], chunk1[1] }; \
     \
     uint64_t b1[2]; \
-    memcpy(b1, b + 16, 16); \
-    chunk1[0] = chunk3[0] + b1[0]; \
-    chunk1[1] = chunk3[1] + b1[1]; \
+    memcpy_swap64le(b1, b + 16, 2); \
+    chunk1[0] = SWAP64LE(chunk3[0] + b1[0]); \
+    chunk1[1] = SWAP64LE(chunk3[1] + b1[1]); \
     \
     uint64_t a0[2]; \
-    memcpy(a0, a, 16); \
-    chunk3[0] = chunk2[0] + a0[0]; \
-    chunk3[1] = chunk2[1] + a0[1]; \
+    memcpy_swap64le(a0, a, 2); \
+    chunk3[0] = SWAP64LE(chunk2[0] + a0[0]); \
+    chunk3[1] = SWAP64LE(chunk2[1] + a0[1]); \
     \
     uint64_t b0[2]; \
-    memcpy(b0, b, 16); \
-    chunk2[0] = chunk1_old[0] + b0[0]; \
-    chunk2[1] = chunk1_old[1] + b0[1]; \
+    memcpy_swap64le(b0, b, 2); \
+    chunk2[0] = SWAP64LE(chunk1_old[0] + b0[0]); \
+    chunk2[1] = SWAP64LE(chunk1_old[1] + b0[1]); \
   } while (0)
 
 #define VARIANT2_INTEGER_MATH_DIVISION_STEP(b, ptr) \
-  ((uint64_t*)(b))[0] ^= division_result ^ (sqrt_result << 32); \
+  uint64_t tmpx = division_result ^ (sqrt_result << 32); \
+  ((uint64_t*)(b))[0] ^= SWAP64LE(tmpx); \
   { \
-    const uint64_t dividend = ((uint64_t*)(ptr))[1]; \
-    const uint32_t divisor = (((uint64_t*)(ptr))[0] + (uint32_t)(sqrt_result << 1)) | 0x80000001UL; \
+    const uint64_t dividend = SWAP64LE(((uint64_t*)(ptr))[1]); \
+    const uint32_t divisor = (SWAP64LE(((uint64_t*)(ptr))[0]) + (uint32_t)(sqrt_result << 1)) | 0x80000001UL; \
     division_result = ((uint32_t)(dividend / divisor)) + \
                      (((uint64_t)(dividend % divisor)) << 32); \
   } \
-  const uint64_t sqrt_input = ((uint64_t*)(ptr))[0] + division_result
+  const uint64_t sqrt_input = SWAP64LE(((uint64_t*)(ptr))[0]) + division_result
 
 #define VARIANT2_INTEGER_MATH_SSE2(b, ptr) \
   do if (variant >= 2) \
@@ -207,14 +208,14 @@ extern int aesb_pseudo_round(const uint8_t *in, uint8_t *out, const uint8_t *exp
 #define VARIANT2_2() \
   do if (variant >= 2) \
   { \
-    *U64(hp_state + (j ^ 0x10)) ^= hi; \
-    *(U64(hp_state + (j ^ 0x10)) + 1) ^= lo; \
-    hi ^= *U64(hp_state + (j ^ 0x20)); \
-    lo ^= *(U64(hp_state + (j ^ 0x20)) + 1); \
+    *U64(hp_state + (j ^ 0x10)) ^= SWAP64LE(hi); \
+    *(U64(hp_state + (j ^ 0x10)) + 1) ^= SWAP64LE(lo); \
+    hi ^= SWAP64LE(*U64(hp_state + (j ^ 0x20))); \
+    lo ^= SWAP64LE(*(U64(hp_state + (j ^ 0x20)) + 1)); \
   } while (0)
 
 
-#if !defined NO_AES && (defined(__x86_64__) || (defined(_MSC_VER) && defined(_WIN64)))
+#if 0 && !defined NO_AES && (defined(__x86_64__) || (defined(_MSC_VER) && defined(_WIN64)))
 // Optimised code below, uses x86-specific intrinsics, SSE2, AES-NI
 // Fall back to more portable code is down at the bottom
 
@@ -1411,7 +1412,7 @@ static void (*const extra_hashes[4])(const void *, size_t, char *) = {
 extern int aesb_single_round(const uint8_t *in, uint8_t*out, const uint8_t *expandedKey);
 extern int aesb_pseudo_round(const uint8_t *in, uint8_t *out, const uint8_t *expandedKey);
 
-static size_t e2i(const uint8_t* a, size_t count) { return (*((uint64_t*)a) / AES_BLOCK_SIZE) & (count - 1); }
+static size_t e2i(const uint8_t* a, size_t count) { return (SWAP64LE(*((uint64_t*)a)) / AES_BLOCK_SIZE) & (count - 1); }
 
 static void mul(const uint8_t* a, const uint8_t* b, uint8_t* res) {
   uint64_t a0, b0;
</pre>

## jtgrassie | 2018-10-30T19:32:03+00:00
@moneromooo-monero hey moo, are all your PPC patches in a branch somewhere? I plan on doing some tests with them (and the the PRs).

## moneromooo-monero | 2018-10-30T19:35:59+00:00
Not a single one. The ones that were reported to work are PRed (4757, 4726). xiphon has 4689. 

## xiphon | 2018-10-31T03:53:08+00:00
#4755  And another one patch. Fixed software AES encryption on big endian.

@nioroso-x3 please do the following:
1. Apply https://github.com/monero-project/monero/issues/3826#issuecomment-434428054
2. Run tests
3. Apply #4755 
4. Run tests

## jtgrassie | 2018-10-31T18:15:17+00:00
Thanks both. I'll get some time this w/e hopefully so will get these in, test then move onto some of the other bits not covered by tests.

## nioroso-x3 | 2018-11-01T19:32:57+00:00
> #4755 And another one patch. Fixed software AES encryption on big endian.
> 
> @nioroso-x3 please do the following:
> 
> 1. Apply [#3826 (comment)](https://github.com/monero-project/monero/issues/3826#issuecomment-434428054)
> 2. Run tests
> 3. Apply #4755
> 4. Run tests

Patch [#3826 (comment)](https://github.com/monero-project/monero/issues/3826#issuecomment-434428054) had no visible effects.
With patch #4755 hash-slow and hash-slow-1 pass, but hash-slow-2 fails.
There were no changes for cncrypto and unit_tests with both patches, Serialization.portability still fails.


## moneromooo-monero | 2018-11-01T22:43:38+00:00
Curious that 3826 has no visible effect since e2i is very unlikely to only pick data where the swap64le is equal to the input. if hash-slow works without it, adding it should break it. If you put a #warning in that function, does it get triggered ? Just to check you're using the version I thought you'd be using.

## xiphon | 2018-11-02T01:08:54+00:00
@nioroso-x3 
Please apply this one on top of the current working tree and check the tests
```diff
diff --git a/src/crypto/slow-hash.c b/src/crypto/slow-hash.c
index cc3f79c7..3c56e9d7 100644
--- a/src/crypto/slow-hash.c
+++ b/src/crypto/slow-hash.c
@@ -154,18 +154,18 @@ extern int aesb_pseudo_round(const uint8_t *in, uint8_t *out, const uint8_t *exp
     \
     uint64_t b1[2]; \
     memcpy_swap64le(b1, b + 16, 2); \
-    chunk1[0] = SWAP64LE(chunk3[0] + b1[0]); \
-    chunk1[1] = SWAP64LE(chunk3[1] + b1[1]); \
+    chunk1[0] = SWAP64LE(SWAP64LE(chunk3[0]) + b1[0]); \
+    chunk1[1] = SWAP64LE(SWAP64LE(chunk3[1]) + b1[1]); \
     \
     uint64_t a0[2]; \
     memcpy_swap64le(a0, a, 2); \
-    chunk3[0] = SWAP64LE(chunk2[0] + a0[0]); \
-    chunk3[1] = SWAP64LE(chunk2[1] + a0[1]); \
+    chunk3[0] = SWAP64LE(SWAP64LE(chunk2[0]) + a0[0]); \
+    chunk3[1] = SWAP64LE(SWAP64LE(chunk2[1]) + a0[1]); \
     \
     uint64_t b0[2]; \
     memcpy_swap64le(b0, b, 2); \
-    chunk2[0] = SWAP64LE(chunk1_old[0] + b0[0]); \
-    chunk2[1] = SWAP64LE(chunk1_old[1] + b0[1]); \
+    chunk2[0] = SWAP64LE(SWAP64LE(chunk1_old[0]) + b0[0]); \
+    chunk2[1] = SWAP64LE(SWAP64LE(chunk1_old[1]) + b0[1]); \
   } while (0)
 
 #define VARIANT2_INTEGER_MATH_DIVISION_STEP(b, ptr) \
```

## moneromooo-monero | 2018-11-02T01:43:14+00:00
Oh nice catch :)

## nioroso-x3 | 2018-11-02T03:05:32+00:00
hash-slow-2 now passes.


## moneromooo-monero | 2018-11-02T09:35:48+00:00
Excellent, those patches are now in https://github.com/monero-project/monero/pull/4781
xiphon, if you prefer PRing yours separately, let me know and I'll amend.
Can you share the new core tests log now please ?

## xiphon | 2018-11-02T12:40:57+00:00
> xiphon, if you prefer PRing yours separately, let me know and I'll amend.

Ah, i don't care. You included the fix into #4781 and specified me as a co-author, so it i'm absolutely fine with how #4781 is done.

Just curious about this define https://github.com/monero-project/monero/pull/4781#pullrequestreview-171079489. i guess we don't have to change it.
Would be better to test the code with previous define version. @nioroso-x3 , could you?

## moneromooo-monero | 2018-11-02T12:45:10+00:00
It was a debug thing I left in, fixed.Thanks for spotting it.

## nioroso-x3 | 2018-11-02T18:32:03+00:00
I fixed the define mentioned by xiphon, slow-hash tests continue to pass with no problems.
Core tests always gets stuck after the gen_block_is_too_big test, CPU load is 0%, so I just killed it.

[cncrypto-tests.log.gz](https://github.com/monero-project/monero/files/2543701/cncrypto-tests.log.gz)
[core_tests.log.gz](https://github.com/monero-project/monero/files/2543702/core_tests.log.gz)
[unit_tests.log.gz](https://github.com/monero-project/monero/files/2543703/unit_tests.log.gz)


Running tests...
Test project /home/jribeiro/Development/monero/build/Linux/master/release
      Start  1: hash-target
 1/15 Test  #1: hash-target ......................   Passed    0.27 sec
      Start  2: core_tests
 2/15 Test  #2: core_tests .......................***Exception: Other5436.55 sec
      Start  3: cncrypto
 3/15 Test  #3: cncrypto .........................   Passed   66.04 sec
      Start  4: unit_tests
 4/15 Test  #4: unit_tests .......................***Failed  789.18 sec
      Start  5: difficulty
 5/15 Test  #5: difficulty .......................   Passed    0.07 sec
      Start  6: hash-fast
 6/15 Test  #6: hash-fast ........................   Passed    0.06 sec
      Start  7: hash-slow
 7/15 Test  #7: hash-slow ........................   Passed    1.42 sec
      Start  8: hash-slow-1
 8/15 Test  #8: hash-slow-1 ......................   Passed    1.83 sec
      Start  9: hash-slow-2
 9/15 Test  #9: hash-slow-2 ......................   Passed    5.49 sec
      Start 10: hash-tree
10/15 Test #10: hash-tree ........................   Passed    0.02 sec
      Start 11: hash-extra-blake
11/15 Test #11: hash-extra-blake .................   Passed    0.04 sec
      Start 12: hash-extra-groestl
12/15 Test #12: hash-extra-groestl ...............   Passed    0.05 sec
      Start 13: hash-extra-jh
13/15 Test #13: hash-extra-jh ....................   Passed    0.04 sec
      Start 14: hash-extra-skein
14/15 Test #14: hash-extra-skein .................   Passed    0.04 sec
      Start 15: hash-variant2-int-sqrt
15/15 Test #15: hash-variant2-int-sqrt ...........   Passed  1350.47 sec

87% tests passed, 2 tests failed out of 15

Total Test time (real) = 7651.73 sec

The following tests FAILED:
          2 - core_tests (OTHER_FAULT)
          4 - unit_tests (Failed)


## moneromooo-monero | 2018-11-02T22:34:00+00:00
The test afer is_too_big is a really slow one. It'll take some time, leave it on :)

All tests so far before this one passed, so it's encouraging.

## moneromooo-monero | 2018-11-02T22:35:45+00:00
Actually, I see you've run for like an hour and a half, that might be a bit much. Can you get an all thread stack trace after it's been stuck for a wihle ?

gdb build/release/core_tests/core_tests \`pidof core_tests\`
thread apply all bt

(s/release/debug/ if you built a debug build, bettter debug info)


## nioroso-x3 | 2018-11-03T03:08:33+00:00
I get this, compiled with debug-test this time

Attaching to program: /home/jribeiro/Development/monero/build/Linux/master/debug/tests/core_tests/core_tests, process 6500
[New LWP 6502]
[New LWP 6503]
[New LWP 6504]
0x00003fffa44eba14 in ?? ()
(gdb) thread apply all bt

Thread 4 (LWP 6504):
#0  0x00003fffa399165c in ?? ()
#1  0x00003fffa399163c in ?? ()
#2  0x00003fffa48245c0 in ?? ()
#3  0x00003fffa4827c88 in ?? ()
#4  0x00003fffa3d759e0 in ?? ()
#5  0x00003fffa398820c in ?? ()
#6  0x00003fffa38c6e30 in ?? ()

Thread 3 (LWP 6503):
#0  0x00003fffa399165c in ?? ()
#1  0x00003fffa399163c in ?? ()
#2  0x00003fffa48245c0 in ?? ()
#3  0x00003fffa4827c88 in ?? ()
#4  0x00003fffa3d759e0 in ?? ()
#5  0x00003fffa398820c in ?? ()
#6  0x00003fffa38c6e30 in ?? ()

Thread 2 (LWP 6502):
#0  0x00003fffa399165c in ?? ()
#1  0x00003fffa399163c in ?? ()
#2  0x00003fffa48245c0 in ?? ()
#3  0x00003fffa4827c88 in ?? ()
#4  0x00003fffa3d759e0 in ?? ()
#5  0x00003fffa398820c in ?? ()
#6  0x00003fffa38c6e30 in ?? ()

Thread 1 (LWP 6500):
#0  0x00003fffa44eba14 in ?? ()
#1  0x00003fffa44ec59c in ?? ()
#2  0x00003fffa4b16114 in ?? ()
#3  0x00003fffa4b34a4c in ?? ()
#4  0x000000010088d024 in ?? ()
#5  0x0000000100891af0 in ?? ()
#6  0x00000001008733c0 in ?? ()
#7  0x0000000100875a78 in ?? ()
#8  0x00000001008abac8 in ?? ()
#9  0x00003fffa37cd188 in ?? ()
#10 0x00003fffa37cd3b0 in ?? ()
#11 0x0000000000000000 in ?? ()


## nioroso-x3 | 2018-11-03T03:12:03+00:00
After detaching gdb cores_tests segfaulted.

## moneromooo-monero | 2018-11-03T10:22:21+00:00
Something is off, even release should have better trace... Did gdb complain about anything when loading ?

## nioroso-x3 | 2018-11-03T16:39:32+00:00
Nope, it loaded all symbols.

## moneromooo-monero | 2018-11-03T19:56:58+00:00
Alright, please try with that particular test (invalid_binary_format) disabled by commenting it out in tests/core_tests/chaingen_main.cpp.


## nioroso-x3 | 2018-11-04T00:50:47+00:00
Ok, now it crashed after the "gen_bp_tx_invalid_borromean_type" test.
Finally the log increased quite a lot.

[core_tests.log.gz](https://github.com/monero-project/monero/files/2545448/core_tests.log.gz)


## moneromooo-monero | 2018-11-04T10:40:42+00:00
Nice, that's all of them except the one you commented :)
The crash at the end is fixed in #4785, unrelated to endianness.
For the remaining (invalid_binary_format), are you able to run with valgrind or ASAN ?
With valgrind, you just prepend "valgrind " to your normal command line.
With ASAN, you build monero with -D SANITIZE=ON on the cmake command line.
ASAN is best if you can (much faster, detects more problems), but might not be available on your particular arch.

## moneromooo-monero | 2018-11-04T10:46:18+00:00
BTW, if you want to run just one test, you can use --filter=regexp
So here, --filter=\\\*invalid_binary_format\\\*

## nioroso-x3 | 2018-11-05T01:06:48+00:00
Valgrind seems to complain a lot about invalid writes and reads in slow-hash.
I ran this using the filter, so only the invalid_binary_format test is running.

[core_tests_valgrind.log.gz](https://github.com/monero-project/monero/files/2546542/core_tests_valgrind.log.gz)

I also ran it without the filter, it also complains about the same lines.

[core_tests_full_valgrind.log.gz](https://github.com/monero-project/monero/files/2546545/core_tests_full_valgrind.log.gz)

I can make an account on my powermac for a dev, it has 4 cores, 8gb of ram and a SSD, should be a lot faster than running a qemu vm.


## moneromooo-monero | 2018-11-05T09:43:17+00:00
Try adding "--max-stackframe=4000000" to the valgrind command line. the Cryptonight stacks need to be large.

## nioroso-x3 | 2018-11-05T17:15:00+00:00
Ok, core_tests crashed with segfault inside valgrind now, but much earlier.

[core_tests_full_valgrind.log.gz](https://github.com/monero-project/monero/files/2549760/core_tests_full_valgrind.log.gz)



## moneromooo-monero | 2018-11-05T20:33:17+00:00
Looks like some compiler or lib problem. Try adding "-D STACK_TRACE=OFF" to the cmake command line.


## jtgrassie | 2018-11-06T14:33:07+00:00
Ubuntu 16, PowerPC BE, 32 bit. PRs: (#4796, #4726, #4689, #4781, #4757, #4755).

**core_tests** took too long so I bailed on that.

**unit_tests** failed. Looks like something to do with -fPIC: 
```
unit_tests: error while loading shared libraries: R_PPC_REL24 relocation at 0x010f521c for symbol '_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc' out of range
```

All other tests passed 👍 

[Log](https://paste.debian.net/1050585/)

Going to run the core_tests again and leave running to see what that reports.

## nioroso-x3 | 2018-11-06T19:30:37+00:00
I made 2 builds, one with D STACK_TRACE=OFF and a -D SANITIZE=ON build
They are both running the inv format test, extremely slowly.
[core_tests_valgrind.log.gz](https://github.com/monero-project/monero/files/2554732/core_tests_valgrind.log.gz)
[core_tests_asan.log.gz](https://github.com/monero-project/monero/files/2554733/core_tests_asan.log.gz)


## nioroso-x3 | 2018-11-06T19:38:06+00:00
> Ubuntu 16, PowerPC BE, 32 bit. PRs: (#4796, #4726, #4689, #4781, #4757, #4755).
> 
> **core_tests** took too long so I bailed on that.
> 
> **unit_tests** failed. Looks like something to do with -fPIC:
> 
> ```
> unit_tests: error while loading shared libraries: R_PPC_REL24 relocation at 0x010f521c for symbol '_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc' out of range
> ```
> All other tests passed 
> 
> [Log](https://paste.debian.net/1050585/)
> 
> Going to run the core_tests again and leave running to see what that reports.

Are you on a G5 too? I remember ubuntu 16.04 being quite buggy, thats why I switched to gentoo.

## jtgrassie | 2018-11-06T21:18:55+00:00
@nioroso-x3 No. Annoyingly I got rid of my G5 last year (it was gathering serious dust!). Thus my tests have been using qemu-system-ppc. It's been pretty stable with Ubuntu on it, although of course, very slow.

## hegjon | 2018-11-06T21:35:21+00:00
> @nioroso-x3 No. Annoyingly I got rid of my G5 last year (it was gathering serious dust!). Thus my tests have been using qemu-system-ppc. It's been pretty stable with Ubuntu on it, although of course, very slow.

Can you paste your public SSH key? I can try to get access to a PPC machine for you on the Fedora infrastructure.

## jtgrassie | 2018-11-11T17:14:32+00:00
Here is the failing core_tests log (Ubuntu 16 PowerPC BE 32bit).
[LastTest.log.tar.gz](https://github.com/monero-project/monero/files/2569594/LastTest.log.tar.gz)


## nioroso-x3 | 2018-11-14T21:36:46+00:00
core_tests also gets stuck in Fedora 25 ppc64.
That also uses gcc 6.4, I'll test the newest gcc just in case

## nioroso-x3 | 2018-11-16T13:48:55+00:00
Core tests passes completely when using llvm3.9 on fedora 25 and llvm (clang) 7.0 in gentoo, looks like gcc is buggy for ppc64 lol

First log is for gentoo in release, second for fedora in debug, looks like at the end there is a double free error, but everything passes for core_tests.


[core_tests_llvm7_release.log.gz](https://github.com/monero-project/monero/files/2589457/core_tests_llvm7_release.log.gz)

[core_tests_llvm39_debug.log.gz](https://github.com/monero-project/monero/files/2589477/core_tests_llvm39_debug.log.gz)

[make_f25_llvm39.log.gz](https://github.com/monero-project/monero/files/2589478/make_f25_llvm39.log.gz)




## moneromooo-monero | 2018-11-16T23:19:21+00:00
And now... does it sync the blockchain ? :)

## nioroso-x3 | 2018-11-17T20:33:57+00:00
Nope, its not syncing.
[bitmonero_gentoo.log.gz](https://github.com/monero-project/monero/files/2592223/bitmonero_gentoo.log.gz)


## moneromooo-monero | 2018-11-18T10:20:52+00:00
https://github.com/monero-project/monero/pull/4866

## nioroso-x3 | 2018-11-18T15:59:13+00:00
New bitmonero log after 4866
What does that patch fix?

[bitmonero.tar.gz](https://github.com/monero-project/monero/files/2592932/bitmonero.tar.gz)



## moneromooo-monero | 2018-11-18T18:10:35+00:00
It fixes values read/written from/to the network differently on little endian and big endian archs.

## moneromooo-monero | 2018-11-18T18:14:37+00:00
And I see at least another one that needs fixing.

## moneromooo-monero | 2018-11-18T18:49:51+00:00
I updated 4866,

## nioroso-x3 | 2018-11-20T00:07:20+00:00
New log
[bitmonero.tar.gz](https://github.com/monero-project/monero/files/2597516/bitmonero.tar.gz)


## moneromooo-monero | 2018-11-20T11:39:18+00:00
I found more places that need endian fixing. I'll post when I've fixed all I see.

## moneromooo-monero | 2018-11-20T12:26:25+00:00
4866 updated again.

## nioroso-x3 | 2018-11-21T21:37:16+00:00
New log, also unit_tests is getting stuck after mnemonics test, core_tests passes.

[bitmonero.log.gz](https://github.com/monero-project/monero/files/2605849/bitmonero.log.gz)
[unit_tests.log.gz](https://github.com/monero-project/monero/files/2605850/unit_tests.log.gz)



## moneromooo-monero | 2018-11-22T01:14:05+00:00
We can receive packet :)
Looks like the payload is also endian dependent though. Not fun.

## nioroso-x3 | 2019-05-09T20:04:52+00:00
Will this bug be fixed? I'm willing to provide ssh access to a machine for testing.

## moneromooo-monero | 2019-05-11T09:38:21+00:00
I can debug as a background task if I have access to such a machine.

## nioroso-x3 | 2019-05-11T18:03:11+00:00
Post a ssh public key, I can give you access to my G5 with gentoo. It has clang-8 and gcc-8.2.
You'll have access at monerodevs@nerv-la.ddns.net:223

## moneromooo-monero | 2019-05-12T14:44:21+00:00
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDEGd0x3Tkn/Ht1gKZlQY2T0oEpPEenGGPqzPMHMvHJ8S/PLbkVAFfNLDuBdshnm3r/4eMYspBO8/Pa55ICrURwhLk/aQ5vuNwvoReSib5omItheNM5ALWZpVfNTBZct1raryBIaDOUn9SvfLhZzhKojRSrFF4P5Nitn4aMjcGiKklIdFluQ0cIOmA4yY2DY8x6NPECVtPsJrwc89CMlPtlXNd8TgAWy8PvEQb7H9T6XaW4Mn1fGwT52+70q/Eyo4iNrGuLx74obvtAd3nCugTJykE1dXIiQQ3FtmtPqZCOQfaAVteKWvUPWYs4yc+b7LCqf06YvFhw+FfkS04F0gV user@host

## nioroso-x3 | 2019-05-12T18:23:32+00:00
You should have access now.

## nioroso-x3 | 2019-05-13T22:06:08+00:00
PPC64le (little endian) is failing some tests:
Test project /monero/build/Linux/master/debug
      Start  1: hash-target
 1/19 Test  #1: hash-target ......................   Passed    2.23 sec
      Start  2: core_tests
 2/19 Test  #2: core_tests .......................***Failed  12970.89 sec
      Start  3: cncrypto
 3/19 Test  #3: cncrypto .........................   Passed   19.66 sec
      Start  4: cnv4-jit
 4/19 Test  #4: cnv4-jit .........................   Passed  1210.97 sec
      Start  5: unit_tests
 5/19 Test  #5: unit_tests .......................***Failed  896.62 sec
      Start  6: difficulty
 6/19 Test  #6: difficulty .......................   Passed    0.09 sec
      Start  7: wide_difficulty
 7/19 Test  #7: wide_difficulty ..................***Failed    0.03 sec
      Start  8: block_weight
 8/19 Test  #8: block_weight .....................   Passed  111.12 sec
      Start  9: hash-fast
 9/19 Test  #9: hash-fast ........................   Passed    0.06 sec
      Start 10: hash-slow
10/19 Test #10: hash-slow ........................   Passed    0.62 sec
      Start 11: hash-slow-1
11/19 Test #11: hash-slow-1 ......................   Passed    0.69 sec
      Start 12: hash-slow-2
12/19 Test #12: hash-slow-2 ......................   Passed    1.71 sec
      Start 13: hash-slow-4
13/19 Test #13: hash-slow-4 ......................   Passed    5.99 sec
      Start 14: hash-tree
14/19 Test #14: hash-tree ........................   Passed    0.02 sec
      Start 15: hash-extra-blake
15/19 Test #15: hash-extra-blake .................   Passed    0.04 sec
      Start 16: hash-extra-groestl
16/19 Test #16: hash-extra-groestl ...............   Passed    0.05 sec
      Start 17: hash-extra-jh
17/19 Test #17: hash-extra-jh ....................   Passed    0.03 sec
      Start 18: hash-extra-skein
18/19 Test #18: hash-extra-skein .................   Passed    0.02 sec
      Start 19: hash-variant2-int-sqrt
19/19 Test #19: hash-variant2-int-sqrt ...........   Passed  473.87 sec

I couldnt find the .log for the wide-difficulty test, what is the filename?
[core_and_unit_tests.zip](https://github.com/monero-project/monero/files/3175008/core_and_unit_tests.zip)



## nioroso-x3 | 2019-05-13T23:41:20+00:00
hash-slow-2 and hash-slow-4 are failing in big endian ppc64
Test project /home/jribeiro/Development/monero-ori/build/Linux/master/debug                                                      
      Start  1: hash-target                                                                                                      
 1/19 Test  #1: hash-target ......................   Passed    2.34 sec                                                          
      Start  2: core_tests                                                                                                       
 2/19 Test  #2: core_tests .......................***Failed  686.95 sec                                                          
      Start  3: cncrypto                                                                                                         
 3/19 Test  #3: cncrypto .........................   Passed   41.94 sec                                                          
      Start  4: cnv4-jit                                                                                                         
 4/19 Test  #4: cnv4-jit .........................   Passed  2062.62 sec                                                         
      Start  5: unit_tests                                                                                                       
 5/19 Test  #5: unit_tests .......................***Failed  609.90 sec                                                          
      Start  6: difficulty                                                                                                       
 6/19 Test  #6: difficulty .......................   Passed    0.25 sec                                                          
      Start  7: wide_difficulty                                                                                                  
 7/19 Test  #7: wide_difficulty ..................   Passed   38.04 sec                                                          
      Start  8: block_weight                                                                                                     
 8/19 Test  #8: block_weight .....................   Passed  184.81 sec                                                          
      Start  9: hash-fast                                                                                                        
 9/19 Test  #9: hash-fast ........................   Passed    0.23 sec                                                          
      Start 10: hash-slow                                                                                                        
10/19 Test #10: hash-slow ........................   Passed    1.37 sec                                                          
      Start 11: hash-slow-1                                                                                                      
11/19 Test #11: hash-slow-1 ......................   Passed    1.80 sec                                                          
      Start 12: hash-slow-2                                                                                                      
12/19 Test #12: hash-slow-2 ......................***Failed    6.17 sec                                                          
      Start 13: hash-slow-4                                                                                                      
13/19 Test #13: hash-slow-4 ......................***Failed   10.52 sec                                                          
      Start 14: hash-tree                                                                                                        
14/19 Test #14: hash-tree ........................   Passed    0.20 sec                                                          
      Start 15: hash-extra-blake                                                                                                 
15/19 Test #15: hash-extra-blake .................   Passed    0.04 sec                                                          
      Start 16: hash-extra-groestl                                                                                               
16/19 Test #16: hash-extra-groestl ...............   Passed    0.05 sec                                                          
      Start 17: hash-extra-jh                                                                                                    
17/19 Test #17: hash-extra-jh ....................   Passed    0.04 sec                                                          
      Start 18: hash-extra-skein                                                                                                 
18/19 Test #18: hash-extra-skein .................   Passed    0.04 sec                                                          
      Start 19: hash-variant2-int-sqrt                                                                                           
19/19 Test #19: hash-variant2-int-sqrt ...........   Passed  1222.28 sec  

[core_and_unit_tests_be.zip](https://github.com/monero-project/monero/files/3175210/core_and_unit_tests_be.zip)


## moneromooo-monero | 2019-05-14T15:16:32+00:00
It should all be in LastTest.log


## moneromooo-monero | 2019-05-14T21:48:05+00:00
https://github.com/monero-project/monero/pull/5544

## moneromooo-monero | 2019-05-14T21:49:22+00:00
Thanks much for the G5 access. The patch above fixes most issues. There's still a failure in serialization unit tests, which I think is due to using boost code that's not endianness nice (not 100% sure). I think all the rest is fixed (but it takes massive amounts of time to build/test on that G5 so I've not run a full test run).

## moneromooo-monero | 2019-05-16T15:01:11+00:00
The serialization test failure is now also fixed, same PR.

## nioroso-x3 | 2019-06-28T02:49:43+00:00
Monero and wallet are fully syncing and working on your PR, tested on my G5 and on a newer power8 in be mode!
I built two Fedora 27 VMs on a newer POWER8 server I got my hands into, big endian and little endian, you may use them for testing and building as you wish, it should be way faster then the G5.

monerodevs@nerv-la.ddns.net:1234 <- BE Fedora 27, 6 threads 8gb ram
monerodevs@nerv-la.ddns.net:4321 <- LE Fedora 27, 6 threads 8gb ram


## moneromooo-monero | 2019-07-05T18:55:18+00:00
Thanks, I'll try to go build/test from time to time and fix any problems.

## selsta | 2022-04-08T14:48:35+00:00
Seems resolved.

# Action History
- Created by: hegjon | 2018-05-17T21:50:04+00:00
- Closed at: 2022-04-08T14:48:35+00:00
