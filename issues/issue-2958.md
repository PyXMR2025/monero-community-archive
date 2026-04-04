---
title: Priority settings could be normalized
source_url: https://github.com/monero-project/monero/issues/2958
author: ghost
assignees: []
labels:
- enhancement
created_at: '2017-12-18T18:20:45+00:00'
updated_at: '2018-09-04T23:32:53+00:00'
type: issue
status: closed
closed_at: '2018-09-04T23:32:53+00:00'
---

# Original Description
Typing `help transfer` gives the following paragraph: 

> Command usage: 
>   `transfer [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> <amount> [<payment_id>]`
> 
> Command description: 
>   Transfer `<amount>` to `<address>`. If the parameter `"index=<N1>[,<N2>,...]"` is specified, the wallet uses outputs received by addresses of those indices. If omitted, the wallet randomly chooses address indices to be used. In any case, it tries its best not to combine outputs across multiple addresses. `<priority>` is the priority of the transaction. The higher the priority, the higher the fee of the transaction. **Valid values in priority order (from lowest to highest) are: unimportant, normal, elevated, priority.** If omitted, the default value (see the command "set priority") is used. `<ring_size>` is the number of inputs to include for untraceability. Multiple payments can be made at once by adding `<address_2> <amount_2>` etcetera (before the payment ID, if it's included)

However, typing `help set` shows priority set a different way:

> priority [0|1|2|3|4]
>      Set the fee too default/unimportant/normal/elevated/priority.

So these are different. In `transfer` the priority setting is a word like "normal" or "priority". But in the `set` command the priority setting is a number from 1-4.

My idea:

Allow for the number 1-4 to be used in the transfer command. So a correct use would be:

`transfer 3 10 <address> <amount>` would send the transfer with a priority of 3-elevated and a ringsize of 10. The cool thing is that the minimum ringsize is 5, yet the priority setting is 1-4, so there's no crossover. In fact, we could even have it that the command `transfer 12 2 <address> <amount>` would send with a priority of 2-normal and ringsize of 12. The point is the numbers are accidentally switched in the command, but since the minimum ringsize is 5 then the CLI knows that any lone digit between 1-4 is the priority setting. The only drawback is if MRL decides to change the minimum ringsize to under 5, then this would have to be rewritten.

Anyways, the bigger issue is that we allow the priority setting in commands like `transfer` or `sweep_all` to have priority be inputted as a number (like it is in the `set` command) and not a word like "elevated" that is harder to remember/type and requires translations. 

TLDR: We should normalize the priority setting across all commands.

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:46:36+00:00
+enhancement

## moneromooo-monero | 2018-08-15T12:17:06+00:00
https://github.com/monero-project/monero/pull/4262

## moneromooo-monero | 2018-09-04T23:12:47+00:00
+resolved

# Action History
- Created by: ghost | 2017-12-18T18:20:45+00:00
- Closed at: 2018-09-04T23:32:53+00:00
