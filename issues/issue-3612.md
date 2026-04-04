---
title: Generating a Private Key
source_url: https://github.com/monero-project/monero/issues/3612
author: quantumproducer
assignees: []
labels:
- invalid
created_at: '2018-04-12T00:16:30+00:00'
updated_at: '2018-04-12T14:00:59+00:00'
type: issue
status: closed
closed_at: '2018-04-12T06:16:49+00:00'
---

# Original Description
What are the technical specifications of a private key?

https://getmonero.org/technical-specs/ doesn't say.

https://en.bitcoin.it/wiki/Private_key shows: "In Bitcoin, a private key is a 256-bit number, which can be represented one of several ways. Here is a private key in hexadecimal - 256 bits in hexadecimal is 32 bytes, or 64 characters in the range 0-9 or A-F. "

I need to generate a private key by coin flipping.

# Discussion History
## moneromooo-monero | 2018-04-12T06:08:24+00:00
That's a good question for monero.stackexchange.com, try there, and not here, which is a bug tracker.

+invalid


## quantumproducer | 2018-04-12T13:39:27+00:00
@moneromooo-monero I consider this a documentation bug. The wiki . https://github.com/monero-project/monero/wiki does not have this information whereas the Bitcoin wiki does.
For anyone reading, I'm seeing reports of 64 bit Hexadecimal.

## fluffypony | 2018-04-12T13:42:11+00:00
64 hexadecimal characters is 256 bits. If you think it should be in the wiki then please add it.

## quantumproducer | 2018-04-12T14:00:59+00:00
Thanks @fluffypony , I will when I get confirmation on monero.stackexchange

# Action History
- Created by: quantumproducer | 2018-04-12T00:16:30+00:00
- Closed at: 2018-04-12T06:16:49+00:00
