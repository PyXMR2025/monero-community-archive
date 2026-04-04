---
title: Log only connects to localhost
source_url: https://github.com/monero-project/monero-gui/issues/3020
author: peterlgarland
assignees: []
labels: []
created_at: '2020-07-22T16:49:05+00:00'
updated_at: '2021-04-21T02:18:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I run the monerod daemon on a virtual machine on my server and connect to it from my PC on the local network, so I open the Monero Wallet, go to Settings and Node, And Connect to my node on the server.

But, if I then go to Log, and enter a command like status, it's sending it to the not running localhost daemon, not the IP address of the Node I'm connected to. Can you adjust the Log commands so they send to the remote node it's connected to?



# Discussion History
## selsta | 2021-04-21T02:18:24+00:00
We have now disabled the sending commands option in remote node mode. I know, not exactly what is suggested here.

# Action History
- Created by: peterlgarland | 2020-07-22T16:49:05+00:00
