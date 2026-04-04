---
title: 30% CPU in Debian buster based VirtualBox VM
source_url: https://github.com/monero-project/monero-gui/issues/2880
author: adrelanos
assignees: []
labels: []
created_at: '2020-05-02T13:41:36+00:00'
updated_at: '2022-11-15T23:11:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I also have 30% CPU using monero GUI `v0.15.0.4` in a VirtualBox VM (Whonix-Workstation). It's just the first screen (language selection screen). No monero installed ever in that VM before.

Already using `QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui` (which reduced CPU use from 100% to now 30%) (which is discussed separately in https://github.com/monero-project/monero-gui/issues/2878).

30% CPU use for monero-gui language selection screen seems still very much.

# Discussion History
## selsta | 2020-05-02T13:44:19+00:00
Can you try to compile with Qt 5.14?

## adrelanos | 2020-05-02T14:02:30+00:00
Sounds difficult.

How would I do that?

Do you have any build with Qt 5.14?

## mmortal03 | 2022-11-15T23:11:19+00:00
Was this ever resolved?

# Action History
- Created by: adrelanos | 2020-05-02T13:41:36+00:00
