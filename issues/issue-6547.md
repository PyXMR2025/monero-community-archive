---
title: import_key_images not working
source_url: https://github.com/monero-project/monero/issues/6547
author: SomaticFanatic
assignees: []
labels: []
created_at: '2020-05-17T01:58:21+00:00'
updated_at: '2020-05-17T16:46:46+00:00'
type: issue
status: closed
closed_at: '2020-05-17T16:46:46+00:00'
---

# Original Description
To recreate issue:

1. Clone master. Create a fresh testnet wallet. Move over some tXMR. Send a single tx so your wallet has a mixture of sent and received funds. 

2. Create an associated view wallet. In the view wallet type `refresh`. View wallet will say `Balance: 123.456790123456, unlocked balance: 123.456790123456 (Some owned outputs have missing key images - import_key_images needed)`

3. Open original wallet. Type `export_key_images keyimagefile`. Wallet will say `Signed key images exported to keyimagefile`.

4. Open view wallet back up. Type `import_key_images keyimagefile`. Wallet will say `Signed key images imported to height [height], 0.000000000000 spent, 123.456790123456 unspent`

   0.000 spent? For some reason it isn't showing the spent funds in imported key images.

5. Type `refresh` in view wallet. Wallet will still say `Balance: 123.456790123456, unlocked balance: 123.456790123456 (Some owned outputs have missing key images - import_key_images needed)`

# Discussion History
## moneromooo-monero | 2020-05-17T13:02:22+00:00
Did you export/import outputs in the other direction first ?

## SomaticFanatic | 2020-05-17T13:13:33+00:00
No. I’ve exported key images before and the above process worked fine. Why is it important to export outputs from a view wallet?

## moneromooo-monero | 2020-05-17T14:33:02+00:00
Because the cold wallet calculates key images on the outputs it gets from the hot wallet.

## SomaticFanatic | 2020-05-17T15:03:19+00:00
Interesting. It works! Perhaps the message can be edited to say “export_outputs then import_key_images needed”

## moneromooo-monero | 2020-05-17T15:54:34+00:00
FWIW, this is done automatically when you make a tx (outputs and key images piggy back on the tx signing files).

# Action History
- Created by: SomaticFanatic | 2020-05-17T01:58:21+00:00
- Closed at: 2020-05-17T16:46:46+00:00
