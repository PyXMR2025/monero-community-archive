---
title: UI - when using bootstrap node, the status bar should show status of local
  daemon
source_url: https://github.com/monero-project/monero-gui/issues/1462
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-06-16T18:44:39+00:00'
updated_at: '2019-09-01T11:39:11+00:00'
type: issue
status: closed
closed_at: '2019-09-01T11:39:10+00:00'
---

# Original Description
not the remote daemon. 

# Discussion History
## dEBRUYNE-1 | 2018-06-17T08:51:34+00:00
Isn't the point of the bootstrap node that the user is able to use the wallet before his local daemon is synced? If the status bar displays the status of the *local* daemon, the user might think his wallet is not ready to be used yet. 

## Gingeropolous | 2018-06-19T00:54:03+00:00
Well, then it should indicate that it is showing the remote node sync status (which is kinda silly, because a remote node has to be 100% to be usable).

how will the user know how close their own node is close to 100% sync then? 

## Gingeropolous | 2018-06-19T00:54:24+00:00
Obviously the solution is another progress bar. 

## stoffu | 2018-06-19T03:10:33+00:00
@Gingeropolous Currently the only way to know the sync status of the local daemon is by the `status` command in the daemon console.

## dEBRUYNE-1 | 2018-06-19T12:47:12+00:00
@stoffu - Simply pressing `Show status` (on the `Settings` page) will provide a status overview as well. 

## qubenix | 2018-06-19T17:59:20+00:00
#1216

## ghost | 2019-08-30T21:33:55+00:00
This issue is included in #2304 (No. 2, bullet 2, and proposals in the end). I'd recommend closing this one here.

## Gingeropolous | 2019-09-01T11:39:10+00:00
yep, #2304 addresses this. 

# Action History
- Created by: Gingeropolous | 2018-06-16T18:44:39+00:00
- Closed at: 2019-09-01T11:39:10+00:00
