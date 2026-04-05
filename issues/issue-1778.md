---
title: API with per GPU not per thread results
source_url: https://github.com/xmrig/xmrig/issues/1778
author: tymoteuszrogalewski
assignees: []
labels:
- question
created_at: '2020-07-14T12:27:33+00:00'
updated_at: '2020-07-14T13:44:43+00:00'
type: issue
status: closed
closed_at: '2020-07-14T13:44:43+00:00'
---

# Original Description
Hi, we are using this command line for fetching results
curl -s http://127.0.0.1:3333/1/summary
but see there is only per threads results with hashrates, nor per GPU.
Sometimes there are more threads than GPUs in rig and from this info we dont know which treads is to which GPU cards.

Could you help us or add another array in results with per gpu results or threads to GPUs relations?

Thanks

# Discussion History
## xmrig | 2020-07-14T12:59:04+00:00
You can use http://127.0.0.1:3333/2/backends for it.

For OpenCL where possible multiple threads per GPU you must combine results on your side to view summary per GPU, example how it looks like http://workers.xmrig.info/
Thank you.


## tymoteuszrogalewski | 2020-07-14T13:44:43+00:00
Thank you very much. The "backends" is good information and now our script is working good ;-)

# Action History
- Created by: tymoteuszrogalewski | 2020-07-14T12:27:33+00:00
- Closed at: 2020-07-14T13:44:43+00:00
