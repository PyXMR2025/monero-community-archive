---
title: bg-mining-miner-target still can't get reached
source_url: https://github.com/monero-project/monero/issues/8986
author: daemonserj
assignees: []
labels:
- bug
- pending review
created_at: '2023-09-09T11:19:29+00:00'
updated_at: '2023-12-07T20:20:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am trying to configure background mining but get strange results with various threads+target combinations.
My system a bit out of date: Windows 7 64 bit, Ryzen 7 5700x 8C/16T, I know that CPU is not officially supported but all other progs&games runs pretty fine.
Node is Monero 'Fluorine Fermi' (v0.18.2.2-release) pruned and fully synced.

So, with this params:

```
mining-threads=10
bg-mining-enable=1
bg-mining-ignore-battery=1
bg-mining-miner-target=100
# for fast bg-mining start
bg-mining-min-idle-interval=10
bg-mining-idle-threshold=10
```

I get only 5-6% CPU used by monerod and 95% overall idle.
If I set 32 threads (too much for 16T CPU) and target is still 100% I get 10-13% monerod usage.



# Discussion History
## moneromooo-monero | 2023-09-09T12:50:30+00:00
If you run with --log-level 0,miner:DEBUG, do the idle percentage reported agree with your 5-6% and 10-13% (are those from top or similar ?) ?

## daemonserj | 2023-09-09T14:21:44+00:00
```
2023-09-09 14:17:54.098	[P2P9]	INFO	miner	src/cryptonote_basic/miner.cpp:410	Mining has started with 10 threads, good luck!
2023-09-09 14:17:54.098	[P2P9]	WARNING	miner	src/cryptonote_basic/miner.cpp:415	Background mining controller thread started
2023-09-09 14:17:54.099	[P2P9]	INFO	miner	src/cryptonote_basic/miner.cpp:420	Ignoring battery
2023-09-09 14:18:04.360	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:802	idle percentage is 87
2023-09-09 14:18:04.360	5460	INFO	miner	src/cryptonote_basic/miner.cpp:805	cpu is 87% idle, idle threshold is 10%, ac power : 1, background mining started, good luck!
2023-09-09 14:18:15.609	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 98%, miner percentage is 1%, ac power : 1
2023-09-09 14:18:15.609	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 301
2023-09-09 14:18:25.860	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 99%, miner percentage is 1%, ac power : 1
2023-09-09 14:18:25.860	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 202
2023-09-09 14:18:36.362	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 99%, miner percentage is 1%, ac power : 1
2023-09-09 14:18:36.362	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 103
2023-09-09 14:18:46.612	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 98%, miner percentage is 2%, ac power : 1
2023-09-09 14:18:46.613	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 5
2023-09-09 14:18:56.866	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 94%, miner percentage is 6%, ac power : 1
2023-09-09 14:18:56.866	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 5
2023-09-09 14:19:07.359	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 95%, miner percentage is 6%, ac power : 1
2023-09-09 14:19:07.359	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 5
2023-09-09 14:19:17.610	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 95%, miner percentage is 6%, ac power : 1
2023-09-09 14:19:17.610	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 5
2023-09-09 14:19:27.863	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 95%, miner percentage is 5%, ac power : 1
2023-09-09 14:19:27.863	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 5
2023-09-09 14:19:38.360	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 95%, miner percentage is 5%, ac power : 1
2023-09-09 14:19:38.360	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 5
2023-09-09 14:19:48.610	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:761	idle percentage is 94%, miner percentage is 6%, ac power : 1
2023-09-09 14:19:48.610	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:782	m_miner_extra_sleep 5
2023-09-09 14:19:49.160	5460	DEBUG	miner	src/cryptonote_basic/miner.cpp:722	background miner thread interrupted 
2023-09-09 14:19:49.161	7964	INFO	miner	src/cryptonote_basic/miner.cpp:469	Mining has been stopped, 10 finished

```

# Action History
- Created by: daemonserj | 2023-09-09T11:19:29+00:00
