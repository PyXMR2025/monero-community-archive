---
title: monero-core crashes on startup on some windows machines
source_url: https://github.com/monero-project/monero-gui/issues/76
author: medusadigital
assignees: []
labels: []
created_at: '2016-10-18T14:43:13+00:00'
updated_at: '2016-11-01T06:12:55+00:00'
type: issue
status: closed
closed_at: '2016-11-01T06:12:55+00:00'
---

# Original Description
This Issue is a placeholder for the crash on startup, which only some windows(?) users experience for now. 

All in all its unclear if the issue is due to some open GL version on windows or something else, the root is still being evaluated.  the logs are unfortunately empty, so the crash seems to happen very early in the start up process.

![appcrash](https://cloud.githubusercontent.com/assets/17108301/19481777/62dd7abe-954f-11e6-920b-56da352436d7.png)

Reports:

**ArticMine**: Graphics on GNU/Linux I am down to OpenGL 3.0 with success On Windows 10 fail at OpenGL 4.4 and 1.1

**iDunk**: OGL 3.3 on Ubuntu, radeon, Gallium 0.4, Mesa 11.2.0. OGL 4.5 on Windows 10, Crimson 16.10.1. Both success with minor artifacting on Ubuntu.

**luigi**: I have 4.4 and it works fine (win 10)

**medusa**: open GL 1.1 here on crashing machine (win7 x64, bitcoinQT runs fine). on same machine, it runs fine under Ubuntu with OGL 2.1 Mesa 11.2.0

issue maybe somehow far related to https://github.com/monero-project/monero-core/issues/69

please feel free to post any related report here


# Discussion History
## mbg033 | 2016-10-18T18:00:37+00:00
Right now I have stable crash for x86 build (doesn't matter of host - x64 or x86) - crashing on Wizard -> Create new wallet step


## medusadigital | 2016-10-18T18:33:22+00:00
hei @mbg033, this crash here is on startup and probalbly due to Opengl requirements. So users never see the wallet, it crashes imediately. @dEBRUYNE-1 will post some details later. 


## Jaqueeee | 2016-10-18T21:22:18+00:00
@mbg033 Could you try building with ANGLE or QtQuick2dRenderer support?
http://stackoverflow.com/questions/27704529/deploying-qt5-on-windows-without-hardware-acceleration


## Jaqueeee | 2016-10-18T21:30:31+00:00
@mbg033 And maybe also MESA? Not sure what's the best option. 


## mbg033 | 2016-10-21T22:22:47+00:00
Updated doc and .pro file to build agains Qt 5.7 MinGW from qt.io (not from msys2): https://github.com/monero-project/monero-core/pull/81


## dEBRUYNE-1 | 2016-10-29T16:45:15+00:00
This was resolved by @hyc. 


## medusadigital | 2016-11-01T06:12:54+00:00
issue is solved on all plaforms. requires libboos build without AVX.

fixed-> closed


# Action History
- Created by: medusadigital | 2016-10-18T14:43:13+00:00
- Closed at: 2016-11-01T06:12:55+00:00
