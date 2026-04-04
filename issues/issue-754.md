---
title: 'GUI 2: On Send Page, the buttons at the bottom are partially hidden.'
source_url: https://github.com/monero-project/monero-gui/issues/754
author: dontbuymonero
assignees: []
labels:
- resolved
created_at: '2017-05-31T17:45:16+00:00'
updated_at: '2018-07-17T14:36:31+00:00'
type: issue
status: closed
closed_at: '2018-07-17T14:36:31+00:00'
---

# Original Description
When you launch the GUI, it opens to its default size (which you can increase with the arrow on the bottom right corner). In this default size, on the send page, the bottom 3 buttons (create tx file, sign tx file, submit tx file), are mostly hidden. These buttons should always be clearly visible to the user when the GUI is in its default size and it should not be necessary to expand in order to fully view/use them.

# Discussion History
## jonathancross | 2017-06-06T00:18:23+00:00
Yeah, the UI does not scroll or scale, so if your window is too small, you simply can't reach the items at the bottom ("advanced options" in this case).  We should look into a general pattern for such situations (scrollbars work, but are pretty terrible. Scaling UI elements might help, but can also lead to bad situations).

_Payment ID_ and _Description_ are optional, so there might be a way to collapse those and some surrounding whitespace if screen real estate is needed.

We can also consider establishing a minimum height for the app (based on the left nav probably) and then adjust the UI to always fit inside.
Looks like min is about 700px now.

Any other ideas on how to solve this problem?

## Jaqueeee | 2017-06-06T08:11:08+00:00
Current master supports scrolling (with scroll-wheel or ), but i agree it's a bad solution for the desktop app. I added that for the mobile versions mostly. I think minimum height/width is the best solution, and scrolling for smaller screens. @jonathancross @dontbuymonero 

## jonathancross | 2017-06-06T12:21:28+00:00
Thanks for the feedback @Jaqueeee.
Once the UI is a bit more stable, we can tighten things up (there is a lot of misused space).

I played around with the idea of something like an "accordion" pattern where the **Advanced options** and **Payment details** are exclusive -- only one can be open at a time.

Here is a really rough mock just to demonstrate (has too many arrows, etc!).

Payment details editing mode (default):
![2017-06-06_height_editpaymentdetails](https://cloud.githubusercontent.com/assets/5115470/26828597/8abdbc00-4ac2-11e7-9c0a-151526a0298c.png)


Advanced Options mode (when there are no payment details):
![2017-06-06_height_adavanced_ no-pymt-details](https://cloud.githubusercontent.com/assets/5115470/26828602/91dad8ce-4ac2-11e7-91e0-ccfec99ab92c.png)


Advanced Options mode (with payment details):
![2017-06-06_height_adavanced_ with-pymt-details](https://cloud.githubusercontent.com/assets/5115470/26828615/9dcf82ce-4ac2-11e7-9947-28df2b9f0d00.png)


I'm not sure this is a good idea, but it would allow us to avoid scrollbars and make sure all content is accessible in small windows.  There is a little complexity added in keeping track of the various states, but I think it improves usability a lot.

Another option would be to have the _Advanced Options_ always visible, but collapse _Ring Size_ into a button until the user selects it.  Ring Size is not going be be a common adjustment in comparison to adding payment ID / description.

While doing these, I had the thought that for mobile, _Advanced Options_ should probably be a modal window that fills the screen.

## visdude | 2017-06-12T21:44:12+00:00
Since this issue is generally similar to mine, I am just going to add related GUI quirks on here instead of opening a new one.

I am using a Netbook (set up as my cold/offline device) with a typical **1024 x 600** maximum screen resolution. The following are my observations of unusual GUI behavior (default window size after launching) related to this window scaling issue according to OS:

Windows 7 x64:

[1]  title bar (along with its control buttons) at the top and the bottom portion of the window are cut off and inaccessible
[2]  window resizing feature (by dragging window edges) is not functional
[3]  vertical/horizontal scrolling (to access cut off areas of window) is not functional.

Linux Mint 18.1 x64:

[1]  title bar is not cut off and accessible; bottom portion is cut off
[2]  window resizing feature is functional
[3]  nevertheless, vertical/horizontal scrolling is still not functional.

It would be nice if the Monero GUI window behaves just like a typical app window on Windows or Linux for that matter  (i.e. Bitcoin Core, Armory, etc.) with functional window resizing/scrolling features regardless of a device's optimal screen resolution.

The following are Windows 7 x64 sample screenshots:

![w7-1](https://user-images.githubusercontent.com/29369222/27055466-16c18b5a-4fb4-11e7-8ef7-4e07122e2b36.jpg)

![w7-2](https://user-images.githubusercontent.com/29369222/27055681-af85cb26-4fb4-11e7-832e-111269988666.jpg)

![w7-3](https://user-images.githubusercontent.com/29369222/27055698-c52342d8-4fb4-11e7-989f-e205e01e620e.jpg)

![w7-4](https://user-images.githubusercontent.com/29369222/27055723-d75f7bec-4fb4-11e7-80d8-ca46de8c253e.jpg)




## sanderfoobar | 2018-07-17T13:56:55+00:00
Resolved since newer versions of the GUI (black-theme).

+resolved

# Action History
- Created by: dontbuymonero | 2017-05-31T17:45:16+00:00
- Closed at: 2018-07-17T14:36:31+00:00
