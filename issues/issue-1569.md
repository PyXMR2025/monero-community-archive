---
title: Please add a reminder to answer the Ledger Nano prompt on exporting the view
  key
source_url: https://github.com/monero-project/monero-gui/issues/1569
author: Laurentiu-Andronache
assignees: []
labels: []
created_at: '2018-09-22T08:31:25+00:00'
updated_at: '2018-10-02T00:03:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When the program starts, please add a reminder to answer the Ledger Nano prompt on exporting the view key. It's easy to forget because the program looks as if it started normally. If you forget, then you get an error because you haven't answered the prompt. Then you have to turn off the program because reloading the wallet would show another error. Then once you've restarted the program, even if you do everything correctly, if you're using a remote node it starts a local one, so again you have to restart the program, And this time it works fine if you remember the prompt.

# Discussion History
## usmarine2141 | 2018-10-01T20:48:57+00:00
wow, each time i close my gui, have to resync the entire wallet blocks again. pretty annoying. 

## Laurentiu-Andronache | 2018-10-02T00:03:29+00:00
> wow, each time i close my gui, have to resync the entire wallet blocks again. pretty annoying.

Maybe you should create a new wallet using a remote node, and set it so that it starts sync from a certain block (around when you received the Monero). It's very fast after you do this... But yeah, definitely not user friendly... and the fees are too damn high... and it has no pruning so downloading the blockchain takes too long... etc.

# Action History
- Created by: Laurentiu-Andronache | 2018-09-22T08:31:25+00:00
