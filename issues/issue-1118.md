---
title: docker/CoreOS crash
source_url: https://github.com/monero-project/monero/issues/1118
author: FelixWeis
assignees: []
labels: []
created_at: '2016-09-23T14:46:08+00:00'
updated_at: '2017-09-30T09:30:21+00:00'
type: issue
status: closed
closed_at: '2017-09-30T09:30:21+00:00'
---

# Original Description
During the initial block download the monerod daemon uses an insane amount of CPU resources and is able to make the whole system non-responsive. (load of 14.00 seen on a CPU with 8 cores). 
At some point the whole docker system crashes.

The option `--max-concurrency` seems to be ignored.


# Discussion History
## moneromooo-monero | 2016-09-25T18:11:49+00:00
https://github.com/monero-project/monero/pull/1129 might help some.


## moneromooo-monero | 2017-09-20T21:14:33+00:00
As well as https://github.com/monero-project/monero/pull/2446 for max-concurrency.

## moneromooo-monero | 2017-09-30T09:24:38+00:00
I'll call that fixed with the patches above.

## moneromooo-monero | 2017-09-30T09:24:42+00:00
+resolved

# Action History
- Created by: FelixWeis | 2016-09-23T14:46:08+00:00
- Closed at: 2017-09-30T09:30:21+00:00
