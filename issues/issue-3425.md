---
title: 'Read error : "end of file'
source_url: https://github.com/xmrig/xmrig/issues/3425
author: Alfrass
assignees: []
labels: []
created_at: '2024-02-20T02:24:28+00:00'
updated_at: '2025-06-18T22:16:26+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:16:26+00:00'
---

# Original Description
Hi,

I got an Read error : "end of file" message
![image](https://github.com/xmrig/xmrig/assets/91729705/3cae3ddb-baa2-4982-b0f6-e02682ab0713)

See the config.json that I have
[config.json](https://github.com/xmrig/xmrig/files/14338648/config.json)

I try to used one batch too the one on .txt which I changed on .bat of course
[Run.txt](https://github.com/xmrig/xmrig/files/14338659/Run.txt)

If I can have some help please







# Discussion History
## geekwilliams | 2024-02-20T02:38:22+00:00
Can you try to navigate to [https://us2.nexellia.herominers.com:1143](https://us2.nexellia.herominers.com:1143) in a browser on the same computer you're mining from? You should get a message that says "Mining Server Online"  

Otherwise, you may have a network issue blocking access to that server 

## Alfrass | 2024-02-20T03:06:42+00:00
Yes right I got the message "Mining Server Online"

## geekwilliams | 2024-02-20T05:18:21+00:00
Try removing --tls from your command to start 

## SChernykh | 2024-02-20T08:59:07+00:00
Actually, you need to do the opposite. You have `"tls": false,` in config.json, you need to set it to true. `us2.nexellia.herominers.com:1143` is a tls port.

## Alfrass | 2024-02-21T00:31:39+00:00
Yes I have try the both still the same error...

## d4f5409d | 2024-02-26T15:07:18+00:00
Same issue sometimes appears on Linux too (self-built)

# Action History
- Created by: Alfrass | 2024-02-20T02:24:28+00:00
- Closed at: 2025-06-18T22:16:26+00:00
