---
title: any help, termux build freeze after few runs
source_url: https://github.com/xmrig/xmrig/issues/2575
author: ignisc4t
assignees: []
labels: []
created_at: '2021-09-09T03:46:51+00:00'
updated_at: '2021-09-09T17:12:52+00:00'
type: issue
status: closed
closed_at: '2021-09-09T17:12:52+00:00'
---

# Original Description
so I just compile this and tries with the default setting.
run for few times, then it's just freeze.

I've tried to disable huge pages in config.json and recompile back, but I got the same issues. even tried -t 1 to lower the thread amount to a single thread.

another thing, hashraye command doesn't work, the rest is okay.

here's the last picture of the fallen comrades:

![Screenshot_20210909-104541](https://user-images.githubusercontent.com/68355570/132619061-1c26337f-1585-42bb-95ad-f81d63f18603.jpg)


if this is the device problem (e.g. old device, then I'm understand, the fix would be get a new device with higher spec. Just want to make something useful out of this old guy).

# Discussion History
## SChernykh | 2021-09-09T09:48:38+00:00
Your device doesn't have enough RAM, xmrig gets stuck initializing dataset. Try running in light mode: `--randomx-mode=light` in the command line or `"mode": "light",` in config.json (`randomx` section)

## ignisc4t | 2021-09-09T10:23:02+00:00
> Your device doesn't have enough RAM, xmrig gets stuck initializing dataset. Try running in light mode: `--randomx-mode=light` in the command line or `"mode": "light",` in config.json (`randomx` section)

ah thanks, I was just testing, if it worth it, then release the kraken army(you know what I mean). otherwise, find another solution.

I'll try this.

## ignisc4t | 2021-09-09T10:39:28+00:00
after trying :


```
./xmrig: unrecognized option `--random-mode=light`
```

I'll try to recompile again or something

## SChernykh | 2021-09-09T10:48:07+00:00
You missed `x` in `--randomx-mode=light`

## ignisc4t | 2021-09-09T11:22:06+00:00
> You missed `x` in `--randomx-mode=light`

ah yes, my bad.
well, I use the config file with 2 threads, looks like its working, gonna leave it for awhile to see how long it can run.

![Screenshot_20210909-181832](https://user-images.githubusercontent.com/68355570/132676959-9096d8ce-3bb1-45e9-9e0c-18729be966f6.jpg)




# Action History
- Created by: ignisc4t | 2021-09-09T03:46:51+00:00
- Closed at: 2021-09-09T17:12:52+00:00
