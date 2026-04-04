---
title: Problem with wallet location inside synced Nextcloud folder on Linux
source_url: https://github.com/monero-project/monero-gui/issues/4397
author: heronimoo
assignees: []
labels: []
created_at: '2025-01-09T12:41:18+00:00'
updated_at: '2025-01-22T09:27:05+00:00'
type: issue
status: closed
closed_at: '2025-01-22T09:27:05+00:00'
---

# Original Description
I'm trying to move my Monero GUI Wallet from a Windows 11 machine to a Linux machine - and I need to keep all labels and descriptions. My understanding is that I should be able to simply copy over the two files inside the wallet directory (one .keys and one without a filetype). On Windows, these files are stored inside a synced Monero Nextcloud folder. The idea is to have automatic backups of these files. (I would have thought I could even use that location from both clients (not concurrently), but I don't really need that.)

On Linux now, the files can be used correctly if I store them inside a subfolder of the default folder, i.e. `/home/user/Monero/wallets/Wallet-from-Win`. But if I store them inside the synced Nextcloud folder, i.e. `/home/user/Nextcloud/Wallet-from-Win`, I run into problems:
1. I need to resync the blockchain, even though I already have another wallet on the Linux machine that is full synced. When I copy the files to the default Monero folder, no resyncing is required.
2. Labels and descriptions do not show up.

I noticed that when I go into `Settings > Info > Wallet path:`, it shows a weird location (`/run/user/1000/doc/<random>/Wallet-from-Win.keys`) instead of the actual location (`/home/user/Nextcloud/Wallet-from-Win/Wallet-from-Win.keys`).

Am I doing something wrong or is it impossible to store these files inside a synced Nextcloud folder

# Discussion History
## heronimoo | 2025-01-09T15:52:46+00:00
Oooooh! Are you a phisherbot?

## heronimoo | 2025-01-09T19:57:42+00:00
Alright, I solved it. The issue was that I was using the flatpak version, but had not given it access to that specific Nextcloud folder. The flatpak version only has access to the folder it creates itself in '/home/user/Monero`.

Using Flatseal, I gave it access to the synced Nextcloud (sub-)folder, and now things work perfectly.

# Action History
- Created by: heronimoo | 2025-01-09T12:41:18+00:00
- Closed at: 2025-01-22T09:27:05+00:00
