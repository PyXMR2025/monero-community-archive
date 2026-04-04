---
title: get_tx_key not supported by HW wallet?
source_url: https://github.com/monero-project/monero/issues/4858
author: eigenbrot
assignees: []
labels: []
created_at: '2018-11-16T03:09:50+00:00'
updated_at: '2019-06-28T06:18:02+00:00'
type: issue
status: closed
closed_at: '2019-06-26T17:49:47+00:00'
---

# Original Description
I'm using a Ledger Nano S as a HW wallet and have `store-tx-info = 1` in monero-wallet-cli version v0.13.0.4. If I try `get_tx_key` the result is **`Error: command not supported by HW wallet`**.

Is this the correct behavior? [This](https://www.reddit.com/r/Monero/comments/8xhijh/using_ledger_comes_at_the_expense_of_functionality/) post suggests that this functionality has not been added yet. If this is true is there any way at all to recover a tx key? (I'm guessing no)

Thanks!

# Discussion History
## moneromooo-monero | 2019-01-19T00:42:55+00:00
AFAIK, the secret tx key is kept on the device, and the monero wallet does not know it. I think the wallet software gets an encrypted version, so it seems possible that code could be added to get the ledger to decrypt it if necessary.

That's my understanding, which may not be correct since I didn't write that code.


## moneromooo-monero | 2019-03-21T13:27:48+00:00
Ledger will support this in the near future.


## ph4r05 | 2019-03-21T13:46:17+00:00
Trezor supports this feature, now in master due to #5211

## golya87 | 2019-06-03T00:36:18+00:00
> Ledger will support this in the near future.

Do you know any ETA for this?

## dEBRUYNE-1 | 2019-06-03T07:40:31+00:00
@golya87 - Should be included in the upcoming v0.14.1 release. 

## golya87 | 2019-06-03T08:38:00+00:00
Sounds promising.
Where can I find a roadmap or relase date for this version?

## dEBRUYNE-1 | 2019-06-03T15:15:27+00:00
Quoting myself:

>I can only provide soon as ETA. Yesterday, almost all remaining pull requests (for the release) have been merged though. Thus, I think we are close.



## dEBRUYNE-1 | 2019-06-26T17:42:13+00:00
CLI v0.14.1.0 has been released. GUI v0.14.1.0 will be out soon. 

## dEBRUYNE-1 | 2019-06-26T17:42:17+00:00
+resolved

## ph4r05 | 2019-06-28T06:18:02+00:00
Just a note: this PR requires following PRs to be merged to monero-core (and monero-gui to use the updated monero-core)

- https://github.com/monero-project/monero/pull/5662
- https://github.com/monero-project/monero/pull/5673

# Action History
- Created by: eigenbrot | 2018-11-16T03:09:50+00:00
- Closed at: 2019-06-26T17:49:47+00:00
