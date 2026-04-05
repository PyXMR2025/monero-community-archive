---
title: 'Can''t Bind memory '
source_url: https://github.com/xmrig/xmrig/issues/3322
author: Miooiio
assignees: []
labels: []
created_at: '2023-08-23T01:24:40+00:00'
updated_at: '2025-06-16T19:57:10+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:57:10+00:00'
---

# Original Description
My server is a 2* EPYC 7551 chip and when I run . /xmrig --coin=XMR -o <poollink>:65501 -u <walletid> -p x --cpu-affinity=0x00000000FFFC0000 
It reports error CPU #01-54 warning: "can't bind memory"
This is my memory alignment: 
P1-DIMMA1: 16 GB DDR4 @ 2667 MHz HMA82GR7AFR4N-VK    
P1-DIMME1: 16 GB DDR4 @ 2667 MHz HMA82GR7AFR4N-VK    
P2-DIMMA1: 16 GB DDR4 @ 2667 MHz HMA82GR7AFR4N-VK   
P2-DIMME1: 16 GB DDR4 @ 2667 MHz HMA82GR7AFR4N-VK    
Note: To save space, the mining address and wallet address are referred to by poollink and walletid.

# Discussion History
## SChernykh | 2023-08-23T07:15:08+00:00
Can you show the screenshot of xmrig when it starts and shows this error? This will give much more information.

# Action History
- Created by: Miooiio | 2023-08-23T01:24:40+00:00
- Closed at: 2025-06-16T19:57:10+00:00
