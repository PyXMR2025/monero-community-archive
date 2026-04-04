---
title: Minor issues in UI strings
source_url: https://github.com/monero-project/monero/issues/3088
author: ordtrogen
assignees: []
labels: []
created_at: '2018-01-08T21:36:04+00:00'
updated_at: '2018-02-16T13:17:56+00:00'
type: issue
status: closed
closed_at: '2018-02-16T13:17:56+00:00'
---

# Original Description
"Integrated address and long payment id can't be used at the same time"

upper case "ID" for consistency:   "... payment ID ..."

-

"Specify ip to bind rpc server"
ip -> IP address
rpc -> RPC

-

"sweep_below <amount_threshold> [mixin] address [payment_id] - Send all unlocked outputs below the threshold to an address"

I think it should be:
"... <amount_threshold> [<mixin>] <address> [<payment_id>] ..."

-

"missing amount threshold"
-->  "... threshold amount ..."

-

"Please try later"
" ... try again ..."

-

"priority must be 0, 1, 2, 3,or 4"
--> "... 3, or ..."

-

"priority must be 0, 1, 2 3,or 4"
--> "... 2, 3, or ..."

- 

"expected at least one payment_id"
--> "... payment ID ..."

-

"The higher the priority, the higher the fee of the transaction."
--> "... transaction fee ..."

-

"locked_transfer [<mixin_count>] <addr> <amount> <lockblocks>(Number of blocks to lock the transaction for, max 1000000) [<payment_id>]"
<addr> --> <address>

-

"invalid language choice passed."
--> "... entered."

-

"Generate new wallet and save it to <arg>"
<arg> --> <file>

-

"Enter new wallet password"
Does it mean "Enter password for new wallet" eller "Enter new password for wallet"

-

"Storing wallet..."
--> "Saving wallet..."

-

"Stored ok"
--> "Saved ok"

-

"Failed to store wallet:"
--> "... save ..."

-

"Use wallet <arg>"
<arg> --> <file>

-

"Failed to initialize wallet rpc server" 
--> "... RPC ..."

- 

"Starting wallet rpc server"
--> "... RPC ..."

-

"Stopped wallet rpc server"
--> "... RPC ..."

-

"Use daemon instance at host <arg> instead of localhost"
<arg> --> <host>

-

"Use daemon instance at port <arg> instead of 18081"
<arg> --> <port>



# Discussion History
# Action History
- Created by: ordtrogen | 2018-01-08T21:36:04+00:00
- Closed at: 2018-02-16T13:17:56+00:00
