---
title: 'XMRIG on alienware R7 - GPU not getting any shares accepted '
source_url: https://github.com/xmrig/xmrig/issues/3459
author: akshay8043
assignees: []
labels: []
created_at: '2024-04-07T17:44:09+00:00'
updated_at: '2025-06-18T22:15:52+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:15:52+00:00'
---

# Original Description
XMRIG on alienware R7

GTX 1080 
nvme ssd with pagefile configured
48gb ram

i dont see my gpu getting any hashes accepted

![image](https://github.com/xmrig/xmrig/assets/32493756/40022c04-0441-42cc-8cdd-d53070cdaab7)


I can see only CPU has accepted shares. can anyone help me with some knowledge. Do i need to stop mining using GTX 1080 GPU? 


or I dont know if gpu has any share accepted even on the API.


2nd Laptop getting error related to AMD GPU RX540, compilation error using the original GPU but when I used this xmrig-AMD compilation is completed. Can someone guide me what do I need to do on original XMRIG binary to ensure that it is compiled correctly. 

Sorry for too many questions in single post.


this image is from xmrig-amd and compilation is completed.
![image](https://github.com/xmrig/xmrig/assets/32493756/2bf50486-3d38-4ec2-9463-d8cef5d45730)




# Discussion History
## SChernykh | 2024-04-07T18:44:20+00:00
With this difficulty, your GPU will find a share only once every 5 minutes on average (it can take longer). RandomX is not recommended for GPUs because they're very inefficient.

## akshay8043 | 2024-04-08T19:44:47+00:00
Thanks,

i saw couple of them accepted. 


# Action History
- Created by: akshay8043 | 2024-04-07T17:44:09+00:00
- Closed at: 2025-06-18T22:15:52+00:00
