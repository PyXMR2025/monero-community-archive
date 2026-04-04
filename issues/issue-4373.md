---
title: Building for Windows in MSYS2. All fine until `make release-win64 -j4`
source_url: https://github.com/monero-project/monero-gui/issues/4373
author: imfatant
assignees: []
labels: []
created_at: '2024-11-08T09:35:24+00:00'
updated_at: '2024-12-13T23:39:34+00:00'
type: issue
status: closed
closed_at: '2024-12-13T23:39:34+00:00'
---

# Original Description
I'm not going to describe the number of errors, or post a log. Usually I would. I think a dev should simply try this and feel his nuts shrink.

I'll put it on hold until you get a chance to look at this. Just follow your own install instructions and you'll see what I mean.

:)

# Discussion History
## selsta | 2024-11-10T00:03:31+00:00
The monero submodule we currently use doesn't compile with the latest boost version used by MSYS2. To fix that you have to manually check out the latest version.

```
cd monero-gui
cd monero
git fetch origin
git reset --hard origin/release-v0.18
cd ..
MANUAL_SUBMODULES=1 make release-win64 -j4 
```

If that does not work for you you wil have to share build logs.

## selsta | 2024-12-13T23:39:34+00:00
Closing due to lack of reply.

# Action History
- Created by: imfatant | 2024-11-08T09:35:24+00:00
- Closed at: 2024-12-13T23:39:34+00:00
