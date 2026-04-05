---
title: OSX running xmrig.exe
source_url: https://github.com/xmrig/xmrig/issues/229
author: danpilgrim
assignees: []
labels: []
created_at: '2017-11-29T09:57:57+00:00'
updated_at: '2018-03-14T23:30:14+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:30:14+00:00'
---

# Original Description
So, when I run xmrig.exe on OSX.. I get this error
![screen shot 2017-11-29 at 2 41 46 am](https://user-images.githubusercontent.com/15642286/33369268-39907948-d4b1-11e7-9b7f-62ee73f401a9.png)
So, when I copy the config.json to that folder, I run it again and get this new error..
![screen shot 2017-11-29 at 2 43 09 am](https://user-images.githubusercontent.com/15642286/33369279-40c88052-d4b1-11e7-9dae-0040acdac432.png)

Any help?


# Discussion History
## rtau | 2017-11-29T14:44:11+00:00
I bet there's something wrong with your config.json. Did you try with a minimal one first, then add your config one by one and see?

Or, either line 1692 or byte 1692 has an invalid value.

## xmrig | 2017-11-30T01:32:05+00:00
Please show your config.json, config file must be valid JSON.
Thank you.

## sanminsoe | 2018-01-26T11:51:18+00:00
I have same issue. Help us to show the right direction.

## vekunz | 2018-01-26T12:57:54+00:00
Are you sure, you're running xmrig.exe on your Mac? Because .exe executables are Windows only.

# Action History
- Created by: danpilgrim | 2017-11-29T09:57:57+00:00
- Closed at: 2018-03-14T23:30:14+00:00
