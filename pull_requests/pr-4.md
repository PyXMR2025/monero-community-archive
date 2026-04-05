---
title: 'wallet2_basic: robust compat lib for loading/storing legacy wallets'
source_url: https://github.com/seraphis-migration/monero/pull/4
author: jeffro256
assignees: []
labels: []
created_at: '2023-08-20T04:09:57+00:00'
updated_at: '2024-05-11T18:47:36+00:00'
type: pull_request
status: merged
closed_at: '2023-10-26T17:40:57+00:00'
merged_at: '2023-10-26T17:40:57+00:00'
---

# Original Description
This library has no dependency on wallet2.h and gives us a way forward to move away from `wallet2` in the (not-so-distant) future, while still supporting conversions of old wallet files. This lib is also useful if you have an application where you want to extract information directly from the wallet file with or without having to setup accounts and devices. This is now possible because I have split the wallet keys loading into two steps: `load_from_memory` and `setup_account_and_devices`. When one is loading a wallet keys file, the user of the API can choose whether or not to contact external devices during this process with use of the flag `allow_external_devices_setup`.

Reorganized for `seraphis_migration`.

# Discussion History
## DangerousFreedom1984 | 2023-09-09T08:45:29+00:00
I believe it will never reach this point as it will succeed or an error will be raised first but my compiler is not happy that there is not a 'return cache' here. Should it be there or should I change some config?
I'm getting that:
src/wallet/wallet2_basic/wallet2_storage.cpp:259:1: error: control reaches end of non-void function [-Werror=return-type]
  259 | }
      | ^
cc1plus: some warnings being treated as errors
make[3]: *** [src/wallet/wallet2_basic/CMakeFiles/obj_wallet2_basic.dir/build.make:90: src/wallet/wallet2_basic/CMakeFiles/obj_wallet2_basic.dir/wallet2_storage.cpp.o] Error 1
make[3]: Leaving directory 'build/Linux/initial_tx_history_final/debug'
make[2]: *** [CMakeFiles/Makefile2:4269: src/wallet/wallet2_basic/CMakeFiles/obj_wallet2_basic.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[3]: Leaving directory 'build/Linux/initial_tx_history_final/debug'

## jeffro256 | 2023-09-09T20:34:01+00:00
Hmm... that seems to be a bug in the compiler. The `[[noreturn]]` annotations on `throw_wallet_ex()` should indicate to the compiler that the control flow ends there. However, I could modify it so the compiler can't mess it up.  

## rbrunner7 | 2023-09-29T19:33:41+00:00
I think now I found a small thing that is not implemented. As reported [here](https://github.com/seraphis-migration/monero/pull/4#issuecomment-1731384481) it looked as if loading a .keys file in ASCII format is not yet supported. Now, looking at your code, I think I confirmed that, because support for `ExportFormat::Ascii` is nowhere to be found.

## jeffro256 | 2023-10-22T21:57:40+00:00
Okay, the wallet now supports loading the keys using PEM ascii format, automatically detecting it. 

## jeffro256 | 2023-10-22T21:57:52+00:00
(and storing it) 

# Action History
- Created by: jeffro256 | 2023-08-20T04:09:57+00:00
- Merged at: 2023-10-26T17:40:57+00:00
