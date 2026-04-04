---
title: 'why monero deleting files repos ? '
source_url: https://github.com/monero-project/monero/issues/3744
author: mountandlaser
assignees: []
labels:
- invalid
created_at: '2018-05-02T01:58:39+00:00'
updated_at: '2018-05-02T02:22:09+00:00'
type: issue
status: closed
closed_at: '2018-05-02T02:22:09+00:00'
---

# Original Description
hello im developing cryptonote i have a lot of monero repos, why monero deleting or changing some files ? 5f09d6c8333b0b0d07252dc157b9e794f6278662 hope fluffypony remember this file, i guess this is real open source file on monero project but seems like deleted community 

# Discussion History
## danrmiller | 2018-05-02T02:09:47+00:00
Instead of maintaining external/unbound, a git submodule is now used. That repository is here:
https://github.com/monero-project/unbound

The README was updated to indicate you now need to clone with the --recursive flag or init and update the submodule. See https://github.com/monero-project/monero#cloning-the-repository



## mountandlaser | 2018-05-02T02:17:10+00:00
okay fine, https://github.com/monero-classic-project/monero-classic ? is that lightest unbugged asic supported monero forks repos ? 

## danrmiller | 2018-05-02T02:20:15+00:00
This is the issue tracker for potential bugs in Monero and not for questions about forks.

+invalid

# Action History
- Created by: mountandlaser | 2018-05-02T01:58:39+00:00
- Closed at: 2018-05-02T02:22:09+00:00
