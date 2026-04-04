---
title: Cannot compile monerod on MacOS 10.14.1
source_url: https://github.com/monero-project/monero/issues/5234
author: scrammy
assignees: []
labels: []
created_at: '2019-03-05T18:38:43+00:00'
updated_at: '2019-03-31T19:09:14+00:00'
type: issue
status: closed
closed_at: '2019-03-31T19:09:14+00:00'
---

# Original Description
Installed all required dependancies (not the optional ones) and followed instructions such as they were documented and get 71% and always fails with a linker error (marked in bold):

[ 71%] Linking CXX executable cnv4-jit-tests
clang: warning: argument unused during compilation: '-pie' [-Wunused-command-line-argument]
**ld: library not found for -lcrypto**
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [tests/crypto/cnv4-jit-tests] Error 1
make[2]: *** [tests/crypto/CMakeFiles/cnv4-jit-tests.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release-all] Error 2

I checked and libsodium is installed and the most current version - is the crypto library something else?

Also tried to use the pre-compiled versions available and simply get an "illegal instruction: 4" message back (See issue #5230).  The previous version (v13) ran fine in this machine (Mac Pro 5,1  6-Core 3.33 GHz)

# Discussion History
## moneromooo-monero | 2019-03-05T22:14:22+00:00
It is openssl.

## scrammy | 2019-03-06T00:09:09+00:00
openssl is installed (version 1.0.2q) via homebrew

## moneromooo-monero | 2019-03-06T00:45:13+00:00
Not sure what's going on here. Previous programs linked, and that one test does not do anything with openssl...

## moneromooo-monero | 2019-03-06T19:34:46+00:00
Fixed in https://github.com/monero-project/monero/pull/5241

## moneromooo-monero | 2019-03-31T19:01:27+00:00
+resolved

# Action History
- Created by: scrammy | 2019-03-05T18:38:43+00:00
- Closed at: 2019-03-31T19:09:14+00:00
