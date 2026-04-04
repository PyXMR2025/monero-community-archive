---
title: Add margin around Remote Node area in Settings
source_url: https://github.com/monero-project/monero-gui/issues/581
author: ghost
assignees: []
labels:
- resolved
created_at: '2017-03-20T00:15:17+00:00'
updated_at: '2018-11-18T13:18:25+00:00'
type: issue
status: closed
closed_at: '2018-11-18T13:18:25+00:00'
---

# Original Description
For the first time I tried connecting to a remote node. I kept typing in node.moneroworld.com and clicking Start daemon, because that's how I assumed the connection was initialized. Yet it kept simply launching the local daemon.

Only after people in #monero-dev told me that I should not click Start daemon was the remote node connection established.

So ideally the Start daemon button should probably be disabled if somebody is connecting to a remote node, so they don't get confused like I did. This could go along with Issue #542 that clicking "Restore localhost" also enables the "Start daemon" button.

# Discussion History
## ghost | 2017-03-20T00:18:08+00:00
Or wait, is that what the Save button does? The Save button isn't just for the Login (optional) field?

If that's the case, then one way to associate the two lines/fields would be to add a larger margin above the Daemon box.

## Jaqueeee | 2017-03-22T15:41:24+00:00
that's right. The save button is for all those fields. I agree it's a bit confusing after we've added the rpc login options. Maybe we could add a margin and also rename the button to Connect?

## ghost | 2017-03-23T17:27:04+00:00
Great. I'll rename the Issue.

## Jaqueeee | 2017-03-28T16:53:11+00:00
Thought some more on this @xmr-eric. I don't think we should disable "start daemon" if connected to remote node. Because there is a scenario where you want your local daemon to sync while you are connected to a remote node. 

## ghost | 2017-03-28T17:03:34+00:00
Cool

## erciccione | 2018-11-18T13:16:59+00:00
New theme, new life

+resolved

# Action History
- Created by: ghost | 2017-03-20T00:15:17+00:00
- Closed at: 2018-11-18T13:18:25+00:00
