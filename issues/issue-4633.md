---
title: 'How to use new config: block-notify.'
source_url: https://github.com/monero-project/monero/issues/4633
author: DinoStray
assignees: []
labels: []
created_at: '2018-10-17T02:58:44+00:00'
updated_at: '2018-10-24T03:57:43+00:00'
type: issue
status: closed
closed_at: '2018-10-24T03:57:43+00:00'
---

# Original Description
I use it in config file:
block-notify=/root/scripts/new_block_callback.sh

then, in new_block_callback.sh:
```
#!/usr/bin/env bash

echo "hi" >> /root/lyl
```

then, nothing happened.


# Discussion History
## xiphon | 2018-10-17T03:04:17+00:00
Should be something like
`--block-notify='/bin/bash /root/scripts/new_block_callback.sh'`

Edit: have to specify the full path to `bash` (https://github.com/monero-project/monero/issues/4633#issuecomment-430559323)

## DinoStray | 2018-10-17T03:44:20+00:00
> Should be something like
> `--block-notify='bash /root/scripts/new_block_callback.sh'`

block-notify='bash /root/scripts/new_block_callback.sh'
Still, nothing happened.

If I run  /root/scripts/new_block_callback.sh directly， everything is OK.

## moneromooo-monero | 2018-10-17T09:34:11+00:00
/usr/bin/bash


## moneromooo-monero | 2018-10-17T10:31:17+00:00
And you should have got an error message about it when monerod started. Did you not ?

## DinoStray | 2018-10-17T12:57:20+00:00
> And you should have got an error message about it when monerod started. Did you not ?

And a lot of defunct thread

## moneromooo-monero | 2018-10-17T13:20:25+00:00
Please expand.

# Action History
- Created by: DinoStray | 2018-10-17T02:58:44+00:00
- Closed at: 2018-10-24T03:57:43+00:00
