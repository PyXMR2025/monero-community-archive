---
title: version 6.3.5 does not work
source_url: https://github.com/xmrig/xmrig/issues/1902
author: andrexTI
assignees: []
labels:
- question
created_at: '2020-10-16T15:23:06+00:00'
updated_at: '2021-04-12T14:46:19+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:46:19+00:00'
---

# Original Description
Hello everyone, version 6.3.5 does not work on my computers. See the error:

![1](https://user-images.githubusercontent.com/60714578/96276715-bece1a80-0fa9-11eb-85aa-687ef8709d74.png)


With version 6.3.3 everything works fine.

![2](https://user-images.githubusercontent.com/60714578/96276970-0d7bb480-0faa-11eb-9ac7-597324b1eccb.png)


Could someone help me make the new version work?



# Discussion History
## xmrig | 2020-10-16T15:35:20+00:00
Seems you use a different config for both versions and didn't enable TLS `"tls": true,` for 6.3.5.
Thank you.


## andrexTI | 2020-10-16T15:52:13+00:00
That was it, now the new version works. 

Thanks =]

## DeadManWalkingTO | 2020-10-20T21:24:07+00:00
Problem solved.
Now this issue can be closed.
Thank you!

# Action History
- Created by: andrexTI | 2020-10-16T15:23:06+00:00
- Closed at: 2021-04-12T14:46:19+00:00
