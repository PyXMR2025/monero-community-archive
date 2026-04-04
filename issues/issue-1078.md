---
title: 'Testnet Error: Failed to connect to any of seed peers, continuing without
  seeds'
source_url: https://github.com/monero-project/monero/issues/1078
author: phloatingman
assignees: []
labels: []
created_at: '2016-09-16T05:03:02+00:00'
updated_at: '2016-09-18T22:41:33+00:00'
type: issue
status: closed
closed_at: '2016-09-18T22:41:33+00:00'
---

# Original Description
I'm running Monero 'Hydrogen Helix' (v0.9.4.0-7c899ec) in a fresh Ubuntu 16.04.1 64-bit install via VirtualBox.

When I run this command...

`monero@monero:~$ '/home/monero/monero/build/release/bin/monerod' --testnet --testnet-rpc-bind-port 38081`

I get this repeating error...

`2016-Sep-15 21:55:55.582913 [P2P0]Failed to connect to any of seed peers, continuing without seeds`

I'm trying to connect monero-core gui wallet to the testnet.  Any help would be appreciated.  Thanks!


# Discussion History
## ghost | 2016-09-16T10:48:06+00:00
Silly question - do you have that port open on your router?


## phloatingman | 2016-09-16T19:37:53+00:00
I have port 28080 open.  When I go to http://www.canyouseeme.org/ it says it can successfully see the service.  

I tried running testnet on a different laptop running Windows and v0.9.4.0-release and get the same error as well.


## phloatingman | 2016-09-16T20:08:59+00:00
I'm able to run other services fine on my network like http, ssh, vnc.. 


## ghost | 2016-09-17T10:04:00+00:00
Why does having port 28080 open matter when you're trying to bind port 38081?


## mbg033 | 2016-09-17T10:11:06+00:00
I would like to run a node connected to public testnet, but having the same issue.  Tried both on Ubuntu VPS and local windows PC, same error, it looks like remote peers just rejecting connection (tried to connect manually with "telnet remote_ip remote_port"). At the same time,  I can successfully run mainnet node on the same VPS.


## phloatingman | 2016-09-17T10:17:07+00:00
I got the default ports from [here](http://monero.stackexchange.com/questions/604/what-ports-does-monero-use-rpc-p2p-etc/605)...

P2P: 18080 for the mainnet, 28080 for the testnet
RPC: 18081 for the mainnet, 28081 for the testnet

I forwarded 28080 because that's the testnet port for p2p.  

I manually set RPC to 38081 because that's the rpc port that lets my local monero-core (gui wallet) connect to testnet.  38081 doesn't need to be forwarded.


## moneromooo-monero | 2016-09-17T15:03:43+00:00
The RPC port is different from the P2P port. You don't need the RPC port open to have incoming P2P connections (and should be able to connect to a seed node even if your P2P port is not open).
That said, I don't even know if there are seed nodes for testnet.


## phloatingman | 2016-09-18T21:45:48+00:00
How does one become a public seed node for testnet?


## fluffypony | 2016-09-18T21:48:04+00:00
@phloatingman we've just revised the list and removed all the dead ones. Becoming a seed node is non-trivial, because of the responsibility involved (even for testnet), so you basically need to be part of the dev community for a few months and then offer.


## phloatingman | 2016-09-18T22:41:26+00:00
@fluffypony thanks for the quick reply!

Monero 'Wolfram Warptangent' (v0.10.0.0-release) seems to be working with testnet just fine now...

`Height: 7201/802057 (0.9%) on testnet, syncing, net hash 324 H/s, v1, up to date, 4+0 connections`


# Action History
- Created by: phloatingman | 2016-09-16T05:03:02+00:00
- Closed at: 2016-09-18T22:41:33+00:00
