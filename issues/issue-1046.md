---
title: Supporting multiple RandomX variants
source_url: https://github.com/xmrig/xmrig/issues/1046
author: jagerman
assignees: []
labels: []
created_at: '2019-06-30T16:14:12+00:00'
updated_at: '2019-07-06T22:20:50+00:00'
type: issue
status: closed
closed_at: '2019-07-06T22:20:50+00:00'
---

# Original Description
Loki is forking to a [https://github.com/loki-project/loki-RandomXL](RandomX variant) ("RandomXL") in about 3.5 weeks; the testnet has already forked to it.

Like RandomWOW, like Monero's RandomX itself, and undoubtedly like other forks in the future, each variant involves the same code compiled with a different set of `#define`s, but that poses a problem for mining software like xmrig and pool code (https://github.com/MoneroOcean/node-cryptonight-hashing/issues/31) that wants to support multiple versions in the same binary.

I'm happy to submit a PR for Loki support, but I need some guidance on how to actually make supporting multiple variants work within xmrig; the current approach of linking in the randomx library won't work for supporting multiple variations.

# Discussion History
## Spudz76 | 2019-07-06T18:58:49+00:00
Already handled, and the randomx lib accepts init arguments for all the possible tweaks, it is not compiled "for" any particular RandomX algo specifically.  It's more like a Java VM than an algo, so one lib and multiple init-methods.

## jagerman | 2019-07-06T22:20:50+00:00
The runtime program configuration added in #1050 a great addition, much thanks (to you and @SChernykh) for the support!

# Action History
- Created by: jagerman | 2019-06-30T16:14:12+00:00
- Closed at: 2019-07-06T22:20:50+00:00
