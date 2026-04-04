---
title: Wayland support
source_url: https://github.com/monero-project/monero-gui/issues/4014
author: Froggy232
assignees: []
labels: []
created_at: '2022-08-23T14:04:15+00:00'
updated_at: '2025-12-23T16:00:10+00:00'
type: issue
status: closed
closed_at: '2022-08-23T17:37:52+00:00'
---

# Original Description
Hello,
Sorry if it's not the good place, I'm not an expert user of github.
Would it be feasible to have monero-gui run on wayland in place of X11/xwayland?
I have found a thread about it, but it date from 2018, qt visibly wasn't compatible with wayland at that date but it should be now.
Thanks you

# Discussion History
## q7nm | 2022-08-23T16:51:28+00:00
You can run it with `QT_QPA_PLATFORM=wayland`.

## Froggy232 | 2022-08-23T16:54:19+00:00
Nice, thanks you a lot, it works!
Maybe is it possible to make it the default option? On gnome at least, it uses xwayland.

## q7nm | 2022-08-23T17:21:36+00:00
> Nice, thanks you a lot, it works! Maybe is it possible to make it the default option? On gnome at least, it uses xwayland.

I think it's not very stable now.



## Froggy232 | 2022-08-23T17:35:27+00:00
Ok, I understand.
Thanks for your help.

## selsta | 2022-08-23T17:37:51+00:00
Closing this as the question seems answered by using the env var.

## q7nm | 2025-12-23T15:59:49+00:00
@selsta 
In a pure Wayland session (like in flatpak with --socket=fallback-x11 on Wayland), the application simply [crashes](https://github.com/flathub/org.getmonero.Monero/issues/208). Maybe it's worth making it so that Wayland is used at least when X11 isn't available, or making it the default (it works quite well now)? Of course, in an X11 session, everything should remain the same.

# Action History
- Created by: Froggy232 | 2022-08-23T14:04:15+00:00
- Closed at: 2022-08-23T17:37:52+00:00
