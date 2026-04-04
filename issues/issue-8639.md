---
title: Podman Rootless Build fails
source_url: https://github.com/monero-project/monero/issues/8639
author: adrubesh
assignees: []
labels: []
created_at: '2022-11-15T17:24:55+00:00'
updated_at: '2024-12-23T16:01:17+00:00'
type: issue
status: closed
closed_at: '2024-12-23T16:01:17+00:00'
---

# Original Description
When using Podman to build, `podman build -t monero .` with Rootless containers it will fail due to user ID namespace constraints.

This can be solved by modifying: https://github.com/monero-project/monero/blob/365fd45b031b0a5c8104195dfabb786e839cb114/contrib/depends/funcs.mk#L81

and appending `--no-same-owner` to the `tar` command. 

```
 $(1)_extract_cmds ?= mkdir -p $$($(1)_extract_dir) && echo "$$($(1)_sha256_hash)  $$($(1)_source)" > $$($(1)_extract_dir)/.$$($(1)_file_name).hash &&  $(build_SHA256SUM) -c $$($(1)_extract_dir)/.$$($(1)_file_name).hash && tar --strip-components=1 --no-same-owner -xf $$($(1)_source) 
```

I'm unsure of what doing this may or may not break in standard build processes though, so I decided not to open a PR to patch for this specific case.. 

# Discussion History
# Action History
- Created by: adrubesh | 2022-11-15T17:24:55+00:00
- Closed at: 2024-12-23T16:01:17+00:00
