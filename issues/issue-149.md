---
title: How does http api work?
source_url: https://github.com/xmrig/xmrig/issues/149
author: TheUnity
assignees: []
labels:
- question
created_at: '2017-10-10T23:56:56+00:00'
updated_at: '2017-10-15T09:23:44+00:00'
type: issue
status: closed
closed_at: '2017-10-15T09:23:44+00:00'
---

# Original Description
How does http api work? I wrote port, token and id in config. Show me example of GET, plz.

# Discussion History
## xmrig | 2017-10-11T00:23:44+00:00
1. Choice some port for api, for example `8080`.
2. Set `access-token` to `null` it important.
3. Run the miner, if try access to API from same machine, open in browser http://127.0.0.1:8080/

For how use access token please check sample page https://gist.github.com/xmrig/c75fdd1f8e0f3bac05500be2ab718f8e

## TheUnity | 2017-10-11T12:43:14+00:00
Thank you

# Action History
- Created by: TheUnity | 2017-10-10T23:56:56+00:00
- Closed at: 2017-10-15T09:23:44+00:00
