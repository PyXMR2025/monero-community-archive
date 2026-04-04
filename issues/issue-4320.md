---
title: Update DNSSEC Trust Anchors
source_url: https://github.com/monero-project/monero/issues/4320
author: wessels
assignees: []
labels:
- duplicate
created_at: '2018-08-31T20:25:14+00:00'
updated_at: '2018-08-31T20:56:52+00:00'
type: issue
status: closed
closed_at: '2018-08-31T20:56:52+00:00'
---

# Original Description
In  monero/src/common/dns_utils.cpp you have copied the function get_builtin_ds() from the Unbound source code.  This is the root zone trust anchor.  When the [root zone key signing key changes](https://www.icann.org/resources/pages/ksk-rollover) (Oct 11, 2018) users whose software has only the old trust anchor will not be able to perform DNSSEC validation, and may not be able to resolve any DNS queries.

Suggest you update get_builtin_ds() from  [unbound](https://github.com/NLnetLabs/unbound)/smallapp/unbound-anchor.c and notify your users to update.

# Discussion History
## moneromooo-monero | 2018-08-31T20:52:11+00:00
See #4287 and #4309 

+duplicate


# Action History
- Created by: wessels | 2018-08-31T20:25:14+00:00
- Closed at: 2018-08-31T20:56:52+00:00
