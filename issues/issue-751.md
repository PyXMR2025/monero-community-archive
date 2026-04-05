---
title: API Keeps Failing w/ Error Code 0
source_url: https://github.com/xmrig/xmrig/issues/751
author: LPX55
assignees: []
labels:
- question
created_at: '2018-09-11T12:48:59+00:00'
updated_at: '2018-10-10T22:21:21+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:21:21+00:00'
---

# Original Description
1. I made sure the port being used is open
2. Used all sorts of CORS tools to no avail
3. I've even tried the front-end tools available on Github

At this point I'm about to just use Apache to serve the endpoint... any ideas?

Settings:

--api-port 88 --api-worker-id LDADC1 --api-access-token <redacted> 

Request being made: 

curl -X GET -v -i 'http://159.xx.xx.xxx:88?api-access-token=<redacted>'


# Discussion History
## xmrig | 2018-09-11T16:23:17+00:00
https://github.com/xmrig/xmrig-proxy/issues/40#issuecomment-370202169 Only possible way is use `Authorization` header.
Thank you.

# Action History
- Created by: LPX55 | 2018-09-11T12:48:59+00:00
- Closed at: 2018-10-10T22:21:21+00:00
