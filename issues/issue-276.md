---
title: Blockchain exporter config change didn't make
source_url: https://github.com/monero-project/monero/issues/276
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-05-01T00:20:50+00:00'
updated_at: '2015-05-06T10:38:28+00:00'
type: issue
status: closed
closed_at: '2015-05-06T10:38:28+00:00'
---

# Original Description
http://pastebin.com/HQzVpi8Y

What I did:

in my existing bitmonero, went in and modified blockchain_export.h according to the instructions. Saved.

Went back to root directory of source, typed in make. Got the above output.

Controlled by reverting the code to original setting, and it compiled fine. 


# Discussion History
## warptangent | 2015-05-01T07:59:18+00:00
Thanks for raising this. blockchain_export hadn't been updated yet to reflect changes in where BlockchainDB is instantiated.

Fixed in #277.


# Action History
- Created by: Gingeropolous | 2015-05-01T00:20:50+00:00
- Closed at: 2015-05-06T10:38:28+00:00
