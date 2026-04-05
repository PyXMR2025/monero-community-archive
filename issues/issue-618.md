---
title: Algo balancing
source_url: https://github.com/xmrig/xmrig/issues/618
author: MoneroOcean
assignees: []
labels:
- enhancement
created_at: '2018-05-08T10:49:57+00:00'
updated_at: '2019-12-21T20:10:45+00:00'
type: issue
status: closed
closed_at: '2019-12-21T20:10:45+00:00'
---

# Original Description
To be able to do algo load balancing from pool side I suggest the following changes to xmrig* miners and xmrig-proxy:

1. Miner sends list of expected algorithm hashrates in `algo-perf` parameter ("cn", "cn-lite", "cn-heavy", "cn-fast" algo names can be used):

```
{
  "id": 1, "jsonrpc": "2.0", "method": "login",
  "params": {
    "login": "...", "pass": "...", "agent": "...",
    "algo": ["cn", "cn/0", "cn/1", "cn/xtl", "cn-heavy", "cn-light/1" ],
    "algo-perf": {"cn": 600.0, "cn-heavy": 400.0 }
  }
}
```

2. Miner config can include extended `threads` section that describes thread setup for "cn", "cn-lite", "cn-heavy" algo names:

```
"threads": {
	"cn": [
		{"low_power_mode": true,  "affine_to_cpu": 0 },
	        {"low_power_mode": false, "affine_to_cpu": 1 },
	        {"low_power_mode": 1,     "affine_to_cpu": 2 },
	        {"low_power_mode": 3,     "affine_to_cpu": false }
	],
	"cn-lite": [
		{"low_power_mode": true,  "affine_to_cpu": 0 },
	        {"low_power_mode": false, "affine_to_cpu": 1 },
	        {"low_power_mode": 1,     "affine_to_cpu": 2 },
	        {"low_power_mode": 3,     "affine_to_cpu": false }
	],
	"cn-heavy": [
		{"low_power_mode": true,  "affine_to_cpu": 0 },
	        {"low_power_mode": false, "affine_to_cpu": 1 },
	        {"low_power_mode": 1,     "affine_to_cpu": 2 },
	        {"low_power_mode": 3,     "affine_to_cpu": false }
	]
}
```

3. Miner config includes optional extra `algo-perf` section that describes expected hashrates for each algorithm ("cn", "cn-lite", "cn-heavy", "cn-fast" algo names can be used). By default, this section is included in config with estimated generic values (absolute values do not matter, only their relation to each other):

```
"algo-perf": {
	"cn": 1000.0,
	"cn-fast": 2000.0,
	"cn-lite": 2000.0,
	"cn-heavy": 700.0
}
```

4. If algo-perf config section is null (or its cn value is 0) then miner will launch automatic algo benchmarking that can be enforced each launch by "calibrate-algo" option. Additional "calibrate-algo-time" option can specify time in seconds of each algo benchmark round.

5. Xmrig-proxy should report common subset of `algo` from its miners (if not yet done) and cumulative `algo-perf` values for this common subset.

# Discussion History
## MoneroOcean | 2018-05-09T19:55:22+00:00
One addition to item number 5. Since proxy miner set can change over time there should be a way to inform pool about changed of `algo` common subset and `algo-perf` without reconnection. The most natural way to do that is via `getjob` request that proxy can send with extra params (like in the login request):

```
  "params": {
    "algo": ["cn", "cn/0", "cn/1", "cn/xtl"],
    "algo-perf": {"cn": 600.0, "cn-fast": 598.0, "cn-heavy": 400.0 }
  }
```

## bobbieltd | 2018-05-09T21:08:42+00:00
+1

## 2010phenix | 2018-05-11T11:13:42+00:00
@MoneroOcean maybe not build new bicycle, xmrig is good project, have own proxy, used by all other pool... 
add xmrig bool
add few byte like nicehash
and simple use over true\false for compatibility
@Snipa22 and other just add few line code to his pool

## MoneroOcean | 2018-05-11T15:31:02+00:00
Sorry, what? Providing expected algo hashrate (the main idea of this proposal) is the most natural way to be implemented in the miner since it has access to precise 1 diff measurements. Also it can conveniently store expected hashrates and provide to pool immediately during login sequence (pool does not have 100% reliable way to understand if it is already known miner to apply some kind of hashrate profile to it).

## aka-lex | 2018-07-20T07:44:03+00:00
Concerning paragraph 4
In the Originally based on cpuminer-multi there was such an option --benchmark.

Concerning paragraph 3
"algo-perf" should contain the values of all possible options for algo/pow.
Miner can fill these values automatically in benchmark mode.
For benchmark, the miner can issue tasks to himself, not even a pool is needed.

With respect to paragraph 2
Miner in the option --algo, except for possible options, should support the value of "-1" or "auto."

Also, in the current situation, the --algo option is more logical to transfer from the group of general configuration settings, to the settings of a particular pool.

# Action History
- Created by: MoneroOcean | 2018-05-08T10:49:57+00:00
- Closed at: 2019-12-21T20:10:45+00:00
