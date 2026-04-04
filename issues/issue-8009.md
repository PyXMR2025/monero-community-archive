---
title: Monerod Using 59% System Memory When Synced?
source_url: https://github.com/monero-project/monero/issues/8009
author: downystreet
assignees: []
labels: []
created_at: '2021-10-16T00:39:57+00:00'
updated_at: '2021-10-17T12:36:39+00:00'
type: issue
status: closed
closed_at: '2021-10-16T01:26:08+00:00'
---

# Original Description
Version: v0.17.2.3

Monerod is sycned and is using 59% of system memory. What is going on here? Daemon is running with --prune-blockchain command. When I stop the daemon there is 12GB available instead of 11. Am I reading this correctly?
![monerod](https://user-images.githubusercontent.com/63488055/137566933-a7491f46-d709-47d0-a4f0-0516de1376bc.png)


# Discussion History
## hyc | 2021-10-16T01:26:08+00:00
It's normal. Any free RAM is used by the filesystem cache, and mapped in as shared memory. Has no impact on the system, the OS will reclaim it if it needs it for other uses.

## trasherdk | 2021-10-17T12:36:39+00:00
Not exactly a memory or resource hog :smiley: 
![image](https://user-images.githubusercontent.com/5003891/137627466-0f38dca0-3e51-4433-a5a4-6c9414c4f4fe.png)



# Action History
- Created by: downystreet | 2021-10-16T00:39:57+00:00
- Closed at: 2021-10-16T01:26:08+00:00
