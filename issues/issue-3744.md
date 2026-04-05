---
title: Can't execute it via liunx sh.
source_url: https://github.com/xmrig/xmrig/issues/3744
author: koseiizawa
assignees: []
labels: []
created_at: '2025-12-20T09:28:17+00:00'
updated_at: '2025-12-22T00:56:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I can't execute it via linux sh cli.

**To Reproduce**
unexpected error `(` : line 1. :)

**Required data**
 - XMRig latest version

# Discussion History
## geekwilliams | 2025-12-20T17:53:08+00:00
Please show the full command you're using to execute xmrig

Also kindly provide information about the system you're attempting to run xmrig on.   

## koseiizawa | 2025-12-22T00:47:41+00:00
./xmrig -o pool.supportxmr.com:443 -u <wallet_address>.$(hostname | tr '.' '_') -p x --threads=4 --max-cpu-usage=75 --tls &

I'm using the linux system.

## geekwilliams | 2025-12-22T00:56:15+00:00
In theory your command should work.  Are you running this manually or via cron or some other script?   

Are you sure you have the right xmrig build for your system?  There are separate builds for 32/64 bit and also ARM. 

Where exactly are you seeing the error message you posted? Screenshot from a terminal would be helpful.  

# Action History
- Created by: koseiizawa | 2025-12-20T09:28:17+00:00
