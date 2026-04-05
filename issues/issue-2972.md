---
title: 'how to fix this: rx.unmineable.com:3333 DNS error: "no such file or directory"'
source_url: https://github.com/xmrig/xmrig/issues/2972
author: BobbieX
assignees: []
labels: []
created_at: '2022-03-15T15:17:25+00:00'
updated_at: '2023-12-30T18:25:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[2022-03-15 22:55:12.306] Huge pages support was successfully enabled, but reboot required to use it

 * ABOUT        XMRig/6.16.4 MSVC/2019

 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0

 * HUGE PAGES   unavailable

 * 1GB PAGES    unavailable

 * CPU          Intel(R) Core(TM) i7-10710U CPU @ 1.10GHz (1) 64-bit AES

                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1

 * MEMORY       6.5/31.8 GB (21%)

                SODIMM1: 16 GB DDR4 @ 2667 MHz LD4AS016G-H2666G    

                SODIMM2: 16 GB DDR4 @ 2667 MHz LD4AS016G-H2666G    

 * MOTHERBOARD  Intel Corporation - NUC10i7FNB

 * DONATE       1%

 * ASSEMBLY     auto:intel

 * POOL #1      rx.unmineable.com:3333 algo rx/0

 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection

 * HTTP API     127.0.0.1:60070 

 * OPENCL       disabled

 * CUDA         disabled

[2022-03-15 22:55:12.327]  net      rx.unmineable.com:3333 DNS error: "no such file or directory"

[2022-03-15 22:55:17.346]  net      rx.unmineable.com:3333 DNS error: "no such file or directory"

[2022-03-15 22:55:22.367]  net      rx.unmineable.com:3333 DNS error: "no such file or directory"

[2022-03-15 22:55:27.390]  net      rx.unmineable.com:3333 DNS error: "no such file or directory"

[2022-03-15 22:55:32.442]  net      rx.unmineable.com:3333 DNS error: "no such file or directory"



# Discussion History
## snipeTR | 2022-03-21T09:05:06+00:00
![image](https://user-images.githubusercontent.com/31975916/159231273-cd2aee42-9c16-4a2d-8ab8-a286768e9871.png)


## silic0ns0ul | 2023-12-30T02:02:54+00:00
thought I'd try out xmrig for the first time. went through the config wizard. loaded up and immediately received this same DNS error... not sure how that relates to 'no file nor directory'?? 

## SChernykh | 2023-12-30T13:38:03+00:00
@silic0ns0ul Try another pool in the wizard.

## silic0ns0ul | 2023-12-30T18:25:48+00:00
So I ditched the wizard one and went back to the example config.json and started editing parameters. and I think what fixed it was setting the tls parameter to 'true' under the "pools" section.

Strangely enough though, under the "tls" section itself in the example config.json, it says enabled false, but everything seems to work fine now?
`    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },`

# Action History
- Created by: BobbieX | 2022-03-15T15:17:25+00:00
