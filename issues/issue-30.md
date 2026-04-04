---
title: Problems with deterministic wallets on Windows (at least)
source_url: https://github.com/monero-project/monero/issues/30
author: jonas-sk
assignees: []
labels: []
created_at: '2014-06-11T00:11:31+00:00'
updated_at: '2014-06-12T23:33:39+00:00'
type: issue
status: closed
closed_at: '2014-06-12T23:33:39+00:00'
---

# Original Description
On Windows generating and restoring of deterministic wallets won't work. The mnemonic seed differs in console and log and restoring won't work with both. Also a wallet created on linux and is working to restore on Linux, won't restore on Linux.  However, you can restore a Windows-wallet if you use the words from the log on Linux. Another thing to mention is, that in the console there are three words mssing, but both seeds have way more differences in words even after that.
Example: Log: sorrow tremble sharp plate bounce ring purpose such nothing pop outside capture neck wild thunder several endless describe valley bruise back surprise split abuse
Console: sorrow tremble sharp plate bounce ring purpose such nothing pop outside capture veral endless describe valley bruise back surprise split abuse

TL;DR: Wrapper Issue when generating on Windows and unknown issue when restoring a wallet


# Discussion History
## monero-project | 2014-06-12T23:33:37+00:00
This issue is now considered close, as it was determined to be caused by the MS VC2012 compiler. Compiling with the 2013 MS compiler fixes it.


# Action History
- Created by: jonas-sk | 2014-06-11T00:11:31+00:00
- Closed at: 2014-06-12T23:33:39+00:00
