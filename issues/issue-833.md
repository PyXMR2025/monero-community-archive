---
title: run xmrig but cpu not start
source_url: https://github.com/xmrig/xmrig/issues/833
author: tarxzvf
assignees: []
labels: []
created_at: '2018-10-21T08:32:23+00:00'
updated_at: '2018-10-31T12:11:19+00:00'
type: issue
status: closed
closed_at: '2018-10-31T12:11:19+00:00'
---

# Original Description
run xmrig on different pc  but no all start cpu , where is problem .. thanks

# Discussion History
## snipeTR | 2018-10-21T09:33:43+00:00
Share config.json

## tarxzvf | 2018-10-21T11:11:18+00:00
{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "asm": true,
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 50,
    "pools": [
        {
            "url": "ca.minexmr.com:5555",
            "user": "474jo9QWGxLde8ohapGQLrfxxhARmAR421FjSpWGbx2x4fWH3USyVhYaanWVCH7nV8ZBWp4uxVjw1g7FpcvFCy9PQ4s3sht",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": null,
    "user-agent": null,
    "watch": false
}


 * ABOUT        XMRig/2.8.1 gcc/8.2.0
 * LIBS         libuv/1.23.1 microhttpd/0.9.59
 * HUGE PAGES   unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz (2) x64 AES
 * CPU L2/L3    4.0 MB/30.0 MB
 * THREADS      4, cryptonight, donate=1%
 * ASSEMBLY     auto:intel
 * POOL #1      ca.minexmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2018-10-21 07:05:58] READY (CPU) threads 4(4) huge pages 0/4 0% memory 8.0 MB
[2018-10-21 07:05:59] [ca.minexmr.com:5555] connect error: "connection refused"




 * ABOUT        XMRig/2.8.1 gcc/8.2.0
 * LIBS         libuv/1.23.1 microhttpd/0.9.59
 * HUGE PAGES   unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz (2) x64 AES
 * CPU L2/L3    4.0 MB/30.0 MB
 * THREADS      4, cryptonight, donate=1%
 * ASSEMBLY     auto:intel
 * POOL #1      ca.minexmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2018-10-21 07:05:58] READY (CPU) threads 4(4) huge pages 0/4 0% memory 8.0 MB
[2018-10-21 07:05:59] [ca.minexmr.com:5555] connect error: "connection refused"


thanks for reply man ... any pool i use said that .. on some pc works .. 

on pc work config is same .. where not work config change auto 

## tarxzvf | 2018-10-21T11:12:36+00:00
if you can help me or have ideea , appreciate , thanks

## gboelter | 2018-10-21T11:31:46+00:00
Only an idea, try 3333 instead 5555 ...

On Sun, 21 Oct 2018, 19:12 tarxzvf <notifications@github.com> wrote:

> if you can help me or have ideea , appreciate , thanks
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/833#issuecomment-431660009>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AAhHQavjYEle6fin-Sf_VOS-MVvdAXwbks5unFalgaJpZM4XyV2v>
> .
>


## 2010phenix | 2018-10-21T11:44:23+00:00
confirm...
Have same problem and on classic C miner....
Check on few pools with few algo that used cn/1 cn/2
In first look, somewhere lost check about variant or wrong work variant auto
@tarxzvf try manual set  variant 2(cn/2)

## tarxzvf | 2018-10-21T11:53:15+00:00
thanks for reply , i try nothing .. same no connect to pool

## xmrig | 2018-10-21T12:10:01+00:00
`"connection refused"` it's network issue, likely your ISP block connection our you banned on pool. `ca.minexmr.com:5555` works fine for me right now, it resolved to 3 address `158.69.25.62`, `158.69.25.71`, `158.69.25.77` you can try check use IP address instead of domain name.

Also try TLS port `ca.minexmr.com:6666` (don't forget about `"tls": true,`) but you need rebuild miner with OpenSSL support for it.

If all above not help, try smaller pools.

## tarxzvf | 2018-10-21T12:30:06+00:00
still same man .. i think need rebuild miner with OpenSSL like you said .. but me not know make ...thanks

## tarxzvf | 2018-10-21T12:33:49+00:00
if someone want lost time with me , i pay for his time .. 

## srwx666 | 2018-10-21T14:42:43+00:00
"connection refused"
is a network problem, not xmrig itself
check Your ISP, check Your firewall
try doing telnet to 
ca.minexmr.com 5555
ca.minexmr.com 6666
or whatever port minexmr supports

easyest way for You to check will be to connect to port 80 or 443, to bypass firewall problem



## snipeTR | 2018-10-21T17:07:01+00:00
I tink firewall.

## tarxzvf | 2018-10-23T05:09:26+00:00
hi ,  i turn off firewall but same ..

[2018-10-23 01:07:54] Huge pages support was successfully enabled, but reboot required to use it
 * ABOUT        XMRig/2.8.1 gcc/8.2.0
 * LIBS         libuv/1.23.1 OpenSSL/1.1.1 microhttpd/0.9.59
 * HUGE PAGES   unavailable
 * CPU          Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz (4) x64 AES
 * CPU L2/L3    12.0 MB/60.0 MB
 * THREADS      6, cryptonight, donate=1%
 * ASSEMBLY     auto:intel
 * POOL #1      ca.minexmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2018-10-23 01:07:54] READY (CPU) threads 6(6) huge pages 0/6 0% memory 12.0 MB
[2018-10-23 01:07:55] [ca.minexmr.com:5555] connect error: "connection refused"
[2018-10-23 01:08:02] [ca.minexmr.com:5555] connect error: "connection refused"
[2018-10-23 01:08:09] [ca.minexmr.com:5555] connect error: "connection refused"
[2018-10-23 01:08:16] [ca.minexmr.com:5555] connect error: "connection refused"
[2018-10-23 01:08:23] [ca.minexmr.com:5555] connect error: "connection refused"

how try telnet see if works , thanks ppl

## snipeTR | 2018-10-23T08:08:57+00:00
Please debug mod enable.

## NmxMilk | 2018-10-23T08:58:13+00:00
What system are you running on ?
On unix you can test with:
# telnet ca.minexmr.com 5555
Here is what I get:
#telnet ca.minexmr.com 5555
Trying 158.69.25.71...
Connected to ca.minexmr.com.
Escape character is '^]'.


## NmxMilk | 2018-10-23T09:00:03+00:00
By the way, with the four 2630 you got, you should be running 60/2 --> 30 threads.
What hashrate are you getting ? I guess such a system can give about 1kH/s.

# Action History
- Created by: tarxzvf | 2018-10-21T08:32:23+00:00
- Closed at: 2018-10-31T12:11:19+00:00
