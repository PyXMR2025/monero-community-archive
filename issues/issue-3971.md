---
title: Would it be possible to mine in p2pool while being in Compatible Monero Remote
  Nodes?
source_url: https://github.com/monero-project/monero-gui/issues/3971
author: vladimirzb
assignees: []
labels: []
created_at: '2022-07-15T01:42:54+00:00'
updated_at: '2022-07-15T22:42:26+00:00'
type: issue
status: closed
closed_at: '2022-07-15T09:30:15+00:00'
---

# Original Description
Hi Everyone! First of all, thanks to the contributors and the comnunity of monero for maintaining this project. If I am not mistaken, p2pool has Remote nodes available when connected you can mine (https://xmrvsbeast.com/p2pool/monero_nodes.html). But when connected to these nodes in the monero gui, it appears a message saying that "Mining is only available on local demons", shouldn't it be possible to make compatible these remote nodes to the monero gui with p2pool? This would be very useful for people who doesnt have a lot of disk space for a local deamon. I agree that local deamons are the most secure way to maintain the monero network but for some people it isn't possible, and I think it could be good for monero to get as many as people to maintain the blockchain in p2pool so it is more decentralized. Sorry if my proposal is dumb I am kinda new to this project but I felt this could help the monero community :D

# Discussion History
## selsta | 2022-07-15T09:30:15+00:00
See this comment: https://github.com/monero-project/monero-gui/pull/3829#issuecomment-1043169556

You have to add `--host` to the startup flags and the remote node must have zmq enabled.

## vladimirzb | 2022-07-15T22:42:25+00:00
> See this comment: [#3829 (comment)](https://github.com/monero-project/monero-gui/pull/3829#issuecomment-1043169556)
> 
> You have to add `--host` to the startup flags and the remote node must have zmq enabled.

Thank you so much :D!

# Action History
- Created by: vladimirzb | 2022-07-15T01:42:54+00:00
- Closed at: 2022-07-15T09:30:15+00:00
