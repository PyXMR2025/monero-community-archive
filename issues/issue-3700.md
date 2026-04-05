---
title: dns resolution
source_url: https://github.com/xmrig/xmrig/issues/3700
author: toxicroadkill
assignees: []
labels: []
created_at: '2025-08-27T01:47:37+00:00'
updated_at: '2025-08-29T00:03:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
proxy_xmr_00.home.arpa is defined in my router to ip 192.168.1.135
and if I ping proxy_xmr_00.home.arpa, it will respond with the correct IP

when running the new xmrig, I get a dns error when specifying the dns entry that is local..

for example "proxy_xmr_00.home.arpa", results in a error (proxy_xmr_00.home.arpa:10001 DNS error: "unknown node or service")

but if i change it to use the IP address, all works fine


xmrig, used to work fine doing this, but the latest version this error message started happening.

proxy_xmr_00.home.arpa is a example, other domains being defined result in the same error


is this a bug, or a "feature" ?

having it use a domain name (including ones locally defined), is very handy, since I run nearly 400 miners, and if for whatever reason the ip of the proxy would change, changing all 400 miners, is a royal pita

running a older version of xmrig, with the same exact setup, worked perfect, and would resolve the locally defined domain, when upgrading to the latest version, this started happening.

# Discussion History
## xmrig | 2025-08-27T07:56:44+00:00
For start, try set `"ip_version": 4,` https://github.com/xmrig/xmrig/blob/master/src/config.json#L96 to force IPv4 only. Version v6.24.0 brings more equality for IPv6. It should work the same as before if only IPv4 is used (by DNS server). I'm not sure what caused the bug for now.
Thank you.

## toxicroadkill | 2025-08-28T04:18:07+00:00
i usually run it directly from the command line and not using a config.json


**however, for testing, i created a quick and dirty config.json**, and added the ip_version 4 command

with the same error

[2025-08-28 03:56:54.318]  net      proxy_xmr_00.home.arpa:10001 DNS error: "unknown node or service"

a ping resolves to the correct machine (in this case 192.168.1.135

root@ip128000:~# ping proxy_xmr_00.home.arpa
PING proxy_xmr_00.home.arpa (192.168.1.135) 56(84) bytes of data.
64 bytes from proxy_xmr_00.home.arpa (192.168.1.135): icmp_seq=1 ttl=64 time=0.204 ms
64 bytes from proxy_xmr_00.home.arpa (192.168.1.135): icmp_seq=2 ttl=64 time=0.251 ms
^C


here is my config.json (please note, that it was just quickly thrown together for testing, and is not a production config.json file)


{
    "api": {
        "id": "ip128000",
        "worker-id": "ip128000"
    },
    "http": {
        "enabled": true,
        "host": "192.168.128.0",
        "port": 10000,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2]
        ],
        "rx": [0, 1, 2],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow"
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "proxy_xmr_00.home.arpa:10001",
            "user": "ip128000",
            "pass": "x",
            "rig-id": null,
            "nicehash": true,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 64,
    "print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ip_version": 4,
        "ttl": 16
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false


if I change the line in config.json ("url": "proxy_xmr_00.home.arpa:10001")

to

("url": "192.168.1.135:10001"")


it works just fine

[2025-08-28 04:02:13.614]  net      use pool 192.168.1.135:10001  192.168.1.135


just for the heck of it, i tried this

("url": "xmr-eu1.nanopool.org")

and it resolved the dns correctly


[2025-08-28 04:04:24.505]  net      xmr-eu1.nanopool.org 57.128.224.74 connect error: "connection refused"

(refused, because i didnt set up for the pool completely), but the point, DNS **does** resolve addresses

just not locally defined ones..im using a cisco router, and have the entry:

ip host proxy_xmr_00.home.arpa 192.168.1.135


and since a ping to the "proxy_xmr_00.home.arpa", results in a correct IP of 192.168.1.135, the router is correctly configured..


now older versions of xmrig, work just fine, it was just when i upgraded to the new version when this issue popped up


so it seems that xmrig, resolves addresses just fine, as long as they are. not a locally defined address, kinda makes me thing

that it's using some "predefined" dns server to resolve entries and not the dns server configured in the host operating system


?????




On 8/27/25 3:57 AM, xmrig wrote:
> xmrig
>  left a comment 
> [(xmrig/xmrig#3700)](https://github.com/xmrig/xmrig/issues/3700#issuecomment-3227189292)
>
> For start, try set "ip_version": 4, https://github.com/xmrig/xmrig/blob/master/src/config.json#L96 to force IPv4 only. Version v6.24.0 brings more equality for IPv6. It should work the same as before if only IPv4 is used. I'm not sure what caused the bug for now.
> Thank you.

> —
> Reply to this email directly, [view it on GitHub](https://github.com/xmrig/xmrig/issues/3700#issuecomment-3227189292), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/ASD5O34CZOPW4RXO6GOT4TL3PVQFDAVCNFSM6AAAAACE4XXRCGVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTEMRXGE4DSMRZGI).
> You are receiving this because you authored the thread.

## xmrig | 2025-08-28T09:39:09+00:00
Changes in xmrig DNS code are not that big and use the same libuv-based `uv_getaddrinfo` function, without the possibility to set a preferred DNS server. However, the idea of a preferred server makes me think that it changes much deeper and is related to switching from `msvct` to `ucrt` #3668, which affects GCC-based builds on Windows. You didn't mention the OS, so I assume it's Windows; otherwise, it's not relevant.

Since I can't reproduce the issue, I may ask you to check all versions starting from [v6.22.2](https://github.com/xmrig/xmrig/releases/tag/v6.22.2) to [v6.23.0](https://github.com/xmrig/xmrig/releases/tag/v6.23.0) and  [v6.24.0](https://github.com/xmrig/xmrig/releases/tag/v6.24.0), both msvc and gcc versions, to make sure when the issue appears.

Please show the output of `nslookup proxy_xmr_00.home.arpa` too.
Thank you.

## toxicroadkill | 2025-08-29T00:03:40+00:00

ok, here are the results for 4 diff versions of xmrig, using the same config file for all four tests


/home/ip008032/xmrig-6.21.0/xmrig --config /home/ip008032/config.json
[2025-08-28 23:56:08.333]  net      use pool proxy_xmr_00.home.arpa:10001  10.0.8.32


/home/ip008032/xmrig-6.22.2/xmrig --config /home/ip008032/config.json
[2025-08-28 23:36:07.826]  net      proxy_xmr_00.home.arpa:10001 DNS error: "unknown node or service"


/home/ip008032# /home/ip008032/xmrig-6.23.0/xmrig --config /home/ip008032/config.json
[2025-08-28 23:37:05.614]  net      proxy_xmr_00.home.arpa:10001 DNS error: "unknown node or service"


root@ip008032:/home/ip008032# /home/ip008032/xmrig-6.24.0/xmrig --config /home/ip008032/config.json
[2025-08-28 23:37:57.304]  net      proxy_xmr_00.home.arpa:10001 DNS error: "unknown node or service"


all these were tested on a fresh install of debian 13 (trixie)

6.21.0 worked just fine
but then by
6.22.2 it stopped working


i dont have access to any of the other versions between 6.21.0 and 6.22.2, if you can provide a link to other versions (binary downloads) in between, i can test those out for you also

i use the 

xmrig-xxx-linux-static-x64.tar.gz

files




# Action History
- Created by: toxicroadkill | 2025-08-27T01:47:37+00:00
