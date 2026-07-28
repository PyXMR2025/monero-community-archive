---
title: Mini PCs crash at [randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168
  +JIT (323 ms)]
source_url: https://github.com/xmrig/xmrig/issues/3834
author: techrivertree
assignees: []
labels: []
created_at: '2026-07-25T22:39:12+00:00'
updated_at: '2026-07-27T03:04:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have 3 mini PCs, all are the same model but with different CPUs. One works great with xmrig, the other two refuse to work.

Working mini PC CPU: 5500U
Not working PCs CPU: 5825U

**To Reproduce**
Setup PC to use xmrig.

**Expected behavior**
XMrig should start to mine.

**Required data**
 - 6.26.0
    - https://github.com/xmrig/xmrig/releases/download/v6.26.0/xmrig-6.26.0-linux-static-x64.tar.gz

<img width="1341" height="429" alt="Image" src="https://github.com/user-attachments/assets/97e225be-7435-4413-8061-a9c7082a859a" />

 - Config file or command line (without wallets)
     I tried two version of config.json
          "pools": [
        {
            "algo": null,
            "coin": Zcash,
            "url": "rx.unmineable.com:3333",
            "user": "mycrptoaddress",
and

         {
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "coin": "zcash",
            "algo": null,
            "url": "stratum+tcp://rx.unmineable.com:3333",
            "user": "mycrptoaddress",
            "pass": "x",
            "tls": false,
            "keepalive": true,
            "nicehash": false
        }
    ]
}


 - OS: Debian


# Discussion History
## SChernykh | 2026-07-26T04:51:10+00:00
This is not XMRig, it's your SSH client disconnecting. `client_loop: send disconnect: Broken pipe` - there is no such message in the XMRig binary. Run XMRig as a systemd service, or in a screen session to not depend on SSH staying connected.

## techrivertree | 2026-07-26T20:17:50+00:00
It is xmrig, the client loop: send disconnect: Broken pipe is when I turned off my mini PC. XMRig gets stuck at allocated. Terminal is freeze and on my JetKVM, it losses HDMI and USB connection. Turning off my mini PCs solves that.


## SChernykh | 2026-07-27T03:00:34+00:00
@techrivertree It is **NOT** XMRig, it's your SSH client: https://sources.debian.org/src/openssh/1%3A10.3p1-1~bpo13%2B1/clientloop.c#L1682-L1688
```
	if ((r = sshpkt_start(ssh, SSH2_MSG_DISCONNECT)) != 0 ||
	    (r = sshpkt_put_u32(ssh, SSH2_DISCONNECT_BY_APPLICATION)) != 0 ||
	    (r = sshpkt_put_cstring(ssh, "disconnected by user")) != 0 ||
	    (r = sshpkt_put_cstring(ssh, "")) != 0 ||	/* language tag */
	    (r = sshpkt_send(ssh)) != 0 ||
	    (r = ssh_packet_write_wait(ssh)) != 0)
		fatal_fr(r, "send disconnect");
```
and fatal_fr code:
```
#define fatal_fr(r, ...) \
    sshfatal(__FILE__, __func__, __LINE__, \
        1, SYSLOG_LEVEL_FATAL, ssh_err(r), __VA_ARGS__)
```
So when it's called from [client_loop](https://sources.debian.org/src/openssh/1%3A10.3p1-1~bpo13%2B1/clientloop.c#L1455) function at line 1688, it prints exactly "client_loop: send disconnect: Broken pipe" (Broken pipe comes from `EPIPE` errno string).

 Run XMRig as a systemd service, or in a screen session to not depend on SSH staying connected.

## SChernykh | 2026-07-27T03:04:49+00:00
See also #3344 and #3406

# Action History
- Created by: techrivertree | 2026-07-25T22:39:12+00:00
