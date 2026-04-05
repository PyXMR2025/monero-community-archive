---
title: 'VIRUS in assets '
source_url: https://github.com/xmrig/xmrig/issues/1813
author: ZeroX66
assignees: []
labels:
- av
created_at: '2020-08-21T07:03:04+00:00'
updated_at: '2020-08-28T16:28:50+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:28:50+00:00'
---

# Original Description
All assets are infected. Can we remove them and update with real stuff?

# Discussion History
## SChernykh | 2020-08-21T21:28:54+00:00
It isn't a virus, it is a false positive. Virus scanners mark the miners as viruses because people have sneakily installed them on other peoples computers without their knowledge, hijacking it to mine for them.

## xmrig | 2020-08-22T02:04:36+00:00
Maybe it some kind of joke, most of antiviruses clearly say it's very dangerous thing with name `*Miner*`.

## ZeroX66 | 2020-08-22T11:43:52+00:00
Yeah, maybe but send it up to VirusTotal. Can be false positive , but how we know?

## xmrig | 2020-08-22T11:54:18+00:00
Compile the source code, upload the result to VirusTotal and you are now a virus maker.

## Lonnegan | 2020-08-22T12:03:44+00:00
VirusTotal says, it's a CoinMiner. So nothing we didn't know before, right?

## SChernykh | 2020-08-22T13:05:28+00:00
AV companies have very perverted definition of what they call a "virus". This is a long story really. XMRig doesn't do anything virus-like at all, it's just a tool for mining.

## ariadarkkkis | 2020-08-22T19:17:10+00:00
The good thing about this miner is that it's open-source. You can check the files and codes and everything and even compile it yourself if you don't trust the compiled version. Most AVs detect miners as dangerous because of what @SChernykh said. Just make sure you either download the latest release from xmrig github or clone the repo and compile it yourself. Because its open-source, so many 3rd party compilations of this miner doesnt even mine for you ( but you think they are ) and maybe they contain some RATs or Backdoors or etc.


# Action History
- Created by: ZeroX66 | 2020-08-21T07:03:04+00:00
- Closed at: 2020-08-28T16:28:50+00:00
