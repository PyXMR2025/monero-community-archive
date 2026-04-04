---
title: monero-gui does not create wallet files
source_url: https://github.com/monero-project/monero-gui/issues/995
author: honzahosek
assignees: []
labels:
- resolved
created_at: '2017-12-07T08:11:03+00:00'
updated_at: '2019-08-25T06:02:45+00:00'
type: issue
status: closed
closed_at: '2018-11-18T14:45:32+00:00'
---

# Original Description
Hi,
I have monero-gui-win-x64-v0.11.1.0 on Windows 7. When I create new wallet or restore it from seed,  the GUI starts, but wallet file never appears in desired path. When I start the GUI again I have to repeat restoration from seed. 

When I create wallet using monero-wallet-cli, I can open it in GUI, save address book entry, restart GUI and the address book entry is there.

It seems like the GUI it self is not able to save the wallet after creation, but does not give any error message. Once the wallet file is there it seems to work correctly.

# Discussion History
## 1337tester | 2017-12-07T13:19:54+00:00
I also observed that the wallet file created/restored from GUI is stored elsewhere as the CLI one. 

If this is about the 'disappearing' of the GUI created wallet - try to search your computer for the file, I don't know where it is stored on W7, but on Linux the GUI wallet is stored in "home/Monero/Wallets"

If it is about the inconsistency of storing the wallet files between GUI and CLI, then yes, this might be improved

## honzahosek | 2017-12-07T19:30:38+00:00
Oh, I only looked to default and my dedicated directory and wallet files were not there. But now I found some in `c:\Users\<username>\AppData\Local\Temp\` .  There are files like `monero-core.mU5380` and `monero-core.mU5380.keys` and many more. It seems the wallet file remained there every-time I created one, but was not saved/moved anywhere else. 

Worth to note, that creating view only wallet from GUI works fine.

Is it necessary to use temp files in this case? Leaving wallet (possibly with week password) in temp directory may be unnecessarily risky.

## medusadigital | 2017-12-08T08:10:53+00:00
Standard Path for GUI wallets on windows is C:\users\xxx\documents\monero
please have a look there.

the temp files seem interesting, good point. i guess we need to see if those are of any danger. 

the inconsistency regarding standard wallet pat mostly comes due to the fact the monero-wallet-gui folder allready contains many files. doing it the same way as the CLI (writing 3 new wallet files to application run path) seemed noob unfriendly. so a new path was added.

thats how i remember it at least. 



## dEBRUYNE-1 | 2017-12-08T10:17:00+00:00
Do you have a non-ASCII character in your username?

## honzahosek | 2017-12-08T10:32:53+00:00
There is not even `monero` directory in my `C:\users\...\documents\`. I think I always wanted create the wallet in my custom path.

There are only ASCII characters in my username.

## filipkratochvil | 2017-12-14T21:44:47+00:00
I have a same problem. Default wallet path is `C:/Users/<username>/Document/Monero/wallets/`. As `dEBRUYNE-1` mentioned, i have a non-ASCII character in my user directory name and i think it is a problem. Messages in log file says that files can't be stored. Windows 10, Monero GUI v0.11.1.0


## filipkratochvil | 2017-12-14T21:51:24+00:00
Additional info:
Installer allows to change wallet path, but when i'll choose different one, it's still the same. It seems to by trying to use temp directory located here `C:/Users/<username>/AppData/Local/Temp/` ... and again, it's in the path with non-ASCII character.

## dEBRUYNE-1 | 2017-12-15T14:45:56+00:00
@filipkratochvil & @honzahosek: This bug has to be fixed, but please try this work around for now:

https://www.reddit.com/r/Monero/comments/7hhgjx/monero_gui_01110_helium_hydra_megathread_download/dr9ewy7/?context=3

## Dark-Energy | 2018-01-19T07:56:07+00:00
On Win7x64 monero-gui-v0.11.1.0 doesn't create wallet file in spciefied path. Also monero-wallet-cli can't find wallet, that have created in default path. When i are placing wallet file in same directory, program found it, but get error: "Key file not found. Failed to open wallet". Pretty bad.

## dEBRUYNE-1 | 2018-01-19T12:14:41+00:00
@Dark-Energy Please try this guide: https://monero.stackexchange.com/questions/6823/my-name-contains-a-special-non-ascii-character-e-g-%C3%A9-%C3%B8-%C3%A2-%C3%96-and-i-cant-c/6824#6824

## erciccione | 2018-11-18T14:15:23+00:00
Should be resolved with new versions

+resolved

## ScottGold | 2019-08-25T06:02:45+00:00
lots of bug

# Action History
- Created by: honzahosek | 2017-12-07T08:11:03+00:00
- Closed at: 2018-11-18T14:45:32+00:00
