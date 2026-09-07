---
title: enhancement - modification of format to enable SPV-type functionality
source_url: https://github.com/monero-project/monero/issues/709
author: Gingeropolous
assignees: []
labels:
- enhancement
created_at: '2016-03-08T12:16:56+00:00'
updated_at: '2026-09-05T18:45:41+00:00'
type: issue
status: closed
closed_at: '2026-09-05T18:45:41+00:00'
---

# Original Description
With the expectation that Monero will have a very large blockchain, perhaps we should consider enabling headers-first network synchronizing , followed by downloading newest blocks first. In this way, a new user of the Monero software will be able to use their client software to manage their funds more quickly. 

This user-experience enhancement will become more relevant over time as the blockchain grows. 


# Discussion History
## ChristopherKing42 | 2016-08-04T03:40:56+00:00
If something like this was adopted, it would be less necessary: https://download.wpsoftware.net/bitcoin/wizardry/mimblewimble.txt


## dEBRUYNE-1 | 2018-01-08T12:42:58+00:00
+enhancement

## selsta | 2026-09-05T18:45:41+00:00
Closing this one, for now we have https://github.com/vtnerd/monero-lws and if there is a concrete proposal to improve wallet / daemon sync it will be opened to research lab repo anyway.

# Action History
- Created by: Gingeropolous | 2016-03-08T12:16:56+00:00
- Closed at: 2026-09-05T18:45:41+00:00
