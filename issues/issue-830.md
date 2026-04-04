---
title: issue Ubuntu 16.04.2 LTS, bug in minimalized iface.
source_url: https://github.com/monero-project/monero-gui/issues/830
author: oshep
assignees: []
labels:
- resolved
created_at: '2017-08-22T11:31:55+00:00'
updated_at: '2018-11-18T15:54:33+00:00'
type: issue
status: closed
closed_at: '2018-11-18T15:54:33+00:00'
---

# Original Description
Steps to reproduce:
1. loggin into a wallet A.
2. Do something with balance.
3. Switch to a minimalized mode. (press arrow in the left top corner)
4. Close the wallet A.
5. Restore some wallet B.
6. During of syncronization, switch to minimalized mode.
![screenshot from 2017-08-22 13-58-16](https://user-images.githubusercontent.com/31243056/29563118-e019a2f4-8744-11e7-8195-72c7c6f478b9.png)

7. In this window, you will see balance from the prewious logged wallet. 
![screenshot from 2017-08-22 13-58-28](https://user-images.githubusercontent.com/31243056/29563119-e032b000-8744-11e7-99ad-988a0d10a2b3.png)

Ubuntu 16.04.2 LTS
monero-gui-0.10.3.1-beta2

Best regards, oshep.

# Discussion History
## erciccione | 2018-11-18T13:51:24+00:00
Related to old version and old theme. Reopen if problem still exists

+resolved

# Action History
- Created by: oshep | 2017-08-22T11:31:55+00:00
- Closed at: 2018-11-18T15:54:33+00:00
