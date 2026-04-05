---
title: Add wget to dependencies for Ubuntu advanced build
source_url: https://github.com/xmrig/xmrig/issues/2884
author: benthetechguy
assignees: []
labels: []
created_at: '2022-01-21T20:38:45+00:00'
updated_at: '2022-01-21T20:38:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
On the [Ubuntu build page](https://xmrig.com/docs/miner/build/ubuntu) of the docs, there's an option for an "advanced build" that compiles some libraries and uses them for a static build.
I've built it in chroots several times, and one of the things I've noticed is that `wget` isn't part of the initial apt install command but is used in the scripts.
I would open a pull request with the fix, but I wasn't able to find a repo or submission page for the docs, so I'm just making an issue here.

# Discussion History
# Action History
- Created by: benthetechguy | 2022-01-21T20:38:45+00:00
