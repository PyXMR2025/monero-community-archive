---
title: setting config.json to work with ip address instead of url
source_url: https://github.com/xmrig/xmrig/issues/738
author: artemide601
assignees: []
labels: []
created_at: '2018-08-21T23:15:54+00:00'
updated_at: '2018-11-05T14:11:22+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:11:22+00:00'
---

# Original Description
it cn be a silly question, but how i can tell to config.json to use ip address:

in my config.json i have this entry
            "url": "gulf.moneroocean.stream:80", // URL of mining server
I want to replace the url with ip, so i set
            "url": "104.207.130.172:80", // URL of mining server
but this does not work... miner will close immediatelly

any suggestion?

thank you


# Discussion History
## artemide601 | 2018-08-22T16:34:47+00:00
@organizmo why a thumb down ????  :-(

## artemide601 | 2018-08-25T21:48:09+00:00
no one can answer?
so it's not so a easy question....

## Spudz76 | 2018-09-10T08:25:45+00:00
Is that even their IP?  I get `45.32.81.217` while you've used whatever `104.207.130.172.vultr.com` is...

## Spudz76 | 2018-09-10T08:31:14+00:00
Otherwise put into hosts file:
```
104.207.130.172 blahpool
```
and then use
```
 "url": "blahpool:80", // URL of mining server
```
which would go around the bug if it is truly a bug, and hosts file returns the IP without any Internet DNS hits.

## xmrig | 2018-09-10T14:15:18+00:00
Syntax like `"url": "104.207.130.172:80",` is fully correct, there may be another error in the configuration file.
Thank you.

## snipeTR | 2018-09-10T15:40:46+00:00
Please paste both json file

# Action History
- Created by: artemide601 | 2018-08-21T23:15:54+00:00
- Closed at: 2018-11-05T14:11:22+00:00
