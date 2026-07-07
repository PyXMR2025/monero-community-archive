---
title: New feature request
source_url: https://github.com/xmrig/xmrig/issues/3828
author: ziorick
assignees: []
labels: []
created_at: '2026-07-05T08:11:35+00:00'
updated_at: '2026-07-05T08:11:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi to all! I use the 6.26.0 version, on various CPU via the proxy. It run perfectly!
I think that may be useful an indication about the "real" difficult for the accepted share.
[2026-07-05 10:09:18.104]  net      new job from 192.168.2.20:3333 diff 106095 algo rx/0 height 3711087 (21 tx)
[2026-07-05 10:09:23.149]  cpu      accepted (3760/0) diff 106095 (172 ms)

The pool request >106095, a share was accepted but... the real diff/value? The Top10 show something but not all:
 - RESULTS
 * accepted         3760 (100.0%)
 * pool-side hashes 401290199 avg 106726
 * difficulty       106066
 * avg result time  36.8s
 - TOP 10
  # | DIFFICULTY | EFFORT % |
  1 |       201M |   198.80 |
  2 |       163M |   245.57 |
  3 |       124M |   321.88 |
  4 |       111M |   360.01 |
  5 |     81551K |   492.07 |
  6 |     72058K |   556.90 |
  7 |     37396K |  1073.08 |
  8 |     36661K |  1094.58 |
  9 |     36336K |  1104.36 |
 10 |     33934K |  1182.54 |


Does anyone think about it?

# Discussion History
# Action History
- Created by: ziorick | 2026-07-05T08:11:35+00:00
