---
title: 'Wallet initialization failed: basic_string::_M_replace_aux (v0.13.0.3 monero-gui)'
source_url: https://github.com/monero-project/monero/issues/4724
author: hrodrig
assignees: []
labels: []
created_at: '2018-10-25T15:10:49+00:00'
updated_at: '2018-10-25T23:27:11+00:00'
type: issue
status: closed
closed_at: '2018-10-25T23:27:11+00:00'
---

# Original Description
I updated to v0.13.0.3-release. "monerod" works but "monero-cli" gives an error.

When I go to open my wallet, if I specify a wrong password, it tells me the wrong password, but if I specify the correct password it says that:

**Error: basic_string::_M_replace_aux**

and I can not get into the wallet.

The only way is to recreate from the seed and once inside it works normal, more if I leave monero-cli and try again to enter, the same error occurs.

Any idea?

# Discussion History
## dEBRUYNE-1 | 2018-10-25T15:11:57+00:00
This will be fixed in GUI v0.13.0.4 and is already fixed in CLI v0.13.0.4 (which can be found [here](https://www.reddit.com/r/Monero/comments/9r7inb/cli_v01304_beryllium_bullet_released/)). In the meantime, you can use this workaround:

https://monero.stackexchange.com/questions/6611/cant-load-wallet-in-cli-v0-13-0-2-or-gui-v0-13-0-3-error-stdbad-alloc-err

## dEBRUYNE-1 | 2018-10-25T15:12:03+00:00
+resolved

# Action History
- Created by: hrodrig | 2018-10-25T15:10:49+00:00
- Closed at: 2018-10-25T23:27:11+00:00
