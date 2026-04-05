---
title: '`--threads` option does not take precedence over automatically-located config
  file'
source_url: https://github.com/xmrig/xmrig/issues/3385
author: unsocial-bleach
assignees: []
labels: []
created_at: '2023-12-21T09:27:24+00:00'
updated_at: '2025-06-18T22:26:38+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:26:38+00:00'
---

# Original Description
**Describe the bug**
I believe that configuration options should be used in this order:
1. If a CLI argument is specified, use it.
2. If a configuration file is specified as a CLI argument via the `--config` argument, use the parameters in that configuration file.
3. Otherwise, use the parameters found in the configuration file found at a default search path (e.g., `.config/xmrig.json`).

Currently, the number of threads configuration parameter (and maybe other parameters too) appear to be fetched in the order 3, 1, 2.

**To Reproduce**
1. Create a configuration file at `~/.config/xmrig.json`. Do not specify threads in this file.
2. Run `xmrig --threads 1`

**Expected behavior**
xmrig should run with only one thread

**Actual behavior**
xmrig runs with as many threads as the system has cores/cpus.

**Required data**
- Linux
- xmrig v6.21.0

**Additional context**
Running with `xmrig --config .config/xmrig.json --threads 1` works properly (and also still works properly independent of the argument order). The issue appears to exclusively be when an auto-located configuration is used.

# Discussion History
# Action History
- Created by: unsocial-bleach | 2023-12-21T09:27:24+00:00
- Closed at: 2025-06-18T22:26:38+00:00
