---
title: 2 additional spaces added after passphrase is pasted from clipboard in dialogue
source_url: https://github.com/monero-project/monero-gui/issues/2271
author: bosomt
assignees: []
labels:
- invalid
created_at: '2019-07-05T09:56:55+00:00'
updated_at: '2019-07-15T13:09:43+00:00'
type: issue
status: closed
closed_at: '2019-07-15T13:09:43+00:00'
---

# Original Description
2 additional spaces added after passphrase is pasted from clipboard in dialogue
Please see screenshot.
If paste your passphrase wallet will add 2 more spaces.
This will generate completely different wallet/account/address compared to passphrase that you enter via keyboard

And no spaces are not included in pasted text

![60710708-9b49a280-9f13-11e9-96c5-a533297142d3](https://user-images.githubusercontent.com/31506317/60714720-e962a400-9f1b-11e9-9116-0478eb1610fd.png)
![60710846-dea41100-9f13-11e9-8725-c5028300249e](https://user-images.githubusercontent.com/31506317/60714722-e962a400-9f1b-11e9-8fce-3dfa31af2a47.png)


# Discussion History
## selsta | 2019-07-15T12:54:34+00:00
Thanks for the report but I can’t reproduce this issue. Looks like you copied your password together with a newline afterwards.

If this issue still persists after upgrading to v0.14.1.1 (should be out soon), please open a new issue. 

+invalid

# Action History
- Created by: bosomt | 2019-07-05T09:56:55+00:00
- Closed at: 2019-07-15T13:09:43+00:00
