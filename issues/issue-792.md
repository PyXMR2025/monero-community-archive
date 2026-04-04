---
title: 'Monero-wallet-gui MAC disappears from DOCK when locked in dock '
source_url: https://github.com/monero-project/monero-gui/issues/792
author: BigslimVdub
assignees: []
labels: []
created_at: '2017-07-09T23:45:16+00:00'
updated_at: '2017-08-07T15:25:31+00:00'
type: issue
status: closed
closed_at: '2017-07-28T01:14:44+00:00'
---

# Original Description
I have a bug for monero wallet on MAC osx.
I lock the wallet to the dock and it stays there. After a couple days of non use (or powering my computer down) the image on the dock for monero is a " ? " on the dock but when you hover over it does show "monero-wallet-gui".
It does not open from this. I have to manually go to ~/library to find and open the gui and it works fine and I can re-lock to the dock.
Anyone else having this issue?
Everything else works fine no problems so far (sans super slow sync to network for update blocks)
![monero gui fault](https://user-images.githubusercontent.com/30030687/27998534-b02b09a6-64d6-11e7-8f03-5e4b5de639f0.jpg)


# Discussion History
## jonathancross | 2017-07-16T20:09:52+00:00
> Anyone else having this issue?

I have never seen this issue on my Mac (MBA with El Capitan).  Have been using self-compiled versions in various locations + official release binary installed in `/Applications/`.  Maybe try moving it to that location?

## BigslimVdub | 2017-07-20T01:34:07+00:00
Just as an update, I moved miners GUI and sub folders to my /users/ in a new folder and it still disappears after 2 days of no use. I will try to move the GUI to /applications/ but when I moved other clients there from ~/library/ sub folders it lost its file directory and went to load as a new gui. Monero-gui did not do this when I moved it from ~/library/ sub folder the initial install was on. 

## jonathancross | 2017-07-24T15:29:15+00:00
Thanks @BigslimVdub, have you tried dragging the app from finder window to the dock instead of using the "Keep in Dock" method?

## BigslimVdub | 2017-07-24T17:37:37+00:00
No not yet. I will try that today. 

## BigslimVdub | 2017-07-28T01:14:44+00:00
@jonathancross I Drag and drop the GUI from my folder and its been 2 days with no disappearing. I will go ahead and close this out and if I have any further issues I will reopen. 

Thank you 

# Action History
- Created by: BigslimVdub | 2017-07-09T23:45:16+00:00
- Closed at: 2017-07-28T01:14:44+00:00
