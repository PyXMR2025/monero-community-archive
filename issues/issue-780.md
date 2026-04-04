---
title: Create a new repository who will host all files in downloads.getmonero.org
  and videos/other media files
source_url: https://github.com/monero-project/monero-site/issues/780
author: erciccione
assignees: []
labels: []
created_at: '2018-06-25T11:19:49+00:00'
updated_at: '2020-04-07T09:41:26+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:41:25+00:00'
---

# Original Description
This will make the `monero-site` repo lighter and will make possible for mirror-websites to link directly to it. Also, general downloadable content could be uploaded here and made easily available to the community.
Opinions?

Proposal made by @fluffypony, see discussions in #393 and #249 

# Discussion History
## erciccione | 2018-06-25T11:20:32+00:00
+discussion

## fluffypony | 2018-06-25T11:35:20+00:00
Here's the current content of the downloads folder:

```
./kovri
./kovri/hosts.txt

./source
./source/monero-source-v0.11.1.0.tar.bz2
./source/monero-source-v0.11.0.0.tar.bz2
./source/monero-gui-source-v0.11.0.0.tar.bz2
./source/monero-source-v0.12.0.0.tar.bz2

./gui
./gui/monero-gui-install-win-x64-v0.11.1.0.exe
./gui/monero-gui-linux-x64-v0.10.3.1.tar.bz2
./gui/monero-gui-mac-x64-v0.10.3.1.tar.bz2
./gui/monero-gui-linux-x86-v0.11.1.0.tar.bz2
./gui/monero-gui-linux-x64-v0.11.1.0.tar.bz2
./gui/monero-gui-linux-x64-v0.12.0.0.tar.bz2
./gui/monero-gui-linux-x64-v0.11.0.0.tar.bz2
./gui/monero-gui-win-x64-v0.11.1.0.zip
./gui/monero.gui.win.x64.beta.zip
./gui/monero-gui-linux-x86-v0.10.3.1.tar.bz2
./gui/monero.gui.mac.x64.beta.tar.bz2
./gui/monero.gui.linux.x64.beta.tar.bz2
./gui/monero-gui-win-x64-v0.10.3.1.zip
./gui/monero-gui-mac-x64-v0.11.0.0.tar.bz2
./gui/monero-gui-mac-x64-v0.11.1.0.tar.bz2
./gui/monero.gui.linux.x86.beta.tar.bz2
./gui/monero-gui-linux-x86-v0.11.0.0.tar.bz2
./gui/monero-gui-mac-x64-v0.12.0.0.tar.bz2
./gui/monero-gui-win-x64-v0.11.0.0.zip
./gui/monero-gui-win-x64-v0.12.0.0.zip

./cli
./cli/monero.mac.x64.v0-9-2-0.tar.bz2
./cli/monero.freebsd.x64.v0-8-8-6.tar.bz
./cli/monero.mac.x64.v0-8-8-6.tar.bz2
./cli/monero-win-x86-v0.10.2.0.zip
./cli/monero-dragonflybsd-x64-v0.10.2.1.tar.bz2
./cli/monero-mac-x64-v0.10.2.0.tar.bz2
./cli/monero-freebsd-x64-v0.11.1.0.tar.bz2
./cli/monero-freebsd-x64-v0.10.3.1.tar.bz2
./cli/monero.linux.x64.v0-9-4-0.tar.bz2
./cli/monero.linux.x86.v0-9-3-0.tar.bz2
./cli/monero-mac-x64-v0.12.2.0.tar.bz2
./cli/monero-dragonflybsd-x64-v0.10.2.0.tar.bz2
./cli/monero-mac-x64-v0.10.2.1.tar.bz2
./cli/monero.win.x64.20140915.zip
./cli/monero-linux-armv8-v0.12.2.0.tar.bz2
./cli/monero-mac-x64-v0.10.3.1.tar.bz2
./cli/monero.linux.x64.20140824.tar.bz2
./cli/monero-linux-x64-v0.11.1.0.tar.bz2
./cli/monero-win-x64-v0.10.3.1.zip
./cli/monero.win.x64.v0-9-3-0.zip
./cli/monero.mac.x64.20140915.tar.bz2
./cli/monero-win-x64-v0.12.2.0.zip
./cli/monero.mac.x64.20140907.tar.bz2
./cli/monero-linux-x86-v0.10.3.0.tar.bz2
./cli/monero-mac-x64-v0.11.0.0.tar.bz2
./cli/monero-win-x64-v0.10.3.0.zip
./cli/monero-win-x64-v0.10.2.0.zip
./cli/monero-linux-armv8-v0.10.3.1.tar.bz2
./cli/monero-mac-x64-v0.11.1.0.tar.bz2
./cli/monero.win.x64.v0-10-1-0.zip
./cli/monero-linux-armv7-v0.10.2.0.tar.bz2
./cli/monero-linux-armv7-v0.10.2.1.tar.bz2
./cli/monero-freebsd-x64-v0.10.2.0.tar.bz2
./cli/monero.mac.x64.v0-8-8-5.tar.bz2
./cli/monero.win.x86.v0-10-1-0.zip
./cli/monero-linux-x86-v0.11.1.0.tar.bz2
./cli/monero.mac.x64.v0-10-1-0.tar.bz2
./cli/monero.mac.x64.v0-9-1-0.tar.bz2
./cli/monero-linux-armv8-v0.10.2.0.tar.bz2
./cli/monero.linux.x64.0610.tar.bz2
./cli/monero-win-x64-v0.11.0.0.zip
./cli/monero-dragonflybsd-x64-v0.10.3.1.tar.bz2
./cli/monero.win.x64.0610.zip
./cli/monero.linux.x64.v0-8-8-6.tar.bz2
./cli/monero-linux-x64-v0.10.3.0.tar.bz2
./cli/monero-linux-x64-v0.11.0.0.tar.bz2
./cli/monero.linux.arm7.v0-10-0-0.tar.bz2
./cli/monero-freebsd-x64-v0.11.0.0.tar.bz2
./cli/monero.win.x86.0526.zip
./cli/monero.win.x86.0520.zip
./cli/monero.win.x64.v0-9-2-0.zip
./cli/monero-win-x64-v0.12.0.0.zip
./cli/monero.freebsd.x64.v0-10-1-0.tar.bz2
./cli/monero.win.x64.v0-8-8-6.zip
./cli/monero.win.x86.v0-9-3-0.zip
./cli/monero.win.x64.0526.zip
./cli/monero.linux.x64.v0-10-0-0.tar.bz2
./cli/monero-linux-armv8-v0.11.1.0.tar.bz2
./cli/monero-linux-armv7-v0.10.3.1.tar.bz2
./cli/monero.mac.x64.0526.tar.bz2
./cli/monero-linux-x86-v0.12.1.0.tar.bz2
./cli/monero.win.x64.v0-8-8-5.zip
./cli/monero.linux.x86.v0-10-1-0.tar.bz2
./cli/monero-linux-x86-v0.11.0.0.tar.bz2
./cli/monero.linux.x64.v0-9-2-0.tar.bz2
./cli/monero.mac.x64.20140824.tar.bz2
./cli/monero.win.x86.v0-10-0-0.zip
./cli/monero.mac.x64.0610.tar.bz2
./cli/monero.linux.x64.v0-8-8-5.tar.bz2
./cli/monero-linux-x64-v0.12.1.0.tar.bz2
./cli/monero.win.x86.0610.zip
./cli/monero.linux.x64.v0-8-8-6b.tar.bz2
./cli/monero-linux-x86-v0.12.0.0.tar.bz2
./cli/monero.linux.x64.v0-10-1-0.tar.bz2
./cli/monero.win.x64.v0-9-4-0.zip
./cli/monero.linux.x64.20140915.tar.bz2
./cli/monero.linux.x64.0520.tar.bz2
./cli/monero-win-x86-v0.12.0.0.zip
./cli/monero-linux-armv7-v0.11.0.0.tar.bz2
./cli/monero.linux.x86.v0-10-0-0.tar.bz2
./cli/monero.win.x64.v0-9-0-0.zip
./cli/monero-win-x86-v0.11.0.0.zip
./cli/monero-linux-armv7-v0.12.0.0.tar.bz2
./cli/monero.mac.x64.v0-10-0-0.tar.bz2
./cli/monero-freebsd-x64-v0.10.2.1.tar.bz2
./cli/monero-linux-x86-v0.10.3.1.tar.bz2
./cli/monero.linux.x86.v0-9-1-0.tar.bz2
./cli/monero.win.x64.0520.zip
./cli/monero-win-x86-v0.12.2.0.zip
./cli/monero-mac-x64-v0.10.3.0.tar.bz2
./cli/monero-linux-armv7-v0.10.3.0.tar.bz2
./cli/monero-linux-x64-v0.10.2.1.tar.bz2
./cli/monero.win.x64.20140907.zip
./cli/monero-freebsd-x64-v0.10.3.0.tar.bz2
./cli/monero-linux-x86-v0.10.2.1.tar.bz2
./cli/monero.linux.x64.0526.tar.bz
./cli/monero.linux.x86.v0-9-2-0.tar.bz2
./cli/monero.linux.arm7.v0-9-2-0.tar.bz2
./cli/monero-win-x86-v0.10.3.0.zip
./cli/monero-dragonflybsd-x64-v0.10.3.0.tar.bz2
./cli/monero.linux.x64.v0-9-3-0.tar.bz2
./cli/monero.linux.arm7.v0-9-3-0.tar.bz2
./cli/monero-win-x86-v0.10.2.1.zip
./cli/monero.freebsd.x64.20140915.tar.bz
./cli/monero.linux.arm8.v0-10-0-0.tar.bz2
./cli/monero-linux-x64-v0.12.2.0.tar.bz2
./cli/monero-mac-x64-v0.12.0.0.tar.bz2
./cli/monero.win.x64.v0-10-0-0.zip
./cli/monero.mac.x64.v0-9-4-0.tar.bz2
./cli/monero.win.x86.v0-9-1-0.zip
./cli/monero-linux-armv8-v0.12.1.0.tar.bz2
./cli/monero-linux-x64-v0.10.3.1.tar.bz2
./cli/monero.mac.x64.v0-9-3-0.tar.bz2
./cli/monero-win-x64-v0.10.2.1.zip
./cli/monero.win.x64.v0-9-1-0.zip
./cli/monero-win-x64-v0.12.1.0.zip
./cli/monero.linux.x64.v0-9-1-0.tar.bz2
./cli/monero-linux-x86-v0.10.2.0.tar.bz2
./cli/monero-linux-armv8-v0.10.2.1.tar.bz2
./cli/monero.linux.x64.20140907.tar.bz2
./cli/monero-linux-x64-v0.10.2.0.tar.bz2
./cli/monero.freebsd.x64.v0-8-8-5.tar.bz
./cli/monero.linux.x64.v0-9-0-0.tar.bz2
./cli/monero-linux-x64-v0.12.0.0.tar.bz2
./cli/monero-dragonflybsd-x64-v0.11.1.0.tar.bz2
./cli/monero.mac.x64.0520.zip
./cli/monero-dragonflybsd-x64-v0.11.0.0.tar.bz2
./cli/monero.win.x86.v0-9-4-0.zip
./cli/monero-win-x64-v0.11.1.0.zip
./cli/monero-linux-x86-v0.12.2.0.tar.bz2
./cli/monero-mac-x64-v0.12.1.0.tar.bz2
./cli/monero.mac.x64.v0-9-0-0.tar.bz2
./cli/monero-linux-armv8-v0.10.3.0.tar.bz2
./cli/monero-linux-armv7-v0.12.2.0.tar.bz2
./cli/monero-linux-armv7-v0.11.1.0.tar.bz2
./cli/monero.linux.x86.v0-9-4-0.tar.bz2
./cli/monero-linux-armv8-v0.11.0.0.tar.bz2
./cli/monero-win-x86-v0.11.1.0.zip
./cli/monero.win.x64.20140824.zip
./cli/monero-win-x86-v0.10.3.1.zip
./cli/monero.linux.arm7.v0-10-1-0.tar.bz2

./resources
./resources/logo-200.jpg
./resources/branding.zip

./index.html
./blockchain.raw
./whitepaper_review.pdf
./whitepaper_annotated.pdf
```

```index.html``` is blank, as a catch in case someone visits the root folder. I guess it should be a meta redirect to getmonero.org/downloads, but whatevs. Whitepapers are historical links that should probably be maintained. blockchain.raw should obviously be in gitignore because it gets updated every 8 hours and can be reproduced.

## erciccione | 2020-04-07T09:41:25+00:00
This issue is old and was discussed and closed on gitlab.

# Action History
- Created by: erciccione | 2018-06-25T11:19:49+00:00
- Closed at: 2020-04-07T09:41:25+00:00
