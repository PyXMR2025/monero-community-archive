---
title: 'iOS build: Remove -n to overwrite existing files'
source_url: https://github.com/MrCyjaneK/monero_c/pull/5
author: sneurlax
assignees: []
labels: []
created_at: '2024-04-19T17:13:13+00:00'
updated_at: '2024-06-02T10:11:34+00:00'
type: pull_request
status: merged
closed_at: '2024-06-02T10:11:34+00:00'
merged_at: '2024-06-02T10:11:34+00:00'
---

# Original Description
`mv -f -n` is contradictory, as @AaronFeickert pointed out.  `-f` will suffice.

```
$ mv --help
...
  -f, --force                  do not prompt before overwriting
  ...
  -n, --no-clobber             do not overwrite an existing file
  ```

I tested this and it will still (re)build, convenient for iterative development and general build testing.

# Discussion History
# Action History
- Created by: sneurlax | 2024-04-19T17:13:13+00:00
- Merged at: 2024-06-02T10:11:34+00:00
