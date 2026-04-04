---
title: Compilation failure of v0.17.3.0 with OpenBSD 7 on RiscV-64
source_url: https://github.com/monero-project/monero/issues/8234
author: antanst
assignees: []
labels: []
created_at: '2022-04-02T06:34:06+00:00'
updated_at: '2022-04-06T02:23:39+00:00'
type: issue
status: closed
closed_at: '2022-04-06T02:23:39+00:00'
---

# Original Description
System is an Unmatched HiFive RISCV-64 running OpenBSD 7.1-beta.

```shell
$ uname -a
OpenBSD hi5.lan 7.1 GENERIC.MP#66 riscv64
$ clang -v
OpenBSD clang version 13.0.0
Target: riscv64-unknown-openbsd7.1
```

Monero is built according to README instructions and fails with this error:

```
$ env DEVELOPER_LOCAL_TOOLS=1 BOOST_ROOT=/usr/local gmake release-static 
mkdir -p build/"OpenBSD/_HEAD_detached_at_v0.17.3.0_"/release
cd build/"OpenBSD/_HEAD_detached_at_v0.17.3.0_"/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../../../.. && gmake
....
<snip>
...
gmake[3]: Leaving directory '/home/user/work/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.0_/release'
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.o
gmake[3]: Entering directory '/home/user/work/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.0_/release'
[ 21%] Built target genversion                                                                                                                                                                 
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[ 21%] Built target qrcodegen
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o        
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parseutil.c.o
cc: error: invalid arch name 'x86-64', string must begin with rv32{i,e,g} or rv64{i,g}
gmake[3]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:76: src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o] Error 1
gmake[3]: *** Waiting for unfinished jobs....
cc: error: invalid arch name 'x86-64', string must begin with rv32{i,e,g} or rv64{i,g}
gmake[3]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:90: src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o] Error 1
gmake[3]: Leaving directory '/home/user/work/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.0_/release'
gmake[2]: *** [CMakeFiles/Makefile2:1695: src/crypto/CMakeFiles/obj_cncrypto.dir/all] Error 2
gmake[2]: *** Waiting for unfinished jobs....
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/rrdef.c.o                                                                                                               
[ 21%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/str2wire.c.o
/home/user/work/monero/external/unbound/sldns/keyraw.c:237:5: error: incomplete definition of type 'struct dsa_st'
        dsa->p = P;                                                                            
        ~~~^                                                                                                                                                                                   
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;                                                                                                                                                                     
               ^            
/home/user/work/monero/external/unbound/sldns/keyraw.c:238:5: error: incomplete definition of type 'struct dsa_st'
        dsa->q = Q;
        ~~~^
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;
               ^
/home/user/work/monero/external/unbound/sldns/keyraw.c:239:5: error: incomplete definition of type 'struct dsa_st'
        dsa->g = G;
        ~~~^
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;
               ^
/home/user/work/monero/external/unbound/sldns/keyraw.c:240:5: error: incomplete definition of type 'struct dsa_st'
        dsa->pub_key = Y;
        ~~~^
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;
               ^
/home/user/work/monero/external/unbound/sldns/keyraw.c:315:5: error: incomplete definition of type 'struct rsa_st'
        rsa->n = modulus;
        ~~~^
/usr/include/openssl/ossl_typ.h:122:16: note: forward declaration of 'struct rsa_st'
typedef struct rsa_st RSA;
               ^
/home/user/work/monero/external/unbound/sldns/keyraw.c:316:5: error: incomplete definition of type 'struct rsa_st'
        rsa->e = exponent;
        ~~~^
/usr/include/openssl/ossl_typ.h:122:16: note: forward declaration of 'struct rsa_st'
typedef struct rsa_st RSA;
               ^
6 errors generated.
gmake[3]: *** [external/unbound/CMakeFiles/unbound.dir/build.make:958: external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.o] Error 1
gmake[3]: *** Waiting for unfinished jobs....
gmake[3]: Leaving directory '/home/user/work/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.0_/release'
gmake[2]: *** [CMakeFiles/Makefile2:1245: external/unbound/CMakeFiles/unbound.dir/all] Error 2
gmake[2]: Leaving directory '/home/user/work/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.0_/release'
gmake[1]: *** [Makefile:146: all] Error 2
gmake[1]: Leaving directory '/home/user/work/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.0_/release'
gmake: *** [Makefile:107: release-static] Error 2
```

# Discussion History
## selsta | 2022-04-02T06:36:46+00:00
Do you have unbound installed?

## antanst | 2022-04-02T06:50:32+00:00
OpenBSD 7.1 comes with unbound 1.15.0 in system; there is no separate package of unbound installed.

## selsta | 2022-04-02T06:51:53+00:00
Can you try master branch?

## antanst | 2022-04-02T06:58:05+00:00
commit 70ceab6c1

```
<snip>
gmake[3]: Entering directory '/home/user/work/monero/build/OpenBSD/master/release'
[ 27%] Building CXX object contrib/epee/src/CMakeFiles/obj_epee.dir/byte_slice.cpp.o
c++: error: invalid arch name 'x86-64', string must begin with rv32{i,e,g} or rv64{i,g}
gmake[3]: *** [contrib/epee/src/CMakeFiles/obj_epee.dir/build.make:76: contrib/epee/src/CMakeFiles/obj_epee.dir/byte_slice.cpp.o] Error 1
gmake[3]: Leaving directory '/home/user/work/monero/build/OpenBSD/master/release'
gmake[2]: *** [CMakeFiles/Makefile2:1465: contrib/epee/src/CMakeFiles/obj_epee.dir/all] Error 2
gmake[2]: Leaving directory '/home/user/work/monero/build/OpenBSD/master/release'
gmake[1]: *** [Makefile:146: all] Error 2
gmake[1]: Leaving directory '/home/user/work/monero/build/OpenBSD/master/release'
gmake: *** [Makefile:107: release-static] Error 2
```

## selsta | 2022-04-02T07:02:48+00:00
What if you do `gmake release` instead of `gmake release-static`

`release-static` has x86-64 hardcoded: https://github.com/monero-project/monero/blob/master/Makefile#L107

Alternatively you can also change the arch in the makefile I linked. I'd try both.

## antanst | 2022-04-02T07:59:23+00:00
```
In file included from /home/user/work/monero/external/randomx/src/bytecode_machine.hpp:32:
/home/user/work/monero/external/randomx/src/intrin_portable.h:674:70: error: expected ')'    
FORCE_INLINE rx_vec_i128 rx_xor_vec_i128(rx_vec_i128 _A, rx_vec_i128 _B) {
                                                                     ^
/usr/include/ctype.h:52:12: note: expanded from macro '_B'                                                                                                                                     
#define _B      0x80
                ^
/home/user/work/monero/external/randomx/src/intrin_portable.h:674:41: note: to match this '('
FORCE_INLINE rx_vec_i128 rx_xor_vec_i128(rx_vec_i128 _A, rx_vec_i128 _B) {                                                                                                                     
                                        ^                                                      
/home/user/work/monero/external/randomx/src/intrin_portable.h:676:27: error: member reference base type 'int' is not a structure or union
        c.u32[0] = _A.u32[0] ^ _B.u32[0];                                                      
                               ~~^~~~    
/home/user/work/monero/external/randomx/src/intrin_portable.h:677:27: error: member reference base type 'int' is not a structure or union
        c.u32[1] = _A.u32[1] ^ _B.u32[1];
                               ~~^~~~
/home/user/work/monero/external/randomx/src/intrin_portable.h:677:27: error: member reference base type 'int' is not a structure or union
        c.u32[1] = _A.u32[1] ^ _B.u32[1];
                               ~~^~~~
/home/user/work/monero/external/randomx/src/intrin_portable.h:678:27: error: member reference base type 'int' is not a structure or union
        c.u32[2] = _A.u32[2] ^ _B.u32[2];
                               ~~^~~~
/home/user/work/monero/external/randomx/src/intrin_portable.h:679:27: error: member reference base type 'int' is not a structure or union
        c.u32[3] = _A.u32[3] ^ _B.u32[3];
                               ~~^~~~
/home/user/work/monero/external/randomx/src/intrin_portable.h:683:61: error: expected ')'
FORCE_INLINE rx_vec_i128 rx_load_vec_i128(rx_vec_i128 const*_P) {
                                                            ^
/usr/include/ctype.h:49:12: note: expanded from macro '_P'
#define _P      0x10
                ^
/home/user/work/monero/external/randomx/src/intrin_portable.h:683:42: note: to match this '('
FORCE_INLINE rx_vec_i128 rx_load_vec_i128(rx_vec_i128 const*_P) {
                                         ^
/home/user/work/monero/external/randomx/src/intrin_portable.h:685:9: error: indirection requires pointer operand ('int' invalid)
        return *_P;
               ^~~
/home/user/work/monero/external/randomx/src/intrin_portable.h:697:50: error: expected ')'
FORCE_INLINE void rx_store_vec_i128(rx_vec_i128 *_P, rx_vec_i128 _B) {
                                                 ^
/usr/include/ctype.h:49:12: note: expanded from macro '_P'
#define _P      0x10
                ^
/home/user/work/monero/external/randomx/src/intrin_portable.h:697:36: note: to match this '('
FORCE_INLINE void rx_store_vec_i128(rx_vec_i128 *_P, rx_vec_i128 _B) {
                                   ^
/home/user/work/monero/external/randomx/src/intrin_portable.h:699:2: error: indirection requires pointer operand ('int' invalid)
        *_P = _B;
        ^~~
9 errors generated.
gmake[3]: *** [external/randomx/CMakeFiles/randomx.dir/build.make:132: external/randomx/CMakeFiles/randomx.dir/src/bytecode_machine.cpp.o] Error 1
gmake[3]: Leaving directory '/home/user/work/monero/build/OpenBSD/master/release'
gmake[2]: *** [CMakeFiles/Makefile2:1391: external/randomx/CMakeFiles/randomx.dir/all] Error 2
gmake[2]: Leaving directory '/home/user/work/monero/build/OpenBSD/master/release'
gmake[1]: *** [Makefile:146: all] Error 2
```

## antanst | 2022-04-02T08:04:05+00:00
The above is related to this which is fixed in a newer version of RandomX:

https://github.com/tevador/RandomX/issues/228

## selsta | 2022-04-06T02:23:39+00:00
Closing this here as it's not a direct monero bug. Will make sure to get it fixed on RandomX side.

# Action History
- Created by: antanst | 2022-04-02T06:34:06+00:00
- Closed at: 2022-04-06T02:23:39+00:00
