---
title: ' coinbase maturity '
source_url: https://github.com/monero-project/monero/issues/699
author: perl5577
assignees: []
labels: []
created_at: '2016-03-04T00:47:15+00:00'
updated_at: '2016-12-15T18:00:04+00:00'
type: issue
status: closed
closed_at: '2016-12-15T18:00:04+00:00'
---

# Original Description
With blocktime change for 2 minutes .

--  CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW 60 
++ CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW 45

Reduce 1/4  for increase blocktime per factor 2 .


# Discussion History
## luigi1111 | 2016-10-04T22:21:08+00:00
This is a hardforking change. Personally, I think the coinbase maturation was possibly dangerously low before. The blocktime bump makes it somewhat better.


# Action History
- Created by: perl5577 | 2016-03-04T00:47:15+00:00
- Closed at: 2016-12-15T18:00:04+00:00
