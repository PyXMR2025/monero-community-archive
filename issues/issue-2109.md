---
title: '[Trezor] - Showing passphrase does not reset'
source_url: https://github.com/monero-project/monero-gui/issues/2109
author: vir-satoshi
assignees: []
labels: []
created_at: '2019-04-24T11:40:15+00:00'
updated_at: '2019-04-25T18:14:48+00:00'
type: issue
status: closed
closed_at: '2019-04-25T18:14:48+00:00'
---

# Original Description
If I uncheck the showing passphrase in Monero wallet for Trezor, the modal does not reset himself after the modal was used. So when next time the modal ask you to type the passphrase, it is unchecked...

![image](https://user-images.githubusercontent.com/37402655/56656521-049c7200-6696-11e9-8aa9-b5c33f289171.png)

This is a security flaw, unintentionally you can reveal your passphrase to someone by not be aware of this feature. 

My proposal is to reset the show passphrase button every time the modal shows up. 
@ph4r05 

# Discussion History
## selsta | 2019-04-24T11:50:38+00:00
Same behaviour with normal password input. I’ll fix it.

## selsta | 2019-04-24T12:22:50+00:00
#2111

## ph4r05 | 2019-04-24T13:39:35+00:00
@vir-satoshi good catch! The proposal makes sense. @selsta thanks for the fix!

# Action History
- Created by: vir-satoshi | 2019-04-24T11:40:15+00:00
- Closed at: 2019-04-25T18:14:48+00:00
