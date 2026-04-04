---
title: 'developer-guides: wallet-rpc: validate_address example is incorrect'
source_url: https://github.com/monero-project/monero-site/issues/1849
author: reemuru
assignees: []
labels:
- bug
- '📚 docs: dev guides'
created_at: '2021-09-25T22:30:58+00:00'
updated_at: '2021-09-29T01:32:20+00:00'
type: issue
status: closed
closed_at: '2021-09-29T01:32:20+00:00'
---

# Original Description
The example curl request for [validate_address](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#validate_address) should have the `params` set with `:` not `=`. Also, `allow_openalias` and `any_net_type` parameters are shown as strings and not boolean values. PR #1848 will fix.

# Discussion History
# Action History
- Created by: reemuru | 2021-09-25T22:30:58+00:00
- Closed at: 2021-09-29T01:32:20+00:00
