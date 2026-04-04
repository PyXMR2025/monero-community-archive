---
title: sign_transfer broken
source_url: https://github.com/monero-project/monero/issues/1692
author: moneroexamples
assignees: []
labels: []
created_at: '2017-02-07T01:00:58+00:00'
updated_at: '2017-02-07T04:12:20+00:00'
type: issue
status: closed
closed_at: '2017-02-07T04:12:20+00:00'
---

# Original Description
Using recent monero version (v0.10.1.0-3473af00) and wanting to use signed and unsiged tx files, result in this problem when signing unsigned tx:

```
Loaded 0 transactions, for 0.000000000000, fee 0.000000000000, with no destinations, no change, with min mixin 18446744073709551615. 245 outputs to import. Is this okay? (Y/Yes/N/No):
```

Later I will investigate more this. Maybe generating unsigned tx file is also broken. Dont know yet. Just creating this issue for the record.



# Discussion History
# Action History
- Created by: moneroexamples | 2017-02-07T01:00:58+00:00
- Closed at: 2017-02-07T04:12:20+00:00
