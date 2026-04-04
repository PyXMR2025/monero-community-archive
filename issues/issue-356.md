---
title: Password kept when using Recovery wizard and then Creation wizard
source_url: https://github.com/monero-project/monero-gui/issues/356
author: ClementJnc
assignees: []
labels: []
created_at: '2016-12-24T10:05:03+00:00'
updated_at: '2017-05-05T09:53:11+00:00'
type: issue
status: closed
closed_at: '2017-05-05T09:53:11+00:00'
---

# Original Description
Reproduction steps:
1. Start the recovery of a wallet
2. Enter the private key
3. Enter a password 
4. Go back to the Welcome page
5. Start the creation of a wallet
6. Pass the mnemonic step
The password is already filled in (in both fields). If you delete the confirmation field and retype the password entered at step 3, you notice it is the same. 

# Discussion History
## medusadigital | 2017-01-18T08:11:55+00:00
reproducible with GUI Beta 1

## medusadigital | 2017-04-18T09:37:55+00:00
same with GUI Beta 2

# Action History
- Created by: ClementJnc | 2016-12-24T10:05:03+00:00
- Closed at: 2017-05-05T09:53:11+00:00
