---
title: '[BUG] Password "line" rendered invisible when a transaction comes in'
source_url: https://github.com/monero-project/monero/issues/2187
author: dEBRUYNE-1
assignees: []
labels:
- bug
created_at: '2017-07-21T14:55:51+00:00'
updated_at: '2019-05-23T19:52:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Noticed this on Linux. When one is entering the password in order to, for instance, obtain the private tx key and simultaneously a transaction comes in, the password will become invisible. That is, the incoming transaction visually overwrites the password line. Note that, if you entered the correct password and hit enter, it will still perform the command as expected. Steps to reproduce:

1. Send a transaction

2. Obtain the private tx key with the `get_tx_key` command.

3. Enter part of the password and wait for the change to come back to your wallet (i.e. when the transaction is mined). 

# Discussion History
## dEBRUYNE-1 | 2017-08-25T15:54:28+00:00
+bug

## Timo614 | 2017-12-07T14:05:05+00:00
The password input is now invisible so we probably can close this issue out.

https://github.com/monero-project/monero/pull/2749

## dEBRUYNE-1 | 2017-12-11T10:26:26+00:00
@Timo614: If I recall correctly it overwrites the whole line, which is not preferred behavior. I'll have to test to make sure. 

## jonathancross | 2019-05-18T17:03:29+00:00
@dEBRUYNE-1  Is this still an issue?

## dEBRUYNE-1 | 2019-05-23T19:52:48+00:00
@jonathancross - Not entirely sure. Can try to reproduce later. 

# Action History
- Created by: dEBRUYNE-1 | 2017-07-21T14:55:51+00:00
