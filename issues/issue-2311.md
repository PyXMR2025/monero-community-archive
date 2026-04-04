---
title: Change wallet modes (simple, intuitive, easy to maintain)
source_url: https://github.com/monero-project/monero-gui/issues/2311
author: ghost
assignees: []
labels: []
created_at: '2019-07-23T11:23:20+00:00'
updated_at: '2019-07-25T19:28:17+00:00'
type: issue
status: closed
closed_at: '2019-07-25T19:16:32+00:00'
---

# Original Description
1. Add one checkbox:
![image](https://user-images.githubusercontent.com/46682965/61789819-efaab880-ae15-11e9-9063-8a0230bc60d8.png)

2. When connecting for the first time, ask:
![image](https://user-images.githubusercontent.com/46682965/61706796-49917c80-ad49-11e9-9216-eca48ce2cdf1.png)

3. In return, drop the 3 different wallet modes.

**Reasons:**
- Silently downloading the blockchain in the background makes people angry, but making remote node the default is bad for privacy. --> We **_must_** ask the user.
- Switching modes sucks when you have to close and reopen the wallet for it.
- The bootstrap mode, which is currently the default mode, is a mess: Too many inconsistencies (#2206 #2304).
- People don't understand the bootstrap mode, because it is not explained and it is not usual in crypto (#2208).
- The "change wallet mode" button can be easily overlooked and is not good: If you click it, you are trapped, because you can't cancel/ go back. You are forced to select a mode, and it doesn't even tell you which mode is selected currently.
- Summary: The differences between the 3 modes are just connection type and showing advanced features, but right now this is obfuscated.

# Discussion History
## ghost | 2019-07-25T19:16:26+00:00
Close because

1.  No fans
2. I didn't know/ forgot that the VERY first time you use the GUI it explicitly asks you which mode you want, as pointed out correctly by dEBRUYNE_1.

## selsta | 2019-07-25T19:24:50+00:00
> No fans

You opened a lot of issues, it will take time to go through all of them.

> You are forced to select a mode, and it doesn't even tell you which mode is selected currently.

This is something I’d like to fix.

## ghost | 2019-07-25T19:27:06+00:00
> You opened a lot of issues, it will take time to go through all of them.
yes :D :D
 
> > You are forced to select a mode, and it doesn't even tell you which mode is selected currently.

Be sure that I didn't forget this ;) It will come up in another better proposal soon. Is that acceptable for you or do you want me to reopen?



## selsta | 2019-07-25T19:28:16+00:00
>  Is that acceptable for you

Sounds good.

# Action History
- Created by: ghost | 2019-07-23T11:23:20+00:00
- Closed at: 2019-07-25T19:16:32+00:00
