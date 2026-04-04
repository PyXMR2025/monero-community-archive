---
title: Issue Getting The Daemon To Start
source_url: https://github.com/monero-project/monero-gui/issues/664
author: Jayhorns
assignees: []
labels: []
created_at: '2017-04-04T21:10:01+00:00'
updated_at: '2017-05-15T10:07:00+00:00'
type: issue
status: closed
closed_at: '2017-05-15T10:07:00+00:00'
---

# Original Description
I have been asked to post this potential issue here. I am trying to use the Windows 64bit version of the GUI. The application appears to have synchronized successfully after about 8 hours, but I cannot get the daemon to start. I receive this message: "Daemon failed to start. Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually." However, the log does not show any message or text at all. And despite the message, the network status still says Connected and monerod is running as a background process in the task manager.

The solution that seemed to work for another user did not work for me (rename the folder that contains the monero-wallet-gui Application to "MoneroGui2").

If I run the monerod application manually, eventually I get a message that says: "You are now synchronized with the network. You may now start monero-wallet-cli."

With all that said, am I synced with the network and able to send Monero to this wallet despite the error message with the daemon?

http://i.imgur.com/dPVB7l6.png

# Discussion History
## TheRealMadmortigan | 2017-04-04T22:41:05+00:00
I'm having the same issue.  The daemon does eventually start, but not until the initial connection times out.  I'm able to receive but sending has been "problematic" at best.  

## Jaqueeee | 2017-04-05T05:24:59+00:00
@Jayhorns Running the gui from C:\some folder\MoneroGui2 won't work either. So you need to ensure there are not spaces in the full path. 
Please also try this build https://build.getmonero.org/downloads/monero-core-5d45967-win64.zip
It's from https://github.com/monero-project/monero-core/pull/646

## Jayhorns | 2017-04-05T17:28:28+00:00
@Jaqueeee I actually have the extraction on my D: drive (D:\My Name\Monero\MoneroGui2). So in this instance, can I run the GUI from the D: drive by making sure there are no spaces in the full file path? Or do I need to move it to the C: drive AND make sure there are no spaces in the full file path?

## Jaqueeee | 2017-04-06T15:14:45+00:00
@Jayhorns It should work with D: drive also. As long as there are no spaces. 

## Jayhorns | 2017-04-06T23:23:42+00:00
Looks like I am synced, connected, and daemon running! Thank you.

## Jaqueeee | 2017-05-03T14:14:12+00:00
Fixed in #646 

## TheRealMadmortigan | 2017-05-03T14:22:11+00:00
Nice work, gents!

On Wed, May 3, 2017 at 10:14 AM, Jaqueeee <notifications@github.com> wrote:

> Fixed in #646 <https://github.com/monero-project/monero-core/pull/646>
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-core/issues/664#issuecomment-298923366>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AZpJlUMuiPVWbZCmW2j9HuAU_6P2MXztks5r2Iu1gaJpZM4Mzb2n>
> .
>


# Action History
- Created by: Jayhorns | 2017-04-04T21:10:01+00:00
- Closed at: 2017-05-15T10:07:00+00:00
