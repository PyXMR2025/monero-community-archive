---
title: Wallet with subaddresses crashes on sweep_all
source_url: https://github.com/monero-project/monero/issues/2781
author: emesik
assignees: []
labels: []
created_at: '2017-11-09T02:50:21+00:00'
updated_at: '2017-11-09T05:00:43+00:00'
type: issue
status: closed
closed_at: '2017-11-09T05:00:42+00:00'
---

# Original Description
```
Monero 'Helium Hydra' (v0.11.0.0-c3c31fa5)
Logging to w2.log
Wallet password: 
Opened wallet: 9wFuzNoQDck1pnS9ZhG47kDdLD1BUszSbWpGfWcSRy9m6Npq9NoHWd141KvGag8hu2gajEwzRXJ4iJwmxruv9ofc2CwnYCE
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 1                                
        Account               Balance      Unlocked balance                 Label
       0 9wFuzN       24.923448000000       24.923448000000       Primary account
       1 BZwH58       56.832907280000       33.981591480000      Untitled account
----------------------------------------------------------------------------------
          Total       81.756355280000       58.905039480000
Currently selected account: [0] Primary account
Balance: 24.923448000000, unlocked balance: 24.923448000000
Background refresh thread started
[wallet 9wFuzN]: sweep_all
Wallet password: 
./runwallet.sh: line 6:  8585 Segmentation fault      (core dumped) ~/devel/monero/bin/monero-wallet-cli --testnet --wallet-file $1 --log-level 2 --log-file $1.log

```

The code is from current `master.` Checked on 2 wallets, 100% reproducible. The log file doesn't contain any info on the error.

Any tips on running `gdb` on it or getting details in some other way?

# Discussion History
## stoffu | 2017-11-09T03:21:39+00:00
This is due to a bug in the `sweep_all` command which is fixed in #2750. 

## emesik | 2017-11-09T05:00:42+00:00
OK, closing then.

# Action History
- Created by: emesik | 2017-11-09T02:50:21+00:00
- Closed at: 2017-11-09T05:00:42+00:00
