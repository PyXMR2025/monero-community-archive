---
title: Config doesn't get overridden by CLI params (opposite standard)
source_url: https://github.com/xmrig/xmrig/issues/2892
author: lfaoro
assignees: []
labels: []
created_at: '2022-01-24T11:27:12+00:00'
updated_at: '2022-01-24T18:04:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If I cmake using feature `XMRIG_FEATURE_EMBEDDED_CONFIG` and pass a CLI arg e.g. `--bench=1M` or `--rig-id=$(hostname)`, xmrig ignores the CLI params.

Is this by design?

# Discussion History
## Spudz76 | 2022-01-24T13:59:06+00:00
Yes it's by design (I don't agree either)

Even a non-embedded config.json wins over (most? some?) command-line arguments.

Position last time I complained was existing users are already expecting it the broken way so making it like every other command-line app ever, where args win, would break their stuff somehow.  And that's somehow worth confusing every new user.

# Action History
- Created by: lfaoro | 2022-01-24T11:27:12+00:00
