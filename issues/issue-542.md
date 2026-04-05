---
title: 'DNS error: "temporary failure"'
source_url: https://github.com/xmrig/xmrig/issues/542
author: ghost
assignees: []
labels: []
created_at: '2018-04-11T23:57:36+00:00'
updated_at: '2020-05-05T18:18:37+00:00'
type: issue
status: closed
closed_at: '2018-04-12T22:03:34+00:00'
---

# Original Description
When trying to mine on a VPS the following gets printed when running xmrig:

    [us-east.cryptonight-hub.miningpoolhub.com:20580] DNS error: "temporary failure"
OS: Ubuntu 16.04.4

# Discussion History
## djfinch | 2018-04-12T21:27:37+00:00
It looks like DNS-related issue with your VPS. Is port 53 unblocked? Try one of following IP instead of hostname. If problem persist then it's not DNS...
```
;us-east.cryptonight-hub.miningpoolhub.com. IN A

;; ANSWER SECTION:
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.132.70
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.224.250
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.250.141
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.252.176
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.148.42
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.126.71
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.217.166
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.151.232
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.247.21
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.143.224
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.207.32
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.205.58
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.76.21
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.49.55
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.205.68
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.210.48
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.235.97
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.241.136
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.204.241
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.210.117
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.94.15
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.200.97
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.46.14
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.159.158
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.60.220
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.210.116
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.65.177
us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.192.137
```

## ghost | 2018-04-12T22:03:27+00:00
Using one of those ip addreses solved the issue, thanks!

## mrshah-1994 | 2020-05-05T18:18:37+00:00
> It looks like DNS-related issue with your VPS. Is port 53 unblocked? Try one of following IP instead of hostname. If problem persist then it's not DNS...
> 
> ```
> ;us-east.cryptonight-hub.miningpoolhub.com. IN A
> 
> ;; ANSWER SECTION:
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.132.70
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.224.250
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.250.141
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.252.176
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.148.42
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.126.71
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.217.166
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.151.232
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.247.21
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.143.224
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.207.32
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.205.58
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.76.21
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.49.55
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.205.68
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.210.48
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.235.97
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.241.136
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.204.241
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.210.117
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.94.15
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.200.97
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.46.14
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.104.159.158
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.60.220
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 172.105.210.116
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 139.162.65.177
> us-east.cryptonight-hub.miningpoolhub.com. 300 IN A 45.79.192.137
> ```
[xmr.pool.minergate.com:45700] DNS error: "temporary failure"


# Action History
- Created by: ghost | 2018-04-11T23:57:36+00:00
- Closed at: 2018-04-12T22:03:34+00:00
