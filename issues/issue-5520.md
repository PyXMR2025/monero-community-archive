---
title: encrypted_seed passwords do not match
source_url: https://github.com/monero-project/monero/issues/5520
author: selsta
assignees: []
labels: []
created_at: '2019-05-07T03:11:42+00:00'
updated_at: '2019-05-07T09:43:56+00:00'
type: issue
status: closed
closed_at: '2019-05-07T09:43:06+00:00'
---

# Original Description
```
[wallet 59aZUL]: encrypted_seed
Wallet password: 
Enter optional seed offset passphrase, empty to see raw seed: 
Confirm password: 
Passwords do not match! Please try again.
```
I can’t get this to work. If I understand it correctly, I enter my password first, then enter my seed offset (that I can choose freely) and then I enter my password again. I always get “Passwords do not match”. The only way I can get this to work is if I enter my password as seed offset passphrase.

# Discussion History
## moneromooo-monero | 2019-05-07T09:37:25+00:00
If I understand what you said, you entered X Y X instead of Y X X ?
It wants you to confirm the *new* encryption password, not the one from two steps before.


## selsta | 2019-05-07T09:43:06+00:00
I totally misunderstood this, I thought it was asking for my wallet password. Thanks for clarifying. Maybe it would be good to change it to `Confirm passphrase`.

# Action History
- Created by: selsta | 2019-05-07T03:11:42+00:00
- Closed at: 2019-05-07T09:43:06+00:00
