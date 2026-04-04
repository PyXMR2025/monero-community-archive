---
title: 'Wizard: Will not load wallet from file if New Account page was visited first'
source_url: https://github.com/monero-project/monero-gui/issues/223
author: mochaccinuh
assignees: []
labels: []
created_at: '2016-11-28T22:30:38+00:00'
updated_at: '2016-12-08T22:05:59+00:00'
type: issue
status: closed
closed_at: '2016-12-08T22:05:59+00:00'
---

# Original Description
Click new account, go back (don't need to finish this wizard). Click "open wallet from file". Open your wallet. It will now start loading the wallet "created" in new account page.

# Discussion History
## Jaqueeee | 2016-11-29T14:54:38+00:00
Can not reproduce this. Which platform are you on?

## mochaccinuh | 2016-11-29T16:38:43+00:00
Sure it is loading the wallet you chose in the file manager?

I'm on osx. I have found the bug btw, and have a quick fix for it. It is very strange if this is platform dependent, but you never know. Anyway I can create a pull request and you can see if you want the fix :)

## Jaqueeee | 2016-11-29T17:21:52+00:00
Yes, you're right! Sorry, didn't try hard enough. =)

# Action History
- Created by: mochaccinuh | 2016-11-28T22:30:38+00:00
- Closed at: 2016-12-08T22:05:59+00:00
