---
title: CLI Wallet v0.16.0.0- All 'set' Commands Throw Error Exposing Password
source_url: https://github.com/monero-project/monero/issues/6653
author: downystreet
assignees: []
labels: []
created_at: '2020-06-14T01:33:05+00:00'
updated_at: '2022-02-19T04:31:23+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:31:22+00:00'
---

# Original Description
Using CentOS 8, when setting the inactivity-lock-timeout using the command set inactivity-lock-timeout 500 or another number fails to set the inactivity lock time and throws an error exposing password. After the command is typed in, it then asks for your password. After typing in your password and pressing enter one time it does nothing. Pressing enter a second time makes it throw an error exposing your full or partial password even though the password given is the correct one. This is the error given after pressing enter the second time:
Error: invalid password
[wallet 47wNd7]: Error: Unknown command 'My_Password', try 'help

I am also still having the issue when I come out of the lock screen there are usually two command prompts stacked beside one another that I submitted earlier in issue #6608. This wallet has some bugs in it for sure at least in CentOS 8. I had no problems with the previous version of the CLI wallet.

Update: I've tried using the other set commands and they all have the same error where I enter my password and have to hit enter twice and then it gives the error exposing my password that I typed in. Just typing 'set' gives the list of the commands. I am using the wallet through ssh. Wallet commands that don't require a password seem to be working fine like 'status' and 'wallet_info' for example. I haven't tried sending any transaction from a CLI wallet since the update to v0.16.0.0 so I'm not sure if sending is affected by this bug. I'm going to try and get all of the dependancies installed and try it out that way.

Update 2: Instead of using ssh to access the wallet on my server I downloaded a CLI wallet from getmonero.org and tested it out on CentOS 8 on my main computer. It had no problems and no errors when using the set command. The wallet on my server was compiled from this site.

Update 3: I downloaded the CLI wallet from getmonero.org to my server using ssh and installed. It cannot even get past generating the wallet keys. After entering the language choice it exits with error: Error: failed to generate new wallet: failed to save file "test.keys".

Update 4: On the compiled wallet from this site when not using ssh and using a computer screen the errors are no longer there. I repeat the errors for the wallet compiled from this site are being caused by the use of ssh. Not using ssh also solves issue #6608. However with that being said, after downloading the latest CLI wallet from getmonero.org and testing it on my server through the computer screen is failing with error see here #6654.

Update 5: There error is still there it is occurring after coming out of lock screen. I repeat the error is only occurring after coming out of the lock screen. I REPEAT THE ERROR IS STILL THERE WITH OR WITHOUT SSH, ALL SET COMMANDS THROW ERROR AFTER UNLOCKING THE LOCK SCREEN. THERE IS NO ERROR THROWN ON INITIAL START BUT ONLY AFTER COMING OUT OF THE LOCK SCREEN.

# Discussion History
## moneromooo-monero | 2020-06-14T11:25:27+00:00
Probably readline again. Did you build with readline ? Can you try again with an older version which you say had no problems (to see if it's a system update).
I think you're typing your password as a command due to readline not reacting to the first password.


## downystreet | 2020-06-14T15:31:34+00:00
I didn't have readline-devel installed so no it was not built with readline, but it says optional in the dependencies section. If readline was required though, why would the normal download from getmonero.org not be having any problems?

Update: I've recompiled v0.16.0.0 with readline and it seems to be working fine now. I'm not getting any errors and it's not stacking command prompts when coming out of lock.

## selsta | 2021-04-16T08:38:44+00:00
from IRC @NReilingH

08:37 <NickReilingh[m]> Would anyone care to add a comment to this issue: https://github.com/monero-project/monero/issues/6653 -- saying it is repro'd exactly as described on 0.17.2.0-release for ARM/macOS Big Sur?

## selsta | 2022-02-19T04:31:22+00:00
fixed readline on macOS ARM

# Action History
- Created by: downystreet | 2020-06-14T01:33:05+00:00
- Closed at: 2022-02-19T04:31:22+00:00
