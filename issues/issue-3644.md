---
title: couldn't find zmq.hpp (FreeBSD)
source_url: https://github.com/monero-project/monero/issues/3644
author: monerorus
assignees: []
labels: []
created_at: '2018-04-15T16:15:08+00:00'
updated_at: '2018-04-24T15:57:24+00:00'
type: issue
status: closed
closed_at: '2018-04-24T15:57:24+00:00'
---

# Original Description
If you have error about zmq on FreeBSD while building from source, then you need install port **net/cppzmq**.  
Where is few ports about zmq(net/czmq, net/libzmq3, net/libzmq4 and etc.), but you need just **net/cppzmq**
Tested on FreeBSD 10.3

# Discussion History
## moneromooo-monero | 2018-04-16T09:53:13+00:00
I'm not sure what the bug is here.
If you're reporting which exact package is needed for FreeBSD, then there is a list in README.md which gives that list for some OSes, and you could add FreeBSD to the list along with the exact packages for each dep.

## monerorus | 2018-04-22T12:35:46+00:00
Are you about PR changes in README.md file?
You right, this is not a bug issue, just for info.

# Action History
- Created by: monerorus | 2018-04-15T16:15:08+00:00
- Closed at: 2018-04-24T15:57:24+00:00
