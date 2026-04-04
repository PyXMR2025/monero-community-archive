---
title: Automatic dev donation not working on mainnet
source_url: https://github.com/monero-project/monero-gui/issues/29
author: medusadigital
assignees: []
labels: []
created_at: '2016-09-20T16:39:28+00:00'
updated_at: '2016-11-06T09:59:26+00:00'
type: issue
status: closed
closed_at: '2016-11-06T09:59:26+00:00'
---

# Original Description
When sending a transaction with monero-core on mainnet, the dev donation is not sent out, even if enabled. 
![nodevdonation](https://cloud.githubusercontent.com/assets/17108301/18679772/57f08f8c-7f61-11e6-9113-d55782f04fa6.jpg)

i sent 1.5 xmr from monero-core ubuntu to my simplewallet on windows.

1.0 and 0.5 is my transaction
0.09 and 0.4 is my change

the dev donation is missing, which is configured for 50% of the transaction fee (in this example that would be 0.005)

--> Ubuntu 16.04 on mainnet together with pull request #23


# Discussion History
## Jaqueeee | 2016-10-30T20:24:57+00:00
no implemented yet. Removed page in https://github.com/monero-project/monero-core/pull/93


## medusadigital | 2016-11-06T09:59:26+00:00
feature disabled for now ---> closed


# Action History
- Created by: medusadigital | 2016-09-20T16:39:28+00:00
- Closed at: 2016-11-06T09:59:26+00:00
