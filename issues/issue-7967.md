---
title: Monero Wallet Gui downloads blockchain in spite of these preferred settings
source_url: https://github.com/monero-project/monero/issues/7967
author: ch9PcB
assignees: []
labels: []
created_at: '2021-09-23T02:56:08+00:00'
updated_at: '2021-09-23T13:08:50+00:00'
type: issue
status: closed
closed_at: '2021-09-23T13:08:50+00:00'
---

# Original Description
I always use the Tor Browser to download the pruned blockchain.

My current Monero Wallet Gui's version is 0.17.2.3 on Debian 11/Bullseye with the following options:

1. package tor is installed using Debian's official repositories but disabled by issuing the command: sudo service tor stop and verified by issuing the command: ss -nlt (confirmed that tor is not running)
2. After launching Monero Wallet Gui:
a. Under Settings --> Node --> Daemon startup flags --> --prune-blockchain --ban-list block.txt
b. Under Settings --> Node --> Bootstrap address is 127.0.0.1, Bootstrap port is 9150 (I use Tor Browser whose port is 9150. Tor's port is 9050, correct? But I stopped Tor's service as stated in (1) above.)
c. I have not even launched Tor Browser; yet the log showed otherwise (see below)

Question: How is it possible for Monero Wallet Gui to connect and download the pruned blockchain to my computer given the above settings? Is this a possible bug in the latest version of Monero Wallet Gui or is it by design?

```
[9/21/21 2:24 AM] 2021-09-21 02:24:40.044 I Monero 'Oxygen Orion' (v0.17.2.3-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[9/21/21 2:25 AM] 2021-09-21 02:25:11.265 I Monero 'Oxygen Orion' (v0.17.2.3-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[9/21/21 2:25 AM] 2021-09-21 02:25:14.645 I Monero 'Oxygen Orion' (v0.17.2.3-release)
Height: 2454814, target: 2455412 (99.9756%)
Downloading at 55 kB/s
3 peers
92.232.116.158:18080 f1301da7ef268b5a normal 0 1 1 kB/s, 0 blocks / 0 MB queued
178.63.100.197:18080 0f992957350f8d58 synchronizing 0 2455412 42 kB/s, 20 blocks / 0 MB queued
72.68.42.62:18080 64113358310cdaea synchronizing 0 2455412 12 kB/s, 20 blocks / 0 MB queued
2 spans, 0 MB
[..]
72.68.42.62:18080 20/187 (2454814 - 2454833) -
178.63.100.197:18080 20/187 (2454834 - 2454853) -
>>> sync_info
[9/21/21 2:25 AM] 2021-09-21 02:25:42.844 I Monero 'Oxygen Orion' (v0.17.2.3-release)
Height: 2454834, target: 2455413 (99.9764%)
Downloading at 1949 kB/s
7 peers
66.130.203.64:18080 3e7ef983a6451779 normal 185 2455413 151 kB/s, 21 blocks / 1.46355 MB queued
52.168.167.130:18080 9eb2375fde7787ce synchronizing 0 2455413 47 kB/s, 20 blocks / 0 MB queued
196.189.91.229:18080 69f85dd7d5e61900 normal 184 2455413 520 kB/s, 60 blocks / 4.84783 MB queued
92.232.116.158:18080 f1301da7ef268b5a normal 0 1 1 kB/s, 0 blocks / 0 MB queued
72.177.224.159:18080 580d9190f410ad51 synchronizing 0 2455413 4 kB/s, 20 blocks / 0 MB queued
178.63.100.197:18080 0f992957350f8d58 synchronizing 0 2455413 1009 kB/s, 358 blocks / 28.2721 MB queued
72.68.42.62:18080 64113358310cdaea synchronizing 0 2455412 217 kB/s, 0 blocks / 0 MB queued
30 spans, 41.6264 MB
[mooooo.ooo.ooooooooooooooooooo]
178.63.100.197:18080 20/187 (2454834 - 2454853, 1528 kB) 1317 kB/s (1)
178.63.100.197:18080 20/187 (2454854 - 2454873, 1276 kB) 1797 kB/s (1)
138.197.77.157:18080 20/187 (2454874 - 2454893, 1191 kB) 264 kB/s (0.29)
178.63.100.197:18080 20/187 (2454894 - 2454913, 1736 kB) 1659 kB/s (1)
196.189.91.229:18080 20/187 (2454914 - 2454933, 1807 kB) 96 kB/s (0.42)
178.63.100.197:18080 20/187 (2454934 - 2454953, 1292 kB) 1494 kB/s (1)
52.168.167.130:18080 20/187 (2454954 - 2454973) -
178.63.100.197:18080 20/187 (2454974 - 2454993, 1435 kB) 1646 kB/s (1)
178.63.100.197:18080 20/187 (2454994 - 2455013, 1812 kB) 1053 kB/s (1)
138.197.77.157:18080 20/187 (2455014 - 2455033, 1817 kB) 392 kB/s (0.29)
72.177.224.159:18080 20/187 (2455034 - 2455053) -
178.63.100.197:18080 20/187 (2455054 - 2455073, 1651 kB) 1240 kB/s (1)
178.63.100.197:18080 20/187 (2455074 - 2455093, 2056 kB) 1510 kB/s (1)
178.63.100.197:18080 20/187 (2455094 - 2455113, 1826 kB) 1720 kB/s (1)
138.197.77.157:18080 20/187 (2455114 - 2455133, 1686 kB) 420 kB/s (0.29)
178.63.100.197:18080 20/187 (2455134 - 2455153, 1378 kB) 1608 kB/s (1)
178.63.100.197:18080 20/187 (2455154 - 2455173, 1418 kB) 1652 kB/s (1)
178.63.100.197:18080 20/187 (2455174 - 2455193, 2121 kB) 1375 kB/s (1)
66.130.203.64:18080 20/187 (2455194 - 2455213, 1410 kB) 170 kB/s (0.11)
138.197.77.157:18080 20/187 (2455214 - 2455233, 1181 kB) 312 kB/s (0.29)
178.63.100.197:18080 20/187 (2455234 - 2455253, 1921 kB) 1406 kB/s (1)
178.63.100.197:18080 20/187 (2455254 - 2455273, 1973 kB) 1405 kB/s (1)
196.189.91.229:18080 20/187 (2455274 - 2455293, 1612 kB) 809 kB/s (0.42)
178.63.100.197:18080 20/187 (2455294 - 2455313, 1393 kB) 1316 kB/s (1)
138.197.77.157:18080 20/187 (2455314 - 2455333, 1165 kB) 364 kB/s (0.29)
178.63.100.197:18080 20/187 (2455334 - 2455353, 1081 kB) 1039 kB/s (1)
196.189.91.229:18080 20/187 (2455354 - 2455373, 1428 kB) 549 kB/s (0.42)
178.63.100.197:18080 20/187 (2455374 - 2455393, 1338 kB) 1244 kB/s (1)
178.63.100.197:18080 18/187 (2455394 - 2455411, 1029 kB) 1188 kB/s (1)
66.130.203.64:18080 1/187 (2455412 - 2455412, 52 kB) 101 kB/s (0.11)

```

# Discussion History
## selsta | 2021-09-23T04:31:03+00:00
Please be a bit more precise on what you want to do. Do you want to download the blockchain or do you want to use a remote node?

Also setting the bootstrap daemon to 127.0.0.1:9050/9150 is wrong. Remove that from the settings.

## selsta | 2021-09-23T13:08:49+00:00
Okay, I understand your issue now. Setting a bootstrap daemon can not be used to set a socks proxy, so it's a configuration bug on your side.

You can go to Settings -> Interface to set a socks proxy, but currently that only works with remote nodes.

# Action History
- Created by: ch9PcB | 2021-09-23T02:56:08+00:00
- Closed at: 2021-09-23T13:08:50+00:00
