---
title: Disable GUI until wallet is fully loaded
source_url: https://github.com/monero-project/monero-gui/issues/68
author: Jaqueeee
assignees: []
labels: []
created_at: '2016-10-16T15:44:55+00:00'
updated_at: '2016-11-06T09:53:02+00:00'
type: issue
status: closed
closed_at: '2016-11-06T09:53:02+00:00'
---

# Original Description
if I click on the receive tab instantly after opening a wallet this happens (se image). The buttons in left panel should be disabled until wallet is fully loaded. 
see: https://github.com/monero-project/monero-core/blob/master/main.qml#L403

![skarmavbild 2016-10-16 kl 17 42 11](https://cloud.githubusercontent.com/assets/5909557/19418619/ec922180-93c7-11e6-99d2-21ed5e29e6a6.png)


# Discussion History
## Jaqueeee | 2016-10-16T15:46:21+00:00
If i switch to another tab and then return to the receive page the addresses are there. 


## medusadigital | 2016-10-16T20:49:39+00:00
Disabling The Tab until the daemon is synced is probably not the best idea @Jaqueeee, since long term we still want the user to be able to generate addresses offline without being synced/having the chain


## taushet | 2016-10-28T19:02:31+00:00
@medusadigital, we can have an offline mode in the future.

In the short term, this is needed, as otherwise people will lose their minds not understanding why things are not working.


# Action History
- Created by: Jaqueeee | 2016-10-16T15:44:55+00:00
- Closed at: 2016-11-06T09:53:02+00:00
