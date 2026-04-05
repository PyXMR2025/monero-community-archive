---
title: KAWPOW not working on windows 6.11.1
source_url: https://github.com/xmrig/xmrig/issues/2249
author: ghost
assignees: []
labels:
- question
created_at: '2021-04-09T04:48:26+00:00'
updated_at: '2021-04-12T13:29:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:29:15+00:00'
---

# Original Description
**Describe the bug**
Starting the miner using kawpow is not recognized

**To Reproduce**
xmrig.exe -kawpow -o *pool* -u *wallet* returns *incompatible or disabled algorithm*




# Discussion History
## Spudz76 | 2021-04-09T05:20:56+00:00
KawPow does not mine on CPU, do you have CUDA or OpenCL?

## SChernykh | 2021-04-09T06:20:47+00:00
`xmrig.exe -a kawpow -o pool -u wallet`
https://xmrig.com/docs/miner/command-line-options

## ghost | 2021-04-09T20:48:29+00:00
> KawPow does not mine on CPU, do you have CUDA or OpenCL?

For the project I'm currently working on I need to use CPU for mining, I was hoping to use RVN if possible

## Spudz76 | 2021-04-10T01:12:04+00:00
You'll have to find some old Ravencoin miner that supports CPU still, maybe doesn't exist.  You probably will never score a hash.  What are you trying to do?  If you just want to mine CPU+GPU to maximum profit on a single box, then get on a pool with multicoin autoswitch like MoneroOcean and run one on CPU and another on GPU they will run different algos whichever is most profitable at the time.  You do need their fork of xmrig to support the extended algo-perf function so the pool knows your hashrates per algo and can decide which algo is best to send.  Vanilla xmrig won't autoswitch.  They pay out in XMR with autochanging which makes mining different coins less hassle.  Then if you want RVN trade the XMR for it.

# Action History
- Created by: ghost | 2021-04-09T04:48:26+00:00
- Closed at: 2021-04-12T13:29:15+00:00
