---
title: Most recent TX shows '%n seconds ago'
source_url: https://github.com/monero-project/monero-gui/issues/3284
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-12-27T17:07:45+00:00'
updated_at: '2025-11-15T20:10:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Screenshot](https://i.imgur.com/tfjC8wc.png)

This is on GUI installer version 0.17.1.7 on Windows 10 with "Human readable date format" enabled. I think I've seen this a couple of times in previous versions but am just now getting to filing a report.

The general flow that seems to make this issue occur is, you're already on the Transactions screen when a new transaction appears. It initially says '0 seconds ago' and stays that way until confirmed, when it switches to '%n seconds ago'. Switching away from and back to transactions page does not fix. Issue corrects itself after a few minutes and thereafter displays the correct "date".

# Discussion History
## xiphon | 2021-01-15T10:48:40+00:00
What OS do you use? Please test it with v0.17.1.9 and report back the results.

## MoneroArbo | 2021-01-15T13:34:51+00:00
I use Windows 10, but a couple days ago in #monero there was a person reporting the problem on Debian using v0.17.1.9. Main difference is they were reporting it for a sent transaction, whereas I saw it for a received transaction.

## nabijaczleweli | 2025-11-15T20:10:45+00:00
I repro this pretty consistently on freshly-sent transactions:

<img width="980" height="313" alt="Image" src="https://github.com/user-attachments/assets/0c4c7844-edd2-4f88-b538-f6578aa52f80" />

It fixes itself after up to a minute. I suspect this happens because the transaction is timestamped in the future vs my local clock, so the relative date becomes negative, which doesn't work somehow.

# Action History
- Created by: MoneroArbo | 2020-12-27T17:07:45+00:00
