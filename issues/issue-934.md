---
title: '[Feature] Show the version somewhere on the GUI screen (or have an ''About''
  button) (0.11.1.0)'
source_url: https://github.com/monero-project/monero-gui/issues/934
author: ronohara
assignees: []
labels: []
created_at: '2017-10-28T08:24:52+00:00'
updated_at: '2017-10-28T11:49:19+00:00'
type: issue
status: closed
closed_at: '2017-10-28T11:49:19+00:00'
---

# Original Description
The cli supports --version as a command, and the GUI needs to present this information somewhere as well.

I opened this issue in the wrong repo...  (monero-core) #2733.  I was advised that version is displayed on the settings screen. It is not.

Screen shot of Settings page https://postimg.org/image/1esaw4ia8b/   ...I have checked all the other screens too. None of them display the version.

# Discussion History
## dEBRUYNE-1 | 2017-10-28T10:16:47+00:00
If you scroll down (on the `Settings` page) or drag the page you'll see the version number. It's under `Debug info`. 

## ronohara | 2017-10-28T11:49:19+00:00
Ok -- I finally worked out how 'scroll' works in the GUI - but it is not obvious because there are no scroll bars indicating that the screen content extends beyond the visible pane, and as a result you have to guess, and work out that you use the mouse to drag the contents up/down.

Scroll bars are the conventional way to offer scrolling, and indicate there is more content.

# Action History
- Created by: ronohara | 2017-10-28T08:24:52+00:00
- Closed at: 2017-10-28T11:49:19+00:00
