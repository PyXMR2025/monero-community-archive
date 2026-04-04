---
title: '[Linux] Latest boost-libs update broke monero-wallet-cli'
source_url: https://github.com/monero-project/monero/issues/3984
author: ElecM8
assignees: []
labels:
- invalid
created_at: '2018-06-11T10:14:39+00:00'
updated_at: '2018-06-11T13:11:23+00:00'
type: issue
status: closed
closed_at: '2018-06-11T10:32:58+00:00'
---

# Original Description
Title's pretty self-explanatory, but boost and boost-libs recently got an update (1.67) and everytime I try to launch monero-wallet-cli I get this error:

`error while loading shared libraries: libboost_chrono.so.1.66.0: cannot open shared object file: No such file or directory`

Downgrading both back to 1.66 fixes the issue.

# Discussion History
## moneromooo-monero | 2018-06-11T10:27:02+00:00
If you update deps, you have to rebuild monero.

+invalid

## ElecM8 | 2018-06-11T13:11:23+00:00
Well, building doesn't work either: https://pastebin.com/vp4WLrkP
Building after downgrading the deps works perfectly though.

# Action History
- Created by: ElecM8 | 2018-06-11T10:14:39+00:00
- Closed at: 2018-06-11T10:32:58+00:00
