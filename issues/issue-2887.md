---
title: Xmrig errors on mac
source_url: https://github.com/xmrig/xmrig/issues/2887
author: Treker381
assignees: []
labels: []
created_at: '2022-01-22T19:26:16+00:00'
updated_at: '2025-06-20T11:07:01+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:07:01+00:00'
---

# Original Description
When running XMRIG, I get one of these errors:
cpu rejected (12/3) diff 100001 "Invalid job id"
or:
net no active pools, stop mining

I also notice my cpu also is not running as heavily as usual when I put my computer to sleep.
Config:
{
"api": {
"id": null,
"worker-id": null
},
"http": {
"enabled": false,
"host": "127.0.0.1",
"port": 0,
"access-token": null,
"restricted": true
},
"autosave": true,
"background": true,
"colors": true,
"title": true,
"randomx": {
"init": -1,
"init-avx2": -1,
"mode": "auto",
"1gb-pages": false,
"rdmsr": true,
"wrmsr": false,
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
"astrobwt-max-size": 550,
"astrobwt-avx2": false,
"argon2": [0, 2, 4, 6, 5, 7],
"astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
"cn": [
[1, 0],
[1, 2],
[1, 4]
],
"cn-heavy": [
[1, 0],
[1, 2]
],
"cn-lite": [
[1, 0],
[1, 2],
[1, 4],
[1, 6],
[1, 5],
[1, 7]
],
"cn-pico": [
[2, 0],
[2, 1],
[2, 2],
[2, 3],
[2, 4],
[2, 5],
[2, 6],
[2, 7]
],
"cn/upx2": [
[2, 0],
[2, 1],
[2, 2],
[2, 3],
[2, 4],
[2, 5],
[2, 6],
[2, 7]
],
"rx": [0, 2, 4],
"rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
"rx/wow": [0, 2, 4, 6, 5, 7],
"cn-lite/0": false,
"cn/0": false,
"rx/keva": "rx/wow"
},
"opencl": {
"enabled": false,
"cache": true,
"loader": null,
"cn-lite/0": false,
"cn/0": false
},
"cuda": {
"enabled": false,
"loader": null,
"cn-lite/0": false,
"cn/0": false
},
"log-file": null,
"donate-level": 1,
"donate-over-proxy": 0,
"pools": [
{
"algo": "rx/0",
"coin": null,
"url": "rx.unmineable.com:3333",
"user": "DOGE:DCruiZQ94po7VXHxejWCQBWELfEav3S3Sw.ClexerlMinerA",
"pass": "x",
"rig-id": null,
"nicehash": false,
"keepalive": false,
"enabled": true,
"tls": false,
"tls-fingerprint": null,
"daemon": false,
"socks5": null,
"self-select": null,
"submit-to-origin": false
}
],
"retries": 5,
"retry-pause": 5,
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
"ipv6": false,
"ttl": 30
},
"user-agent": null,
"verbose": 0,
"watch": true,
"pause-on-battery": false,
"pause-on-active": false
}

# Discussion History
# Action History
- Created by: Treker381 | 2022-01-22T19:26:16+00:00
- Closed at: 2025-06-20T11:07:01+00:00
