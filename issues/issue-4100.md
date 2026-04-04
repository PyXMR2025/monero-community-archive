---
title: Ubuntu and Windows actions not completing
source_url: https://github.com/monero-project/monero-gui/issues/4100
author: brg2
assignees: []
labels: []
created_at: '2023-01-10T17:48:19+00:00'
updated_at: '2023-02-27T22:53:55+00:00'
type: issue
status: closed
closed_at: '2023-02-27T22:53:54+00:00'
---

# Original Description
Ubuntu just needs qt5-default replaced with qtchooser, qt5-qmake and qtbase5-dev-tools (I have a fix [here](https://github.com/monero-project/monero-gui/pull/4099))
Not sure what windows needs but it halts at obj_epee:
![image](https://user-images.githubusercontent.com/760126/211624545-e5018519-c6b6-42de-a445-e138f9934e85.png)



# Discussion History
## selsta | 2023-01-10T17:50:26+00:00
Ubuntu will be solved by #4079 and Windows will be solved by https://github.com/monero-project/monero/pull/8683

## selsta | 2023-02-27T22:53:54+00:00
Resolved in #4120 

# Action History
- Created by: brg2 | 2023-01-10T17:48:19+00:00
- Closed at: 2023-02-27T22:53:54+00:00
