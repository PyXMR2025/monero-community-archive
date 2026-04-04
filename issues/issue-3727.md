---
title: (Feature Request) Store configs in ~/.config/ rather than home folder for linux
source_url: https://github.com/monero-project/monero-gui/issues/3727
author: peepo5
assignees: []
labels: []
created_at: '2021-11-05T14:36:11+00:00'
updated_at: '2024-04-11T14:51:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is annoying because it clutters the home directory.

# Discussion History
## selsta | 2021-11-05T18:19:06+00:00
Which config are you talking about exactly? The `.bitmonero` folder or the default wallet location (`~/Monero`)?

## peepo5 | 2021-11-05T21:17:13+00:00
Both

## peepo5 | 2021-11-05T21:18:01+00:00
For data, .local/share/ is the standard I am pretty sure. Any configs are normally stored in folders inside of .config/

## HumanG33k | 2021-11-11T00:07:12+00:00
All information are https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html 
By the way MacOs and Windows have this kind of specification too.

## mj-xmr | 2022-03-03T08:04:56+00:00
I'll gladly take it up, unless there's already some progress made by somebody else?

## mj-xmr | 2022-03-03T16:42:46+00:00
This task has to be split into 2 parts. The "config" directory in question is AFAIK created by the GUI, while the daemon's `.bitmonero` is indeed created by the daemon. The CLI wallet simply creates its files in the current working directory.

## mj-xmr | 2022-03-04T09:06:22+00:00
Related GUI PR: https://github.com/monero-project/monero-gui/pull/2272 (Re: config directory, not data)

## jarlucmat | 2024-04-11T14:51:57+00:00
Hello everyone,

Like peepo said either respecting the XDG schema or giving a config parameter like "--config-file" to monero-wallet-gui command line which allows moving the files away from the home root directory. 

Preferred scenario is that all files regarding monero are somewhere under .config/monero. The wallet can already be moved but there is .shared-ringdb and .bitmonero and settings.ini not. 

# Action History
- Created by: peepo5 | 2021-11-05T14:36:11+00:00
