---
title: GUI WALLET does not create blockchain
source_url: https://github.com/monero-project/monero-gui/issues/1307
author: lukebook
assignees: []
labels:
- resolved
created_at: '2018-04-11T00:23:44+00:00'
updated_at: '2018-04-28T17:27:18+00:00'
type: issue
status: closed
closed_at: '2018-04-28T17:27:18+00:00'
---

# Original Description
I send the coin from the GUI WALLET to another account but I can't receive the coin.
Even I can not check the TX ID in a blockchain.
GUI WALLET  signify the coin is already sent and i can not see the coin in GUI WALLET.
Please help me.

![kakaotalk_20180411_084706657](https://user-images.githubusercontent.com/38267080/38589842-898ee8d8-3d68-11e8-9542-c64fa778d864.png)



# Discussion History
## sanderfoobar | 2018-04-11T11:18:34+00:00
Looks like the transaction is still `PENDING`. At this time of writing, current block height is `1548797`. If it still says `PENDING`, after 11 hours, I would guess you're having trouble connecting to the network, or, there is a bug that is preventing you from making transactions.

Could you verify your transaction is still pending as of now?

## lukebook | 2018-04-12T00:23:35+00:00
Yes, transaction is still pending as of now.

Please help me how solve this problem! 

![kakaotalk_20180412_090247676](https://user-images.githubusercontent.com/38267080/38649699-287fe152-3e33-11e8-89cf-c4e730b09a43.png)


## dEBRUYNE-1 | 2018-04-12T09:06:37+00:00
@lukebook:

You're probably on the wrong (alternative) chain. Therefore, you should be able to resolve your issue with this guide:

https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-created-pe/

Please note (from the [linked guide](https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-as-a-result)):

>As a general rule of thumb, for each day you synced after the fork height (1546000 or April 6) you have to pop 800 blocks. Thus, let's say you synced 10 days on the wrong (alternative) chain, you should use --pop-blocks 8000

Since we're 6 days after the scheduled network upgrade, you ought to use `--pop-blocks 4800`

## sanderfoobar | 2018-04-28T17:05:57+00:00
Like @dEBRUYNE-1 mentioned, you're most likely on the wrong chain. Therefore, I'm closing this issue. For more help, try [r/monero](https://reddit.com/r/monero)

+resolved

# Action History
- Created by: lukebook | 2018-04-11T00:23:44+00:00
- Closed at: 2018-04-28T17:27:18+00:00
