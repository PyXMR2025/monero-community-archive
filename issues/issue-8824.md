---
title: Persistent high CPU usage for a 24 hours
source_url: https://github.com/monero-project/monero/issues/8824
author: g00g1
assignees: []
labels: []
created_at: '2023-04-16T08:21:52+00:00'
updated_at: '2023-04-23T10:35:05+00:00'
type: issue
status: closed
closed_at: '2023-04-23T10:35:05+00:00'
---

# Original Description
How can I figure out why monero daemon is utilizing almost 2 CPU cores fully for more than 24 hours is straight? Is it normal behavior for a public node? I am not observing high bandwidth utilization although. As of daemon start the blockchain was already synchronized.

```
$ date -u; echo; monerod status
Sun Apr 16 08:18:55 UTC 2023

2023-04-16 08:18:56.829	I Monero 'Fluorine Fermi' (v0.18.2.2-unknown)
Height: 2865386/2865386 (100.0%) on mainnet, not mining, net hash 2.49 GH/s, v16, 258(out)+73(in) connections, uptime 2d 20h 48m 29s
```

![image](https://user-images.githubusercontent.com/91201021/232284935-bbfdf14b-b65e-4eb6-958b-b59c3a817c3c.png)

![image](https://user-images.githubusercontent.com/91201021/232284599-21d8998a-d184-4d2e-ab87-a190b1ac5c68.png)


# Discussion History
## selsta | 2023-04-16T11:53:17+00:00
How did you install monerod? Did you compile it yourself?

## g00g1 | 2023-04-16T11:59:03+00:00
> How did you install monerod? Did you compile it yourself?

Yes, I have compiled it from source with `CXXFLAGS="-march=native -O2 -pipe"` using [Gentoo ebuild](https://gitweb.gentoo.org/repo/proj/guru.git/tree/net-p2p/monero/monero-0.18.2.2.ebuild) and `USE="daemon -readline -tools -wallet-cli -wallet-rpc"`

## selsta | 2023-04-16T12:00:31+00:00
Apply this patch: https://github.com/monero-project/monero/pull/8731

# Action History
- Created by: g00g1 | 2023-04-16T08:21:52+00:00
- Closed at: 2023-04-23T10:35:05+00:00
