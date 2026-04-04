---
title: UI broken for restoring hardware wallet
source_url: https://github.com/monero-project/monero/issues/5469
author: Belkaar
assignees: []
labels: []
created_at: '2019-04-20T06:34:46+00:00'
updated_at: '2019-04-21T06:57:18+00:00'
type: issue
status: closed
closed_at: '2019-04-21T06:57:18+00:00'
---

# Original Description
Client: monero-wallet-gui v0.14.0.0
OS: Windows

* Select "Create new wallet from hardware"
* Select "Restore a wallet from device."

The UI breaks and you can't enter the wallet creation heigt.

![HWwalletUiProblem](https://user-images.githubusercontent.com/2395990/56453757-1bb22b80-6347-11e9-9a4b-cbe2f4ea447e.png)


# Discussion History
## dEBRUYNE-1 | 2019-04-20T07:12:35+00:00
We're aware of this issue. It will be fixed in the upcoming release. In the meantime, you should be able to use this work around:

>There is a fix for the time being: You can access the restore height window by selecting the wallet location and pressing tab once.

## erciccione | 2019-04-20T12:20:25+00:00
@Belkaar This is the wrong repo. This issue should have been opened in monero-gui.

@fluffypony @luigi1111 There is a new GitHub feature which allow to transfer issues to another repo (https://help.github.com/en/articles/transferring-an-issue-to-another-repository). That could be used instead of closing and reopening this issue.

## Belkaar | 2019-04-20T18:19:32+00:00
@erciccione Sorry for choosing the wrong repo. Feel free to move the issue, i don't seem able to.

## dEBRUYNE-1 | 2019-04-21T06:47:36+00:00
@Belkaar - I'll close it if you confirm that the work around I posted works. 

## Belkaar | 2019-04-21T06:49:35+00:00
@dEBRUYNE-1 - Yes, the workaround did work.

## dEBRUYNE-1 | 2019-04-21T06:51:15+00:00
All right, going to mark this as resolved then. 

## dEBRUYNE-1 | 2019-04-21T06:51:19+00:00
+resolved

# Action History
- Created by: Belkaar | 2019-04-20T06:34:46+00:00
- Closed at: 2019-04-21T06:57:18+00:00
