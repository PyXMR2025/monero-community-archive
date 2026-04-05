---
title: 'Making impossible mining in centralized pools over 25 % of net hashrate '
source_url: https://github.com/xmrig/xmrig/issues/3086
author: Rack96
assignees: []
labels: []
created_at: '2022-07-12T19:23:29+00:00'
updated_at: '2025-06-28T10:42:52+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:42:52+00:00'
---

# Original Description
**Describe the bug**

I’m asking for a solution for implementing on xmrig software itself to make impossible for my computers to make a connection on a centralized pool over a limited hasrate. 

In think something like that should be default on xmrig to improve network 
**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2022-07-13T04:03:07+00:00
There is no standard way of getting a pool total hashrate so this is not possible.

Nobody wants to maintain individual pool API calls or even worse web scrapes to find this (probably inaccurate) information.

## Rack96 | 2022-07-13T05:56:57+00:00
> There is no standard way of getting a pool total hashrate so this is not possible.
> 
> Nobody wants to maintain individual pool API calls or even worse web scrapes to find this (probably inaccurate) information.

I read somewhere it’s possible to read the block template from each pool by the miner 

## Spudz76 | 2022-07-13T17:07:16+00:00
And then where in a block template does any sort of statistic like total pool hashrate become available?  Reasonably sure it doesn't.

# Action History
- Created by: Rack96 | 2022-07-12T19:23:29+00:00
- Closed at: 2025-06-28T10:42:52+00:00
