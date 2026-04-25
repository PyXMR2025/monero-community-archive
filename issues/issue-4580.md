---
title: Monero GUI cannot be moved to second monitor
source_url: https://github.com/monero-project/monero-gui/issues/4580
author: eth0fox
assignees: []
labels: []
created_at: '2026-04-22T05:20:59+00:00'
updated_at: '2026-04-23T17:05:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After installing Monero GUI on macOS 15.7.5, the application launched on my laptop monitor, and attempts to move it onto my external display simply leave it trapped on the laptop display.

https://github.com/user-attachments/assets/22e3c85a-baf1-45eb-8dc1-b2a8b8eb6596

```
GUI version: 0.18.4.7-release (Qt 5.15.13)
Embedded Monero version: 0.18.4.6-dbcc7d212
Wallet restore height: 1996468
Wallet mode: Simple mode
Graphics mode: OpenGL
```

# Discussion History
## selsta | 2026-04-22T17:20:41+00:00
Could you go to Settings -> Interface and disable custom decorations? Does it make it difference?

## eth0fox | 2026-04-23T03:37:34+00:00
Yes, if you disable custom decorations its allowed to move. If you switch them back on it snaps back to the original monitor

# Action History
- Created by: eth0fox | 2026-04-22T05:20:59+00:00
