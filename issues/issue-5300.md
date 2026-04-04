---
title: 'Monero balance after full sync. says 0. '
source_url: https://github.com/monero-project/monero/issues/5300
author: kinza1509
assignees: []
labels: []
created_at: '2019-03-15T22:33:57+00:00'
updated_at: '2019-03-28T16:57:46+00:00'
type: issue
status: closed
closed_at: '2019-03-28T16:57:46+00:00'
---

# Original Description
Hallo
My Balance at gui wallet is 0 after full sync. I am using the new Version 0.14.0
What can i do? 

# Discussion History
## kinza1509 | 2019-03-16T07:35:29+00:00
Can anyone Help me?

## dEBRUYNE-1 | 2019-03-16T08:00:07+00:00
Are you using the GUI in conjunction with a Ledger device? Also, have you looked at this guide?

https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

## kinza1509 | 2019-03-16T15:51:51+00:00
No no connection with the ledger. i did not find the problem, so i deleted all monero files.
Now i want to install the latest version and recover my wallet with my seed.
That should work or?
Can you tell me the latest version of gui wallet?
On getmonero.com there are 3 types of things i can download forwindows 64bit? i don´t know the difference and if it is the newest version?
Thx for answering :)

## dEBRUYNE-1 | 2019-03-16T19:39:21+00:00
>That should work or?

Yes. However, make sure to set a sensible `Restore height`

https://monero.stackexchange.com/questions/7581/what-is-the-relevance-of-the-restore-height

>Can you tell me the latest version of gui wallet?

The latest version of the GUI wallet is v0.14.0.0. 

>On getmonero.com there are 3 types of things i can download forwindows 64bit? 

If you want the GUI, you need `Windows, 64-bit` or `Windows, 64-bit Installer` 

> i don´t know the difference 

The first one is a portable version, whereas the second one is an installer. 

>and if it is the newest version?

Yes. To reiterate, most recent version for the *GUI* is v0.14.0.0.

## kinza1509 | 2019-03-19T21:52:17+00:00
So now i tried to recover my wallet with seed on a other computer also local note. The old transactions are here But the new ones are not here. And the Balance says 0. But i had also some monero bevor the new transactions?
Also the Error come that There are 0 incoming connection on Port 18080. Can that be the reason that my Balance is 0 and the new transactions do not came in? Restore height i Set 01.01.2019.
Please Help.



## dEBRUYNE-1 | 2019-03-20T06:51:06+00:00
>Also the Error come that There are 0 incoming connection on Port 18080

This is a warning which you can safely ignore, as it doesn't inhibit the daemon (monerod) from syncing properly. 

>Please Help.

Can you type `status` in `monerod` and post the output here? 

## kinza1509 | 2019-03-20T14:08:34+00:00
Ok i thought that could be the reason that i have the new transactions not in my wallet.
Yes there is the post.
![Unbenannt](https://user-images.githubusercontent.com/48460347/54690585-036da780-4b22-11e9-86fb-b43897557c67.PNG)


## kinza1509 | 2019-03-20T14:17:41+00:00
Further i do not see any transactions in my wallet.

## dEBRUYNE-1 | 2019-03-20T16:26:51+00:00
Do you remember when you made the first transaction to this particular wallet? 

## dEBRUYNE-1 | 2019-03-26T13:32:44+00:00
@kinza1509 - ping. 

## dEBRUYNE-1 | 2019-03-28T16:49:13+00:00
Author has not responded. As such, I am going to close this. 

## dEBRUYNE-1 | 2019-03-28T16:49:17+00:00
+resolved

# Action History
- Created by: kinza1509 | 2019-03-15T22:33:57+00:00
- Closed at: 2019-03-28T16:57:46+00:00
