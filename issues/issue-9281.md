---
title: master branch does not contain newer checkpoints
source_url: https://github.com/monero-project/monero/issues/9281
author: vtnerd
assignees: []
labels:
- bug
created_at: '2024-04-05T22:35:38+00:00'
updated_at: '2024-05-21T04:36:44+00:00'
type: issue
status: closed
closed_at: '2024-05-21T04:36:44+00:00'
---

# Original Description
The [release branch has checkpoints](https://github.com/monero-project/monero/blob/81d4db08eb75ce5392c65ca6571e7b08e41b7c95/src/checkpoints/checkpoints.cpp#L252) not found in the [master branch](https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/checkpoints/checkpoints.cpp#L242). I am wondering when the `master` branch will "catch" up (assuming it will).

----

Additional background information not really needed for this "bug" report:

This caused an issue with LWS, which only syncs blocks since the last checkpoint to reduce the information needed to get LWS up and running. Someone compiled LWS with a recent monero `release-0.18` branch, initialized the LWS DB (with users), then switched to another LWS build using the monero `master` branch.

And for those curious why the switch to `master` for the monero repo - a change to how [libsodium is found](https://github.com/monero-project/monero/commit/cdab0d489c8b12558655467d5544b60c1713737b) causes build errors in LWS if not properly updated. So recent `develop` and `master` branches of LWS only work using `master` branch of monero, and the current `release-0.2_0.18` branch of LWS works only using `release-0.18` branch of monero, etc.

# Discussion History
## selsta | 2024-04-05T22:40:01+00:00
I can open a PR to bring the checkpoints up to date, and in the future always open 2 PRs to update checkpoints (one for master, one for release).

# Action History
- Created by: vtnerd | 2024-04-05T22:35:38+00:00
- Closed at: 2024-05-21T04:36:44+00:00
