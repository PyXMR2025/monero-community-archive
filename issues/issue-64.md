---
title: WalletImpl::integratedAddress unexpectedly overriding payment id
source_url: https://github.com/monero-project/monero-gui/issues/64
author: moneromooo-monero
assignees: []
labels: []
created_at: '2016-10-16T12:14:11+00:00'
updated_at: '2016-11-01T08:25:57+00:00'
type: issue
status: closed
closed_at: '2016-11-01T08:25:57+00:00'
---

# Original Description
This is straddling monero and the GUI a bit, but it seems best here:

In std::string WalletImpl::integratedAddress(const std::string &payment_id) const
if payment_id can't be parsed, a random one is generated instead.
This seems wrong, and potentially dangerous. It should error out instead (ie, return empty string, or throw).


# Discussion History
## moneromooo-monero | 2016-10-16T12:19:08+00:00
https://github.com/monero-project/monero/pull/1228


## fluffypony | 2016-11-01T08:25:57+00:00
Fixed


# Action History
- Created by: moneromooo-monero | 2016-10-16T12:14:11+00:00
- Closed at: 2016-11-01T08:25:57+00:00
