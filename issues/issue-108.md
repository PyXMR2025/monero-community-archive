---
title: license violation
source_url: https://github.com/monero-project/monero/issues/108
author: sabelnikov
assignees: []
labels: []
created_at: '2014-08-29T22:43:20+00:00'
updated_at: '2014-09-03T08:02:22+00:00'
type: issue
status: closed
closed_at: '2014-08-29T23:23:28+00:00'
---

# Original Description
Hello dear developers.
I have noticed that you removed author's copyright from sources by following commit: 
https://github.com/rfree2monero/bitmonero/commit/71f83a487f89e1ef8e70e5d613a9854d8331e55b

I'm glad that you are using this library, but i would like to ask you please comply with terms of license, as copyright law requires you to do.

Sincerely, 
Andrey N Sabelnikov


# Discussion History
## monero-project | 2014-08-29T23:23:28+00:00
Hello,

This isn't on our HEAD so I cannot edit it. The main branch file is here:
https://github.com/monero-project/bitmonero/blob/master/contrib/epee/include/net/abstract_tcp_server2.inl

And contains the applicable license. Please contact the developer to have them modify their personal branch.


## sabelnikov | 2014-08-29T23:31:38+00:00
It was merged into your repo and now it is in your "development" branch:

https://github.com/monero-project/bitmonero/blob/development/contrib/epee/include/net/abstract_tcp_server2.inl


## monero-project | 2014-08-29T23:36:20+00:00
Ah thanks, I have reverted this (not sure how it happened in the first place).


## fluffypony | 2014-08-30T06:07:33+00:00
@rfree2monero please fix the licensing headers and resubmit the PR


## rfree2monero | 2014-09-03T08:02:22+00:00
@sabelnikov hi, sorry for this mistake, that is now fixed.

No offence intended of course, accompanying header file .h still had your full copyright line in that comit.

Thanks for reporting


# Action History
- Created by: sabelnikov | 2014-08-29T22:43:20+00:00
- Closed at: 2014-08-29T23:23:28+00:00
