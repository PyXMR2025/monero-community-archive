---
title: Create a new password dialog
source_url: https://github.com/monero-project/monero-gui/issues/2204
author: sanderfoobar
assignees: []
labels:
- resolved
created_at: '2019-06-08T21:10:22+00:00'
updated_at: '2019-07-16T17:18:45+00:00'
type: issue
status: closed
closed_at: '2019-07-16T17:18:45+00:00'
---

# Original Description
There are 3 QML components for displaying a password dialog.

```bash
$ ls components | grep -i pass
NewPasswordDialog.qml
PassphraseDialog.qml
PasswordDialog.qml
```

Should be combined into one, modular QML component.

# Discussion History
## ghost | 2019-06-11T09:57:54+00:00
Not 100% sure if this belongs here (please tell me):
![image](https://user-images.githubusercontent.com/46682965/59261898-87758e00-8c3e-11e9-8999-cb995a412fde.png)

Reasons:

A) Clicking on "Change wallet" doesn't change your wallet, it just takes you back to the window before, where you can do many things, FOR EXAMPLE changing your wallet.

B) The wording can be misinterpreted like this: When a user actually closes his wallet to open another wallet, he may think "Do I have to click 'Change wallet' to confirm that I actually want to change my wallet now, or do I have to click 'Continue' to confirm that I want to continue to use my previous wallet?"

## selsta | 2019-07-16T17:02:43+00:00
+resolved

# Action History
- Created by: sanderfoobar | 2019-06-08T21:10:22+00:00
- Closed at: 2019-07-16T17:18:45+00:00
