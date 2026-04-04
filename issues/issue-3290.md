---
title: Seed Recovery
source_url: https://github.com/monero-project/monero-gui/issues/3290
author: sainta13
assignees: []
labels: []
created_at: '2021-01-02T21:38:21+00:00'
updated_at: '2021-01-19T20:48:50+00:00'
type: issue
status: closed
closed_at: '2021-01-19T20:48:50+00:00'
---

# Original Description
I'm having an issue getting my 25 seed. I've found this page 

https://github.com/LedgerHQ/app-monero/tree/master/tools/python#requirements

but I have little to know python knowledge. I'm stuck on the requirements and how to add them to my mac. then where to enter the commands. 

# Discussion History
## jarjarfan666 | 2021-01-19T20:30:35+00:00
That's a command for Linux. You need to look at the command for OSX and use iterm. I don't use OSX, so can't help

This isn't an issue with monero-gui. I recommend opening a ticket on that repo.

## selsta | 2021-01-19T20:48:50+00:00
@sainta13 try opening Terminal and then entering to following line by line:

```
pip3 install readline
pip3 install pycryptodomex
pip3 install ECPy
pip3 install ledgerblue
git clone https://github.com/LedgerHQ/app-monero
cd app-monero/tools/python
PYTHONPATH=`pwd`/src  python3 -m ledger.monero.seedconv.py offline
```


# Action History
- Created by: sainta13 | 2021-01-02T21:38:21+00:00
- Closed at: 2021-01-19T20:48:50+00:00
