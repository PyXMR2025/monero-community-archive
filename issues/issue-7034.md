---
title: '[CI] Windows build failing - deprecated actions'
source_url: https://github.com/monero-project/monero/issues/7034
author: mj-xmr
assignees: []
labels: []
created_at: '2020-11-21T07:10:46+00:00'
updated_at: '2020-12-04T05:53:34+00:00'
type: issue
status: closed
closed_at: '2020-12-04T05:53:34+00:00'
---

# Original Description
For the below PRs (and others) the Windows build fails since about Saturday, 14.11.

[Xiphon's](https://github.com/monero-project/monero/pull/7030) 
[Mine1](https://github.com/monero-project/monero/pull/6956) 
[Mine2](https://github.com/monero-project/monero/pull/6977) 
[Vtnerd's](https://github.com/monero-project/monero/pull/7028) 

The error message is:

Error: Unable to process command '::add-path::D:\a\_temp\msys' successfully. 

105Error: The `add-path` command is disabled. Please upgrade to using Environment Files or opt into unsecure command execution by setting the `ACTIONS_ALLOW_UNSECURE_COMMANDS` environment variable to `true`. For more information see: https://github.blog/changelog/2020-10-01-github-actions-deprecating-set-env-and-add-path-commands/ 

106Error: Unable to process command '::set-env name=MSYSTEM::MINGW64' successfully. 

107Error: The `set-env` command is disabled. Please upgrade to using Environment Files or opt into unsecure command execution by setting the `ACTIONS_ALLOW_UNSECURE_COMMANDS` environment variable to `true`. For more information see: https://github.blog/changelog/2020-10-01-github-actions-deprecating-set-env-and-add-path-commands/

# Discussion History
## sumogr | 2020-11-21T07:24:09+00:00
skipping eine's and using msys2/setup-msys2@v2 will fix that i guess. its not the commits

## selsta | 2020-11-21T07:25:25+00:00
Thanks, there should be a PR for it already from a couple weeks ago, we just didn’t merge it yet.

## selsta | 2020-11-21T07:25:53+00:00
#6982 

## mj-xmr | 2020-11-21T18:31:28+00:00
Thanks for the input. I confirm, that the version switch helped in my PRs.

## selsta | 2020-11-22T12:48:50+00:00
Issue is resolved now.

## mj-xmr | 2020-12-04T05:53:34+00:00
Since this is resolved for a time long enough, I think I can close the issue.

# Action History
- Created by: mj-xmr | 2020-11-21T07:10:46+00:00
- Closed at: 2020-12-04T05:53:34+00:00
