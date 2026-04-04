---
title: sync issue in gui
source_url: https://github.com/monero-project/monero-gui/issues/999
author: lasergoat
assignees: []
labels:
- invalid
created_at: '2017-12-07T20:57:26+00:00'
updated_at: '2018-01-11T15:54:42+00:00'
type: issue
status: closed
closed_at: '2018-01-11T15:54:42+00:00'
---

# Original Description

![monero-sync-issue](https://user-images.githubusercontent.com/15964/33734781-07a7fb42-db53-11e7-824b-02638fca11c5.gif)

It just keeps showing a small number like 20, 40 or 60 blocks and then switching to 53,000 or so.

Is this normal?

# Discussion History
## medusadigital | 2017-12-08T08:26:30+00:00
this can happen once or twice, but shouldnt be something you can reproduce or see regulary. 

it happens like this afaik: your node doesnt know the top block of the chain, it only knows what other nodes tell it is the top block. So depending on which other nodes your node talks to...that number can eventually change during sync process. 



## dEBRUYNE-1 | 2017-12-08T10:17:58+00:00
Can you try this guide?

https://monero.stackexchange.com/questions/6651/my-gui-feels-buggy-freezes-all-the-time

## medusadigital | 2018-01-11T13:30:38+00:00
closing here, issue not reproduceable. 


## medusadigital | 2018-01-11T13:30:46+00:00
+invalid

# Action History
- Created by: lasergoat | 2017-12-07T20:57:26+00:00
- Closed at: 2018-01-11T15:54:42+00:00
