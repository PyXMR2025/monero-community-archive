---
title: Problems with  Windows Gui Wallet
source_url: https://github.com/monero-project/monero-gui/issues/992
author: sgf
assignees: []
labels: []
created_at: '2017-12-05T12:02:49+00:00'
updated_at: '2017-12-09T15:36:44+00:00'
type: issue
status: closed
closed_at: '2017-12-09T15:36:44+00:00'
---

# Original Description
recently the minerxmr.com transformed 0.5 XMR to me.
but i cant see it on the monero-gui on windows.

its always syn..ing ,has been take lots disk.(the sync takes me several days.)

but when sync completed my XMR also is 0.

im not sure is the monero-gui  works ?


# Discussion History
## 1337tester | 2017-12-05T14:01:34+00:00
Wich version you use?

Can be that you have high wallet creation height (the value from which block your wallet scans the blockchain)

## sgf | 2017-12-05T14:13:09+00:00
im using the last version v0.11.1.0
![monerogui](https://user-images.githubusercontent.com/2557696/33611459-6ac21ece-da09-11e7-9839-0a6bafd19f38.PNG)


## 1337tester | 2017-12-05T14:17:42+00:00
change this
![image](https://user-images.githubusercontent.com/6553766/33611620-583dfa3c-d9cf-11e7-8efd-b0cbe6321f2a.png)
set it to 0 as I have

## sgf | 2017-12-05T14:27:20+00:00
![monerogui1](https://user-images.githubusercontent.com/2557696/33612068-72d02ffa-da0b-11e7-95bf-be2ed486e199.PNG)

thank u mate. but it seems not a good idea....😂

it seems im lost the sync history and now i need sync soo much blocks.

## 1337tester | 2017-12-05T14:38:29+00:00
if you know ~~which block it was that you received the monero, you can set it to this value, it will sync from there

## dEBRUYNE-1 | 2017-12-06T21:00:08+00:00
>it seems im lost the sync history and now i need sync soo much blocks.

In Monero there's two "syncs". First, the blockchain sync, which is basically downloading the blockchain from other nodes / peers. Second, the wallet sync, which is the wallet "refreshing" / scanning blocks looking for transactions belonging to your address / wallet. The GUI currently uses the status bar for both syncs, which can be a bit confusing to newcomers. Thus, what you are seeing is the wallet refresh. 





## dEBRUYNE-1 | 2017-12-06T21:00:34+00:00
Also:

https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

## sgf | 2017-12-09T15:36:42+00:00
the problems soloved.im keep the client running 3 days.now the  0.5 XMR  got.
thank all,hope the monero Wallet gui  could be release more linght weight version .


# Action History
- Created by: sgf | 2017-12-05T12:02:49+00:00
- Closed at: 2017-12-09T15:36:44+00:00
