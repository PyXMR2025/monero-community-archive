---
title: '[Question] Regarding NiceHash Option'
source_url: https://github.com/xmrig/xmrig/issues/3089
author: bwq90
assignees: []
labels: []
created_at: '2022-07-19T04:14:07+00:00'
updated_at: '2022-07-19T06:45:01+00:00'
type: issue
status: closed
closed_at: '2022-07-19T06:45:01+00:00'
---

# Original Description
Hi Team,

I am using xmrig miners on multiple machines. All of those are connected to my xmrig proxy server which submits the shares to moneroocean pool.

My question is:

Do I need to enable nicehash flag to true on my miners side?

This confusion arises because of two conflicting suggestions in your docs.

1. On [this](https://xmrig.com/docs/miner/config/pool#nicehash) link it is stated that

> [NiceHash](https://xmrig.com/docs/extensions/nicehash) support. This option is **only required** if you mine on **nicehash.com**.

2. On Xmrig proxy Repo [Homepage](https://github.com/xmrig/xmrig-proxy). it is clearly stated on top i.e.

> Nicehash support **must** be enabled on miner side, it mandatory.

The above line does not indicate whether this should be enabled **only** when mining on nicehash.com or regardless of whatever pool we mine. If we use xmrig proxy server then all of our miners connecting to proxy should have nicehash flag set to true in their config.json.

Can someone elaborate on this?

At the moment, I have set this nicehash flag set to false on miners site. Still everything looks normal to me ( All miners successfully connect to proxy and then connections are bundles towards moneroocean pool from my proxy).

What difference it will make if I set this flag to true on miners side?

I often see below errors in my xmrig proxy logs.

```
[gulf.moneroocean.stream:11024] send failed, invalid state: 1
gulf.moneroocean.stream:11024 error: "Unauthenticated", code: -1
0193 no active pools, stop
gulf.moneroocean.stream:11024 error: "New connections from this IP address are temporarily suspended from mining (10 minutes max)", code: -1
```

Regardless of these errors I get constant hashrate on proxy side and on pool side.


# Discussion History
## SChernykh | 2022-07-19T06:13:44+00:00
XMRig auto-detects if it should use nicehash mode when it connects to the proxy, you don't need to change the config. The XMRig-proxy homepage is probably out of date.

## bwq90 | 2022-07-19T06:45:01+00:00
Thank you @SChernykh for quick response. Much appreciated. 

# Action History
- Created by: bwq90 | 2022-07-19T04:14:07+00:00
- Closed at: 2022-07-19T06:45:01+00:00
