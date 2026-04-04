---
title: 'Settings page: redesign change password process'
source_url: https://github.com/monero-project/monero-gui/issues/2521
author: rating89us
assignees: []
labels: []
created_at: '2019-11-27T18:41:58+00:00'
updated_at: '2020-01-07T18:29:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Imagine a user wants to change his password:
![image](https://user-images.githubusercontent.com/45968869/69750346-d52e7600-114c-11ea-8d1d-c5eba1b44ae4.png)

This dialog opens:
![image](https://user-images.githubusercontent.com/45968869/69750363-dfe90b00-114c-11ea-9adb-4e6778c222c4.png)

But what password should be entered here? The current password? The new password?

If you type the current password, then you see:
![image](https://user-images.githubusercontent.com/45968869/69750431-0c048c00-114d-11ea-9471-b77d14099fcf.png)

So why don't we do like all traditional change password forms and display three password fields in the same page? 

My suggestion:
![image](https://user-images.githubusercontent.com/45968869/69752946-af0bd480-1152-11ea-8155-f5ab904a2b1f.png)

Some ideas:
- Passwords don't match: turn text input border red + display error message. Currently `Ok` button gets disabled and no error message is displayed
- Passwords match: display green check sign
- Display password strength indicator (#2666)

# Discussion History
## selsta | 2019-11-27T18:43:59+00:00
I think I’ve seen a lot of processes that were current password -> 2x new password. But you are right, the first screen should say current password.

## rating89us | 2019-11-27T18:46:58+00:00
I believe that displaying three fields in the same page is more common and should be preferred.

But sure, changing the text in the first dialog is the easiest thing to do here.

# Action History
- Created by: rating89us | 2019-11-27T18:41:58+00:00
