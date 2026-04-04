---
title: sub-addresses created with the cli are unrecognized by the gui and vice versa
source_url: https://github.com/monero-project/monero/issues/3554
author: jonahar
assignees: []
labels:
- invalid
created_at: '2018-04-04T18:29:04+00:00'
updated_at: '2018-04-07T13:48:42+00:00'
type: issue
status: closed
closed_at: '2018-04-07T13:48:42+00:00'
---

# Original Description
I have some sub-addresses created with the cli which are not recognized by the gui, and sub-addresses created by the gui which are not recognized by the cli.
It's like each of them looks at a different set of sub-addresses.

# Discussion History
## moneromooo-monero | 2018-04-05T11:55:03+00:00
Are you running one on big endian and another on little endian ?
Define "recognized".


## jonahar | 2018-04-05T12:24:50+00:00
I guess I didn't explain properly. By "recognized" I meant "shows" or "lists".
When opening the same wallet file both in the cli and in the gui:
- The cli only lists sub-addresses that were created in the cli.
- The gui only lists sub-addresses that were created in the gui.

I used the official download for Linux 64-bit. I run both of them on the same Linux machine, so I think the answer to the endianness question is no.

## stoffu | 2018-04-05T13:23:38+00:00
Maybe you’re not aware of it, but subaddresses are organized into groups using a pair of indices, namely major index and minor index. Money received by subaddresses sharing the same major index are summed up to form a separate balance, leading to the concept of an “account”.
Currently, the GUI only supports creation of subaddresses belonging to the default account (major index = 0), while the CLI fully supports creation of multiple accounts.

When you open a wallet with the CLI, the default account is always selected as the initial state. You can see the list of all subaddresses stored in the cache belonging to the default account by typing `address all`. The displayed list of subaddresses should be the same as the list of subaddresses you see in the GUI.

If they don’t agree, it’s a bug. Please provide logs and screenshots.


## jonahar | 2018-04-05T20:43:16+00:00
Thank you for the clarification.
Indeed, when the default account is chosen in the cli, `address all` shows the addresses created in the gui.

## moneromooo-monero | 2018-04-07T12:03:34+00:00
So all  is working as expected, just confusing, right ?

## jonahar | 2018-04-07T13:05:20+00:00
Yes. I guess the issue can be closed.
Thanks

## moneromooo-monero | 2018-04-07T13:46:43+00:00
+invalid

# Action History
- Created by: jonahar | 2018-04-04T18:29:04+00:00
- Closed at: 2018-04-07T13:48:42+00:00
