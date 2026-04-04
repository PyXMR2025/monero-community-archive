---
title: Fix help strings of show_transfers and export_transfers commands
source_url: https://github.com/monero-project/monero/issues/6438
author: binaryFate
assignees: []
labels: []
created_at: '2020-04-08T15:25:44+00:00'
updated_at: '2020-05-01T20:22:17+00:00'
type: issue
status: closed
closed_at: '2020-05-01T20:22:17+00:00'
---

# Original Description
```
[wallet 4XXXX]: help show_transfers
Command usage: 
  show_transfers [in|out|pending|failed|pool|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]]
...

[wallet 4XXXX]: help export_transfers
Command usage: 
  export_transfers [in|out|all|pending|failed|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]] [output=<filepath>]
...
```

"all" is missing among the options for `show_transfers`. 

"pool" is missing among the options for `export_transfers`.

# Discussion History
## sumogr | 2020-04-08T16:19:22+00:00
done with #6440 

# Action History
- Created by: binaryFate | 2020-04-08T15:25:44+00:00
- Closed at: 2020-05-01T20:22:17+00:00
