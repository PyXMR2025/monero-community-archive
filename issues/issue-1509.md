---
title: '[Proposal] Change "Default" to "Automatic" for Transaction Priority'
source_url: https://github.com/monero-project/monero-gui/issues/1509
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2018-07-16T07:26:28+00:00'
updated_at: '2018-07-19T19:16:09+00:00'
type: issue
status: closed
closed_at: '2018-07-19T19:16:08+00:00'
---

# Original Description
This change was initially proposed by smooth, in light of this discussion: 

https://www.reddit.com/r/Monero/comments/8yvts5/kudelski_security_completed_their_bulletproof/e2ex5be/

"Automatic" better conveys the expected behavior than "Default" and therefore it would be prudent to switch to this term. 

# Discussion History
## medusadigital | 2018-07-16T08:11:13+00:00
good idea

## stoffu | 2018-07-17T03:26:52+00:00
As I've already explained in the reddit thread: https://www.reddit.com/r/Monero/comments/8yvts5/kudelski_security_completed_their_bulletproof/e2fbz6m

> The `Default` in the GUI really means the same as the default priority used in the CLI; e.g., if the default priority is set to 3 in the CLI (using `set priority <N>`), this will also be used in the GUI when `Default` is selected. The automatic low priority functionality is used when this default value is set to 0 in the CLI. It is initially set to 0, so normally GUI users will be using the auto low fee with the `Default` prioroty.

In this sense, replacing the `Default` string with `Automatic` can cause inconsistency if the user does `set priority <N>` in the CLI with `N` being greater than 0, where those user-specified default priority will be used instead of automatic. That said, the GUI is primarily intended for novice users who will never touch the CLI, so I think it's fine to replace the text.


## jonathancross | 2018-07-18T15:23:13+00:00
Thanks for the clarification @stoffu 
Seems this can be closed though given "That said, the GUI is primarily intended for novice users who will never touch the CLI, so I think it's fine to replace the text." -- correct?

## dEBRUYNE-1 | 2018-07-19T19:16:08+00:00
Resolved with #1510. 

# Action History
- Created by: dEBRUYNE-1 | 2018-07-16T07:26:28+00:00
- Closed at: 2018-07-19T19:16:08+00:00
