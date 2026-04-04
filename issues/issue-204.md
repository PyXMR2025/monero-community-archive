---
title: Not enougth outputs to transfer with 3 mixes
source_url: https://github.com/monero-project/monero/issues/204
author: CryptoPools
assignees: []
labels: []
created_at: '2014-12-12T00:50:12+00:00'
updated_at: '2014-12-15T00:46:32+00:00'
type: issue
status: closed
closed_at: '2014-12-15T00:46:32+00:00'
---

# Original Description
Got trouble after upgrading monero from 0.8.8.4 to 0.8.8.6.
Can't send coins with 3 mixes - wallet reports "not enought outputs to mix". With 0 mixes all right.
Nothing changed at system config (ubuntu 14.04) - only replaced bitmonerod and simplewallet.
Whats wrong?


# Discussion History
## fluffypony | 2014-12-12T06:05:24+00:00
There's likely a dust input in the tx you're creating, and dust inputs typically have no match in the utxoset to mix with. Nothing has changed on this functionality between 0.8.8.4 and 0.8.8.6, but you can try revert to 0.8.8.4 and try the transaction again.


## CryptoPools | 2014-12-12T06:47:47+00:00
Thanks for answer.
Is there any possibility to solve this problem with monero 0.8.8.6?


## fluffypony | 2014-12-12T07:28:36+00:00
Send all your funds to yourself in chunks with 0 mixin, that way you're consolidating your inputs.


# Action History
- Created by: CryptoPools | 2014-12-12T00:50:12+00:00
- Closed at: 2014-12-15T00:46:32+00:00
