---
title: Opening wallet created in CLI does not work
source_url: https://github.com/monero-project/monero-gui/issues/4058
author: Querens
assignees: []
labels: []
created_at: '2022-10-30T19:30:07+00:00'
updated_at: '2023-01-18T05:59:08+00:00'
type: issue
status: closed
closed_at: '2023-01-18T05:59:08+00:00'
---

# Original Description
I have installed monero-gui to replace CLI. Trying to open <user_name>.keys from wallet created in CLI results in "wrong password" error while this same password opens the wallet from CLI fine. 

# Discussion History
## selsta | 2022-10-30T21:50:29+00:00
Which operating system are you using? Which version do you use?

## Querens | 2022-10-30T22:06:43+00:00
Debian GNU/Linux bookworm/sid 
i    --\ monero-gui                                                0:0.18.1.2-1

## selsta | 2022-10-30T22:09:30+00:00
I assume you installed it using your package manager? Can you try to reproduce the issue with the GUI binary from getmonero.org ?

## Querens | 2022-10-30T23:14:38+00:00
 Isn't that a correct repository? Also link in the description for debian package leads nowhere
 
 Homepage: https://github.com/Whonix/monero-gui
 Priority: optional
 Section: misc
 Maintainer: Patrick Schleizer <adrelanos@whonix.org>
 Architecture: all
 Compressed Size: 96.1 M
 Uncompressed Size: 345 M
 Source Package: monero-gui
 Label: Whonix
 Origin: Whonix:deb.whonix.org [all]
 Origin URI: https://deb.whonix.org/pool/main/m/monero-gui/monero-gui_0.18.1.2-1_all.deb 

## selsta | 2022-10-30T23:19:34+00:00
It's maintained by a third party. Would be great it you could test both your issues with the getmonero.org binary so that we can make sure it's not related to the debian package.

## selsta | 2023-01-18T05:59:08+00:00
Closing due to inactivity and no reply from issue creator.

# Action History
- Created by: Querens | 2022-10-30T19:30:07+00:00
- Closed at: 2023-01-18T05:59:08+00:00
