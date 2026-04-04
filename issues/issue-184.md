---
title: 'exceptions.ImportError: cannot import name CoverallsCommand'
source_url: https://github.com/monero-project/meta/issues/184
author: mesouug
assignees: []
labels: []
created_at: '2018-02-22T18:01:00+00:00'
updated_at: '2020-03-09T22:03:59+00:00'
type: issue
status: closed
closed_at: '2020-03-09T22:03:59+00:00'
---

# Original Description
Good day.

I'm trying to replicate your buildbot setup. I'm using python 2.7.12 and buildbot 0.8.14 in virtualenv directory. When I execute `buildbot checkconfig master.cfg` I'm getting rather strange error.
```
exceptions.ImportError: cannot import name CoverallsCommand

Configuration Errors:
  error while parsing config file: cannot import name CoverallsCommand (traceback in logfile)
```
Can you please point me what I'm doing wrong?

Thanks,
Mikhail.

# Discussion History
## danrmiller | 2018-02-22T20:14:22+00:00
Hi. While I haven't checked in the buildbot config in a while, it shouldn't affect your issue.
You do have this file?
https://github.com/monero-project/meta/blob/master/buildbot/master/commands/coveralls.py

## mesouug | 2018-02-22T20:19:21+00:00
Yes. I just cloned that repository. I've looked for all possible ways to import this class. All manuals state that I need to have `__init__.py` file in `commands` the line to import this class changes completely to: `from coveralls import CoverallsCommand`. It works with just python itself but throws same error with buildbot.

## danrmiller | 2018-02-22T20:54:51+00:00
Thanks I just took a look and I get the same error you posted when running ```buildbot checkconfig master.cfg```

However, the command does seem to be working, take a look at the checks section of a kovri pull request such as https://github.com/monero-project/kovri/pull/813.

I'll try to look into this more.

## danrmiller | 2018-03-01T01:30:20+00:00
@mesouug Are you the one running an "xmr_buildbot" in #monero-bots on freenode that announces your builds on "http://buildbot.dev/"?

## mesouug | 2018-03-01T01:44:52+00:00
Sorry I will disable it.

## danrmiller | 2018-03-01T01:56:50+00:00
Well it just probably isn't much use in that particular channel since we can't resolve that url, but maybe say hey to me (pigeons) there and we can chat and maybe feed you some builds, maybe debug builds or run tests or something if you want.

# Action History
- Created by: mesouug | 2018-02-22T18:01:00+00:00
- Closed at: 2020-03-09T22:03:59+00:00
