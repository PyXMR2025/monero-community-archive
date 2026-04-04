---
title: Version 0.17.2.1
source_url: https://github.com/monero-project/monero-gui/issues/3421
author: toneloc7
assignees: []
labels: []
created_at: '2021-04-20T20:29:24+00:00'
updated_at: '2021-04-21T05:01:11+00:00'
type: issue
status: closed
closed_at: '2021-04-21T05:01:11+00:00'
---

# Original Description
Hello, I downloaded latest version of GUI today (0.17.2.1) but daemon synchronization is not picking up where it left off. It looks to be starting from scratch with 2 million+ blocks remaining. My prior GUI version was recent and was fully synced today before I downloaded 0.17.2.1. I have Windows 10 and downloaded 0.17.2.1 via Windows 64-bit (Installer)

Does anyone know how to get daemon to pick up where it left off? Any advice is really appreciated, thanks



# Discussion History
## selsta | 2021-04-20T20:30:13+00:00
Did you have a custom blockchain path?

## toneloc7 | 2021-04-20T20:37:05+00:00
> Did you have a custom blockchain path?

not that I am aware of. I just download via Windows 64-bit (Installer)

## selsta | 2021-04-20T20:37:54+00:00
Can you go to Settings -> Log, type "status" and then post the output here.

## toneloc7 | 2021-04-20T20:44:26+00:00
> Can you go to Settings -> Log, type "status" and then post the output here.

thank you selsta:

[4/20/2021 3:02 PM] 2021-04-20 20:02:34.557 I Monero 'Oxygen Orion' (v0.17.2.0-release) 
Height: 73498, target: 73498 (100%) 
Downloading at 0 kB/s 
Next needed pruning seed: 2 
0 peers 
0 spans, 0 MB 
[]
>>> status
>>> status
[4/20/2021 3:42 PM] 2021-04-20 20:39:02.275 I Monero 'Oxygen Orion' (v0.17.2.0-release) 
Error: Problem fetching info-- rpc_request:

## selsta | 2021-04-20T20:45:45+00:00
Can you please go to Settings -> Info and post the output of:

"Wallet mode"

## toneloc7 | 2021-04-20T20:47:46+00:00
> Can you please go to Settings -> Info and post the output of:
> 
> "Wallet mode"

Advanced mode (Local node)

## selsta | 2021-04-20T20:50:00+00:00
Something is really weird. Typing "status" should look like this:

```
>>> status
[20.04.21 22:49] 2021-04-20 20:49:18.896 I Monero 'Oxygen Orion' (v0.17.2.0-release)
Height: 2343702/2343702 (100.0%) on mainnet, not mining, net hash 2.48 GH/s, v14, 12(out)+0(in) connections, uptime 1d 17h 37m 58s
```

Can you try restarting the GUI and also node?

## toneloc7 | 2021-04-21T01:20:23+00:00
> Something is really weird. Typing "status" should look like this:
> 
> ```
> >>> status
> [20.04.21 22:49] 2021-04-20 20:49:18.896 I Monero 'Oxygen Orion' (v0.17.2.0-release)
> Height: 2343702/2343702 (100.0%) on mainnet, not mining, net hash 2.48 GH/s, v14, 12(out)+0(in) connections, uptime 1d 17h 37m 58s
> ```
> 
> Can you try restarting the GUI and also node?

@selsta here is status output after restarting GUI and node:

>>> status
[4/20/2021 8:17 PM] 2021-04-21 01:17:14.688 I Monero 'Oxygen Orion' (v0.17.2.0-release) 
Height: 119412/2343838 (5.1%) on mainnet, not mining, net hash 13.09 MH/s, v1, 12(out)+0(in) connections, uptime 0d 0h 1m 28s

## selsta | 2021-04-21T01:21:47+00:00
Hmm, it's not clear why your chain got lost. We did not get any other reports about this.

## toneloc7 | 2021-04-21T02:09:34+00:00
> Hmm, it's not clear why your chain got lost. We did not get any other reports about this.

thanks @selsta ....I found a "data" file in a different Imdb folder for GUI that is 101 GB....I suspect this is the chain. Do you know if I can adjust current blockchain path?

## selsta | 2021-04-21T02:10:19+00:00
You can change the patch inside Settings -> Node.

## toneloc7 | 2021-04-21T04:51:31+00:00
> You can change the patch inside Settings -> Node.

Got it. That worked. Thanks again @selsta 

# Action History
- Created by: toneloc7 | 2021-04-20T20:29:24+00:00
- Closed at: 2021-04-21T05:01:11+00:00
