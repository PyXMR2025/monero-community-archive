---
title: '''Interleaving'' messages seem to slow down accepted hash rate'
source_url: https://github.com/xmrig/xmrig/issues/911
author: lost-bro
assignees: []
labels: []
created_at: '2019-01-16T21:34:13+00:00'
updated_at: '2019-01-17T06:13:33+00:00'
type: issue
status: closed
closed_at: '2019-01-17T06:13:33+00:00'
---

# Original Description
![interleaving](https://user-images.githubusercontent.com/37913805/51279642-610b3980-19a3-11e9-8651-ebfa3b57d879.png)

Checking the hashrate average before and after installing Xmrig-amd-2.9.2 on windows7, I notice a decrease in *accepted* hashes.
My primary concern is *if* the miner is constantly pausing the threads for *x* milliseconds, doesn't that decrease the Total possible Hashes submitted to pool?
This can be seen in the screenshot of miner window.
Is this normal behavior for the "interleaving" message to appear constantly, or is something not adjusted correctly?
The 2.8.3 version of XMRIG did not show these messages.
Can the *interleave* function be turned off?
Please advise.
Thanks

# Discussion History
## xmrig | 2019-01-17T06:13:33+00:00
It was debug messages by mistake got into release. Fixed in v2.9.3.
Thank you.

# Action History
- Created by: lost-bro | 2019-01-16T21:34:13+00:00
- Closed at: 2019-01-17T06:13:33+00:00
