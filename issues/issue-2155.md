---
title: 'Question: Is there Anyway of Making the rig-id in config_default.h a random
  number'
source_url: https://github.com/xmrig/xmrig/issues/2155
author: sapmi
assignees: []
labels:
- question
created_at: '2021-03-03T11:23:42+00:00'
updated_at: '2021-04-12T14:06:25+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:06:25+00:00'
---

# Original Description
I guess the parameters here are in a JSON format, similar to the normal config file. When running xmrig with command line parameters I used --rig-id %uname% no problem - which contains a string and a random number. 

I tried changing the parameter to %random% which is an environmental variable in windows, but the exe file will not run. If I put it in quotes within the parameters - it lists my rig ID as just %random% - 

"rig-id": %random%,   - program won't run
"rig-id": "%random%"   - rig ID is not a random number - its just random

Maybe a clue to solving this is, when I look at  Config_platform.h, I see this: { "rig-id",  1, nullptr, IConfig::RigIdKey   },

Any ideas? I am now completely stuck

# Discussion History
## xmrig | 2021-03-03T11:46:30+00:00
For config file you should use different syntax https://xmrig.com/docs/miner/environment-variables for example `"rig-id": "${random}"`.
Thank you.


## sapmi | 2021-03-06T10:37:20+00:00
Hello XMRIG, sorry for not saying thank you, had computer issues. So thank you!!!!!!

# Action History
- Created by: sapmi | 2021-03-03T11:23:42+00:00
- Closed at: 2021-04-12T14:06:25+00:00
