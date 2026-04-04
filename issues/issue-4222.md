---
title: Monero CLI wallet on Whonix
source_url: https://github.com/monero-project/monero/issues/4222
author: poopaapoopaa
assignees: []
labels: []
created_at: '2018-08-04T15:01:28+00:00'
updated_at: '2018-08-14T15:45:51+00:00'
type: issue
status: closed
closed_at: '2018-08-14T15:45:51+00:00'
---

# Original Description
I run the following on Whonix 13 workstation:

>torsocks ./monero-wallet-cli --daemon-host xmrag4hf5xlabmob.onion:18081 --restore-height -1

Most features work well. But when I run a transaction using:

>transfer [addr] [amt] [payment_id]

I get the following error, multiple times:

>libunbound[12335:0] error: can’t create socket: Operation not permitted

The transaction actually works though. Is this error something that should concern me, and is there a way to avoid it? I saw that there are specific settings for Tails, but I'm not sure if they're relevant for Whonix.

# Discussion History
## moneromooo-monero | 2018-08-04T15:15:53+00:00
You can ignore, it's very likely to be a DNS check for a TXT record to get the "segregation height", which is not so relevant now. When this fails, it uses the hardcoded default, which is still good.

# Action History
- Created by: poopaapoopaa | 2018-08-04T15:01:28+00:00
- Closed at: 2018-08-14T15:45:51+00:00
