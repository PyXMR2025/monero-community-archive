---
title: When creating a wallet in Simple Mode with no internet, the GUI hangs after
  prompting for a password
source_url: https://github.com/monero-project/monero-gui/issues/2252
author: dginovker
assignees: []
labels: []
created_at: '2019-07-03T14:57:27+00:00'
updated_at: '2021-06-29T03:12:19+00:00'
type: issue
status: closed
closed_at: '2021-06-29T03:12:19+00:00'
---

# Original Description
It's looking for remote nodes and after a while it says "No remote nodes found" (something akin to that), but during the search the user has no idea what is going on, simply that "Next" isn't functioning.

# Discussion History
## selsta | 2019-07-03T15:10:31+00:00
Works fine on my system. Can you post the exact steps to reproduce?

## sanderfoobar | 2019-07-03T15:25:46+00:00
context;

https://github.com/monero-project/monero-gui/blob/5f38dbb7dd3c25755427b103ae389ccc619b6c42/wizard/WizardController.qml#L562-L570

## dginovker | 2019-07-03T15:26:42+00:00
Looking closer, it seems this happens when internet is connected, but can't do anything meaningful because it's too slow or has other issues. In this case, you click "Next" and the GUI appears to do nothing. If the internet is fully unplugged, the GUI will immediately notify you.

## sanderfoobar | 2019-07-03T15:30:20+00:00
Made an issue.

## selsta | 2021-06-29T03:12:19+00:00
We don't use this system for simple mode anymore, thus closing.

# Action History
- Created by: dginovker | 2019-07-03T14:57:27+00:00
- Closed at: 2021-06-29T03:12:19+00:00
