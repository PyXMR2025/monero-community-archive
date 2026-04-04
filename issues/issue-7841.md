---
title: Where do wallets created via the monero wallet RPC get stored? (Aside from
  main)
source_url: https://github.com/monero-project/monero/issues/7841
author: eddiejibson
assignees: []
labels: []
created_at: '2021-08-08T18:15:47+00:00'
updated_at: '2022-01-26T00:43:34+00:00'
type: issue
status: closed
closed_at: '2022-01-26T00:43:34+00:00'
---

# Original Description
Hello,

So obviously beside the --wallet-file that is defined upon startup of the RPC, where do all the other addresses get stored that are created via the wallet RPC? Whenever I create them I look inside the directory of the wallet file etc, but no files are present? And the .address.txt file still only has one address. So where exactly can I find the files for the keys, address etc? At first I thought this was defined within the --wallet-dir but obviously you cannot set the --wallet-file and --wallet-dir at the same time.

Thanks

# Discussion History
## trasherdk | 2021-08-09T04:29:18+00:00
Did you look in ` ~/.bitmonero/` ? That would be my guess.

## selsta | 2021-10-06T02:30:20+00:00
Do you mean subaddresses? I don't think they get stored in any file.

## elibroftw | 2022-01-26T00:26:46+00:00
I think you should've asked this question on the monero stack exchange. It's just so poorly worded. There's only one key per wallet. 

## selsta | 2022-01-26T00:43:34+00:00
Closing this as it's a question and the original issue creator never replied.

# Action History
- Created by: eddiejibson | 2021-08-08T18:15:47+00:00
- Closed at: 2022-01-26T00:43:34+00:00
