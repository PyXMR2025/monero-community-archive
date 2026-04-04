---
title: '''ctrl-a'' shortcut conflict'
source_url: https://github.com/monero-project/monero-gui/issues/1374
author: 1337tester
assignees: []
labels:
- bug
- resolved
- easy
created_at: '2018-05-06T18:37:42+00:00'
updated_at: '2018-10-02T19:00:30+00:00'
type: issue
status: closed
closed_at: '2018-10-02T19:00:30+00:00'
---

# Original Description
**Problem**
This shortcut is used for selection of the whole text on the cursor location, using it also for Shared RingDB tab is leading to confusion for users trying to select the whole string in some field (they suddenly find themselves in a completely different tab -> at least my case initially)

**Solution**
Assign some other shortcut for for Shared RingDB tab (anything that does not collide with some commonly used OS shortcuts)

# Discussion History
## sanderfoobar | 2018-05-07T07:21:19+00:00
+bug
+easy

## pazos | 2018-05-08T16:30:29+00:00
I will go for rewrite the 'ctrl+tab' logic too, because seems random. The logic order would be Transfer->adressbook->Receive->Advanced-tabs->Options. I would skip the seeds page because I think it would stop the workflow asking for a password.

~~Any suggestion for an alternative to 'ctrl+a' to switch to Shared Ring DB? I can include that fix too.~~
Nevermind, the shortcut was duplicated -> ctrl+a and ctrl+s. I will leave only ctrl+s

## dEBRUYNE-1 | 2018-10-02T18:59:49+00:00
+resolved

# Action History
- Created by: 1337tester | 2018-05-06T18:37:42+00:00
- Closed at: 2018-10-02T19:00:30+00:00
