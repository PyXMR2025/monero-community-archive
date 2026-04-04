---
title: '[GUI] Selected button state unclear'
source_url: https://github.com/monero-project/monero-gui/issues/673
author: jonathancross
assignees: []
labels: []
created_at: '2017-04-12T17:10:29+00:00'
updated_at: '2018-09-26T22:22:30+00:00'
type: issue
status: closed
closed_at: '2018-09-26T22:22:30+00:00'
---

# Original Description
The buttons in the GUI are reversed from most UI conventions.  The "selected" button is displayed as low-contrast making the "unselected" buttons stand out (issue is amplified because of the orange color which dominates).

![2017-04-12_monero-buttons-mining](https://cloud.githubusercontent.com/assets/5115470/24969380/ec83be9a-1fb0-11e7-98ed-1d0d33c4a9bd.png)
<small>_Is it mining already?_</small>

I would suggest this be reversed:
When the user clicks a button, it should react by highlighting / "standing out" somehow, making it clear that the click was registered and that the button was selected. This gives the user a satisfying feeling of control over the UI which "responds" to their actions.

An option would be to reverse the rendering so that **unselected** buttons are low contrast because they are of lower importance.  However this can be hard to read with the current color scheme. Changing the text color could help, but we could also experiment with reduced color saturation for the disabled buttons and / or higher contrast text.

I'll follow up later with an additional concern related to interdependent buttons and GUI state.

Related: #145

# Discussion History
# Action History
- Created by: jonathancross | 2017-04-12T17:10:29+00:00
- Closed at: 2018-09-26T22:22:30+00:00
