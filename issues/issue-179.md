---
title: Worker in config.json
source_url: https://github.com/xmrig/xmrig/issues/179
author: gboelter
assignees:
- xmrig
labels:
- enhancement
created_at: '2017-10-29T12:18:04+00:00'
updated_at: '2020-02-09T10:37:56+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:37:56+00:00'
---

# Original Description
Is there a way to add the worker to my address using the environment variable from Windows or Linux in config.json? Something like 

"user": "48edfHu7V9Z84YzzMa6fUueoELZ9ZRXq9VetWzYGzKt52XU5xvqgzYnDK9URnRoJMk1j8nLwEVsaSWJ4fhdUyZijBGUicoD.%computername%",

# Discussion History
## xmrig | 2017-10-29T13:01:55+00:00
You can use command line options for environment variables, it can be used with or instead of config file.

Actually it not hard to add support for it on Windows, there has `ExpandEnvironmentStrings` function, on Linux need write some custom code with regex or something like that.
Thank you.

## NmxMilk | 2017-10-29T18:41:00+00:00
What would be nice is to have a new option --user-extension that when specified would be concatenated to the user.
This will allow to run on several machines, using a shared config file,  with a simple command like
$ xmrig -c config.json --user-extension \`hostname\`

This would be usefull for people running xmrig on different similar machines.



## xmrig | 2017-10-29T21:55:00+00:00
How to specify worker id depends of pool, for some pools it simple added to wallet address, for others it should specified in password. Also some pools don't support worker id at all.
Thank you.

## gboelter | 2017-10-30T04:09:40+00:00
Ok, what about a config.txt instead where I can add some placeholders like '.%computername%' or '$hostname'?
This file could be easily converted by xmrig to a valid config.json file during startup using my placeholders?

## djdomi | 2018-02-01T10:24:06+00:00
Hi

To be easy:

- Windows uses: %hostname%
-Linux useses: $HOSTNAME (UPPERCASE!) 

## xmrig | 2019-12-22T18:08:56+00:00
Implemented in dev branch, docs https://xmrig.com/docs/miner/environment-variables
Thank you.

# Action History
- Created by: gboelter | 2017-10-29T12:18:04+00:00
- Closed at: 2020-02-09T10:37:56+00:00
