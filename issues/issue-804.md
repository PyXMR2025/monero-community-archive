---
title: 'sweep_unmixable Error: no connection to daemon. Please make sure daemon is
  running.'
source_url: https://github.com/monero-project/monero/issues/804
author: perl5577
assignees: []
labels: []
created_at: '2016-04-12T22:46:15+00:00'
updated_at: '2016-04-16T10:17:03+00:00'
type: issue
status: closed
closed_at: '2016-04-16T10:17:03+00:00'
---

# Original Description
```
[wallet xxxxxx]: sweep_unmixable
Error: no connection to daemon. Please make sure daemon is running.
[wallet xxxxxx]: refresh
Starting refresh...
Refresh done, blocks received: 0                                
Balance: xxxxxxx, unlocked balance: xxxxxxx
[wallet xxxxxx]: sweep_unmixable
Error: no connection to daemon. Please make sure daemon is running.

```


# Discussion History
## moneromooo-monero | 2016-04-14T23:17:23+00:00
Can you post a relevant excerpt from the daemon log with set_log 2 ?


## osensei | 2016-04-15T20:03:23+00:00
@perl5577 were you using daemon v0.9.4? 

I saw this error too a while back, but I was using simplewallet v0.9.4 connected to a remote daemon running v0.9.3.


## perl5577 | 2016-04-16T10:17:03+00:00
I think is at the problèm.
Not error now 


# Action History
- Created by: perl5577 | 2016-04-12T22:46:15+00:00
- Closed at: 2016-04-16T10:17:03+00:00
