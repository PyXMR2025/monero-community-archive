---
title: status only shows 100% as daemon is synchronizing
source_url: https://github.com/monero-project/monero/issues/8879
author: Gingeropolous
assignees: []
labels:
- low priority
- daemon
- reproduction needed
created_at: '2023-05-26T10:56:20+00:00'
updated_at: '2025-12-28T23:31:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
Height: 1837972/1837972 (100.0%) on mainnet, not mining, net hash 318.13 MH/s, v11, 12(out)+0(in) connections, uptime 1d 0h 19m 45s
```

and a minute later or so..

```
2023-05-26 10:55:09.943	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Height: 1838352/1838352 (100.0%) on mainnet, not mining, net hash 310.89 MH/s, v11, 12(out)+0(in) connections, uptime 1d 0h 21m 4s
```

this is the result of the "status" command. The daemon is daemonized and managed by systemd. im using RPC to send the status command. 

v0.18.2.2 . release binaries. 

# Discussion History
## selsta | 2023-05-26T11:07:43+00:00
Does sync_info work? Also do you always have this behaviour with status or just now suddenly?

## Gingeropolous | 2023-05-26T13:08:55+00:00
honestly it's been a while since I've done a fresh sync, but it just seems "now suddenly". 

sync_info shows the same

```
user@phantom:~$ monerod --rpc-bind-port 12345 sync_info
2023-05-26 13:08:30.270	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Height: 1892752, target: 1892752 (100%)
Downloading at 612 kB/s
Next needed pruning seed: 1
12 peers
```

## selsta | 2023-05-26T13:10:29+00:00
Is this on the machine with sync troubles?

## Gingeropolous | 2023-05-26T13:25:07+00:00
it is on both machines. the login node had sync troubles. phantom already syncd once with fast-sync=1, now its trudging along doing fast-sync=0.

## Gingeropolous | 2023-05-26T18:11:18+00:00
more information. I'm running the daemon with

```
rpc-restricted-bind-ip=192.168.1.22
rpc-bind-ip=0.0.0.0
confirm-external-bind=1
rpc-restricted-bind-port=18089
rpc-bind-port=12345
public-node=1
log-level=2

```
and throwing the status command at it with:

```
monerod --rpc-bind-port 12345 status
```



## Gingeropolous | 2023-05-28T18:07:12+00:00
now it seems to be showing realistic things

```
2023-05-28 18:06:20.938	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Height: 2566652/2895883 (88.6%) on mainnet, not mining, net hash 2.94 GH/s, v14, 12(out)+0(in) connections, uptime 0d 5h 28m 33s
```

## selsta | 2025-12-28T23:30:46+00:00
Is this still happening recently?

# Action History
- Created by: Gingeropolous | 2023-05-26T10:56:20+00:00
