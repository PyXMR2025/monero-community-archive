---
title: Error - couldn't connect to daemon (from RPC) for status command
source_url: https://github.com/monero-project/monero/issues/604
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-01-11T12:23:05+00:00'
updated_at: '2016-10-04T02:39:42+00:00'
type: issue
status: closed
closed_at: '2016-10-04T02:39:42+00:00'
---

# Original Description
I think this is similar to a bug that has been fixed and then unfixed a couple of times. 

http://fpaste.org/309344/51457314/

So, with the old self-compiled binaries (bitmonero v0.8.8.7-0193bfc), I'm able to use "./bitmonerod --bind-rpc-ip (IP ADDRESS) status " to get the status of the daemon. 

With a new compile (Monero 'Hydrogen Helix' (v0.9.0.0-10cc6a8)) and hydrogen helix release, I can't use that command.

Oddly enough, in all versions,  print_cn and diff work.   


# Discussion History
## moneromooo-monero | 2016-02-21T13:57:34+00:00
Works here. Can you try with latest ? Also, you don't need --bind-rpc-ip here.


## Gingeropolous | 2016-10-04T02:39:42+00:00
Pastie dead, and I think this was fixed at some point. 


# Action History
- Created by: Gingeropolous | 2016-01-11T12:23:05+00:00
- Closed at: 2016-10-04T02:39:42+00:00
