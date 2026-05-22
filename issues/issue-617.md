---
title: disable ANSI escape codes when not a interactive terminal
source_url: https://github.com/Cuprate/cuprate/issues/617
author: redsh4de
assignees: []
labels: []
created_at: '2026-05-20T13:30:36+00:00'
updated_at: '2026-05-20T14:14:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
currently `logging.rs` builds the stdout layer with ANSI on unconditionally, so piping cuprated into a file outputs ANSI codes into it which renders into garbage:
```
[2m2026-05-20T14:11:13.063522Z[0m [32m INFO[0m Recovering database at /Users/red/Library/Application Support/Cuprate/fjall
[2m2026-05-20T14:11:13.074436Z[0m [32m INFO[0m Recovering LSM-tree at /Users/red/Library/Application Support/Cuprate/fjall/keyspaces/0
[2m2026-05-20T14:11:13.074513Z[0m [32m INFO[0m Recovering current manifest at /Users/red/Library/Application Support/Cuprate/fjall/keyspaces/0/v24
[2m2026-05-20T14:11:13.075354Z[0m [32m INFO[0m Recovering LSM-tree at /Users/red/Library/Application Support/Cuprate/fjall/keyspaces/9
[2m2026-05-20T14:11:13.075387Z[0m [32m INFO[0m Recovering current manifest at /Users/red/Library/Application Support/Cuprate/fjall/keyspaces/9/v12
[2m2026-05-20T14:11:13.075726Z[0m [32m INFO[0m Recovering LSM-tree at /Users/red/Library/Application Support/Cuprate/fjall/keyspaces/11
[2m2026-05-20T14:11:13.075748Z[0m [32m INFO[0m Recovering current manifest at /Users/red/Library/Application Support/Cuprate/fjall/keyspaces/11/v12
```

# Discussion History
# Action History
- Created by: redsh4de | 2026-05-20T13:30:36+00:00
