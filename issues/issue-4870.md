---
title: Hot wallet complains about missing key images after offline send
source_url: https://github.com/monero-project/monero/issues/4870
author: rndbr
assignees: []
labels: []
created_at: '2018-11-19T21:30:53+00:00'
updated_at: '2019-03-19T15:09:46+00:00'
type: issue
status: closed
closed_at: '2019-03-19T15:09:46+00:00'
---

# Original Description
I'm wondering if there has been a regression with offline signing in 13.0.x. I'm running 13.0.4 and doing a normal offline send (`transfer` from the hot wallet, then `sign_transfer` from cold wallet, then `submit_transfer` from hot wallet) will have the balance command showing `"Some owned outputs have missing key images - import_key_images needed"`.

I've done it with no issues since the feature was first added a year or two ago. To fix this I need to do the whole `export_outputs` -> `import_outputs` -> `export_key_images` -> `import_key_images` dance. It seems the key images may not be moving back over properly in the `signed_monero_tx` file?

I was able to reproduce this issue:

* After I had the issue, I did a `rescan_bc` on the hot wallet to reset the balance state.
* I then did `export_outputs` on hot wallet -> `import_outputs` on cold wallet -> `export_key_images` on cold wallet -> `import_key_images` on hot wallet. Balance showed up correctly on the hot wallet and the `balance` command was normal (no mention of missing key images)
* I then did an offline send (`transfer` from the hot wallet, then `sign_transfer` from cold wallet, then `submit_transfer` from hot wallet)
* After receiving the change, the `balance` command on the hot wallet now shows: 

```
[wallet 42dZ6t]: balance
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: XXXX, unlocked balance: XXXX (Some owned outputs have missing key images - import_key_images needed)
```

I sent the XMR to an address that uses an encrypted payment ID, if that matters.

_Versions:_
* Hot wallet: `Monero 'Beryllium Bullet' (v0.13.0.4-release)`
* Cold wallet: `Monero 'Beryllium Bullet' (v0.13.0.4-release)`

The hot wallet binaries were compiled from the 13.0.4 git tagged source on Ubuntu 18.04.1. The cold wallet binaries were downloaded from github (I used the Linux x64 version, and am running them on an older version of Ubuntu...16.04 I believe).


# Discussion History
## rndbr | 2018-12-04T13:41:21+00:00
hi, just checking in on this issue, to see if it was able to be reproduced

## moneromooo-monero | 2018-12-25T14:28:27+00:00
https://github.com/monero-project/monero/pull/5014

## moneromooo-monero | 2019-03-19T14:17:59+00:00
+resolved

# Action History
- Created by: rndbr | 2018-11-19T21:30:53+00:00
- Closed at: 2019-03-19T15:09:46+00:00
