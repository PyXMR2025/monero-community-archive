---
title: /get_info doesn't include peers
source_url: https://github.com/monero-project/monero-gui/issues/3312
author: jnbarlow
assignees: []
labels: []
created_at: '2021-01-19T03:11:32+00:00'
updated_at: '2021-02-01T01:43:19+00:00'
type: issue
status: closed
closed_at: '2021-02-01T01:43:19+00:00'
---

# Original Description
I've found that the /get_info call doesn't include connected peers (sync_info ran directly in the daemon returns peers).  Also, the /get_peer_info call returns a 404.

Really, a lot of methods in the rpc documentation don't seem to exist ... return "method not found" errors (yes, I'm running monerod and not the wallet)


# Discussion History
## selsta | 2021-01-31T23:03:55+00:00
Are you running restricted rpc?

## jnbarlow | 2021-01-31T23:53:59+00:00
@selsta Yes, but I'm running the restricted RPC on port 18089, and the regular rpc running at 18080 (the port I'm using)

## selsta | 2021-01-31T23:55:07+00:00
18080 is P2P port, you sure that you are using 18080 for RPC?

## jnbarlow | 2021-02-01T00:00:02+00:00
@selsta sorry, I meant 18081 ... the default rpc port. 

```
 --rpc-use-ipv6 --rpc-bind-ip 0.0.0.0 --rpc-bind-ipv6-address ::0  --confirm-external-bind --rpc-payment-credits 250 --rpc-payment-difficulty 1000 --rpc-payment-address  <addy> --restricted-rpc --rpc-restricted-bind-port 18089 --public-node --rpc-restricted-bind-ip 0.0.0.0 --enable-dns-blocklist
```

## jnbarlow | 2021-02-01T00:02:11+00:00
status command in monerd:
```
Height: 2286891/2286891 (100.0%) on mainnet, not mining, net hash 1.92 GH/s, v14, 12(out)+69(in) connections, uptime 16d 2h 5m 9s
```
output of /get_info
![image](https://user-images.githubusercontent.com/1322371/106402287-c8fc1380-63f6-11eb-9c97-e9d71e711d73.png)


## selsta | 2021-02-01T00:51:57+00:00
I don't see an unrestricted RPC running at 18081 in your config. Also setting --restricted-rpc will make everything restricted.

try removing --restricted-rpc and add --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18081 --rpc-restricted-bind-ip 0.0.0.0 --rpc-restricted-bind-port 18089

## jnbarlow | 2021-02-01T01:43:19+00:00
@selsta That did it.  I assumed that since it came up with `--rpc-restricted-rpc` that it would use the specific bind port, but it was restricting both of them.  Removing that and specifying each type of rpc port made things work.  Closing issue :)

# Action History
- Created by: jnbarlow | 2021-01-19T03:11:32+00:00
- Closed at: 2021-02-01T01:43:19+00:00
