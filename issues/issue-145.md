---
title: '"Low Difficulty share" '
source_url: https://github.com/xmrig/xmrig/issues/145
author: ChildishJack
assignees: []
labels: []
created_at: '2017-10-09T22:38:40+00:00'
updated_at: '2017-10-15T09:23:58+00:00'
type: issue
status: closed
closed_at: '2017-10-15T09:23:58+00:00'
---

# Original Description
I'm getting all shares rejected by minexmr for "Low Difficulty share". I'm running xmrig

`./xmrig -o pool.minexmr.com:3333 -u me4real.computer -p x -k -a cryptonight-lite --donate-level=1 -t 4 >> hello.txt
jack@xserve2:~/xmrig/build$ ./xmrig -o pool.minexmr.com:3333 -u me4real.computer -p x -k -a cryptonight-lite -t 4`

Ubuntu 16.04 Server, libuv/1.15.1-dev, gcc/5.4.0. The default difficulty on that port worked on the system in the past. Any ideas?

# Discussion History
## xmrig | 2017-10-09T22:41:56+00:00
Please remove `-a cryptonight-lite`. This option must be used only with AEON pools.
Thank you.

# Action History
- Created by: ChildishJack | 2017-10-09T22:38:40+00:00
- Closed at: 2017-10-15T09:23:58+00:00
