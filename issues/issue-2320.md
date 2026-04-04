---
title: Unbundle "connection type selection" and "difficulty selection"
source_url: https://github.com/monero-project/monero-gui/issues/2320
author: ghost
assignees: []
labels: []
created_at: '2019-07-25T21:27:33+00:00'
updated_at: '2019-09-04T09:11:06+00:00'
type: issue
status: closed
closed_at: '2019-09-04T09:11:06+00:00'
---

# Original Description
Currently "connection type selection" and "difficulty selection" are bundled:
![image](https://user-images.githubusercontent.com/46682965/64239480-9a77c180-cf00-11e9-9521-7dcdeaecc92f.png)


Proposal:
![image](https://user-images.githubusercontent.com/46682965/64240076-99935f80-cf01-11e9-9277-83a5bd92eefe.png)

Reasons:
- **This is SO CLEAR AND LOGICAL.**
- The wording is simple and non-technical. (Correct, though.)
- It sucks to have to close and reopen the wallet to change modes.
- Many users will suffer from reduced privacy because they will choose the mode that sounds the simplest to them, which is "Simple mode" (without bootstrap).
- A lot of other problems around our 3 modes (#2304, #2321)



# Discussion History
## GBKS | 2019-07-26T08:42:14+00:00
I looked into this earlier this year, here's one of my explorations (ignore the icons). I forgot the rationale why we ended up combining the options. Maybe somebody else remembers?

![monero-wallet-onboarding-node-mode-gbks-190211](https://user-images.githubusercontent.com/695901/61938625-d9296c00-af91-11e9-8435-5cd7587592d4.png)


## ghost | 2019-07-26T08:57:02+00:00
@GBKS ABSOLUTELY STUNNINGLY BEAUTIFUL AND LOGICAL!!! (We'd just need to add bootstrap mode)

## ghost | 2019-09-04T09:11:05+00:00
Closed and integrated in #2321.

# Action History
- Created by: ghost | 2019-07-25T21:27:33+00:00
- Closed at: 2019-09-04T09:11:06+00:00
