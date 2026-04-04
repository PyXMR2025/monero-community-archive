---
title: Switch GUI node aggregator service to privacy aware hosting
source_url: https://github.com/monero-project/monero-gui/issues/2203
author: sanderfoobar
assignees: []
labels:
- invalid
created_at: '2019-06-08T17:56:38+00:00'
updated_at: '2020-02-13T14:45:54+00:00'
type: issue
status: closed
closed_at: '2020-02-13T14:45:54+00:00'
---

# Original Description
https://autonode.xmr.pm is our node aggregator for Simple Mode inside the GUI. This centralised functionality will be replaced by xiphon soon. Till then, we have it hosted in The Netherlands, EU at a company called TransIP B.V (transip.nl).

I would like to switch hosting to https://ovo.sc/ for the following reasons:

### Benefits:

- Datacenter in Seychelles, Africa. Outside of EU jurisdiction.
- Unmanaged free speech hosting
- Payment methods are exclusively Bitcoin / Monero

### Downsides:

- Servers might not be as stable (as 'regular' hosters), however, I don't expect much downtime.
- Higher chance of being shutdown/raided due to the nature of unmanaged free speech hosting. But since the application I'm planning to host is not difficult to setup, I can quickly pivot to another hoster when necessary.

To conclude, I believe moving autonode.xmr.pm to a country that's not in the US/EU will harden privacy/decentralisation for any user using Simple Mode.

# Discussion History
## selsta | 2019-06-14T21:42:27+00:00
Are the servers in Romania or Seychelles?

## sanderfoobar | 2019-06-15T13:25:52+00:00
Seychelles

## SamsungGalaxyPlayer | 2019-06-15T16:23:27+00:00
I have no strong opinion.

## selsta | 2020-02-13T14:39:25+00:00
Closing as we don’t use a node aggregator currently.

+invalid

# Action History
- Created by: sanderfoobar | 2019-06-08T17:56:38+00:00
- Closed at: 2020-02-13T14:45:54+00:00
