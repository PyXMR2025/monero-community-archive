---
title: create Debian package / APT repository
source_url: https://github.com/monero-project/monero-gui/issues/2887
author: adrelanos
assignees: []
labels:
- proposal
created_at: '2020-05-05T17:47:49+00:00'
updated_at: '2020-05-11T09:52:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Dunno if you are aware of this (successfully funded) CCS proposal. Not too important for what I am suggesting here.
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/130
Initial implementation is done: https://github.com/Whonix/monero-gui

Disadvantage: users need to trust my signing key on top of your signing key.

Proposal:

As a "bonus" on top of that proposal, I am wondering if you would be interested to integrate into your build process:

1) building `.deb` package and/or,
2) creating APT repository metadata?

I would create bash scripts to maximally/fully automate the process. Seems doable to me. The monero-gui Debian package metadata is ready, and build of `.deb` packages and APT repository metadata (such as deb.whonix.org) is automated in Whonix build script. I could create a standalone version and contribute it here.

What I would need from you:

* answering some questions about current build process (public information only)
* maybe minor help with the existing Makefile / build script, i.e. calling the deb/apt creation automation script

The final result would be, you could run (draft):

* `./create_deb.bsh`
* `./create_apt_repo.bsh`
* `./upload_apt_repo.bsh` (which would rsync to deb.getmonero.org)

The two or three commands (matter of taste) could be integrated into your build scripts / process.

What do you think?

I would have to ask: are you a Debian user, or building on Debian or using some Debian based distribution? If yes, that would simplify some things. If not, a Debian based build chroot could work too.

# Discussion History
# Action History
- Created by: adrelanos | 2020-05-05T17:47:49+00:00
