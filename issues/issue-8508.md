---
title: The User Experience With Hardware Wallets is Complete Shit
source_url: https://github.com/monero-project/monero/issues/8508
author: k98kurz
assignees: []
labels: []
created_at: '2022-08-15T22:45:50+00:00'
updated_at: '2022-08-26T20:24:58+00:00'
type: issue
status: closed
closed_at: '2022-08-16T00:15:37+00:00'
---

# Original Description
Every time I connect my Nano S and open a software wallet to do anything, there's another update that has to be applied because the Monero network broke backwards compatibility with a minor version upgrade. So I upgrade the software wallet. Now it says it can't talk to my Nano S because the Monero app on it is a minor version behind or ahead of current (e.g. 1.7.x instead of 1.6.x or 1.5.x instead of 1.6.x; both have occurred), so I have to update it. But I can't update it because I have to update the firmware first, which I can't do because Ledger Live has to be updated first, which it won't because it is shit software that hangs at "100%" during the update process.

So I have to fix Ledger Live to update the Nano S firmware to update the Monero app on it, then the software wallet now doesn't work because the Monero app on the Nano S is now a minor version ahead (e.g. 1.8.x instead of 1.7.x). So now I have to hope that I can update the software wallet again to become compatible with the new new version of the hardware wallet app.

This is retarded. This is a horrible, time-wasting, and frustrating experience. Monero advocates are always talking about how much easier and better the experience is compared to privately transacting in Bitcoin, but this is a far worse experience.

Does nobody understand the concept of having a stable application interface? I shouldn't have to spend hours debugging why software that previously did work now doesn't just because I haven't opened it in a week or two and one piece in a chain of software that need to be in sync was forced to update.

Does nobody understand how to do semantic versioning correctly? Minor version changes are explicitly supposed to be backwards compatible. [See the semver rules. They are very simple.](https://semver.org) Making the whole thing just stop working because of a minor version patch is nonsense.

Had to get that off my chest because it has been a constant frustration the whole time I have used this cryptocurrency. Some part of this process has to be fixed. Maybe the source of this issue lies elsewhere; if so, let me know where to direct my frustration.

# Discussion History
## selsta | 2022-08-15T23:05:59+00:00
> because the Monero network broke backwards compatibility with a minor version upgrade

Monero had a major network upgrade, so calling this a minor upgrade is incorrect. Monero versions work like this: `0.Major.Minor.Patch` with the first zero indicating that the program is still in beta.

See here the release notes calling it a major release: https://www.getmonero.org/2022/07/19/monero-0.18.0.0-released.html

> Every time I connect my Nano S and open a software wallet to do anything, there's another update that has to be applied

This is because Ledger decided to version lock the app so that every time we put out a minor release they had to release a new compatible version. Ledger has removed this now and only version lock to major releases. You won't have to update the  app until we release v0.19.0.0. This means no update for a year or longer.

> But I can't update it because I have to update the firmware first, which I can't do because Ledger Live has to be updated first, which it won't because it is shit software that hangs at "100%" during the update process.

This should be reported to Ledger.

> Maybe the source of this issue lies elsewhere; if so, let me know where to direct my frustration.

The Ledger integration is developed by Ledger.

-----

To summarize, your issue should largely be resolved since the version lock has been made less strict in v1.8.0.

## k98kurz | 2022-08-16T00:15:37+00:00
I sincerely hope this is the last time I have to go through this irritating process.

## BeholdersEye | 2022-08-26T20:24:57+00:00
Considering they delayed the auto-updater for everyone (whether or not they use a hardware wallet) to give Ledger time to get its act together but expect Linux users to just deal with a broken archive it seems to me that Monero development gives hardware wallet users the red carpet treatment.

# Action History
- Created by: k98kurz | 2022-08-15T22:45:50+00:00
- Closed at: 2022-08-16T00:15:37+00:00
