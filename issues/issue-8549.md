---
title: 'Problems at shutdown: Transport endpoint is not connected '
source_url: https://github.com/monero-project/monero/issues/8549
author: DeeDeeRanged
assignees: []
labels: []
created_at: '2022-09-03T17:52:22+00:00'
updated_at: '2022-10-21T09:21:57+00:00'
type: issue
status: closed
closed_at: '2022-10-21T09:21:57+00:00'
---

# Original Description
Running Debian testing (bookworm)
When I call monerod --lpg-level 2 status I get the following as the last line:

Problems at shutdown: Transport endpoint is not connected

Don't know what it actually is referring to and I would like to find out.

# Discussion History
## selsta | 2022-09-03T17:53:34+00:00
Do you have any issues or do you just want to know what it means? Also can you post a larger log with a couple lines before (and after)?

## selsta | 2022-09-03T18:10:16+00:00
From what I can tell the message means that it tries to shutdown a network socket that is already disconnected.

## DeeDeeRanged | 2022-09-03T19:58:21+00:00
Was just curious and the log lines before, there no lines after, that don't say anything either. Have tried all the log-levels if I could see anything specific that would trigger a bell with me.
In my time I have been digging through scripts and logfiles besides scripting when I was still working, just a retired IT soecialist now and still learning things lol.

## selsta | 2022-09-07T14:16:06+00:00
Can you post a larger log with a couple lines before at a higher log level?

## DeeDeeRanged | 2022-10-21T09:21:57+00:00
Have nothing to add anymore than what I stated before and it is not important enough and it doesn't stop monerod running as intended. So I close this issue as of now.

# Action History
- Created by: DeeDeeRanged | 2022-09-03T17:52:22+00:00
- Closed at: 2022-10-21T09:21:57+00:00
