---
title: 'Transfer: implement "busy indicator" while creating and committing transaction'
source_url: https://github.com/monero-project/monero-gui/issues/130
author: mbg033
assignees: []
labels: []
created_at: '2016-11-07T21:26:18+00:00'
updated_at: '2016-11-11T10:44:39+00:00'
type: issue
status: closed
closed_at: '2016-11-11T10:44:39+00:00'
---

# Original Description
probably by implementing async versions of `Wallet::createTransaction()` and `PendingTransaction::commit()`

# Discussion History
## Jaqueeee | 2016-11-08T13:53:14+00:00
@mbg033 I'm working on this one. I'm also replacing the standard dialogs with custom. 


## M5M400 | 2016-11-10T08:59:35+00:00
great - saves me to suggest custom dialogs for TX stuff :+1: 


# Action History
- Created by: mbg033 | 2016-11-07T21:26:18+00:00
- Closed at: 2016-11-11T10:44:39+00:00
