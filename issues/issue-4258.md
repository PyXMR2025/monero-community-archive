---
title: Flatpak hash doesn't match
source_url: https://github.com/monero-project/monero-gui/issues/4258
author: marqusat
assignees: []
labels: []
created_at: '2023-12-28T14:23:07+00:00'
updated_at: '2023-12-29T10:28:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've run the command at the bottom of:
https://github.com/monero-project/monero-gui/actions/runs/6473857113
and I'm getting a different hash:
```
$ flatpak run --command=sha256sum org.getmonero.Monero /app/bin/monero-wallet-gui
446b674e2c86533933ce32ac817b7d3583ba4582136aa4afdfb25b48b7a445c5  /app/bin/monero-wallet-gui
```
not matching the one from the list linked above:
```
fbb25109d7c59cb6620e056030a1678e73112d259a87bd3b934f1d139896dfac  monero-wallet-gui
```
Please advise what can be wrong.

# Discussion History
## selsta | 2023-12-29T01:34:28+00:00
@BigmenPixel0 

## q7nm | 2023-12-29T10:28:32+00:00
That hash isn't correct for now. Monero-gui hasn't been pushed to Flathub from Github Actions yet. 

# Action History
- Created by: marqusat | 2023-12-28T14:23:07+00:00
