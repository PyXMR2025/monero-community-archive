---
title: miner stops after maximum 1 hour for all versions newer than 6.10.0
source_url: https://github.com/xmrig/xmrig/issues/2573
author: Macacul
assignees: []
labels: []
created_at: '2021-09-05T16:53:28+00:00'
updated_at: '2021-10-10T23:12:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, I have this issues on both of my systems:
-newest version including 6.15.0 ( actually all version > 6.10.0) stops running after approx 1 hour.;
-with newest version including 6.15.0 ( actually all version > 6.10.0), the hash rate drop with 2-3 MH/s compared with 6.10.0 where the drop is between 0.5 - 0.7 MH/s. Sometimes the drop is bigger.
i have in config file this : --cpu-priority 0

my systems:
1-5950x, 32 GB 4000 but work at 3766, tomahawk x570 wireless, rx 6900xt;
2-3950x, 32 GB 3600, msi mpg x570 gaming edge wireless, rtx 3090. 

Any idea?

I use:
win 10 pro.
this is my cmd:
mrig.exe -o xmr-eu1.nanopool.org:14433 -u wallet.worker/mail --tls --coin monero --cpu-priority 0

without cpu priority 0 the hash drops severly om gpu

So same behavior with 6.15.1. after one reboot i found this error:
![image](https://user-images.githubusercontent.com/87904537/135071715-d2af4a25-9c93-420e-b69d-1fdb9315d711.png)


# Discussion History
## DeeDeeRanged | 2021-09-27T11:47:04+00:00
Windows / Linux ? Have you tried without --cpu-priority 0 ? Take it you use command line only, then pls. show the full command line used (without your wallet). Otherwise it is a guessing game.

## Spudz76 | 2021-09-27T13:09:12+00:00
Win10?  Try the tweaks [from here ](https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/) especially the memory bandwidth destroying Compression/Diagnostic tasks (advanced section 3 and 4) which will run whenever it likes randomly.

## Macacul | 2021-09-27T13:17:34+00:00
win 10 pro.
this is my cmd:
mrig.exe -o xmr-eu1.nanopool.org:14433 -u wallet.worker/mail --tls --coin monero --cpu-priority 0

without cpu priority 0 the hash drops severly om gpu

## DeeDeeRanged | 2021-09-28T18:13:32+00:00
You are mining monero on CPU and GPU? If you want to utilise GPU for monero better use another miner like gminer or phoenixminer and mine on https://moneroocean.stream/ as they payout in monero. For Phoenixminer it would be phoenixminer.exe -coin eth -proto 4 -pool stratum+tcp://gulf.moneroocean.stream:11024 -wal your_monero_wallet -pass rig_id~ethash You have to fine tune the settings but it will yeald you a much greater income and all paidout in monero. I only use xmrig with my CPU's for mining monero directly and use phoenixminer or gminer on moneroocean.stream to mine ethash.

## Macacul | 2021-09-28T18:25:11+00:00
i mine monero only on cpu. gpu is for eth

## DeeDeeRanged | 2021-10-10T08:53:49+00:00
What command and miner do you use for the gpu as xmrig cannot mine eth.

## Macacul | 2021-10-10T09:01:05+00:00
t-rex :
t-rex.exe -a ethash -o stratum+tcp://eu1.ethermine.org:4444 -u wallet -p x -w worker pause

and 
teamredminer:
teamredminer.exe -a ethash -o stratum+tcp://eu1.ethermine.org:4444 -u wallet.worker -p x --enable_compute


## Spudz76 | 2021-10-10T23:12:29+00:00
I use lolMiner for autolykos2 on AMD stuff works pretty well, and on smaller VRAM that can't ethash, and back to Maxwell cards with t-rex

# Action History
- Created by: Macacul | 2021-09-05T16:53:28+00:00
