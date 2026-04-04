---
title: Inactivity screen lock covers Transaction confirmation dialog
source_url: https://github.com/monero-project/monero-gui/issues/3511
author: stephan-henningsen
assignees: []
labels: []
created_at: '2021-05-27T14:23:29+00:00'
updated_at: '2021-06-01T06:39:36+00:00'
type: issue
status: closed
closed_at: '2021-06-01T06:39:36+00:00'
---

# Original Description
Test case:

1. Perform transaction
2. Stay at confirmation dialog
3. Have screen lock engage

Observed:
1. The lock screen fades the main screen
2. The confirmation dialog stays readable
3. The screen lock components are drawn on top of confirmation dialog
4. Both the confirmation components and screen lock components can be interacted with, e.g. buttons can be pressed.

Expected (I suppose):
1. The screen lock covers and blurs everything.
2. Only the screen lock can be interacted with.
3. When unlocked, the user is returned to the confirmation dialog.

![image](https://user-images.githubusercontent.com/7459151/119842971-6aa7f300-bf07-11eb-9fd7-9bdb81b1db14.png)



# Discussion History
## stephan-henningsen | 2021-05-27T14:24:32+00:00
GUI version: 0.17.2.2-937cb98 (Qt 5.15.2)
Embedded Monero version:  0.17.2.0-release
Ubuntu 20.04.2 LTS

## stephan-henningsen | 2021-05-27T14:25:54+00:00
Rumors has it that this happens on Windows too.

# Action History
- Created by: stephan-henningsen | 2021-05-27T14:23:29+00:00
- Closed at: 2021-06-01T06:39:36+00:00
