---
title: 'I2P: no incoming connections created'
source_url: https://github.com/monero-project/monero/issues/7885
author: xanoni
assignees: []
labels: []
created_at: '2021-08-20T02:13:48+00:00'
updated_at: '2025-12-28T22:43:36+00:00'
type: issue
status: closed
closed_at: '2025-12-28T22:42:53+00:00'
---

# Original Description
Continuation of this ticket here: https://github.com/monero-project/monero/issues/7863 (if I forgot info, it's probably there)

TL;DR: Node only has the below types of connections:

- Outgoing: IP, Tor, I2P
- Incoming: Tor

The lack of incoming IP connections is expected and desired. Lack of incoming I2P is to be explained.

**Settings / Version:**

`Monero 'Oxygen Orion' (v0.17.2.0-release)` with the below key settings:
```
tx-proxy=i2p,127.0.0.1:4447,25
tx-proxy=tor,127.0.0.1:9050,25

anonymous-inbound=XYZ.b32.i2p:12349,127.0.0.1:18087,25 # `i2pd` tunnel was defined manually
anonymous-inbound=XYZ.onion:2837,127.0.0.1:18088,25

# settings equivalent to the below also used for RPC 
p2p-ignore-ipv4=1
p2p-use-ipv6=0
p2p-bind-ip=127.0.0.1
p2p-bind-port=18080

hide-my-port=0 # think this is needed to get incoming anon connections
public-node=0
no-igd=1
allow-local-ip=1 # why not
no-zmq=1

# also added several Tor peers (not shown)
add-priority-node XYZ.b32.i2p:0
add-priority-node XYZ.b32.i2p:0
[...]
add-priority-node XYZ.b32.i2p:0
```

Tunnel config (confirmed that it's getting loaded and that the dest is created by `i2pd`):
```bash
~# cat /etc/i2pd/tunnels.conf.d/xmr.conf
[MONEROD-P2P]
type = server
host = 127.0.0.1
port = 18087
inport = 12349
keys = xmr-keys.dat
inbound.quantity = 64
outbound.quantity = 64
```

Ideas?

# Discussion History
## selsta | 2021-08-26T23:59:06+00:00
Did you regularly check? I don't think there are too many I2P connections used currently, most use Tor.

## xanoni | 2021-08-27T01:08:54+00:00
> Did you regularly check? I don't think there are too many I2P connections used currently, most use Tor.

Yup. I2P is always 100% outgoing. It's usually 10-15 outgoing connections for I2P.

Tor on the other hand has more incoming than outgoing connections, but there are always both types.

I noticed that `hide-my-port=0/1` doesn't seem to make a difference. That's probably just for IP (should be explained somewhere).

## selsta | 2021-08-27T01:12:49+00:00
Did you test with i2p-zero? So that you can make sure it isn't i2pd config related.

## xanoni | 2021-08-27T02:44:41+00:00
> Did you test with i2p-zero? So that you can make sure it isn't i2pd config related.

Nope, net yet. But if someone who knows i2pd better could check my i2pd config above, that would also be helpful.

## xanoni | 2021-08-29T04:30:47+00:00
FYI, this is what it usually looks like. **I highlighted all incoming connections,** you'll see that it's just Tor (IPv4/IPv6 is filtered). Haven't tested i2p-zero, yet. **_EDIT: _** i2p-zero doesn't seem to exist for ARM... but I guess I could try regular i2p... but not sure I want to :) i2pd works fine with bitcoind.

This is with these settings:
- tx-proxy=i2p,127.0.0.1:4447,**40**
- tx-proxy=tor,127.0.0.1:9050,**40**
- anonymous-inbound=XYZ.onion:$PORT,127.0.0.1:$PORT,**40**
- anonymous-inbound=ZYX.b32.i2p:$PORT,127.0.0.1:$PORT,**40**
- out_peers=20 # this is just IPv4/IPv6, for block downloads
- in_peers=0 # filtered

![image](https://user-images.githubusercontent.com/77220130/131238393-0b210b81-3410-478d-9b46-c3ce3c4d6fa6.png)


## jbakosi | 2022-08-21T14:17:35+00:00
I think I am getting incoming i2pd p2p connections with this setup:

monerod.conf
```
data-dir=/opt/monero
log-file=/opt/monero/monerod.log
log-level=0
p2p-bind-ip=127.0.0.1
p2p-bind-port=18080
rpc-restricted-bind-ip=0.0.0.0
rpc-restricted-bind-port=18089
zmq-rpc-bind-ip=0.0.0.0
zmq-rpc-bind-port=18082
out-peers=64
in-peers=1024

tx-proxy=i2p,127.0.0.1:4447
anonymous-inbound=iwliolsvujhespetsl3h3vv5uw4dfwqlce2irv3gqs7knclmhd7q.b32.i2p,127.0.0.1:8061
```
i2pd tunnels.conf:
```
[MONEROD-P2P]
type = server
host = 127.0.0.1
port = 8061
keys = monerod-rpc-keys.dat
```
```sh
$ monerod status
2022-08-21 14:14:15.452	I Monero 'Fluorine Fermi' (v0.18.1.0-release)
Height: 2694495/2694495 (100.0%) on mainnet, not mining, net hash 2.52 GH/s, v16, 64(out)+0(in) connections, uptime 0d 7h 42m 29s
$ monerod print_cn | grep -i i2p
INC :                         I2P     no    0000000000000001    0                   46831(7)/18956(7)             normal                   2451                0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   507150(46)/16291(46)          normal                   2879                0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   44582(39)/275880(5)           normal                   4975                0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   386042(35)/37653(35)          normal                   6987                0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   46191(10)/282946(4)           normal                   7288                0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   496337(7)/63772(34)           normal                   10481               0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   46140(25)/368146(25)          normal                   7348                0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   77406(12)/629710(12)          normal                   10484               0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   44780(46)/438601(49)          normal                   10795               0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   963766(10)/76482(10)          normal                   12973               0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   127490(49)/1391714(49)        normal                   26077               0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   581776(9)/18383(49)           normal                   4262                0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   93000(49)/1518566(49)         normal                   26687               0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   98263(48)/1489534(49)         normal                   27237               0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   400545(48)/62563(49)          normal                   15107               0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   111849(49)/18751(49)          normal                   3038                0           0             0         0            
INC :                         I2P     no    0000000000000001    0                   1378452(48)/116872(49)        normal                   27297               0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   187138(34)/1642888(34)        normal                   27233               0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   88961(49)/1243454(49)         normal                   27533               0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   43398(48)/11636(49)           normal                   1304                0           0             0         0            
OUT :                         I2P     no    0000000000000001    0                   96693(48)/454680(48)          normal                   27639               0           0             0         0        
$  monerod print_pl white | grep i2p
white      0000000000000001          3jkxk2gc4ky2l4j4wh66ipehbsy5trcwijsymjmgliglo6gzg3oa.b32.i2p:21301:0 -     -     0    d0.h15.m10.s31
white      0000000000000001          3kjgczoqw4c2vx4753754ew2utoqoool3jfbusqlxh7jasc6mzxq.b32.i2p:0 -     -     180  d0.h2.m8.s9
white      0000000000000001          3kjgczoqw4c2vx4753754ew2utoqoool3jfbusqlxh7jasc6mzxq.b32.i2p:18080:0 -     -     180  d0.h6.m38.s21
white      0000000000000001          4nunfpng5bqtjnkizjrten7lahoeml5442fpapqsz2x7h2n4edva.b32.i2p:18088:0 -     -     0    d0.h0.m1.s12
white      0000000000000001          4xhgs65kvxxrs6qnpmpmg746vhdb2us6fl7utsdxd7ipu66rywwa.b32.i2p:0 -     -     0    d0.h16.m32.s35
white      0000000000000001          4xhgs65kvxxrs6qnpmpmg746vhdb2us6fl7utsdxd7ipu66rywwa.b32.i2p:18080:0 -     -     0    d0.h1.m26.s53
white      0000000000000001          5wmqpuvbomvppsuwndq742xltmv7sxuan6asvgqdmrlx7mycjx2q.b32.i2p:0 -     -     180  d0.h3.m2.s16
white      0000000000000001          6z3tnxs7ruiufxblutjvxegxuc2yyg75w3eurhusvfbbpdgxalya.b32.i2p:18089:0 -     -     0    d0.h15.m10.s31
white      0000000000000001          6zwb3bzitlcjn54mfqmlnkte6indjyuifxqvetreq5gzytm327qq.b32.i2p:18080:0 -     -     0    d0.h4.m48.s38
white      0000000000000001          7ncin2lc23pbbew45gvqrch6vo3e366esbtdkrysualyshuxsmra.b32.i2p:18088:0 -     -     0    d0.h0.m1.s12
white      14de9a61c7d9a3e4          core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p:18080:0 -     -     0    never
white      ab13b3121c8dc047          dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p:18080:0 -     -     0    never
white      0000000000000001          ee6mzvf3vuclyrji3wb6ymkqnjgmhtqyx7sy7723532dfhyoqqwq.b32.i2p:0 -     -     0    d0.h17.m31.s9
white      0000000000000001          ee6mzvf3vuclyrji3wb6ymkqnjgmhtqyx7sy7723532dfhyoqqwq.b32.i2p:18080:0 -     -     0    d0.h17.m30.s30
white      0000000000000001          ee6mzvf3vuclyrji3wb6ymkqnjgmhtqyx7sy7723532dfhyoqqwq.b32.i2p:29700:0 -     -     0    d0.h0.m1.s13
white      0000000000000001          fylbfwok5xqo4lyz3yodqroiegw2al66acggwmxmiy7h5mxqpwda.b32.i2p:0 -     -     180  d0.h5.m45.s55
white      0000000000000001          gaymspfzeg6wubotk653ejiwxtmjunjsflrrbhpv3u34eheufvda.b32.i2p:0 -     -     0    d0.h2.m8.s7
white      0000000000000001          gaymspfzeg6wubotk653ejiwxtmjunjsflrrbhpv3u34eheufvda.b32.i2p:18081:0 -     -     0    d0.h4.m5.s2
white      0000000000000001          gaymspfzeg6wubotk653ejiwxtmjunjsflrrbhpv3u34eheufvda.b32.i2p:18084:0 -     -     0    d0.h2.m8.s7
white      0000000000000001          jl4gghrtmrs64i6rurwpzpwn25ij2xdtzhq3qs4rrf7hh6td5txa.b32.i2p:0 -     -     0    d0.h0.m34.s57
white      0000000000000001          jrem7aeisrukkalxksznskxp7y6dwqwrd7hw7x4dx7wao26a5tla.b32.i2p:18088:0 -     -     0    d0.h0.m1.s13
white      0000000000000001          jtnfklxptqoyjnd3x5e7x25btn24ucxp3xe5t75vteagauxfcd6a.b32.i2p:18088:0 -     -     0    d0.h0.m1.s13
white      0000000000000001          knpdzlkfhsk5vfxynywsi3v7y55nf5i7r5vjkgulzf2f74y5l52q.b32.i2p:0 -     -     0    d0.h15.m10.s31
white      0000000000000001          moneroti7lckp4hjrqckoq5cfi2apuyxia42sp5x7tkbzjfwqfiq.b32.i2p:18080:0 -     -     0    d0.h6.m2.s27
white      0000000000000001          pxtsal53b6blcxodaje4el2ajjesszfqhiig4r2dbb6bylf76m4a.b32.i2p:28082:0 -     -     0    d0.h0.m1.s12
white      0000000000000001          r4s6xrdypmkjoeb4vv3ss2vy7n5bzu4dc3hip7gweoob73jdoota.b32.i2p:0 -     -     0    d0.h0.m1.s10
white      0000000000000001          rrr6uqtvt4whli6r2cp4coulcd5z6k27c6kejoggsrejk5yv5luq.b32.i2p:18080:0 -     -     0    d0.h0.m1.s13
white      0000000000000001          s3l6ke4ed3df466khuebb4poienoingwof7oxtbo6j4n56sghe3a.b32.i2p:0 -     -     0    d0.h17.m31.s9
white      0000000000000001          s3l6ke4ed3df466khuebb4poienoingwof7oxtbo6j4n56sghe3a.b32.i2p:18080:0 -     -     0    d0.h16.m32.s37
white      0000000000000001          s3l6ke4ed3df466khuebb4poienoingwof7oxtbo6j4n56sghe3a.b32.i2p:28081:0 -     -     0    d0.h0.m1.s13
white      0000000000000001          sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p:0 -     -     180  d0.h1.m5.s48
white      0000000000000001          sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p:18080:0 -     -     180  d0.h16.m3.s56
white      4268a937101b2003          spn4ef3gddveqxkco6fhh7epyxnvdmei4w6hioiiunfvvljxgcoa.b32.i2p:18080:0 -     -     0    never
white      0000000000000001          vru4v4tbsdxx5l2n5upqortuo6h7knzdcnyerlnip6kwfjzroeyq.b32.i2p:0 -     -     0    d0.h4.m20.s53
white      0000000000000001          vru4v4tbsdxx5l2n5upqortuo6h7knzdcnyerlnip6kwfjzroeyq.b32.i2p:8061:0 -     -     0    d0.h0.m32.s30
white      0000000000000001          whd7p6ah6wmfdhhdfo7i5e4x3dj3gpswpn5vs2ovmgunyj34pmbq.b32.i2p:0 -     -     0    d0.h0.m1.s13
white      0000000000000001          wqcbpmrlvulvhv7vn4r6jbx7d6qgodvh676amtlynn5eg32umc4q.b32.i2p:0 -     -     182  d0.h5.m24.s14
white      0000000000000001          wqcbpmrlvulvhv7vn4r6jbx7d6qgodvh676amtlynn5eg32umc4q.b32.i2p:18080:0 -     -     182  d0.h1.m8.s30
white      0000000000000001          wxpymgbovamvpymrelw7bqocjgib6n6otxzn6fuy3nt5rn64de2q.b32.i2p:18080:0 -     -     0    d0.h15.m10.s31
white      0000000000000001          x3wuvir7uv37k4scw2pcjymajbcwcungc5zo5x6yicwaqr4pnizq.b32.i2p:0 -     -     185  d0.h0.m1.s13
white      0000000000000001          xmr3dasxv7merbnfd7xigwxsv7lw6so62ejjuc6hd6szhh5lqwsq.b32.i2p:0 -     -     0    d0.h0.m1.s13
white      e9e467a3b55bbeb0          yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p:18080:0 -     -     0    never
$ i2pd --version
i2pd version 2.36.0 (0.9.49)
Boost version 1.74.0
OpenSSL 1.1.1j  16 Feb 2021
```

## selsta | 2025-12-28T22:43:36+00:00
There are no known issues with i2pd and incoming connections in the latest version.

# Action History
- Created by: xanoni | 2021-08-20T02:13:48+00:00
- Closed at: 2025-12-28T22:42:53+00:00
