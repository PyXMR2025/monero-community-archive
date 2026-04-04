---
title: Monerod report
source_url: https://github.com/monero-project/monero/issues/6649
author: Cideg
assignees: []
labels: []
created_at: '2020-06-13T10:21:12+00:00'
updated_at: '2021-08-13T04:59:34+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:59:34+00:00'
---

# Original Description
does anyone know what that means in the deamon


2020-06-12 18:47:01.761 I END DUMP
2020-06-12 18:47:01.761 I Please send moneromooo on Freenode the contents of this log, from a couple dozen lines before START DUMP to END DUMP

# Discussion History
## moneromooo-monero | 2020-06-13T11:02:42+00:00
It means the log contains information to help debug a particular issue that you experienced, and that START DUMP and END DUMP mark the start and end of that information, and that I would like to get that information. Please either paste it here, or on a paste site (without javascript, does not reject tor), or send it to moneromooo on Freenode. Please also try to inlcude a couple dozen lines before the START DUMP line, in case there's interesting things going on before the trigger.

## Cideg | 2020-06-13T11:08:04+00:00
@moneromooo-monero
https://paste.ubuntu.com/p/BCTzXqSzdX/



## moneromooo-monero | 2020-06-13T11:19:37+00:00
Thanks, can you paste from the start marker (a few dozen lines before it even) ?

## Cideg | 2020-06-13T11:27:42+00:00
> Danke, können Sie von der Startmarkierung aus einfügen (ein paar Dutzend Zeilen davor sogar)?
https://paste.ubuntu.com/p/RbRSFNMJVV/



## moneromooo-monero | 2020-06-13T12:50:34+00:00
Thanks.
Can you paste the entirety of the data between START DUMP and END DUMP ? 
If it's too large, it can go on a temp git repo.

## Cideg | 2020-06-13T13:13:04+00:00

https://github.com/Cideg/Monero-log/blob/master/dump.log
or
START DUMP and END DUMP
https://paste.ubuntu.com/p/Z8S49bg9Pf/

## moneromooo-monero | 2020-06-13T13:22:27+00:00
Excellent, thanks!
Hopefully that'll help me fix this bug.
In the meantime, your blockchain probably has an incorrect difficulty value.
You may want to pop 20000 blocks and let it resync those:
pop_blocks 20000


## Cideg | 2020-06-13T13:34:59+00:00
OK thank you,

I will sync again with:

/ monero-blockchain-import - pop_blocks 20000


## moneromooo-monero | 2020-06-13T15:03:44+00:00
The logs were very useful, thanks. I think I fixed the bug, see https://github.com/monero-project/monero/pull/6650


## selsta | 2021-08-13T04:59:34+00:00
Fix has been merged.

# Action History
- Created by: Cideg | 2020-06-13T10:21:12+00:00
- Closed at: 2021-08-13T04:59:34+00:00
