---
title: some commands are ignored if entered in quick succession
source_url: https://github.com/monero-project/monero/issues/2155
author: moneromooo-monero
assignees: []
labels:
- bug
created_at: '2017-07-06T13:14:03+00:00'
updated_at: '2018-09-04T23:14:25+00:00'
type: issue
status: closed
closed_at: '2018-09-04T23:14:25+00:00'
---

# Original Description
Sometimes, commands are ignored. Press enter after a command, and nothing happens. A subsequent command will be executed, so it's not like it's timing out waiting on a lock (this can happen, and is something unrelated entirely - when needing the blockchain lock while syncing, for instance).This is rare-ish, but happens a few times daily. This happens with or without readline. A good test is to sync from scratch, ensuring some good load, then quickly enter "status" and "exit". status will execute after a delay once it's got the blockchain lock, and exit will never run.

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:30:40+00:00
+bug

## moneromooo-monero | 2018-09-04T23:14:25+00:00
I'll say this is fine, it's serial, and the "apparent" problem is really readlin displaying the prompt too early, making you think you can enter a new command.

# Action History
- Created by: moneromooo-monero | 2017-07-06T13:14:03+00:00
- Closed at: 2018-09-04T23:14:25+00:00
