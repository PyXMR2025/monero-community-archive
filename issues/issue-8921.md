---
title: Assistance needed to regain access to my account
source_url: https://github.com/monero-project/monero/issues/8921
author: JAAFAR1996
assignees: []
labels: []
created_at: '2023-06-29T16:04:58+00:00'
updated_at: '2023-06-30T11:03:41+00:00'
type: issue
status: closed
closed_at: '2023-06-30T11:03:41+00:00'
---

# Original Description
I recently experienced an issue with my personal computer that unfortunately caused me to lose access to my electronic wallet with your institution.



Specifically, I found it necessary to do a complete reset and reinstall of my computer's operating system and applications. As a result, I seem to have lost access to my wallet/account.



When I attempt to log in using my usual credentials, the balance shows zero despite the fact that I previously had funds in the wallet.



I hope you may be able to assist me in regaining access to my wallet and determining if my previous balance is still intact. Please let me know what additional details or information I can provide to help you investigate and resolve this issue.



I appreciate your understanding and look forward to your reply. Thank you in advance.

# Discussion History
## selsta | 2023-06-29T16:06:42+00:00
Which wallet are you using?

## JAAFAR1996 | 2023-06-29T16:11:43+00:00
Monero GUI Wallet for Windows 64-bit

## selsta | 2023-06-29T16:12:39+00:00
Can you go to Settings -> Info and share what "Wallet mode" and "Wallet restore height" you have?

## JAAFAR1996 | 2023-06-29T16:14:55+00:00
Wallet mode : Simple mode
Wallet restore height: 2838868

## selsta | 2023-06-29T16:15:52+00:00
When was the first time you have received funds into your wallet? Approximately which month / year?

## JAAFAR1996 | 2023-06-29T16:17:54+00:00
april , 2023

## selsta | 2023-06-29T16:19:33+00:00
And just to confirm the transaction history shows zero transactions? And your wallet address matches your old address?


## JAAFAR1996 | 2023-06-29T16:22:34+00:00
Yes it is identical


## selsta | 2023-06-29T16:25:07+00:00
Is the wallet fully synchronized in the bottom left corner?

## JAAFAR1996 | 2023-06-29T16:25:47+00:00
yes it is 

## JAAFAR1996 | 2023-06-29T16:27:44+00:00
But the restore height number is different from what is written in the program now the previous thousand was 2839000 now 2838868


## plowsof | 2023-06-29T17:28:50+00:00
the number being less than what you wrote down is normal (to account for user error i believe the gui will shave a month off the blockheight) 

because you are in simple mode (a remote node randomly selected, which could be 'bad') - i will ask you to 'use another remote node that we know is 'good'. how can we do that? well first we need to change you wallet mode to advanced. 

With your wallet open so you are viewing the balance. click the [<- looking symbol in the top left corner. this will close you wallet. then on this screen you will see a button to "change wallet mode". click this and select advanced. then, you need to click open wallet from file and select this wallet again.

any popup asking you to start a local node - you should cancel. go to settings -> node and make sure that "Remote node" is highlighted by clicking it (the option below Local node)

click on (+) add remote node. in the address field type `selsta2.featherwallet.net` and in the port field type `18081` (username / password not required) click ok. then, click on this node in the list so it is highlighed grey. it should then start connecting.

OK - we're connected but we need to resync from this good node. Go to settings -> info . click change restore height - Do  not adjust the number. simply press ok.. and ok again. then wait until its finished. your true balance should display

## JAAFAR1996 | 2023-06-30T00:04:49+00:00
Thank you the full refund has been refunded .. Thank you, friends, for helping me

# Action History
- Created by: JAAFAR1996 | 2023-06-29T16:04:58+00:00
- Closed at: 2023-06-30T11:03:41+00:00
