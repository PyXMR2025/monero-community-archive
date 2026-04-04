---
title: --p2p-bind-ip not work with virtual address
source_url: https://github.com/monero-project/monero/issues/241
author: perl5577
assignees: []
labels:
- bug
created_at: '2015-03-14T02:37:40+00:00'
updated_at: '2018-01-08T12:32:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,
--p2p-bind-ip not work with virtual address

Methode for see pb.
Prerequit for reproduce:
NO IGP in network 
2 IP public routed on server 

if use ip on eth0 
print_cn  as more 40 connexion in 3 minutes with 80% [INC]

if use other address
ip addr add 45.45.45.45/32 dev eth0
print_cn  as more 15 connexion in 3 minutes without [INC]
print_cn  as more 24 connexion in 3 minutes without [INC]


# Discussion History
## moneromooo-monero | 2016-03-20T12:39:50+00:00
Do you need two NICs to test that ?


## dEBRUYNE-1 | 2018-01-08T12:27:43+00:00
+bug

# Action History
- Created by: perl5577 | 2015-03-14T02:37:40+00:00
