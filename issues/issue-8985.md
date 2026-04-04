---
title: '[Manjaro/aarch64] monero-wallet-cli can no longer open stagenet wallet after
  system update'
source_url: https://github.com/monero-project/monero/issues/8985
author: phytohydra
assignees: []
labels:
- pending review
- arm
created_at: '2023-09-08T00:51:23+00:00'
updated_at: '2023-12-07T20:16:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This happened some time ago.  According to the filesystem, I last modified stagenet.wallet on Oct 17  2021, so I think that's the last time I successfully opened it.

I had two wallets named mainnet.wallet and stagenet.wallet which had the same password.  Prior to a Manjaro system update, they would both open.  Afterwards, mainnet.wallet could still be opened, while stagenet.wallet gave "Error: failed to load wallet: invalid password".

This happens on both Rockpro64 and Pinebook Pro hardware running Manjaro.
The oldest Monero version I have to test with is monero-aarch64-linux-gnu-v0.17.2.3 (Oxygen Orion).  The filesystem shows its folder was created on Oct 16  2021.  I think I downloaded that and was able to open the stagenet wallet the next day.  That version of monero-wallet-cli, on the current Manjaro, is not able to open the stagenet wallet.

I tried creating a new stagenet wallet with the same password with the current monero-wallet-cli + the current OS version, and that one can be opened.

I don't have a copy of the seed phrase for the stagenet wallet, so I can't try recreating it.

I found a file of notes I made on 2022.02.03, when I first noticed the issue.
Last opened successfully 2022.01.25 - that's a copy on the Rockpro64, which was mining stagenet for a while.

monero-wallet-cli invoked with --log-level=1 said,
```
2022-02-04 00:03:02.772     ffffb25626f0        ERROR   console_handler contrib/epee/include/storages/portable_storage.h:175    portable_storage: wrong binary format - signature mismatch
2022-02-04 00:03:02.773     ffffb25626f0        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4393     !r. THROW EXCEPTION: error::invalid_password
2022-02-04 00:03:02.774     ffffb25626f0        WARNING net.http        src/wallet/wallet_errors.h:896  /home/ubuntu/build/monero/src/wallet/wallet2.cpp:4393:N5tools5error16invalid_passwordE: invalid password
2022-02-04 00:03:02.774     ffffb25626f0        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: failed to load wallet: invalid password
2022-02-04 00:03:02.910     ffffb25626f0        ERROR   console_handler contrib/epee/include/storages/portable_storage.h:175    portable_storage: wrong binary format - signature mismatch
2022-02-04 00:03:02.912     ffffb25626f0        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:4636  failed to open account
2022-02-04 00:03:02.912     ffffb25626f0        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:10517 Failed to initialize wallet
```

# Discussion History
# Action History
- Created by: phytohydra | 2023-09-08T00:51:23+00:00
