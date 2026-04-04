---
title: Clear clipboard on "Show seed & keys" page to clear sensitive info from clipboard
source_url: https://github.com/monero-project/monero-gui/issues/3072
author: garlicgambit
assignees: []
labels: []
created_at: '2020-09-07T18:26:30+00:00'
updated_at: '2020-09-07T20:54:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Have a simple way to clear the clipboard when the user has copied sensitive information like the mnemonic seed. After pasting the information you want to clear it asap from the clipboard. This can prevent things like accidental pasting in a search engine or online word processor.   
  
Ideas:  
  
- Add a note that informs the user to clear the clipboard after use.  
- Add one or more 'clear clipboard' buttons on the page. This could be at the top and/or bottom of the page or next to the copy buttons.  
- Clear the clipboard when the user leaves the "Show seed & keys" page. Could make this explicit when you leave the page. Example: "Leave page and clear clipboard"  
- Add keyboard shortcut to clear the clipboard. Example: control+x  
- Automatically clear the clipboard after X number of seconds.  
  
This could also be added to the "Send" and "Receive" pages. As addresses should be regarded as sensitive information as well.

# Discussion History
## sanderfoobar | 2020-09-07T20:54:02+00:00
cross-platform clipboard manager is a lot of work, in addition I'm not sure to what extend it is the job of the GUI to babysit the user.

# Action History
- Created by: garlicgambit | 2020-09-07T18:26:30+00:00
