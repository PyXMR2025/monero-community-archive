---
title: Most people does mine with using power - I would do it without
source_url: https://github.com/xmrig/xmrig/issues/2219
author: amb-iota
assignees: []
labels:
- wontfix
created_at: '2021-03-31T10:05:03+00:00'
updated_at: '2021-04-12T13:39:51+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:39:51+00:00'
---

# Original Description
Dear Friends,

I think everybody nows, that some processors does run parts of them even if there is no use for it. I would like to use exact this parts to mine because this would never cost energy but it will give some miningpower and will use left power not unused.

To do something like this xmrig should be able to be adjusted in a way like never use full capacity or never do itself speed up the processor but if a thread is runnig anyway that speeds it up use the second one if it is free.

Do you understand what I miss in here?

Maybe it is in and I did not recognise but I would like to use it like that. Just now I mine with a script that is allways looking for the system it runs on to have some spare threads and even this would be a nice function to define -t for max threads used from xmrig like it is now and -T for maximum used threads in a CPU (not from xmrig) because in this case a 10 Core unit could be adjusted to do something like -t 10 -T 18 what means as long as a user working on the system isn't using more than 8 threads it will run xmrig with 10 threads but if he uses 10 threads xmrig is slowing down for 8 threads and if he uses 18threads xmrig will pause itself. This would make it possible to mine without being disturbed by it.

Hope my request is for everybody understandable and not for nothing because I think it would be more nice for xmrig.



# Discussion History
# Action History
- Created by: amb-iota | 2021-03-31T10:05:03+00:00
- Closed at: 2021-04-12T13:39:51+00:00
