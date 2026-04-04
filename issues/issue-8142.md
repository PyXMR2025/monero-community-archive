---
title: monerod constantly re-running checkpointing
source_url: https://github.com/monero-project/monero/issues/8142
author: nkinnan
assignees: []
labels: []
created_at: '2022-01-15T21:14:19+00:00'
updated_at: '2022-01-16T23:06:18+00:00'
type: issue
status: closed
closed_at: '2022-01-16T11:41:22+00:00'
---

# Original Description
I see messages like this in the log file:

```
2022-01-15 20:04:07.176	        b6f67040	INFO	global	src/cryptonote_core/cryptonote_core.cpp:692	Loading checkpoints
2022-01-15 20:04:07.180	        b6f67040	INFO	checkpoints	src/checkpoints/checkpoints.cpp:260	Blockchain checkpoints file not found
2022-01-15 20:04:07.875	        b6f67040	INFO	checkpoints	src/checkpoints/checkpoints.cpp:121	CHECKPOINT PASSED FOR HEIGHT 1 <771fbcd656ec1464d3a02ead5e18644030007a0fc664c0a964d30922821a8148>

<...>

2022-01-15 20:04:26.887	        b6f67040	INFO	checkpoints	src/checkpoints/checkpoints.cpp:121	CHECKPOINT PASSED FOR HEIGHT 2478000 <692fc889f5328c9cfe47e9846ca2bb3d61d82dbeb37077e90e0f8c36b8fc0c84>
```

This happens over and over again.  Its as if a checkpoint file isn't being created/persisted or something?  I am running PiNodeXMR on a pi 4 (4GB) with the lmdb on a USB SSD.  I do not see any related errors in the logs.  Where is this checkpoint information stored?  What should I do / look for to debug this?  Thanks!

# Discussion History
## moneromooo-monero | 2022-01-15T22:09:49+00:00
There might be an exception after checking which skips the last check time setting. Unlikely but... This patcj will tell is if this is the case:

```
diff --git a/src/cryptonote_core/cryptonote_core.cpp b/src/cryptonote_core/cryptonote_core.cpp
index 4ddb90bb2..c66d84b12 100644
--- a/src/cryptonote_core/cryptonote_core.cpp
+++ b/src/cryptonote_core/cryptonote_core.cpp
@@ -310,6 +310,7 @@ namespace cryptonote
     }
     else if (time(NULL) - m_last_json_checkpoints_update >= 600)
     {
+MGINFO("update_checkpoints: now " << time(NULL) << ", last " << m_last_json_checkpoints_update);
       res = m_blockchain_storage.update_checkpoints(m_checkpoints_path, false);
       m_last_json_checkpoints_update = time(NULL);
     }
```

If you built without libunwind, you would not see exception traces in the logs. If you can see any other exception trace in the logs, it cannot be that.

Now, your log shows about 20 seconds between the first and last checks. Are those two checks part of hte same set of checks, or two different ones ?

The check will nornally happen at semi regular intervals of about 10 minutes.


## nkinnan | 2022-01-15T22:48:00+00:00
I do not see any stack traces in the logs.  I'm using the pre-compiled binaries downloaded by PiNodeXMR, I believe it gets them with this command: 

```git clone --recursive -b $RELEASE https://github.com/monero-project/monero.git```

No idea what the build options were for that.  I can attempt to apply the patch and then build from scratch but that would take me some time to get up to speed on how to do so, and would presumably take many hours on a pi 4.  I'm a dev but am used to MSVS on the windows side, so a pointer to any instructions / tutorial would be appreciated.

Here are some additional examples of the checkpointing running:

```
2022-01-15 11:04:57.342	        b6fa1040	INFO	global	src/cryptonote_core/cryptonote_core.cpp:692	Loading checkpoints
2022-01-15 11:04:57.411	        b6fa1040	INFO	checkpoints	src/checkpoints/checkpoints.cpp:260	Blockchain checkpoints file not found
2022-01-15 11:04:58.453	        b6fa1040	INFO	checkpoints	src/checkpoints/checkpoints.cpp:121	CHECKPOINT PASSED FOR HEIGHT 1 <771fbcd656ec1464d3a02ead5e18644030007a0fc664c0a964d30922821a8148>

2022-01-15 11:05:18.989	        b6fa1040	INFO	checkpoints	src/checkpoints/checkpoints.cpp:121	CHECKPOINT PASSED FOR HEIGHT 2478000 <692fc889f5328c9cfe47e9846ca2bb3d61d82dbeb37077e90e0f8c36b8fc0c84>
```

```
2022-01-15 12:39:14.285	[P2P2]	INFO	checkpoints	src/checkpoints/checkpoints.cpp:260	Blockchain checkpoints file not found
2022-01-15 12:39:19.172	[P2P2]	INFO	checkpoints	src/checkpoints/checkpoints.cpp:121	CHECKPOINT PASSED FOR HEIGHT 1 <771fbcd656ec1464d3a02ead5e18644030007a0fc664c0a964d30922821a8148>

2022-01-15 12:39:46.368	[P2P2]	INFO	checkpoints	src/checkpoints/checkpoints.cpp:121	CHECKPOINT PASSED FOR HEIGHT 2478000 <692fc889f5328c9cfe47e9846ca2bb3d61d82dbeb37077e90e0f8c36b8fc0c84>
```

It seems to do this every between 10 and 30 minutes and takes 20-30 second to complete.

## moneromooo-monero | 2022-01-16T08:24:41+00:00
> It seems to do this every between 10 and 30 minutes and takes 20-30 second to complete.

Then it seems expected. Once every 10 minutes, and your I/O is dire on a Pi.

You can disable it with --disable-dns-checkpoints (yes, it's called dns, but it controls both dns and file checkpoints at once).

## nkinnan | 2022-01-16T11:41:16+00:00
If you say it's nothing to be concerned about then I won't worry about it.  Thanks!

## nkinnan | 2022-01-16T23:06:17+00:00
FYI my checksum times decreased to < 1 second after applying this fix which seems to have been the root of all my issues (the checkpointing itself was a red herring) https://forums.raspberrypi.com/viewtopic.php?f=28&t=245931 hopefully this can help someone else.

# Action History
- Created by: nkinnan | 2022-01-15T21:14:19+00:00
- Closed at: 2022-01-16T11:41:22+00:00
