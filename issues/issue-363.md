---
title: Missing transactions in GUI
source_url: https://github.com/monero-project/monero-gui/issues/363
author: Jaqueeee
assignees: []
labels: []
created_at: '2016-12-27T18:58:38+00:00'
updated_at: '2017-01-09T00:39:30+00:00'
type: issue
status: closed
closed_at: '2017-01-09T00:39:30+00:00'
---

# Original Description
Transactions sent to wallet created in GUI can be missed. This can happen when the wallet is created before the daemon is fully synced. After daemon sync is finished the wallet will fast refresh until current blockheight which will miss any transactions sent to the wallet before daemon was fully synced. 

**Temporary solution to make transaction appear in GUI**
Delete the wallet cache file to trigger a new refresh. 
http://monero.stackexchange.com/questions/3122/how-do-i-delete-the-wallet-cache/3123#3123

# Discussion History
# Action History
- Created by: Jaqueeee | 2016-12-27T18:58:38+00:00
- Closed at: 2017-01-09T00:39:30+00:00
