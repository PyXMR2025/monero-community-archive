---
title: bitmonerod.exe crashes on fat32 file system after about block 250,000
source_url: https://github.com/monero-project/monero/issues/852
author: pointbiz
assignees: []
labels: []
created_at: '2016-05-28T15:21:18+00:00'
updated_at: '2017-11-22T10:24:25+00:00'
type: issue
status: closed
closed_at: '2017-11-22T10:24:25+00:00'
---

# Original Description
Using --data-dir option to store the blockchain on an external hard drive with FAT32 formatting.

I'm not suggesting it should work on FAT32 but it crashes without any indication in the logs for why the crash occurred. Therefore, user does not know how to rectify the problem. I solved this by formatting the external hard drive in NTFS format.

Is there a way to detect the disk format and shut down bitmonerod.exe with appropriate log message?

Crash happens after around block 250,000. Using Windows.
v 0.9.4


# Discussion History
## luigi1111 | 2016-08-10T14:49:31+00:00
Probably a file size limitation. I'm not sure this will be common enough to justify spending much time on.


## moneromooo-monero | 2017-09-30T09:27:13+00:00
monerod should not error out instead of crashing. It certainly worked when I ran on a filled up partition (failure to commit, but no crash).

## hyc | 2017-10-01T01:26:03+00:00
FAT32 has a max filesize of 4GB so you can't use that for storing the blockchain.


## moneromooo-monero | 2017-11-22T10:17:56+00:00
I saw a report of someone else trying to use FAT32, and it doesn't crash anymore, it errors out with I/O errors.

+resolved


# Action History
- Created by: pointbiz | 2016-05-28T15:21:18+00:00
- Closed at: 2017-11-22T10:24:25+00:00
