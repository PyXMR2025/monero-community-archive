---
title: '[Manjaro/aarch64] monero-wallet-cli plus Trezor Model T: Can''t send transactions
  to itself'
source_url: https://github.com/monero-project/monero/issues/8984
author: phytohydra
assignees: []
labels:
- question
- arm
created_at: '2023-09-08T00:16:32+00:00'
updated_at: '2023-12-07T20:25:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm using monero-wallet-cli on a Pinebook Pro running the current release of Manjaro linux.

When using a wallet in conjunction with a Trezor, I am able to receive transfers, and send to my non-Trezor wallet.  However, the Trezor-managed wallet cannot send to itself.
```
transfer <address> 0.1

Transaction 1/1:                                                                                                                                                                
Spending from address index 1
Sending 0.100000000000.  The transaction fee is 0.000044380000
                                            
Is this okay?  (Y/Yes/N/No): y                                                                                                                                                  
Please confirm the transaction on the device                                                                                                                                    
Error: unexpected error: Call method failed
```

Whether using the main address or a subaddress, if the address is in the trezor-managed wallet, it always fails like that.  sweep_all does as well.  Usually it doesn't get to the point of showing anything on the Trezor.

# Discussion History
# Action History
- Created by: phytohydra | 2023-09-08T00:16:32+00:00
