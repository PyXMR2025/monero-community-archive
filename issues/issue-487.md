---
title: Failover pools with different algorithms
source_url: https://github.com/xmrig/xmrig/issues/487
author: danielhuang
assignees: []
labels:
- enhancement
created_at: '2018-03-30T13:40:50+00:00'
updated_at: '2018-11-05T14:45:41+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:45:41+00:00'
---

# Original Description
Is it possible to have 2 pools, but with different algorithms?
## Example
Pool 1: aeon.example.com
Pool 2: monero.example.com
If pool 1 goes down, it should switch to pool 2 and also switch the algorithm.

Thanks in advance

# Discussion History
## xmrig | 2018-03-30T14:02:11+00:00
It not possible at this moment, but I thinking about this feature. Different algorithms, requires different settings, so should be added ability to set it separably for each algorithms, second hugepages should be reused.
Thank you.

## JPaulMora | 2018-04-01T06:31:55+00:00
This should be pretty easy to implement as long as the user specifies which algo to use with which pool. You can't quite "guess" the algorithm without sending invalid shares.

That, or extend pool protocol to tell which algorithm to use.. I'd be curious to try that.

## xmrig | 2018-04-01T06:47:55+00:00
Protocol or specify algo per pool is easiest part. Hard part different algorithms required different settings, for example, typical desktop i7 8 MB.

- `cryptonight-lite` 4 or 8 threads.
- `cryptonight` 4 or 2 threads.
- `cryptonight-heavy` 2 or 1 thread.

## 2010phenix | 2018-04-01T12:26:47+00:00
maybe simple, after change pool(algo) ... disconnect\reset hugepages \ active threads and connect over
swich (algo)
case: 
{
(settings)
}

## reeyon | 2018-06-01T01:36:16+00:00
I would like to see this feature on the next release. 

## xmrig | 2018-11-05T14:45:40+00:00
Merge with #618

# Action History
- Created by: danielhuang | 2018-03-30T13:40:50+00:00
- Closed at: 2018-11-05T14:45:41+00:00
