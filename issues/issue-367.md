---
title: mining in two pools or two wallets?
source_url: https://github.com/xmrig/xmrig/issues/367
author: axe-usat
assignees: []
labels: []
created_at: '2018-01-28T00:27:19+00:00'
updated_at: '2018-02-05T05:55:41+00:00'
type: issue
status: closed
closed_at: '2018-01-31T08:38:42+00:00'
---

# Original Description
it's possible to mining in two wallets?

# Discussion History
## axe-usat | 2018-01-29T00:56:52+00:00
in DonateStrategy i just must to put the pool, the port and the wallet or username?
would be something like this?
Url *url = new Url("pool", Options::i()->algo() == Options::ALGO_CRYPTONIGHT_LITE ? 3333 : port, wallet, nullptr, false, true);

# Action History
- Created by: axe-usat | 2018-01-28T00:27:19+00:00
- Closed at: 2018-01-31T08:38:42+00:00
