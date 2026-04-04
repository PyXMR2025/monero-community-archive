---
title: 2 additional spaces added after passphrase is pasted from clipboard in dialogue
source_url: https://github.com/monero-project/monero/issues/5736
author: bosomt
assignees: []
labels:
- invalid
created_at: '2019-07-05T08:59:08+00:00'
updated_at: '2019-07-05T09:55:32+00:00'
type: issue
status: closed
closed_at: '2019-07-05T09:25:46+00:00'
---

# Original Description
2 additional spaces added after passphrase is pasted from clipboard in dialogue
Please see screenshot.
If paste your passphrase wallet will add 2 more spaces.
This will generate completely different wallet/account/address compared to passphrase that you enter via keyboard 
![image](https://user-images.githubusercontent.com/31506317/60710846-dea41100-9f13-11e9-8725-c5028300249e.png)

![image](https://user-images.githubusercontent.com/31506317/60710708-9b49a280-9f13-11e9-96c5-a533297142d3.png)


# Discussion History
## moneromooo-monero | 2019-07-05T09:17:29+00:00
Please file on the GUI repo: https://github.com/monero-project/monero-gui

I assume you double checked you did not copy those spaces in the first place (if, if you paste into a text editor, you don't get the spaces) ? It might also be a newline, these should be filtered out I guess.

+invalid


## bosomt | 2019-07-05T09:55:32+00:00
@moneromooo-monero sorry, i will open it there. No there is no space included and this problem is there since we started to test Trezor integration

# Action History
- Created by: bosomt | 2019-07-05T08:59:08+00:00
- Closed at: 2019-07-05T09:25:46+00:00
