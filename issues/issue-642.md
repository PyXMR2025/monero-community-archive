---
title: xmrig using all pagefile, even with huge pages disabled
source_url: https://github.com/xmrig/xmrig/issues/642
author: shigutso
assignees: []
labels:
- bug
created_at: '2018-05-21T13:31:18+00:00'
updated_at: '2018-06-17T18:01:25+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:01:25+00:00'
---

# Original Description
After leaving xmrig (cpu) mining for a while, I realized that the pagefile.sys file in windows got very large (10GB+) and the computer hangs after ~48h.

I thought that it was a problem with huge pages and then tried to disable it, but the issue persisted

Is there anything else I can do to stop xmrig from using a lot of the windows pagefile?

Thanks

# Discussion History
## xmrig | 2018-05-21T13:54:45+00:00
Sounds like memory leak, can you make screenshot of Task Manager where I can see miner process really eats memory and please provide all possible information, including config files (without wallets).
Thank you.

## shigutso | 2018-05-21T14:27:38+00:00
Thanks, I'll be updating to the latest version to see if it fixes the problem, if it doesn't I'llvpost here my full specs and config files

The task manager shows xmrig using as low as 10MB of RAM, but the pagefile on Windows just keeps getting bigger and bigger until the OS crashes, it's very odd, and if I just restart xmrig, the pagefile frees up memory and the process of growing slowly starts again

## xmrig | 2018-05-30T09:10:29+00:00
Any updates? Is issue solved by updating to latest version?
Thank you.

# Action History
- Created by: shigutso | 2018-05-21T13:31:18+00:00
- Closed at: 2018-06-17T18:01:25+00:00
