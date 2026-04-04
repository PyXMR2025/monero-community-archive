---
title: No XMR , no transaction history
source_url: https://github.com/monero-project/monero-gui/issues/1197
author: Dar1win
assignees: []
labels:
- invalid
- wontfix
created_at: '2018-03-25T21:49:50+00:00'
updated_at: '2018-03-30T02:36:56+00:00'
type: issue
status: closed
closed_at: '2018-03-29T21:45:21+00:00'
---

# Original Description
I trades some ripple to monero in January and use mymonero wallet. I believe it was the real site not the phishing site. Now when i check my balance there is no XMR and no history. I have also used GUI and downloaded the block chains and same results.
I have followed these instructions as well and still nothing.
https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

I have contacted the exchange and they are looking for the transaction to confirm i did receive the funds. I remember getting the XMR and then checking a day or two later and storing the seed in an encrypted file.

So what now?

# Discussion History
## 1337tester | 2018-03-25T22:01:09+00:00
How does this issue relate to this project? This is not the mymonero wallet project.

If you would transfer the actual monero to this wallet successfully and somehow lost them here, it might be an issue, but I suppose you just trusted your private keys to a third party, or? 

## Dar1win | 2018-03-25T23:07:51+00:00
I am wondering why i can not get transaction history from my seed. Seems to be a problem with the block chain?

## 1337tester | 2018-03-25T23:24:42+00:00
so I suppose you are using the Monero-GUI wallet, there should be something like "block height" in settings, this value tells the wallet from which height (meaning block number) it should scan the blockchain
![image](https://user-images.githubusercontent.com/6553766/33611778-e301f2d6-d9cf-11e7-9aa0-b738c13f2967.png)
try setting this value to 0, to scan the whole blockchain (or if you know the blocks of your tx, set the height to the oldest of these blocks)

## Dar1win | 2018-03-26T10:39:13+00:00
Hi, i tried that.
I tried all these thing:
https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

Still no history...

## 1337tester | 2018-03-26T21:41:32+00:00
Rule of thumb here
- if you can reproduce this scenario with a fresh wallet - then it is probably an issue and worth investigation
- if this, however, applies only to one specific situation in which you are not certain about the party sending you the XMR -> it's probably not a software issue...

## sanderfoobar | 2018-03-29T21:33:25+00:00
Sorry to hear you are experiencing problems. However, like @1337tester pointed out, the github issue tracker is for application issues (and enhancements). Best to ask in another place:

- Via Reddit using [this thread](https://www.reddit.com/r/Monero/comments/7hhgjx/monero_gui_01110_helium_hydra_megathread_download/?sort=new)
- On [stackexchange](https://monero.stackexchange.com)

The community will pick your questions up.

## sanderfoobar | 2018-03-29T21:34:45+00:00
+invalid

## sanderfoobar | 2018-03-29T21:37:05+00:00
+wontfix

# Action History
- Created by: Dar1win | 2018-03-25T21:49:50+00:00
- Closed at: 2018-03-29T21:45:21+00:00
