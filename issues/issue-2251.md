---
title: Monero-wallet-CLI slow exit when attempting to connect to dead / nonexistent
  daemon
source_url: https://github.com/monero-project/monero/issues/2251
author: Gingeropolous
assignees: []
labels: []
created_at: '2017-08-05T11:52:19+00:00'
updated_at: '2017-10-15T13:22:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In my home network I have the daemon running on a separate machine than my wallet.

Without fail, I always forget which port that daemon has the rpc bound to. So I load up my wallet with the wrong port for --daemon-host.

With the wrong port entered, the wallet just sort of sits there. I ctrl-c the hell out of it but nothing happens. Eventually the program exits. 

# Discussion History
## moneromooo-monero | 2017-08-05T14:50:20+00:00
Seems fine here. Most of the time waiting is spent loading the wallet cache, but after that it's fairly quick till the red message about the daemon not being found. What are the wait times for (1) correct daemon host and (2) wrong daemon host ?

## hyc | 2017-08-05T20:14:32+00:00
huh. do you mean --daemon-address? --daemon-host only takes an IP address, no port number.

## moneromooo-monero | 2017-08-05T20:27:38+00:00
Same thing. I don't get a large delay before the error.

## moneromooo-monero | 2017-10-15T13:22:46+00:00
Can you give an all thread stack trace showing what it's doing ?

# Action History
- Created by: Gingeropolous | 2017-08-05T11:52:19+00:00
