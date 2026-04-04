---
title: '[Discussion] DNS Seed Nodes Maintenance and Centralization'
source_url: https://github.com/monero-project/monero/issues/9695
author: ohchase
assignees: []
labels:
- discussion
created_at: '2025-01-11T18:39:40+00:00'
updated_at: '2025-01-18T12:41:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Briefly, in order to run a Monerod daemon and successfully communicate with the network there is an initial effort to search for additional Monerod daemon p2p instances to communicate with. 

The default behavior when running over Clearnet on the mainnet chain is to first consider the DNS Seed Nodes [0] .
When considering DNS Seed Nodes, if `m_enable_dns_seed_nodes` is set to false, the entire DNS Seed Node mechanism will be skipped in favor of the IP based seed node mechanism [1]. `m_enable_dns_seed_nodes` is set to true by default though [2]. 
There is 4 DNS seed nodes hard coded as of now found in [3].
```
    const std::vector<std::string> m_seed_nodes_list =
    { "seeds.moneroseeds.se"
    , "seeds.moneroseeds.ae.org"
    , "seeds.moneroseeds.ch"
    , "seeds.moneroseeds.li"
    };
```
From a historical stackexchange communication it seems that @fluffypony is in control of all of these seed nodes [4].

All of these seed nodes do not seem to be operational.
``` 
dig seeds.moneroseeds.se

; <<>> DiG 9.18.28 <<>> seeds.moneroseeds.se
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 12086
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;seeds.moneroseeds.se.		IN	A

;; AUTHORITY SECTION:
moneroseeds.se.		10694	IN	SOA	a.dns.gandi.net. hostmaster.gandi.net. 1560022071 10800 3600 604800 10800

;; Query time: 27 msec
;; SERVER: 10.96.0.1#53(10.96.0.1) (UDP)
;; WHEN: Sat Jan 11 13:35:30 EST 2025
;; MSG SIZE  rcvd: 111
```

The community should consider either
1. Removing DNS Seed Node Mechanism in Full
2. Decentralizing the owners of seed nodes

My largest concern with this situation is, if someone was to squat one of the domains they could immediately begin feeding Monerod nodes with their own selection of curated possibly nefarious nodes.


citations/sources
[0] https://github.com/monero-project/monero/blob/2e8a128c752a3cee2a0bee43b3c15ae7ec344792/src/p2p/net_node.inl#L860
[1] https://github.com/monero-project/monero/blob/2e8a128c752a3cee2a0bee43b3c15ae7ec344792/src/p2p/net_node.inl#L759
[2] https://github.com/monero-project/monero/blob/2e8a128c752a3cee2a0bee43b3c15ae7ec344792/src/p2p/net_node.h#L257
[3] https://github.com/monero-project/monero/blob/2e8a128c752a3cee2a0bee43b3c15ae7ec344792/src/p2p/net_node.h#L301
[4] https://monero.stackexchange.com/questions/11128/how-does-monero-use-dns-to-discover-seed-nodes

# Discussion History
## ohchase | 2025-01-16T11:26:06+00:00
Would like to propose setting enable_dns_seed_nodes to default to false, until community establishes standards on seed nodes

## ohchase | 2025-01-18T12:41:13+00:00
another simple solution 🤷 

```c
    const std::vector<std::string> m_seed_nodes_list = { };
```

# Action History
- Created by: ohchase | 2025-01-11T18:39:40+00:00
