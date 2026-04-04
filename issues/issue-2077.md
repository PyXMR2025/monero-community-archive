---
title: '[request] Windows environment variable for blockchain data storage location'
source_url: https://github.com/monero-project/monero/issues/2077
author: imakiro
assignees: []
labels:
- invalid
created_at: '2017-06-08T09:09:14+00:00'
updated_at: '2017-10-03T11:18:22+00:00'
type: issue
status: closed
closed_at: '2017-10-03T11:18:22+00:00'
---

# Original Description
Hello,

It seems that the blockchain data location cannot be easily specified on a windows machine, forcing a windows user to first launch monerod.exe with the --data-dir parameter and then launch the GUI.

It would help ease things up to do like QT and have a possible environment variable to set once and for all for the user the blockchain location.
example https://github.com/monero-project/monero-core/issues/660#issuecomment-291591638

this would allow for wallet startup at boot with a different blockchain location.

Regards

# Discussion History
## YellowOnion | 2017-09-06T13:14:39+00:00
is daemon start-up flags in GUI setting page not what you're looking for?

## moneromooo-monero | 2017-10-03T11:11:43+00:00
Since it seems to be already doable as per YellowOnion's comment, I'll close.

+invalid

# Action History
- Created by: imakiro | 2017-06-08T09:09:14+00:00
- Closed at: 2017-10-03T11:18:22+00:00
