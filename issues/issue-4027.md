---
title: Allow local monerod server when using Socks5 proxy
source_url: https://github.com/monero-project/monero-gui/issues/4027
author: zquestz
assignees: []
labels: []
created_at: '2022-09-09T22:09:11+00:00'
updated_at: '2023-01-11T17:16:37+00:00'
type: issue
status: closed
closed_at: '2023-01-11T17:16:37+00:00'
---

# Original Description
Currently there is no way to connect to a local monerod instance and have all other connections go over the Socks5 proxy. When the Socks5 proxy is set, you lose connection to your local node. Many users will want to make sure price discovery is happening over Tor, and that is not currently possible when connecting to your own local monerod instance.

![image](https://user-images.githubusercontent.com/83898/189452150-8fbb116a-0093-4273-88c8-e5831e61e4d5.png)

Ideally we can add a check box that allows it to bypass the proxy for local connections.

![image](https://user-images.githubusercontent.com/83898/189452455-28574380-b814-4e10-bcd7-b38404825738.png)

I wouldn't mind looking into adding it, as long as that is something that would be accepted.

# Discussion History
## plowsof | 2022-12-18T04:10:51+00:00
Confirmed issue:
- ./monerod
- point wallet at localhost:18081 (connected)
- enable socks5 proxy 
- note the disconnection from localnode
`Some problems at connect, message: Socks request rejected or failed`

## selsta | 2022-12-18T13:14:39+00:00
This does work by selecting "Local node" inside Settings -> Node with socks5 proxy enabled.

## plowsof | 2022-12-18T14:12:09+00:00
Confirmed this fixes the problem, thanks! 

# Action History
- Created by: zquestz | 2022-09-09T22:09:11+00:00
- Closed at: 2023-01-11T17:16:37+00:00
