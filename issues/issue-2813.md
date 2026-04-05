---
title: Command the miner to pause/resume with API calls
source_url: https://github.com/xmrig/xmrig/issues/2813
author: CidiRome
assignees: []
labels:
- question
created_at: '2021-12-15T16:01:44+00:00'
updated_at: '2022-04-03T14:36:40+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:36:40+00:00'
---

# Original Description
Hi there.

Where I find the full set of commands/calls that can be made the API?

I want to pause and resume the operations with it, what I the commands?

Cheers.

# Discussion History
## Spudz76 | 2021-12-15T18:19:32+00:00
Best you can do via API is send a different config file.

There are no keyboard controls wired into the API.

`/2/summary` or `/2/backends` or `/1/benchmark` or `/2/config` or `/2/dmi` are the only endpoints

## CidiRome | 2021-12-15T18:47:29+00:00
Can it at least load config files with different names from the program folder?
Or
Where can I get examples of sending API instructions and config files with linux wget?
Cheers.

## Spudz76 | 2021-12-16T09:50:57+00:00
https://github.com/xmrig/xmrig/blob/master/doc/API.md#put-1config

except now use /2/config otherwise same

## CidiRome | 2021-12-16T10:48:27+00:00
Will it actually overwrite the config.json file in the program folder, or the file will only be in memory until the program shuts down and next time it starts will be with the original file?

## Spudz76 | 2021-12-16T15:44:59+00:00
Overwrites.

## xmrig | 2021-12-19T14:53:43+00:00
You can use `POST /json_rpc` with following bodies `{"method":"pause","id":1}` and `{"method":"resume","id":1}`.
Thank you.


# Action History
- Created by: CidiRome | 2021-12-15T16:01:44+00:00
- Closed at: 2022-04-03T14:36:40+00:00
