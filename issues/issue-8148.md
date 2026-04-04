---
title: Where is the blockchain file stored at? (NAB)
source_url: https://github.com/monero-project/monero/issues/8148
author: TimyIsCool
assignees: []
labels: []
created_at: '2022-01-18T16:21:52+00:00'
updated_at: '2022-01-20T06:12:10+00:00'
type: issue
status: closed
closed_at: '2022-01-18T16:22:56+00:00'
---

# Original Description
I was wondering where the blockchain file is, I need to delete it because i have no space left on my ssd

# Discussion History
## selsta | 2022-01-18T16:22:56+00:00
~/.bitmonero/lmdb/data.mdb

## TimyIsCool | 2022-01-18T16:53:36+00:00
> ~/.bitmonero/lmdb/data.mdb

Thank you, anyway to move it to a different folder to a different disk?

## selsta | 2022-01-18T16:54:33+00:00
Use the `--data-dir` flag when starting monerod.

## TimyIsCool | 2022-01-18T17:00:15+00:00
> 

ty

## TimyIsCool | 2022-01-19T21:52:43+00:00
> Use the `--data-dir` flag when starting monerod.

What is the size of the blockchain file?

## selsta | 2022-01-20T06:12:10+00:00
~ 110GB, 40GB pruned

# Action History
- Created by: TimyIsCool | 2022-01-18T16:21:52+00:00
- Closed at: 2022-01-18T16:22:56+00:00
