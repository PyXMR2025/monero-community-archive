---
title: '''transfer'' RPC question'
source_url: https://github.com/monero-project/monero/issues/5265
author: Crypto2
assignees: []
labels: []
created_at: '2019-03-10T23:19:27+00:00'
updated_at: '2019-03-11T16:48:51+00:00'
type: issue
status: closed
closed_at: '2019-03-11T16:48:51+00:00'
---

# Original Description
In the transfer RPC call, it says subaddr_indices defaults to 0, does this mean it is only going to spend from the one single index 0 address, or will it spend randomly from all subaddresses? (The latter would definitely be preferred and/or have an option to do so since subaddresses are being pushed so hard in lieu of payment IDs/integrated addresses.)

# Discussion History
## moneromooo-monero | 2019-03-11T09:45:53+00:00
subaddr_indices does not default to 0. It defaults to empty, in which case all subaddresses within the account are considered. Please send a patch to those docs :)

## el00ruobuob | 2019-03-11T10:06:47+00:00
My bad. I create a PR right away to correct it on the dev-guides.

## el00ruobuob | 2019-03-11T10:22:27+00:00
PRd in https://repo.getmonero.org/monero-project/monero-site/merge_requests/1013

Sorry for this misunderstanding.

## Crypto2 | 2019-03-11T16:48:51+00:00
No worries, thanks for the clarification :)

# Action History
- Created by: Crypto2 | 2019-03-10T23:19:27+00:00
- Closed at: 2019-03-11T16:48:51+00:00
