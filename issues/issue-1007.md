---
title: New HTTP API backend.
source_url: https://github.com/xmrig/xmrig/issues/1007
author: xmrig
assignees: []
labels:
- enhancement
- META
created_at: '2019-04-01T07:02:35+00:00'
updated_at: '2019-08-02T11:53:13+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:53:13+00:00'
---

# Original Description
In v2.15.1-beta **old HTTP API backend** based on libmicrohttpd, **replaced to custom HTTP server** (libuv + [http_parser](https://github.com/nodejs/http-parser)).
It means libmicrohttpd dependency now complete removed, but miner or proxy can still build without HTTP support.


### Command line changes

* Added new options `--http-enabled` and `--http-host`.
* Options `--api-access-token`, `--api-port`, `--api-no-restricted` now deprecated, use `--http-access-token`, `--http-port`, `--http-no-restricted` instead.
* Option `--api-ipv6` removed, use `--http-host "::"` instead.


### Config file changes

Format for API options changed:

Old:
```
"api": {
	"port": 0,
	"access-token": null,
	"id": null,
	"worker-id": null,
	"ipv6": false,
	"restricted": true
},
```

New:
```
"api": {
	"id": null,
	"worker-id": null,
},
"http": {
	"enabled": false,
	"host": "127.0.0.1",
	"port": 0,
	"access-token": null,
	"restricted": true
}
```

Don't need change format by hand, miner or proxy will automatically update config to new format.

* To enable or disable API use field `enabled`.
* Zero port now valid option (random port).
* By default (except upgrade previous config) API now bind to locahost only, to remote access change host option to `"0.0.0.0"` (IPv4) or `"::"` (IPv4+IPv6). 
* All options now can be changed in runtime.

# Discussion History
## xmrig | 2019-04-01T12:29:14+00:00
* https://github.com/xmrig/xmrig/releases/tag/v2.15.1-beta
* https://github.com/xmrig/xmrig-proxy/releases/tag/v2.15.1-beta

# Action History
- Created by: xmrig | 2019-04-01T07:02:35+00:00
- Closed at: 2019-08-02T11:53:13+00:00
