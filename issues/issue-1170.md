---
title: Can't delete past edge when typing seed in --restore-deterministic-wallet
source_url: https://github.com/monero-project/monero/issues/1170
author: ghost
assignees: []
labels: []
created_at: '2016-10-03T00:14:45+00:00'
updated_at: '2016-10-04T20:06:45+00:00'
type: issue
status: closed
closed_at: '2016-10-04T20:01:41+00:00'
---

# Original Description
In v0.10 if I'm restoring a wallet from seed (Linux 64-bit), a typical seed may take up 3 or 4 lines of text when the software prompts me to enter it. 

Here's the issue: if I'm fifteen or so words in and realize I made an error earlier in the word list, and hit backspace/delete to get back, it will hit the edge of terminal and refuse to keep going. It will stay on that single line, hitting the edge of the page and staying there. Does that make sense? It's as if you can't delete more than the single line you're already on when restoring from seed.


# Discussion History
## ghost | 2016-10-03T00:35:58+00:00
Are you able to perform multi-line deletion when trying this in other programs?


## ghost | 2016-10-03T03:49:01+00:00
It works in Terminal. Can you suggest another program for me to test?


## moneromooo-monero | 2016-10-03T08:29:41+00:00
Are you using rlwrap ?


## ghost | 2016-10-03T20:02:50+00:00
@moneromooo-monero That solved it. Thanks. It would be interesting to make this a default setting, though I assume ya'll got bigger fish to fry.

Feel free to mark this task as "solved".

Edit: talked with Saddam and he said rlwrap is not ideal for restoring from seed since it keeps the command inside its log file. So perhaps this is an important feature to add to the CLI wallet.


## ghost | 2016-10-03T21:58:40+00:00
Do you want to open that as a [Feature Request] issue and close this one? Then it'll remain obvious into the future.


## ghost | 2016-10-04T20:01:41+00:00
Great

https://github.com/monero-project/monero/wiki/Feature-Requests


# Action History
- Created by: ghost | 2016-10-03T00:14:45+00:00
- Closed at: 2016-10-04T20:01:41+00:00
