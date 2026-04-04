---
title: cli wallet strange little bug
source_url: https://github.com/monero-project/monero/issues/6496
author: sumogr
assignees: []
labels: []
created_at: '2020-05-03T09:51:35+00:00'
updated_at: '2020-05-04T14:20:04+00:00'
type: issue
status: closed
closed_at: '2020-05-04T14:17:05+00:00'
---

# Original Description
using latest release (15.0.5): on entering the wrong password upon opening an existing wallet  
`Error: failed to load wallet: invalid password` good

using compiled bins from latest master: on entering the wrong password upon opening an existing wallet 
` Error: failed to load wallet: std::exception`
it doesnt grab the e.what(). 
why?

# Discussion History
## sumogr | 2020-05-04T14:17:05+00:00
nevermind its due to the wallet2.h for wasm restructuring i found what caused it

## selsta | 2020-05-04T14:18:22+00:00
Are you going to open a PR to fix it?

## sumogr | 2020-05-04T14:20:04+00:00
> Are you going to open a PR to fix it?

ok

# Action History
- Created by: sumogr | 2020-05-03T09:51:35+00:00
- Closed at: 2020-05-04T14:17:05+00:00
