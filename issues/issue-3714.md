---
title: XMRig not mining after updating Tari Universe 1.6.2
source_url: https://github.com/xmrig/xmrig/issues/3714
author: ELIGNOTICO
assignees: []
labels: []
created_at: '2025-09-26T13:40:38+00:00'
updated_at: '2025-09-27T01:43:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Since updating to Tari Universe 1.6.2, XMRig runs normally but does not perform effective mining. The share counter does not increase, and no valid shares are submitted.

**Steps to reproduce**
1. Update Tari Universe to version 1.6.2
2. Launch XMRig with the same configuration as before
3. Observe that the miner runs but no shares are accepted

**Expected behavior**
XMRig should continue to submit valid shares after the update.

**System information**
- OS: Windows 10/11 (please specify exact version)
- CPU: AMD Ryzen 9 9950X (16 cores / 32 threads)
- XMRig version: 1.6.2
- Pool: Tari Universe (merged mining setup)
- Config: using standard config.json and .bat file (can provide if needed)

**Additional context**
Mining was working correctly with version 1.6.1. After the 1.6.2 update, the issue appeared.



# Discussion History
## SChernykh | 2025-09-26T15:31:25+00:00
How is it an XMRig bug and not Tari Universe bug?

## ELIGNOTICO | 2025-09-26T17:20:29+00:00
> ¿Cómo es un error XMRig y no un error de Tari Universe?

Honestly, I’m not sure whose error this might be. I initially reported it on both sites in case it’s an issue on both ends. My XMRig is working correctly, but the amount of Tari XTM I’m receiving hasn’t increased; the token balance hasn’t updated for over 13 hours.

## geekwilliams | 2025-09-27T01:43:12+00:00
Sounds like a Tari bug, not an issue with xmrig.   

# Action History
- Created by: ELIGNOTICO | 2025-09-26T13:40:38+00:00
