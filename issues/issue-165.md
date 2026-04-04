---
title: Account/Wallet Terminology
source_url: https://github.com/monero-project/monero-site/issues/165
author: palexande
assignees: []
labels: []
created_at: '2016-09-22T08:23:31+00:00'
updated_at: '2018-06-25T10:15:16+00:00'
type: issue
status: closed
closed_at: '2018-06-25T10:15:16+00:00'
---

# Original Description
Anybody have any input on this?  I am thinking of changing all references of "account" to "wallet"?  This would align with monero-wallet-cli.  Personally I prefer the term account, but I think most prefer the term wallet.


# Discussion History
## TedTheFicus | 2016-10-01T03:01:36+00:00
New here, but I agree with you 100%. Keep it simple for the user and standardize the terminology to wallet. 


## QuickBASIC | 2017-08-31T12:44:44+00:00
I think the calling it an "account" vs "wallet" was purposeful. Perhaps someone that's been in the community can clarify why that decision was made.

With Monero, I'm not certain if there's any difference in the way we use the terms or if they're interchangeable. 

I agree it could be confusing for a new user to have different terms than they're used to, but I'm not certain that we have to use the same terms that other cryptocurrencies do.

I feel like a lot of new users are confused by the wallet paradigm when it comes to crypto. Advanced users understand that their transactions are stored in a blockchain as inputs and outputs and their private keys allow them to sign inputs to send as outputs. There's no "account balance" and nothing is stored in a "wallet".

New users commonly are concerned when they delete a wallet file, or lose access to a computer that stores their crypto that the funds are somehow stored *in* that wallet file or *on* that device. 

I think "wallet" connotes holding actual physical bills and coins where "account" is something that we understand to be something we access by correctly identifying ourselves. (Photo ID at a branch, password on a bank website, 2-factor, signature on a check, etc). When you access your Monero "account" you're identifying yourself by the keys that you hold and scanning the blockchain for your transactions. In this case a banking institution is not responsible for holding your funds, the blockchain "holds" your funds, but you're responsible for keeping access to them with your keys, and the network is responsible for verifying that your keys are valid for the transactions that you're doing. 

 I think this verbiage is easier to grok and explain to new users than other alternatives.

## QuickBASIC | 2017-10-21T21:33:53+00:00
+discussion

## el00ruobuob | 2018-04-28T06:39:31+00:00
Please have a look to Moneropedia account entry [here](https://getmonero.org/resources/moneropedia/account.html).
The concept of account refers to a banking account. To me, the Wallet is only the software.
By the way, there is a few changes to make to GUI and CLI wallet to refer to account instead of wallet.

## erciccione | 2018-06-25T10:02:39+00:00
Looks to me the consensus here is to keep the wording as it is. And for me also make sense to keep it that way. Closing this issue, if relevant for GUI or CLI, please open another issue on those repositories.

+resolved

# Action History
- Created by: palexande | 2016-09-22T08:23:31+00:00
- Closed at: 2018-06-25T10:15:16+00:00
