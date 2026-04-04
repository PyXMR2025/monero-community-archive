---
title: 'Error: Failed to initialize ring database: privacy enhancing features will
  be inactive'
source_url: https://github.com/monero-project/monero/issues/3722
author: nueverest
assignees: []
labels: []
created_at: '2018-04-28T20:03:13+00:00'
updated_at: '2019-03-28T22:09:08+00:00'
type: issue
status: closed
closed_at: '2018-04-28T20:03:18+00:00'
---

# Original Description
I upgraded from 0.11.1.0 to 0.12.0.0

When I run:
`./monero-wallet-cli`

I see:

```
Monero 'Lithium Luna' (v0.12.0.0-master-release)
....
Opened Wallet: ......
Error: Failed to initialize ring database: privacy enhancing features will be inactive
Starting refresh...
```

Even though I get this error I can see my unlocked balance.

However, I am unable to do a transfer.

**Update**

I read the logs and found.

> initialize ringdb: Failed to open rings database file '/home/*********/.shared-ringdb': Permission denied

So I ran `chown` to change ownership. The problem remained.

**Solution**

Run as Admin
`sudo ./monero-wallet-cli`

Error goes away.


# Discussion History
## italocoin-project | 2019-03-28T22:09:08+00:00
I think is because monero is running not as root but as user, i saw a commit that will start the daemon with user not root, someting like that, you can look it up

# Action History
- Created by: nueverest | 2018-04-28T20:03:13+00:00
- Closed at: 2018-04-28T20:03:18+00:00
