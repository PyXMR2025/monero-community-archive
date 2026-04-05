---
title: HTTPD isnt rechable
source_url: https://github.com/xmrig/xmrig/issues/3226
author: SandUhrGucker
assignees: []
labels: []
created_at: '2023-03-21T10:33:28+00:00'
updated_at: '2024-12-31T09:31:02+00:00'
type: issue
status: closed
closed_at: '2023-03-21T12:44:35+00:00'
---

# Original Description
**Describe the bug**
I build from source without errors. But the HTTPD isnt rechable.

**To Reproduce**
Build from scratch (Debian Bulleye):
You may or not compile with -DWITH_HTTP=ON
config with wizard, enable HTTP Service, set Host to 0.0.0.0 Port 80

**Expected behavior**
Simple Statistic Page should apear in Webbrowser at IP or localhost

**Required data**
```
bubu@miner:~/xmrig/build$ nmap -sT -p80 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2023-03-21 12:22 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00012s latency).
Other addresses for localhost (not scanned): ::1

PORT   STATE  SERVICE
80/tcp closed http

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
```

```
bubu@miner:~/xmrig/build$ ./xmrig
 * ABOUT        XMRig/6.19.0 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1n hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7 CPU 920 @ 2.67GHz (1) 64-bit -AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       0.5/5.8 GB (9%)
 * DONATE       2%
 * ASSEMBLY     auto:none
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     0.0.0.0:80
 * OPENCL       disabled
 * CUDA         disabled

```
I tried with config-file and with commandline:
./xmrig --donate-level 2 --api-worker-id powerminer --http-host 0.0.0.0 --http-port 80 --http-access-token bubu --http-no-restricted -o pool.supportxmr.com:443 -u WALLETADDRESS  -k --tls -p powerminer


# Discussion History
## SChernykh | 2023-03-21T12:17:03+00:00
This is not how it works. You should add your worker at workers.xmrig.info to see the data.

## SandUhrGucker | 2023-03-21T12:44:35+00:00
> This is not how it works. You should add your worker at workers.xmrig.info to see the data.

I know. But I expected an open Port ready to communicate locally.

However. After some Minutes/reboots the Port pops up. I didnt change anything!
Now I'm able to challenge the Token communication handling like described in the API-Doc: https://github.com/xmrig/xmrig/blob/master/doc/API.md

```
bubu@miner:~/xmrig/build$ nmap -sT -p80 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2023-03-21 14:38 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00017s latency).
Other addresses for localhost (not scanned): ::1

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds

```

Thank you.

## dchmelik | 2024-12-31T09:30:52+00:00
Well, xmrig does have an HTTPD which displays JSON, so this is how it works (at least now); using remote website doesn't work well if you can't port forward one port to many servers and want to keep standard configurations, besides is less secure.

# Action History
- Created by: SandUhrGucker | 2023-03-21T10:33:28+00:00
- Closed at: 2023-03-21T12:44:35+00:00
