---
title: wallet not use/known https connect to the node!?
source_url: https://github.com/monero-project/monero-gui/issues/1480
author: minzak
assignees: []
labels: []
created_at: '2018-06-29T16:46:54+00:00'
updated_at: '2021-07-02T01:22:33+00:00'
type: issue
status: closed
closed_at: '2021-07-02T01:22:33+00:00'
---

# Original Description
I run my own monero node and it works wit my mobile wallet in usual http mode.

I use node as backend with nginx.
And i see that wallet not use or can't use https, when i use https on nginx.
It is something wrong in my wallet? Or wallet still weak?

![image](https://user-images.githubusercontent.com/12154217/42104267-9972604a-7bd4-11e8-8a86-371cf659cf3d.png)



# Discussion History
## selsta | 2021-07-02T01:22:33+00:00
By default the GUI will connect using SSL if the daemon has --rpc-ssl auto / enabled.

# Action History
- Created by: minzak | 2018-06-29T16:46:54+00:00
- Closed at: 2021-07-02T01:22:33+00:00
