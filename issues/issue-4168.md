---
title: 'Monero GUI Wallet: "Restore from seed" - Restored wallet not allowed to be
  in the same wallet path?'
source_url: https://github.com/monero-project/monero-gui/issues/4168
author: ch9PcB
assignees: []
labels: []
created_at: '2023-05-03T09:20:30+00:00'
updated_at: '2023-05-04T16:58:03+00:00'
type: issue
status: closed
closed_at: '2023-05-04T16:58:03+00:00'
---

# Original Description
Below are the software that I use on my device (Intel 12th generation CPU, 24GB of RAM, 1TB of PCIe NVMe SSD):

```
Debian 11.7.0, 64bit (backported kernel version 6.1.15-1~bpo11+1)
Monero GUI Wallet, 0.18.2.2 - Fluorine Fermi
```

The first wallet was created about two years ago, and the path to the wallet points to a directory/folder of a different partition of the SSD. Let's call the folder `monero` and the partition is called `K`. 

Path to the first wallet: `/media/<name of user of Debian OS>/<name of the K: partition>/monero/wallet-1`

This `wallet-1` has two files: `wallet-1` (36.1MB) and `wallet-1.keys` (1.6KB)

I experimented restoring `wallet-1` from keys or mnemonic seed.

One thing I noticed is that the path of the restored `wallet-1` must not be identical to `/media/<name of user of Debian OS>/<name of the K: partition>/monero/wallet-1`. If I did that, the error message `Failed to store wallet appeared.`

I had no choice but to accept the default location of the restored wallet, which is `/home/<name of user of Debian OS>/Monero/wallets`

The full path of the restored wallet becomes `/home/<name of user of Debian OS>/Monero/wallets/wallet-1`. The restored `wallet-1` has two files that are identical to the original `wallet-1` files of identical file sizes.

**Questions**

1. Is it by design that the restored wallet cannot overwrite the original wallet? Because that was what I had planned to do. But when I did that, the error message `Failed to store wallet appeared`.
2. Even though `Daemon is synchronized`, is it normal for the wallet blocks of the restored wallet to count down to completion, I mean, until the orange bar is full?



# Discussion History
## selsta | 2023-05-03T09:24:30+00:00
I feel like you are overcomplicating things, just make sure to select a unique wallet name. If you want to use the same wallet name you have to select a different path.

> Is it by design that the restored wallet cannot overwrite the original wallet? Because that was what I had planned to do. But when I did that, the error message Failed to store wallet appeared.

Yes, it's not possible to overwrite a wallet. Delete it manually using your file explorer.

> Even though Daemon is synchronized, is it normal for the wallet blocks of the restored wallet to count down to completion, I mean, until the orange bar is full?

Yes, wallet sync and daemon sync are separate.

## ch9PcB | 2023-05-04T16:58:03+00:00
@selsta 

Thanks for your clarifications.

I shall close this issue now.

# Action History
- Created by: ch9PcB | 2023-05-03T09:20:30+00:00
- Closed at: 2023-05-04T16:58:03+00:00
