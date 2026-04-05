---
title: ignoring --threads=1
source_url: https://github.com/xmrig/xmrig/issues/2851
author: eofreternal
assignees: []
labels: []
created_at: '2022-01-01T04:16:20+00:00'
updated_at: '2022-01-02T19:19:52+00:00'
type: issue
status: closed
closed_at: '2022-01-02T19:19:52+00:00'
---

# Original Description
**Describe the bug**
XMRig ignores `./xmrig --threads=1` and proceeds with 5 threads anyway

**To Reproduce**
Download lastest xmrig
Make a config file from XMRig.com wizard
run xmrig with `--threads=N` switch

**Expected behavior**
XMRig should proceed with 1 thread and CPU usage should go down to about ~100% (Only on core should be used)

**Required data**
 - Miner log as text or screenshot: Not sure what this is but it runs fine without error
 - Config file or command line (without wallets) https://pastebin.com/f9XUqkkL
 - OS: MacOS Catalina 10.15.7
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
I have to manually control CPU uasage with AppPolice (https://github.com/AppPolice/AppPolice)


# Discussion History
## Spudz76 | 2022-01-01T06:21:29+00:00
`--threads` is a *hint* which only works when there are no thread definitions already in config.json.

If there are already definitions you have to go edit them to remove all but one thread, or delete all thread definitions and then use `--threads` so it can write new definitions with the limiting-hint.

It simply never considers hints unless it is autoconfiguring which it doesn't even do if that part of the configuration already exists.

## eofreternal | 2022-01-01T15:10:38+00:00
@Spudz76 I tried finding all mentions of threads in the config.json file but nothing came up


## Spudz76 | 2022-01-02T08:30:11+00:00
Yeah because under the `cpu` section there are listings per algorithm like:

```
        "rx": [0, 2, 4],
```

Which are the thread definitions.  This sample has three.  Remove `4` and then you've got... two threads, one on `0` and one on `2`.

## eofreternal | 2022-01-02T19:19:52+00:00
Thank you

# Action History
- Created by: eofreternal | 2022-01-01T04:16:20+00:00
- Closed at: 2022-01-02T19:19:52+00:00
