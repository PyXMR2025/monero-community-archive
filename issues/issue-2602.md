---
title: HTTP API config
source_url: https://github.com/xmrig/xmrig/issues/2602
author: vpts1202
assignees: []
labels: []
created_at: '2021-09-23T19:13:11+00:00'
updated_at: '2021-10-01T05:56:46+00:00'
type: issue
status: closed
closed_at: '2021-10-01T05:56:46+00:00'
---

# Original Description
My query is for HTTP API config
How to use it?
What should I add(http:// ?) as the “new worker”?
How(in plain language, i.e. click/right click/double click/etc.)  to execute “executing API calls”?
I have configured as below but it does not seems workable
{
    "api": {
        "worker-id": "0.0.0.0"
    },
    "http": {
        "enabled": true,
        "host": "0.0.0.0",
        "port": 0,
        "access-token": null,
        "restricted": false
    },

Thanks


# Discussion History
## Spudz76 | 2021-09-23T19:28:17+00:00
Examples at the bottom of [API documentation](https://github.com/xmrig/xmrig/blob/master/doc/API.md)

Not sure if it works without setting an `access-token`...

## vpts1202 | 2021-09-24T07:39:35+00:00
> 
> 
> Examples at the bottom of [API documentation](https://github.com/xmrig/xmrig/blob/master/doc/API.md)
> 
> Not sure if it works without setting an `access-token`...

Many thanks for prompt and useful feedback.
1)	How to set  access-token? Or its okay to place some kind of password like “xYz2mj”?
2)	Should be config looks like below?

"api": {
	"id": null,
	"worker-id": null,
},
"http": {
	"enabled": true,
	"host": "0.0.0.0",
	"port": 0,
	"access-token": [?],
	"restricted": false
}

Once again thank you for your kind assistance. Look forward for your feedback for in above.


## Spudz76 | 2021-09-24T12:45:34+00:00
Yes access-token is simply shared secret string, long and random is good.

If you use workers.xmrig.info site it is a locally-running API client.

## vpts1202 | 2021-09-26T10:15:39+00:00
> 
> 
> Yes access-token is simply shared secret string, long and random is good.
> 
> If you use workers.xmrig.info site it is a locally-running API client.

1)	What does it mean “a locally-running API client” in your context?
2)	Port should be chosen in the range of open ports of website workers.xmrig.info?

Sorry for annoying you, I just want to make sure in all details since rule “The devil is in details” is always in place))
Thank you!


## Spudz76 | 2021-09-26T14:37:54+00:00
workers.xmrig.info does not receive any information about your miners.  The browser runs a fully local private monitoring -- it does not cause the web server to connect to your miners from "outside", your browser itself becomes an API client app.  All your miners are set in a cookie which is not sent to the outside Internet.  Therefore it can't be a security hole, none of your information leaves your browser.  Usually a web site sends information to the server so I mentioned "locally-running" meaning it is a javascript app that does all its work inside your LAN.

You don't need any firewall openings for workers.xmrig.info since the browser itself is doing the connections to your miners (all inside LAN realm).

## vpts1202 | 2021-09-27T23:51:30+00:00
> 
> 
> workers.xmrig.info does not receive any information about your miners. The browser runs a fully local private monitoring -- it does not cause the web server to connect to your miners from "outside", your browser itself becomes an API client app. All your miners are set in a cookie which is not sent to the outside Internet. Therefore it can't be a security hole, none of your information leaves your browser. Usually a web site sends information to the server so I mentioned "locally-running" meaning it is a javascript app that does all its work inside your LAN.
> 
> You don't need any firewall openings for workers.xmrig.info since the browser itself is doing the connections to your miners (all inside LAN realm).

If such then for remote access to the stats the api host 127.0.0.1 in config isn’t workable and I should use IPs of each worker/miner?
If so, what to do if there is dynamic IPs?
Thanks


# Action History
- Created by: vpts1202 | 2021-09-23T19:13:11+00:00
- Closed at: 2021-10-01T05:56:46+00:00
