---
title: tx splitting likely resulting in uselessly small outputs
source_url: https://github.com/monero-project/monero/issues/754
author: iamsmooth
assignees: []
labels: []
created_at: '2016-03-24T02:20:23+00:00'
updated_at: '2016-07-03T22:33:25+00:00'
type: issue
status: closed
closed_at: '2016-07-03T22:33:25+00:00'
---

# Original Description
This tx looks like a portion of a split, and the .______666666 amount results in both useless payment and fee outputs.

http://moneroblocks.info/tx/ab3607ce839614131de594bd5eaaba9910bcb68ebebedae9a396722ed0ea5e09

When splitting probably should do something other than just divide by N to calculate the target size for each piece. For example repeatedly: divide by number of remaining pieces, truncate to desired precision, and subtract from remaining total.


# Discussion History
## iamsmooth | 2016-03-24T02:21:10+00:00
The other 2 portions of the split are in adjacent blocks


## moneromooo-monero | 2016-03-28T15:50:09+00:00
That's one of the things that transfer_new changes.


## fluffypony | 2016-04-02T03:26:58+00:00
Can this be closed?


## iamsmooth | 2016-04-06T04:16:00+00:00
Not unless we are completely replacing 'transfer' with 'transfer_new' which seemed in some way undesirable when discussed in the past (I don't remember the details). We can consider this an issue with regular 'transfer' exclusively.


## iamsmooth | 2016-07-03T22:33:22+00:00
will become irrelevant with ringct, so closing


# Action History
- Created by: iamsmooth | 2016-03-24T02:20:23+00:00
- Closed at: 2016-07-03T22:33:25+00:00
