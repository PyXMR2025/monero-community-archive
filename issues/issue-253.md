---
title: Retry count not being honored
source_url: https://github.com/xmrig/xmrig/issues/253
author: txtilde
assignees: []
labels:
- wontfix
created_at: '2017-12-10T21:14:53+00:00'
updated_at: '2018-03-14T23:35:15+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:35:15+00:00'
---

# Original Description
The --retries flag doesn't seem to be working properly.  Notably, ccminer allows one to specify 0 retry attempts.  In the below example, I'm attempting to have it try once, but it doesn't seem to give up.

Example:
```
/opt/miners/xmrig-nvidia/build/xmrig-nvidia --retries 1 --retry-pause 2 -a cryptonight -k --donate-level 1 -o us-east.cryptonight-hub.miningpoolhub.com:12024 -u XXXX -p XXXX 
 * VERSIONS:     XMRig/2.4.2 libuv/1.8.0 CUDA/8.0 gcc/5.4.0
 * CPU:          Intel(R) Celeron(R) CPU G3930 @ 2.90GHz x64 AES-NI
 * GPU #0:       GeForce GTX 1070 @ 1835/4004 MHz 64x45 10x0 arch:61 SMX:15
 * GPU #1:       GeForce GTX 1070 @ 1835/4004 MHz 64x45 10x0 arch:61 SMX:15
 * GPU #2:       GeForce GTX 1070 @ 1835/4004 MHz 64x45 10x0 arch:61 SMX:15
 * GPU #3:       GeForce GTX 1070 @ 1835/4004 MHz 64x45 10x0 arch:61 SMX:15
 * ALGO:         cryptonight, donate=1%
 * POOL #1:      us-east.cryptonight-hub.miningpoolhub.com:12024
 * COMMANDS:     hashrate, health, pause, resume
[2017-12-10 16:08:57] [us-east.cryptonight-hub.miningpoolhub.com:12024] error: "invalid username used for login", code: -1
[2017-12-10 16:09:00] [us-east.cryptonight-hub.miningpoolhub.com:12024] error: "invalid username used for login", code: -1
[2017-12-10 16:09:05] [us-east.cryptonight-hub.miningpoolhub.com:12024] error: "invalid username used for login", code: -1
[2017-12-10 16:09:08] [us-east.cryptonight-hub.miningpoolhub.com:12024] error: "invalid username used for login", code: -1
[2017-12-10 16:09:11] [us-east.cryptonight-hub.miningpoolhub.com:12024] error: "invalid username used for login", code: -1
[2017-12-10 16:09:13] Ctrl+C received, exiting
```

Same pool with ccminer:

```
/opt/miners/ccminer/ccminer -r 0 -a cryptonight -o stratum+tcp://us-east.cryptonight-hub.miningpoolhub.com:12024 -u txtilde.ccminer -p min3d 
*** ccminer 2.2.3 for nVidia GPUs by tpruvot@github ***
    Built with the nVidia CUDA Toolkit 8.0 64-bits

  Originally based on Christian Buchner and Christian H. project
  Include some kernels from alexis78, djm34, djEzo, tsiv and krnlx.

BTC donation address: 1AJdfCpLWPNoAMDfHF1wD5y8VgKSSTHxPo (tpruvot)

[2017-12-10 16:12:14] Using JSON-RPC 2.0
[2017-12-10 16:12:14] Starting on stratum+tcp://us-east.cryptonight-hub.miningpoolhub.com:12024
[2017-12-10 16:12:14] 4 miner threads started, using 'cryptonight' algorithm.
[2017-12-10 16:12:14] Stratum authentication failed
[2017-12-10 16:12:14] invalid username used for login
[2017-12-10 16:12:14] ...terminating workio thread
```
ccminer program exits properly...

# Discussion History
## xmrig | 2017-12-11T10:16:18+00:00
This option only usefull if you specify one or more backup pools. Miner always try recovery connection. Can you give example when exit is useful?
Thank you.

## txtilde | 2017-12-15T14:18:42+00:00
This option is used for ccminer when you are connected to pools that allow auto-switching between algorithms.  The upstream server sends down an authentication failure, and the next line in your batch file is another instance of ccminer w/ a different algorithm.  Example:

> :start
EthDcrMiner64.exe -epool us-east.ethash-hub.miningpoolhub.com:12020 -ewal username.workername -eworker username.workername -esm 3 -epsw x -allcoins 1 -retrydelay -1
#ethminer --farm-retries 0 -G -S us-east.ethash-hub.miningpoolhub.com:12020 -O username.workername:x -FS exit
ccminer -r 0 -a groestl -o stratum+tcp://hub.miningpoolhub.com:12004 -u username.workername -p x
ccminer -r 0 -a myr-gr -o stratum+tcp://hub.miningpoolhub.com:12005 -u username.workername -p x
ccminer -r 0 -a x11 -o stratum+tcp://hub.miningpoolhub.com:12007 -u username.workername -p x
ccminer -r 0 -a x13 -o stratum+tcp://hub.miningpoolhub.com:12008 -u username.workername -p x
ccminer -r 0 -a x15 -o stratum+tcp://hub.miningpoolhub.com:12009 -u username.workername -p x
ccminer -r 0 -a neoscrypt -o stratum+tcp://hub.miningpoolhub.com:12012 -u username.workername -p x
ccminer -r 0 -a qubit -o stratum+tcp://hub.miningpoolhub.com:12014 -u username.workername -p x
ccminer -r 0 -a quark -o stratum+tcp://hub.miningpoolhub.com:12015 -u username.workername -p x
ccminer -r 0 -a skein -o stratum+tcp://hub.miningpoolhub.com:12016 -u username.workername -p x
ccminer -r 0 -a lyra2v2 -o stratum+tcp://hub.miningpoolhub.com:12018 -u username.workername -p x
ccminer -r 0 -a vanilla -o stratum+tcp://hub.miningpoolhub.com:12019 -u username.workername -p x
timeout 1
goto start

## txtilde | 2017-12-18T18:18:18+00:00
Is this example sufficient to answer your question?

## konqueror1 | 2017-12-20T14:12:53+00:00
I am looking for the same. May be it will not be too hard to make the app to exit if "--retries" is set to "0" and pool disconnects?

# Action History
- Created by: txtilde | 2017-12-10T21:14:53+00:00
- Closed at: 2018-03-14T23:35:15+00:00
