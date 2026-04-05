---
title: 'Connection Issue '
source_url: https://github.com/xmrig/xmrig/issues/2144
author: vanthome
assignees: []
labels: []
created_at: '2021-03-01T10:18:03+00:00'
updated_at: '2021-04-12T14:08:46+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:08:46+00:00'
---

# Original Description
Hi, I have two machines and one of them can connect and the other one not, I see this error:

`[2021-03-01 10:16:57.906]  net      pool.xmr.pt:9000 connect error: "operation canceled"`

The only different is that once machine is exposed to the internet with a public IP and the other one not. Could that be the reason?
Of course both machines have unlimited Internet connection.

BG


# Discussion History
## vanthome | 2021-03-25T20:22:48+00:00
More info about this:

XMRig is running on a machine that has access to the Internet vie a router on which ipforwarding is enabled and the following iptables rules exist:

```
iptables -t nat -I POSTROUTING -s x.x.x.x/24 ! -o bond0 -j MASQUERADE
iptables -I FORWARD -i bond0 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

What could be missing to allow XMrig to connect?


## Spudz76 | 2021-03-26T19:24:01+00:00
If the default disposition for OUTPUT table is not ACCEPT you probably also need:
`iptables -I OUTPUT -m tcp -p tcp --dport 9000 -j ACCEPT`

In order to allow the `state NEW` portion of the outgoing connection (so it can even achieve `RELATED,ESTABLISHED`).

`iptables-save` provides a nice dump of all the current rules including the default disposition for the main tables.

# Action History
- Created by: vanthome | 2021-03-01T10:18:03+00:00
- Closed at: 2021-04-12T14:08:46+00:00
