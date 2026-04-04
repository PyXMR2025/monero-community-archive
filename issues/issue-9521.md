---
title: Stagenet tor unable to relay transactions
source_url: https://github.com/monero-project/monero/issues/9521
author: darkerego
assignees: []
labels:
- question
created_at: '2024-10-16T04:40:27+00:00'
updated_at: '2024-11-04T15:24:00+00:00'
type: issue
status: closed
closed_at: '2024-10-20T14:43:03+00:00'
---

# Original Description
I have been debugging this for a couple of days. I am starting to think that maybe the problem is that there just aren't many tor stagenet nodes? But then I don't understand why that would matter, it's not as if tor isn't capable of connecting to an ipv4 address. I have tried a variety of configurations including running with torsocks, and running with `--proxy` and `--tx-proxy` , and then also just running with` --tx-proxy`, both with and without the disable noise parameter, I have tried deleting my p2pstate.bin file, I have tried `--add--peer` <some.ip.addresss.123:38081> and --add-exclusive-node <some.ip.addresss.123:38081> with a bunch of both onion and ipv4 addresses ... I think I have tried everything I can think of. The result is always the same.

` W Unable to send transaction(s) to tor - no available outbound connections`

This is my current configuration. 


```
 /usr/local/bin/monerod --data-dir /home/user/stagenet --rpc-login xmr:olly123456seven --rpc-bind-ip 127.0.0.1 --rpc-bind-port 38081 --p2p-bind-ip 127.0.0.1 --p2p-bind-port 38084 --anonymous-inbound naa4r4irvpuhi2vkdergpukdwejxaq67lsrxosv6uxilpsqalnhmw7ad.onion.onion:38080,127.0.0.1:38080,25,disable_noise --rpc-ssl enabled --add-peer ct36dsbe3oubpbebpxmiqz4uqk6zb6nhmkhoekileo4fts23rvuse2qd.onion:38081 --add-peer plowsoffjexmxalw73tkjmf422gq6575fc7vicuu4javzn2ynnte6tyd.onion:38089 --add-peer ykqlrp7lumcik3ubzz3nfsahkbplfgqshavmgbxb4fauexqzat6idjad.onion:38081 --add-peer  --add-priority-node ct36dsbe3oubpbebpxmiqz4uqk6zb6nhmkhoekileo4fts23rvuse2qd.onion:38081 --add-priority-node ykqlrp7lumcik3ubzz3nfsahkbplfgqshavmgbxb4fauexqzat6idjad.onion:38081 --add-priority-node plowsoffjexmxalw73tkjmf422gq6575fc7vicuu4javzn2ynnte6tyd.onion:38089 --seed-node 37.187.74.171:38080 --seed-node 51.79.173.165:38080 --seed-node 176.9.0.187:38080 --seed-node 192.99.8.110:38080 --bootstrap-daemon-address auto --tx-proxy tor,127.0.0.1:9050,50 --proxy 127.0.0.1:9050 --no-zmq --no-igd --non-interactive --log-file /var/log/monero/monero.log --log-level 1 --stagenet
```


What the actual heck is happening here?

I did manage to get one transaction to go through by setting up an external node without --tx-proxy enabled and setting up a hidden service on this node and then adding that as a peer and priority node, but initially the tx was rejected , deep in the debug logs was a 'double spend' error ... which makes no sense as this wallet had never sent any transactions, failed or otherwise before. But then I ran rescan_spent and suddenly the transaction went through ... which is progress, I GUESS, except I am building something that needs to be reliable, and this is the antithesis of that. So I am wondering, does stagenet just suck over tor? Because I have totally ran functional monero mainnet nodes behind whonix and that was a cakewalk. This is 3 days of debugging and tearing my hair out.



Here's a debug log : https://termbin.com/4wis

# Discussion History
## selsta | 2024-10-17T23:32:16+00:00
> it's not as if tor isn't capable of connecting to an ipv4 address

If you setup `--tx-proxy` then it will only send transactions over Tor, if there are no Tor connections it won't fallback to clearnet. The issue is likely the lack of people running Tor on stagenet.

## darkerego | 2024-10-17T23:50:17+00:00
> > it's not as if tor isn't capable of connecting to an ipv4 address
> 
> If you setup `--tx-proxy` then it will only send transactions over Tor, if there are no Tor connections it won't fallback to clearnet. The issue is likely the lack of people running Tor on stagenet.

I figured. Thanks for confirming.

## 0xFFFC0000 | 2024-10-20T14:42:59+00:00
I am closing this issue. Please feel free to reopen it in case you had any questions. 

## darkerego | 2024-11-04T15:23:42+00:00
Yeah,  I have confirmed that it a lack of stable peers on stagenet.

# Action History
- Created by: darkerego | 2024-10-16T04:40:27+00:00
- Closed at: 2024-10-20T14:43:03+00:00
