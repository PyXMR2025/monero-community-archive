---
title: mainnet sync very slow
source_url: https://github.com/seraphis-migration/monero/issues/219
author: nahuhh
assignees: []
labels: []
created_at: '2025-11-06T16:24:59+00:00'
updated_at: '2025-11-08T01:26:54+00:00'
type: issue
status: closed
closed_at: '2025-11-08T01:26:39+00:00'
---

# Original Description
Using the stressnet binaries:

1. Poor connectivity -> i commented out the dummy hard fork heights for mainnet and was able to connect
2. Notably slower sync - 22 blocks/sec vs 262 blocks/sec using master

not sure if this is some regression, an issue with checkpoints,  or sonething else

Ive so-far bisected back to the stressnet release and see the same behavior.

.. i swear i had tested mainnet sync before, but maybe not from genesis(?).. need to check my notes..

# Discussion History
## nahuhh | 2025-11-08T01:26:54+00:00
Will reopen if necessary after better testing

# Action History
- Created by: nahuhh | 2025-11-06T16:24:59+00:00
- Closed at: 2025-11-08T01:26:39+00:00
