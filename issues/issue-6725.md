---
title: Can't exit from password prompt
source_url: https://github.com/monero-project/monero/issues/6725
author: benmoss
assignees: []
labels: []
created_at: '2020-07-27T16:11:36+00:00'
updated_at: '2020-07-27T19:15:04+00:00'
type: issue
status: closed
closed_at: '2020-07-27T19:15:04+00:00'
---

# Original Description
When the CLI becomes locked due to inactivity, it presents a password prompt. Often I just want to exit the program rather than re-enter my password to unlock, but I can't seem to by the normal ways I know how. Both Ctrl-C (SIGINT) and Ctrl-D (EOF) just result in "Error: failed to read wallet password". In filing this bug I learned that Ctrl-\ is also a thing and sends SIGQUIT, which does in fact work. 

# Discussion History
## selsta | 2020-07-27T16:23:59+00:00
Are you using screens / ssh?

Does readline work for you, e.g. can you press the up arrow to get the last command?

## benmoss | 2020-07-27T16:33:07+00:00
No, not using any terminal muxer or ssh, and yeah readline normally works. Ctrl-C does work on the initial password prompt when I load the CLI as well. Probably worth mentioning this is against `Monero 'Nitrogen Nebula' (v0.16.0.0-25419b4bf)`

## benmoss | 2020-07-27T16:46:12+00:00
[![asciicast](https://asciinema.org/a/349968.svg)](https://asciinema.org/a/349968)

## selsta | 2020-07-27T16:51:38+00:00
https://github.com/monero-project/monero/issues/6192

## benmoss | 2020-07-27T19:15:04+00:00
Closing as duplicate, thanks @selsta 

# Action History
- Created by: benmoss | 2020-07-27T16:11:36+00:00
- Closed at: 2020-07-27T19:15:04+00:00
