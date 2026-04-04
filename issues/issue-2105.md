---
title: readline history is reset at every run
source_url: https://github.com/monero-project/monero/issues/2105
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-06-22T10:28:21+00:00'
updated_at: '2017-06-27T16:46:55+00:00'
type: issue
status: closed
closed_at: '2017-06-27T16:46:55+00:00'
---

# Original Description
When I run monero-wallet-cli without rlwrap, command history only being remembered in the current process. If I exit and run it again, the history will be blank.

# Discussion History
## jtgrassie | 2017-06-22T10:47:53+00:00
This is by design implementation. I decided to not store history to file for potential security issues. 

## moneromooo-monero | 2017-06-23T11:49:02+00:00
That's a fair point, but it also kinda defeats the purpose of readline.

## jtgrassie | 2017-06-23T12:15:41+00:00
Well it depends on how the cli tools are used really. If a user just starts one up, runs a command, then exits, sure it's not much benefit. But if you run the daemon non-detached, it's really useful. Or if you have your wallet open for a longer session. If you think we should persist history I could add that in though.

## moneromooo-monero | 2017-06-23T12:20:06+00:00
Not sure. Your point about security is very good and I had not thought of it :/

## jtgrassie | 2017-06-23T12:28:11+00:00
Whilst somewhat unrelated, one thing I wanted to add was tab-completion. This is a nice feature of readline that makes it easier for the user. We then keep from writing history to disk but its quicker to type commands.

## moneromooo-monero | 2017-06-23T12:29:46+00:00
Sounds good. Someone already added a command list for rlwrap (possibly a bit out of date now though).

## jtgrassie | 2017-06-23T12:35:11+00:00
I'm thinking about using the command binder instead of a list. That way it's more generic and we don't need to maintain a separate list.

## moneromooo-monero | 2017-06-23T16:21:51+00:00
About history, I think you're right that it's best removed, though an option to allow it would be nice, keeping the default to not saving it. Nothing pressing though.

## moneromooo-monero | 2017-06-27T16:46:55+00:00
The privacy argument is good, closing.

# Action History
- Created by: moneromooo-monero | 2017-06-22T10:28:21+00:00
- Closed at: 2017-06-27T16:46:55+00:00
