---
title: Latest build doesn't detect connected daemon
source_url: https://github.com/monero-project/monero-gui/issues/290
author: ghost
assignees: []
labels: []
created_at: '2016-12-15T20:27:11+00:00'
updated_at: '2016-12-17T01:19:49+00:00'
type: issue
status: closed
closed_at: '2016-12-17T01:19:49+00:00'
---

# Original Description
If I log in, the daemon starts but the GUI shows that it's disconnected. If I click "Start Daemon", the Initializing Daemon window pops up and just spins. If I look at the Daemon Log, it shows that it tried starting the daemon a second time, even though it's already running, so that's why starting it failed.

![screen shot 2016-12-15 at 3 21 22 pm](https://cloud.githubusercontent.com/assets/21302237/21240810/e418708a-c2da-11e6-8c79-1d44908b41b1.png)

In picture above, you can see the daemon log shows the daemon has connected, but the GUI in the bottom left still says Disconnected. (OSX 10.12.2)


# Discussion History
## Jaqueeee | 2016-12-16T01:52:51+00:00
https://github.com/monero-project/monero-core/pull/291

# Action History
- Created by: ghost | 2016-12-15T20:27:11+00:00
- Closed at: 2016-12-17T01:19:49+00:00
