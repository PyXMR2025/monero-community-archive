---
title: 'fatal error: wallet/api/wallet2_api.h: No such file or directory'
source_url: https://github.com/monero-project/monero-gui/issues/2407
author: dchmelik
assignees: []
labels: []
created_at: '2019-10-04T02:59:47+00:00'
updated_at: '2019-10-04T06:22:58+00:00'
type: issue
status: closed
closed_at: '2019-10-04T06:15:14+00:00'
---

# Original Description
Since it's unclear how to install precompiled gui wallet (normally there'd at least be instructions for setup in /usr/local) I tried compliling gui wallet 0.14.1.0 on Kubuntu 19.04 (with a 
[log](https://gist.github.com/dchmelik/0cb855b3df148443f80d73bcb5db5dde).)  It ends up saying several times 'fatal error: wallet/api/wallet2_api.h: No such file or directory.'  I see someone had this error in the past and the ticket was closed without anything really being explained.

# Discussion History
## xiphon | 2019-10-04T06:09:45+00:00
You have to `git clone` GUI repository instead of using .zip source archive.

## dchmelik | 2019-10-04T06:15:14+00:00
Alright.  I had another problem when I did that (will post shortly) so someone on the freenode IRC said don't do that, rather than download a stable normal version-numbered release.

## xiphon | 2019-10-04T06:22:58+00:00
Just do `git checkout v0.14.1.0` after cloning the repo to switch the source tree to the latest tagged release version.

# Action History
- Created by: dchmelik | 2019-10-04T02:59:47+00:00
- Closed at: 2019-10-04T06:15:14+00:00
