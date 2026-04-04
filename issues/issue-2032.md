---
title: GUI crashes moving from [Create a New Wallet] to [Open a Wallet from File]
  +label:bug
source_url: https://github.com/monero-project/monero-gui/issues/2032
author: MoneroChan
assignees: []
labels: []
created_at: '2019-03-25T13:04:51+00:00'
updated_at: '2019-04-29T03:02:59+00:00'
type: issue
status: closed
closed_at: '2019-04-29T03:02:59+00:00'
---

# Original Description
Hi, it seems some data lingers around after using the [back to menu] button, 
on the [create a new wallet] screen, causing GUI to crash.
(Not sure if this will corrupt anything?)

Procedure to Replicate Crash on GUI V0.14.0.0: 

1. Start GUI 
2. Click 'Create New Wallet' 
3. Click 'BACK to Menu' button (before finishing the wallet creation)
4. Select 'Open wallet from file'  
5. Browse file system and open wallet
6. Enter password
7. GUI Crashes with " Error: Couldn't open wallet: Please Restart GUI "

Problem only occurs once you've "created a wallet" , and then click the back to menu button 
(e.g if you accidentally click create new wallet, but don't complete the wallet creation process) . Then when you try to load a wallet after it crashes.

Looks like the 'back to menu' button doesn't seem to reset the GUI state to accept a new wallet, something stored in cache/memory wasn't cleared perhaps? I'm not sure.

Hope this helps.


# Discussion History
## dEBRUYNE-1 | 2019-03-26T16:31:29+00:00
Are you using the release binary or a self-compiled one? 

## sanderfoobar | 2019-03-27T17:37:50+00:00
I followed your steps, and could not reproduce. However, `Error: Couldn't open wallet: Please Restart GUI` is a bug we've had for a while that occurs after closing and opening multiple wallets in a row. The pragmatic solution for now is to... restart the GUI.

Could you verify you are experiencing this problem after following your own steps, right after starting the GUI? 



## sanderfoobar | 2019-03-29T16:15:43+00:00
Possible related issue: #1194

## MoneroChan | 2019-03-30T09:14:08+00:00
Hi,  I'm using the release version. 

The following may also be necessary to replicate bug:
- Custom wallet directory (not the default directory) 
- Custom blockchain directory, (not default directory)
- Advanced mode 

To replicate make sure you click the 'BACK to Menu [<] ' button before you complete the wallet creation, and also use a custom wallet/blockchain save directory)

I replicated this error every time successfully. Happens every time without fail.

i'm just worried it might be a security issue since something is "lingering" when it shouldn't be under some circumstances. otherwise i'm not fussed.

Possible Solution : 
- Force the "BACK to Menu" button to completely clear entire wallet / path / GUI cache in memory.

# Action History
- Created by: MoneroChan | 2019-03-25T13:04:51+00:00
- Closed at: 2019-04-29T03:02:59+00:00
