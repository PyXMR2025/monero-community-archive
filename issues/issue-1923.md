---
title: Check for config file in standard directories on Linux/BSD
source_url: https://github.com/xmrig/xmrig/issues/1923
author: nopeinomicon
assignees: []
labels:
- enhancement
created_at: '2020-10-31T07:15:44+00:00'
updated_at: '2020-11-02T07:37:40+00:00'
type: issue
status: closed
closed_at: '2020-11-02T07:37:40+00:00'
---

# Original Description
Hello, I'm attempting to package xmrig on OBS for distribution on OpenSUSE, but the one roadblock I see right now is that the package lacks a way to load config files from standard locations (i.e. /etc and ~/.config) without an extra command line argument. 

From what I know it would probably be best to check for the config file at /etc/xmrig.json, ~/.xmrig.json, and ~/.config/xmrig.json, but I'm not absolutely sure about the exact paths and filenames.

Adding this change here upstream would make distribution-specific packaging on Linux and BSD systems much easier.

I'd be totally willing to try to submit a patch for this myself with a little guidance on some specifics here.

# Discussion History
## nopeinomicon | 2020-10-31T07:20:54+00:00
Also attached to this I think it would be a good idea for the app to copy the default config to ~/.config/xmrig.json upon launch or add a command line argument to output the default config to a file, for ease of use, but that isn't totally necessary.

# Action History
- Created by: nopeinomicon | 2020-10-31T07:15:44+00:00
- Closed at: 2020-11-02T07:37:40+00:00
