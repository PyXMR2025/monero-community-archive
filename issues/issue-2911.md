---
title: 'Mining ghostrider algo to daemon yields "connect error: Invalid Wallet Address"'
source_url: https://github.com/xmrig/xmrig/issues/2911
author: downystreet
assignees: []
labels: []
created_at: '2022-01-31T10:36:10+00:00'
updated_at: '2022-02-01T01:13:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Starting xmrig to mine Butkoin with daemon true, algo 'ghostrider', and url to 127.0.0.1:9998 yields "connect error: Invalid Wallet Address". The same wallet address will work when mining to a Butkoin pool.

**To Reproduce**
Mine with algo ghostrider to local daemon.

**Expected behavior**
It should start mining to daemon.

**Required data**
"connect error: Invalid Wallet Address"
OS: Fedora 35

**Additional context**
I set the Butkoin daemon algo to ghostrider. It is possible that my Butkoin node is misconfigured as the cli is rather complicated but I think it is configured correctly and this is something to do with xmrig. There is no problem mining to a pool, only when trying to mine to local daemon.

Update: When mining to a pool xmrig starts doing the work but when a block is found by the pool it shows the work done and my payment amount but is giving status invalid for payout.

# Discussion History
## downystreet | 2022-02-01T00:52:18+00:00
I've gotten more information and apparently my wallet address is showing up as the user name in the pool. I have the wallet address in the "user": walletaddress but it is showing in the pool as the worker name. There is something crossed up in xmrig. This is probably why the daemon is saying invalid address as well. I'm using xmrig version 6.16.3. I will also add that I am configuring it from the config.json file and have not tried using the command line instructions. I have tried using the command line and also tried using the next two versions before this one and they all do the same thing.

# Action History
- Created by: downystreet | 2022-01-31T10:36:10+00:00
