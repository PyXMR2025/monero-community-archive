---
title: Cann't build bitmonero [rev 26292c]
source_url: https://github.com/monero-project/monero/issues/18
author: o01eg
assignees: []
labels: []
created_at: '2014-05-28T11:45:12+00:00'
updated_at: '2014-08-02T09:22:53+00:00'
type: issue
status: closed
closed_at: '2014-08-02T09:22:53+00:00'
---

# Original Description
When I build bitmonero I get error:

```
[ 51%] Building CXX object src/CMakeFiles/wallet.dir/wallet/wallet2.cpp.o
cd /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999_build/src && /usr/bin/x86_64-pc-linux-gnu-g++  -DSTATICLIB  -DNDEBUG -O2 -march=native -pipe -msse -msse2 -msse3 -mssse3 -mmmx -mcx16 -msahf -momit-leaf-frame-pointer  -std=c++11 -D_GNU_SOURCE  -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Werror -Wno-error=extra -Wno-error=deprecated-declarations -Wno-error=sign-compare -Wno-error=strict-aliasing -Wno-error=type-limits -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-reorder -Wno-missing-field-initializers -march=native -maes -I/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src -I/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/contrib/epee/include -I/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/external -I/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999_build/version    -o CMakeFiles/wallet.dir/wallet/wallet2.cpp.o -c /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.cpp
In file included from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.h:24:0,
                 from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.cpp:13:
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:123:12: error: looser throw specifier for ‘virtual tools::error::unexpected_txin_type::~unexpected_txin_type()’
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:115:12: error:   overriding ‘virtual tools::error::wallet_internal_error::~wallet_internal_error() noexcept (true)’
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:201:12: error: looser throw specifier for ‘virtual tools::error::acc_outs_lookup_error::~acc_outs_lookup_error()’
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:192:12: error:   overriding ‘virtual tools::error::refresh_error::~refresh_error() noexcept (true)’
In file included from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.h:24:0,
                 from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.cpp:13:
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:395:12: error: looser throw specifier for ‘virtual tools::error::tx_rejected::~tx_rejected()’
In file included from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.h:24:0,
                 from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.cpp:13:
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:266:12: error:   overriding ‘virtual tools::error::transfer_error::~transfer_error() noexcept (true)’
In file included from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.h:24:0,
                 from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.cpp:13:
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:451:12: error: looser throw specifier for ‘virtual tools::error::tx_too_big::~tx_too_big()’
In file included from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.h:24:0,
                 from /mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet2.cpp:13:
/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999/src/wallet/wallet_errors.h:266:12: error:   overriding ‘virtual tools::error::transfer_error::~transfer_error() noexcept (true)’
make[2]: *** [src/CMakeFiles/wallet.dir/wallet/wallet2.cpp.o] Error 1
make[2]: Leaving directory `/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999_build'
make[1]: *** [src/CMakeFiles/wallet.dir/all] Error 2
make[1]: Leaving directory `/mnt/anythings/tmp/portage/net-p2p/monero-9999/work/monero-9999_build'
make: *** [all] Error 2
```

gcc-4.7.3
boost-1.53


# Discussion History
## canselcik | 2014-06-17T01:26:58+00:00
I am experiencing the same problem when trying to install `bitmonerod` on OSX Mavericks. I have `libboost 1.55` installed, and brew fails to build `bitmonero` and gives out this error.


## fluffypony | 2014-08-02T09:22:53+00:00
Monero requires gcc 4.8, which we have now noted on the new README :)


# Action History
- Created by: o01eg | 2014-05-28T11:45:12+00:00
- Closed at: 2014-08-02T09:22:53+00:00
