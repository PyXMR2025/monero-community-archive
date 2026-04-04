---
title: Monero GUI cannot open on Windows 64
source_url: https://github.com/monero-project/monero-gui/issues/1742
author: geft
assignees: []
labels: []
created_at: '2018-11-18T13:37:51+00:00'
updated_at: '2018-11-19T15:47:20+00:00'
type: issue
status: closed
closed_at: '2018-11-19T15:42:50+00:00'
---

# Original Description
I'm using 0.13.0.4. Clicking on it does literally nothing. Rebooted, deleted old wallet data, etc. Nothing. Is there any log I can read?

Before this I was using pre-hardfork GUI. It worked fine.

# Discussion History
## sanderfoobar | 2018-11-18T15:00:38+00:00
Open `cmd.exe`, navigate to the folder containing `monero-wallet-gui.exe` and execute it.

There should be some output you can observe. In addition; post some OS details and videocard driver version (if any).

## dEBRUYNE-1 | 2018-11-18T15:14:07+00:00
@geft - Do you have an AV running that could have been quarantining necessary files (i.e. files required in order for the GUI to run properly)? 

## geft | 2018-11-18T20:21:19+00:00
@skftn 
Still nothing. It's like pressing enter. I'm using Windows 10 Pro 1803 build 17134.407.

@dEBRUYNE-1 
I use Avira and Malwarebytes but disabling both doesn't seem to fix the problem. There was no alert either. Just want to add that the CLI works just fine, so it'd be weird if they just choose to quarantine GUI stuff.

## sanderfoobar | 2018-11-18T20:58:53+00:00
@geft Can you confirm `monero-wallet-gui.exe` is there?

You're saying that when you try to run it from `cmd.exe`, there is no output? at all?

## geft | 2018-11-19T05:31:22+00:00
Well I use PowerShell but yeah, there's no output. `monero-wallet-gui.exe` is there. I even have the shortcut on my taskbar. Like I said, I was using the GUI just fine pre-hardfork. Even verified the zip hash to ensure it's not corrupt.

## dEBRUYNE-1 | 2018-11-19T10:18:11+00:00
@geft - The AV could have quarantined some files upon extracting the `.zip` file. 

Could you perhaps try the following steps:

1. Create a new directory / folder.

2. Add the folder to the exception list in your AV. Put differently, you have to whitelist the folder in your AV.

3. Extract the `.zip` file to aforementioned folder.

4. Double click on `monero-wallet-gui.exe` to open the GUI. 

Does it work now? 

## geft | 2018-11-19T15:42:50+00:00
Hey, it works! Not sure what's stopping it, either Avira or Malwarebytes. I checked both and nothing was quarantined. Why would the Monero GUI trigger a false positive anyway?

Regardless, thanks for the help!

EDIT: Apparently it's flagged by Malwarebytes since the daemon has a built-in miner. https://www.reddit.com/r/Monero/comments/99ofpm/malwarebytes_considers_monero_malware/

# Action History
- Created by: geft | 2018-11-18T13:37:51+00:00
- Closed at: 2018-11-19T15:42:50+00:00
