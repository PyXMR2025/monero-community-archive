---
title: '[QUESTION] Why not notify wallet about incoming unconfirmed transactions?'
source_url: https://github.com/monero-project/monero/issues/5771
author: naughtyfox
assignees: []
labels: []
created_at: '2019-07-22T16:50:59+00:00'
updated_at: '2019-07-24T11:21:23+00:00'
type: issue
status: closed
closed_at: '2019-07-24T11:21:23+00:00'
---

# Original Description
Hey guys!

We've been faced the problem when unconfirmed incoming transaction doesn't show up in gui interface. It seems it's been made deliberately (https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L2022). I think it would be very convenient if a receiver could see the incoming payment in a few moments after send.

Is there any reason why I shouldn't show these payments? If you are ok with it I can file a patch.

Thanks.

# Discussion History
## naughtyfox | 2019-07-24T11:21:23+00:00
Oh, I find the reason why, I believe. It's already done :) Sorry :)

# Action History
- Created by: naughtyfox | 2019-07-22T16:50:59+00:00
- Closed at: 2019-07-24T11:21:23+00:00
