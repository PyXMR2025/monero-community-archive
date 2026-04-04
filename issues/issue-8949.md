---
title: wallet2 `frozen` incorrectly asserts key image ordering and causes error on
  multisig tx signing
source_url: https://github.com/monero-project/monero/issues/8949
author: woodser
assignees: []
labels: []
created_at: '2023-07-16T13:23:07+00:00'
updated_at: '2023-08-17T15:25:05+00:00'
type: issue
status: closed
closed_at: '2023-08-17T15:25:05+00:00'
---

# Original Description
A [recent commit](https://github.com/monero-project/monero/commit/dc24312bc3c8c9d865e4576631832c81d6dd212d) to wallet2's `frozen` function incorrectly [asserts that key images are ordered](https://github.com/monero-project/monero/blob/ab826008d614a3722398642942c291be9650be6d/src/wallet/wallet2.cpp#L2008), resulting in the error `Mismatched key image b/t vin and construction data` when multisig participants sync key images such that they're ordered differently.

This issue requests fixing the assertion to not rely on key image ordering.

# Discussion History
# Action History
- Created by: woodser | 2023-07-16T13:23:07+00:00
- Closed at: 2023-08-17T15:25:05+00:00
