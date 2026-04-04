---
title: After v0.12 upgrade, wallet RPC transfer calls sometimes return an empty response
source_url: https://github.com/monero-project/monero/issues/3655
author: solidus1
assignees: []
labels: []
created_at: '2018-04-17T19:24:10+00:00'
updated_at: '2018-09-09T13:08:49+00:00'
type: issue
status: closed
closed_at: '2018-09-09T13:08:49+00:00'
---

# Original Description
After upgrading to v0.12, with get_tx_key set to true and mixin set to 6, transfers out are generally succeeding, but approximately 1 of 4 transfer RPC calls are returning an empty response. Without a txid clients are unable to determine whether a transfer was successful.

Running rescan spent and sweep unmixable on our wallet showed no improvement.



# Discussion History
## stoffu | 2018-04-18T04:55:00+00:00
Does the daemon print anything in response to that failed transfer RPC?

## moneromooo-monero | 2018-04-18T09:06:56+00:00
Are you sure it's not a timeout from the wallet side ?
How much time does the call take when it "return[s] an empty response" ?

## solidus1 | 2018-04-20T04:14:53+00:00
As slow as it sounds, the client timeout was set to 120 seconds, but upping that value considerably seems to be avoiding the issue now

## moneromooo-monero | 2018-04-20T07:16:36+00:00
Great. #3584 should help for some speedup too. It'll be made a lot faster by caching in the db in the future.

## moneromooo-monero | 2018-09-09T13:04:23+00:00
And that's merged now, so I'll call this fixed. Please reopen if you're still seeing it after that.

+resolved


# Action History
- Created by: solidus1 | 2018-04-17T19:24:10+00:00
- Closed at: 2018-09-09T13:08:49+00:00
