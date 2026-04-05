---
title: 'problem with threads '
source_url: https://github.com/xmrig/xmrig/issues/849
author: systech-bat
assignees: []
labels: []
created_at: '2018-10-25T14:16:48+00:00'
updated_at: '2018-11-05T15:06:53+00:00'
type: issue
status: closed
closed_at: '2018-11-05T15:06:53+00:00'
---

# Original Description
hello. i have E5-2665 v1. it has 8 cores + 8 threads = 16 logical threads and 20 mb cache. here is config:
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

"log-file": "log.txt",

"max-cpu-usage": 95,

"pools": [
{
"url": "xmr-eu1.nanopool.org:14433",
"user": "43Psg4wUFsq76xqdHFTJjKECgD2DPxvjnEvfZLBr3cfgVXfYUodnemGJgxvZfCKrcFcCovQXyAQETKrQRVT5G2CyQdkkjt7.Rig9/x",
"pass": "x",
"rig-id": null,
"nicehash": false,
"keepalive": false,
"variant": -1,
"tls": true,
"tls-fingerprint": null
},
{
"url": "xmr-eu2.nanopool.org:14433",
"user": "43Psg4wUFsq76xqdHFTJjKECgD2DPxvjnEvfZLBr3cfgVXfYUodnemGJgxvZfCKrcFcCovQXyAQETKrQRVT5G2CyQdkkjt7.rig9/x",
"pass": "x",
"rig-id": null,
"nicehash": false,
"keepalive": false,
"variant": -1,
"tls": true,
"tls-fingerprint": null
},

],

"print-time": 60,

"retries": 5,

"retry-pause": 5,

"safe": false,

"threads" :


[
{

"low_power_mode": 1,

"affine_to_cpu": true,

"asm": true
},

{
"low_power_mode": 1,

"affine_to_cpu": false,

"asm": true
}
],

"user-agent": null,

"watch": false
}

problem is that i can't use more than 2 threads. i tried to change "max-cpu-usage" 5 and 90 =  no difference, just 2 threads work. i tried to change "threads" : , but if i type "threads" :  8, or anything i have an error: No valid configuration found. Exiting.
Press any key to continue . . .
where i made a mistake? 

# Discussion History
## snipeTR | 2018-10-25T15:42:47+00:00
config json
`"threads": "all",`

and please use https://config.xmrig.com/

## systech-bat | 2018-10-25T15:49:44+00:00
> config json
> `"threads": "all",`

didn't help. But i changed "low_power_mode": 1, to "low_power_mode": 0, and miner recreate config himself, with 20 threads (2 cpu per motherboard)

# Action History
- Created by: systech-bat | 2018-10-25T14:16:48+00:00
- Closed at: 2018-11-05T15:06:53+00:00
