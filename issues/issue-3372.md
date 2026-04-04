---
title: When Monero package from Debian bullseye/testing repo is installed the Monero
  gui is not working
source_url: https://github.com/monero-project/monero-gui/issues/3372
author: DeeDeeRanged
assignees: []
labels: []
created_at: '2021-04-02T17:36:50+00:00'
updated_at: '2022-03-28T06:44:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Installed the official monero package from Debian bullseye/testing, unable to install the Monero gui from whonix due to dependencies. The tarball monero-gui also only works when the official debian package is uninstalled.

I take it there is some cooperation going-on between devs and the Debian Cryptocoin Team <team+cryptocoin@tracker.debian.org> .

Would be nice to see monero-gui officially supported by Debian :)

# Discussion History
## ch9PcB | 2021-04-04T08:43:14+00:00
> Installed the official monero package from Debian bullseye/testing,

I am unable to locate the package in Debian 11. Can you provide me the direct link please?



## DeeDeeRanged | 2021-04-04T15:20:24+00:00
Hi,
The link is here https://packages.debian.org/bullseye/monero
Do note it is the monero-cli and monerod.

Succes ;)


## adrelanos | 2022-03-28T06:44:11+00:00
The https://gitlab.com/whonix/monero-gui package has been created by me (but of course I didn't create monero or monero-gui, only the package which is a tiny source code size by comparison).

I wasn't previously aware of this ticket. Hence late answer. If things are reported to https://gitlab.com/whonix/monero-gui or if I am @adrelanos mentioned then I'll reply much quicker.

As for the issue.

> dpkg: error processing archive /tmp/apt-dpkg-install-iaStKd/10-monero_0.17.2.0+~
0+20200826-1_amd64.deb (--unpack):
> trying to overwrite '/usr/bin/monero-blockchain-ancestry', which is also in pac
kage monero-gui 0.17.3.0.0-1

https://gitlab.com/whonix/monero-gui doesn't need to be co-installed with https://packages.debian.org/bullseye/monero

https://gitlab.com/whonix/monero-gui contains both, CLI and GUI.

Use either:

* A) https://packages.debian.org/bullseye/monero OR,
* B) https://gitlab.com/whonix/monero-gui

There should be no need to install both at the same time.

> Installed the official monero package from Debian bullseye/testing, unable to install the Monero gui from whonix due to dependencies. The tarball monero-gui also only works when the official debian package is uninstalled.
> 
> I take it there is some cooperation going-on between devs and the Debian Cryptocoin Team [team+cryptocoin@tracker.debian.org](mailto:team+cryptocoin@tracker.debian.org) .

https://gitlab.com/whonix/monero-gui won't ever be in packages.debian.org.
https://gitlab.com/whonix/monero-gui has no contact with Debian Cryptocoin Team.
Reasons:
See the history...
https://ccs.getmonero.org/proposals/adrelanos-debian-package.html

> The tarball monero-gui also only works when the official debian package is uninstalled.

For that I recommend a separate issue and not mixing it into this issue. I also recommend posting the full links to what package you're talking about to avoid confusion.


# Action History
- Created by: DeeDeeRanged | 2021-04-02T17:36:50+00:00
