---
title: Title bar should be permanently shown
source_url: https://github.com/monero-project/monero-gui/issues/141
author: antanst
assignees: []
labels: []
created_at: '2016-11-09T20:03:54+00:00'
updated_at: '2016-11-17T19:43:57+00:00'
type: issue
status: closed
closed_at: '2016-11-17T19:43:57+00:00'
---

# Original Description
The fact that the title bar is in "auto-hide" mode, has the following consequences:

* The title bar has to be activated for the window to be moved. Because it can't be activated when a dialog is shown (like the password or sync progress dialogs) there's no way to move the window then.

* It's a non-standard behaviour that confuses new users.

I suggest that the title bar is fixed and on by default as in almost all applications.

# Discussion History
## moneromooo-monero | 2016-11-13T13:26:55+00:00
I'm unsure what it is for. I think it might as well be removed, as it doesn't actually do anything AFAICT.
Moving the window works just fine using the window manager's top bar here.


## antanst | 2016-11-13T13:36:49+00:00
I'm not sure I understood your comment. At least in Linux, the window manager's topbar is overridden by the GUI's custom top bar (which is black and has the close buttons on the right, contrary to system defaults). In addition, this top bar is hidden automatically by default, hence my initial comment.


## Jaqueeee | 2016-11-13T17:57:16+00:00
@mbg033 Can we make top bar permanently visible or is there a reason it behaves this way?


## dternyak | 2016-11-13T18:02:52+00:00
I agree with this being an issue on macOS and also agree with the solution being to make the top bar permanently visible. 


## medusadigital | 2016-11-13T23:01:16+00:00
the only downside would be that the cool rainbow stripe on top wouldnt be visible anymore (is this a leftover of the initial color choices ?) . anyway im cool with everything personally. 


## mbg033 | 2016-11-14T18:36:59+00:00
@Jaqueeee, yes, we obviously can, but it was designed "auto-hidden" from the beginning (not by me). Anyway, I can prepare PR with permanently visible titlebar soon.
Personally, I'm not a big fan of such "custom-painted-title-bars", for me window manager's title bar is better, but here "normal view/simple view" toggle depends on it.


## M5M400 | 2016-11-15T12:12:16+00:00
I second that request. In simple view the title bar is also fixed. I prefer that.


## antanst | 2016-11-17T19:43:57+00:00
Thanks for the fix! Closing.


# Action History
- Created by: antanst | 2016-11-09T20:03:54+00:00
- Closed at: 2016-11-17T19:43:57+00:00
