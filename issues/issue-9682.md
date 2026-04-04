---
title: Transaction stuck on Pending for a long time
source_url: https://github.com/monero-project/monero/issues/9682
author: CocolinoFan
assignees: []
labels: []
created_at: '2025-01-06T12:57:52+00:00'
updated_at: '2025-01-06T17:33:29+00:00'
type: issue
status: closed
closed_at: '2025-01-06T15:18:07+00:00'
---

# Original Description
Hey,
I am trying to make a transaction as I did many times before. But this time things are odd.
->First, I only made one transaction in the GUI wallet, but for whatever reason it was split in multiple transactions. 
->Secondly, if I add the transactions together it does not add up to the original amount I've send (the XMR shows as gone in the top left where it shows you your balance) . -> Small update on this. I was checking with `monero-wallet-cli` and `monero-wallet-cli` does see all (3) transactions that add up to the right amount, but the GUI only sees 2 transactions.
->Thirdly, and the biggest issue, two of the three transactions are stuck at Pending for hours. This transactions have not been broadcast as I can't find them in block explorers. 

Let me know if there are any logs I can provide to troubleshoot this.

I am using: `0.18.3.4-release`

# Discussion History
## CocolinoFan | 2025-01-06T15:18:07+00:00
[UPDATE]: I found [this article](https://www.getmonero.org/resources/user-guides/howto_fix_stuck_funds.html) and got the idea to delete the wallet files and recover from seed. This worked, the pending transactions wore removed and the founds are back into my wallet.
I must say:
1) This was not intuitive at all.
2) I am still confused why my 1 transaction was split up into 3 transactions.

## CocolinoFan | 2025-01-06T16:25:14+00:00
😡😡😡
The founds wore back after I deleted the wallet and re-sync buy I could not spend my founds, It was giving me a `Error: transaction was rejected by daemon Reason: double spend`
I go to Settings -> Rescan wallet balance 
Now it shows the amount XMR like those pending transactions went through, but they didn't, and I can't see them in the Transaction history in the GUI or the `cli` wallet.

Ok I found this comment: https://github.com/monero-project/monero-gui/issues/3930#issuecomment-2070540221
What was happening is that those pending transactions wore in my local `monerod`'s pool, running the command `flush_txpool` in `monerod` flushed the transaction from my local node and I can spend the founds.
😇😇😇


## CocolinoFan | 2025-01-06T17:30:56+00:00
While I am here I will also add. 
The problem was originally caused by the following error in `monerod`: `E notify::send_txs provided message exceeding covert fragment size`
My monero node is using Tor, I2P and is also used for mining. 
So, to solve this, I just used a fresh monero node running on the clear-net without any mining. After I broadcasted my transaction I went back to my original node.

## selsta | 2025-01-06T17:33:13+00:00
@CocolinoFan the transaction is too large to send over I2P/Tor without adding the `disable_noise` parameter, which slightly reduces your privacy.

Example way too use it

```
--tx-proxy i2p,127.0.0.1:4447,disable_noise
```

alternatively you can send a smaller transaction (in size, meaning less inputs)

# Action History
- Created by: CocolinoFan | 2025-01-06T12:57:52+00:00
- Closed at: 2025-01-06T15:18:07+00:00
