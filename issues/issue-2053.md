---
title: Bake options into binary
source_url: https://github.com/xmrig/xmrig/issues/2053
author: pamlloyd
assignees: []
labels: []
created_at: '2021-01-21T20:35:40+00:00'
updated_at: '2021-01-22T16:12:19+00:00'
type: issue
status: closed
closed_at: '2021-01-22T16:12:19+00:00'
---

# Original Description
Not really an issue, just a question.  I have a set of options, such as coin, tls, log-file, etc, that I use across my machines.  I was wondering if there is a way I can "bake" them into the compiled binary instead of using a config file or additional command line options.  I just want to run it as  is: ./xmrig

Thanks, 
Pam

# Discussion History
## snipeTR | 2021-01-21T21:26:56+00:00
https://github.com/xmrig/xmrig/blob/master/src/core/config/Config_default.h

## pamlloyd | 2021-01-21T22:03:31+00:00
Thanks, I altered the values in the Config_default.h and rebuilt, but it was still asking for the a config file.  :(

./xmrig
[2021-01-21 15:44:39.834] unable to open "/tmp/config.json".
[2021-01-21 15:44:39.835] unable to open "/home/lloyd/.xmrig.json".
[2021-01-21 15:44:39.835] unable to open "/home/lloyd/.config/xmrig.json".
[2021-01-21 15:44:39.835] no valid configuration found, try https://xmrig.com/wizard


## snipeTR | 2021-01-21T23:51:07+00:00
#957

## pamlloyd | 2021-01-22T16:12:19+00:00
Thanks snipeTR!  Just needed to added -DWITH_EMBEDDED_CONFIG=ON after editing Config_default.h

# Action History
- Created by: pamlloyd | 2021-01-21T20:35:40+00:00
- Closed at: 2021-01-22T16:12:19+00:00
