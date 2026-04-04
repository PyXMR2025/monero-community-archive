---
title: Initial config written is wrong
source_url: https://github.com/monero-project/monero-gui/issues/151
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-11T11:45:24+00:00'
updated_at: '2016-11-13T18:03:48+00:00'
type: issue
status: closed
closed_at: '2016-11-13T18:03:48+00:00'
---

# Original Description
How to reproduce:


- delete Registry in HKEY_CURRENT_USER/software/The Monero Project/
- start monero-core

registry will look like this:
![wrong_reg](https://cloud.githubusercontent.com/assets/17108301/20214139/872d7ade-a80c-11e6-85b3-e7364e92349a.png)


this cause known follow up issues, like genesis-missmatch. 

--> happened with hyc's newest build, which is based on https://github.com/Jaqueeee/monero-core/tree/dev





# Discussion History
## medusadigital | 2016-11-11T21:55:20+00:00
definetely related to the spontaneous creation of testnet wallets. i created several testnet wallets, besides the option being unaviable in the GUI


## medusadigital | 2016-11-13T18:03:48+00:00
fixed--> wroks --> closed


# Action History
- Created by: medusadigital | 2016-11-11T11:45:24+00:00
- Closed at: 2016-11-13T18:03:48+00:00
