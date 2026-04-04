---
title: 'Tor / I2P node: How serious are these log messages? ("Unable to send transaction(s)
  to (tor|i2p) - no suitable outbound connections at height X", "Incoming connections
  disabled, enable them for full connectivity")'
source_url: https://github.com/monero-project/monero/issues/7863
author: xanoni
assignees: []
labels: []
created_at: '2021-08-16T00:33:38+00:00'
updated_at: '2021-08-27T01:09:51+00:00'
type: issue
status: closed
closed_at: '2021-08-20T02:03:00+00:00'
---

# Original Description
I keep seeing below messages, should I be concerned or are these just IP-artifacts that don't matter in case of Tor / I2P nodes (see configuration below)?

1. `I Incoming connections disabled, enable them for full connectivity`
2. `W Unable to send transaction(s) to i2p - no suitable outbound connections at height Y`
3. `W Unable to send transaction(s) to tor - no suitable outbound connections at height X`

I see (2) and (3) maybe 10-25x per hour, whereas (1) is less frequent at ~2x per hour.

**Settings / Version:**

`Monero 'Oxygen Orion' (v0.17.2.0-release)` with the below key settings:
```
tx-proxy=i2p,127.0.0.1:4447,25
tx-proxy=tor,127.0.0.1:9050,25

anonymous-inbound=XYZ.b32.i2p:${I2P_EXT_PORT},127.0.0.1:18080,25 # `i2pd` tunnel was defined manually
anonymous-inbound=XYZ.onion:${TOR_EXT_PORT},127.0.0.1:18080,25

# settings equivalent to the below also used for RPC 
p2p-ignore-ipv4=1
p2p-use-ipv6=0
p2p-bind-ip=127.0.0.1
p2p-bind-port=18080

hide-my-port=1
public-node=0
no-igd=1
allow-local-ip=0
no-zmq=1
```

EDIT1: `torsocks` / `proxychains` / `torify` are NOT used.
EDIT2: Another observation, not sure if related — I see only very few Tor and I2P nodes among my connected peers. Which setting should be tweaked to increase the ratio?

# Discussion History
## xanoni | 2021-08-16T03:32:57+00:00
I guess at least the first one is serious ... 

```bash
$ xmrd status
2021-08-16 XYZ I Monero 'Oxygen Orion' (v0.17.2.0-release)
Height: XYZ/XYZ (100.0%) on mainnet, not mining, net hash 2.69 GH/s, v14, 64(out)+0(in) connections, uptime X
```

See the connection count (64 out / 0 in). I thought I had taken care of this by defining the `anonymous-inbound` lines.

Or did I use the wrong ports in these lines? I couldn't find anything in the documentation that explained what these ports are:

```
anonymous-inbound=XYZ.b32.i2p:${I2P_EXT_PORT},127.0.0.1:18080,25 # `i2pd` tunnel was defined manually
anonymous-inbound=XYZ.onion:${TOR_EXT_PORT},127.0.0.1:18080,25
```

The ${I2P_EXT_PORT} and ${TOR_EXT_PORT} are clearly discretionary and depend on how you set up the HS. But what about the second port? Should that not be the P2P port that `monerod` is already listening on? Is it maybe the RPC port, or is it a completely different port? Docs are not explaining it.

EDIT: Well here's a good start, I now specified two new & unused ports and `monerod` indeed started listening ... 

monerod   24967        xmrd   15u  IPv4 12228187      0t0  TCP localhost:18084 (LISTEN)
monerod   24967        xmrd   16u  IPv4 12228188      0t0  TCP localhost:18083 (LISTEN)


EDIT2: But still 0 incoming connections. Would I have to disable `--hide-my-port` maybe?

## xanoni | 2021-08-17T06:18:26+00:00
No clue. Can someone say if my hypothesis is correct, i.e., that `--hide-my-port` needs to be removed for `anonymous-inbound` to work? Or is it something else? Still no peers after more than a day.

## xanoni | 2021-08-19T08:28:15+00:00
Alright, the removal of `--hide-my-port` actually seems to have fixed it (EDIT — bullshit... it doesn't make a difference, was just Placebo). The confusion was caused by the fact that the `status` RPC command only shows IPv4 / IPv6 peers. The documentation doesn't explain these things very well.

```bash
$ monerod status
2021-08-19 12:21:44.344 I Monero 'Oxygen Orion' (v0.17.2.0-release)
Height: 2430372/2430372 (100.0%) on mainnet, not mining, net hash 2.63 GH/s, v14, 0(out)+0(in) connections, uptime 1d 5h 14m 41s
```

I also realized that the `in_peers` and `out_peers` config lines only affect IPv4/IPv6 connections and are NOT inclusive of the Tor and I2P connection count defined via `--anonymous-inbound` and `--tx-proxy`. In the above, I set both to 0 (disclaimer: has to be positive to receive blocks). Only the Tor and I2P connections (which are now plenty ... ) remain when I check `monerod print_cn`.

I see ~90 total connections, with ~65 incoming Tor connections. The majority of the outgoing connections are I2P. I don't have any incoming I2P connections. I haven't figured out, yet, why this is the case. I suspect that that "0" port causes trouble with `i2pd`.

## xanoni | 2021-08-20T02:03:00+00:00
Given Tor now seems to be working fine, I'll close this and open a ticket specifically for I2P incoming connections.

# Action History
- Created by: xanoni | 2021-08-16T00:33:38+00:00
- Closed at: 2021-08-20T02:03:00+00:00
