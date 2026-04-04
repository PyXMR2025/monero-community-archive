---
title: Mode selection window is a trap and complicated.
source_url: https://github.com/monero-project/monero-gui/issues/2321
author: ghost
assignees: []
labels: []
created_at: '2019-07-26T07:14:38+00:00'
updated_at: '2019-11-27T18:23:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Problems:
- The mode selection window forces you to select something but you can't go back.
- It doesn't tell you the current mode.
- It sucks to have to close and reopen the wallet to change modes.
- The mode selection window doesn't allow us to preselect something during setup.
- Many users suffer from reduced privacy because they choose the mode that sounds the simplest to them, which is "Simple mode" (without bootstrap).

Proposal: Drop modes completely and go like this:
![image](https://user-images.githubusercontent.com/46682965/64263099-67005b80-cf2f-11e9-9b37-1c6973982172.png)
No technical terms like "remote node", "bootstrap" and such needed!

...with some small changes we'd have a streamlined setup with intuitive `<Back` and `Next>` buttons:
![image](https://user-images.githubusercontent.com/46682965/65494667-8565d100-deb5-11e9-8448-10d37500f123.png)



# Discussion History
## GBKS | 2019-07-26T08:15:54+00:00
Yeah, the "Back" button labels were not implemented as [originally designed](https://www.dropbox.com/s/wec41pejuevlpqd/monero-onboarding-wallet-mode-gbks-190203.png?dl=0). Should always just  read "Back" (not use the previous screens name) and the buttons should be light grey so they are less prominent visually compared to the "Next" button. There was some confusion around this I saw in users during this recent [user testing session](https://paper.dropbox.com/doc/Monero-GUI-user-testing--Ahq0IskVq_SDsjTKEwvlQqAcAg-YAWmy01OJa5vkmdQvt6wg). The list of modes should also have a "selected" state (like they do in the settings page) with a "Next" button to confirm the choice. Definitely some small interaction tweaks that would improve usability.

I don't have a super strong opinion on whether the language picker is a dropdown or an independent screen.

## ghost | 2019-07-26T08:46:15+00:00
@GBKS thank you, man! It's such a pleasure to hear that you already came up with this years ago! By the way: Your idea for the `transactions` page (option 1) looks INCREDIBLY beautiful!

> I don't have a super strong opinion on whether the language picker is a dropdown or an independent screen.

Me neither. Here are the 3 reasons why I did it as shown:
- A user who doesn't speak English had to understand the English word "language" in order to be able to change the language. Now it's enough if he understands "Next >". 
- The current orange "Language" button directly next to the "Continue" button were too close. What the user can do on every wizard page should be in the middle of the page - not hidden on the bottom in the navigation area.
- I looked at other install wizards and most of them have a dedicated welcome screen.

## selsta | 2019-11-27T18:23:30+00:00
> The mode selection window forces you to select something but you can't go back.

#2520 

# Action History
- Created by: ghost | 2019-07-26T07:14:38+00:00
