---
title: wallet-cli cold storage balance
source_url: https://github.com/monero-project/monero/issues/2954
author: jakubtrnka
assignees: []
labels:
- enhancement
- easy
created_at: '2017-12-18T13:49:18+00:00'
updated_at: '2018-08-15T12:41:00+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:41:00+00:00'
---

# Original Description
cold storage generated from viewkey should tell the user that it's not possible to determine the final balance unless key_images are imported. monero-wallet-cli is telling potentially incorrect value. 

# Discussion History
## jakubtrnka | 2017-12-18T13:59:24+00:00
wallet should tell something like
"verified balance: xxx"
"unverified balance:yyy"
for transaction whose key_images have been imported and whose not respectively.

## ghost | 2017-12-18T15:29:57+00:00
Interesting idea

## moneromooo-monero | 2017-12-19T16:57:05+00:00
The multisig code does this already. Extending it for cold wallets should be a simple task for a newcomer to get their first patch in.

## dEBRUYNE-1 | 2018-01-08T12:46:27+00:00
+enhancement

## dEBRUYNE-1 | 2018-01-08T12:56:06+00:00
+easy

## al-maisan | 2018-01-14T19:26:51+00:00
I would like to try my hand on this unless someone else is already working on it.

## moneromooo-monero | 2018-01-15T11:07:17+00:00
Go for it, try #monero-dev if you want help finding things.

## al-maisan | 2018-02-24T16:40:24+00:00
I was too optimistic -- 5 weeks passed already and I did not find any time to work on this.
If anyone else is interested: please ignore me and go for it.

## jakubtrnka | 2018-02-26T12:19:09+00:00
Ok, I'll make a try 

## mizuki-hikaru | 2018-04-13T07:05:57+00:00
I'm trying to do this.

Am I correct in understanding that we should modify the existing code so that `balance` shows something like "image keys are not imported" instead of the balances when the image keys are not present?

@moneromooo-monero Right now I am looking at the `simple_wallet::show_balance_unlocked` code. How is this implemented in the multisig code? Is there a file and line number I can check, to see what you mean by this?

## moneromooo-monero | 2018-04-18T10:48:42+00:00
Yes to the first paragraph.
For the second:
```
  std::string extra;
  if (m_wallet->has_multisig_partial_key_images())
    extra = tr(" (Some owned outputs have partial key images - import_multisig_info needed)");
```
So you'll to add a function to wallet2 that chels whether any key images are missing. Pretty much the same as has_multisig_partial_key_images, just a different bool to check.

## mizuki-hikaru | 2018-04-19T02:25:25+00:00
After looking into this further I think it's not possible to detect if the image keys aren't present, so this is just a simple warning for all watch-only wallets. Is this right?

for example at https://github.com/monero-project/monero/compare/monero-project:master...jcktm:wallet-cli-cold-storage-balance?expand=1

## moneromooo-monero | 2018-05-09T10:12:22+00:00
The code I pasted above does it.

## moneromooo-monero | 2018-08-15T11:49:24+00:00
+resolved

# Action History
- Created by: jakubtrnka | 2017-12-18T13:49:18+00:00
- Closed at: 2018-08-15T12:41:00+00:00
