---
title: Update Boost
source_url: https://github.com/monero-project/monero/issues/3960
author: jrrcdev
assignees: []
labels: []
created_at: '2018-06-08T15:05:27+00:00'
updated_at: '2018-06-08T18:17:36+00:00'
type: issue
status: closed
closed_at: '2018-06-08T18:17:36+00:00'
---

# Original Description
Please, update boost on windows(Msys) to use the last version(1.67), the last version do not have some files, like thread.hpp that is imported on monero code and we can't install the 1.58 on msys with pacman

# Discussion History
## moneromooo-monero | 2018-06-08T16:36:46+00:00
What commt hash are you running ?

## jrrcdev | 2018-06-08T16:41:20+00:00
Didnt understand, what?

## dEBRUYNE-1 | 2018-06-08T17:41:35+00:00
@jonatanrinckus - Post the output of `monerod.exe --version` here. That will show the commit hash. 

## jrrcdev | 2018-06-08T17:46:49+00:00
I'm trying to compile this source on windows, there is no monerod.exe yet

# Action History
- Created by: jrrcdev | 2018-06-08T15:05:27+00:00
- Closed at: 2018-06-08T18:17:36+00:00
