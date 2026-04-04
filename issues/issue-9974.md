---
title: 'simplewallet: `sweep_single` does not respect `do-not-relay`'
source_url: https://github.com/monero-project/monero/issues/9974
author: hinto-janai
assignees: []
labels: []
created_at: '2025-07-02T21:42:01+00:00'
updated_at: '2025-07-10T12:19:13+00:00'
type: issue
status: closed
closed_at: '2025-07-10T12:19:13+00:00'
---

# Original Description
`sweep_single` will relay a transaction to the connected node even if `do-not-relay` is passed.

It seems that the check that exists for `sweep_{all,account,below,unmixable}`:

https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/simplewallet/simplewallet.cpp#L7228

https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/simplewallet/simplewallet.cpp#L6932

does not exist for `sweep_single`:

https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/simplewallet/simplewallet.cpp#L7463-L7467

# Discussion History
# Action History
- Created by: hinto-janai | 2025-07-02T21:42:01+00:00
- Closed at: 2025-07-10T12:19:13+00:00
