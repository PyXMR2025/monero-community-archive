---
title: 'v0.17.1.16: CTRL+H fails to unhide .bitmonero in "Please choose a folder"'
source_url: https://github.com/monero-project/monero-gui/issues/3263
author: ch9PcB
assignees: []
labels: []
created_at: '2020-12-09T23:49:32+00:00'
updated_at: '2023-01-17T17:46:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
My setup:

Debian 10.7, 64bit
Gnome desktop environment version 3.30
Nautilus, official file manager of Gnome DE

Description of the issue:

After launching Monero Wallet GUI, I carried out the following steps:

Settings --> Node --> Blockchain location (Change) --> (a window pops up)  --> Please choose a folder

No matter how many times I pressed the combination keys CTRL+H, the hidden file .bitmonero refuses to show up. My data.mdb is in the lmdb sub-folder which in turn is in .bitmonero

# Discussion History
## selsta | 2020-12-09T23:51:08+00:00
Does right click -> show hidden folders work?

#1495

## ch9PcB | 2020-12-10T01:12:44+00:00
> Does right click -> show hidden folders work?

In **Please choose a folder** there was no response when I right-clicked in the empty space. Neither was there a response when I left-clicked in it.

When I first started using Monero Wallet GUI some two years ago, I had no such problems.



## selsta | 2020-12-10T01:19:21+00:00
You can simply enter the path and press enter.

<img width="957" alt="Screenshot 2020-12-10 at 02 18 42" src="https://user-images.githubusercontent.com/7697454/101708665-0777f080-3a8e-11eb-9d6a-bf4aafecf95a.png">

Will see if we can switch to a different file picker, this one seems annoying on Linux.

## ch9PcB | 2020-12-10T07:51:06+00:00
> You can simply enter the path and press enter.

Sure, you can manually enter the path BUT the problem is that it does not appear in **Blockchain location**. It means that in the box under **Blockchain location**, there is no .bitmonero folder.

> Will see if we can switch to a different file picker, this one seems annoying on Linux.

Which one? I don't understand what you meant.

## selsta | 2020-12-13T14:33:15+00:00
I see the issue now, thanks.

## ch9PcB | 2020-12-14T21:37:27+00:00
> I see the issue now, thanks.

Same bug occurs in v0.17.1.7

selsta, if you have some time to spare, could you answer the questions in [Monero-Wallet-GUI: Why does the default folder/directory have to be hidden in Linux and why can't users customize the path to lmdb](https://www.reddit.com/r/monerosupport/comments/kd73tw/monerowalletgui_why_does_the_default/)?

Thanks.

## selsta | 2023-01-17T05:07:37+00:00
Seems this old issue was resolved according to this comment: https://github.com/monero-project/monero-gui/issues/4102#issue-1534252353

## ch9PcB | 2023-01-17T11:27:00+00:00
@selsta

> Seems this old issue was resolved according to this comment: [#4102 (comment)](https://github.com/monero-project/monero-gui/issues/4102#issue-1534252353)

No, not at all.

Would you like to know how I worked around i?

My last post was December 14, 2020.

On December 15, 2020, using Microsoft Windows, I created a drive and assigned it the letter K.

I moved all the essential files of Monero to the K: drive such as

(a) the folder `lmdb` containing `data.mdb` and `lock.mdb`
(b) the folder mo containing a sub-folder named `fantasy` (`fantasy` is the username that I created during the installation of Debian) and other files. The sub-folder `fantasy` contains `fantasy.keys`)

After moving the above files to the K: drive, I changed the blockchain location to the files on the K: drive.

Since December 2020, I realized that it was not at all critical to the functioning of Monero GUI wallet whether CTRL+H failed or did not fail to unhide .bitmonero in "Please choose a folder". I learned how to live with this bug.

P.S.: I am sorry to disappoint you but the bug still persists, even on my brand new computer with version 0.18.1.2 of Monero GUI wallet; but like I said, the bug did not prevent Monero GUI wallet from functioning.

## selsta | 2023-01-17T16:46:43+00:00
@ch9PcB I reopened it.

## plowsof | 2023-01-17T17:12:47+00:00
On ubuntu, ctrl+h works , in windows im able to see the hidden folders too in the file chooser (by default?) can't reproduce this. iirc selsta fixed/changed the file browser some time after 2020 

## ch9PcB | 2023-01-17T17:43:52+00:00
> in windows im able to see the hidden folders too in the file chooser (by default?) can't reproduce this. iirc selsta fixed/changed the file browser some time after 2020

I don't use Microsoft Windows to run Monero GUI wallet for privacy reasons.



## ch9PcB | 2023-01-17T17:46:39+00:00
> On December 15, 2020, using Microsoft Windows, I created a drive and assigned it the letter K.

I forgot to mention that my SSD has a dual-boot configuration consisting of Debian and Microsoft Windows. Both of them share common logical drives; that is why the K: drive is visible to both of them.

# Action History
- Created by: ch9PcB | 2020-12-09T23:49:32+00:00
