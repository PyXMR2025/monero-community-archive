---
title: 240 compiling errors
source_url: https://github.com/xmrig/xmrig/issues/762
author: ghost
assignees: []
labels: []
created_at: '2018-09-22T23:49:45+00:00'
updated_at: '2018-11-05T14:18:55+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:18:55+00:00'
---

# Original Description
why don't you just upload the vs source ...
i generated the project with cmake then included the missing libraries,
and when i was trying to compile i got 240 errors 

# Discussion History
## reeyon | 2018-09-25T04:15:55+00:00
I have problem after compiling in dev branch, the xmrig cannot run due to missing dlls.
![image](https://user-images.githubusercontent.com/3666089/45992480-bce04880-c0bc-11e8-8e1b-70fbb9ae3a52.png)
![image](https://user-images.githubusercontent.com/3666089/45992481-bf42a280-c0bc-11e8-9ef9-6e3a974c54a1.png)


## xmrig | 2018-09-25T07:58:58+00:00
Follow documentation https://github.com/xmrig/xmrig/wiki/Windows-Build and use [xmrig-deps](https://github.com/xmrig/xmrig-deps/releases) if you for some reason don't like use prebuilt libraries, you should use static libraries to avoid such issues.
Thank you.

## reeyon | 2018-09-25T09:07:01+00:00
cmake with the updated xmrig-deps fixed the issue, thanks.

# Action History
- Created by: ghost | 2018-09-22T23:49:45+00:00
- Closed at: 2018-11-05T14:18:55+00:00
