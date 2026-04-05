---
title: Windows binaries are not extracting!
source_url: https://github.com/xmrig/xmrig/issues/515
author: jodobear
assignees: []
labels:
- av
created_at: '2018-04-07T23:51:14+00:00'
updated_at: '2018-11-05T13:21:57+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:21:57+00:00'
---

# Original Description
The windows binaries are not being extracted! How is this possible (!)
I downloaded MSVC & GCC64, same issue!

# Discussion History
## Gill1000 | 2018-04-08T02:02:25+00:00
I too face this issue ...your chrome is blocking this...allow him!!!!
your chrome thinks these are might be dangerous files!!

## jodobear | 2018-04-09T12:49:37+00:00
I am using firefox and i can download the zip file like `xmr-stak` for example and run them. When i open `xmrig` zip file i do see the three files: `config, start & xmrig` . BUT, when i try to extract them, nothing happens. So, i tried to manually drag and drop them in a new folder, all files get copied except the `xmrig` application. How can this be explained? 

## Zambi9 | 2018-04-09T15:25:42+00:00
It's possible the file does get copied / extracted, but then quickly gets identified by Windows Defender or your AV and gets deleted. Check your Defender logs. Sometimes its being done silently with no notification to user. I had cases where the executable disappeared seconds after being built, with no notification. I looked up the logs, it's there.

## Zambi9 | 2018-04-09T15:40:11+00:00
By the way it can also change from one day to another - previously I had only the 32bit file get hit by windows defender, now it's also the 64bit.

## jodobear | 2018-04-10T21:15:35+00:00
Ok! So I did find it in my Defender's log by the name of `Coinminer!bit` with `Severe` tagged to it. One question before i actually do try to white list it (which i don't know yet) is why is `xmrig` detected as threat and not `xmr-stak`?

Thanks @Zambi9

## xmrig | 2018-04-10T23:05:59+00:00
Windows Defender is very funny, some long time ago block xmrig-proxy only for word Monero in file description. It can stop blocking file after few days or start and... stop again. Also it was detect xmrig and xmr-stak with same name including letters after `!`. So is today xmr-stak not detected it not meant anything it can start detected tomorrow or not. Personally I add folder where I build miner to exclusion list after Windows Defender start remove freshly complied exe, after release with minor changes was published on github.

Anyway av description `Coinminer` is pretty good for coin miner.
Thank you.

# Action History
- Created by: jodobear | 2018-04-07T23:51:14+00:00
- Closed at: 2018-11-05T13:21:57+00:00
