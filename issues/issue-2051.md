---
title: Question about the workflow of leveraging multiple threads together to mine
  XMR
source_url: https://github.com/xmrig/xmrig/issues/2051
author: rainkin1993
assignees: []
labels:
- question
created_at: '2021-01-21T16:42:38+00:00'
updated_at: '2021-04-12T14:23:08+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:23:08+00:00'
---

# Original Description
Hi,

xmrig is a great job! I am trying to read and understand the source of xmrig, but I am a little confused about the workflow of mining.
In my understanding, after receiving a new job from the network, the main thread will let multiple mining threads immediately stop doing the previous job and start doing the new job. However, I do not figure out the way how the main thread (Miner) tells threads to stop and start. Would you please tell me which line of code or variables of functions to do that?

Thanks.

# Discussion History
## tarboss | 2021-01-22T20:08:54+00:00
you can start with Source: CpuWorker.cpp line 200:
template<size_t N>
void xmrig::CpuWorker<N>::start()
{
- consumejob
- randomx_calculate_hash
- inc nonce
- check pool target & send
- wait for other thread to do job


For example:
 i have 3 threads running on my computer (6MB L3 Cache, intel i5-3570k, 1600H/s).
- the template parameter is N = 1 (void xmrig::CpuWorker<1>::start(), runs on each core).
- consumejob inits the nonce for thread0=0, thread1=0x8000, thread2=0x10000)



# Action History
- Created by: rainkin1993 | 2021-01-21T16:42:38+00:00
- Closed at: 2021-04-12T14:23:08+00:00
