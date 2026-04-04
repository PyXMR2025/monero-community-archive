---
title: 'Wallet v0.16, multiple [wallet 49... (out of sync)]: filling the screen when
  coming out of lock'
source_url: https://github.com/monero-project/monero/issues/6608
author: downystreet
assignees: []
labels: []
created_at: '2020-05-31T12:39:31+00:00'
updated_at: '2022-05-25T10:12:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When coming out of the lock screen back to the main terminal for the wallet v0.16 there are multiple [wallet 49... (out of sync)]:, stacked together. Sometimes there are 2 or more stacked together and one time I unlocked the wallet and they took up the whole screen.
For example:
A normal terminal will look like this-
[wallet 49... (out of sync)]:

When I'm coming out of the lock screen it is looking like this
[wallet 49... (out of sync)]: [wallet 49... (out of sync)]: [wallet 49... (out of sync)]:

and sometimes it looks like this
[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:[wallet 49... (out of sync)]:

# Discussion History
## moneromooo-monero | 2020-05-31T12:47:12+00:00
Did you build it with readline ? This should be mentioned in the cmake output, or with:
grep READLINE build/Linux/crash/release/CMakeCache.txt
Adapt to whatever build tree your machine has.

## downystreet | 2020-05-31T13:06:22+00:00
it says USE_READLINE:BOOL=ON

## moneromooo-monero | 2020-05-31T13:09:32+00:00
Does it print this "forever", or only once you press enter ? If you type something else, does it show up, or not ?

## downystreet | 2020-05-31T17:58:11+00:00
Once I type in a command then it goes back to normal with one instance of it on the line.

## downystreet | 2020-06-14T05:06:05+00:00
I thought that I had figured out the problem and that it was ssh causing the errors here but it is still happening with or without ssh. There are usually 2 command prompts stacked side by side after exiting the lock screen and it is also causing this error #6653.

## trasherdk | 2020-06-14T06:25:55+00:00
I'm seeing the same thing. ssh'ing to the host, launching wallet-cli in a screen session.

The wallet was created with no password, hoping to avoid the prompt for password.
It's till asking for password. Not on launch, but any command normally requiring a password. So pressing enter, when prompted, to continue.

Setting `set ask-password 0` prompt for password. Pressing enter to continue.

Activity timeout fills the screen with `out of sync` errors. Pressing enter to continue.

Setting `set inactivity-lock-timeout 0` prompt for password. Pressing enter to continue.

Now it seems to be working, with no `out of sync` filling the screen.

Trying to `set inactivity-lock-timeout` I get:
```
[wallet 9wiAxp]: set inactivity-lock-timeout 30
Wallet password: Error: failed to read wallet password
[wallet 9wiAxp (out of sync)]:  
[wallet 9wiAxp (out of sync)]: refresh        
Starting refresh...
Refresh done, blocks received: 0                                
```

Trying to set a password:
```
[wallet 9wiAxp]: password       
Wallet password: Error: failed to read wallet password
Error: Your original password was incorrect.
```


# Action History
- Created by: downystreet | 2020-05-31T12:39:31+00:00
