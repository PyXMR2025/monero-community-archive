---
title: New motherboard, now no start of bitmonerod
source_url: https://github.com/monero-project/monero/issues/894
author: Elmit2015
assignees: []
labels: []
created_at: '2016-07-09T11:11:40+00:00'
updated_at: '2016-12-15T17:38:29+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:38:29+00:00'
---

# Original Description
Since I could not start anymore bitmonerod I rebuild the updated source.

I did not see any error during compiling.

The start however looks like:

~/bitmonero/build/release/bin$ ./bitmonerod 

```
Creating the logger system
2016-Jul-09 18:33:31.942942 Initializing cryptonote protocol... 
2016-Jul-09 18:33:31.943086 Cryptonote protocol initialized OK  
2016-Jul-09 18:33:31.943435 Initializing p2p server...         
2016-Jul-09 18:33:32.647114 Set limit-up to 2048 kB/s
2016-Jul-09 18:33:32.647355 Set limit-down to 8192 kB/s
2016-Jul-09 18:33:32.647469 Set limit-up to 2048 kB/s
2016-Jul-09 18:33:32.647602 Set limit-down to 8192 kB/s 
2016-Jul-09 18:33:32.657789 Binding on 0.0.0.0:18080 
2016-Jul-09 18:33:32.658064 Net service bound to 0.0.0.0:18080
2016-Jul-09 18:33:32.658135 Attempting to add IGD port mapping.

2016-Jul-09 18:36:13.756596 Deinitializing rpc server...                                           
2016-Jul-09 18:36:13.756789 Deinitializing p2p...                                                   
2016-Jul-09 18:36:13.768390 Deinitializing core...
2016-Jul-09 18:36:13.768981 Closing IO Service. 
2016-Jul-09 18:36:13.769242 Failed to deinitialize core... 
2016-Jul-09 18:36:13.769347 Deinitializing cryptonote_protocol...
```

How to track down the problem?


# Discussion History
## antanst | 2016-07-09T11:14:14+00:00
I noticed this behaviour when I accidentally tried to run an older bitmonerod using a data dir with an updated database format from a newer version of the daemon. Are you sure you've compiled bitmonerod from latest master?


## radfish | 2016-07-09T16:15:05+00:00
Run with verbose logging and attach the log:

```
./bitmonerod --log-level 6
```


## ghost | 2016-09-15T14:56:47+00:00
@Elmit2015 is this issue still current or can it be closed?


## luigi1111 | 2016-12-15T17:38:29+00:00
@Elmit2015 Please reopen with more information if this is still relevant.

# Action History
- Created by: Elmit2015 | 2016-07-09T11:11:40+00:00
- Closed at: 2016-12-15T17:38:29+00:00
