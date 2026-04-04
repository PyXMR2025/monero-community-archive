---
title: node.moneroworld.com providing too many records, truncated and switches to
  TCP which breaks OS X
source_url: https://github.com/monero-project/monero/issues/3190
author: Paris
assignees: []
labels: []
created_at: '2018-01-27T12:59:21+00:00'
updated_at: '2021-08-13T04:12:23+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:12:23+00:00'
---

# Original Description
On OS X (fails):
```
$ nslookup node.moneroworld.com
;; Truncated, retrying in TCP mode.
;; Connection to 192.168.1.254#53(192.168.1.254) for node.moneroworld.com failed: connection refused.
```

On Linux (works):
```
;; Truncated, retrying in TCP mode.
Server:		108.61.10.10
Address:	108.61.10.10#53

Non-authoritative answer:
Name:	node.moneroworld.com
Address: 103.208.86.41
Name:	node.moneroworld.com
Address: 73.252.200.173
Name:	node.moneroworld.com
Address: 62.210.124.152
Name:	node.moneroworld.com
Address: 91.121.57.211
Name:	node.moneroworld.com
Address: 45.77.79.9
Name:	node.moneroworld.com
Address: 129.232.220.90
Name:	node.moneroworld.com
Address: 185.54.115.25
Name:	node.moneroworld.com
Address: 87.98.219.208
Name:	node.moneroworld.com
Address: 45.63.14.175
Name:	node.moneroworld.com
Address: 89.27.3.43
Name:	node.moneroworld.com
Address: 83.251.191.132
Name:	node.moneroworld.com
Address: 74.98.232.170
Name:	node.moneroworld.com
Address: 37.59.250.166
Name:	node.moneroworld.com
Address: 71.71.202.191
Name:	node.moneroworld.com
Address: 51.15.213.174
Name:	node.moneroworld.com
Address: 172.245.41.237
Name:	node.moneroworld.com
Address: 173.255.205.142
Name:	node.moneroworld.com
Address: 163.172.142.217
Name:	node.moneroworld.com
Address: 99.150.228.240
Name:	node.moneroworld.com
Address: 139.59.59.176
Name:	node.moneroworld.com
Address: 185.194.143.154
Name:	node.moneroworld.com
Address: 220.134.32.226
Name:	node.moneroworld.com
Address: 162.210.173.15
Name:	node.moneroworld.com
Address: 85.17.172.179
Name:	node.moneroworld.com
Address: 52.53.73.145
Name:	node.moneroworld.com
Address: 217.237.182.62
Name:	node.moneroworld.com
Address: 138.201.221.109
Name:	node.moneroworld.com
Address: 72.50.221.9
Name:	node.moneroworld.com
Address: 216.155.149.66
Name:	node.moneroworld.com
Address: 96.43.139.226
Name:	node.moneroworld.com
Address: 37.153.1.247
Name:	node.moneroworld.com
Address: 173.87.36.128
```

Suggestion: have the server return only 3-4 records to fit into a UDP packet.

# Discussion History
## Gingeropolous | 2018-01-27T17:44:07+00:00
if you have the skills to run a DNS server that can do that, please do. 

or please consider hacking away at issue #2204 , so we can avoid having to use DNS servers entirely. 

I don't have the skills to do either. At best, im a skiddie. 

## leonklingele | 2018-01-27T17:48:01+00:00
> On OS X (fails):

It works just fine for me on OS X. Maybe it's a problem with your DNS resolver (`192.168.1.254`)? DNS over TCP is not that uncommon at all.

## Gingeropolous | 2018-01-27T17:48:09+00:00
also, I've found that the error can occur based on your DNS server settings - i.e., if your main server is googles, it usually works fine.

Also, this is better suited for the moneriote repo. 

## selsta | 2021-08-13T04:12:23+00:00
Wrong repo, also issue doesn't see relevant anymore. Closing.

# Action History
- Created by: Paris | 2018-01-27T12:59:21+00:00
- Closed at: 2021-08-13T04:12:23+00:00
