---
title: Payment ID rejection with 106 character address
source_url: https://github.com/monero-project/monero-gui/issues/831
author: doobilydo
assignees: []
labels: []
created_at: '2017-08-22T20:57:05+00:00'
updated_at: '2017-08-23T02:19:06+00:00'
type: issue
status: closed
closed_at: '2017-08-23T02:19:06+00:00'
---

# Original Description
I'm getting a rejection (red background) for the payment ID in both **Send** and **Address book**. It's not accepting 16 or 64 character IDs (or anything in between). I'm not able to send because of this. 

I'm running the downloaded binary for Linux 64. The checksum matches.

It should be mentioned that there is inconsistency in labeling among the fields:
* Send: *16 or 64 hexadecimal characters*
* Address book: *Paste 64 hexadecimal characters*
* Receive: *16 hexadecimal characters*



# Discussion History
## stoffu | 2017-08-22T23:36:35+00:00
An address with 106 characters is called "integrated address" which already includes an 8-byte (i.e. 16-character) payment ID. As such, you can't additionally specify yet another payment ID with it.

## doobilydo | 2017-08-23T02:19:03+00:00
Yep. Just figured that out from my stack exchange post. I completely missed that one.

# Action History
- Created by: doobilydo | 2017-08-22T20:57:05+00:00
- Closed at: 2017-08-23T02:19:06+00:00
