---
title: 'monero-blockchain-export: Failed to create a transaction for the db: Permission
  denied'
source_url: https://github.com/monero-project/monero/issues/4826
author: coneiric
assignees: []
labels: []
created_at: '2018-11-09T01:14:59+00:00'
updated_at: '2018-11-09T02:58:21+00:00'
type: issue
status: closed
closed_at: '2018-11-09T02:58:21+00:00'
---

# Original Description
This problem was reported by a user on IRC. Here is a [paste of their logs](https://paste.ee/p/4Erhk).

Have had similar issues manually moving, then trying to import the moved blockchain. Get the same error.

# Discussion History
## hyc | 2018-11-09T01:55:43+00:00
Sounds like it's quite plainly a file permissions problem with the blockchain database.

## coneiric | 2018-11-09T02:27:56+00:00
That's what I thought at first, too. But in the IRC user's case, and mine, the file and directory are owned by the user running the tool.

In one desperate attempt, I even changed the file permissions to 777, to no avail. Any ideas? Or, did you mean the file permissions set/read by LMDB itself?

## hyc | 2018-11-09T02:30:15+00:00
If you're sure the file permissions are OK, then try running with strace and see which actual system call returned EPERM.

## coneiric | 2018-11-09T02:55:50+00:00
Alright, just ran monero-blockchain-export/import tools. Seems to complete exporting/importing the database fine, but core dumps with unhandled exception `boost: mutex lock failed in pthread_mutex_lock: Invalid argument`. Looks like the same error addressed [here](https://github.com/monero-project/monero/pull/4785).

Good times...

# Action History
- Created by: coneiric | 2018-11-09T01:14:59+00:00
- Closed at: 2018-11-09T02:58:21+00:00
