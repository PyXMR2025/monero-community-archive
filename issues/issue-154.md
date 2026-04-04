---
title: '4'
source_url: https://github.com/monero-project/monero-gui/issues/154
author: tikwanleap
assignees: []
labels: []
created_at: '2016-11-11T18:35:10+00:00'
updated_at: '2016-11-13T18:05:05+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:57:18+00:00'
---

# Original Description
Steps to reproduce:
1. Open wallet 1.
2. Note receive address.
3. Close wallet 1.
4. Open wallet 2.
5. The receive address is the same as wallet 1. Should have updated to match wallet 2.

Temporary workaround:
1. Click the "Generate" button next to Payment ID. This will update to the correct receive address.

# Discussion History
## dEBRUYNE-1 | 2016-11-11T20:11:25+00:00
Can confirm. I was able to reproduce this. 


## taushet | 2016-11-12T07:25:32+00:00
Yep, me too.


## moneromooo-monero | 2016-11-12T10:57:19+00:00
https://github.com/monero-project/monero-core/pull/155


## taushet | 2016-11-12T10:59:46+00:00
Good pickup, btw. This could have had nasty consequenses if undiscovered.


## tikwanleap | 2016-11-12T12:07:15+00:00
Thanks! Happy to help and really glad this was fixed quickly. Great job moneromooo-monero!


## dEBRUYNE-1 | 2016-11-13T14:04:00+00:00
Can confirm the fix works. 


## dternyak | 2016-11-13T17:52:51+00:00
@tikwanleap This can be closed right @taushet ?


## fluffypony | 2016-11-13T17:57:47+00:00
Closing as fixed


# Action History
- Created by: tikwanleap | 2016-11-11T18:35:10+00:00
- Closed at: 2016-11-13T17:57:18+00:00
