---
title: Build problem at `master`
source_url: https://github.com/monero-project/monero/issues/4010
author: rodentrabies
assignees: []
labels:
- duplicate
created_at: '2018-06-17T13:05:43+00:00'
updated_at: '2018-06-17T17:56:56+00:00'
type: issue
status: closed
closed_at: '2018-06-17T17:56:56+00:00'
---

# Original Description
Trying to build `master` branch, I get an error from memaccess warning:
```text
[ 21%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
/home/whythat/Code/foss/monero/src/cryptonote_basic/account.cpp: In member function ‘void cryptonote::account_base::create_from_viewkey(const cryptonote::account_public_address&, const secret_key&)’:
/home/whythat/Code/foss/monero/src/cryptonote_basic/account.cpp:160:34: error: ‘void* memset(void*, int, size_t)’ clearing an object of non-trivial type ‘using secret_key = struct tools::scrubbed<crypto::ec_scalar>’ {aka ‘struct tools::scrubbed<crypto::ec_scalar>’}; use assignment or value-initialization instead [-Werror=class-memaccess]
     memset(&fake, 0, sizeof(fake));
                                  ^
In file included from /home/whythat/Code/foss/monero/src/crypto/chacha.h:42,
                 from /home/whythat/Code/foss/monero/src/serialization/crypto.h:37,
                 from /home/whythat/Code/foss/monero/src/cryptonote_basic/cryptonote_basic.h:44,
                 from /home/whythat/Code/foss/monero/src/cryptonote_basic/account.h:33,
                 from /home/whythat/Code/foss/monero/src/cryptonote_basic/account.cpp:34:
/home/whythat/Code/foss/monero/contrib/epee/include/memwipe.h:53:10: note: ‘using secret_key = struct tools::scrubbed<crypto::ec_scalar>’ {aka ‘struct tools::scrubbed<crypto::ec_scalar>’} declared here
   struct scrubbed : public T {
          ^~~~~~~~
```

# Discussion History
## moneromooo-monero | 2018-06-17T17:53:30+00:00
Fixed somewhere in the PRs. https://github.com/monero-project/monero/pull/3851/files

+duplicate


# Action History
- Created by: rodentrabies | 2018-06-17T13:05:43+00:00
- Closed at: 2018-06-17T17:56:56+00:00
