---
title: Issue with HTTP API
source_url: https://github.com/xmrig/xmrig/issues/3221
author: chapst1ck
assignees: []
labels: []
created_at: '2023-03-01T16:42:37+00:00'
updated_at: '2023-03-01T18:59:29+00:00'
type: issue
status: closed
closed_at: '2023-03-01T17:13:16+00:00'
---

# Original Description
Trying to make changes in config like this:
`curl -v -d '{"color":false}' -X PUT -H 'Content-Type: application/json' -H "Authorization: Bearer CHERRY" http://127.0.0.1:80/1/config`

In result I get:
```
{
    "status": 400,
    "error": "Bad Request"
}
```
Сan you tell me where I made a mistake?

# Discussion History
## Spudz76 | 2023-03-01T16:49:47+00:00
You have to send a complete config.json content object not just single entries.  Like the route overwrites the current config.json just like if you scp'd it.

## Spudz76 | 2023-03-01T16:50:36+00:00
So, you do a GET request to download the active full config.json, modify the entry you want to change, then PUT the whole thing back.

## chapst1ck | 2023-03-01T17:13:16+00:00
Oh, now I understand it. Thanks.

## Spudz76 | 2023-03-01T18:59:28+00:00
The API docs are way out of date, I updated them a long time ago and it still isn't merged.  You can view the updated [API.md here](https://github.com/xmrig/xmrig/blob/ddf304620575218bbb4b91cd205c99c486238f86/doc/API.md#apiversion-2-1).

You should be using `/2/config` not the old version route.

# Action History
- Created by: chapst1ck | 2023-03-01T16:42:37+00:00
- Closed at: 2023-03-01T17:13:16+00:00
