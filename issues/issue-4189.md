---
title: 'Can''t create transaction: not enough money to transfer'
source_url: https://github.com/monero-project/monero-gui/issues/4189
author: '0x241F31'
assignees: []
labels: []
created_at: '2023-06-22T09:20:26+00:00'
updated_at: '2023-06-22T13:47:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have `Total unlocked balance: 0.086504114542 XMR`
Trying to send `0.08510` and getting this error:
![image](https://github.com/monero-project/monero-gui/assets/17229619/e68d7564-78a3-4ae0-9206-b482a4115342)
0.0865 > 0.0864, wut?
Tried to change transaction priority to lowest, no difference. 
However, setting amount to (all) allows to send.
![image](https://github.com/monero-project/monero-gui/assets/17229619/060c3691-1fc3-44a4-b93e-78f0e3545cc6)




# Discussion History
## selsta | 2023-06-22T12:34:47+00:00
Can you reproduce the issue with monero-wallet-cli?

## 0x241F31 | 2023-06-22T13:47:40+00:00
> Can you reproduce the issue with monero-wallet-cli?

Have no money anymore, will try when get them

# Action History
- Created by: 0x241F31 | 2023-06-22T09:20:26+00:00
