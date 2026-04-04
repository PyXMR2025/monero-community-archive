---
title: 'Mac: Files in an odd location'
source_url: https://github.com/monero-project/monero-gui/issues/350
author: ghost
assignees: []
labels: []
created_at: '2016-12-23T17:01:54+00:00'
updated_at: '2017-03-03T15:28:42+00:00'
type: issue
status: closed
closed_at: '2017-03-03T15:28:42+00:00'
---

# Original Description
Not a big problem, but the location that the GUI installs its files on OSX is quite odd. It took me.a while to find before I realised they were right in front of my eyes.

At the minute the app files are stored at:

> /users/[name]

Usually apps would store their information in a hidden folder at: 

> /users/[name]/library/application support

# Discussion History
## medusadigital | 2016-12-24T10:01:14+00:00
the config File is located in: `$HOME/Library/Preferences/org.getmonero.monero-core.plist`

wallets get created in `/users/xxx/Monero/wallets`

## ghost | 2016-12-24T10:02:48+00:00
I see. Thanks!

## Jaqueeee | 2017-03-03T11:48:35+00:00
Can this be closed @SilverPin?

# Action History
- Created by: ghost | 2016-12-23T17:01:54+00:00
- Closed at: 2017-03-03T15:28:42+00:00
