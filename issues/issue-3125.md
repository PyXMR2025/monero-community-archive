---
title: Duplicate Shares issue on GhostRider
source_url: https://github.com/xmrig/xmrig/issues/3125
author: Jimmy062006
assignees: []
labels:
- bug
created_at: '2022-09-18T23:39:52+00:00'
updated_at: '2023-01-04T17:40:33+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:20:25+00:00'
---

# Original Description
**Describe the bug**
Duplicate Shares issue on GhostRider only using XMRig

**To Reproduce**
Mine with XMRig to a miningcore pool

**Expected behavior**
No Duplicate Shares

**Required data**
`[2022-09-19 00:34:31.692]  net      new job from strat.just4miners.com:3008 diff 96827 algo ghostrider height 401925
[2022-09-19 00:34:32.632]  cpu      rejected (69/3) diff 96827 "duplicate share" (25 ms)
[2022-09-19 00:34:33.656]  cpu      rejected (69/4) diff 96827 "duplicate share" (25 ms)`

```{"jsonrpc":"2.0","method":"mining.notify","params":["00002e87","d32a951c72b8e768392d82cfc9f7dd73b8e1c3c2a990271dbc867e9213f3c2a7","03000500010000000000000000000000000000000000000000000000000000000000000000ffffffff1d03cd050404d548256200","0a4d696e696e67636f72650000000003a8ea7648170000001976a9143542a8dd417574b43e091fb246b6ca46b6a54b7288acaaba1dd2050000001976a914cc36a8de36f6ff61dbfb798982e8b47354ad4e0e88acf8efbd4f570000001976a9149fdf79eacbfae060f9344cbcc1864e0b2f3a579c88ac00000000460200cd0504001aae02b30746cdb0a86e0626b50f042c80eec359293f416533f8af37dac35b41822e50a1386107de3180098c5965de207e9063a83a1e32a821eca94d9f421f22",["01e793ff27660b201792f9ab16c3a43d7704e3d1fcf90940a9376a2d31adc123","b272feacb6b5dabfa0292388ad943b7ac3547338d3a90240fee03ad02ea4d7f0","03aabbeec95d753a3494d4e0216b6578d6791bf4ce71a4a2db5984ba2e21edb7"],"20000000","1c38040a","622548d5",false],"id":null} {"id":99,"jsonrpc":"2.0","method":"mining.submit","params":["RRAWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.WORKER001","00002e87","00000000","622548d5","001a8010"]} {"result":true,"id":99} {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[1.0869940759657157],"id":null} {"jsonrpc":"2.0","method":"mining.notify","params":["00002e87","d32a951c72b8e768392d82cfc9f7dd73b8e1c3c2a990271dbc867e9213f3c2a7","03000500010000000000000000000000000000000000000000000000000000000000000000ffffffff1d03cd050404d548256200","0a4d696e696e67636f72650000000003a8ea7648170000001976a9143542a8dd417574b43e091fb246b6ca46b6a54b7288acaaba1dd2050000001976a914cc36a8de36f6ff61dbfb798982e8b47354ad4e0e88acf8efbd4f570000001976a9149fdf79eacbfae060f9344cbcc1864e0b2f3a579c88ac00000000460200cd0504001aae02b30746cdb0a86e0626b50f042c80eec359293f416533f8af37dac35b41822e50a1386107de3180098c5965de207e9063a83a1e32a821eca94d9f421f22",["01e793ff27660b201792f9ab16c3a43d7704e3d1fcf90940a9376a2d31adc123","b272feacb6b5dabfa0292388ad943b7ac3547338d3a90240fee03ad02ea4d7f0","03aabbeec95d753a3494d4e0216b6578d6791bf4ce71a4a2db5984ba2e21edb7"],"20000000","1c38040a","622548d5",false],"id":null} {"id":100,"jsonrpc":"2.0","method":"mining.submit","params":["RRAWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.WORKER001","00002e87","00000000","622548d5","001a8010"]} {"result":false,"error":{"code":22,"message":"duplicate share","data":null},"id":100}```

**Additional context**
I'm just trying to understand why this happens and if this if needs to be in XMRig or in the pool I'm running this does not happen on any other GhostRider Miner on my pool and the second job log (pool side) is not the same as the first duplicate share log.

https://github.com/oliverw/miningcore/discussions/1301

# Discussion History
## SChernykh | 2022-09-19T07:50:15+00:00
The pool sent exactly the same job twice, so XMRig found exactly the same solution twice.

## SChernykh | 2022-09-19T07:53:12+00:00
I will add a check for this in XMRig, but the pool shouldn't send duplicate jobs in the first place.

## Jimmy062006 | 2022-09-19T09:19:26+00:00
@SChernykh I thought that but when I brought it up with the pool dev I was told this.

That's not a duplicate but a job refresh to include the latest transactions in the merkle tree.

## SChernykh | 2022-09-19T09:20:43+00:00
Job refresh would have a different mining blob, and the log you pasted has exactly the same blob, so it's broken on the pool side.

## Jimmy062006 | 2022-09-19T09:21:25+00:00
@SChernykh thanks for the confirmation on that. I thought I was going mad :D lol.

cpuminer does not report this issue though. Is that due to what your going to code above ?

## SChernykh | 2022-09-19T09:37:43+00:00
I don't know how cpuminer handles it.

## snoby | 2023-01-04T17:39:51+00:00
@xmrig 
This tends to happen on a vardiff update ( below snippet is from the pool stratum ).
```
{ "time": "2023-01-04 17:37:18.2125", "level": "INFO", "logger": "bitoreum_pool", "message": "[0HMNEBNQH8I9E] VarDiff update to 0.311" }

{ "time": "2023-01-04 17:37:22.1194", "level": "INFO", "logger": "bitoreum_pool", "message": "[0HMNEBNQH8I9E] Share rejected: duplicate share [XMRigCC/3.3.1 (Linux x86_64) libuv/1.44.1 gcc/10.3.0]" }
```

I've seen the same thing before  with bzminer and radiant algorithm.

# Action History
- Created by: Jimmy062006 | 2022-09-18T23:39:52+00:00
- Closed at: 2022-12-13T14:20:25+00:00
