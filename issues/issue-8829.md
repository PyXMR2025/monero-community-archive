---
title: REDACTED FOR PRIVACY
source_url: https://github.com/monero-project/monero/issues/8829
author: ghost
assignees: []
labels: []
created_at: '2023-04-23T03:25:50+00:00'
updated_at: '2023-10-25T21:28:32+00:00'
type: issue
status: closed
closed_at: '2023-04-23T16:49:21+00:00'
---

# Original Description
REDACTED FOR PRIVACY

# Discussion History
## selsta | 2023-04-23T03:28:55+00:00
See https://github.com/monero-project/monero/issues/8657

It's unclear if this is an issue with macOS or on our side. Two workarounds:

- Start monerod with the `MONERO_RANDOMX_UMASK=8` env var.
- Use the binaries from getmonero.org – they are built with an older SDK that doesn't have this issue.

## selsta | 2023-04-23T16:49:21+00:00
Closing as a duplicate.

# Action History
- Created by: ghost | 2023-04-23T03:25:50+00:00
- Closed at: 2023-04-23T16:49:21+00:00
