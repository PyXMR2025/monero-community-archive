---
title: Add rpc-restricted-bind-ip option
source_url: https://github.com/monero-project/monero/issues/6369
author: omurad
assignees: []
labels: []
created_at: '2020-03-04T17:20:37+00:00'
updated_at: '2024-07-28T06:57:37+00:00'
type: issue
status: closed
closed_at: '2020-12-01T22:21:25+00:00'
---

# Original Description
When running a node as a service (noninteractive) the only way to run commands against the daemon is through the unrestricted RPC port, a port that should not be publicly accessible.

Currently, `monerod` binds both restricted and unrestricted RPC ports to the `rpc-bind-ip` value. So a firewall must be used in order to block incoming connections to the unrestricted RPC port.

It would be nice to have a `rpc-restricted-bind-ip` option so that the unrestricted RPC port can be bound to `localhost` or a private IP, rather than a public IP.

This option would mainly be useful for nodes that are directly exposed to the internet (VPSs) since they can't simply choose not to port forward the unrestricted RPC port.

# Discussion History
## trasherdk | 2020-03-04T19:42:05+00:00
Maybe related to #3083 ?

A clear description/documentation might be helpful.

## omurad | 2020-03-04T23:49:35+00:00
Not related. issue #3083 seems to be related to adding user/pass authentication to specific daemon ports.

What I am proposing is a new option in `monerod`, `rpc-restricted-bind-ip`, which would allow for the restricted and unrestricted RPCs to listen on different IPs. 

This would remove the need for a firewall by allowing the unrestricted RPC to be protected and bound to localhost or LAN IP, while keeping the restricted RPC exposed and bound to LAN IP(port forward)/Public IP.

## pvols1979 | 2020-03-25T16:19:08+00:00
Will this be added soon?  What is the current status?

## thisIsNotTheFoxUrLookingFor | 2024-07-28T06:56:47+00:00
Now we need to be able to remove user:pass login from unrestricted RPC, or are we expected to scope the unrestricted RPC to LAN only and then expose restricted out to the world using this IP? Is that what people are doing? Seems wrong not to put user:pass on the unrestricted RPC! but is we do it, it also puts user:pass on the public RPC which defeats the point of the public RPC!

# Action History
- Created by: omurad | 2020-03-04T17:20:37+00:00
- Closed at: 2020-12-01T22:21:25+00:00
