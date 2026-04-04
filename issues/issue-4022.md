---
title: "[P2P9]\tWARN \tblockchain\tsrc/cryptonote_core/blockchain.cpp:3914\tinvalid\
  \ hash for blocks 1545984 - 1546239"
source_url: https://github.com/monero-project/monero/issues/4022
author: lh1008
assignees: []
labels: []
created_at: '2018-06-18T15:49:41+00:00'
updated_at: '2018-06-21T12:39:57+00:00'
type: issue
status: closed
closed_at: '2018-06-21T12:39:57+00:00'
---

# Original Description
Hi guys,

I started syncing from scratch several days ago and everything went fine until I got to blocks 1545984 - 1546239 and an ERROR(invalid hash) shows up. The deamon still synchronizes itself but this error shows up even though it keeps on running. 

Here are the 162 last lines of the bitmonero.log.

https://paste.fedoraproject.org/paste/36SmDYQEN6gC5xD~WG7ifg

Is there any problem? Can it get fixed? 

Thank you :). 

# Discussion History
## Jorropo | 2018-06-18T16:15:26+00:00
Hi, the interesting things is this problem is isolated, so this is probably on your side.
Please, what is your :
Os
Deamon version
And Arch ?

## lh1008 | 2018-06-18T16:23:08+00:00
Thanks,

OS - Ubuntu 16.04 LTS
Deamon 12.02
Intel Core i3 Toshiba Satellite C655 laptop

## Jorropo | 2018-06-18T16:29:56+00:00
Do you try to remove these blocks (5k blocks arround) with Blockchain utils ?

## lh1008 | 2018-06-18T16:34:47+00:00
I don't know how to remove blocks with Blockchain utils.

## Jorropo | 2018-06-18T16:38:39+00:00
Right now I have only my phone so I can't help you right now, but I will help you asap.

## lh1008 | 2018-06-18T16:55:00+00:00
ok thank you :)

## moneromooo-monero | 2018-06-18T20:13:27+00:00
Don't remove anything, it seems to be syncing fine, you can just ban the peer that's sending you these bad blocks. It's probably a peer on a fork that hasn't updated to the current software and so mining invalid blocks.
I'll make this error a bannable offense so it'll cut down on retries :)

Actually, turns out it's already a bannable offense since very recently.


## lh1008 | 2018-06-18T20:17:59+00:00
@moneromooo-monero, how can I ban the peer who is sending these bad blocks?  

## moneromooo-monero | 2018-06-18T20:19:17+00:00
set_log 1
You will get a "Got NEW blocks..." message just before these bad hash messages. It will include the node's IP. Then:
ban THATIPADDRESS
This will ban it for 24 hours.

## lh1008 | 2018-06-21T12:39:57+00:00
I was not able to get the IP to ban it. In the bitmonero.log directory, 2 different bitmonero.log files(bitmonero.log-2018-06-18-23-50-50/bitmonero.log-2018-06-19-04-10-43) were created and I was not sure where to find the IP. 
I'm closing the issue because what I did was close the deamon and started syncing the next day. Then the Invalid Hash ERROR was no longer showing up. @Jorropo and @moneromooo-monero thank you a lot for your support and assistance. If I encounter another error I will open another Issue, I'll be closing this one.

Thank you :).

# Action History
- Created by: lh1008 | 2018-06-18T15:49:41+00:00
- Closed at: 2018-06-21T12:39:57+00:00
