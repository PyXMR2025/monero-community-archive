---
title: impossible to create a view-only wallet (v0.13.0.2)
source_url: https://github.com/monero-project/monero/issues/4566
author: solartune
assignees: []
labels: []
created_at: '2018-10-12T10:41:49+00:00'
updated_at: '2018-10-15T12:32:57+00:00'
type: issue
status: closed
closed_at: '2018-10-15T12:32:57+00:00'
---

# Original Description
Hello everyone! And thank you for the new release of Monero!
Unfortunately I've faced with a problem using new 0.13.0.2 version. When I'm trying to create a view-only stagenet wallet with `--stagenet --generate-from-view-key` flags, I get an error: 
```Error: failed to parse view key secret key```

 **BUT** I can restore a stagenet wallet from both (spend and view keys) using `--stagenet --generate-from-keys` flags. In this case I have no problems with parsing view key.
I've tried to do that again using the previous version (0.12.3.0) and it worked. I can restore the view-only wallet without any problems using this version. But no way with the new one

# Discussion History
## normoes | 2018-10-12T10:53:54+00:00
I am faced with the same problem on mainnet (using `v0.13.0.2`).

When trying to generate a read only wallet like this:
```
monero-wallet-cli --generate-from-view-key view_only
```
After inserting the wallet's address and the secret view key, it just says
```
Error: failed to parse view key secret key
```

## moneromooo-monero | 2018-10-12T12:55:28+00:00
https://github.com/monero-project/monero/pull/4567

## moneromooo-monero | 2018-10-15T12:30:04+00:00
+resolved

# Action History
- Created by: solartune | 2018-10-12T10:41:49+00:00
- Closed at: 2018-10-15T12:32:57+00:00
