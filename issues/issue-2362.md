---
title: 'wallets: RINO?'
source_url: https://github.com/monero-project/monero-site/issues/2362
author: plowsof
assignees: []
labels: []
created_at: '2024-08-28T20:18:44+00:00'
updated_at: '2024-10-05T09:36:09+00:00'
type: issue
status: closed
closed_at: '2024-10-05T09:36:09+00:00'
---

# Original Description
https://www.rino.io/

- multisig for the purposes of wallet back up with features such as multi user accounts and public display of in/out tx's.
- claims to be open source and have reproducible builds which i have not confirmed
    - [How to build it and verify it matches RINO online version
](https://github.com/rino-wallet/frontend?tab=readme-ov-file#how-to-build-it-and-verify-it-matches-rino-online-version)
- in use by monerokon organisers to handle XMR funds.
- highest tier sponsor of monerokon for 2 consecutive years (see [past events](https://monerokon.org/past))

# Discussion History
## HardenedSteel | 2024-08-31T23:25:45+00:00
its so easy to put backdoor to web apps, is it possible to "self host"?

## plowsof | 2024-09-01T09:05:47+00:00
The hashes of the javascript file(s) served to you by rino that run in your browser can be built from source and the hashes should match. I will confirm this soon. 
https://app.rino.io/build-integrity.txt this would prevent any hidden changes to the source code. 

They also have https://github.com/rino-wallet/integrity-checker which ive not used. 

We could ask a rino rep to respond if needed

## plowsof | 2024-10-05T09:36:09+00:00
closing down end of october https://www.reddit.com/r/Monero/comments/1fwmhto/rino_wallet_closing_down_end_of_october/

# Action History
- Created by: plowsof | 2024-08-28T20:18:44+00:00
- Closed at: 2024-10-05T09:36:09+00:00
