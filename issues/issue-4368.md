---
title: 'No monerod log on OS X to check after monerod refuses to start. '
source_url: https://github.com/monero-project/monero-gui/issues/4368
author: kupietools
assignees: []
labels: []
created_at: '2024-10-22T22:58:47+00:00'
updated_at: '2024-10-22T23:05:01+00:00'
type: issue
status: closed
closed_at: '2024-10-22T23:05:01+00:00'
---

# Original Description
Monero GUI won't start the seed on OS X: "local node is not responding after 120 seconds. Check your wallet and daemon log for errors." There is no ~/.bitmonero folder (yes, I know the dot would make it invisible initially) nor is there any monerod.log anywhere on my drive that I can find. System logs contain no mention of monero.

EDIT: Never mind. Will leave this up for future users' reference. The problem was an old install left an ~/.bitmonero alias a few years ago, which was blocking writing the new one. I wasn't seeing it because I was sorting ~/ by modification date, looking for new changes, and the old alias wasn't being touched so it was down buried in older files. Deleting ~/.bitmonero fixed it. 



# Discussion History
# Action History
- Created by: kupietools | 2024-10-22T22:58:47+00:00
- Closed at: 2024-10-22T23:05:01+00:00
