---
title: Option to set external advertised IP
source_url: https://github.com/monero-project/monero/issues/5979
author: b3rsrk
assignees: []
labels: []
created_at: '2019-10-11T08:43:29+00:00'
updated_at: '2024-07-29T11:12:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### Problem
I would like to run my Monero nodes (at home) behind my edge server (cloud). The nodes should use my home internet connection for outgoing connections and accept connections on the edge server.

My current setup:
![monerod](https://user-images.githubusercontent.com/29061652/66636116-d2190e00-ec10-11e9-8947-175187ba81a3.png)

My current solution is to route the upstream traffic through the VPN as well. But the Edge Server got multiple public IPs, so there is still an issue.

### Proposal
I'd propose an option similar to `p2p-external-port` to set the advertised external IP: `p2p-external-ip`.

### Reference
bitcoind already got an option like this: https://github.com/bitcoin/bitcoin/issues/15
Additional reference: https://monero.stackexchange.com/questions/6600/monerod-advertise-different-external-ip

# Discussion History
## jbg | 2020-07-10T05:02:22+00:00
This feature is necessary for running a Monero node in any environment where the IP that outbound traffic will be SNAT'ed to differs from the IP that inbound traffic should connect to.

An example is Kubernetes, where the Service abstraction for incoming connections provides an IP dedicated to the service, whereas all outbound connections from the cluster node (or in the case of private clusters, the whole cluster) are usually NAT'ed to the same IP or one of a pool of IPs. At the moment there doesn't appear to be any way to run a Monero node reliably in this kind of environment, as only outbound connections work.

## jbg | 2020-07-10T11:32:03+00:00
Saving this from #monero here:

```
<moneromooo> Should be fairly easy to add. If you're looking for a guide for doing it yourself:
<moneromooo> - Add the same option as --external-p2p-port (if the name's right).
<moneromooo> - Add a field for an IP in the handshake structure, in one of
               src/{p2p,protocol}/*defs.h
<moneromooo> - Write it there when creating your own handshake packet
<moneromooo> - when you receive a handshake, check whether an IP is set in that packet, and use
               that IP instead of the incoming IP if so
<moneromooo> - use that IP to add to the peer list instead of always the incoming IP
<moneromooo> That should be it.
```

I'm hoping to work on this and send a PR next week.

## qertoip | 2021-11-15T13:33:14+00:00
I would also welcome this option.

## reijerh | 2023-03-24T15:01:47+00:00
Related to this: is there a way to advertise a domain/sub-domain instead of an IP for RPC auto-discovery? This way you can use a reverse proxy (e.g. NGINX) to still host monero RPC when you can only forward 1 port that is already needed for other services.

## thisIsNotTheFoxUrLookingFor | 2024-07-29T08:28:51+00:00
Did this ever happen?

## selsta | 2024-07-29T11:12:39+00:00
@tortxoFFoxtrot doesn't appear implemented yet, otherwise this issue would be closed

# Action History
- Created by: b3rsrk | 2019-10-11T08:43:29+00:00
