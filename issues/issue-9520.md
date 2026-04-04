---
title: Inconsistent transfers in wallet RPC (in/out, integrated/standard, separate
  transfers vs destinations array, multi-amount, edge cases, etc)
source_url: https://github.com/monero-project/monero/issues/9520
author: martinoshub
assignees: []
labels:
- question
- proposal
- discussion
created_at: '2024-10-15T16:45:41+00:00'
updated_at: '2024-10-20T14:43:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There seem to be major pitfalls in building a custodial wallet using the wallet RPC, ie. trying to process payments (user deposits).

You would think it's a simple task: do `get_transfers` since last processed height, look at "in" array, iterate through the array, look for any addresses that belong to a user, credit the amount when confirmed.

It's when you consider "what if a user sends coins to an address that is part of the wallet" it starts to fall apart. Since there's absolutely no sign of this transaction in the "in" array. The transfer is only present in the "out" section. So if a user of mine tries to send coins to an address that happens to belong to another user using the website which has a custodial XMR wallet that I'm building, the recipient never receives it.

You may say "why don't you just also iterate through the outgoing". That's where it starts to get really ugly. There are some major differences in how the same transfer looks on the incoming and outgoing side.

- Multiple destinations show up as one transfer with multiple destinations in the outgoing section, but show up as separate transfers in the incoming section
- Sending different amounts to the same address however, shows up as one incoming transfer, with the amounts added together, but on the outgoing side they are separate destinations
- Incoming transfers show the standard address, while outgoing transfers show the integrated address when sending to integrated addresses

Because of these inconsistencies, I would practically have to do validate_address and split_integrated_address for each destination when iterating through the outgoing destinations, which may slow down the whole process if there are many transfers and destinations involved. And depending on which wallet I process, I may get different results in the end.

It's also quite a crappy workaround and a lot of extra complexity for nothing. And there may be further edge cases I haven't thought of that may result in double-crediting payments one way or the other. I've pretty much dropped this option.

The only current way I could avoid making the payment processing super complicated and insecure would be to never use the same wallet for receiving payments as the one I'm using to send payments. But is that really necessary? Do I really need a separate routine to transfer funds from one wallet to another because of how information is provided by the RPC?

To fix this, I propose the following: if a transfer involves a local address as a destination (in the same account I'm doing `get_transfers` on), just include it in the "in" section. Like other coin RPCs do. This would solve this problem. It's a matter of principle, anyway. Just because it was sent from the same wallet, doesn't mean there's no incoming transfer. It's both outgoing and incoming, as far as the local addresses are concerned.


# Discussion History
# Action History
- Created by: martinoshub | 2024-10-15T16:45:41+00:00
