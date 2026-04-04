---
title: monerod and monero-wallet-gui don't use the same directory with data-dir
source_url: https://github.com/monero-project/monero/issues/6195
author: goin2mars
assignees: []
labels: []
created_at: '2019-11-29T13:19:17+00:00'
updated_at: '2019-12-09T19:22:18+00:00'
type: issue
status: closed
closed_at: '2019-12-09T19:22:18+00:00'
---

# Original Description
Hi not sure if this is intended behavior or not. Using ./monerod --data-dir 'path' makes a folder 'lmdb' to put the db into and monero-wallet-gui set to go to the same path as the data-dir goes into 'LMDB'. I'd attempted to rename the folder, but long story short here I'm re-downloading the entire blockchain because I've since inadvertently deleted the wrong folder so I wasn't able to verify if renaming one to the other and feeding it to the other program will work. Using linux, monero 0.15.0.1

# Discussion History
## moneromooo-monero | 2019-11-29T15:00:20+00:00
Not intended. The GUI setting is passed to monerod though, which makes the case switch puzzling.

## goin2mars | 2019-12-09T19:22:18+00:00
Turns out I've done this to myself. I'd decided it was smart to name the chains intended resting place to be descriptive yet not actually say monero and also not be more than a word long and in stupidity settled on 'LMDB' and named the folder that myself then continued to be confused for a bit.

# Action History
- Created by: goin2mars | 2019-11-29T13:19:17+00:00
- Closed at: 2019-12-09T19:22:18+00:00
