---
title: 'Monero Wallet GUI Deamon crash at blockchain #313285'
source_url: https://github.com/monero-project/monero-gui/issues/1760
author: SBSeed
assignees: []
labels: []
created_at: '2018-11-29T06:55:23+00:00'
updated_at: '2018-12-01T14:57:07+00:00'
type: issue
status: closed
closed_at: '2018-12-01T05:13:29+00:00'
---

# Original Description
not sure what is going on, ill try to attach the log file.
[bitmonero.log](https://github.com/monero-project/monero-gui/files/2627922/bitmonero.log)

anyways now it will try to start sync, twice, then it crashes... do i need to set wallet height or something weird.
the annoying part is there is plenty of space on the HDD, i can manually run deamon (monerod.exe) which then tries to save the blockchain information to the default drive (which does not have enough room for that) kinda frustrated and mostly tired.

it was almost done downloading at around 80% plus...
also, this is after i changed drives from default to another one as well as copy/pasting the blockchain to the new area pointed to for storing the blockchain.
(hoping i do not have to re-download the entire blockchain again)

# Discussion History
## dEBRUYNE-1 | 2018-11-29T07:40:32+00:00
>also, this is after i changed drives from default to another one as well as copy/pasting the blockchain to the new area pointed to for storing the blockchain.

Did you make sure all Monero related software was closed whilst doing this? 

## SBSeed | 2018-11-29T09:08:33+00:00
i think so... hmmm, it is possible that i could have had the GUI open, but the deamon (monerod.exe) was shutdown, had saved the new location and copy/pasted to new dir...
double checked the dir was correct both in monero and placement of blockchain data.

the deamon did run for a couple of hours after this and then crashed.... i can run it manually, not sure how i would change the save/check dir for manually running it.

i changed because i keep my OS drive small, i like to keep it that way for a number of reasons... mostly i am doing this on my gaming PC so i can work out how everything works and try to troubleshoot any potential issues before i try to do anything with the U4 server (intel quad zenon server hardware) that a bought a while back or at least use that to mine with, i might keep the wallet on my gaming PC.

anyways i am trying to get the XMRig to work too, but i need the wallet/deamon working properly first.
casual at this point basically so nothing is critical like losing monero i do not have :P
specially any of my own stupidity in using this api.

## SBSeed | 2018-11-29T09:48:15+00:00
just noticed another log file, not sure if it will help but here it is (this one from the monero wallet-gui:
[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/2628473/monero-wallet-gui.log)

(ignore my redundancy here)

## dEBRUYNE-1 | 2018-11-29T15:57:12+00:00
@SBSeed - Could you first provide the exact path of the blockchain file (data.mdb) on the external drive? Then I can give specific instructions on how to run monerod.exe manually and properly sync to the external drive. 

## SBSeed | 2018-11-30T01:36:42+00:00
its not an external drive...
it is drive F:\Monero\bitmonero (3rd drive on/attached my PC)
i am keeping all of the monero files/api's on the same drive.
this is also where the location in the monero wallet-GUI points to as well.

## dEBRUYNE-1 | 2018-11-30T08:55:21+00:00
Can you perform the following steps?

1. Browse to the directory / folder `monerod.exe` v0.13.0.4 is located.

2. Create a new shortcut of `monerod.exe` v0.13.0.4

3. Right click on the shortcut -> `Properties`

4. Now look at the `Target` box.

5. Behind `monerod.exe` add a space and `--data-dir F:\Monero\bitmonero` 

6. It should thus read as `monerod.exe --data-dir F:\Monero\bitmonero` 

7. Click on `Apply` / `OK` to properly save the changes.

8. You can now open `monerod.exe` manually and it will sync properly to your external drive. 

## SBSeed | 2018-11-30T09:56:00+00:00
ok, ill try that thanks.
ill give an update shortly.

edit:
well that is not working....
im going to try overwritting the entire mondero directory with the api from the zip file, if that does not work i guess ill try to just delete the blockchain data etc. and start over from scratch redownloading the entire blockchain again...
must have done something that caused the data storage to become corrupted, at a guess....

## SBSeed | 2018-11-30T10:53:15+00:00
i found part of the problem, that before i uninstalled malwarebytes, it had quarentined/deleted some QT files (possibly others)*.... files missing when i tried to overwrite them with files from latest version of monero.
* this could have also happened from security essentials doing similar stuff as well.
this could account for both the monerod.exe and the blockchain data storage issues since they could potentially be blocking access to the data files themselves.


i am sure there are other issues causing this, i will continue to mess around with monero api and see what else i can come up with... will be looking at security essential closer along with malwarebytes as well as the windows security UAC bullshit.
will also need to varify if the blockchain data has been corrupted somehow or just blocked.

## dEBRUYNE-1 | 2018-11-30T11:50:36+00:00
Does it start to sync if you rename `data.mdb` in `F:\Monero\bitmonero` to `data-old.mdb`? 

With respect to the AV, see #1747. 

## SBSeed | 2018-11-30T12:34:20+00:00
i could run the deamon just fine if it was not trying to access the old data file, was stated earlier i think, so in short yes, will see how things continue tomorrow.

well i have gotten it working again, at least for now....
anyways, it was (as far as i can tell) a bunch of different issues:
- set all exceptions for the api's in any antivirus/malware/adware programs where possible before running the program
- carefully review and decide on where you want to have ALL of your stuff, if you do not want to have on default drive
- do not stop the deamon and try to move blockchain data storage, not that you have to keep the deamon running till it ends (as far as i can tell the deamon stops/starts fine with monero GUI)

targeted files (from what i can tell):
- deamond.exe (false flag, blocking, potential quarantine)
- one or several of the files in QT and QtQml folders (deletion, possible quarantine)
- potential corruption of blockchain data (moving, possible blocking of access)
- interruptions if internet loss happens, possible down of ISP and/or VPN
- corruption of blockchain data on harddrive being full causing shutdown of deamon (monerod.exe) potential interrupt of data on crash
- finally a lot of user error

not sure if trying to run XMRig GUI at the same time as the deamon is running can cause issues...

needs to be more mouseon/scrollover tip type popups, possibly a FAQ/Troubleshooting section at the top of the nav.bar on the left or some warnings about virus/malware/etc. programs before allowing anyone new to this stuff to start the blockchain data download and storage...

might be a good idea to rework the getting started stuff on the official monero GUI website (specially for beginner idiots like me)... i think i did not read enough despite reading everything i could find.
will be able to give more feedback on this in a day or two, see if i can get the blockchain to download completely.

## SBSeed | 2018-12-01T05:13:29+00:00
ok so far so good, was able to download the entire blockchain to the data storage....
i will now start working on XMRig and the monero wallet GUI mining.

have been able to confirm that security essentials was never an issues since i had an exception setup for the entire drive, will probably change that to specific files/folders later on.
so as long as the setup is done before you use the monero wallet and deamon specifically it makes things much smoother.

thanks for the help, much appriciated in finding these issues and hopefully keep others from making the same mistakes etc., so thanks again.

## dEBRUYNE-1 | 2018-12-01T14:57:07+00:00
You're welcome and thanks for your reports! 

# Action History
- Created by: SBSeed | 2018-11-29T06:55:23+00:00
- Closed at: 2018-12-01T05:13:29+00:00
