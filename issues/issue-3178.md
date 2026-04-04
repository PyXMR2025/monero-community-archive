---
title: --data-dir isn't passed correctly by start-gui.sh (becomes --datadir)
source_url: https://github.com/monero-project/monero/issues/3178
author: mdPlusPlus
assignees: []
labels: []
created_at: '2018-01-24T17:49:20+00:00'
updated_at: '2018-01-24T17:58:06+00:00'
type: issue
status: closed
closed_at: '2018-01-24T17:55:18+00:00'
---

# Original Description
~~My way to start Monero GUI (`monero.sh` in the parent folder):  
`./monero-gui-v0.11.1.0/start-gui.sh --data-dir ./bitmonero`  
(notice the hypen between "data" and "dir")~~

~~Error message when starting via my `monero.sh`:~~  
> Failed to parse arguments: unrecognised option '--datadir'

~~Somehow `--data-dir` becomes `--datadir` and refuses to work.  
When I set the option in the GUI though, it works.~~

~~My system:  
Ubuntu 17.10 x86_64, monero-linux-x64-v0.11.1.0.tar.bz2~~

**EDIT:**  
Okay, apparently start-gui.sh isn't passing the parameter at all and the --datadir was a previous setting I tried in the GUI. Sorry for not checking that before opening the issue.

# Discussion History
# Action History
- Created by: mdPlusPlus | 2018-01-24T17:49:20+00:00
- Closed at: 2018-01-24T17:55:18+00:00
