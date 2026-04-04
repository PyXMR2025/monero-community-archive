---
title: No --detach option for monero-wallet-rpc
source_url: https://github.com/monero-project/monero/issues/2999
author: rwdim
assignees: []
labels:
- proposal
created_at: '2017-12-23T22:36:13+00:00'
updated_at: '2018-10-01T11:40:55+00:00'
type: issue
status: closed
closed_at: '2018-10-01T11:40:55+00:00'
---

# Original Description
Hi guys,

Wallet RPC is designed to run as a process without UI, so it stands to reason that it should have a --detach option as well.

Yes, I know I can background it with &, but why not be consistent and make all backround-able processes support "--detach"?

Great work otherwise!! :)


# Discussion History
## hyc | 2017-12-23T23:25:38+00:00
Why add code for a feature that no one actually needs, since `&` works perfectly well?

## moneromooo-monero | 2017-12-24T00:47:25+00:00
& would still kill the process on term exit IIRC. nohup *might* get around that but I'm not sure...

## rwdim | 2017-12-24T03:04:16+00:00
Just a suggestion.

if consistency isn't a consideration, then it's a non-issue.

## hyc | 2017-12-24T04:12:07+00:00
@moneromooo-monero yes, nohup addresses that for Bourne-style shells. For C-Shell derivatives, it's not needed.

## dEBRUYNE-1 | 2018-01-08T12:39:44+00:00
+proposal

## lessless | 2018-07-09T06:00:59+00:00
RPC service is an API service and only reason to keep it in the foreground is for logs monitoring. Not the most urgent feature, but would be a nice addition imo.


## moneromooo-monero | 2018-07-11T15:16:40+00:00
There is a patch for this, but the author did not use the existing daemon code, and didn't reply. Someone who wants this can feel free to change it.

## moneromooo-monero | 2018-10-01T11:35:11+00:00
+resolved

# Action History
- Created by: rwdim | 2017-12-23T22:36:13+00:00
- Closed at: 2018-10-01T11:40:55+00:00
