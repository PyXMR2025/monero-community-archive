---
title: Shutdown process is not clean nor quick
source_url: https://github.com/monero-project/monero/issues/1176
author: ghost
assignees: []
labels: []
created_at: '2016-10-03T21:41:19+00:00'
updated_at: '2016-12-04T21:54:08+00:00'
type: issue
status: closed
closed_at: '2016-12-04T21:54:08+00:00'
---

# Original Description
After creating #1168, it looks like the shutdown procedure is anything but smooth.

The system can take 10-20 seconds to stop collecting and verifying transactions after receiving a stop signal

The system also reduplicates a couple of steps during shutdown, as shown below:

```
2016-Oct-03 22:05:40.712207 [SRV_MAIN]net_service loop stopped.
2016-Oct-03 22:05:40.712394 [SRV_MAIN]p2p net loop stopped
2016-Oct-03 22:05:40.712431 [SRV_MAIN]Stopping core rpc server...
2016-Oct-03 22:05:40.712867 [SRV_MAIN]Node stopped.
2016-Oct-03 22:05:40.712919 [SRV_MAIN]Deinitializing rpc server...
2016-Oct-03 22:05:40.713232 [SRV_MAIN]Deinitializing p2p...
2016-Oct-03 22:05:40.731353 [SRV_MAIN]Deinitializing core...
2016-Oct-03 22:05:40.731453 [SRV_MAIN]Miner has received stop signal
2016-Oct-03 22:05:40.731488 [SRV_MAIN]Not mining - nothing to stop
2016-Oct-03 22:05:40.731523 [SRV_MAIN]Received signal to deactivate memory pool store
2016-Oct-03 22:05:40.731566 [SRV_MAIN]Stopping blockchain read/write activity
2016-Oct-03 22:07:03.617020 [SRV_MAIN]Local blockchain read/write activity stopped successfully
2016-Oct-03 22:07:03.617224 [SRV_MAIN]Blockchain directory successfully unlocked
2016-Oct-03 22:07:03.617347 [SRV_MAIN]Miner has received stop signal
2016-Oct-03 22:07:03.617388 [SRV_MAIN]Not mining - nothing to stop
2016-Oct-03 22:07:03.619834 [SRV_MAIN]Stopping cryptonote protocol...
2016-Oct-03 22:07:03.619954 [SRV_MAIN]Cryptonote protocol stopped successfully
```

Note:
- the miner is asked to stop twice at  22:05:40.731453 and 22:07:03.617347
- the core rpc server is asked to stop at 22:05:40.712431, which then stops with the 'node stopped' message at 22:05:40.712867, but then another stop signal is sent at 22:05:40.712919 with a different message
- the p2p system is stopped at 22:05:40.712394 and again at 22:05:40.713232

I'm going to go through and try to dissect these, but some help would be great, as well as someone a bit more experienced to try to smooth out the shutdown process. To me, the system should just stop all IO and in-memory validation when it receives a stop signal, roll back to the last confirmed block and then write everything to disk - the extra 10-20 seconds of validation could be a potential attack vector or lead to data corruption if someone turns their box off having expected a faster shutdown - 20 seconds of inactivity can look a lot like a crash...


# Discussion History
## moneromooo-monero | 2016-10-04T11:42:11+00:00
The one I'm aware of that's taking a long time is handle_response_get_objects. It will loop through 200 blocks (soon to be overridable, which may be a good idea when using a remote node), but does not know about the stop signal. I could not find a way to cleanly access it to break out of the loop when set. Maybe setting a flag in the p2p endpoints from the p2p stop function, if it has access to that...


## ghost | 2016-10-04T15:49:49+00:00
Could it check a stop flag each time it starts processing a new block? It would add a few microseconds overhead to each block at most.


## moneromooo-monero | 2016-10-04T16:22:34+00:00
Depends how clean it is :)


## ghost | 2016-10-04T21:14:21+00:00
Isn't there a global 'go' flag initiated at startup? I'm going to try to trace through the startup process and see where it might be sensible to add one unless you happen to have any suggestions :)


## moneromooo-monero | 2016-10-04T21:36:19+00:00
What do you mean by a 'go' flag ?


## ghost | 2016-10-04T22:13:39+00:00
Just rethinking it...issues of concurrency. Anyway, this is probably better discussed elsewhere.


## moneromooo-monero | 2016-12-04T12:30:13+00:00
https://github.com/monero-project/monero/pull/1397

## ghost | 2016-12-04T21:54:08+00:00
Awesome! Closing.

# Action History
- Created by: ghost | 2016-10-03T21:41:19+00:00
- Closed at: 2016-12-04T21:54:08+00:00
