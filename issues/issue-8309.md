---
title: v0.17.3.2 does not compile on OpenBSD 7.1
source_url: https://github.com/monero-project/monero/issues/8309
author: random-xmr-user
assignees: []
labels: []
created_at: '2022-05-02T22:49:55+00:00'
updated_at: '2022-05-07T20:44:38+00:00'
type: issue
status: closed
closed_at: '2022-05-07T20:44:38+00:00'
---

# Original Description
I have been running monerod on OpenBSD for over a year now. The new release (v.017.3.2) does not compile on Openbsd 7.1. 
Any help would be appreciated.

This is as far as I got:

[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/dns64/dns64.c.o
/home/stef/monero/external/unbound/dns64/dns64.c:504:7: warning: cast to smaller integer type 'enum dns64_qstate' from 'void *' [-Wvoid-pointer-to-enum-cast]
        if ( (enum dns64_qstate)qstate->minfo[id] == DNS64_INTERNAL_QUERY
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1 warning generated.
[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/testcode/checklocks.c.o
[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.o
/home/stef/monero/external/unbound/sldns/keyraw.c:237:5: error: incomplete definition of type 'struct dsa_st'
        dsa->p = P;
        ~~~^
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;
               ^
/home/stef/monero/external/unbound/sldns/keyraw.c:238:5: error: incomplete definition of type 'struct dsa_st'
        dsa->q = Q;
        ~~~^
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;
               ^
/home/stef/monero/external/unbound/sldns/keyraw.c:239:5: error: incomplete definition of type 'struct dsa_st'
        dsa->g = G;
        ~~~^
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;
               ^
/home/stef/monero/external/unbound/sldns/keyraw.c:240:5: error: incomplete definition of type 'struct dsa_st'
        dsa->pub_key = Y;
        ~~~^
/usr/include/openssl/ossl_typ.h:119:16: note: forward declaration of 'struct dsa_st'
typedef struct dsa_st DSA;
               ^
/home/stef/monero/external/unbound/sldns/keyraw.c:315:5: error: incomplete definition of type 'struct rsa_st'
        rsa->n = modulus;
        ~~~^
/usr/include/openssl/ossl_typ.h:122:16: note: forward declaration of 'struct rsa_st'
typedef struct rsa_st RSA;
               ^
/home/stef/monero/external/unbound/sldns/keyraw.c:316:5: error: incomplete definition of type 'struct rsa_st'
        rsa->e = exponent;
        ~~~^
/usr/include/openssl/ossl_typ.h:122:16: note: forward declaration of 'struct rsa_st'
typedef struct rsa_st RSA;
               ^
6 errors generated.
gmake[3]: *** [external/unbound/CMakeFiles/unbound.dir/build.make:958: external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.o] Error 1
gmake[3]: Leaving directory '/home/stef/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.2_/release'
gmake[2]: *** [CMakeFiles/Makefile2:1274: external/unbound/CMakeFiles/unbound.dir/all] Error 2
gmake[2]: Leaving directory '/home/stef/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.2_/release'
gmake[1]: *** [Makefile:146: all] Error 2
gmake[1]: Leaving directory '/home/stef/monero/build/OpenBSD/_HEAD_detached_at_v0.17.3.2_/release'
gmake: *** [Makefile:107: release-static] Error 2


# Discussion History
## selsta | 2022-05-03T01:03:19+00:00
Did you build master previously?

## random-xmr-user | 2022-05-03T03:08:07+00:00
Yes, I have compiled v0.17.3.0 without any issues.

## selsta | 2022-05-03T05:13:03+00:00
Did you build `master` branch or `v0.17.3.0` tag? That's two different things.

## random-xmr-user | 2022-05-03T19:48:44+00:00
I downloaded the archived source from the website last night and attempted to build and get the same errors as above.

## selsta | 2022-05-04T09:48:59+00:00
Can you do

```
git clone --recursive -b v0.17.3.0 https://github.com/monero-project/monero
```

and double check if `v0.17.3.0` builds correctly?

## random-xmr-user | 2022-05-04T15:50:03+00:00
I tried it again this morning. v0.17.3.0 does not build correctly and fails at 34% with the same errors as above. 

I had previously compiled it on OpenBSD 7.0 without issues. Now, after upgrading to OpenBSD7.1 it does not compile.

## jeffro256 | 2022-05-06T06:27:32+00:00
This post might be related: <https://stackoverflow.com/questions/60418967/openssl-1-1-1d-invalid-use-of-incomplete-type-struct-dsa-st>.

Perhaps OpenBSD updated their version of OpenSSL to remove the deprecated API with version 7.1, while our in-tree version of `libunbound` still relies on it. If @random-xmr-user can compile against his system's `unbound` library, instead of in-tree, perhaps it will compile.

## jeffro256 | 2022-05-06T06:31:03+00:00
@random-xmr-user Can you see if the following will compile?:

```bash
git clone --recursive https://github.com/monero-project/monero monero_newest
cd monero_newest
make
```

I ask you to compile this latest version as a test because `libunbound` was factored out of the tree somewhere along the way in the `master` branch.

## random-xmr-user | 2022-05-06T21:44:49+00:00
@jeffro256 You are right, OpenBSD has upgraded LibreSSL to version 3.5.2, it was released with OpenBSD7.1

I was able to compile monero_newest without issues. However, the binary produced is v0.17.0.0-67e5ca9ad.

## selsta | 2022-05-07T10:15:31+00:00
> However, the binary produced is v0.17.0.0-67e5ca9ad.

That's normal for the `master` branch. It doesn't use the same version system, just the major one and the git commit hash.

# Action History
- Created by: random-xmr-user | 2022-05-02T22:49:55+00:00
- Closed at: 2022-05-07T20:44:38+00:00
