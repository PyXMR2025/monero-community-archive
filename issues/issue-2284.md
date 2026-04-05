---
title: which algo supports solo mining ?
source_url: https://github.com/xmrig/xmrig/issues/2284
author: github-vp
assignees: []
labels: []
created_at: '2021-04-19T05:57:43+00:00'
updated_at: '2021-04-20T20:18:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Solo mining with CCX seems to be not working. In core log, Miner makes connection, sends json request and server sends response. This keeps on repeating. No update on miner screen. Connection status check on miner indicates no connections. ON shutting miner core log indicated closing of all connections. 

Additionally It would be nice to have list of algo/coins that suport solo mining and working.**

**To Reproduce**
Start miner with algo cn/ccx along with -daemon option. 
xmrig.exe -cuda -o 127.0.0.1:16000 -u address -a cn/ccx  --daemon

**Required data**

 - Node log 
 **STARTING MINER**
2021-Apr-20 15:10:51.190387 DEBUG [HttpServer] Incoming connection from 127.0.0.1:59107
2021-Apr-20 15:10:51.191600 TRACE [RpcServer] JSON-RPC request: {"id":10,"jsonrpc":"2.0","method":"getblocktemplate","params":{"wallet_address":"ccx7CVLziVD5U8bkuG6q31LKvW7y4ZvUteiTNJGjg5eje8PLohViPyPQBcryvwfq6NWyPBXVsHCmNgzqJDQprL6a2Low1xd7oh","extra_nonce":"5d8d5e100564483c"}}
2021-Apr-20 15:10:51.195624 TRACE [RpcServer] JSON-RPC response: {"id":10,"jsonrpc":"2.0","result":{"blocktemplate_blob":"0800cbeafc8306535d36cc8345de20a083a8429bb96547d023e8dccecbeffb56ac3af91d780d99000000000196df2d01ff8cdf2d01809bee020201503a305944f4ae8ddff5f222d012fc63c5852426e10cebd7260ea034a99d978b0101d4b8ed3935b78aa2693713836f05683676e2ca75c3bf2d672bf57b20aed2a4770268000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000","difficulty":103000000,"height":749452,"reserved_offset":128,"status":"OK"}}

**STOPPING MINER**
2021-Apr-20 00:32:47.276340 DEBUG [HttpServer] Closing connection from 127.0.0.1:58464 total=4
2021-Apr-20 00:32:47.277337 DEBUG [HttpServer] Closing connection from 127.0.0.1:58467 total=3
2021-Apr-20 00:32:47.278335 DEBUG [HttpServer] Closing connection from 127.0.0.1:58485 total=2
2021-Apr-20 00:32:47.279333 DEBUG [HttpServer] Closing connection from 127.0.0.1:58505 total=1

 - Config file or command line (without wallets)
xmrig.exe -cuda -o 127.0.0.1:16000 -u address -a cn/ccx  --daemon

 - OS: 
 Windows 10, xmrig 6.11.2, CCX Core 6.4.5
 



# Discussion History
# Action History
- Created by: github-vp | 2021-04-19T05:57:43+00:00
