---
title: 'GitHub notification bot not working in #kovri-dev'
source_url: https://github.com/monero-project/meta/issues/183
author: anonimal
assignees: []
labels: []
created_at: '2018-02-21T06:48:58+00:00'
updated_at: '2020-03-21T01:30:40+00:00'
type: issue
status: closed
closed_at: '2020-03-21T01:30:30+00:00'
---

# Original Description
I've noticed that the github notification bot is sending IRC NOTICEs to `#monero-dev` instead of PRIVMSGs (or the other way around now?...). Coincidentally, `#kovri-dev` has stopped receiving notifications for over a week now.

Did someone change any settings on our end or is this a github issue?

# Discussion History
## anonimal | 2018-05-25T21:34:46+00:00
Appears fixed.

## anonimal | 2018-06-07T22:44:12+00:00
Worked for a day or two, hasn't worked since. Works fine for `#monero-dev`.

## anonimal | 2018-07-03T04:20:12+00:00
Anyone? Also referencing #77.

## anonimal | 2018-07-03T04:27:51+00:00
This continues to work fine in `#monero-dev`.

## selsta | 2020-03-21T01:30:30+00:00
Closing. The GitHub IRC notification service has been deprecated/removed and we run our own bot now.

# Action History
- Created by: anonimal | 2018-02-21T06:48:58+00:00
- Closed at: 2020-03-21T01:30:30+00:00
