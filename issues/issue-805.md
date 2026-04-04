---
title: '''Limit'' command in GUI wallet sets download and upload speed to zero instead
  of displaying current speeds. '
source_url: https://github.com/monero-project/monero-gui/issues/805
author: mLouMN
assignees: []
labels:
- bug
- resolved
created_at: '2017-07-30T21:13:07+00:00'
updated_at: '2017-10-27T14:27:13+00:00'
type: issue
status: closed
closed_at: '2017-10-27T14:27:13+00:00'
---

# Original Description
settings>show status>(enter 'limit')>press enter

# Discussion History
## medusadigital | 2017-08-07T18:17:41+00:00
what you mean by "displaying current speed" ? 

the "limit" command comes from monerod and is used to set daemon upload and download speed.

there is no command to see which speed currently set. 

## Jaqueeee | 2017-08-08T17:19:51+00:00
yes, if you enter "limit" alone in monerod it shows the current limit.
+bug

## mLouMN | 2017-08-08T17:21:46+00:00
To clarify:

Enter 'limit' in monerod.exe

Now open the GUI wallet > status > 'limit'

Why do they do different things?

## medusadigital | 2017-08-08T17:28:32+00:00
ah sorry i did not know about that feature, my mistake

## MaxXor | 2017-09-17T19:28:53+00:00
This is actually a `monerod` bug. Fixed it in the PR referenced above.

The problem was the following: When you execute a command in the Monero GUI it spawns a new monero process which then calls the RPC, but the RPCs for the `limit` commands weren't implemented yet. So instead of showing the actual `limit` values it displayed the uninitialized values of the just spawned process.

## dEBRUYNE-1 | 2017-10-27T13:51:17+00:00
+resolved

# Action History
- Created by: mLouMN | 2017-07-30T21:13:07+00:00
- Closed at: 2017-10-27T14:27:13+00:00
