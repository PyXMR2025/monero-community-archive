---
title: canceling stuck tx
source_url: https://github.com/monero-project/monero-gui/issues/3407
author: ZuckaBoy
assignees: []
labels: []
created_at: '2021-04-17T14:26:23+00:00'
updated_at: '2021-04-19T16:38:31+00:00'
type: issue
status: closed
closed_at: '2021-04-19T16:38:31+00:00'
---

# Original Description
hello, i sent a tx which showed as failed in To: tab, coins goes back to my wallet so i sent it again, after second sending the first sending goes through and confirmed, the second send is still on pending situation but shows failed in To: tab.  how can i cancel the second one? i dont have enough coins to cover the second one but i am afraid that when i have then this one goes through too. i need to cancel it so this dont happen, the tx id isnt still on blockchain. 

my version is: 0.17.1.9-3ca5f10f (Qt 5.15.2)
windows: 10
no tor
remote node



# Discussion History
## selsta | 2021-04-19T16:38:31+00:00
The tx will time out automatically.

> i dont have enough coins to cover the second one but i am afraid that when i have then this one goes through too.

This will not happen.

# Action History
- Created by: ZuckaBoy | 2021-04-17T14:26:23+00:00
- Closed at: 2021-04-19T16:38:31+00:00
