---
title: Can't see grab QR code icon
source_url: https://github.com/monero-project/monero-gui/issues/3396
author: rating89us
assignees: []
labels: []
created_at: '2021-04-14T19:23:46+00:00'
updated_at: '2021-04-16T17:56:09+00:00'
type: issue
status: closed
closed_at: '2021-04-16T17:56:09+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/45968869/114767195-a330aa80-9d67-11eb-8105-128a2ca033d4.png)

all other fontawesome icons on the monero gui are displayed normally

Windows 7 64 bits
GUI version: 0.17.2.0-816eeb46 (Qt 5.15.2)

# Discussion History
## selsta | 2021-04-14T19:35:11+00:00
might be fixed by #3397

## rating89us | 2021-04-15T06:40:58+00:00
Unfortunately it's not fixed by #3397:

![image](https://user-images.githubusercontent.com/45968869/114825243-3f899a00-9dc6-11eb-9570-973067f5b608.png)
GUI version: 0.17.2.1-2-g6116b972 (Qt 5.15.2)


## selsta | 2021-04-15T12:56:55+00:00
@rating89us I just force pushed, please check again in ~2h here: https://github.com/monero-project/monero-gui/actions/runs/752081047

## rating89us | 2021-04-15T18:45:40+00:00
@selsta 
Great, now it's working: 
![image](https://user-images.githubusercontent.com/45968869/114922030-7cd44300-9e2b-11eb-9082-c4ad8f91ef9c.png)


## selsta | 2021-04-15T18:46:34+00:00
@rating89us thanks for testing, please approve the PR.

# Action History
- Created by: rating89us | 2021-04-14T19:23:46+00:00
- Closed at: 2021-04-16T17:56:09+00:00
