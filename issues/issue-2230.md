---
title: usning config file
source_url: https://github.com/xmrig/xmrig/issues/2230
author: Blisk
assignees: []
labels: []
created_at: '2021-04-02T13:09:00+00:00'
updated_at: '2021-04-03T09:07:43+00:00'
type: issue
status: closed
closed_at: '2021-04-03T09:07:43+00:00'
---

# Original Description
**Describe the bug**
I have config.json in folder where executable is, but whatever I change in config.json doesn't affect miner.
Do I need to configure in cmd to select config.json file or exe will automatically find it if exist in the same folder??
I didn't find any info about that.




# Discussion History
## Spudz76 | 2021-04-03T07:26:15+00:00
If you only run the exe (not some batch file, with extra arguments) then it will read config.json from same folder as the exe

Command line arguments always override config.json contents

## Blisk | 2021-04-03T08:27:27+00:00
I have batch with exe in it. Is there a way to have a log file?
Where I can find more Command line arguments?

## SChernykh | 2021-04-03T08:31:25+00:00
https://xmrig.com/docs/miner/command-line-options

## Blisk | 2021-04-03T09:07:43+00:00
thank you

# Action History
- Created by: Blisk | 2021-04-02T13:09:00+00:00
- Closed at: 2021-04-03T09:07:43+00:00
