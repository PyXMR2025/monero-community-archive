---
title: get_output_distribution needs speeding up
source_url: https://github.com/monero-project/monero/issues/4662
author: moneromooo-monero
assignees: []
labels: []
created_at: '2018-10-19T09:46:59+00:00'
updated_at: '2018-12-13T01:57:09+00:00'
type: issue
status: closed
closed_at: '2018-12-13T01:57:09+00:00'
---

# Original Description
The cache (on_get_output_distribution) could  be made better by not fetching the whole thing when asked for 0..height-1 after height increases.

The wallet could also cache the data and ask for incremental data.

This is what takes a lot of the tx time now.

# Discussion History
## moneromooo-monero | 2018-11-10T16:42:53+00:00
https://github.com/monero-project/monero/pull/4825/files and another patch I can't PR yet because it's conflicting with master, so don't waste time doing this if you see no patch yet.

## moneromooo-monero | 2018-11-27T14:51:18+00:00
The second patch is https://github.com/monero-project/monero/pull/4908

## moneromooo-monero | 2018-12-13T01:17:51+00:00
+resolved

# Action History
- Created by: moneromooo-monero | 2018-10-19T09:46:59+00:00
- Closed at: 2018-12-13T01:57:09+00:00
