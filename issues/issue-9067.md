---
title: Troubleshooting monerod, pauses at 2688969 finds no new blocks
source_url: https://github.com/monero-project/monero/issues/9067
author: dgiff802
assignees: []
labels: []
created_at: '2023-11-12T14:54:26+00:00'
updated_at: '2023-11-13T02:27:28+00:00'
type: issue
status: closed
closed_at: '2023-11-13T02:27:28+00:00'
---

# Original Description
Initial blockchain sync on Ubuntu 22.04.3 LTS. Using monero-gui-v0.18.3.1

monerod synced over 48 hours till hitting height 2688969 then paused for about 10 hours finding no new block candidates.
I searched monero.fail at this time and several failed nodes were also displaying top block height of 2688969. 

I am running monerod from the monero-gui file with terminal and no additional arguments. Since repeated restarts saw no change (even with adding in --db-salvage argument) I tried syncing the rest of the way with the GUI and it noticed additional block height and then continued syncing immediately upon startup. 

Are there different lists of peers to attempt sync with when running GUI or just the monerod daemon?

# Discussion History
## selsta | 2023-11-12T15:01:16+00:00
2688969 appears to be nodes that are still using v0.17. Is it possible that you were using an old monerod somehow?

> I tried syncing the rest of the way with the GUI and it noticed additional block height and then continued syncing immediately upon startup.

The GUI just starts monerod, it does not have any specific settings that would explain the behaviour you saw.

## dgiff802 | 2023-11-12T19:21:10+00:00
old monerod... it's quite possible because I am extremely weak in linux. 

I used the gui to initiate downloading a copy of the new version v0.18.3.1 and tried to extract the contents to the desktop but I could not drag and drop for security reasons the OS explained.  
I used a mv command to put the file from downloads to the Desktop.  (with sudo and several tries to get file path right)
Then I opened that new folder and opened a terminal there and run monerod. (but which version?)
It starts syncing from zero as expected.
Two days later I noticed it was stuck at 2688969.
Eventually I run the v0.18.3.1 gui and it syncs to full block height fine.  (but which monerod version?)

Must be that I am running old monerod. I will have a look at the logs later.

## dgiff802 | 2023-11-13T02:00:32+00:00
2023-11-13 01:16:26.417	I Monero 'Oxygen Orion' (v0.17.2.0-unknown)
2023-11-13 01:16:26.417	I Initializing cryptonote protocol...
2023-11-13 01:16:26.417	I Cryptonote protocol initialized OK
2023-11-13 01:16:26.417	I Initializing core...
2023-11-13 01:16:26.418	I Loading blockchain from folder /home/mclovin.bitmonero/lmdb ...
2023-11-13 01:16:26.418	E Failed to parse block from blob
2023-11-13 01:16:26.422	I Stopping cryptonote protocol...
2023-11-13 01:16:26.422	I Cryptonote protocol stopped successfully
2023-11-13 01:16:26.422	E Exception in main! Failed to parse block from blob retrieved from the db

Running monero-wallet-gui by clicking on it in the gui avoids this problem but I want to run monerod alone. Clicking on the monerod program in the folder monero-gui v0.18.3.1 also opens the v0.17 version of monerod. 

## selsta | 2023-11-13T02:01:33+00:00
Where did you download the GUI? The one from getmonero.org definitely does not come with v0.17.2.0.

## dgiff802 | 2023-11-13T02:24:16+00:00
I got it working!!  Lets assume my GUI archive download is reputable for now :)
I ended up opening a terminal in the recently downloaded and extracted directory and running which command. I got into reading about $PATH variables...

~/Desktop/monero-gui-v0.18.3.1$ which monerod
/usr/bin/monerod
~/Desktop/monero-gui-v0.18.3.1$ 

I figured this is what I needed to update. Looking at properties at the monerod executable at /usr/bin location I confirmed it was v0.17. 
I tried a mv command to force the file from my downloaded archive folder into /usr/bin

~/Desktop/monero-gui-v0.18.3.1$ sudo mv monerod /usr/bin/monerod

Now when I run monerod from a terminal open at any directory location it is running v0.18.

## selsta | 2023-11-13T02:27:28+00:00
Glad you were able to resolve the issue! :)

# Action History
- Created by: dgiff802 | 2023-11-12T14:54:26+00:00
- Closed at: 2023-11-13T02:27:28+00:00
