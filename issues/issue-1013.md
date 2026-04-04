---
title: 'bitmonerod: --offline flag not working '
source_url: https://github.com/monero-project/monero/issues/1013
author: medusadigital
assignees: []
labels: []
created_at: '2016-08-29T21:00:53+00:00'
updated_at: '2016-11-21T16:26:33+00:00'
type: issue
status: closed
closed_at: '2016-11-21T16:26:33+00:00'
---

# Original Description
It seems the --offline flag doesnt work anymore in bitmonerod. Simplewallet is unable to connect to daemon.

**how to reproduce:** 
-make sure your computer has no Internet connection (detach cable)
-launch bitmonerod --offline 
-launch simplewallet
-refresh simplewallet 

-> simplewallet will throw an Error here.

**bitmonerod has to be able to work with --offline flag when:**
-No IP has been distributed
-No Interface is installed at all 


# Discussion History
## moneromooo-monero | 2016-09-01T17:15:17+00:00
https://github.com/monero-project/bitmonero/pull/1031


## ghost | 2016-09-02T20:18:14+00:00
Who closes these issues once they've been solved?


## medusadigital | 2016-09-04T03:14:34+00:00
quickly tested without cable --> worked fine.
didnt test without Network Interface


## moneromooo-monero | 2016-09-18T09:18:21+00:00
NanoAkron, typically fluffypony whenever he gets to it.


## medusadigital | 2016-11-21T16:26:33+00:00
long time no see, works now for some time. ---> closed

# Action History
- Created by: medusadigital | 2016-08-29T21:00:53+00:00
- Closed at: 2016-11-21T16:26:33+00:00
