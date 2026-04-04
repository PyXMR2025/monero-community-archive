---
title: Add AppStream file to further ease of adoption
source_url: https://github.com/monero-project/monero-gui/issues/3478
author: scottAnselmo
assignees: []
labels: []
created_at: '2021-05-11T00:27:54+00:00'
updated_at: '2021-10-12T15:43:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Problem: Currently the GUI doesn't ship w/ an AppStream File. This causes problems in trying to package for Flatpak and get into FlatHub (https://github.com/flathub/flathub/pull/2124). This is notable because currently at least one major distro, Fedora, doesn't have an official GUI package manageable via Fedora's package manager or even w/ RPMFusion added as a source. This would be remedied by having the GUI in FlatHub

Solution: Add the AppStream XML file to the GUI packaging. Suggest following guidelines by FlatHub (https://github.com/flathub/flathub/wiki/App-Requirements#appstream). Guidelines/HowTos by distros such as [Debian's](https://wiki.debian.org/AppStream/Guidelines) or DE's like [KDE's](https://community.kde.org/Guidelines_and_HOWTOs/AppStream) may be useful

# Discussion History
## selsta | 2021-05-11T00:45:22+00:00
Why can't this be done on Flatpack / Flathub side?

Reading the guidelines this AppStream file has to be installed in a specific directory, we only offer static binaries on getmonero.org that don't install anything.

## selsta | 2021-05-11T00:51:58+00:00
Though we do offer to install a .desktop file on first startup, is that enough? Similar thing could theoretically be done for this .AppStream thing

## scottAnselmo | 2021-05-11T00:59:00+00:00
Hopefully, I can ask in the FlatHub PR if given more details to ask with. I think the main thing is the validation: 

_Applications must provide appstream data and pass `flatpak run org.freedesktop.appstream-glib validate`. If application metadata has not been provided by the upstream, it should be licensed with Creative Commons Zero, version 1, by stating CC0-1.0 in metadata_license._

Updating original comment to reference [FlatHub guidelines](https://github.com/flathub/flathub/wiki/App-Requirements#appstream) instead of Debian since FlatHub is the main point of interest

## selsta | 2021-07-13T22:21:18+00:00
Flathub added Monero, is this still required?

## scottAnselmo | 2021-07-14T07:46:51+00:00
Not required, just a recommended guideline for having standardized software metadata across distros maintained by Red Hat, Debian, and Canonical. While still helpful to have, it is not a blocker for Monero remaining on FlatHub.

## q7nm | 2021-10-12T15:43:24+00:00
It would be nice if [this](https://github.com/flathub/org.getmonero.Monero/blob/master/extra/org.getmonero.Monero.metainfo.xml) appstream file appeared in monero-gui.

# Action History
- Created by: scottAnselmo | 2021-05-11T00:27:54+00:00
