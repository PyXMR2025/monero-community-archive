---
title: rpc command 'get_version' run failed
source_url: https://github.com/monero-project/monero/issues/6010
author: past2017
assignees: []
labels: []
created_at: '2019-10-23T12:12:05+00:00'
updated_at: '2020-05-16T16:22:11+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:22:11+00:00'
---

# Original Description
**version:**
Monero 'Boron Butterfly' (v0.14.1.0-release)

**steps:**
_run below command on wallet rpc port 18082:_
```
curl -X POST http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_version"}' -H 'Content-Type: application/json'
```
_result:_
```
Warning: Binary output can mess up your terminal. Use "--output -" to tell 
Warning: curl to output it to your terminal anyway, or consider "--output 
Warning: <FILE>" to save to a file.
```
And when I add --output file, it keep stucking

**expected result:**  
should return version number

**below is my config:**
```
log-file=/root/data/monerod.log
log-level=0
max-log-file-size=1048500000 
p2p-bind-ip=0.0.0.0           
p2p-bind-port=18080       
rpc-bind-ip=0.0.0.0            
rpc-bind-port=18081          
confirm-external-bind=1      
restricted-rpc=1              
no-igd=1                     
db-sync-mode=safe:sync
enforce-dns-checkpointing=1
```

**And I run a rpc command by daemon rpc, it looks ok**
```
 curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "alt_blocks_count": 0,
    "block_size_limit": 600000,
    "block_size_median": 300000,
    "block_weight_limit": 600000,
    "block_weight_median": 300000,
    "bootstrap_daemon_address": "",
    "cumulative_difficulty": 3518024849055825,
    "cumulative_difficulty_top64": 0,
    "database_size": 32212254720,
    "difficulty": 29822394845,
    "difficulty_top64": 0,
```


# Discussion History
## moneromooo-monero | 2019-10-23T13:34:29+00:00
Your config:

> rpc-bind-port=18081          

Your client:

> curl -X POST http://localhost:18082


## past2017 | 2019-10-24T03:10:10+00:00
> Your config:
> 
> > rpc-bind-port=18081
> 
> Your client:
> 
> > curl -X POST http://localhost:18082

---------------------------------------------------

**According to https://web.getmonero.org/zh-cn/resources/developer-guides/wallet-rpc.html  monero-wallet-rpc calls should use 18082, daemon rpc use 18081** 

## ndorf | 2019-10-24T03:49:50+00:00
To use wallet RPC, you must have the separate program `monero-wallet-rpc` running, not just the daemon. That program takes its own `--rpc-bind-port` argument.

You can use any port you want for that, but don't use 18082. That port is used by the daemon for ZMQ (that's the binary output you're seeing when you try it). I guess the doc you linked needs updating.

## moneromooo-monero | 2019-10-24T09:12:11+00:00
Examples aren't normative. You should connect to whateve port you've configured (possibly the default), not whatever a particular example uses.

## past2017 | 2019-10-24T09:45:00+00:00
@moneromooo-monero @ndorf  thank you very much, I will try

## past2017 | 2019-10-25T02:25:35+00:00
**something is wrong when I run monero-wallet-rpc, please help me**
.......
_2019-10-25 02:21:13.362	E No message store file found: test.mms_
```
#./monero-wallet-rpc --rpc-bind-port=19999 --wallet-file=test --password ttttttttt --disable-rpc-login
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Boron Butterfly' (v0.14.1.0-release)
Logging to ./monero-wallet-rpc.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
2019-10-25 02:21:09.783	W Loading wallet...
2019-10-25 02:21:09.804	I Generating SSL certificate
2019-10-25 02:21:10.838	I Generating SSL certificate
2019-10-25 02:21:11.840	W Loaded wallet keys file, with public address: 4AtxqnFH5APYb8dW5ZUGgsRRpR4LRC4Ao3UeiiwiUSFvXFSLy6FCdC5Q2tYz1u8TVi1dcFJChJi6g3Ax64udzZvY8BH3QdS
2019-10-25 02:21:13.362	E No message store file found: test.mms
```
@moneromooo-monero @ndorf

## ndorf | 2019-10-25T04:13:40+00:00
Run with `--log-level=4` for more detailed output.

Does `curl -v --insecure https://localhost:18081/get_info` work? (edit: fixed url)

## moneromooo-monero | 2020-05-16T16:22:11+00:00
Seems there's no bug here (that error message is not a bug).

# Action History
- Created by: past2017 | 2019-10-23T12:12:05+00:00
- Closed at: 2020-05-16T16:22:11+00:00
