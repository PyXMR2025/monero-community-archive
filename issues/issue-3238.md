---
title: HTTP API / 401 - Unauthorized
source_url: https://github.com/xmrig/xmrig/issues/3238
author: FSOL-XDAG
assignees: []
labels: []
created_at: '2023-03-28T08:45:19+00:00'
updated_at: '2023-03-28T09:57:41+00:00'
type: issue
status: closed
closed_at: '2023-03-28T09:57:40+00:00'
---

# Original Description
Hello ! 

I'm trying to use HTTP API (XMRig 6.19.1). I've read [this documentation](https://github.com/xmrig/xmrig/blob/ddf304620575218bbb4b91cd205c99c486238f86/doc/API.md#apiversion-2-1) and modify config.json file : 

![image](https://user-images.githubusercontent.com/128682335/228179845-30f3cb8b-aea0-4c2b-8600-f230cfb3fa87.png)

Then in browser, I try `http://localhost:44441/2/summary` and I still get this : 

![image](https://user-images.githubusercontent.com/128682335/228180476-0f4b57f1-470c-43cf-a44f-42bd33e4fe77.png)

In XMRig log, I see request : 

![image](https://user-images.githubusercontent.com/128682335/228180676-ca5d886a-52b4-4ada-ad42-c3516cdd52c1.png)

Did I make something wrong ? 🫤

Thanks for your help. Regards.

# Discussion History
## FSOL-XDAG | 2023-03-28T09:23:59+00:00
Edit : 

Ok, it's working when I set `"restricted": true` .

Why ? 

## SChernykh | 2023-03-28T09:44:48+00:00
Because `"restricted": false,` requires you to use access-token. You can't have both restricted = false and a null token.

## FSOL-XDAG | 2023-03-28T09:57:40+00:00
Thanks ! 

# Action History
- Created by: FSOL-XDAG | 2023-03-28T08:45:19+00:00
- Closed at: 2023-03-28T09:57:40+00:00
