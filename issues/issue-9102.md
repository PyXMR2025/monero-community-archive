---
title: Bug with input-transaction
source_url: https://github.com/monero-project/monero/issues/9102
author: developergames2d
assignees: []
labels:
- question
created_at: '2023-12-24T22:25:25+00:00'
updated_at: '2023-12-24T22:32:50+00:00'
type: issue
status: closed
closed_at: '2023-12-24T22:32:39+00:00'
---

# Original Description
I got moneros to #2-address, but monero-gui writes #0.
![image](https://github.com/monero-project/monero/assets/106807841/ad1853d9-93d8-452c-a692-c4893bdd69e9)



# Discussion History
## developergames2d | 2023-12-24T22:28:00+00:00
Maybe it #0-subaddress of addres #2...

## selsta | 2023-12-24T22:32:39+00:00
Please open GUI related issues here: https://github.com/monero-project/monero-gui/issues

Regarding your question, you have account 2 selected and you receives funds in subaddress 0.

Each account has its own list of subaddresses.

# Action History
- Created by: developergames2d | 2023-12-24T22:25:25+00:00
- Closed at: 2023-12-24T22:32:39+00:00
