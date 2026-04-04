---
title: CLI crashes if ledgerwaller runs account new
source_url: https://github.com/monero-project/monero/issues/3958
author: krtschmr
assignees: []
labels: []
created_at: '2018-06-08T06:34:40+00:00'
updated_at: '2018-07-12T23:16:57+00:00'
type: issue
status: closed
closed_at: '2018-07-12T23:16:57+00:00'
---

# Original Description
Trying to create a new account which apparently isn't supported by ledger (yet). 

Freezes the  CLI. Win10.

Maybe for 0.12.3 we can see which features are already supported and then just disable commands that ain't supported?

# Discussion History
## stoffu | 2018-06-08T07:32:45+00:00
The `account new` command works for me with OSX. I think it's supported. Can anyone else reproduce the same crash?

## moneromooo-monero | 2018-06-08T07:40:23+00:00
Send a stack trace for the crash. Not sure how for Window though.

For the freeze, an all thread stack trace from the running process.

## VanSenpai | 2018-06-08T22:31:44+00:00
account new worked on Windows 10 with v0.12.2.0-release. Took about 1 minute for CLI to return.

## tficharmers | 2018-06-19T14:52:53+00:00
I created a new account and it was successful. I then created a 2nd account and after a few minutes the CLI was unresponsive and CTRL + C wouldn't quit. I unplugged the Ledger and reinitialized it and because I hadn't saved anything, I had to setup the first account again.

## stoffu | 2018-06-20T02:58:17+00:00
@tficharmers 
That stall is caused by the default subaddress lookahead sizes being too large. I've made a patch that lowers the default when creating a wallet with Ledger (https://github.com/monero-project/monero/pull/3921/commits/758072d2c095775ab5af533007b8f766eb026c91), which is yet to be merged. In the meantime, you can add this option `--subaddress-lookahead 5:20` to the command `monero-wallet-cli --generate-from-device`.


## moneromooo-monero | 2018-07-03T14:39:56+00:00
Was there a crash then ?
The delay fix was merged. If there's no further claim of a crash, I'll close as fixed.


## tficharmers | 2018-07-03T16:17:41+00:00
@stoffu Yes I could see that being the case. I actually generated my wallet with:

`--subaddress-lookahead 5:200`

I actually just tried it again and was able to create two accounts consecutively without it dying.

## moneromooo-monero | 2018-07-12T22:15:37+00:00
+resolved

# Action History
- Created by: krtschmr | 2018-06-08T06:34:40+00:00
- Closed at: 2018-07-12T23:16:57+00:00
