---
title: 'Cannot compile 0.14 on ARMv7: undefined reference to CryptonightR_instruction'
source_url: https://github.com/monero-project/monero/issues/5200
author: gavriilos
assignees: []
labels: []
created_at: '2019-02-26T16:01:54+00:00'
updated_at: '2019-03-05T14:17:53+00:00'
type: issue
status: closed
closed_at: '2019-03-05T14:17:53+00:00'
---

# Original Description
I am trying to build the [`v0.14.0.0` tag](https://github.com/monero-project/monero/releases/tag/v0.14.0.0) with `-DBUILD_SHARED_LIBS=1` on an ARMv7. At first, compilation failed due to #5178 which I could fix after applying #5184. Now compilation is failing at a later step, when linking the executables:

```
[ 84%] Linking CXX executable ../../bin/monero-wallet-rpc
../crypto/libcncrypto.so: undefined reference to `CryptonightR_instruction87'
../crypto/libcncrypto.so: undefined reference to `CryptonightR_instruction_mov47'
../crypto/libcncrypto.so: undefined reference to `CryptonightR_instruction_mov84'
../crypto/libcncrypto.so: undefined reference to `CryptonightR_instruction237'
../crypto/libcncrypto.so: undefined reference to `CryptonightR_instruction151'
../crypto/libcncrypto.so: undefined reference to `CryptonightR_instruction196'
[...]
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:133: recipe for target 'bin/monero-wallet-rpc' failed
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2254: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
```

# Discussion History
## moneromooo-monero | 2019-02-26T16:59:56+00:00
There is a new patch in 5184 now. Does it fix that new error ?

## gavriilos | 2019-02-26T17:57:21+00:00
Thanks for looking into it. It does fix that error but I get a new one:

```
[ 45%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/CryptonightR_JIT.c.o
../monero/src/crypto/CryptonightR_JIT.c: In function ‘v4_generate_JIT_code’:
../monero/src/crypto/CryptonightR_JIT.c:83:42: error: ‘instructions_mov’ undeclared (first use in this function)
     const uint8_t* p1 = (const uint8_t*) instructions_mov[c];
                                          ^~~~~~~~~~~~~~~~
../monero/src/crypto/CryptonightR_JIT.c:83:42: note: each undeclared identifier is reported only once for each function it appears in
../monero/src/crypto/CryptonightR_JIT.c:93:40: error: ‘instructions’ undeclared (first use in this function)
   const uint8_t* p1 = (const uint8_t*) instructions[c];
                                        ^~~~~~~~~~~~
src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:494: recipe for target 'src/crypto/CMakeFiles/obj_cncrypto.dir/CryptonightR_JIT.c.o' failed
make[2]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/CryptonightR_JIT.c.o] Error 1
CMakeFiles/Makefile2:753: recipe for target 'src/crypto/CMakeFiles/obj_cncrypto.dir/all' failed
make[1]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
```

## moneromooo-monero | 2019-02-26T18:32:05+00:00
And now ?

## gavriilos | 2019-02-26T23:46:47+00:00
(Sorry for the delay, it takes a long time to compile this on an ARMv7.)
That seems to have fixed it. It compiled successfully and I am now running `monerod`. It is now migrating the blockchain DB version. I'll let you know if something breaks latter on.

## gavriilos | 2019-02-27T15:43:26+00:00
All seems fine. The DB migration was successful, the node got up to speed with the network, and is now correctly handling `monero-wallet-cli` connections.
You can/should merge this into `v0.14`.

## moneromooo-monero | 2019-02-27T18:29:07+00:00
Thanks. It will be.

## moneromooo-monero | 2019-03-05T13:40:41+00:00
+resolved

# Action History
- Created by: gavriilos | 2019-02-26T16:01:54+00:00
- Closed at: 2019-03-05T14:17:53+00:00
