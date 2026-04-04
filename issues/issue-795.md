---
title: Standard wallet location (Linux)
source_url: https://github.com/monero-project/monero-gui/issues/795
author: SleepingShell
assignees: []
labels:
- enhancement
- resolved
created_at: '2017-07-14T02:22:42+00:00'
updated_at: '2018-12-16T08:09:24+00:00'
type: issue
status: closed
closed_at: '2018-12-16T08:09:24+00:00'
---

# Original Description
Currently, the CLI and GUI create wallets in a different manor.

Program | Location
------------|------------
CLI | Same folder as binary
GUI | ~/Monero

I believe there should be a standard between the two implementations. After I created my wallet in the GUI and tried to use the wallet-cli tool, I had to specify the full path. This is not much of a problem, but there should either be a standard to create wallets in the same folder, or have the GUI and CLI check for wallets in the default location for the other program.

Perhaps a wallet subdirectory in the same dir as the binaries would make sense, since these binaries are in the same directory when doing a default install. Additionally, there are already different folders such as plugins, qml, etc.

The .bitmonero folder would also be a good contender, as that would not depend upon the location of the binaries. Additionally, this would follow the standard most other blockchains use such as Bitcoin and Ethereum with keeping the wallet file in the same directory structure as the blockchain itself.

# Discussion History
## Jaqueeee | 2017-08-07T21:18:44+00:00
Storing in same folder as binaries is tricky because it's easy to delete them by accident when upgrading. Also, on Mac it wouldn't make sense because the binaries are embedded in a DMG-file that average users never opens. 

.bitmonero could work on Linux and Mac but not on windows where blockchain is stored in `C:\ProgramData\bitmonero`. I.e outside the users home folder.  I prefer the current setup over that. 

Good idea to make cli wallet more aware of the wallet paths used by the GUI. Maybe you could open an issue in the cli repo for this?

+enhancement

## Jaqueeee | 2017-08-07T21:23:21+00:00
testing the new labeling system. didn't mean to close this issue. Will be opened again shortly :)

## medusadigital | 2017-08-08T14:35:37+00:00
seems it doesnt open again even if the label is removed 

## danrmiller | 2017-08-08T16:06:48+00:00
to re-open you tell the bot to remove the label, don't remove the command you gave to add the label.

-wontfix


## sanderfoobar | 2018-03-30T01:52:36+00:00
+enhancement

## mmbyday | 2018-12-16T05:55:43+00:00
Soon the wallet will be encrypted by default and stored in the lmdb database.
Won't be an issue then.
+resolved 

## dEBRUYNE-1 | 2018-12-16T07:58:13+00:00
+resolved

# Action History
- Created by: SleepingShell | 2017-07-14T02:22:42+00:00
- Closed at: 2018-12-16T08:09:24+00:00
