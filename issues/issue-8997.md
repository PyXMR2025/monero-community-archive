---
title: monerod connection count vs RPC get_info call
source_url: https://github.com/monero-project/monero/issues/8997
author: edge7
assignees: []
labels: []
created_at: '2023-09-21T11:57:22+00:00'
updated_at: '2023-09-21T13:41:51+00:00'
type: issue
status: closed
closed_at: '2023-09-21T13:41:50+00:00'
---

# Original Description
the output of monerod status, in particular, the connections part:

`16(out)+32(in) connections
`
  should match `incoming_connections_count` and `outgoing_connections_count` given by `get_info` RPC call?

# Discussion History
## SChernykh | 2023-09-21T12:27:00+00:00
Yes, `status` gets data from `/getinfo` RPC call: https://github.com/monero-project/monero/blob/master/src/daemon/rpc_command_executor.cpp#L461 and https://github.com/monero-project/monero/blob/master/src/daemon/rpc_command_executor.cpp#L528

## edge7 | 2023-09-21T12:41:33+00:00
ok, good to know.
For me, for some reason, it does not.
this is my node: http://edge7.servebeer.com:18089/get_info
![image](https://github.com/monero-project/monero/assets/5433786/fec6e4c2-1998-4741-b289-0d32570d4a5b)

this is the status:
```
~ $ monerod status
2023-09-21 12:39:03.804 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Height: 2979050/2979050 (100.0%) on mainnet, not mining, net hash 2.32 GH/s, v16, 16(out)+32(in) connections,
```
I can clearly see the connections, running some netstat | grep ...

It's not the most important thing ever, but If anyone has a clue would be great. Thanks

## selsta | 2023-09-21T12:48:03+00:00
Are you running a node with restricted RPC? If yes it won't display the amount of connections.

## SChernykh | 2023-09-21T12:48:14+00:00
`monerod status` should connect to port 18081 (unrestricted RPC) by default. You're connecting to port 18089 (restricted RPC), maybe this is why.

## edge7 | 2023-09-21T12:53:33+00:00
`docker run -d --restart unless-stopped --name="monerod"  --log-opt max-size=10m -p 18080:18080 -p 18089:18089 -p 18083:18083 -v /home/edge7/Desktop/monerod:/home/monero/.bitmonero  sethsimmons/simple-monerod:latest --rpc-restricted-bind-ip=0.0.0.0 --rpc-restricted-bind-port=18089 --no-igd --zmq-pub tcp://0.0.0.0:18083  --in-peers=32 --out-peers=16 --public-node --disable-dns-checkpoints --enable-dns-blocklist`

so yes, definetely.
Potentially, can I bind the non-restricted one just to the local LAN IP, so I can use that one to check stuff visually with the browser?



## edge7 | 2023-09-21T12:57:28+00:00
this works fine:

```
~ $ wget http://localhost:18081/get_info
Connecting to localhost:18081 (127.0.0.1:18081)
```

I get all the info

## SChernykh | 2023-09-21T12:58:29+00:00
`--rpc-bind-ip YOUR_LAN_IP --confirm-external-bind`

## edge7 | 2023-09-21T13:03:12+00:00
Can you spend 2 words on  --confirm-external-bind, as the first makes sense?

Then I can happily close the issue! :)

## SChernykh | 2023-09-21T13:06:20+00:00
From command line description `Confirm rpc-bind-ip value is NOT a loopback (local) IP`

# Action History
- Created by: edge7 | 2023-09-21T11:57:22+00:00
- Closed at: 2023-09-21T13:41:50+00:00
