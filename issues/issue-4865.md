---
title: '[Suggestion] Move Blockchain Location'
source_url: https://github.com/monero-project/monero/issues/4865
author: norsehealer
assignees: []
labels:
- invalid
created_at: '2018-11-18T04:39:58+00:00'
updated_at: '2018-11-19T07:05:12+00:00'
type: issue
status: closed
closed_at: '2018-11-18T10:08:58+00:00'
---

# Original Description
Add a method that the CLI/GUI can easily move the blockchain file.

While the user can do this manually it's probably best to simplify it for the user. This can help the user experience and could prevent blockchain corruption.

# Discussion History
## moneromooo-monero | 2018-11-18T10:07:44+00:00
It actually exists already (--data-dir for monerod, and I believe there's a widget in the GUI somewhere for this).

+invalid


## SamsungGalaxyPlayer | 2018-11-19T03:46:18+00:00
Although the "move" functionality is not included, the option of specifying a different location already exists, which imo is plenty for a command line program.

## norsehealer | 2018-11-19T07:05:12+00:00
I'm also talking about the GUI.  There's a "Change" option but it doesn't MOVE the data to the location. If it does then it's labeled wrong.

The --data-dir only tells monerod to check for data in a directory but again it doesn't move data.

I have a SSD, which I imagine many people have or they have a M.2, and putting the blockchain on a storage drive instead of their OS drive is the smart thing to do. I didn't know it was putting the BC on my SSD until I looked at the daemon and searched it on google. Then I had to find out how to move to the data and how to point it to the new directory.

# Action History
- Created by: norsehealer | 2018-11-18T04:39:58+00:00
- Closed at: 2018-11-18T10:08:58+00:00
