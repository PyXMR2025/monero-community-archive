---
title: Shutdown node if RPC fails to start
source_url: https://github.com/Cuprate/cuprate/issues/688
author: Boog900
assignees: []
labels: []
created_at: '2026-08-14T21:10:24+00:00'
updated_at: '2026-08-14T22:44:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Not quite sure either but if we want to shutdown on listener bind failure then we would have to move TcpListener outside of this task, which would transform init_rpc_servers into an async fn. Since the task is stored in task_executor I believe it is more suited for the graceful shutdown pr to join all tasks and shutdown on failure.

_Originally posted by @SyntheticBird45 in https://github.com/Cuprate/cuprate/pull/675#discussion_r3787053229_
            

# Discussion History
## redsh4de | 2026-08-14T22:41:02+00:00
Done in #586, if address fails to bind the node will shut down

```
2026-08-14T22:43:58.508273Z  INFO Starting blockchain syncer
2026-08-14T22:43:58.508473Z  INFO Starting RPC server restricted=false address=127.0.0.1:18081
2026-08-14T22:43:58.508510Z ERROR Failed to launch node: failed to bind RPC listener on 0.0.0.0:18089: Address already in use (os error 98)
2026-08-14T22:43:58.508529Z  INFO Blockchain manager shut down.
2026-08-14T22:43:58.508530Z  INFO Txpool manager shut down.
2026-08-14T22:43:58.508567Z  INFO Blockchain syncer shut down.
2026-08-14T22:43:58.508655Z  INFO RPC server shut down. restricted=false
```

# Action History
- Created by: Boog900 | 2026-08-14T21:10:24+00:00
