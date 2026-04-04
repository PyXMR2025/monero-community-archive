---
title: No warning for start_mining when already mining
source_url: https://github.com/monero-project/monero/issues/2987
author: quantumproducer
assignees: []
labels:
- enhancement
created_at: '2017-12-22T06:57:48+00:00'
updated_at: '2018-10-02T13:35:50+00:00'
type: issue
status: closed
closed_at: '2018-10-01T11:56:57+00:00'
---

# Original Description
Minor issue, but this made me think my mining wasn't running. 
I run start_mining <addr> then checked later. Typed start_mining because I wasn't sure if it was still mining. The response it gave I inferred to not be mining already

```
[
l:1521	SYNCHRONIZED OK
start_mining 49CNVYT2NEriMGzaBAvPxg7jR8Tr82V2TXz4e9ufbNhJFmVAb7W2zuGHSdeH7uLz5gJ1Eigncyz8u27WyhQ369SfNGsnYks
2017-12-22 06:56:20.408	  0x70000a4fc000	WARN 	miner	src/cryptonote_basic/miner.cpp:305	Mining has started with 1 threads, good luck!
2017-12-22 06:56:20.408	[miner 0]	INFO 	global	src/cryptonote_basic/miner.cpp:416	Miner thread was started [0]
start_mining
Please specify a wallet address to mine for: start_mining <addr> [<threads>]
start_mining 49CNVYT2NEriMGzaBAvPxg7jR8Tr82V2TXz4e9ufbNhJFmVAb7W2zuGHSdeH7uLz5gJ1Eigncyz8u27WyhQ369SfNGsnYks
2017-12-22 06:56:24.906	  0x70000a4fc000	ERROR	miner	src/cryptonote_basic/miner.cpp:282	Starting miner but it's already started
2017-12-22 06:56:24.906	  0x70000a4fc000	WARN 	daemon.rpc	src/rpc/core_rpc_server.cpp:705	Failed, mining not started
Error: Mining did not start -- Failed, mining not started](url)
```

# Discussion History
## Timo614 | 2017-12-27T16:52:51+00:00
Took a quick look, it does mention why it failed above: "Starting miner but it's already started"

We could add another condition [here](https://github.com/monero-project/monero/blob/master/src/rpc/core_rpc_server.cpp#L763) like

````c++
if(m_core.get_miner().is_mining()) {
  rest.status = "Failed, mining has already started";
  LOG_PRINT_L0(res.status);
  return true;
}
...
````

But any of the other errors the miner may have like threads already started etc would then fall back to the original error. 

We could also pass in some error message string and populate its contents to then display after failure but since it's already in the log it feels like overkill. Perhaps a generic, "Failed" message in place would work here? Would then cause people to look up at the previous errors and see it failed since it was already running (versus assuming it broke in some way due to the messaging about it failing to start which implies it isn't currently running?).

## dEBRUYNE-1 | 2018-01-08T12:46:46+00:00
+enhancement

## moneromooo-monero | 2018-10-01T11:35:37+00:00
+resolved

## quantumproducer | 2018-10-02T13:35:50+00:00
Thank you

# Action History
- Created by: quantumproducer | 2017-12-22T06:57:48+00:00
- Closed at: 2018-10-01T11:56:57+00:00
