---
title: Xmrig reconnecting to Xmrig Proxy every few minutes
source_url: https://github.com/xmrig/xmrig/issues/3521
author: panosarp
assignees: []
labels:
- bug
- review later
created_at: '2024-07-30T18:12:08+00:00'
updated_at: '2025-06-18T22:08:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
On an epyc 9654 96c/192t system with win server 2022 and xmrig miner connected to xmrig proxy cpu mining only, the miner disconnects amd reconnects to the proxy every few minutes, the frequency is variable. I have ruled out network issues.
The disconnects disappear if i launch 4 instances with 48 threads each.  I have configured the system with 1, 4 and 12 numa nodes with the disconnects occuring on all numa configs. I have tried running the proxy on the same epyc system and on a seperate machine with the same result.

**To Reproduce**
Launch xmrig on the described machine and connect it to xmrig proxy. The miner will reconnect to the proxy every 3 - 10 minutes

**Expected behavior**
The miner should operate without frequent reconnects.

**Required data**
 - XMRig version     XMRig/6.21.3 MSVC/2022, tried prebuild and build myself.
 - Below is the console output when disconnect occurs from a build with -DWITH_DEBUG_LOG=ON
 [2024-07-30 20:50:13.536] [192.168.0.68:3333] send (215 bytes): "{"id":37,"jsonrpc":"2.0","method":"submit","params":{"id":"48d836672605ddce","job_id":"138165798683810","nonce":"1e7d6b17","result":"6aa210b6dde912fc4d75fc19ad5f5e3c1b09b8b7b013b02447a255d21a020000","algo":"rx/0"}}"
[2024-07-30 20:50:13.655] [192.168.0.68:3333] received (63 bytes): "{"id":37,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}"
[2024-07-30 20:50:13.655]  cpu      accepted (26/0) diff 5180K (119 ms)
[2024-07-30 20:50:15.991] [192.168.0.68:3333] state: "connected" -> "closing"
[2024-07-30 20:50:15.992] [192.168.0.68:3333] state: "closing" -> "unconnected"
[2024-07-30 20:50:15.999] [192.168.0.68:3333] state: "unconnected" -> "reconnecting"
[2024-07-30 20:50:15.999]  net      no active pools, stop mining
[2024-07-30 20:50:17.228] [192.168.0.68:3333] state: "reconnecting" -> "host-lookup"
[2024-07-30 20:50:17.229] [192.168.0.68:3333] state: "host-lookup" -> "connecting"
[2024-07-30 20:50:17.270] [192.168.0.68:3333] state: "connecting" -> "connected"
 - OS: windows server 2022




# Discussion History
## SChernykh | 2024-07-30T22:34:24+00:00
You need to provide logs from the proxy side (with debug log enabled). Proxy logs will show the reason for disconnects.

## panosarp | 2024-08-01T00:02:15+00:00
I have viewed the net traffic between miner and proxy with MS net monitor, the connection close is initiated by the miner:
![image](https://github.com/user-attachments/assets/1d43262a-5a0f-4514-92e5-01b4c316dc46)

In the above 192.168.0.120 is the miner , on 7:43:39  miner sends a packet with F flag (end of data), previous packet is 30 sec before.

On the proxy side:
![image](https://github.com/user-attachments/assets/11d107f7-64d7-4eb2-a646-af5b924ac560)
If you mean proxy with DWITH_DEBUG_LOG=ON, i dont have that.


## SChernykh | 2024-08-01T06:32:13+00:00
How do you connect to the proxy? Please show the command line or config.json for XMRig that you use (you can redact wallet and IP/pool addresses).

## panosarp | 2024-08-01T23:33:14+00:00
Here is the miner config.
I currently have the proxy and miner on the affected server so the miner connects to 127.0.0.1, but the same problem occurs if the proxy is on another machine and the miner connects through lan or wan.
[config.json](https://github.com/user-attachments/files/16462751/config.json)


## SChernykh | 2024-08-02T06:13:40+00:00
Config looks ok, you could try to enable `keepalive` and see if it helps.

## panosarp | 2024-09-18T20:16:47+00:00
Disconnections disappear completely by changing proxy mode parameter to simple.

## SChernykh | 2024-09-18T20:23:48+00:00
Ah, now I understand what's happening. EPYC 9654 has 90-100 kh/s hashrate (per CPU), and it exhausts the search space in NiceHash proxy mode in less than 3 minutes - when it happens, XMRig disconnects. If you have dual CPU server (384 threads in total), it's 1.5 minutes until disconnect. You should connect to a pool which sends jobs much more often than once per minute.

# Action History
- Created by: panosarp | 2024-07-30T18:12:08+00:00
