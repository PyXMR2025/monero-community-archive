---
title: 'General :: Special Characters'
source_url: https://github.com/monero-project/monero-gui/issues/199
author: M5M400
assignees: []
labels:
- resolved
created_at: '2016-11-24T17:53:06+00:00'
updated_at: '2018-05-10T16:45:21+00:00'
type: issue
status: closed
closed_at: '2018-05-10T16:45:21+00:00'
---

# Original Description
1) When creating a new wallet and set the wallet_path to an existing path containing special characters (in this case "c:\I Am From Österreich\Wallets\"), the path, though picked from the "open file" dialog, will be treated as non-existent and created from scratch - with encoding error:

![screenshot from 2016-11-24 18-33-19](https://cloud.githubusercontent.com/assets/22886679/20607174/72acf688-b276-11e6-8204-ba755d661315.png)

![screenshot from 2016-11-24 18-48-05](https://cloud.githubusercontent.com/assets/22886679/20607187/8f977b7e-b276-11e6-888c-25c3f8da5446.png)

The wallet is being stored in that faulty path. Everything works as expected.

2) When loading an existing wallet from a wallet_path containing special characters, the wallet cannot be opened:

![screenshot from 2016-11-24 18-39-55](https://cloud.githubusercontent.com/assets/22886679/20607220/bf6ccdcc-b276-11e6-8e36-c0dbca662c1b.png)

![screenshot from 2016-11-24 18-40-40](https://cloud.githubusercontent.com/assets/22886679/20607223/c5b841ac-b276-11e6-8bb2-d7d69ec14adc.png)

![screenshot from 2016-11-24 18-40-57](https://cloud.githubusercontent.com/assets/22886679/20607226/cbc73c2e-b276-11e6-8789-99fc16a145c1.png)

Note that the path in the registry is correct...

![screenshot from 2016-11-24 18-42-17](https://cloud.githubusercontent.com/assets/22886679/20607227/d0c34ed4-b276-11e6-9cb7-d32dac3598f5.png)

This is the unofficial win32-161123 build from jaquee, but I suspect this also applies to current master.

thanks for discovering this to /u/electricoomph on /r/monero


# Discussion History
## moneromooo-monero | 2016-11-25T16:56:20+00:00
Works fine with monero-wallet-cli, so it's a GUI only thing.

## moneromooo-monero | 2016-11-25T17:00:22+00:00
Actually, is works also with the GUI. Must be a Windows thing.

## moneromooo-monero | 2016-11-26T10:56:11+00:00
Possibly related to https://github.com/monero-project/monero/issues/938

## Jaqueeee | 2016-11-29T16:39:13+00:00
related to https://github.com/monero-project/monero/issues/1390
temporary fix in https://github.com/monero-project/monero-core/pull/226

## ghost | 2017-03-29T03:58:13+00:00
@M5M400 Can this issue be closed?

## medusadigital | 2017-04-18T08:49:28+00:00
situation right now:

- if a wallet-name or wallet-path with non ascii characters wants to be saved, the GUI will pop up an error message.

- if an existing wallet is moved to a path with non ascii characters and is opened, the GUI will say "Couldnt open Wallet: Wallet file not found"


closing seems fine to me.




## peen333 | 2017-06-29T20:50:45+00:00
I cant create a Monero wallet on Windows 10 using monero-gui-win-x64-v0.10.3.1, because my last name contains an o with two dots over it. When I installed Windows, Windows created a user folder with my name including my last nam containing an o with two dots over it. The Monero gui automatically fetches the windows user folder name as the wallet name along with the filepath. 

I can change the wallet name, but I cant change the filepath because if I do I get another error message. So whatever I do I get an error message and can't complete the wallet creation. Do I have to create a new Windows user account to be able to use Monero?

![bild](https://user-images.githubusercontent.com/29784819/27709583-f1718870-5d1c-11e7-8b06-17e5168a4952.png)


## sanderfoobar | 2018-05-10T16:40:56+00:00
Resolved in #1141

+resolved

# Action History
- Created by: M5M400 | 2016-11-24T17:53:06+00:00
- Closed at: 2018-05-10T16:45:21+00:00
