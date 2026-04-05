---
title: The Small vRam GPU can`t mining Kawpow(opencl)
source_url: https://github.com/xmrig/xmrig/issues/3045
author: xzh767
assignees: []
labels: []
created_at: '2022-05-07T14:21:54+00:00'
updated_at: '2022-06-05T06:08:07+00:00'
type: issue
status: closed
closed_at: '2022-06-05T06:08:07+00:00'
---

# Original Description
If the GPU`S Vram<2048MB，It can`t minging Kawpow,but the xmrig will try to mining it
The opencl will dead,but xmrig don`t know it
Xmrig will keep trying
It can lead to a dead cycle

# Discussion History
## Spudz76 | 2022-05-07T17:32:22+00:00
Yes so when kawpow DAG becomes too large, you disable kawpow.

## xzh767 | 2022-05-09T07:02:03+00:00
> Yes so when kawpow DAG becomes too large, you disable kawpow.

But If In Algo-Testing,xmrig will try to mine kawpow
opencl can't produce any hashrate
Xmrig can't break and in a dead cycle

## xzh767 | 2022-05-09T07:03:32+00:00
And How can disable Kawpow and run Algo-Testing?

## SChernykh | 2022-05-09T07:43:05+00:00
Algo-Testing is not a part of the official Xmrig, ask this question to whoever added it (MoneroOcean?)

## xzh767 | 2022-05-09T08:40:27+00:00
> Algo-Testing is not a part of the official Xmrig, ask this question to whoever added it (MoneroOcean?)

emmmmm
I know
But How can disable Kawpow?

## Spudz76 | 2022-05-09T14:36:44+00:00
Compile with `-DWITH_KAWPOW=OFF` and then it won't even know it's a thing (that's what I do).

I have been working on ways to actually disable algorithms because I think the above is the only way it works.  But it may also be able to skip based on DAG size.

## Spudz76 | 2022-05-09T14:38:03+00:00
And yes you should be posting MO problems over at [MoneroOcean/xmrig Issues](https://github.com/MoneroOcean/xmrig/issues)

## xzh767 | 2022-05-11T11:56:27+00:00
> Compile with `-DWITH_KAWPOW=OFF` and then it won't even know it's a thing (that's what I do).
> 
> I have been working on ways to actually disable algorithms because I think the above is the only way it works. But it may also be able to skip based on DAG size.

I know and search
But...Is not have how to compile on windows

## ghost | 2022-05-17T18:09:51+00:00
Windows build instructions can be found [here](https://xmrig.com/docs/miner/build/windows).

## xzh767 | 2022-06-05T06:08:07+00:00
I Knew
Thank You

# Action History
- Created by: xzh767 | 2022-05-07T14:21:54+00:00
- Closed at: 2022-06-05T06:08:07+00:00
