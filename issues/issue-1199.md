---
title: '''Dust'' amounts in transactions.  Suggest changing dust threshold and/or
  remove dust-handling'
source_url: https://github.com/monero-project/monero/issues/1199
author: AwfulCrawler
assignees: []
labels: []
created_at: '2016-10-09T21:15:19+00:00'
updated_at: '2016-10-15T07:10:56+00:00'
type: issue
status: closed
closed_at: '2016-10-15T07:10:56+00:00'
---

# Original Description
With the decrease in per Kb fees, the dust threshold has remained the same.  In my last tx I got

> The transaction fee is 0.010000000000, of which 0.008000000000 is dust from change.

in my confirmation message.

To me this is slightly annoying paying a 'tip' in the form of dust which is greater than the official fee amount.

At the moment, any amount < 0.01 XMR is considered dust.  Short term, I suggest decreasing DEFAULT_DUST_THRESHOLD in cryptonote_config.h by a power of 10.

Removing 'dust' as a concept altogether from the wallet code might be the way to go longer-term.  It would remove some complexity from the code and prevent these sorts of little annoyances.  I don't think it's a difficult change and I'm willing to do it myself if people think it's a good idea.


# Discussion History
## AwfulCrawler | 2016-10-15T07:10:56+00:00
PR submitted


# Action History
- Created by: AwfulCrawler | 2016-10-09T21:15:19+00:00
- Closed at: 2016-10-15T07:10:56+00:00
