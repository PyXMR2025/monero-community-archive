---
title: 'Feature request: option to turn off simplewallet logging'
source_url: https://github.com/monero-project/monero/issues/913
author: mmortal03
assignees: []
labels:
- enhancement
created_at: '2016-07-14T20:57:26+00:00'
updated_at: '2016-09-16T04:01:04+00:00'
type: issue
status: closed
closed_at: '2016-09-04T20:09:00+00:00'
---

# Original Description
With Monero being considered a privacy-centric cryptocurrency, there should be an option to disable simplewallet's logging completely.  Maybe --log-level -1 or something, such that no transaction data or even public addresses are logged? The less information that is left around in plain text the better when wanting to avoid any privacy concerns.


# Discussion History
## moneromooo-monero | 2016-08-21T11:12:46+00:00
There's a vague plan to replace the whole logging infrastructure in the near/medium future, which this will likely be part of.


## grummerd | 2016-08-21T12:00:09+00:00
--log-level=false

or

--log-level=0


## mmortal03 | 2016-08-21T20:22:37+00:00
grummerd, I tested --log-level=0, and it did not turn off logging. I did not test --log-level=false.


## iamsmooth | 2016-09-04T03:06:01+00:00
--log-file nul (windows) or --log-file /dev/null (linux)

Have not tested


## mmortal03 | 2016-09-04T20:09:00+00:00
I just tested --log-level=false, and that doesn't work.

I next tested --log-file nul, and that works, both for simplewallet and bitmonerod.

I noticed that bitmonerod still creates an empty folder structure, though, called "log\dr-monero\net"

Anyway, I'll close this, as this is a sufficient workaround.


## grummerd | 2016-09-16T04:01:04+00:00
it's not sufficient until it's well documented. Has the documentation been updated?


# Action History
- Created by: mmortal03 | 2016-07-14T20:57:26+00:00
- Closed at: 2016-09-04T20:09:00+00:00
