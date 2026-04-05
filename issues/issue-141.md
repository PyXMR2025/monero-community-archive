---
title: Pause mining when using computer
source_url: https://github.com/xmrig/xmrig/issues/141
author: Valke88
assignees:
- xmrig
labels:
- enhancement
- wontfix
created_at: '2017-10-06T19:11:18+00:00'
updated_at: '2021-11-02T09:03:00+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:30:47+00:00'
---

# Original Description
Hi,

Is it possible to stop mining for x amount of minutes after mouse or keyboard input?

Regards, Valke

# Discussion History
## xmrig | 2017-10-06T22:09:26+00:00
Now it possible only manually, press p/r in miner window.
Thank you.

## Twanislas | 2017-10-22T08:40:11+00:00
Hi !

I would also love this, a little bit like how the NiceHash Legacy miner does. Wait for computer to be idle for at least <x> seconds then start/resume mining, and pause mining whenever the computer is not idle anymore or there is peripheral input (mouse, keyboard, whatever (so this includes remote input such as RDP, VNC, etc..)

Thanks for the great work out there, xmrig is a big perf increase for me ! ;)

## EUA | 2017-11-13T00:54:08+00:00
I have 8/16 cores and I don't like pausing, instead want to pause threads when necessary!
I open issue #195 due this purpose.
Regards.

## dunklesToast | 2017-11-26T17:12:39+00:00
Would be nice if there is also an (POST) API Endpoint to change the miners state - have some great ideas for little scripts with that :)

## ghost | 2017-12-08T17:03:11+00:00
is there any meaningful difference between issuing `STOP`/`CONT` signals and sending literal `p`/ `r` key events? mmmh obviously the keepalives stop

## MetallianFR68 | 2017-12-23T22:52:01+00:00
+1 for this feature.
I have 10 employees.
I ask them to run the miner manually at the end of their workday but they always forget.
With such a feature, I could run the miner in background and set it to launch after 5mn idle time.

## Zelecktor | 2018-02-02T16:52:32+00:00
anyone working on this? some miner like Silent Miner got this feature.
https://xmrminer.net/
If someone risk in buy and apply reverse engineering to got the source code of that miner, would be great

## Zelecktor | 2018-02-03T05:57:08+00:00
I found that this feature is used by lots of miners
https://www.reddit.com/r/EtherMining/comments/6eip9a/automatic_mining_in_windows_while_idle_task/

Just add Task Scheduler at the source code and make a custom configure
@xmrig can you have a look to this? thanks in advance

## Zambi9 | 2018-02-19T05:09:26+00:00
Even better will be - use x threads for idle time, y threads for non-idle time.

## leonelsr | 2020-05-30T03:35:06+00:00
> Even better will be - use x threads for idle time, y threads for non-idle time.

At least on Windows, I've just implemented a AutoHotkey script that does this by changing **config.json** file on the fly. Pretty easy to improve, tweak and extend to any other intents (like fully stopping the miner when PC is in use).
It currently uses PowerShell Core 7.0 `pwsh.exe` to modify the JSON file more easily, but should work with standard `powershell.exe` as well.

The gist features a suitable `config.json` sample for reference

https://gist.github.com/leonelsr/25e06a88cd8fc4efc6f0a9a9568ef27e

## jaga3421 | 2021-01-19T14:23:57+00:00
I am trying to implement pause/resume from a node environment. Right now, my option is to identify the keyboard/mouse inputs from a node module like iohook and then kill the process/start the process. Would like the expert mind's input on this approach. 

## exclm | 2021-08-14T12:47:03+00:00
Sample solutions [here](https://stackoverflow.com/a/68681090/4246799)

## gaga9999 | 2021-10-18T11:56:08+00:00
i would love a <time> parameter with p/r, i.e. p180 (3 hours),
from my experience any idle-program using much cpu is just fucking up the gui experience any way, so i would just prefer pause -time as i got the thing running on a daemon-watcher which restarts it if it exits, so all i need is a: hey pause 3hours, now i will work for max 3h, but i will forget to unpause.
btw thanks for the program

## G2G2G2G | 2021-11-02T03:11:12+00:00
This was already marked as won't fix, so they're not going to fix/add it. It's been years of milestone pushback etc. To add this functionality is very basic and exclm linked one example. 

## SChernykh | 2021-11-02T09:03:00+00:00
https://xmrig.com/docs/miner/config/misc#pause-on-active

# Action History
- Created by: Valke88 | 2017-10-06T19:11:18+00:00
- Closed at: 2019-08-02T12:30:47+00:00
