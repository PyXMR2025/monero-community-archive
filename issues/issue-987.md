---
title: Readline support in the command-line tool simplewallet
source_url: https://github.com/monero-project/monero/issues/987
author: aalex
assignees: []
labels: []
created_at: '2016-08-24T15:20:23+00:00'
updated_at: '2017-08-07T19:06:17+00:00'
type: issue
status: closed
closed_at: '2017-08-07T19:06:17+00:00'
---

# Original Description
The users would find it easier to use the command-line tool if the code was using readline.
- control-A to move to the beginning of the line
- up/down arrow to navigate through history
- control-C to cancel a line (instead of cancelling a foreground refresh and/or exit without saving)
- control-D to quit
- etc.


# Discussion History
## radfish | 2016-08-25T02:10:53+00:00
Agreed. As a temporary crutch: https://github.com/monero-project/bitmonero#using-readline

PS. To add another favorite to your list: `~/.inputrc: set editing-mode vi`


## moneromooo-monero | 2017-08-07T17:32:09+00:00
+resolved

# Action History
- Created by: aalex | 2016-08-24T15:20:23+00:00
- Closed at: 2017-08-07T19:06:17+00:00
