---
title: Clicking "Sweep Unmixable" on gui crashes program on windows
source_url: https://github.com/monero-project/monero-gui/issues/1567
author: BigslimVdub
assignees: []
labels: []
created_at: '2018-09-21T02:18:56+00:00'
updated_at: '2019-07-04T06:30:35+00:00'
type: issue
status: closed
closed_at: '2019-07-04T02:33:47+00:00'
---

# Original Description
Windows 10
Monero GUI release v.0.12.3
Aeon GUI release v.012.5
Issue repeatable 4 times In a row. Open GUI, login to wallet, select "sweep unmixable" and GUI locks up. Click anywhere In the GUI and program crashes and windows exits the program. 




# Discussion History
## maogo | 2018-10-12T02:53:02+00:00
Yes ,i have same issue.GUI  v.0.12.3

## dEBRUYNE-1 | 2019-07-03T17:38:56+00:00
Can you check whether this is still an issue with GUI v0.14.1.0?



## BigslimVdub | 2019-07-03T17:51:21+00:00
I will when I get a chance. 

## dEBRUYNE-1 | 2019-07-03T21:00:43+00:00
Thanks. 

## BigslimVdub | 2019-07-04T02:33:47+00:00
Ok so I check with 14.1 GUI release on Windows 10 and when selecting "sweep unmixable" the gui hangs up and then windows prompts the "gui not responding" error prompt but before I could click "close monero-gui", the GUI sent me to the screen "Error-no unmixable outputs to sweep" and gui function returned to normal. 

So at this point, I would say that it is working properly as performance has enhanced and selecting this does not totally crash the gui like before. I am testing this with the same wallet file from November and it is an unused wallet file with no tx history. Possibly someone with a more "used" wallet with actual tx's may have an issue of the gui locking up but I am not.  

## dEBRUYNE-1 | 2019-07-04T06:30:35+00:00
Thanks for testing @BigslimVdub.

# Action History
- Created by: BigslimVdub | 2018-09-21T02:18:56+00:00
- Closed at: 2019-07-04T02:33:47+00:00
