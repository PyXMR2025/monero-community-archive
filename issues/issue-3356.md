---
title: Missing transactions (!)
source_url: https://github.com/monero-project/monero-gui/issues/3356
author: JeanFrancoeur
assignees: []
labels: []
created_at: '2021-03-15T12:40:40+00:00'
updated_at: '2021-03-16T10:41:18+00:00'
type: issue
status: closed
closed_at: '2021-03-16T10:41:18+00:00'
---

# Original Description
There's missing transactions, the Monero-gui state that the wallet is synchronized and the daemon is started and even we use Rescan wallet balance nothing change.  What to do next?

Thank you in advance

# Discussion History
## selsta | 2021-03-15T12:41:55+00:00
Can you try restoring the wallet from seed and setting a proper restore height?

## JeanFrancoeur | 2021-03-15T12:51:16+00:00
Thank you @selsta, since I never do that, do you suggest that I need to uninstall and do a reinstall using the seed & restore height we took in backup?  Or there's another way to do it?

## selsta | 2021-03-15T12:52:27+00:00
You don't have to uninstall anything. You can go to the main menu by clicking the door symbol in the top left corner, then click on "Restore wallet from seed".

## JeanFrancoeur | 2021-03-15T13:31:38+00:00
ok got it, but I'm feeling like a dumb.  I've tried by using seed or keys, but I simply cannot press the next button, it stays disabled.

## selsta | 2021-03-15T13:32:30+00:00
You have to set an unique wallet name.

## JeanFrancoeur | 2021-03-15T13:47:52+00:00
I thought I need to restore over the same wallet.  I did twice, first time using the restore height at the wallet creation and the second time with the restore height found under the Settings/Wallet page.   The ui retrieved the latest data, but the missing transactions are still present.  I have the missing transactions ids.  Thank you for your support, it's very appreciated.

## selsta | 2021-03-15T13:52:20+00:00
Please use the restore height from wallet creation.

Which "wallet mode" are you using? You can check under Settings -> Info.

## JeanFrancoeur | 2021-03-15T13:55:13+00:00
I have tried both, but I note to use the creation one next time. I'm using 0.17.1.9-3ca5f10f (Qt 5.15.2) in advanced mode.

## selsta | 2021-03-15T13:56:10+00:00
And under advanced mode, do you use a local node or remote one?

## JeanFrancoeur | 2021-03-15T13:59:27+00:00
Local from day one.  I tried another time restoring the wallet with the restore height got at the creation.  The gui synchronize 39k-ish blocks.  But nothing change, same result.  Sorry for taking your time on this.

## selsta | 2021-03-15T14:00:56+00:00
No problem, can you try entering your txid on xmrchain.net and use the decode output feature to check if you received the coins?

## JeanFrancoeur | 2021-03-15T16:01:55+00:00
Well, I don't know why.  I restarted wallet-gui in the evening, synchronizing the deamon was so long, but this time no more missing transaction.  It's so weird, because one of those was 6 days old.  You can close the issue.  Again thank you for your help and support  @selsta 

## selsta | 2021-03-16T10:41:18+00:00
Hmm, not clear what the issue was. Please open a new issue if you encounter this again.

# Action History
- Created by: JeanFrancoeur | 2021-03-15T12:40:40+00:00
- Closed at: 2021-03-16T10:41:18+00:00
