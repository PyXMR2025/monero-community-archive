---
title: Intelligent block propagation
source_url: https://github.com/monero-project/monero/issues/89
author: fluffypony
assignees: []
labels: []
created_at: '2014-08-08T08:44:50+00:00'
updated_at: '2015-03-26T14:59:36+00:00'
type: issue
status: closed
closed_at: '2015-03-26T14:59:36+00:00'
---

# Original Description
Right now blocks are broadcast to all peers, regardless of whether they already have that block.

Peers should be sent a hash of the new block and should respond confirming whether or not they want to accept the block. Obviously if the block matching that hash has already been received from a connected peer, it does not need to be sent.


# Discussion History
## iamsmooth | 2014-08-23T00:22:58+00:00
Want to avoid slowing propagation too much though, so this gets tricky. The current algorithm is probably close to optimal until blocks get larger


# Action History
- Created by: fluffypony | 2014-08-08T08:44:50+00:00
- Closed at: 2015-03-26T14:59:36+00:00
