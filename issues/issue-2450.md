---
title: 'monero-blockchain-import v0.11.0.0 ERROR "MDB_MAP_FULL: Environment mapsize
  limit reached"'
source_url: https://github.com/monero-project/monero/issues/2450
author: RigacciOrg
assignees: []
labels: []
created_at: '2017-09-15T09:17:33+00:00'
updated_at: '2017-09-26T04:29:00+00:00'
type: issue
status: closed
closed_at: '2017-09-25T14:57:14+00:00'
---

# Original Description
I tried to import the blockchain into v0.11.0.0, after exporting it from from v0.10.3.1. The host is a GNU/Linux amd64, 12 Gb RAM, over 120 Gb of free disk on SATA III HD.

During the process, the host becomes almost unresponsive, the 4 cores went overwhelmed by more of 10 pending processes. Some suggestion on how to help in debugging? You can see the error in the log attached.

[monero-blockchain-import.log.txt](https://github.com/monero-project/monero/files/1305848/monero-blockchain-import.log.txt)


# Discussion History
## moneromooo-monero | 2017-09-15T11:18:52+00:00
Try with --batch-size 100

## hyc | 2017-09-17T00:27:40+00:00
Just to confirm, I tried to do an import from scratch and hit this error around block 1015000. All default parameters. (Note that simply restarting will let it progress further.)

## RigacciOrg | 2017-09-26T04:28:59+00:00
I repeated the same exact import using "--batchsize 100" as suggested (same raw file, same monero-blockchain-import executable). This time the process took 9.5 hours instead of 16, no errors were reported, the load average was less problematic. Thanks!

# Action History
- Created by: RigacciOrg | 2017-09-15T09:17:33+00:00
- Closed at: 2017-09-25T14:57:14+00:00
