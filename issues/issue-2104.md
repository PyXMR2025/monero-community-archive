---
title: readline prompt displayed after each output line in incoming_transfers
source_url: https://github.com/monero-project/monero/issues/2104
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-06-22T10:26:03+00:00'
updated_at: '2017-08-07T15:48:56+00:00'
type: issue
status: closed
closed_at: '2017-07-24T09:57:46+00:00'
---

# Original Description
eg:

               amount   spent    unlocked  ringct    global index                                                               tx id
      10000.000000000       T    unlocked       -          473514  <f58314d3f9a137c94f550df79c752570f382bfca9132b17eb90f75907fc4a733>[wallet 9zcJy2]

Probably other commands too. I've just tried show_transfers, and it shows up too.


# Discussion History
## jtgrassie | 2017-06-22T10:53:19+00:00
Looks like any multiline logging outputs using `message_writer`. I will address.

## jtgrassie | 2017-06-22T13:42:40+00:00
I'm not actually getting any output from `show_transactions` whether with or without readline support. Any idea why that could be?

## moneromooo-monero | 2017-06-23T11:47:56+00:00
From show_transfers, you mean ? If so, it could be that all your txes on that wallet were made before the data for show_transfers was kept. If not, it appears to be a bug.

Also, when you refresh a wallet and it takes a while, you see just the end of the counting messages, the first part is hidden by the prompt. This is possibly the same bug, so I'm not opening one for now. This happens only for manual refresh (ie, you type refresh at the prompt), not automatic refresh when the wallet starts.

## moneromooo-monero | 2017-06-23T11:56:28+00:00
You could try the get_transfers RPC to see if you get any data. That'll tell you whether it's missing data or output bug.

## jtgrassie | 2017-06-23T12:12:25+00:00
@moneromooo-monero I'm not sure why it was doing that but I rescanned and that fixed it. I'm working on the readline prompt issues at the moment. I just need to find all the commands that cause the issue!

## jtgrassie | 2017-06-23T12:53:13+00:00
Fixed by #2112 

## moneromooo-monero | 2017-06-23T16:20:16+00:00
Also the "tx saved as..." line when creating a tx from view wallet (probably also fixed by your patch, I'm just mentioning it here so I remember to check when I test your patch)

## moneromooo-monero | 2017-06-26T05:31:15+00:00
Using 2112, I still see things like a command being hidden, eg: at the prompt, I type a command, then enter. This erases the command, and just displays the prompt. Due to the temporary hang filed elsewhere, this looks like it's completely been ignored. Later on, a password prompt comes up on the same line, and you see: [wallet A27QfV]: Wallet password: 
So it needs to echo the user's newline.

## moneromooo-monero | 2017-06-27T19:34:13+00:00
There's another manifestation of that bug, which hides random messages. For example:

sign_transfer xxxxx

xxxxx being an existing file, but a multisig unsigned tx. The signing fails (since the file isn't the expected cold wallet information), but that message does not show up (though it does appear in the log, as expected). It's hidden by the prompt.



## moneromooo-monero | 2017-06-27T19:34:49+00:00
I'm using all the patches, including the process lock and my patches to fix the random delay in readline stop.

## moneromooo-monero | 2017-07-24T09:57:46+00:00
All this seems fine with latest patches.

# Action History
- Created by: moneromooo-monero | 2017-06-22T10:26:03+00:00
- Closed at: 2017-07-24T09:57:46+00:00
