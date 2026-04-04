---
title: reverse proxy for rpc?
source_url: https://github.com/monero-project/monero/issues/8362
author: Roki100
assignees: []
labels: []
created_at: '2022-05-29T02:41:49+00:00'
updated_at: '2022-06-19T01:12:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello! I started my node few days ago and i am using nginx for my node now to connect to rpc with wallets, but i have noticed that monerod is not aware of this at all and when i enable log level to 1 each http request is actually an ip of nginx's docker container, is there a way to get monerod to be "aware" of the reverse proxy and recognize real ips via some real ip header? like `--reverse-proxy` or something?

# Discussion History
## plowsof | 2022-05-31T23:43:32+00:00
Do you have monerod running in a docker container? if so you can force the docker container to have a static ip [see here](https://github.com/plowsof/flipstarter-waas-wip/blob/32cd2628a4285437eaf698e8ee52b77e948e79ef/docker-compose.yml#L13) note: this is considered bad practice, but it works for me. 
and then in nginx something like:
```
  location /something {
    proxy_pass http://172.20.111.2:8000;
  }
```

## Roki100 | 2022-06-01T08:04:32+00:00
> Do you have monerod running in a docker container? if so you can force the docker container to have a static ip [see here](https://github.com/plowsof/flipstarter-waas-wip/blob/32cd2628a4285437eaf698e8ee52b77e948e79ef/docker-compose.yml#L13) note: this is considered bad practice, but it works for me. 
> and then in nginx something like:
> ```
>   location /something {
>     proxy_pass http://172.20.111.2:8000;
>   }
> ```

yes it is running in docker container and i have already set up networking properly, proxy_pass https://monerod:18089;
but that is not what i asked though, monerod is not aware of being behind a proxy and it doesnt recognize real request ips, so i guess its a bad thing for any sort of anti abuse mechanisms

## plowsof | 2022-06-01T22:40:04+00:00
sounds like a docker container / networking issue rather than monerod problem? It reminds me of running a tor hidden service* where all ip's are 'localhost', is there a specific issue that this causes? or are you worried about something potentially happening?

## Roki100 | 2022-06-02T05:51:26+00:00
> sounds like a docker container / networking issue rather than monerod problem? It reminds me of running a tor hidden service* where all ip's are 'localhost', is there a specific issue that this causes? or are you worried about something potentially happening?

no its not docker issue, monerod simply does not respect any real ip/forwarded for header

# Action History
- Created by: Roki100 | 2022-05-29T02:41:49+00:00
