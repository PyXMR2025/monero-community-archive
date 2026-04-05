---
title: '[Enhancement] API, Total hashrate of all miners'
source_url: https://github.com/xmrig/xmrig/issues/1772
author: vPrapo
assignees: []
labels:
- enhancement
- META
created_at: '2020-07-11T21:27:22+00:00'
updated_at: '2024-12-28T09:47:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I would like to see the total hashrate of all miners in workers.xmrig.info
Something like this

![Total-Hashrate2](https://user-images.githubusercontent.com/47542625/87234102-4578c780-c3bd-11ea-964d-9be82d68243e.png)

Or this

![Total-Hashrate](https://user-images.githubusercontent.com/47542625/87234083-00ed2c00-c3bd-11ea-84c8-748abea4c232.png)


# Discussion History
## ludufre | 2021-04-06T21:05:36+00:00
Where is the repo? I'll submit some PRs...

## Spudz76 | 2021-04-10T01:49:54+00:00
I never found a repo, it's probably private, but would add/fix a bunch of stuff if I could find it.

## ludufre | 2021-04-26T05:15:44+00:00
@alinoob2 @Spudz76 take a look on my repo: https://github.com/ludufre/xmworkers


## xmrig | 2021-04-26T10:58:36+00:00
@ludufre Nice work, note about HTTPS: it's supported https://xmrig.com/docs/miner/config/network#tls but to make it work smoothly valid certificates are required on each miner, so it is complicated to set up. 
Thank you.

## xmrig | 2021-04-26T17:33:31+00:00
Source code published https://github.com/xmrig/xmrig-workers
Thank you.

## dchmelik | 2024-12-28T03:49:42+00:00
I'd like to see such/all data in [xmrig-monitor](http://github.com/bitlamas/xmrig-monitor) accessible from each server; not just external site (may not always have connection).  Neither instructions for monitor nor website seem basic/complete/sufficient/usable.  I used to use xmr-stak-rx (no longer compiles, or I still would) which let you configure such as http://192.168.1.n:11380 (n∈ℕ) and it'd just work (without requiring 'access token').  It should be that simple.  If I put "host", "port" in config.json it's rewritten with host changed from 0.0.0.0 or 192.168.1.n to 127.0.0.1, and port randomized, and changed from '"restricted": "false"' to "true", none which I want.  Why give options if they just get changed?

## Spudz76 | 2024-12-28T06:31:03+00:00
Dunno this works for me:
```
    "api": {
        "id": null,
        "worker-id": "hostname-or-whatever"
    },
    "http": {
        "enabled": true,
        "host": "::",
        "port": 10083,
        "access-token": "redacted",
        "restricted": false
    },
```
which shows listening properly on wildcard
```
# ss -nlp | grep 10083
tcp   LISTEN 0      511                                                  *:10083                  *:*    users:(("xmrig",pid=1407642,fd=13))
```

Perhaps you didn't quote the ip, or did quote the port?  It should not regen the config with other host/port unless they were invalid type or invalid content (ip's are strings, ports are integers... booleans are not quoted...) as then they are taken as `null`

## dchmelik | 2024-12-28T07:38:22+00:00
No.
```
"http": {                                                                                                                                  
        "enabled": true,                                                                                                                       
        "host": "0.0.0.0",                                                                                                                     
        "port": 11380,                                                                                                                         
        "restricted": false                                                                                                                    
    }
```
However, it started configuring okay.
```
"http": {                                                                                                                                 
        "enabled": true,                                                                                                                      
        "host": "0.0.0.0",                                                                                                                   
        "port": 11380,                                                                                                                       
        "access-token": null,                                                                                                                
        "restricted": false                                                                                                                  
    }
```
However, xmrig-monitor has blank fields, and http://192.168.1.3:11380 says:
```
{
    "status": 401,
    "error": "Unauthorized"
}
```
This shouldn't take so much more configuration than xmr-stak-rx did.

## Spudz76 | 2024-12-28T09:37:09+00:00
`xmrig-monitor` is written for the deprecated old API and requires the full endpoint (not just the `http://host:port/` like it says to use)

So set `endpointAPI` in `variables.js` to `http://192.168.1.3:11380/1/summary` and it works.  Same with browser.  `/` is not a valid URL for the API (since ~7 years ago?) and will always return 401 or 404.

It's not a very robust widget, and lacks tons of information that would otherwise be in the current API version 2 (`/2/summary` and `/2/backends` along with possibly `/2/dmi`)

Or, really the first line of `functions.js` should just be:
```
$.getJSON(endpointAPI + '1/summary', function(data) {
```
and then it would match the comment docs in the `variables.js` (requires ending slash!)

Handling duplicate superfluous slashes (or missing ones) would take more code since it does absolutely zero sanity checking or input sanitization, and `.getJSON` does not tolerate malformed URLs.  But then I'd be rewriting the whole dumb tool.

# Action History
- Created by: vPrapo | 2020-07-11T21:27:22+00:00
