---
title: monerod.exe crashing (again)
source_url: https://github.com/monero-project/monero-gui/issues/1773
author: SBSeed
assignees: []
labels: []
created_at: '2018-12-03T17:59:24+00:00'
updated_at: '2018-12-31T02:50:52+00:00'
type: issue
status: closed
closed_at: '2018-12-31T02:50:52+00:00'
---

# Original Description
reaches 81% @ blockchain 313939 (left to dl) and crashes, restart just crashes again...

i can download the testnet stuff just fine, but mainnet seems to have an issue here for some reason.

[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/2640624/monero-wallet-gui.log)

[bitmonero.log](https://github.com/monero-project/monero-gui/files/2640623/bitmonero.log)

added exception for a blocked IP, same result.... not sure what is causing this, will continue to try some different stuff, in the meantime have a look at the logs see if the information points to anything i am not seeing.

edit:
this only seems to be happening with Mainnet connection/wallet so far... its starting to get a little frustrating.
(will update as i try to find out what is going on)

# Discussion History
## dEBRUYNE-1 | 2018-12-04T14:32:38+00:00
Did one of the following occur?

- A power shut down
- A system crash
- `monerod.exe` was not shut down gracefully (monerod is shut down gracefully by typing `exit`)
- Internet temporarily disconnected 

## SBSeed | 2018-12-04T14:51:44+00:00
i usually use the wallet-GUI stop local node, which shuts down monerod.exe...
it is possible that there was a temporary disconnect or that the VPN caused an interrupt when it reconnected.
no OS/Computer crash
no Power outage or shutdown on system.

i have looked at port/firewall everything is fine, nothing is blocked from being used...
the only warnings i see from deamon (cmd window) are for opening port 18080, or before (last time this happened) it was 18081, but it continues past this to sync....

something else i noticed was that it would show in the monero wallet-GUI that blockchain data was being downloaded but then on restarted the monerod.exe (via the wallet) would start at the same place (with whatever new blockchain data detected) try to sync twice last about 5-10 seconds then the deamon monerod.exe would crash while monero wallet-GUI still runs just disconnected.

again so far this is happening ONLY with the mainnet connection/wallet, i am wondering if some kind of clonflict in how the monero wallet-GUI handles custom blockchain data is saved (altho i would expect this to have no effect on the downloading of blockchain data or saving it in any dir) i only state this since of the three connection net types mainnet does not create a mainnet folder in the custom dir.

it is odd that this is not also happening with testnet and/or stagenet as well...
i was wondering if there was a way to contain/merge all the net blockchain data into a single blockchain data file? or is that not possible?

## dEBRUYNE-1 | 2018-12-04T18:32:58+00:00
>something else i noticed was that it would show in the monero wallet-GUI that blockchain data was being downloaded but then on restarted the monerod.exe (via the wallet) would start at the same place (with whatever new blockchain data detected) try to sync twice last about 5-10 seconds then the deamon monerod.exe would crash while monero wallet-GUI still runs just disconnected.

This sounds kind of vague to be honest. Can you be more detailed or post a screenshot for illustration purposes?

>again so far this is happening ONLY with the mainnet connection/wallet, i am wondering if some kind of clonflict in how the monero wallet-GUI handles custom blockchain data is saved (altho i would expect this to have no effect on the downloading of blockchain data or saving it in any dir) i only state this since of the three connection net types mainnet does not create a mainnet folder in the custom dir.

`bitmonero/lmdb` is the folder for mainnet. For testnet and stagenet separates directories / folders are indeed created. 

>i was wondering if there was a way to contain/merge all the net blockchain data into a single blockchain data file? or is that not possible?

That is not possible currently. I also think the problem is not necessarily related to mainnet itself, but rather to mainnet having significantly more transactions (and thus a significantly bigger size). 

-------------------

Can you perhaps try these steps in order to properly sync the blockchain.

1. Delete `data.mdb` again because it is, most likely, corrupted.

2. Add the following two flags to your `monerod.exe` shortcut -> `--max-concurrency 2 --db-sync-mode=safe` 

3. The first flag will ensure that `monerod.exe` does not take all CPU resources. This thus allows one to use the system whilst monerod.exe is syncing. The second flag ensures the daemon guards against corruption in case of an unexpected shutdown.

4. Open `monerod.exe` (do not open the GUI) and let it start the sync.

5. If you have to shutdown your system, type `exit` in the `monerod.exe` window. 

6. Once it is fully synced, you can open the GUI (which will automatically connect to the daemon (monerod.exe) that is already running). 

Hopefully these steps ensure that you will finally be able to properly perform the initial blockchain sync. 

## SBSeed | 2018-12-04T19:05:08+00:00
![monero_wallet-gui](https://user-images.githubusercontent.com/11578159/49465760-295d7f00-f7b3-11e8-9605-700b091fb72b.jpg)

this shows that there is a small bit of syncing left, however if i restart my computer and open monero again it shows the same starting point for blockchain data and how much is left... it is different shown there first of all, second the first time open monero (after booting up my PC again) it goes back to 600k-800k blockchain data download.

also, i am wondering if this is related to the NTFS issue that was happening for monero v0.11.0.1 (or there abouts) with the data file stopping because of an issue with the file reaching a certain size within the windows 7 OS...

anyways, ill try deleting the file and using the flags...

## SBSeed | 2018-12-11T08:16:43+00:00
first crash
![monerod](https://user-images.githubusercontent.com/11578159/49786833-e2ebb100-fcd9-11e8-81df-cbda9aeb66b1.png)
#255103

second/third crash
![monerod2](https://user-images.githubusercontent.com/11578159/49786858-f8f97180-fcd9-11e8-9b0f-54080413056d.png)
#255109

4th crash
![monerod3](https://user-images.githubusercontent.com/11578159/49787053-79b86d80-fcda-11e8-979c-71554544c903.png)
#255111

something wrong with some of these blockchains?

## dEBRUYNE-1 | 2018-12-11T12:24:06+00:00
@SBSeed - How is your external drive formatted? Does it allow file sizes above a certain size? Also, the fact that it seems to crash at approximately the same block kind of indicates that you have hardware issues. 

## SBSeed | 2018-12-11T22:51:16+00:00
drive is NTFS format...
it can accept huge file sizes, since i downloaded the full (after the deamon started crashing again) blockchain.raw file in about 4 hours or so.

i can and have been downloading all kinds of software/files/games etc. onto this harddrive without any issues before, the only time i have had any issues is with downloading the blockchain data using deamon (monerod.exe, etc.)...

i did ask about the issues with the NTFS format and an old bug/issue that did not seem to have been solved.

is there a way to get the GUI to use the blockchain.raw without having to sync using the CMD (dosbox) commands?

## SBSeed | 2018-12-14T02:18:50+00:00
well i guess im SoL then...

## selsta | 2018-12-14T16:00:46+00:00
It’s rather hard to find out remotely why your daemon is crashing. A bug like this is not known to me in v0.13.0.4.

Can you use a remote node alternatively?

## dEBRUYNE-1 | 2018-12-14T19:06:40+00:00
@SBSeed - You can try to import the blockchain raw file with the `monero-blockchain-import` tool. Instructions can be found here:

https://monero.stackexchange.com/questions/7788/which-directory-does-monero-blockchain-import-by-default-use-to-store-the-impo/

## SBSeed | 2018-12-15T05:22:18+00:00
@selsta:
i am not sure, i am trying a few different things... i have not tried this just yet, it is on the docket to try this.

@dEBRUYNE-1:
yea i am trying this as well...

working on:
- default folder name on the 3rd harddrive
- try downloading 'importing' to a different harddrive
- possibly USB drive later on
- bootstrap/remote node later on

sometimes there is a conflict caused by naming conventions within the software either trying to force copy (on a single line of code) to default drive instead of using the alternative or custom drive/folder...
sometimes it is also the name of the folder, this should not matter but it only takes 1 reference/1 line of code/1 callback to create a conflict...

in this case it could be a conflict within the blockchain hashes/data being downloaded, so i am trying to figure out alternatives to try to bypass potential glitches within the program's...
this is going to be a lengthy process.

## SBSeed | 2018-12-19T09:47:07+00:00
FYI
computer setup:
OS: Windows 7 pro
Disk Formatting: NTFS (as far as i know, altho in the device menu's it shows as GPT or something)
Internal Disks:
- C:\ (150 GB total space, 36.8 GB free space)
- D:\ (2 TB total space, 303 GB free space)
- F:\ (3 TB total space, 1.48 TB free space)

Background programs, programs in systray:
- Private Internet Access (VPN)
- Malwarebytes (obvious)
- Security Essentials (anti-virus plus)
- Steam (valve game platform)
- CPU monitoring programs (process explorer, task killer)
- GWX control panel (prevent automatic Win10 upgrade)
- Magic Disk/ISO (virtual disk manager, etc.)
- Nvidia Experience (VGA Hardware Monitor and software upgrades)
- NLXT Kraken Control (liquid cooling and fan monitoring software)
- QBittorrent (sometimes)

currently have monero on F:\
running into issues with deamon crashing at high file size or after long periods of being open.
same for other forms of copy/paste/input-output of data.

effecting other programs systems, including Physical Memory usage skyrocketing during these times of trying to use verious monero sync/update/etc. programs... still unsure if crashing is caused because of idleing and freezing of opperations being preformed by deamon and other applications with monero.

some issues with harddrive idling and sleeping and becoming inaccessible...
still working on potential work arounds, input blockchain.raw issues accross 2 drives, check data download via deamon across 2 harddrives (expecting crashing/freezing again)...
will try to move to D:\ and do stuff from there.

btw, i have all sleep options turned off on my PC.

## SBSeed | 2018-12-25T18:14:31+00:00
i have been able to find out what part of the problem is....
https://github.com/monero-project/monero-gui/issues/1862

this gives as in-depth of a rundown of part of the problem i personally have been facing but i think there is more that might be going on with my personal computer.
i am still looking into as much information as possible and still working on trying to get the blockchain working on my computer.

## SBSeed | 2018-12-28T23:03:53+00:00
i might have figured out another part of the issues i am having... connection issues with a specific IP address/machine.

![monerod1](https://user-images.githubusercontent.com/11578159/50531072-a8478e00-0ab9-11e9-9d8a-7e3d06b9a35e.png)

is there anyway to force remote machine connections?
is it possible that remote machines could have rejected connections for lack of password/etc. on trying to connect?
anyway to bypass and set connection to different machine to download this section of the blockchain?
is it possible to use blockchain.raw to add this part of the blockchain?

## selsta | 2018-12-30T19:46:22+00:00
@SBSeed It’s getting difficult to follow your issues. Could you close your current issues and open a new one where you try to accurately describe the problem?

## SBSeed | 2018-12-31T02:50:52+00:00
i have been trying to show what the issue's are...
i have been trying to run down every lead i can get as to why my computer does not like to download the blockchain past the specific spot within the blockchain...

the last pic is (i think) the crux of the problems, i have been learning everything i can about monero in general (all the applications involved) and the monero-GUI-wallet specifically...
problems as shown in this thread:
- not knowing commands
- my own lack of knowledge with monero itself (to begin with)
- other programs, the OS that might be effecting the GUI
- hardware issues, HDD etc.
- rejected (in this last image) connection from the node/machine when it gets to roughly 80% or so

i have been able to rule out hardware issues completely, since the same thing happens no matter which drive i use.
i have been learning as much as i can to lessen user error issues, lack of knowledge, not knowing the commands etc.

i have been trying to narrow things down as much as i, myself possibly can.
i have found that most of the things i tried, as suggest by contributors or suggested in information found on the main monero gui site, all helped or made things easier but did not fix the problem...

i have redownloaded the blockchain up to 80% area about 5 times now, i am now trying to figure out if the issues are from malwarebytes and/or PIA (the VPN), OR if it the issues is being caused SOLELY by the node/machine that monerod is trying to download that particular hash/data set from....

it has been really difficult since it appears that most of the people here who help out or potentially work on the GUI do not seem to read english very good... also, that people who should understand how programs can inter-effect each other and the hardware, do not seem to know what i am talking about most of the time (altho this could be in part to me having aspergers somewhat, but not as much as there has been).

what is really annoying is the lack of in-depth/in-detail information there is about ALL of the monero programs that are only accessed or used by the GUI second hand such as monerod (altho this one is better documented than any of the others).

the learning curve (currently) for monero is so steep that i am surprised at how many people are still using it or trying to use it... it also seems that there is not a regular/dedicated team to work on the programs and consolidate them all properly into the GUI.

also, someone needs to document all the files/programs that come with the GUI download in a text document so that people can easily track down files that get quarantined without the users knowledge from protection programs.... it would make things a lot easier to create immunization for those files so they are no longer quarantined/deleted from the computer.

the site getmonero.org needs a massive update and better organization of the site, a lot of which is consolidation of information into proper categories, not to mention tutorial updates for the latest GUI versions and the QT stuff... at this point i feel that if banged my head against a hard wall long enough it would be much more productive.

anyways, i have been trying to give as much information about specific things as i possibly can looking at the logs myself trying to troubleshoot everything from what i already know about programming etc., i would hoping this would be of use in helping others to find out what I CAN do to bypass or fix issues soonest and maybe anyone who has been working on the monero project can use the information to make the GUI (and the rest of the programs) more stable and easier to use and understand intuitively in the future.

to that end have i asked the latest question's (i have given up on the earlier questions/answers) so that i can find out if there are alternative ways to make a connection with a node/machine that holds part of the blockchain... if there is anyway to force or bypass connections?, has anyone even thought of this or thought of adding it to any of the programs or the GUI?, is it possible to use the blockchain.raw to update an already in-progress download of the imdb files?...

i thought these questions where pretty self-explanatory and clear in regards to the information i am trying to get, maybe i am being too specific/detailed in my questions?!... how is that no one seems to have run into these particular issues in the years that monero (just the GUI even) has been around?

i have already pointed out flaws within the monero suite of programs, not sure if it will make any difference at this point, i am beginning to think that i should just give up on this completely.

i will THINK about starting a new issue thread...

# Action History
- Created by: SBSeed | 2018-12-03T17:59:24+00:00
- Closed at: 2018-12-31T02:50:52+00:00
