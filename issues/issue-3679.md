---
title: 'Xmrig should be able to mine from local daemon and not spit out receive job
  error: "Invalid block template received from daemon."'
source_url: https://github.com/xmrig/xmrig/issues/3679
author: miltoncarpenter665
assignees: []
labels:
- question
created_at: '2025-06-22T16:01:25+00:00'
updated_at: '2025-06-28T10:24:05+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:24:05+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
./Xmas -o myrqmanodeipaddress:19994 -u ar3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -a rx/arq -t 1 --daemon

**Expected behavior**
Xmrig should be able to mine from local daemon and not spit out receive job error: "Invalid block template received from daemon."

**Required data**
 - XMRig version
XMRig 6.23.0
 built on Jun 16 2025 with GCC 13.2.1
 features: 64-bit AES

libuv/1.51.0
OpenSSL/3.0.16
hwloc/2.12.1


**Additional context**
In addition to this https://github.com/xmrig/xmrig/issues/3627 , --rpc-login is disabled on my daemon, but still i receive job error: "Invalid block template received from daemon."


When I mine from a mining pool it works:

root@f2f1380dc555:~# ./Xmas --donate-level 1 -o fastxyz.xxxxxxxxxxxxx.uk:6360 -u solo:ar3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@Test -p x -a rx/arq -k -t 1
 * ABOUT        XMRig/6.23.0 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          DO-Regular (1) 64-bit AES VM
                L2:16.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.6/7.8 GB (8%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      fastxyz.xxxxxxxxxxxxxxxx.uk:6360 algo rx/arq
 * COMMANDS     hashrate, pause, resume, results, connection
[2025-06-22 17:56:14.408]  net      use pool fastxyz.xxxxxxxxx.uk:6360  127.0.0.1
[2025-06-22 17:56:14.408]  net      new job from fastxyz.xxxxxxxxxxx.uk:6360 diff 15000 algo rx/arq height 1739384 (1 tx)
[2025-06-22 17:56:14.408]  cpu      use argon2 implementation AVX2
[2025-06-22 17:56:14.412]  msr      msr kernel module is not available
[2025-06-22 17:56:14.412]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2025-06-22 17:56:14.412]  randomx  init dataset algo rx/arq (4 threads) seed 853629da2c5afcd0...
[2025-06-22 17:56:14.413]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2025-06-22 17:56:27.510]  randomx  dataset ready (13097 ms)
[2025-06-22 17:56:27.510]  cpu      use profile  rx/wow  (4 threads) scratchpad 256 KB
[2025-06-22 17:56:27.515]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 1024 KB (5 ms)
[2025-06-22 17:56:44.568]  cpu      accepted (1/0) diff 15000 (50 ms)
[2025-06-22 17:56:46.322]  cpu      accepted (2/0) diff 15000 (45 ms)
[2025-06-22 17:56:51.947]  net      new job from fastxyz.xxxxxxxxxxx.uk:6360 diff 30000 algo rx/arq height 1739384 (1 tx)
[2025-06-22 17:57:00.335]  cpu      accepted (3/0) diff 30000 (45 ms)
[2025-06-22 17:57:11.660]  cpu      accepted (4/0) diff 30000 (58 ms)



What can be done in order to allow Xmrig to be able to solo mine from the node?


Note: I'm not blaming Xmrig, rather, I'd like to be assisted mining Solo on my node.

Even when expanding this further by trying to use Mining Core from https://github.com/Kudaraidee/miningcore


I'm trying to mine Arqma, I'm using this config: https://github.com/Kudaraidee/miningcore/blob/dev/examples/arqma_pool.json

{
	"logging": 
	{
		"level": "info",
		"enableConsoleLog": true,
		"enableConsoleColors": true,
		"logFile": "",
		"apiLogFile": "",
		"logBaseDirectory": "",
		"perPoolLogFile": false
	},
	"banning": 
	{
		"manager": "Integrated",
		"banOnJunkReceive": true,
		"banOnInvalidShares": false
	},
	"notifications": 
	{
		"enabled": false,
		"email": 
		{
			"host": "smtp.example.com",
			"port": 587,
			"user": "user",
			"password": "password",
			"fromAddress": "info@yourpool.org",
			"fromName": "support"
		},
		"admin": 
		{
			"enabled": false,
			"emailAddress": "user@example.com",
			"notifyBlockFound": true
		}
	},
	"persistence": 
	{
		"postgres": 
		{
			"host": "127.0.0.1",
			"port": 5432,
			"user": "miningcore",
			"password": "password",
			"database": "miningcore"
		}
	},
	"paymentProcessing": 
	{
		"enabled": true,
		"interval": 600,
		"shareRecoveryFile": "recovered-shares.txt"
	},
	"api": 
	{
		"enabled": true,
		"listenAddress": "*",
		"port": 4000,
		"metricsIpWhitelist": [],
		"rateLimiting": 
		{
			"disabled": true,
			"rules": 
			[
				{
					"Endpoint": "*",
					"Period": "1s",
					"Limit": 5
				}
			],
			"ipWhitelist": 
			[
				""
			]
		}
	},
	"pools": 
	[
		{
			"id": "arqma",
			"enabled": true,
			"coin": "arqma",
			"randomXRealm": "arqma",
			"address": "ar2dDEehonEYXkJkXyZGNxAZhU8vFKmrtPKgebmKDpMvYz8YPjiRztfR5WMWpH8u6MCqsVpqnJ5bh5VVgP2Sw1Xh2iWsqC4ro",
			"rewardRecipients": 
			[
				{
					"address": "ar2dDEehonEYXkJkXyZGNxAZhU8vFKmrtPKgebmKDpMvYz8YPjiRztfR5WMWpH8u6MCqsVpqnJ5bh5VVgP2Sw1Xh2iWsqC4ro",
					"percentage": 1
				}
			],
			"blockRefreshInterval": 500,
			"clientConnectionTimeout": 600,
			"banning": 
			{
				"enabled": true,
				"time": 600,
				"invalidPercent": 50,
				"checkThreshold": 50
			},
			"ports": 
			{
				"6360": 
				{
					"listenAddress": "0.0.0.0",
					"difficulty": 50000,
					"name": "CPU Mining",
					"varDiff": 
					{
						"minDiff": 15000,
						"maxDiff": null,
						"targetTime": 15,
						"retargetTime": 90,
						"variancePercent": 30
					}
				}
			},
			"daemons": 
			[
				{
					"host": "127.0.0.1",
					"port": 19994,
					"user": "user",
					"password": "password"
				},
				{
					"host": "127.0.0.1",
					"port": 19995,
					"user": "user",
					"password": "password",
					"category": "wallet"
				}
			],
			"paymentProcessing": 
			{
				"enabled": true,
				"minimumPayment": 0.25,
				"minimumPaymentToPaymentId": 1.0,
				"transferSplit": true,
				"payoutScheme": "PPLNS",
				"payoutSchemeConfig": 
				{
					"factor": 0.5
				}
			}
		}
	]
}


When mining to a Miningcore port i see this:

[2025-06-22 16:23:24.2834] [I] [Core] Version 0.1.0.0-dev [db051abefab00e1017de5bb234eae34ad7d641b4]
[2025-06-22 16:23:24.2997] [I] [Core] Runtime .NET 6.0.36 on Linux 6.1.0-26-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.112-1 (2024-09-30) [X64]
[2025-06-22 16:23:24.3141] [I] [Core] Prometheus Metrics API listening on http://0.0.0.0:4000/metrics
[2025-06-22 16:23:24.3141] [I] [Core] WebSocket Events streaming on ws://0.0.0.0:4000/notifications
[2025-06-22 16:23:26.1416] [I] [XmlKeyManager] User profile is available. Using '/home/pool/.aspnet/DataProtection-Keys' as key repository; keys will not be encrypted at rest.
[2025-06-22 16:23:26.1930] [I] [ShareRecorder] Online
[2025-06-22 16:23:26.2613] [I] [PayoutManager] Online
[2025-06-22 16:23:26.2613] [I] [StatsRecorder] Online
[2025-06-22 16:23:26.6297] [I] [Core] 210 coins loaded from '/home/pool/miningcore/build/coins.json'
[2025-06-22 16:23:26.6619] [I] [arqma] Starting Pool ...
[2025-06-22 16:23:26.6752] [I] [arqma] Starting Job Manager ...
[2025-06-22 16:23:26.7871] [I] [Core] API Access to /api/admin restricted to 127.0.0.1,::1,::ffff:127.0.0.1
[2025-06-22 16:23:26.7904] [I] [Core] API Access to /metrics restricted to 127.0.0.1,::1,::ffff:127.0.0.1
[2025-06-22 16:23:26.7904] [I] [arqma] All daemons online
[2025-06-22 16:23:26.8150] [I] [arqma] All daemons synched with blockchain
[2025-06-22 16:23:26.8638] [I] [arqma] Job Manager Online
[2025-06-22 16:23:26.9455] [I] [Lifetime] Now listening on: http://0.0.0.0:4000
[2025-06-22 16:23:26.9455] [I] [Lifetime] Application started. Press Ctrl+C to shut down.
[2025-06-22 16:23:26.9488] [I] [Lifetime] Hosting environment: Production
[2025-06-22 16:23:26.9488] [I] [Lifetime] Content root path: /home/pool/miningcore/build/
[2025-06-22 16:23:27.4188] [I] [arqma] Detected new block 1739397 [POLL]
[2025-06-22 16:23:27.4188] [I] [arqma] Detected new seed hash 853629da2c5afcd034e629b68949d33ca55cc80ec250d779b635cfb8c9b568e7 starting @ height 1739397
[2025-06-22 16:23:27.4278] [I] [RandomARQ] Creating VM arqma@1 [RANDOMX_FLAG_HARD_AES, RANDOMX_FLAG_JIT, RANDOMX_FLAG_ARGON2], hash 853629da2c5afcd034e629b68949d33ca55cc80ec250d779b635cfb8c9b568e7 ...
[2025-06-22 16:23:27.6612] [I] [RandomARQ] Created VM arqma@1 in 00:00:00.2336538
[2025-06-22 16:23:27.6729] [I] [arqma] Broadcasting jobs
[2025-06-22 16:23:27.7596] [I] [arqma] Pool Online
[2025-06-22 16:23:27.7634] [I] [arqma]

Mining Pool:            arqma
Coin Type:              ARQ [ARQ]
Network Connected:      Main
Detected Reward Type:   POW
Current Block Height:   1739397
Current Connect Peers:  3
Network Difficulty:     685M
Network Hash Rate:      5.44 MH/s
Stratum Port(s):        6360
Pool Fee:               1%

[2025-06-22 16:23:27.7740] [I] [arqma] Stratum ports 0.0.0.0:6360 online
[2025-06-22 16:23:27.8915] [I] [arqma] [0HNDHL4FAUOE9] Accepting connection from ::ffff:127.0.0.1:47634 ...
[2025-06-22 16:23:27.9083] [I] [arqma] [0HNDHL4FAUOE9] Connection from ::ffff:127.0.0.1:47634 accepted on port 6360
[2025-06-22 16:23:28.0166] [I] [arqma] [0HNDHL4FAUOE9] Authorized miner ar3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx5K
[2025-06-22 16:23:28.0577] [I] [arqma] [0HNDHL4FAUOE9] Connection closed


On Xmrig side i see: " login error code: 2"

pool@FreddieFordDeb12:~$ ./Xmas -o 127.0.0.1:6360 -u ar3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx5K -k -a rx/arq -t 1
 * ABOUT        XMRig/6.22.2 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          DO-Regular (1) 64-bit AES VM
                L2:16.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       2.1/7.8 GB (27%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      127.0.0.1:6360 algo rx/arq
 * COMMANDS     hashrate, pause, resume, results, connection
[2025-06-22 16:25:29.782]  net      127.0.0.1:6360 login error code: 2



# Discussion History
## xmrig | 2025-06-22T17:17:07+00:00
Generally, daemon support is limited to Monero or compatible with Monero daemons. There are no plans to extend compatibility right now. The maximum is to document somewhere what exactly is supported.
The ARQ coin might have been supported in the past, but it has changed.

Pools hide all implementation details and provide compatible jobs for miners. Miners do not need to know how a specific coin works under the hood, and I can't provide support for setting up pool software.
Thank you.

# Action History
- Created by: miltoncarpenter665 | 2025-06-22T16:01:25+00:00
- Closed at: 2025-06-28T10:24:05+00:00
