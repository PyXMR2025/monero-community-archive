---
title: OSX client stuck in Synchronizing mode – also eating up all the CPU
source_url: https://github.com/monero-project/monero/issues/2574
author: balinterdi
assignees: []
labels: []
created_at: '2017-10-03T17:55:30+00:00'
updated_at: '2017-10-04T07:20:26+00:00'
type: issue
status: closed
closed_at: '2017-10-04T07:20:26+00:00'
---

# Original Description
I downloaded the 64-bit Mac OSX client from getmonero.org today and launched it. It went download the blockchain for a while (I assume) and I had to quit it at one point because I had a video call and it the process made the video call lag remarkably.

I then wanted to resume but it now it seems to be stuck in Synchronized mode forever:
![](https://cl.ly/1K2L2P1s1t1E/download/Screen%20Shot%202017-10-03%20at%2019.46.47.png)

And it's still spinning the CPUs at 250% while doing that:
![](https://cl.ly/1Y2C2T3E263t/download/Screen%20Shot%202017-10-03%20at%2019.46.56.png)

I'm not sure whether this is due to having had to quit the app once, of course.

Could you recommend something to unstuck the process – or issue a fix?

Thank you.

# Discussion History
## moneromooo-monero | 2017-10-03T18:36:53+00:00
What is Synchronized mode ? If you mean synchronizing, then it's expected to keep at it for a while, till it's finished syncing the blockchain, which may take from a few hours to a few days, depending on your hardware (especially hard disks are pretty slow compared to SSDs). During that time it will use a lot of CPU verifying blocks and transactions.
If it's not that, then please be precise about the symptoms you're seeing which seem to be unexpected.

## balinterdi | 2017-10-04T07:20:26+00:00
Thank you for the quick response.

You were right, I let the process run during the night and in the morning and it was all good, the status is now Connceted and it's no longer spinning the CPU.

Sorry for the false alarm.

# Action History
- Created by: balinterdi | 2017-10-03T17:55:30+00:00
- Closed at: 2017-10-04T07:20:26+00:00
