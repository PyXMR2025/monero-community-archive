---
title: torrent magnet link?
source_url: https://github.com/monero-project/monero-site/issues/508
author: phloatingman
assignees: []
labels: []
created_at: '2017-12-13T05:28:14+00:00'
updated_at: '2020-04-07T09:35:07+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:35:06+00:00'
---

# Original Description
Any plans on having a torrent magnet link as an option to download the gui and cli?

# Discussion History
## erciccione | 2017-12-15T13:51:41+00:00
+feature

## QuickBASIC | 2018-01-30T02:03:41+00:00
Generally the slow part isn't the download it's the verification. Importing the blockchain with verification set to true can be a very slow process... I'm not sure we want to encourage people to download and import a blockchain any other way than a direct download from the site. (I believe Fluffy updates the blockchain.raw direct download at the moment.) I'm afraid some might be tempted to use verify=0 to make the import faster and have possibly compromised data.

The blockchain changes each block and while conceivably we could add SHA256 hashes and GPG sign it say once a month, people aren't good at checking hashes against downloads anyway.



## erciccione | 2020-04-07T09:35:06+00:00
This issue is old and was discussed and closed on gitlab. Please reopen if you feel it's still relevant.

# Action History
- Created by: phloatingman | 2017-12-13T05:28:14+00:00
- Closed at: 2020-04-07T09:35:06+00:00
