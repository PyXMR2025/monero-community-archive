---
title: CUDA disabled if starting from miner
source_url: https://github.com/xmrig/xmrig/issues/2677
author: chriz74x
assignees: []
labels: []
created_at: '2021-11-10T14:52:20+00:00'
updated_at: '2021-11-11T19:43:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I don't know why but on Windows 11 if I setup a miner as in this page -> https://dev.to/courseprobe/how-to-mine-shiba-inu-shib-with-your-computer-in-under-5-minutes-in-2021-4e13 and the config.json to use cuda, when I start the miner (with admin privileges) CUDA is disabled. If I start the program directly it's enabled. Clues?

# Discussion History
## Spudz76 | 2021-11-11T19:29:09+00:00
You need the [`xmrig-cuda` plugin](https://github.com/xmrig/xmrig-cuda/) to use CUDA.

## chriz74x | 2021-11-11T19:30:19+00:00
Yes I know. It’s there.

## Spudz76 | 2021-11-11T19:39:10+00:00
Well then what's the GPU and which driver are you on and which CUDA version was the plugin built for?

## chriz74x | 2021-11-11T19:41:13+00:00
GTX 1060 6GB Cuda 11. The plug-in is there and works if I start the program directly. Doesn’t work if launching from the .bat file . Cuda is enabled in json.

## Spudz76 | 2021-11-11T19:42:12+00:00
oh then your "start in" folder is wrong, set it to where the xmrig works by itself.

Or toss a `cd` command at the top of the bat file to jump to the right place before launching.

# Action History
- Created by: chriz74x | 2021-11-10T14:52:20+00:00
