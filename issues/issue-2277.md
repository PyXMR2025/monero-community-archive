---
title: Update I2P guide to use i2pd
source_url: https://github.com/monero-project/monero-site/issues/2277
author: jermanuts
assignees: []
labels:
- 📚 docs
created_at: '2024-03-14T14:35:25+00:00'
updated_at: '2024-10-23T21:21:31+00:00'
type: issue
status: closed
closed_at: '2024-10-23T21:21:30+00:00'
---

# Original Description
https://www.getmonero.org/resources/user-guides/node-i2p-zero.html utilizes i2p zero which is no longer maintained since 2021.

They use a very old version of I2p version [0.9.50 ](https://github.com/i2p-zero/i2p-zero/blob/master/bin/import-packages.sh#L16)(2021-05-18) which is vulnerable, example: https://xeiaso.net/blog/CVE-2023-36325/ (Attackers can de-anonymize i2p hidden services with a message replay attack). Official site https://geti2p.net/en/blog/post/2023/06/25/new_release_2.3.0, https://geti2p.net/en/blog/post/2023/12/18/i2p-release-2.4.0, https://geti2p.net/en/blog/post/2022/04/21/Easy-Install-Updates etc

Update guide using [i2pd](https://i2pd.website/) which is more well maintained implementation in C++ and very fast and lightweight.

Reference: https://landchad.net/monerod/#i2p

# Discussion History
## jermanuts | 2024-03-17T17:01:19+00:00
I just saw https://github.com/monero-project/monero-site/pull/1968#issuecomment-1783948345

@plowsof can you open a PR with the updated guide?

## nahuhh | 2024-04-05T04:17:43+00:00
Afaik i2pzero pulls in latest java i2p router

## HardenedSteel | 2024-08-12T16:33:58+00:00
My related draft for the tutorial which can help: https://github.com/PurpleI2P/i2pd_docs_en/pull/95

> Afaik i2pzero pulls in latest java i2p router

I think we should still migrate to i2pd or i2p java

## HardenedSteel | 2024-10-07T00:55:54+00:00
this issue can be moved to: https://github.com/monero-project/monero-docs

## nahuhh | 2024-10-07T03:32:09+00:00
https://github.com/monero-project/monero-docs/pull/66

the above PR will remedy this issue.
We'll need to modify the i2p guide on -site to redirect accordingly

# Action History
- Created by: jermanuts | 2024-03-14T14:35:25+00:00
- Closed at: 2024-10-23T21:21:30+00:00
