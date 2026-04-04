---
title: Private testnet - getblocktemplate returns invalid (previous) prev_hash
source_url: https://github.com/monero-project/monero/issues/4922
author: jakubschimer
assignees: []
labels: []
created_at: '2018-11-30T14:10:30+00:00'
updated_at: '2019-01-01T14:33:00+00:00'
type: issue
status: closed
closed_at: '2019-01-01T14:33:00+00:00'
---

# Original Description
I'am running Monero (v0.13.0.4-release) private testnet from height 1.
I'am periodically calling getblocktemplate via RPC. After few successfull block submits (1 to 4),
the prev_hash field in getblocktemplate response doesen't change - it stays on the same value which of course results in new block submits being rejected. (----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT N message in monerod). On the other hand, when i run start_mining <wallet_addr> on monerod, prev_hash field in getblocktemplate result seems to be changing as it's supposed to.

Iam running testnet nodes as:
monerod --testnet --no-igd --hide-my-port --data-dir ~/testnet/node_01 --p2p-bind-ip 0.0.0.0 --log-level 1 --add-exclusive-node 127.0.0.1:38080 --add-exclusive-node 127.0.0.1:48080 --fixed-difficulty 199 --detach
monerod --testnet --p2p-bind-port 48080 --rpc-bind-port 48081 --zmq-rpc-bind-port 48082 --no-igd --hide-my-port  --log-level 1 --data-dir ~/testnet/node_03 --p2p-bind-ip 0.0.0.0 --add-exclusive-node 127.0.0.1:28080 --add-exclusive-node 127.0.0.1:38080 --fixed-difficulty 199 --detach 
monerod --testnet --p2p-bind-port 38080 --rpc-bind-port 38081 --zmq-rpc-bind-port 38082 --no-igd --hide-my-port  --log-level 0,blockchain:DEBUG,*rpc*:DEBUG --data-dir ~/testnet/node_02 --p2p-bind-ip 0.0.0.0 --add-exclusive-node 127.0.0.1:28080 --add-exclusive-node 127.0.0.1:48080 --fixed-difficulty 199

Log output from node to which i'am connecting via RPC can be found here:
https://paste.fedoraproject.org/paste/csSp6In4lX2UPxVg-LgPxQ

# Discussion History
## moneromooo-monero | 2018-12-02T13:11:30+00:00
https://github.com/monero-project/monero/pull/4928

I could repro the problem. I did not see it after the patch. Given it's race, this does not prove it's 100% fixed though. Please check whether you can still see it.


## moneromooo-monero | 2018-12-13T01:13:21+00:00
Can you confirm it fixed your problem ?

## jakubschimer | 2018-12-13T07:14:19+00:00
Hello,
Yes, your patch fixed the problem.

Thank you
Jakub


> On 13 Dec 2018, at 02:13, moneromooo-monero <notifications@github.com> wrote:
> 
> Can you confirm it fixed your problem ?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero/issues/4922#issuecomment-446805575>, or mute the thread <https://github.com/notifications/unsubscribe-auth/AAXfTtJdGSvJDLWOMOlgi7cOTctoBCNaks5u4am6gaJpZM4Y7vGK>.
> 



## moneromooo-monero | 2019-01-01T14:09:07+00:00
+resolved

# Action History
- Created by: jakubschimer | 2018-11-30T14:10:30+00:00
- Closed at: 2019-01-01T14:33:00+00:00
