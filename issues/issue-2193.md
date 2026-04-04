---
title: monerod.exe/Windows GUI sync very slow, almost no CPU usage
source_url: https://github.com/monero-project/monero-gui/issues/2193
author: lunaoe
assignees: []
labels: []
created_at: '2019-06-03T17:19:30+00:00'
updated_at: '2019-06-29T19:58:49+00:00'
type: issue
status: closed
closed_at: '2019-06-29T19:58:49+00:00'
---

# Original Description
I'm using the latest version of monero gui for Windows, the sync is terribly slow just for 10 days behind, the cpu and hard drive usage are like 3%, it's always been like that, but I open an issue just in case something's wrong. 
CPU is Ryzen 1600X
SSD is 860 EVO
Internet is 300Mbps

# Discussion History
## moneromooo-monero | 2019-06-03T17:43:03+00:00
Run "sync-info" in monerod (if it was started by the GUI, you'll have to stop it and start manually).
Do this after it's been running for a minute, so it has the time to connect to peers first.
Also add "--log-level 1" to monerod, and paste the logs to paste.debian.net or similar.

## lunaoe | 2019-06-03T17:47:19+00:00
I have found some kind of solution
I made a shortcut to monerod.exe and added "--max-concurrency 12" as an option and now CPU averages 70% and SSD 40% usage wich is much better. The thing is, I can't put the "max-concurrency" option in the GUI (Settings->Node->Startup flags), when I try that, the daemon window flashes and dissapears, but I could read the first line: 
"Failed to parse arguments: option 'max-concurrency' cannot be specified more than once"
But then the shortcut I made only boosts the initial check, then it's again very slow, consuming 4% CPU, and 0% SSD usage, only downloading like 6Mbps.

## moneromooo-monero | 2019-06-03T17:51:05+00:00
I do remember some talk about the GUI setting things to be "lightweight" to not bring the computer to its knees. I don't know whether that got done though, but it looks like it did :)

What do you mean by "initial check" ?

## selsta | 2019-06-03T17:52:56+00:00
GUI uses half of the available cores.

> "Failed to parse arguments: option 'max-concurrency' cannot be specified more than once"

This will be fixed in the next version.

## lunaoe | 2019-06-03T17:59:55+00:00
```
2019-06-03 17:50:40.983 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182    [82.17.53.156:18080 OUT]  Synced 1842288/1849007
2019-06-03 17:56:59.993 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182    [188.165.192.153:18080 OUT]  Synced 1842317/1849012
2019-06-03 18:01:17.307 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182    [212.129.34.205:18080 OUT]  Synced 1842347/1849015
```
Is it normal, 6 minutes for a few blocks? Is there any bandwith limit I can override? It's very difficult to use when it takes more than an hour to sync just 10 days. 

## moneromooo-monero | 2019-06-03T18:02:18+00:00
It does not seem right. But these logs also don't seem right, they're missing stuff. Can you do this:
set_log 2
Then wait 10 minutes, then:
set_log 0
Then paste the resulting log to paste.debian.net. It'll be a fair amount of logs, if it's too big you could also push it to a github repo.

## lunaoe | 2019-06-03T18:42:40+00:00
Some screenshots

![2019-06-03](https://user-images.githubusercontent.com/45894616/58825989-e7b57000-863f-11e9-812e-5303928eae28.png)
![2019-06-03 (1)](https://user-images.githubusercontent.com/45894616/58826006-f439c880-863f-11e9-86cd-68dacb95506e.png)
![2019-06-03 (2)](https://user-images.githubusercontent.com/45894616/58825956-d1a7af80-863f-11e9-81f3-d203113af9a1.png)
![2019-06-03 (4)](https://user-images.githubusercontent.com/45894616/58825982-e5531600-863f-11e9-86ee-3bf7c6cb7b8d.png)



## dEBRUYNE-1 | 2019-06-03T19:13:32+00:00
@lunaoe - Which wallet mode did you select by the way?

## moneromooo-monero | 2019-06-03T19:29:47+00:00
The "Got block with unknown parent"... messages are a bug which got fixed a while back IIRC. You're using 0.14.0.2, right ?

## lunaoe | 2019-06-03T19:32:07+00:00
wallet mode:
I don't know about the wallet, I created one with the GUI with a password in 2018.

version:
Monero 'Boron Butterfly' (v0.14.0.2-release)

## moneromooo-monero | 2019-06-04T00:27:03+00:00
OK, so the sync bug should get fixed whenever you switch to 0.14.1.0, which should be released... soon.

## lunaoe | 2019-06-05T16:35:56+00:00
I redownloaded the blockchain again in an empty directory and it went well, but around 80-90% the sync is terribly slow, now its 98% (49 days behind) and seems almost stagnated

## lunaoe | 2019-06-29T19:58:49+00:00
![2019-06-29 (2)](https://user-images.githubusercontent.com/45894616/60388911-d6ce1200-9ab8-11e9-99a9-18ab33266e80.png)
v0.14.1.0 fixed the problem 👍 

# Action History
- Created by: lunaoe | 2019-06-03T17:19:30+00:00
- Closed at: 2019-06-29T19:58:49+00:00
