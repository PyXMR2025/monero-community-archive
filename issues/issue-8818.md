---
title: Monero seems to have an IPv4-only problem.
source_url: https://github.com/monero-project/monero/issues/8818
author: 86dd
assignees: []
labels: []
created_at: '2023-04-04T13:46:41+00:00'
updated_at: '2026-02-06T01:57:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
- My IPv6-only monerod node can't seem to find any IPv6 peers. It only wastes it's time on IPv4 nodes.
- The seed nodes seem to only be IPv4. Adding some IPv6 seed nodes would be important.
- When I told it to use IPv6 only (p2p-ignore-ipv4=1, rpc-ignore-ipv4=1), it still tries and binds IPv4. It would be great to be able to fully turn off IPv4.
- You must explicitly enable IPv6 (p2p-use-ipv6=1, rpc-use-ipv6=1). Ideally, IPv6 should be enabled by default.
- Node websites I've visited are either .onion or IPv4 only. I'm aware this has nothing to do with this repository, but including it in this discussion may get them to support IPv6.

I'd love to contribute to the source code, but unfortunately I don't feel comfortable in C++ (yet), so maybe starting this discussion will help getting the "IPv6 ball rolling" for Monero.

# Discussion History
## poiuty | 2023-04-05T19:23:53+00:00
Why is ipv6 disabled by default?

```
--p2p-use-ipv6 | Enable IPv6 for p2p (disabled by default).

https://monerodocs.org/interacting/monerod-reference/
```

## rnhmjoj | 2023-04-07T08:03:28+00:00
If not enabled by default IPv6 support is quite useless in a p2p application. 
Probably the only users that will go through the docs, find the cli option and enable it are those on an IPv6-only network, but then it won't matter because there's nobody else to peer: dual stacked users will only ever use IPv4.

## kkarhan | 2023-04-18T07:25:49+00:00
> Why is ipv6 disabled by default?
> 
> ```
> --p2p-use-ipv6 | Enable IPv6 for p2p (disabled by default).
> 
> https://monerodocs.org/interacting/monerod-reference/
> ```

I'm convinced this is done amidst the fears of [pseudo-]static IPv6 assignments?
A lot of people think that NAT is a security feature and the lack of said NAT + the use of EUI48 aka. MAC-Adresses to create the Interface Indentifier unless Privacy Extensions are being enabled [which basically all Desktop & mobile OSes do by default!] is seen as a privacy infringement.

Still, I think that Monero should support proper dual-stack and not care whether or not someone uses IPv4, IPv6 nor VPNs or even Tor and thus default to proper dual stack, with the option to prefer and/or disable IPv4 [or even IPv6 if there would be any legit reason to do so]... 

## boldsuck | 2023-04-22T21:03:53+00:00
> * My IPv6-only monerod node can't seem to find any IPv6 peers. It only wastes it's time on IPv4 nodes.
> 
> * The seed nodes seem to only be IPv4. Adding some IPv6 seed nodes would be important.

You can use mine for `seed-node= | add-priority-node= | add-peer=` if you want. RPC & P2P is dual stacked + .onion.

xmr-de.boldsuck.org | xmr-in-berlin.boldsuck.org
185.220.101.63:18080
2a0b:f4c2:2::63:18080
2i3jrsezgjyqgmrqk4t3dxoixihv3aa6zzmrxlz7qr6n3l2bhilxwxyd.onion:18083  <- p2p
i4jsfwmw22yjzzmzkoc7aahiaqlyhnykn5wxel43u3o5ibz2k4275jqd.onion:18081  <- RPC

xmr-de-2.boldsuck.org | xmr-in-berlin-2.boldsuck.org
185.220.101.223:18080
2a0b:f4c2:2:1::223:18080
sqzrokz36lgkng2i2nlzgzns2ugcxqosflygsxbkybb4xn6gq3ouugqd.onion:18083  <- p2p
6dsdenp6vjkvqzy4wzsnzn6wixkdzihx3khiumyzieauxuxslmcaeiad.onion:18081  <- RPC

For blockchain sync use the top two. They are connected with 2x10G, the others only have 1G NIC.

xmr-de-1.boldsuck.org | crypto-01.boldsuck.org
217.79.184.72:18080
2001:4ba0:ffff:c4::2:18080
k6eefejth3zgej4xr7zzxlw457akgswg5bapfn4ragc2yxtvi3j7cxid.onion:18083  <- p2p
ip4zpbps7unk6xhlanqtw24f75akfbl3upeckfjqjks7ftfnk4i73oid.onion:18081   <- RPC

**Stagenet node:**
xmr-lux.boldsuck.org
104.244.75.217:38080
2605:6400:30:f91d::2:38080
rsdfcp3c7v7shamu5quyuw72takrlxgqbg3x5tyvts2d4whtstf35iyd.onion:38083   <- p2p
ct36dsbe3oubpbebpxmiqz4uqk6zb6nhmkhoekileo4fts23rvuse2qd.onion:38081   <- RPC


## 86dd | 2023-04-29T15:54:56+00:00
I've tried them but as mentioned before monero unfortunately keeps trying IPv4.
I'll look into writing patches - if I have the time - to enable IPv6 by default, an "algorythm" to test for connectivity and add an option to restrict it to a network - like with bitcoinds --onlynet=ipv6|ipv4|onion.

## rnhmjoj | 2023-04-29T17:08:13+00:00
@juliaszone: If you want an algorithm for choosing between IPv4/IPv6 [RFC 8305](https://www.rfc-editor.org/rfc/rfc8305.txt) may be worth a look. Also, [RFC 8880](https://www.rfc-editor.org/rfc/rfc8880.txt) for detecting an IPv6-only network with NAT64 available.

## boldsuck | 2023-04-29T21:06:55+00:00
> I've tried them but as mentioned before monero unfortunately keeps trying IPv4.

@juliaszone Have you tried the following options in your monerod.conf?

`~$ monerod --help`
```
p2p-bind-ipv6-address[::] 
p2p-use-ipv6=1                     Enable IPv6 for p2p
p2p-ignore-ipv4=1                  Ignore unsuccessful IPv4 bind for p2p
rpc-bind-ipv6-address=[::1]
rpc-restricted-bind-ipv6-address=[::]
rpc-use-ipv6=1                     Allow IPv6 for RPC
rpc-ignore-ipv4=1                  Ignore unsuccessful IPv4 bind for RPC
```


## 86dd | 2023-05-01T19:58:20+00:00
@boldsuck Yes:
![grafik](https://user-images.githubusercontent.com/90114526/235520578-4c946d5d-10a8-408c-a83d-ac445a7a3af1.png)
(it's supposed to be a public node fy)

## ivanka2012 | 2023-05-02T14:08:50+00:00
@boldsuck All 3 of your IPv6 mainnet nodes are resetting p2p connections being made to port 18080


## boldsuck | 2023-05-07T21:47:09+00:00
I looked at the peer lists on all my nodes, only IP and .onion, there isn't a single IPv6 address among thousands :-(

```
marco@boldsuck2:~$ monerod --rpc-bind-port=8081 print_pl_stats
2023-05-07 15:16:55.073 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
White list size: 1532/1000 (153.2%)
Gray list size: 5613/5000 (112.26%)
```
This is how my own nodes look in the list:
```
white      2d7f80e8053574e2          185.220.101.192:18080     18081 -     0    d0.h1.m31.s3
white      2d7f80e8053574e2          185.220.101.223:18080     18081 -     0    d0.h0.m1.s15
gray       1cac1e4b919c97a8          185.220.101.32:18080      18081 -     184  never
gray       1cac1e4b919c97a8          185.220.101.33:18080      18081 -     0    never
gray       1cac1e4b919c97a8          ::ffff:185.220.101.32:18080 18081 -     0    never
gray       392ffba366eb11a3          ::ffff:185.220.101.33:18080 18081 -     0    never
gray       1cac1e4b919c97a8          ::ffff:185.220.101.39:18080 18081 -     0    never
gray       1cac1e4b919c97a8          ::ffff:185.220.101.63:18080 18081 -     0    never
gray       2d7f80e8053574e2          ::ffff:185.220.101.192:18080 18081 -     0    never
```

[ditatompel's node](https://www.ditatompel.com/monero/node-peers) doesn't see IPv6 either.

All my monerod nodes are not listening on the IPv6 P2P port even though it is configured:

```
# P2P full node
p2p-bind-ip=0.0.0.0            # Bind default to all interfaces (0.0.0.0)
p2p-bind-port=18080            # Bind to default port 18080, 28080 if 'testnet', 38080 if 'stagenet'
p2p-bind-ipv6-address=[::]     # Bind default to all interfaces (::)
p2p-bind-port-ipv6=18080      # (default same as ipv4 port for given nettype)
p2p-use-ipv6=1                 # Enable IPv6 for p2p (default false)
```

```
root@boldsuck:~# ss -lt src :18080
State                       Recv-Q                      Send-Q                                           Local Address:Port                                             Peer Address:Port                      Process
LISTEN                      0                           128                                                    0.0.0.0:18080                                                 0.0.0.0:*
root@boldsuck:~# ss -lt src :18081
State                       Recv-Q                      Send-Q                                           Local Address:Port                                             Peer Address:Port                      Process
LISTEN                      0                           128                                                    0.0.0.0:18081                                                 0.0.0.0:*
LISTEN                      0                           128                                                       [::]:18081                                                    [::]:*
```
¯\_(ツ)_/¯

## boldsuck | 2023-05-07T22:55:01+00:00
Uhh I got it. The brackets at `p2p-bind-ipv6-address=[::]` interfere.
Weird `rpc-bind-ipv6-address=[::1] `and `rpc-restricted-bind-ipv6-address=[::]` can be specified with brackets.
Now with `p2p-bind-ipv6-address=::` all nodes are listening dual again:
```
root@boldsuck:~# ss -lt src :18080
State                       Recv-Q                      Send-Q                                           Local Address:Port                                             Peer Address:Port                      Process
LISTEN                      0                           128                                                    0.0.0.0:18080                                                 0.0.0.0:*
LISTEN                      0                           128                                                       [::]:18080                                                    [::]:*
root@boldsuck2:~# ss -lt src :18080
State                       Recv-Q                      Send-Q                                           Local Address:Port                                             Peer Address:Port                      Process
LISTEN                      0                           128                                                    0.0.0.0:18080                                                 0.0.0.0:*
LISTEN                      0                           128                                                       [::]:18080                                                    [::]:*
root@crypto-01:~# ss -lt src :18080
State                       Recv-Q                      Send-Q                                           Local Address:Port                                             Peer Address:Port                      Process
LISTEN                      0                           128                                                    0.0.0.0:18080                                                 0.0.0.0:*
LISTEN                      0                           128                                                       [::]:18080                                                    [::]:*
```
And now there are also IPv6 addresses in my peer list:
```
white      40da54d17d341a75          2001:4ba0:ffff:c4::2:18080 18081 -     0    d0.h0.m1.s1
white      9e2447f269b04293          2a0b:f4c2:2:1::223:18080  18081 -     0    d0.h0.m1.s1
```
Is this a bug or a new feature?
Previously, IPv6 addresses had to be specified as "[xx:xx:xx::xx:xx]:port" in the configuration file, except in the cases of the cli arguments for the bind address. For these, the square brackets can be omitted.

## cyboerg42 | 2023-05-14T14:24:22+00:00
```
add-priority-node=[2001:41d0:801:2000::5811]:18080
add-priority-node=[2a03:3b40:100::1:513]:18080
add-priority-node=[2602:ff16:1:0:1:138:0:1]:18080
add-priority-node=[2001:470:de5a::ec]:18080
add-priority-node=[2a01:4f9:3051:17a1::2]:18080
add-priority-node=[2604:4300:a:358::146]:18080
add-priority-node=[2a0b:f4c2:2::63]:18080
add-priority-node=[2a0b:f4c2:2:1::223]:18080
add-priority-node=[2001:4ba0:ffff:c4::2]:18080
add-priority-node=[2001:678:7f8::b00b]:18080
add-priority-node=[2a01:190:1337::206]:18080
```

Some of the nodes I've found while scanning public nodes for AAAA DNS entries.

## boldsuck | 2023-05-14T22:10:05+00:00
> add-priority-node=[2001:4ba0:ffff:c4::2]:18080

Will be offline in a few weeks, new server is up & monerod synced:
`add-priority-node=[2001:4ba0:ffff:4a::2]:18080`

## imcdona | 2023-12-01T23:31:06+00:00
I've been running an IPv6 enabled node for several weeks and haven't had a single incoming IPv6 connection. Is there a config option that must be specified to advertise the IPv6 node port?

Here's my IPv6 enabled node for anyone needing an IPv6 enabled peer:

`add-priority-node=[2602:41:642e:a610::251]:18080`

## X3KT0 | 2023-12-07T10:49:36+00:00
I've read the entire thread.
So nobody will find my IPv6 address by regular P2P node address advertising procedure, am I right?

## boldsuck | 2023-12-07T15:16:06+00:00
There are only a few, but all my monero nodes have some IPv6 in the P2P list:

```
marco@boldsuck:~$ monerod --rpc-bind-port=8081 print_cn | grep IPv6
OUT :                         IPv6    no    0000000000000000    0                   0(0)/307(0)                   before_handshake         0                   0           0             0         0
INC :                         IPv6    no    37248f7ff5715720    1                   782069(5)/784239(13)          normal                   672                 1           0             1         1
INC :                         IPv6    no    f39c9b0803a808f5    1                   1230393(13)/1228912(2)        normal                   1245                0           0             0         0
INC :                         IPv6    no    d752fad99e6821ad    1                   2157030(13)/2112355(13)       normal                   2409                0           0             0         0
INC :                         IPv6    no    6462ed4390b9c40f    1                   3061361(9)/2887251(13)        normal                   3130                0           0             0         0
INC :                         IPv6    no    fbe6ab466e2cc94e    1                   8190820(7)/8056261(7)         normal                   9479                0           0             0         0
OUT :                         IPv6    no    f39c9b0803a808f5    1                   12175537(13)/12685845(3)      normal                   16047               0           0             0         0
INC :                         IPv6    no    ad5f30519e65c472    1                   18722655(10)/18278745(13)     normal                   25079               0           0             0         1

marco@boldsuck2:~$ monerod --rpc-bind-port=8081 print_cn | grep IPv6
INC :                         IPv6    no    fbe6ab466e2cc94e    1                   128528(0)/139627(0)           normal                   156                 0           1             0         0
OUT :                         IPv6    no    71ebf0d42f511a38    1                   1238675(0)/1240262(0)         normal                   1263                0           0             0         0
INC :                         IPv6    no    d752fad99e6821ad    1                   842828(0)/834662(0)           normal                   761                 1           0             1         0
INC :                         IPv6    no    8615d8f13f9db3f5    1                   7904802(3)/7596024(13)        normal                   9076                0           0             0         0
INC :                         IPv6    no    6db01b6b0729252d    1                   10100052(2)/10010134(12)      normal                   12384               0           0             0         0
INC :                         IPv6    no    71ebf0d42f511a38    1                   12694127(2)/12183078(0)       normal                   16065               0           0             0         0
INC :                         IPv6    no    ad5f30519e65c472    1                   23487750(0)/22208378(9)       normal                   32377               0           1             0         0

user@tor-proxy-00:~$ monerod --rpc-bind-port=8081 print_cn | grep IPv6
INC :                         IPv6    no    37248f7ff5715720    1                   461716(4)/459349(4)           normal                   541                 0           0             0         1
INC :                         IPv6    no    d752fad99e6821ad    1                   530791(3)/541561(2)           normal                   604                 0           0             0         1
OUT :                         IPv6    no    f39c9b0803a808f5    1                   139627(7)/130115(2)           normal                   163                 0           0             0         0
OUT :                         IPv6    no    71ebf0d42f511a38    1                   8066024(6)/8202223(1)         normal                   9500                0           0             0         0
INC :                         IPv6    no    ad5f30519e65c472    1                   23242715(3)/22580314(3)       normal                   31972               0           0             0         1
INC :                         IPv6    no    a986bbf685b22d34    1                   70679524(4)/78054807(5)       normal                   61071               1           0             1         1
INC :                         IPv6    no    8c6d9506ef3c9b39    1                   141750244(2)/137792766(4)     normal                   132334              1           0             1         1

user@crypto-01:~$ monerod --rpc-bind-port=8081 print_cn | grep IPv6
OUT :                         IPv6    no    f39c9b0803a808f5    1                   10017012(10)/10105448(6)      normal                   12396               0           1             0         0
INC :                         IPv6    no    a986bbf685b22d34    1                   63648370(5)/67514279(7)       normal                   49196               1           0             1         1
INC :                         IPv6    no    979f82daaebd5508    1                   11294842(41129)/10309057(40992)normal                   55188               0           50            0         7
```

## deavmi | 2024-02-24T21:27:28+00:00
Shit needs v6 by default. What era we living in>

## shortwavesurfer2009 | 2024-03-23T20:53:08+00:00
So my v4 is cgnat with no ability to port forward. I have 18080 and 18089 forwarded for p2p and restricted rpc but have 0 in connections for days. Issueing status gets me `Height: 3111599/3111599 (100.0%) on mainnet, not mining, net hash 2.01 GH/s, v16, 11(out)+0(in) connections, uptime 2d 5h 50m 15s`

Edit: incoming RPC connections on v6 work perfectly, but no peers for inbound p2p

## nice42q | 2024-04-08T17:50:02+00:00
> So my v4 is cgnat with no ability to port forward. I have 18080 and 18089 forwarded for p2p and restricted rpc but have 0 in connections for days. Issueing status gets me `Height: 3111599/3111599 (100.0%) on mainnet, not mining, net hash 2.01 GH/s, v16, 11(out)+0(in) connections, uptime 2d 5h 50m 15s`
> 
> Edit: incoming RPC connections on v6 work perfectly, but no peers for inbound p2p

I have the same problem with the connection.

## 86dd | 2024-08-11T22:41:57+00:00
I am now running some IPv6 Ready monerod nodes if anyone wants to peer.
https://julias.zone/p2p/
Sadly, not much IPv6 activity, except for the nodes I explicitly defined.

## 86dd | 2024-08-11T23:33:26+00:00
Also, monero gui seems to only try resolving IPv4. To connect to an IPv6 node (For example from IPv6 only network) you need to specify IPv6 literals... One should do IPv6 first, then after a few hundred ms try IPv4, like happy eyeballs.
And maybe detect NAT64 prefix using ipv4only.arpa IN AAAA.
```
01:31:20.233506 IP6 2a02:810d:b5bf:ec20::2.50711 > 2a02:810d:b5bf:ec20::1.53: 27511+ A? xmr1.julias.zone. (34)
01:31:20.237922 IP6 2a02:810d:b5bf:ec20::1.53 > 2a02:810d:b5bf:ec20::2.50711: 27511 1/0/0 A 77.22.157.203 (50)
```

## 86dd | 2024-08-12T05:15:30+00:00
Also, I can't seem to see monerod making DNS lookups over IPv6... only ever tries IPv4 for some reason to some random DNS recursors including my DNS recursor, even though I configured IPv6 resolvers in systemd-networkd etc...

## thisIsNotTheFoxUrLookingFor | 2024-08-24T15:10:02+00:00
> Also, I can't seem to see monerod making DNS lookups over IPv6... only ever tries IPv4 for some reason to some random DNS recursors including my DNS recursor, even though I configured IPv6 resolvers in systemd-networkd etc...

Hello I am trying to peer to you via IPv6 I have resolved IPv6 of both your nodes.

I have added in my config file
```
p2p-bind-ip=0.0.0.0
p2p-bind-ipv6-address=::
p2p-bind-port=18080
p2p-use-ipv6=1
add-priority-node=[2a02:810d:b5bf:ece0::1:180]:18080
add-priority-node=[2a01:4f8:a0:3800::7]:18080
```

But I do a `get_connections` to my RPC and I only have IPv4 and .onion peers no IPv6 at all.

When I `netstat -a | grep 18080` monerod is definitely listening on IPv6 address

```
tcp        0      0 0.0.0.0:18080           0.0.0.0:*               LISTEN     
tcp        0      0 2f829fce9361:18080      119.130.159.155:34997   ESTABLISHED
tcp        0      0 2f829fce9361:18080      120.229.38.17:21018     ESTABLISHED
tcp        0      0 2f829fce9361:18080      nat.exodus-stage.:57678 ESTABLISHED
tcp6       0      0 [::]:18080              [::]:*                  LISTEN   
```
Seems like maybe P2P by IPv6 is broken?

## thisIsNotTheFoxUrLookingFor | 2024-08-24T15:29:00+00:00
Ahah!

I had `proxy=127.0.0.1:9050` in my conf so I guess all connections were being forced to IPv4 and proxied through Tor. Disabling this line sees IPv6 connection to your nodes now.

Changing to  `proxy=[::1]:9050` does not seem to allow IPv6 connections either, have to not proxy through Tor I guess. I have tx-proxy for Tor still though.

**Edit**

This is why, `proxy` is SOCKS4 https://github.com/monero-project/monero/issues/9390#issuecomment-2198622339

## 86dd | 2024-09-08T13:14:03+00:00
Looks like `anonymous-inbound` doesn't work with `*.onion:18083,[::1]:18083,100`.
Same for `tx-proxy` as it also doesn't work with `tor,[::1]:9050,16`.
Changing those from IPv6 to 127.0.0.1 did work however.
I also cannot use like `xmr*.*.onion`, it only takes `*.onion`. Seems like it does some splitting on `.` and then doesn't get `onion` back when I prefix the .onion with something...
I think this has to do with https://github.com/monero-project/monero/issues/9390#issuecomment-2198622339


## vtnerd | 2024-09-08T13:58:48+00:00
You cannot connect to IPv6 addresses over a proxy until #9443 gets merged.

## boldsuck | 2024-09-09T15:46:35+00:00
When #9443 gets merged.
Remember SocksPort and HiddenService in torrc must be dualstack, if it is not already. ;-)

## thisIsNotTheFoxUrLookingFor | 2024-09-10T01:05:05+00:00
> You cannot connect to IPv6 addresses over a proxy until #9443 gets merged.

Thanks @vtnerd very much looking forward to this!

## thisIsNotTheFoxUrLookingFor | 2024-09-10T01:06:28+00:00
> When #9443 gets merged. Remember SocksPort and HiddenService in torrc must be dualstack, if it is not already. ;-)

Do we make hidden service dual stack by utilising `[::1]:18083` for example?

## boldsuck | 2024-09-10T16:55:57+00:00
Yes, I separated P2P and RPC. You can also put both ports in one HiddenServiceDir.
And I always set allow/deny policy on Socks or MetricsPort.

```
SocksPolicy accept 127.0.0.1
SocksPolicy accept6 [::1]
SocksPolicy reject *
```
```
# Monero incoming P2P anonymity connections
HiddenServiceDir /var/lib/tor/monero-node/
HiddenServicePort 18083 127.0.0.1:18083
HiddenServicePort 18083 [::1]:18083

# Monero incoming RPC anonymity connections
HiddenServiceDir /var/lib/tor/monero-service/
HiddenServicePort 18081 127.0.0.1:18081
HiddenServicePort 18081 [::1]:18081
```


## thisIsNotTheFoxUrLookingFor | 2024-09-10T22:10:10+00:00
> Yes, I separated P2P and RPC. You can also put both ports in one HiddenServiceDir. And I always set allow/deny policy on Socks or MetricsPort.
> 
> ```
> SocksPolicy accept 127.0.0.1
> SocksPolicy accept6 [::1]
> SocksPolicy reject *
> ```
> 
> ```
> # Monero incoming P2P anonymity connections
> HiddenServiceDir /var/lib/tor/monero-node/
> HiddenServicePort 18083 127.0.0.1:18083
> HiddenServicePort 18083 [::1]:18083
> 
> # Monero incoming RPC anonymity connections
> HiddenServiceDir /var/lib/tor/monero-service/
> HiddenServicePort 18081 127.0.0.1:18081
> HiddenServicePort 18081 [::1]:18081
> ```

Thank you, yea I am doing very similar I am restricting the socks interface to my LAN and Docker bridge, but I am using the same hidden service for P2P and RPC Restricted, I could split them but meh.

## 86dd | 2025-05-21T16:51:58+00:00
Another issue:
If you try to set DNS_PUBLIC to your own local DNS resolvers, like 2001:db8::2 it will fail, because there is an IPv4 only check hardcoded and it calls your IPv6 address an invalid "IP" address.
(I would not use IP to only refer to IPv4! There are two versions of the internet protocol.)
https://github.com/monero-project/monero/blob/125622d5bdc42cf552be5c25009bd9ab52c0a7ca/src/common/dns_utils.cpp#L568-L595
I would rather rely on a networking library to do the proper IP (as in IPv4+IPv6) address check, or update the function, but it can be a bit more complex on IPv6.
(Somehow 0x1010101 or 16843009 would also be an invalid IP(v4) despite them being pingable...)
And it would also be cool to support udp:// I guess.

## hhartzer | 2025-12-29T16:46:46+00:00
I've added @boldsuck's two peers as priority. I see with netstat that connection is established, but it won't sync. Has anyone else had this problem?

Edit: It seems like this is a Monero+OpenBSD+IPv6 issue. On Linux I'm able to make this work.

# Action History
- Created by: 86dd | 2023-04-04T13:46:41+00:00
