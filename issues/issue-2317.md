---
title: Drop/ move shortcuts to make the GUI intuitive
source_url: https://github.com/monero-project/monero-gui/issues/2317
author: ghost
assignees: []
labels: []
created_at: '2019-07-25T07:30:30+00:00'
updated_at: '2019-08-06T20:55:37+00:00'
type: issue
status: closed
closed_at: '2019-08-06T20:55:37+00:00'
---

# Original Description
Currently:
![image](https://user-images.githubusercontent.com/46682965/62207847-74a54d00-b395-11e9-8d11-efc150b93b55.png)
The marked shortcuts are unnecessary (see 11 reasons below). Contrary to that, the "close wallet" shortcut in the balance card is not unnecessary. But it is in the wrong place, because it doesn't do something with just the balance or the account - instead, it closes the whole wallet. Therefore, it should be in the title bar.

Proposal:
![image](https://user-images.githubusercontent.com/46682965/62208342-d6b28200-b396-11e9-91b3-b876cf2c9925.png)
(Design also shows #2293, #2298, #2304, #2325):


**Reasons:**

- General:
  - Only frequently used features should be in prominent places.
  - It causes **anxiety** for new users when they have to find out what something does by clicking on it. Because they have the fear that something may happen they don't want or don't understand and don't know how to revert it. We all know how this sucks!

- Language shortcut:
  - Who needs to **quickly** change the language?
  - During first startup we have a dedicated page to select the language.
  - Which other program has a shortcut to quickly change the language? Not even a browser.
  - A user who actually **wants** to change the language will not find it in the settings. Because it's not there. And the world symbol in the title bar may not be found at all or recognized as such, and even if it is found and recognized as world symbol: In many other applications that's not a symbol for the language, it's a symbol for the internet. Correct solution: Add a language option to the settings using the following symbol:
![image](https://user-images.githubusercontent.com/46682965/62210363-437c4b00-b39c-11e9-9aa4-97a7248d7dd6.png)

- Theme shortcut:
  - People don't switch every morning to day mode and every night to night mode, as if that were to help with eye vision or something. (Even if 1 of 1000 did this, it wouldn't make much sense, because the GUI is no full screen application.)
  - The symbol is not self explaining since it may not be recognized as a light bulb. Even if it is recognized as a light bulb, in many other programs the light bulb is a symbol for extra hints that will "enlighten" you.

- "Hide/show menu" shortcut:
  - Nobody needs it.
  - No other program has it.
  - **If** somebody should actually need it, he's not gonna find it. Instead, he's gonna try to do what's intuitive: Hover the mouse over the line between the menu and the main window and hope for the arrows to come up. (They won't.)
 


# Discussion History
## selsta | 2019-07-25T07:41:47+00:00
I think tool tips would help with explaining buttons.

> Even if 1 of 1000 did this, it wouldn't make much sense because the GUI is no full screen application.

GUI can be used full screen on macOS.

## ghost | 2019-07-25T07:50:02+00:00
> I think tool tips would help with explaining buttons.

Definitely!!

> GUI can be used full screen on macOS.

Nobody does that because you don't gain anything because the GUI isn't made for it. See:
![image](https://user-images.githubusercontent.com/46682965/61855947-5df88500-aec1-11e9-88a4-2b30d7fc6a04.png)



## ghost | 2019-08-06T20:55:37+00:00
Closed because dropping the icons is not gonna happen I guess. So I will try to go for smaller changes: #2339

# Action History
- Created by: ghost | 2019-07-25T07:30:30+00:00
- Closed at: 2019-08-06T20:55:37+00:00
