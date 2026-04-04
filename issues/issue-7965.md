---
title: 'E Failed to bind IPv6: resolve: Host not found (authoritative)'
source_url: https://github.com/monero-project/monero/issues/7965
author: li5lo
assignees: []
labels: []
created_at: '2021-09-22T11:18:30+00:00'
updated_at: '2025-08-29T17:49:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
IPv6 addresses are supposed to be specified in brackets (although i don't know if it's a requirement).

Run monerod with this command:
`./monerod --testnet --log-level 1 --data-dir /[your directory]/ --p2p-bind-ip 0.0.0.0 --p2p-bind-port 28080 --p2p-use-ipv6 --p2p-bind-ipv6-address [::] --p2p-bind-port-ipv6 28080
`

You will get an error that monerod failed to bind IPv6 but it looks like monerod then still successfully binds to [::]:
```
2021-09-22 10:08:25.524	I Binding (IPv4) on 0.0.0.0:28080
2021-09-22 10:08:25.524	I Binding (IPv6) on [::]:28080
2021-09-22 10:08:25.526	E Failed to bind IPv6: resolve: Host not found (authoritative)
2021-09-22 10:08:25.526	I Net service bound (IPv4) to 0.0.0.0:28080
2021-09-22 10:08:25.526	I Net service bound (IPv6) to [::]:28080
2021-09-22 10:08:25.526	I p2p server initialized OK
2021-09-22 10:08:25.526	I Initializing core RPC server...
2021-09-22 10:08:25.526	I Set server type to: 1 from name: RPC, prefix_name = RPC
2021-09-22 10:08:25.526	I Binding on 127.0.0.1 (IPv4):28081
2021-09-22 10:08:25.527	I Generating SSL certificate
2021-09-22 10:08:25.957	I core RPC server initialized OK on port: 28081
```

Now do the same **without** putting brackets around the IPv6 address:
`./monerod --testnet --log-level 1 --data-dir /[your directory/ --p2p-bind-ip 0.0.0.0 --p2p-bind-port 28080 --p2p-use-ipv6 --p2p-bind-ipv6-address :: --p2p-bind-port-ipv6 28080`

You will **not** get an error:
```
2021-09-22 10:09:19.615	I Binding (IPv4) on 0.0.0.0:28080
2021-09-22 10:09:19.615	I Binding (IPv6) on :::28080
2021-09-22 10:09:19.615	I Net service bound (IPv4) to 0.0.0.0:28080
2021-09-22 10:09:19.615	I Net service bound (IPv6) to :::28080
2021-09-22 10:09:19.615	I p2p server initialized OK
2021-09-22 10:09:19.616	I Initializing core RPC server...
2021-09-22 10:09:19.616	I Set server type to: 1 from name: RPC, prefix_name = RPC
2021-09-22 10:09:19.616	I Binding on 127.0.0.1 (IPv4):28081
2021-09-22 10:09:19.616	I Generating SSL certificate
2021-09-22 10:09:20.023	I core RPC server initialized OK on port: 28081
```

I don't know what the error message tries to tell me but i believe it should _not_ success _without_ error message when i do it the wrong way and success _with_ error when i do it correctly.

# Discussion History
## knofte | 2025-08-29T17:49:44+00:00
Any update to this?

# Action History
- Created by: li5lo | 2021-09-22T11:18:30+00:00
