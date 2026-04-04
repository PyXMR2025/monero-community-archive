---
title: getblocktemplate rpc call always returns "Core is busy" despite daemon being
  synced.
source_url: https://github.com/monero-project/monero/issues/1788
author: osensei
assignees: []
labels: []
created_at: '2017-02-24T01:56:46+00:00'
updated_at: '2017-02-25T08:23:28+00:00'
type: issue
status: closed
closed_at: '2017-02-25T08:23:28+00:00'
---

# Original Description
Happens on v0.10.2, on both testnet and mainnet:

    {
      "error": {
        "code": -9,
        "message": "Core is busy"
      },
      "id": "0",
      "jsonrpc": "2.0"
    }

# Discussion History
## hyc | 2017-02-24T02:34:49+00:00
Known issue, fixed by PR #1786

## osensei | 2017-02-24T05:16:58+00:00
Great! I can confirm it works.

## osensei | 2017-02-25T01:00:47+00:00
Hmmm, it keeps happening. It worked yesterday and it was working today, but I restarted the daemon and now it happens again.

## osensei | 2017-02-25T01:31:47+00:00
Sorry, my bad. 
It is working now, but it wasn't working in the testnet I was synced using one exclusive node that seemed to be out of sync of the real testnet.

# Action History
- Created by: osensei | 2017-02-24T01:56:46+00:00
- Closed at: 2017-02-25T08:23:28+00:00
