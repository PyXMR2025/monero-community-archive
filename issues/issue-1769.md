---
title: Bestshare
source_url: https://github.com/xmrig/xmrig/issues/1769
author: needhelp101
assignees: []
labels:
- bug
- kawpow
created_at: '2020-07-10T10:46:59+00:00'
updated_at: '2021-04-12T14:54:01+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:54:01+00:00'
---

# Original Description
Hi,

Bit confused in the bestshare display for kawpow... so for example while mining Raven i get 

- TOP 10
  # | DIFFICULTY | EFFORT % |
  1 |       140G |    27.60 |
  2 |     18700M |   206.71 |
  3 |     10392M |   371.96 |
  4 |      9487M |   407.44 |
  5 |      6181M |   625.39 |
  6 |      5656M |   683.37 |
  7 |      5598M |   690.50 |
  8 |      4774M |   809.58 |
  9 |      4502M |   858.47 |

now what size would my bestshare need to be in order to secure a block ???

# Discussion History
## needhelp101 | 2020-07-10T10:56:06+00:00
the display system of the bestshare is bit confusing

## xmrig | 2020-07-10T11:40:00+00:00
Seems need to add a special case for Raven, unlike all other coins it does not use absolute difficulty.
Thank you.


# Action History
- Created by: needhelp101 | 2020-07-10T10:46:59+00:00
- Closed at: 2021-04-12T14:54:01+00:00
