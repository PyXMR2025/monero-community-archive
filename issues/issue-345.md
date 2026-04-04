---
title: ~/log/dr-monero/net directory structure
source_url: https://github.com/monero-project/monero-gui/issues/345
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2016-12-22T22:15:39+00:00'
updated_at: '2016-12-22T23:44:45+00:00'
type: issue
status: closed
closed_at: '2016-12-22T23:44:45+00:00'
---

# Original Description
After testing the [macOS GUI](https://getmonero.org/2016/12/22/monero-core-gui-beta-released.html), I am seeing the following directory structure in my home directory, even **after stopping the application**:
```
log
log/dr-monero
log/dr-monero/net
```
When I remove that `~/log` directory, it just reappears, which is annoying because it clutters up my home directory. Since I was nowhere prompted for this location, it should at least be in a hidden directory.

# Discussion History
## peanutsformonkeys | 2016-12-22T22:59:29+00:00
When I stop my `monerod` daemon (0.10.1.0), I can remove the `~/log` directory. As soon as I restart the daemon, the directory reappears. I haven't noticed this before, so is this a daemon thing since the 0.10.1.0 release?

## peanutsformonkeys | 2016-12-22T23:44:45+00:00
Going to close this issue as apparently it has nothing to do with the Monero Core GUI. Sorry …

# Action History
- Created by: peanutsformonkeys | 2016-12-22T22:15:39+00:00
- Closed at: 2016-12-22T23:44:45+00:00
