---
title: timestamp strangeness in archive on Linux auto update
source_url: https://github.com/monero-project/monero/issues/8522
author: BeholdersEye
assignees: []
labels: []
created_at: '2022-08-20T12:22:01+00:00'
updated_at: '2022-10-11T14:38:05+00:00'
type: issue
status: closed
closed_at: '2022-08-20T12:38:55+00:00'
---

# Original Description
tar xvf monero-gui-linux-x64-v0.18.1.0.tar.bz2
monero-gui-v0.18.1.0/
monero-gui-v0.18.1.0/LICENSE
tar: monero-gui-v0.18.1.0/LICENSE: implausibly old time stamp -9223372036854775808
monero-gui-v0.18.1.0/extras/
monero-gui-v0.18.1.0/extras/monero-blockchain-ancestry
tar: monero-gui-v0.18.1.0/extras/monero-blockchain-ancestry: implausibly old time stamp -9223372036854775808
monero-gui-v0.18.1.0/extras/monero-blockchain-depth
tar: monero-gui-v0.18.1.0/extras/monero-blockchain-depth: implausibly old time stamp -9223372036854775808



Crashes the archive manager under Ubuntu.

# Discussion History
## selsta | 2022-08-20T12:23:22+00:00
Try to use `tar --warning=no-timestamp`

## BeholdersEye | 2022-08-20T12:29:59+00:00
Overriding the warning is addressing the symptom and not the cause.

I will wait until an archive with no screwy timestamps is released, I think. Hopefully this is not the standard for Monero going forward.



## selsta | 2022-08-20T12:38:55+00:00
All the binaries are reproducible. You can build your own GUI binaries with docker or wait for the next release where this issue is resolved. Or you can manually fix the timestamp.

We are not going to fix this for the existing release as this would mean the archive gets a new hash which might confuse people.

Closing this as the timestamp issue is fixed internally in the packaging script and this is the wrong repo.

## BeholdersEye | 2022-08-20T12:43:04+00:00
 This was just to notify you of the problem. Take as much time to address it as you need.

"Just build it yourself" seems like a less than ideal response to a problem with the auto updater, and the same goes for "just do a manual install". I already intended on waiting for the next version. I expect many Monero users are not going to be comfortable suppressing error messages no matter how benign.

## selsta | 2022-08-20T12:49:36+00:00
Which auto updater are you talking about? The one inside the GUI doesn't extract any files and I have not seen any warnings with Ubuntu when extracting this archive, otherwise this would obviously have been fixed before release.

Are you extracting the file from the command line or from your desktop environment? What is your exact Ubuntu version?

## BeholdersEye | 2022-08-20T13:20:04+00:00
The problem is not with the auto-updater itself, the problem is that the archive:

"monero-gui-linux-x64-v0.18.1.0.tar.bz2"

Causes Ubuntu's Archive Manager to crash when attempting to open the file. The tar command was just to show the problem.

I expect most auto-update users will attempt to open the archive with the GUI manager, fail, and get no further than that.

I am using version 3.28.0, Archive Manager, the default archive manager for Gnome. It has no difficulty opening the tar.bz2 files associated with previous Monero releases, so I believe the fault to lie in the timestamps. However, If you believe the problem is with Archive Manager and not the archive's formatting, you might report the error here:

https://gitlab.gnome.org/GNOME/file-roller/-/issues

I don't consider further details of my operating environment to be relevant, since other users, who are using a different version of Ubuntu, also experience the problem:

https://old.reddit.com/r/Monero/comments/wmtrs8/cli_gui_v01810_fluorine_fermi_ledger_monero_app/ik6y1kv/

## selsta | 2022-08-20T14:47:27+00:00
I see the issue now. Right click -> `Extract here` works without issues. That's what I do usually and also have done while testing this release. Only double clicking causes the crash in Archive Manager.

## BeholdersEye | 2022-08-20T17:11:01+00:00
It is a bad look to delay the auto-updater while Trezor gets its act together but tell Linux users they have to wait until next release if they want the auto-updater to deliver an archive they can double-click. I will wait, don't get me wrong- but it's a bad look.

## stefan-reich | 2022-08-23T16:58:24+00:00
I am using tar xvfj and also got the timestamp warning. Extracted fine anyway though.

## BeholdersEye | 2022-08-26T19:57:51+00:00
> We are not going to fix this for the existing release as this would mean the archive gets a new hash which might confuse people.

In my opinion fixing the archive is less confusing than expecting Ubuntu users to know not to double click it.

I hope everyone reading this appreciates how the tone changed from "What's your Ubuntu version?" (implying I'm not able to discern whether my config is at fault) to "fixing this might confuse people" (acknowledging the faulty archive is the problem) once I provided a link with other people experiencing the same problem.

## selsta | 2022-08-26T20:21:42+00:00
As I already explained we can't fix it without putting out a new release. We never change the archive hash of an existing release.

We are already preparing v0.18.1.1 which will have correct timestamps: https://github.com/monero-project/monero/pull/8534

## BeholdersEye | 2022-08-26T20:28:24+00:00
In that case all I can say is that I am champing at the bits. :)

## selsta | 2022-09-19T22:10:21+00:00
https://www.getmonero.org/2022/09/19/monero-GUI-0.18.1.1-released.html is now released. Auto updater will be activated in 1-2 days assuming no major issues get reported.

## selsta | 2022-10-11T14:38:05+00:00
v0.18.1.2 has been released and the auto updater should work now.

# Action History
- Created by: BeholdersEye | 2022-08-20T12:22:01+00:00
- Closed at: 2022-08-20T12:38:55+00:00
