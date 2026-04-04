---
title: v0.16.0 get_blocks.bin request returns incorrect current_height value
source_url: https://github.com/monero-project/monero/issues/6628
author: gutenye
assignees: []
labels: []
created_at: '2020-06-05T14:41:40+00:00'
updated_at: '2020-07-08T22:57:05+00:00'
type: issue
status: closed
closed_at: '2020-07-08T22:57:05+00:00'
---

# Original Description
## Steps to reproduce
1. Start v0.16.0 `monerod`
2. call `get_blocks.bin` API
3. check the `current_height` field in the response

The response is
```js
{
  blocks: [ .. ], 
  credits: 0,
  current_height: 0,  //-> current_height is always 0, which is incorrect. Previous version has the correct value.
  output_indices: [ .. ], 
  start_height: 2114044,
  status: 'OK',
  top_hash: '',
  untrusted: false
}
```

# Discussion History
## moneromooo-monero | 2020-06-05T15:27:48+00:00
Thanks, https://github.com/monero-project/monero/pull/6629

## moneromooo-monero | 2020-07-08T22:57:05+00:00
Merged.

# Action History
- Created by: gutenye | 2020-06-05T14:41:40+00:00
- Closed at: 2020-07-08T22:57:05+00:00
