---
title: WARNING,net:FATAL,net.p2p:FATAL ...
source_url: https://github.com/monero-project/monero/issues/3342
author: wmoreno3
assignees: []
labels: []
created_at: '2018-03-04T01:07:22+00:00'
updated_at: '2018-03-04T13:39:50+00:00'
type: issue
status: closed
closed_at: '2018-03-04T13:38:54+00:00'
---

# Original Description
I have this information on `monerod.log`

`INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO`

How I can fix it?

# Discussion History
## moneromooo-monero | 2018-03-04T09:03:56+00:00
set_log SETTINGYOUPREFER
There's no central list of all existing categories, but you can find out with:
```
git grep define.MONERO_DEFAULT_LOG_CATEGORY | cut -d : -f 2 | sort | uniq | sed -e s/^[^\"]*\"// -e s/\".*$//
```

## wmoreno3 | 2018-03-04T13:38:50+00:00
Thanks you

## fluffypony | 2018-03-04T13:39:50+00:00
@wmoreno3 just butting in to say you have the most appropriate surname;)

# Action History
- Created by: wmoreno3 | 2018-03-04T01:07:22+00:00
- Closed at: 2018-03-04T13:38:54+00:00
