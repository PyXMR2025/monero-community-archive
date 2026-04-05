---
title: Arm
source_url: https://github.com/xmrig/xmrig/issues/601
author: 0xman
assignees: []
labels:
- arm
created_at: '2018-05-04T04:53:01+00:00'
updated_at: '2018-06-17T18:09:45+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:09:45+00:00'
---

# Original Description
Does This support arm mining like with a home raspberry pi server ?

# Discussion History
## calvintam236 | 2018-05-05T03:35:17+00:00
I don't think it is effective mining on pi. It is too slow.

https://monero.stackexchange.com/questions/6862/could-i-use-a-raspberry-pi-to-mine-monero

## 0xman | 2018-05-05T14:46:20+00:00
So its possible  ? 

## ghost | 2018-05-05T23:28:56+00:00
Yes. It is possible.

Raspberry Pi can get about 10h/s per watt, which is actually pretty good for 'per watt' performance... But the total hashes are still pretty low (despite being efficient): For cryptonight algo, Pi 2 and 3 get about 8-10 h/s, Pi 1 and zero get about 0.75-1 h/s. For cryptonight-lite, triple the hashes.

## lunhg | 2018-05-14T14:41:07+00:00
I could get  14 H/s, up to 21Hs with CPU mining in a ArchLinux (aarch64) in a model Pi 3,  with cryptonight-lite.

The only issue i found is that you need to connect with a port that accept low diffs. Generally solves hashes with 300-500 diff, but sometimes solves 1000-1200 diff.

With splitted tests, i colud get 0.0001889814 AEONS with ~ 700k Hashes, i think, in a sum of 12 hs

There are any way to use GPU?

# Action History
- Created by: 0xman | 2018-05-04T04:53:01+00:00
- Closed at: 2018-06-17T18:09:45+00:00
