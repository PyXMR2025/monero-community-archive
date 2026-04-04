---
title: Some seed nodes can not be connected
source_url: https://github.com/monero-project/monero/issues/5314
author: TC0057
assignees: []
labels: []
created_at: '2019-03-19T13:32:52+00:00'
updated_at: '2022-02-22T21:30:39+00:00'
type: issue
status: closed
closed_at: '2022-02-22T21:30:39+00:00'
---

# Original Description
Hello,

In past few weeks, I tried to connect to eight hardcoded seed nodes (212.83.175.67  163.172.182.165  212.83.172.165  107.152.130.98  5.9.100.248  198.74.231.92  161.67.132.39  195.154.123.123) by using "--add-exclusive-node". However, I found that 5 seed nodes (107.152.130.98  5.9.100.248  198.74.231.92  161.67.132.39  195.154.123.123) can not be reached. Precisely, three unreached seed nodes (107.152.130.98 5.9.100.248 198.74.231.92) did not reply ping command, and two unreached seed nodes (161.67.132.39 195.154.123.123) did reply.

My question is:
Are these unreached seed nodes still working? If they are working, why my node can not connect with them?

Thanks in advance!



# Discussion History
## fluffypony | 2019-03-19T14:11:23+00:00
Many of the seed nodes are configured not to respond to ICMP traffic so you can ignore the ping responses. I've messaged the people that I know that run some of the unresponsive nodes, so hopefully a few more should be responsive. We can do a full run through them closer to the next release and replace those that are truly no longer operational. In reality you only need to connect to 1 during initial sync to get its peer-list, so if a few of them are down it's not a big deal.

## TC0057 | 2019-03-19T16:37:08+00:00
@fluffypony  thank you very much.
 It seems, so far, every new participant can receive peer-list from these three available seed nodes to initiative its connections. But, considering about network congestion, network scalability, and server's capacity, three available hardcoded seed nodes are not enough to afford all initialization requests in the future. 
For these unreachable seed nodes, is it possible that some of them are fully connected? Because they have reached the maximum number of connections, so we can not connect with them. If this is true, then other three available seed nodes are going to be fully connected soon. If there is no any fully connected seed node, then three available seed nodes are adequate so far.


## fluffypony | 2019-03-19T16:41:59+00:00
This a backup discovery mechanism, the primary discovery mechanism is DNS seeds.

All of the backup seed nodes allow a large number of connections, and leave a large buffer untouched for peerlist requests, so it’s unrelated. I’ve confirmed that two of the five unreachable seed nodes are permanently gone, one is being reinstalled, one is up but has a routing issue of some sort, and one I can’t get hold of the owner.

## erciccione | 2020-07-23T08:11:09+00:00
I would say this can be closed after #6571 is merged.

# Action History
- Created by: TC0057 | 2019-03-19T13:32:52+00:00
- Closed at: 2022-02-22T21:30:39+00:00
