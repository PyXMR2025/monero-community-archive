---
title: '[Design] Cyclical dependency between libdevice and libcryptonote_basic'
source_url: https://github.com/monero-project/monero/issues/7053
author: mj-xmr
assignees: []
labels: []
created_at: '2020-12-02T16:19:23+00:00'
updated_at: '2021-07-27T20:52:17+00:00'
type: issue
status: closed
closed_at: '2021-07-27T20:52:17+00:00'
---

# Original Description
In this [issue](https://github.com/monero-project/monero/pull/7051) (where you'll find info how to trigger the problem), I have noticed the following cyclical dependency:

The `libdevice` depends on `libcryptonote_basic through cryptonote::get_transaction_prefix_hash(cryptonote::transaction_prefix const&, crypto::hash&)`, used in `device_default.cpp`, while `libcryptonote_basic` depends on `libdevice`, via the file `crypronote_basic.h`, where the `device.hpp` is included and used.

The remedy would be to feed the `libcryptonote_basic` with the class (or rather interface) `device` from `libdevice`, but extracting any implementations (i.e. `device_default`) outside of `libdevice` into, say, `libdeviceImpl`.

This is not high on my prio list currently, but I would be capable of resolving this one once I have more capacity.

# Discussion History
# Action History
- Created by: mj-xmr | 2020-12-02T16:19:23+00:00
- Closed at: 2021-07-27T20:52:17+00:00
