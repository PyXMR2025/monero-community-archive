---
title: Excessive CPU and GPU usage on Monero-gui [Win64]
source_url: https://github.com/monero-project/monero-gui/issues/935
author: GreatWhiteMuffloN
assignees: []
labels:
- duplicate
created_at: '2017-10-28T12:26:23+00:00'
updated_at: '2019-04-27T00:54:34+00:00'
type: issue
status: closed
closed_at: '2019-04-27T00:54:34+00:00'
---

# Original Description
As can be seen in the attached picture this is the constant useage of resources when monero-gui is running, it's trying to permanently eat up 1 of 4 cores (haswell) and 30% of GPU0 which is a NVIDIA 970 with 388.00 drivers.

The wallet is not running a daemon but connects to one on the local subnet, mining is not enabled nor has it ever been.

This issue affects me on Windows 10 Fall Update on both monero-gui-0.11.0.0 and monero-gui-0.11.1.0

This is my first bugreport on github if anyone requires more information just ask, I apologize for any breach of etiquette I may have committed.

![monerogui](https://user-images.githubusercontent.com/33177721/32134345-e9c05362-bbeb-11e7-8a61-ac60fe0e9ffc.PNG)



# Discussion History
## bootsmann | 2017-11-28T15:39:50+00:00
Me too.
GUI-Version v0.11.1.0  (monero-gui-win-x64-v0.11.1.0.zip)
Win 8.1 x64
`Height: 1399583/1452973 (96.3%) on mainnet, not mining, net hash 261.24 MH/s, v5, up to date, 8(out)+0(in) connections, uptime 0d 0h 0m 12s`
I am using remote daemon `node.moneroworld.com:18089`
![monero_high_cpu](https://user-images.githubusercontent.com/5744853/33328692-e8f7adc2-d45a-11e7-9346-7720ea3ab5e9.png)



## dEBRUYNE-1 | 2017-11-28T16:11:25+00:00
@bootsmann That's expected. It's your local daemon doing the initial sync. 

## 0dp | 2017-11-30T18:00:00+00:00
@dEBRUYNE-1 initial sync has completed long time ago. Can confirm that the daemon is consuming in the excess of 60%

macOS 10.13.1 (17B1003)

## medusadigital | 2017-12-01T15:13:22+00:00
guys, regarding high daemon usage, if you think there is an issue, please open Issue here: https://github.com/monero-project/monero/issues

This Ticket is about high CPU/GPU usage of **monero-wallet-gui** for now.

having similar issues on Windows: 

![cpuusage](https://user-images.githubusercontent.com/17108301/33488744-f186cc9e-d6b1-11e7-9d38-a7f7c16d6b1b.png)

monero-wallet-gui.exe constantly using 50%.

Using quick2D renderer, CPU intel core 2 duo e8400, integrated gpu.

I remember similar issue last release, for which we sucesfully tested and deployed a fix. --> https://github.com/monero-project/monero-gui/issues/757


maybe there is some Issue with the fix ?









## medusadigital | 2017-12-01T15:22:16+00:00
@Jaqueeee u remember what PR that was ?

## scheerer | 2017-12-08T00:17:20+00:00
Just chiming in: I am also seeing this high CPU/GPU usage on the GUI when the daemon is off (connected to remote) after the network is fully sync'ed.

## ghost | 2018-04-18T02:01:37+00:00
Somebody secretly mining in wallet background? Very suspicious...

## selsta | 2019-04-27T00:41:17+00:00
Let’s continue this in #2013.

+duplicate

# Action History
- Created by: GreatWhiteMuffloN | 2017-10-28T12:26:23+00:00
- Closed at: 2019-04-27T00:54:34+00:00
