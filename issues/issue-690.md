---
title: Display max CPU thread count allowed in Solo mining, warn users about impact
  to other apps
source_url: https://github.com/monero-project/monero-gui/issues/690
author: scottAnselmo
assignees: []
labels: []
created_at: '2017-04-24T01:53:07+00:00'
updated_at: '2018-12-18T15:53:09+00:00'
type: issue
status: closed
closed_at: '2018-12-18T15:53:09+00:00'
---

# Original Description
The CPU miner doesn't seem to have anything that prevents you from mining with the UI with more CPU threads than you have. I suspect it's due to how it's handled on the backend and thus this isn't a huge concern. For example with an i7-6700K I can mine with 20 CPU threads even though the 6700K only has 8 CPU threads. Even with 20 threads selected the GUI nor Windows crashes which is good.

While mining is under 'Advanced', the everyday user has no idea how many CPU threads they can use. Thus for the sake of miner diversification by making it easier to understand and do solo mining, the max CPU thread count should be displayed. For example I would know that by using 6 threads, I'm theoretically using 75% of my threads. Bad inputs could be prevented from the front end by having a dropdown instead of a text field wherein the dropdown has list of values 1 to i where i is the max CPU threads.

Lastly, there should be some degree of disclosure that mining may reduce the performance of other running applications and processes. This can be included in the current text about strengthening the network or as a warning pop-up dialog box (with a toggle to never display warning again).

# Discussion History
# Action History
- Created by: scottAnselmo | 2017-04-24T01:53:07+00:00
- Closed at: 2018-12-18T15:53:09+00:00
