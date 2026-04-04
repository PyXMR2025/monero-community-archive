---
title: The running sync status message on linux  terminal
source_url: https://github.com/monero-project/monero/issues/5545
author: potatoisfood
assignees: []
labels: []
created_at: '2019-05-15T20:51:19+00:00'
updated_at: '2019-08-27T15:58:18+00:00'
type: issue
status: closed
closed_at: '2019-08-27T15:58:18+00:00'
---

# Original Description
The running sync status message on linux terminal is a little bit confusing.
Synced 1305532/1835430 (71% 529898 blocks remaining)


Could be better like this
Synced 71% 1305532/1835430 (529898 blocks remaining)

or
Synced 71% 1305532/1835430 ( 29% 529898 blocks remaining)

# Discussion History
## moneromooo-monero | 2019-05-15T20:53:43+00:00
Odd, I have a comma here, which removes the ambiguity.

## potatoisfood | 2019-05-15T20:55:56+00:00
Could you copy paste it here? What it looks like.

## moneromooo-monero | 2019-05-15T21:15:04+00:00
Synced 1212057/1212251 (99%, 194 left)


## potatoisfood | 2019-06-02T11:13:49+00:00
When there is more than 98% synced, it looks like this.
Synced 1847938/1848071

So there is no parentheses and nothing inside them

## moneromooo-monero | 2019-06-02T16:53:39+00:00
Are you using an old version (0.14.0.2 and earlier are deemed old for the purposes of this question) ?

## moneromooo-monero | 2019-06-29T12:06:30+00:00
ping

## moneromooo-monero | 2019-08-27T15:11:14+00:00
It is more user friendly currently. That was probably an old version, so closing.

+resolved

# Action History
- Created by: potatoisfood | 2019-05-15T20:51:19+00:00
- Closed at: 2019-08-27T15:58:18+00:00
