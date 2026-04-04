---
title: In regtest, generateblocks returns status:BUSY if using --no-sync
source_url: https://github.com/monero-project/monero/issues/9124
author: meglio
assignees: []
labels:
- low priority
- more info needed
created_at: '2024-01-17T14:49:33+00:00'
updated_at: '2024-01-19T16:41:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I can generate blocks just fine when running a regtest node like this:

`monerod --non-interactive --regtest --keep-fakechain --offline --fixed-difficulty=1 --data-dir=/monero/data --log-file=/monero/logs/monerod.log --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18551 --confirm-external-bind --log-level=2 --rpc-login="monero:monero" --disable-rpc-ban --db-sync-mode=safe --no-zmq`

But as soon as I add `--no-sync`, calls to `generateblocks` would return:

```json
{
  "id": "generateblocks",
  "jsonrpc": "2.0",
  "result": {
    "height": 0,
    "status": "BUSY",
    "untrusted": false
  }
}
```

`v0.18.3.1`

# Discussion History
## selsta | 2024-01-17T14:53:09+00:00
Why do you want to use --no-sync here in the first place? It means the daemon stays on the current height.

## meglio | 2024-01-17T14:57:11+00:00
The command line `--help` says something different:

> Don't synchronize the blockchain with other peers

It is not the same as "stay on the current height". I.e. I assumed I could generate blocks but just stop it from synchronizing with other peers.

So my suggestion is then to do two things:

1. Improve the description of the `--no-sync` parameter. Maybe say generating blocks won't work.
2. Improve the error message. Returning `status:BUSY` does not help identify the issue at all.

This was really not obvious and I spent whole day asking people around and in the IRC channel, plus a bit of experimentation, to find it out.

## ghost | 2024-01-18T14:26:21+00:00
Mu^drt2/to-dt1s' = 3.134gak1v . at^2
8/2ab^b'c|ax| / qt3E(pn) . Thd( = QoV
1/2TcsGv(KN) . V(He) / Od(CO2) . Od(He) = g08ru'imy^-eish/at^2
Oc|mx| = ad^2 || MGg·Kfu/^(-e^2).+eK.piu'
Kt(a) . dgid(ntciby) = ucvg /e.(d^2)gv(a)
Ort . g01pi = chmg'p|y| / (x)out
Kpc(a) = 10/4 Ecv / 4/2 Ecb
C(n+1)^(e-e+)^2 = At1^2/-(D(n+1)ts)^2

## moneromooo-monero | 2024-01-19T16:41:43+00:00
I think selsta meant that if left to its own devices, the daemon will stay on its current height. IIRC the --no-sync option got added to allow the proxy system to work without delay, it does not need to prevent mining.

# Action History
- Created by: meglio | 2024-01-17T14:49:33+00:00
