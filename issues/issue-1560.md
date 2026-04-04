---
title: 'Discussion: integrating approved FFS proposals into the GUI'
source_url: https://github.com/monero-project/monero-gui/issues/1560
author: ghost
assignees: []
labels: []
created_at: '2018-09-15T19:13:50+00:00'
updated_at: '2021-05-24T23:42:01+00:00'
type: issue
status: closed
closed_at: '2021-05-24T23:42:01+00:00'
---

# Original Description
I would like to start a discussion to see if there is any interest in the community/developers on creating a tab in the GUI indicating the current proposals awaiting funding in the FFS.

I understand that this would necessarily imply an interaction of the software with an external entity (server where FFS is hosted). This interaction should be limited in the simple reading of a JSON file containing the current approved proposals. I admit I do not know to what degree this can be dangerous to the software (perhaps by injecting malicious code via this file?). If this is a deal breaker because it adds an attack vector, then it's completely understandable to not add it.

That being said, it seems to me that integrating the GUI wallet with the FFS would increase the visibility of these proposals and would likely induce more users of the Monero network to participate in community actions.

# Discussion History
## sanderfoobar | 2018-09-15T20:06:28+00:00
It's a good idea, like #1484, but connections should most definitely go through Kovri. Another option is to explicitly opt-in in the settings, however I'm afraid not many people will be bothered to manually enable it.

## wqking | 2018-09-16T06:02:25+00:00
Re-post my comment on Reddit here.  
I suggest it's split to two layers,
Layer 1, backend API. Some REST API to list/fund an FFS.
Layer 2, the front end. For official wallet, it's the funding tab, but other wallets/websites are free to integrate it using Layer 1.

## selsta | 2021-05-24T23:42:01+00:00
FWIW Feather wallet does this. We decided a while ago that the official GUI should not integrate external things like CCS proposals. If someone has different opinions, please comment here and I can reopen the issue.

# Action History
- Created by: ghost | 2018-09-15T19:13:50+00:00
- Closed at: 2021-05-24T23:42:01+00:00
