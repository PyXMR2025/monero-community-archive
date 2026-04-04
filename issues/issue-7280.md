---
title: stop_mining_for_rpc command not working
source_url: https://github.com/monero-project/monero/issues/7280
author: lh1008
assignees: []
labels: []
created_at: '2021-01-05T17:13:10+00:00'
updated_at: '2022-05-25T10:04:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello :hand: 

This is another issue I found in the rpc_wallet when connecting to the RPC-server. You can `start_mining_for_rpc` but it doesn't stop when prompt -> `stop_mining_for_rpc`. It first stopped but it kept mining after.

![stop_mining_for_rpc](https://user-images.githubusercontent.com/7443480/103676278-e2708380-4f4e-11eb-8bab-f8998c13c030.png)

These are the continued images from the terminal.

![stop_mining_for_rpc_1](https://user-images.githubusercontent.com/7443480/103676288-e56b7400-4f4e-11eb-9baa-15cb85b65ff2.png)

Finally `exit`

![exit](https://user-images.githubusercontent.com/7443480/103676491-26638880-4f4f-11eb-95ad-4be98535319e.png)


# Discussion History
## drlef | 2021-01-12T13:18:37+00:00
I think this is the intended behaviour, at least from looking at the code. You can stop it mining for RPC by lowering your credits target to say 1000, then when your current credits is above this it will stop. Use:
set credits-target 1000
Note, if you set it to 0, then it will use the default of 50000.

## lh1008 | 2021-01-14T13:28:30+00:00
So that means `stop_mining_for_rpc` command is actually not doing what is supposed to be doing. 

Yes, I've seen how mining stops once the credits target is reached. 

## drlef | 2021-01-14T13:42:22+00:00
I think it is doing what it's supposed to, acting as the negative of `start_mining_for_rpc`, although I agree that it stopping automining could also make sense.

In the comment on the commit this feature was added, https://github.com/monero-project/monero/commit/2899379791b7542e4eb920b5d9d58cf232806937#diff-eb68bc, it says:
"The wallet can be set to automatically mine if connected to a daemon which requires payment for RPC usage. It will try to keep a balance of 50000 credits, stopping mining when it's at this level, and starting again as credits are spent."

So `stop_mining_for_rpc` doesn't affect the status of auto-mining, only the manually triggered mining.

## moneromooo-monero | 2021-01-18T15:59:24+00:00
Yes, it's as designed. It probably stops, then restarts as it's under the target. start/stop is for manual control.

## lh1008 | 2021-01-19T15:28:06+00:00
Okay, thank you for the clarification. Should this issue be closed?

## moneromooo-monero | 2021-01-20T15:41:06+00:00
Not sure. I guess there's an argument for stopping it till next wallet restart too.

# Action History
- Created by: lh1008 | 2021-01-05T17:13:10+00:00
