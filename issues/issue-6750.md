---
title: Wallet that did not generate transaction cannot store private transaction keys,
  check_tx states it did not receive change as output in transaction
source_url: https://github.com/monero-project/monero/issues/6750
author: Adreik
assignees: []
labels: []
created_at: '2020-08-07T09:05:13+00:00'
updated_at: '2022-05-25T10:07:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The following are transaction id/key pairs for a stagenet wallet with private spendkey 699a460e795cd125100d01c236e9568efbe9dd5199d8b175af00f25d25673108 and private viewkey e3b3f65ee75321adf69414bf6d995a5331e633c4d68cfa5cd8c170351632cb00:

197a032eb1441f7645673a702dafd79fa12694c2dda5ec8bee365fe8cc03a1b1, 8bcb301d635b6d5d814861b5f537302958cfcdf88572e5ef1c4d0efa47325401

1e701f4a3b7b6f16ba62d4cbfca6d0314a360237d7aec34979b576ada32fbd85, bf2e43ad85027610eea97377f6c6d55a8b4a07aa248be4c4a0b6747af3ba5209

15a0cc3004f656a2f9f372cb4cd475e32d2211675c49cb8a2e9af59b3515cf7d, ee6572fd11495d8332c9eb4943bc660392062f039218a762deeee3dbae38cf0a

Upon attempting to use the set_tx_key function to save each of these in a watch-only version of the wallet that signed these transactions, there are some problems that result.

In the case of txid 197a032eb1441f7645673a702dafd79fa12694c2dda5ec8bee365fe8cc03a1b1; sending to the address 59McWTPGc745SRWrSMoh8oTjoXoQq6sPUgKZ66dQWXuKFQ2q19h9gvhJNZcFTizcnT12r63NFgHiGd6gBCjabzmzHAMoyD6, entering "set_tx_key 197a032eb1441f7645673a702dafd79fa12694c2dda5ec8bee365fe8cc03a1b1 8bcb301d635b6d5d814861b5f537302958cfcdf88572e5ef1c4d0efa4732540" results in the message "Tx key successfully stored.", as expected. However entering "get_tx_key 197a032eb1441f7645673a702dafd79fa12694c2dda5ec8bee365fe8cc03a1b1" results in "0100000000000000000000000000000000000000000000000000000000000000" being returned, despite that the wallet just asserted that the correct transaction key was saved.



In the case of txid 1e701f4a3b7b6f16ba62d4cbfca6d0314a360237d7aec34979b576ada32fbd85 sending to 74wn1gQU5zEGCDco9XPM1H494Z7LJxGcuWe1u6GS2QpXBakL47K9oGpWUQbuSPJ33qBsN3FQ8uftRQ97ZrTC17rjDqVZDG2 (i.e. a subaddress rather than a main address), when entering "set_tx_key 1e701f4a3b7b6f16ba62d4cbfca6d0314a360237d7aec34979b576ada32fbd85 bf2e43ad85027610eea97377f6c6d55a8b4a07aa248be4c4a0b6747af3ba5209" an error message returns; that being "Error: Failed to store tx key: Given tx secret key doesn't agree with the tx public key in the blockchain". However, entering "check_tx_key 1e701f4a3b7b6f16ba62d4cbfca6d0314a360237d7aec34979b576ada32fbd85 bf2e43ad85027610eea97377f6c6d55a8b4a07aa248be4c4a0b6747af3ba5209 74wn1gQU5zEGCDco9XPM1H494Z7LJxGcuWe1u6GS2QpXBakL47K9oGpWUQbuSPJ33qBsN3FQ8uftRQ97ZrTC17rjDqVZDG2" results in the expected success message; "74wn1gQU5zEGCDco9XPM1H494Z7LJxGcuWe1u6GS2QpXBakL47K9oGpWUQbuSPJ33qBsN3FQ8uftRQ97ZrTC17rjDqVZDG2 received 9.999873540000 in txid <1e701f4a3b7b6f16ba62d4cbfca6d0314a360237d7aec34979b576ada32fbd85>".



The transaction 15a0cc3004f656a2f9f372cb4cd475e32d2211675c49cb8a2e9af59b3515cf7d includes change sent to 53BfKq328TnLjye9PU2qgiHnmbSvayJeef7C2X5LX5dgF4CpjfgzybaKDkJZGw9Vfreng6WRs86o6Btqpw4TJchPGHWU8Cc with another output sent to 74wn1gQU5zEGCDco9XPM1H494Z7LJxGcuWe1u6GS2QpXBakL47K9oGpWUQbuSPJ33qBsN3FQ8uftRQ97ZrTC17rjDqVZDG2 again. However, although entering "check_tx_key 15a0cc3004f656a2f9f372cb4cd475e32d2211675c49cb8a2e9af59b3515cf7d ee6572fd11495d8332c9eb4943bc660392062f039218a762deeee3dbae38cf0a 74wn1gQU5zEGCDco9XPM1H494Z7LJxGcuWe1u6GS2QpXBakL47K9oGpWUQbuSPJ33qBsN3FQ8uftRQ97ZrTC17rjDqVZDG2" works as expected, displaying "74wn1gQU5zEGCDco9XPM1H494Z7LJxGcuWe1u6GS2QpXBakL47K9oGpWUQbuSPJ33qBsN3FQ8uftRQ97ZrTC17rjDqVZDG2 received 1.000000000000 in txid <15a0cc3004f656a2f9f372cb4cd475e32d2211675c49cb8a2e9af59b3515cf7d>" as the returned text, entering "check_tx_key 15a0cc3004f656a2f9f372cb4cd475e32d2211675c49cb8a2e9af59b3515cf7d ee6572fd11495d8332c9eb4943bc660392062f039218a762deeee3dbae38cf0a 53BfKq328TnLjye9PU2qgiHnmbSvayJeef7C2X5LX5dgF4CpjfgzybaKDkJZGw9Vfreng6WRs86o6Btqpw4TJchPGHWU8Cc" displays the error, Error: 53BfKq328TnLjye9PU2qgiHnmbSvayJeef7C2X5LX5dgF4CpjfgzybaKDkJZGw9Vfreng6WRs86o6Btqpw4TJchPGHWU8Cc received nothing in txid <15a0cc3004f656a2f9f372cb4cd475e32d2211675c49cb8a2e9af59b3515cf7d>.

# Discussion History
## moneromooo-monero | 2020-08-08T14:41:49+00:00
https://github.com/monero-project/monero/pull/6752 fixes setting the tx key.

As for "doesn't agree", you seem to have the wrong secret key, generating the matching pubkey yields a different one that is on the chain.

## moneromooo-monero | 2020-08-08T14:42:49+00:00
Oh actually, was that sent to a subaddress ?

## Adreik | 2020-08-09T04:39:40+00:00
Screencap from wallet that generated the transaction:

https://i.imgur.com/r1Tddkc.png

Screencap from other wallet:

https://i.imgur.com/LuDfOXF.png

Yes, it was sent to a subaddress (74wn1gQU5zEGCDco9XPM1H494Z7LJxGcuWe1u6GS2QpXBakL47K9oGpWUQbuSPJ33qBsN3FQ8uftRQ97ZrTC17rjDqVZDG2).

- As for "doesn't agree", you seem to have the wrong secret key, generating the matching pubkey yields a different one that is on the chain.

I'm not sure what you mean by this; the corresponding check_tx_key statements do not produce any errors (only the one where the main address used as change causes an unexpected error with check_tx_key). Regardless, if the wallet signing the transaction is displaying the wrong private transaction key this is also a bug that might cause someone problems, no? check_tx_key statements not generating an error:

https://i.imgur.com/tzhJmgb.png

Observe that an incoming transaction is recorded for subaddress index 0 with txid 15a0cc3004f656a2f9f372cb4cd475e32d2211675c49cb8a2e9af59b3515cf7d, but using the same private transaction key the check_tx_key statement to verify if any outputs were sent to the address generates an error:

https://i.imgur.com/MR1ED7p.png

## moneromooo-monero | 2020-08-09T10:43:00+00:00
When sending to a subaddress, the derivation is different, it's not a simple private-to-secret. The set_tx_key call was not updated to support those.


## Adreik | 2020-08-09T11:29:44+00:00
Since the check_tx_key call as an example seems to work as usual in these cases, can the set_tx_key call not be modified to work for transactions where the outputs are subaddresses?

Also, is the behavior regarding check_tx_key for the change output as expected?

## moneromooo-monero | 2020-08-09T12:20:06+00:00
It can be modified to support this.
I suspect the check_tx_key error is wrong for a similar reason (but only suspect).

## moneromooo-monero | 2020-08-10T21:29:41+00:00
#6752 now handles setting the tx key for a tx which sent to a subaddress.

# Action History
- Created by: Adreik | 2020-08-07T09:05:13+00:00
