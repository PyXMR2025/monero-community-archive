---
title: Busy daemon makes monero-core throw no_connection_to_daemon
source_url: https://github.com/monero-project/monero-gui/issues/75
author: medusadigital
assignees: []
labels: []
created_at: '2016-10-18T14:12:05+00:00'
updated_at: '2016-10-18T16:34:53+00:00'
type: issue
status: closed
closed_at: '2016-10-18T16:34:53+00:00'
---

# Original Description
when downloading the blockchain, daemon is busy and cant answer to other requests.

right now the following combination seems to happen when running monero-core, while the daemon is downloading blocks(head+head):

![gethaschesfail](https://cloud.githubusercontent.com/assets/17108301/19480894/75634e32-954c-11e6-963e-0e8efb738bb6.png)
- monero-core calls get_hasches() from daemon
- daemon fails to execute get_hashes(), since he is busy downloading blocks
- monero-core interprets the return code as offline, throws no_connection_to_daemon

this happens around every ~10 sec during the whole block downloading process. 
the GUI behaves always fine, this issue is just about the exceptions being thrown.

Not quite sure to me how the solution should look like, goal is definetely to get rid of the exceptions for now.


# Discussion History
## medusadigital | 2016-10-18T16:34:33+00:00
seems to be an accident on my side for now. however, the resulting follow-up issue still needs some love https://github.com/monero-project/monero/issues/1235 


# Action History
- Created by: medusadigital | 2016-10-18T14:12:05+00:00
- Closed at: 2016-10-18T16:34:53+00:00
