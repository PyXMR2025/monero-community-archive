---
title: inconsistent API for vmkit microvm hgosv bake
source_url: https://github.com/xmrig/xmrig/issues/3800
author: P4X-ng
assignees: []
labels: []
created_at: '2026-04-13T18:01:40+00:00'
updated_at: '2026-04-13T18:40:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
when baking a microvm with vmkit microvm hgosv bake: add-elf has a user specify --target, whereas add-file has a user specify a mapping host_path:guest_path - this is a bit confusing especially since the help just says 'NAME MAPPING' - the user doesn't necessarily know what the heck a mapping is or what name is being referred to (it's the hosted image name). Lets make all of these apis from run to run-bg to bake consistent please

# Discussion History
## SChernykh | 2026-04-13T18:40:35+00:00
what

# Action History
- Created by: P4X-ng | 2026-04-13T18:01:40+00:00
