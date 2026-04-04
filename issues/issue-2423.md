---
title: Review dart package.
source_url: https://github.com/monero-project/monero-site/issues/2423
author: mrtnetwork
assignees: []
labels: []
created_at: '2024-11-18T14:33:34+00:00'
updated_at: '2025-07-16T13:56:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Please leave your review and link it on the Monero website if possible. thanks

 [monero_dart ](https://github.com/mrtnetwork/monero_dart) is a Dart package that implements Monero cryptography for creating and signing RingCT (Rct) transactions in pure Dart. It supports the latest Bulletproof Plus for RCT signatures and multisignature accounts for transaction creation. This package includes comprehensive account management features such as account generation, seed-to-mnemonic conversion, and serialization. It also provides full support for interacting with Monero daemons and wallet RPCs, making it a complete solution for working with Monero in Dart.


# Discussion History
## mrtnetwork | 2025-07-16T12:11:52+00:00
@plowsof 
Now its 10x Faster 😎 

## plowsof | 2025-07-16T13:20:03+00:00
Impressive. 10x faster overall?

Will see if this can be reviewed by someone who knows what theyre looking at. I do have some basic questions though. 

How does this compare to an archived monero_dart repo @ https://github.com/mrcyjanek/monero.dart 
and this is yours https://pub.dev/packages/monero_dart correct?

Is monero_dart being used currently by any projects?


## mrtnetwork | 2025-07-16T13:45:01+00:00
> Impressive. 10x faster overall?
> 
> Will see if this can be reviewed by someone who knows what theyre looking at. I do have some basic questions though.
> 
> How does this compare to an archived monero_dart repo @ https://github.com/mrcyjanek/monero.dart and this is yours https://pub.dev/packages/monero_dart correct?
> 
> Is monero_dart being used currently by any projects?

**Impressive. 10x faster overall?**
Yes — in the previous version, signing an RCT transaction with 16 inputs and 16 outputs in pure Dart took about 2 minutes. Now, with the latest improvements, it completes in around 10 seconds.

**How does this compare to an archived monero_dart repo @ https://github.com/mrcyjanek/monero.dart?**
I'm not entirely sure what that archived repo was aiming to achieve or how complete it is — I haven’t based my implementation on it. My version was built independently to support full functionality in Dart, with a strong focus on performance.
Also, I don’t use any external libraries — my package is built entirely in pure Dart.

**And this is yours https://pub.dev/packages/monero_dart correct?**
Yes, that package is mine.

**Is monero_dart being used currently by any projects?**
Yes, it’s currently used in my Dart wallet project called [OnChain](https://github.com/mrtnetwork/onchain_wallet) Wallet, which you can find in my GitHub repository.
It also supports all major platforms: Android, Web, browser extensions, macOS, and Windows.

# Action History
- Created by: mrtnetwork | 2024-11-18T14:33:34+00:00
