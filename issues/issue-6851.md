---
title: wallet2::store_to() does not create main wallet file
source_url: https://github.com/monero-project/monero/issues/6851
author: woodser
assignees: []
labels: []
created_at: '2020-09-29T16:01:32+00:00'
updated_at: '2020-09-29T16:01:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`wallet2::store_to()` does not create the main wallet file when moving to a new location.  `wallet2::store()` must be called to create the main wallet file.

[This comment](https://github.com/monero-project/monero/blob/3cbb44a2fd79ce9c667006e2e42e61513993e59a/src/wallet/wallet2.cpp#L5868) suggests the main wallet should already be created when moving to a new location, but I don't see the corresponding logic which should probably follow.

# Discussion History
# Action History
- Created by: woodser | 2020-09-29T16:01:32+00:00
