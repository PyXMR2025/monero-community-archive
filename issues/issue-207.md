---
title: ' Suggestion: GUI Wallet should have an option to use a remote node until it
  is fully sunchronised'
source_url: https://github.com/monero-project/monero-gui/issues/207
author: sornros
assignees: []
labels:
- duplicate
created_at: '2016-11-26T12:01:00+00:00'
updated_at: '2017-08-08T15:45:09+00:00'
type: issue
status: closed
closed_at: '2017-08-08T15:45:09+00:00'
---

# Original Description
The GUI should have an option where it uses a remote node until the deamon is sunchronised with the network. This would allow to use monero much faster. 
Also the chain should be synched backwards, with the latest block first.

# Discussion History
## taushet | 2016-11-26T15:31:42+00:00
I disagree. The point of the official GUI is to be the core user implementation of the Monero currency, and therefore security should always take precedence. There are many "lighter" wallets in the pipeline (as well as several already released) that will forfeit a small amount of security for convenience and speed. I actually believe that most people will use these lightwallets over this GUI in the longer term (as pretty as it is). I am not in principle against the ability to connect to a remote node, however to endorse this behaviour to the user while he is syncing in order "allow him to use his monero faster" is not correct.

As to the direction of syncing, I believe bottom-up still makes sense to ensure that all your outputs are captured, but I obviously defer to the wiser squirrels on here who can give a more educated answer.

## medusadigital | 2017-08-07T20:08:57+00:00
this ticket is very old. but the feature request is still present.

im closing this one with the dublicate tag in the favour of this newer ticket: https://github.com/monero-project/monero-core/issues/750

+duplicate


## danrmiller | 2017-08-08T15:43:34+00:00
+duplicate

(spelling)

# Action History
- Created by: sornros | 2016-11-26T12:01:00+00:00
- Closed at: 2017-08-08T15:45:09+00:00
