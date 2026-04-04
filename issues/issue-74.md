---
title: In-memory encryption of privkeys
source_url: https://github.com/monero-project/monero/issues/74
author: fluffypony
assignees: []
labels:
- enhancement
created_at: '2014-08-02T09:47:26+00:00'
updated_at: '2025-12-19T15:05:50+00:00'
type: issue
status: closed
closed_at: '2025-12-19T15:05:50+00:00'
---

# Original Description
To prevent them ever being paged to disk unencrypted, they should be encrypted in-memory until they are needed.

Reference in terms of how Bitcoin does it (we don't have to follow their model 1:1) - https://bitcointalk.org/index.php?topic=8728.0

per @gmaxwell - "best effort mlocked, zeroized when the wallet is no longer unlocked or when freed."


# Discussion History
## ghost | 2016-11-10T00:30:37+00:00
@fluffypony has anyone taken this forward?


## fluffypony | 2016-11-10T07:06:52+00:00
@nanoakron no not yet


## dEBRUYNE-1 | 2018-01-08T12:42:07+00:00
+enhancement

## moneromooo-monero | 2018-02-10T11:39:10+00:00
Partially done with jroelofs' patches above, still some left to do though.

## stoffu | 2018-02-10T14:56:39+00:00
IIUIC the ringct code lumps the different kinds of data (pubkey/seckey/hash) into a single type `rct::key`, and thus the encryption for the secret key isn’t achieved yet.

## selsta | 2025-12-19T15:05:45+00:00
As far as I know, this has been implemented for a while. If not, I can reopen it.

# Action History
- Created by: fluffypony | 2014-08-02T09:47:26+00:00
- Closed at: 2025-12-19T15:05:50+00:00
