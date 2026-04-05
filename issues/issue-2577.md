---
title: XMRIG with a load balancing cluster
source_url: https://github.com/xmrig/xmrig/issues/2577
author: decoderprogrammer
assignees: []
labels: []
created_at: '2021-09-13T10:58:17+00:00'
updated_at: '2025-06-16T20:51:48+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:51:48+00:00'
---

# Original Description
Hi
I want to run xmrig within a load balancing cluster such as docker swarm for cpu and memory sharing in a lan in linux. but when i run it with a docker swarm service or even docker container the xmrig app say me "Failed to apply msr mode ,Hash rate will be low"

what is your suggestion for run xmrig under a load balancing technology? 
thanks


# Discussion History
## decoderprogrammer | 2021-09-14T05:30:58+00:00
it seems to me if I can't put The XMRIG in a cluster ,I must create separated wallet id for each my own systems in my Lan! Otherwise, I have no other way to aggregate all of my LAN systems with One Wallet ID! of course, I was able to do this through docker swarm but with low hash and without MSR mode! 

please Tell my what can I do for resolve my problem?

Thanks

## Spudz76 | 2021-09-14T22:39:19+00:00
What?  You give them all the same wallet ID but use different rig-id or depending on how the pool does rig-id it might be specially formatted into the password string.

## decoderprogrammer | 2021-09-15T10:55:37+00:00
I create a service under docker swarm with a special docker image which run xmrig miner with a wallet id. docker swarm automatically distribute the miner to all of nodes in cluster. Each node starts to mine and send separately through the network. but The only problem is "MSR mode is disable with low hash rate!" message!!

## Lonnegan | 2021-09-16T06:36:25+00:00
To apply the MSR mod xmrig needs direct access to the hardware with full rights. That's not the case in virtualized oder "dockered" environments.

# Action History
- Created by: decoderprogrammer | 2021-09-13T10:58:17+00:00
- Closed at: 2025-06-16T20:51:48+00:00
