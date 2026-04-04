---
title: Monerod is stuck while synchronizing
source_url: https://github.com/monero-project/monero/issues/8759
author: meyou69
assignees: []
labels: []
created_at: '2023-03-03T13:16:51+00:00'
updated_at: '2023-03-03T20:42:50+00:00'
type: issue
status: closed
closed_at: '2023-03-03T20:42:50+00:00'
---

# Original Description
I'm currently running the monerod executable (version 0.18.1.2-release) on an x86-64 Arch linux server in headless mode.

The node was fully synchronized with the network and everything worked just fine until yesterday when suddenly, it got behind the blockchain with 1 or 2 blocks. It started synchronizing with the peers to retrieve those blocks but it never continued to function afterwards. When trying to connect my wallets to it, the wallets attempt to connect to it but the server doesn't seem to respond. It's stuck in a synchronization step and it doesn't seem to finish it.

The program is run as a systemd service with the following ExecStart entry:

ExecStart=/usr/local/bin/monerod --log-level=2 --config-file=/etc/monero/monerod.conf --pidfile /var/run/monero/monero.pid --zmq-pub tcp://127.0.0.1:18083 --out-peers 64 --in-peers 32 --add-priority-node=node.supportxmr.com:18080 --add-priority-node=nodes.hashvault.pro:18080 --disable-dns-checkpoints --enable-dns-blocklist --non-interactive

The reason there's the zmq protocol activated is because I'm also running p2pool over it, in the background.

Things I tried to get it unstuck (none of them worked):

1. Restarted the systemd service
2. Reboot the machine
3. Removed the peers cache file p2pstate.bin and restarted the systemd service again

The contents of monerod.conf are the following:

```
# /etc/monero/monerod.conf

# Data directory (blockchain db and indices)
data-dir=/big-storage/monero/.bitmonero  # Remember to create the monero user first

# Log file
log-file=/var/log/monero/monerod.log

# P2P configuration
p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
p2p-bind-port=18080            # Bind to default port
p2p-bind-ipv6-address=::
p2p-bind-port-ipv6=18080
p2p-use-ipv6=1

# RPC configuration
public-node=1                             # Advertise the RPC-restricted port over p2p peer lists
rpc-restricted-bind-ip=0.0.0.0            # Bind restricted RPC to all interfaces
rpc-restricted-bind-port=18089            # Bind restricted RPC on custom port to differentiate from default unrestricted RPC (18081)
confirm-external-bind=1                   # Open restricted RPC node (confirm)
no-igd=1                                  # Disable UPnP port mapping

# CUSTOM: enable IPv6
rpc-restricted-bind-ipv6-address=::1
rpc-use-ipv6=1

# ZMQ configuration
#no-zmq=1

# Block known-malicious nodes from a DNSBL
enable-dns-blocklist=1

# Set download and upload limits, if desired
# limit-rate-up=128000 # 128000 kB/s == 125MB/s == 1GBit/s; a raise from default 2048 kB/s; contribute more to p2p network
# limit-rate-down=128000 # 128000 kB/s == 125MB/s == 1GBit/s; a raise from default 2048 kB/s; contribute more to p2p network
```
I considered the possibility that it was due to poor network speed but I let the server run overnight and checked it again and it's still hanging. I don't think it's normal to take this long to download a 2 blocks.

I'll also attach the log file although this is only partial, as I activated verbose level 2, which made the log be extremely heavy and I had to cut out some contents.

[monerod.log](https://github.com/monero-project/monero/files/10882272/monerod.log)

If the logging level is too verbose, please let me know and I'll reduce it

# Discussion History
## selsta | 2023-03-03T18:31:52+00:00
Can you post the output of

"status" and "sync_info"

and then wait 20 minutes and post the same output again of both commands?

Also is `big_storage` a network storage?

## meyou69 | 2023-03-03T20:34:13+00:00
Before the 20 minute wait:

status output:
2023-03-03 20:03:09.238 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Height: 2834139/2834139 (100.0%) on mainnet, not mining, net hash 2.56 GH/s, v16, 64(out)+32(in) connections, uptime 0d 7h 22m 26s

sync_info output
```
2023-03-03 20:03:37.536 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Height: 2834139, target: 2834139 (100%)
Downloading at 40 kB/s
94 peers
Remote Host                        Peer_ID   State   Prune_Seed          Height  DL kB/s, Queued Blocks / MB
78.198.23.131:35896       23ddf029506a0d04  normal            180       2834139  2 kB/s, 0 blocks / 0 MB queued
188.165.183.101:18080     98e1b5f91a8eb50f  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
45.77.127.20:18180        2c4bded2d9d746fd  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
152.169.168.224:18080     34bd29eef84c42f4  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
185.56.83.83:38628        e8f8aa22a5c65895  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
198.1.231.6:18080         0d6c54ade62147f6  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
185.41.68.106:18080       66d38a1b73e4b97a  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
121.201.18.35:47492       3cabe063763c4bbf  normal            180       2834139  0 kB/s, 0 blocks / 0 MB queued
94.112.168.129:51562      adc3db509a3edf25  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
80.241.217.144:18080      0ae325aad4556045  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
206.189.76.124:18080      0431076923725203  normal            182       2834139  0 kB/s, 0 blocks / 0 MB queued
173.50.83.166:50034       7d4058548d6e6ab8  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
123.195.45.19:41482       f950cce5982955a1  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
5.146.248.176:57528       3e4a3baf64051533  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
98.216.239.226:18080      13add45e60588885  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
81.217.189.90:42498       83b1b882e3b8bc3f  normal            181       2834139  0 kB/s, 0 blocks / 0 MB queued
3.234.177.79:18080        e12e610f133e18a8  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
98.63.48.247:18080        88ef0b2710bd06b4  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
51.38.53.106:18080        e6093b1f42f1a3cf  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
168.119.58.31:46410       6dbf803f898f022d  normal            181       2834139  0 kB/s, 0 blocks / 0 MB queued
104.191.84.34:41848       da5c2fb305e424c7  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
73.139.90.249:18080       0d5a7835cb23ff7d  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
146.70.179.26:49290       932357cb0598d018  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
74.15.120.98:18080        f256301a3c179f75  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
45.78.183.59:3712         57998627631e9be7  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
85.14.254.23:44802        05c2257580791fe7  normal            185       2834139  0 kB/s, 0 blocks / 0 MB queued
73.110.151.82:18080       617302414e3d4eca  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
68.115.93.16:18080        edc60cf4fca8416f  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
74.14.31.41:18080         85f90fd98b18134d  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
161.35.103.143:18080      7adea320334da83f  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
70.163.206.194:18080      47351cbc497569a4  normal            182       2834139  0 kB/s, 0 blocks / 0 MB queued
134.122.50.39:44734       843247872a4aec65  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
185.203.56.7:18080        2df9d5b474841481  normal            185       2834139  2 kB/s, 0 blocks / 0 MB queued
5.189.187.89:18080        c366bf430396c907  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
144.217.81.221:54236      eedddaaea31ba169  normal            181       2834139  0 kB/s, 0 blocks / 0 MB queued
163.41.113.199:10050      c7a6d8a09c1d42d3  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
98.41.179.179:18080       c2caf4121fa03bad  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
217.138.252.228:42252     14a58f9ce45ca083  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
208.64.230.6:18080        82ac1c585de6e093  normal            183       2834139  0 kB/s, 0 blocks / 0 MB queued
46.22.40.159:18080        370c501bc234ab63  normal            187       2834139  0 kB/s, 0 blocks / 0 MB queued
24.191.230.137:18080      addb1d8a2b61d536  normal            181       2834139  0 kB/s, 0 blocks / 0 MB queued
92.117.38.101:18080       0ce561c7370d344f  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
161.97.166.49:36894       4ffa1b7a7b4c3048  normal            182       2834139  0 kB/s, 0 blocks / 0 MB queued
185.240.242.36:18080      c3f33cd49740fde1  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
47.55.110.17:18080        9c94ad0d4cedd251  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
60.242.213.123:18080      ce1b16dc016c1146  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
45.129.56.200:55176       fc66df1d2e61f161  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
141.94.218.175:18080      0b8c20807e941855  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
144.217.181.208:18080     8562417c4f4b69e8  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
212.41.9.32:18080         7ca9ad24683cc289  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
91.209.70.35:18080        b9e2dd0356608e76  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
109.155.198.145:18080     cbe2bac186b08bd6  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
46.32.46.171:18080        07648b7b4eadeac2  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
85.214.142.120:18080      6c40d38c7d334c24  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
84.237.229.84:18090       1190cad33313ab10  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
208.167.255.10:18080      e797d6da6c87c79f  normal            186       2834139  1 kB/s, 0 blocks / 0 MB queued
217.251.91.37:33082       8adf3c6323efc06d  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
194.67.208.191:18080      ce58335de15986f9  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
97.126.17.72:18080        6e37e4f88e1cca95  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
178.249.214.10:61254      cb39602551a72c19  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
116.202.170.226:47042     156f74a3569f3c80  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
77.24.114.229:18080       87cb198dce917c43  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
45.159.188.98:18080       398d19210f50018f  normal            0         1  0 kB/s, 0 blocks / 0 MB queued
3.217.133.209:63638       fb2d3c334e8c044b  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
88.198.22.229:18080       311e7ea273b9fe18  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
166.70.240.22:18080       65d24c973d223e76  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
119.17.158.221:18080      a3d5655fc8ae97d2  normal            184       2834139  2 kB/s, 0 blocks / 0 MB queued
216.177.227.214:18080     304788ec3ac5168c  normal            180       2834139  0 kB/s, 0 blocks / 0 MB queued
84.24.129.246:18080       219a6d81e61fd528  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
99.231.74.26:18080        bac5c24ef999f97a  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
109.248.206.13:18080      21f3487779bad2d9  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
23.137.250.141:18080      875702f0c1309976  normal            180       2834139  0 kB/s, 0 blocks / 0 MB queued
31.47.202.73:18080        fb5d04b5950c15f3  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
76.142.189.119:18080      9febaa0e1430df2d  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
51.195.237.138:18080      68b6f8c438f48ddf  normal            187       2834139  1 kB/s, 0 blocks / 0 MB queued
185.183.34.250:18080      30987d3ccc6f7876  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
49.12.86.248:36480        3960415dbb2dc3c3  normal            187       2834139  0 kB/s, 0 blocks / 0 MB queued
185.59.100.77:18080       4f6f2623433fb56d  normal            184       2834139  1 kB/s, 0 blocks / 0 MB queued
83.99.12.19:18080         5df9d59e4b932716  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
212.233.125.50:57876      c80d7de22f0a299d  normal            183       2834139  0 kB/s, 0 blocks / 0 MB queued
91.238.50.91:44832        971a33de9f64a9ef  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
58.248.107.189:18080      304b9bc525f5da1a  normal            0         1  0 kB/s, 0 blocks / 0 MB queued
71.94.168.116:18080       9bf7d39581b64084  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
37.187.142.2:18080        a3f409f4e5dd9aaa  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
77.57.219.55:18080        bc565e0b74387b84  normal            0         2377920  0 kB/s, 0 blocks / 0 MB queued
155.138.134.171:18080     aaa32c7854b84de5  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
198.54.130.94:35226       817c063e1b98beda  normal            186       2834139  0 kB/s, 0 blocks / 0 MB queued
168.119.166.230:52978     d3376834f24cdf39  normal            0         2834139  2 kB/s, 0 blocks / 0 MB queued
213.136.71.55:52142       9b462722ab8a8e94  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
185.204.1.184:41490       cba1a7eb813723b8  normal            0         2834139  1 kB/s, 0 blocks / 0 MB queued
142.202.242.45:45692      422678b4f9cc6902  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
156.246.77.207:51450      251ba86d0a7a1428  normal            183       2834139  0 kB/s, 0 blocks / 0 MB queued
207.6.204.147:63931       74469a8603b54652  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
15.235.9.228:35840        c15820b90dbcef51  normal            0         2834139  0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
```

After the 20 minute wait:
status:
2023-03-03 20:31:57.827 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Height: 2834156/2834156 (100.0%) on mainnet, not mining, net hash 2.55 GH/s, v16, 64(out)+32(in) connections, uptime 0d 7h 51m 15s

sync_info:
```
2023-03-03 20:32:34.159 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Height: 2834157, target: 2834157 (100%)
Downloading at 0 kB/s
95 peers
Remote Host                        Peer_ID   State   Prune_Seed          Height  DL kB/s, Queued Blocks / MB
73.152.188.151:52244      357f1482103b196f  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
5.206.224.126:56370       50bc9e24b3ce9aaf  normal            181       2834156  0 kB/s, 0 blocks / 0 MB queued
94.198.43.62:59339        e78901bcab27e3aa  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
178.148.143.27:18080      f94e5faea815051a  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
163.172.90.168:18080      ddb8e25f38743387  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
174.16.64.5:36358         7e8dcf8e434f7a3c  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
51.195.237.138:18080      68b6f8c438f48ddf  normal            187       2834156  0 kB/s, 0 blocks / 0 MB queued
15.235.144.187:38972      77966524fd37e80b  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
138.201.125.152:18080     2940f44802c6abbd  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
207.173.21.234:48058      420312fe8c3af0d9  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
223.25.24.85:36318        aa06d3b39aa79b79  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
185.3.240.1:47075         d1698b91bd7bafcf  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
62.210.206.84:18080       6608998db22cd912  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
167.86.101.138:18080      dc61f1f40564dce9  normal            186       2834157  0 kB/s, 0 blocks / 0 MB queued
180.150.107.222:18080     231ef0263de9bc29  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
185.197.192.164:65502     5be5b0ef8806cdfb  normal            0         56508  0 kB/s, 0 blocks / 0 MB queued
95.217.36.126:54572       4b49fbbd0d54311f  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
78.198.23.131:35896       23ddf029506a0d04  normal            180       2834156  0 kB/s, 0 blocks / 0 MB queued
188.165.183.101:18080     98e1b5f91a8eb50f  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
45.77.127.20:18180        2c4bded2d9d746fd  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
152.169.168.224:18080     34bd29eef84c42f4  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
97.101.1.174:18080        a5e7cdd51e130f0d  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
198.1.231.6:18080         0d6c54ade62147f6  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
185.41.68.106:18080       66d38a1b73e4b97a  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
94.112.168.129:51562      adc3db509a3edf25  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
80.241.217.144:18080      0ae325aad4556045  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
206.189.76.124:18080      0431076923725203  normal            182       2834156  0 kB/s, 0 blocks / 0 MB queued
173.50.83.166:50034       7d4058548d6e6ab8  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
37.209.101.76:18080       a161e55dec337079  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
98.216.239.226:18080      13add45e60588885  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
81.217.189.90:42498       83b1b882e3b8bc3f  normal            181       2834157  0 kB/s, 0 blocks / 0 MB queued
3.234.177.79:18080        e12e610f133e18a8  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
95.228.214.121:18080      c407b84b39f456a5  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
98.63.48.247:18080        88ef0b2710bd06b4  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
107.213.91.83:18080       a6a6cbcefc0b0f84  normal            180       2834156  0 kB/s, 0 blocks / 0 MB queued
51.38.53.106:18080        e6093b1f42f1a3cf  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
73.139.90.249:18080       0d5a7835cb23ff7d  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
74.15.120.98:18080        f256301a3c179f75  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
45.78.183.59:3712         57998627631e9be7  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
85.14.254.23:44802        05c2257580791fe7  normal            185       2834157  0 kB/s, 0 blocks / 0 MB queued
73.110.151.82:18080       617302414e3d4eca  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
92.63.192.58:18080        6982d9eb6296a5a8  normal            180       2834157  0 kB/s, 0 blocks / 0 MB queued
68.115.93.16:18080        edc60cf4fca8416f  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
74.14.31.41:18080         85f90fd98b18134d  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
161.35.103.143:18080      7adea320334da83f  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
70.163.206.194:18080      47351cbc497569a4  normal            182       2834156  0 kB/s, 0 blocks / 0 MB queued
134.122.50.39:44734       843247872a4aec65  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
185.203.56.7:18080        2df9d5b474841481  normal            185       2834156  0 kB/s, 0 blocks / 0 MB queued
5.189.187.89:18080        c366bf430396c907  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
86.201.145.14:18080       3344f4a9cfae129b  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
144.217.81.221:54236      eedddaaea31ba169  normal            181       2834156  0 kB/s, 0 blocks / 0 MB queued
163.41.113.199:10050      c7a6d8a09c1d42d3  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
98.41.179.179:18080       c2caf4121fa03bad  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
208.64.230.6:18080        82ac1c585de6e093  normal            183       2834156  0 kB/s, 0 blocks / 0 MB queued
119.96.221.29:18080       9334cde950f5b4b4  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
168.119.58.31:50306       6dbf803f898f022d  normal            181       2834156  0 kB/s, 0 blocks / 0 MB queued
46.22.40.159:18080        370c501bc234ab63  normal            187       2834157  0 kB/s, 0 blocks / 0 MB queued
24.191.230.137:18080      addb1d8a2b61d536  normal            181       2834157  0 kB/s, 0 blocks / 0 MB queued
92.117.38.101:18080       0ce561c7370d344f  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
161.97.166.49:36894       4ffa1b7a7b4c3048  normal            182       2834156  0 kB/s, 0 blocks / 0 MB queued
185.240.242.36:18080      c3f33cd49740fde1  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
47.55.110.17:18080        9c94ad0d4cedd251  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
60.242.213.123:18080      ce1b16dc016c1146  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
45.129.56.200:55176       fc66df1d2e61f161  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
71.94.168.116:18080       9bf7d39581b64084  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
141.94.218.175:18080      0b8c20807e941855  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
181.44.117.9:10642        709b71b29ad1f742  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
5.78.45.245:47970         5bcbb6a3361c68e1  normal            181       2834156  0 kB/s, 0 blocks / 0 MB queued
144.217.181.208:18080     8562417c4f4b69e8  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
212.41.9.32:18080         7ca9ad24683cc289  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
91.209.70.35:18080        b9e2dd0356608e76  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
109.155.198.145:18080     cbe2bac186b08bd6  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
46.32.46.171:18080        07648b7b4eadeac2  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
85.214.142.120:18080      6c40d38c7d334c24  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
70.162.238.193:44236      09fadd436a8c64e6  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
84.237.229.84:18090       1190cad33313ab10  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
208.167.255.10:18080      e797d6da6c87c79f  normal            186       2834157  0 kB/s, 0 blocks / 0 MB queued
194.67.208.191:18080      ce58335de15986f9  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
64.201.122.243:54323      ad5af1cf2a339178  normal            185       2834156  0 kB/s, 0 blocks / 0 MB queued
97.126.17.72:18080        6e37e4f88e1cca95  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
178.249.214.10:61254      cb39602551a72c19  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
77.24.114.229:18080       87cb198dce917c43  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
45.159.188.98:18080       398d19210f50018f  normal            0         1  0 kB/s, 0 blocks / 0 MB queued
3.217.133.209:63638       fb2d3c334e8c044b  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
88.198.22.229:18080       311e7ea273b9fe18  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
166.70.240.22:18080       65d24c973d223e76  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
109.199.233.11:41314      9bcf0fc25d8dfe82  normal            182       2834156  0 kB/s, 0 blocks / 0 MB queued
91.238.50.91:44832        971a33de9f64a9ef  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
198.54.130.94:35226       817c063e1b98beda  normal            186       2834156  0 kB/s, 0 blocks / 0 MB queued
213.136.71.55:52142       9b462722ab8a8e94  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
185.204.1.184:41490       cba1a7eb813723b8  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
142.202.242.45:45692      422678b4f9cc6902  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
156.246.77.207:51450      251ba86d0a7a1428  normal            183       2834156  0 kB/s, 0 blocks / 0 MB queued
207.6.204.147:63931       74469a8603b54652  normal            0         2834156  0 kB/s, 0 blocks / 0 MB queued
15.235.9.228:35840        c15820b90dbcef51  normal            0         2834157  0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
```

No, big_storage is a silly name for a mount point for my SATA-connected hard disk drive.

## selsta | 2023-03-03T20:36:20+00:00
Both status updates show that you are fully synced and on the same height as your peers. What do you mean with stuck? Is the issue purely on the wallet side?

## meyou69 | 2023-03-03T20:41:43+00:00
Huh, this is strange.
I just opened Cake Wallet against my node just now, and it immediately started to sync with my node, even though up until now, the wallet would remain stuck on "Synchronizing".

The fact that it unfroze by itself is extremely strange.

Honestly, I don't know what could have caused it to work all of a sudden.

If you don't know what happened, we can just close this issue and dismiss it as a fluke

## selsta | 2023-03-03T20:42:50+00:00
You can open a new issue if the issue shows up again.

# Action History
- Created by: meyou69 | 2023-03-03T13:16:51+00:00
- Closed at: 2023-03-03T20:42:50+00:00
