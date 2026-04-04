---
title: mac monero-wallet-gui cannot be opened because of a problem
source_url: https://github.com/monero-project/monero-gui/issues/1715
author: ametadope
assignees: []
labels:
- resolved
created_at: '2018-10-31T01:52:32+00:00'
updated_at: '2018-10-31T07:42:23+00:00'
type: issue
status: closed
closed_at: '2018-10-31T07:27:24+00:00'
---

# Original Description
When I download the monero-gui-mac-x64-v0.13.0.3.tar.bz2 file, unzip it, and attempt to run the monero-wallet-gui.app file, I get the error "monero-wallet-gui cannot be opened because of a problem." I am running macOS 10.13.6.

# Discussion History
## gmerrall | 2018-10-31T05:15:05+00:00
Open the Console app on your machine and take a look at the "User Reports" section and you should hopefully see the crash log in there.  Just check the date/time field in the report to ensure you've got a current report and paste/attach here.
I'm also getting a crash on my Mac but want to ensure we've got the same issue before I contribute to this issue or open a new one.

## dEBRUYNE-1 | 2018-10-31T07:26:01+00:00
@ametadope & @gmerrall - There's basically four ways to resolve this issue.

1. Use the temporary work around described in [this guide](https://monero.stackexchange.com/questions/10364/gui-v0-13-0-3-does-not-start-on-mac-os-x-monero-wallet-gui-cannot-be-opened-bec). 

2. Use the GUI v0.13.0.4 pre-release binaries from [here](https://www.reddit.com/r/Monero/comments/9qrcw7/gui_v01304_prerelease_test_binaries_buildbot/).

3. Wait until GUI v0.13.0.4 is released, which includes the fix for this particular issue.

4. Compile GUI v0.13.0.4 yourself. 

5. Tempoarily use CLI v0.13.0.4, which can be found [here](https://www.reddit.com/r/Monero/comments/9r7inb/cli_v01304_beryllium_bullet_released/). 

## dEBRUYNE-1 | 2018-10-31T07:26:06+00:00
+resolved

# Action History
- Created by: ametadope | 2018-10-31T01:52:32+00:00
- Closed at: 2018-10-31T07:27:24+00:00
