---
title: 'sendto: Network is unreachable'
source_url: https://github.com/monero-project/monero/issues/7904
author: S1700
assignees: []
labels: []
created_at: '2021-08-28T14:47:37+00:00'
updated_at: '2021-08-31T17:05:38+00:00'
type: issue
status: closed
closed_at: '2021-08-31T17:04:53+00:00'
---

# Original Description
When I ran the command `monerod` in the bin dir after a bit of time it said `sendto: Network is unreachable`. I can't find any solutions online what could be the problem?

# Discussion History
## selsta | 2021-08-28T16:17:21+00:00
Do you have any issues apart from this message?

## S1700 | 2021-08-28T16:36:17+00:00
wat?

## cirocosta | 2021-08-28T19:31:05+00:00
Hey @Samuel20354, without much context is hard to help (e.g., which version? which OS? any other logs? did it ever work? have you tried with a higher log-level number? which flags passed to `--monerod`? etc).

"Network is unreachable" (`ENETUNREACH`) arrives when the kernel can't find a route to send a packet through in order to reach that destination ip. 

e.g., if I have no routes and ifaces (other than loopback) at all and try to ping `1.1.1.1`, i'll get back an `ENETUNREACH`

```console
$ route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface

$ ip a
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

$ ping 1.1.1.1
ping: connect: Network is unreachable
```

---

upadate: I'm not suuuper familiar with the codebase, but it's _very_ likely `sendto` is being used on something UDP-related, which I imagine would be either on dns resolution or the miniupnp stuff (which can be disabled via `--no-igd`)

## S1700 | 2021-08-29T13:13:15+00:00
Oh hi, I just saw this sorry. So the OS that I'm using is Ubuntu it's a VPS from vultr. This is the first time I have ran this and so it has not worked for me before. I don't know how to get the logs or how to change the log number. and I ran the monerod command by its self. This is what happens when I run the commands that you ran:
![image](https://user-images.githubusercontent.com/68336568/131251631-cc2f7d82-e324-4e4b-8112-170110832266.png)

Thanks!

## S1700 | 2021-08-31T12:08:59+00:00
?

## selsta | 2021-08-31T17:04:53+00:00
If `ping 1.1.1.1` fails on your VPS it's not a monero related issue so I don't think the issue tracker here is the best place to resolve this. I would suggest you to contact Vultr support.

## S1700 | 2021-08-31T17:05:38+00:00
ok

# Action History
- Created by: S1700 | 2021-08-28T14:47:37+00:00
- Closed at: 2021-08-31T17:04:53+00:00
