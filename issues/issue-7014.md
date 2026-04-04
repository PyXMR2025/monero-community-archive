---
title: 'Wallet UX: `set ask-passsword never` doesn''t work as expected.'
source_url: https://github.com/monero-project/monero/issues/7014
author: jonathancross
assignees: []
labels: []
created_at: '2020-11-11T17:01:00+00:00'
updated_at: '2020-11-11T17:01:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Setting `set ask-passsword never` one would expect to "never" be prompted for a password after the initial wallet has been decrypted.  However that is not what I am seeing in v0.17.1.1:
```
set ask-passsword never
Wallet password:
set export-format ascii
Wallet password:
```

At the very least, options like `set export-format` with little or no security impact should not prompt for password.


# Discussion History
# Action History
- Created by: jonathancross | 2020-11-11T17:01:00+00:00
