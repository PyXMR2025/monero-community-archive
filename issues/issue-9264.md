---
title: Currently unable to restore wallet even with seedphrase
source_url: https://github.com/monero-project/monero/issues/9264
author: randomaccountlookingforsolutions
assignees: []
labels:
- question
created_at: '2024-03-28T00:32:36+00:00'
updated_at: '2024-03-29T02:21:02+00:00'
type: issue
status: closed
closed_at: '2024-03-28T15:22:18+00:00'
---

# Original Description
Here is the error i am getting even when using the correct (triple-checked) 25-word seed phrase to restore monero wallet, if someone could please help look into this:



'WalletRestoreFromSeedException'
#0      restoreWalletFromSeedSync (package:cw_monero/api/wallet_manager.dart:101)
#1      _restoreFromSeed (package:cw_monero/api/wallet_manager.dart:176)
#2      compute.<anonymous closure> (package:flutter/src/foundation/_isolates_io.dart:19)
#3      _RemoteRunner._run (dart:isolate:1090)
#4      _RemoteRunner._remoteExecute (dart:isolate:1084)
#5      _delayEntrypointInvocation.<anonymous closure> (dart:isolate-patch/isolate_patch.dart:300)
#6      _RawReceivePort._handleMessage (dart:isolate-patch/isolate_patch.dart:184)






# Discussion History
## selsta | 2024-03-28T00:34:34+00:00
Can you restore that seed with monero-wallet-cli? If not, what error message does it show.

## randomaccountlookingforsolutions | 2024-03-28T01:12:52+00:00
Hi selsta and thank you so much for such a prompt response. I have already posted the error at the post you have responded to. It is the entire error log. 'WalletRestoreFromSeedException'
I am using Stack Wallet by CypherStack for iOS 
I do not have monero-wallet-cli at the moment. I am relatively new to monero, but I can try and learn. I will look into it and try to get back to you.


## selsta | 2024-03-28T01:15:18+00:00
This is not the repository for Cake Wallet. If you can reproduce the issue with monero-wallet-cli then it will be easier for me to help because I can rule out an issue with Cake Wallet.

## randomaccountlookingforsolutions | 2024-03-28T13:35:54+00:00
Hi selsta:
I learned (as much as I reasonably could in a short amount of time) on how to use a monero-wallet-cli for macbook, and I tried to restore xmr wallet there using 25 word seedphrase.
And it gave this error:
"Electrum-style word-list failed verification."



## selsta | 2024-03-28T13:37:29+00:00
It means the seed is invalid. Is it possible you wrote it down incorrectly?

## randomaccountlookingforsolutions | 2024-03-28T15:22:18+00:00
Hi selsta:
As I have stated in my previous post, i have triple-checked the 25 word seedphrase, and also made sure each word was valid in the blobmaster github for monero here: https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h 

But yes, even after triple-checking I admit it is still possible, that maybe the order that I have them in may be incorrect. It is also a possibility that even though all 25 words are valid, that the order they are in may be inaccurate. I might just attempt to change the combinations and try restoring the wallet successfully that way. Regardless, thank you for your attempt at helping me, selsta. I will close the issue. 

## selsta | 2024-03-28T17:45:44+00:00
The order of words is important.

Here is a list of English words, make sure that all words are in this list: https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h#L56

## randomaccountlookingforsolutions | 2024-03-29T02:19:20+00:00
Hi selsta,
 
I have great news! I finally figured out the issue. I confused one of the words with another word, even though both were valid in the master mnemonic list! So it turns out i copied a different similar correctly spelled word with another. I have now restored my monero xmr wallet. THANK YOU!


## selsta | 2024-03-29T02:20:54+00:00
Glad you were able to resolve it!

# Action History
- Created by: randomaccountlookingforsolutions | 2024-03-28T00:32:36+00:00
- Closed at: 2024-03-28T15:22:18+00:00
