---
title: User is prompted to keep daemon running upon closing wallet when connected
  to a remote node
source_url: https://github.com/monero-project/monero-gui/issues/2455
author: tobtoht
assignees: []
labels:
- resolved
created_at: '2019-11-23T17:06:06+00:00'
updated_at: '2019-12-21T04:36:38+00:00'
type: issue
status: closed
closed_at: '2019-12-21T04:36:38+00:00'
---

# Original Description
Expected behaviour: The wallet closes without the prompt.

# Discussion History
## selsta | 2019-11-23T17:28:52+00:00
Can reproduce when switching from local to remote node. If the GUI starts with a remote node connection, the GUI closes without a prompt.

## tobtoht | 2019-12-08T14:31:11+00:00
Not resolved in v0.15.0.2.

Steps to reproduce:
1. During wallet setup connect to an .onion node
2. Close the wallet

## xiphon | 2019-12-09T13:38:57+00:00
@tobtoht 

Yep, another bug gets triggered this time though, please re-open this issue

## tobtoht | 2019-12-09T13:42:05+00:00
I can't. @luigi1111 ?

## xiphon | 2019-12-20T20:48:26+00:00
@tobtoht 
Should be fixed via https://github.com/monero-project/monero-gui/pull/2604.

## selsta | 2019-12-21T04:31:49+00:00
+resolved

# Action History
- Created by: tobtoht | 2019-11-23T17:06:06+00:00
- Closed at: 2019-12-21T04:36:38+00:00
