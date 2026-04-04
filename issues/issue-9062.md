---
title: Monerod crashing on Macbook Pro M1
source_url: https://github.com/monero-project/monero/issues/9062
author: thankfulfornever
assignees: []
labels: []
created_at: '2023-11-07T14:51:11+00:00'
updated_at: '2023-11-07T18:36:47+00:00'
type: issue
status: closed
closed_at: '2023-11-07T17:37:42+00:00'
---

# Original Description
Monerod --log-level 2 output: https://paste.debian.net/hidden/cb58677a/

Mdb_stat output: https://paste.debian.net/hidden/39140c0b/

I've had this problem for a while. Seems it is related to RandomX. I recently tried rebuilding as I thought that it might be fixed with RandomX v1.2.1, which merged [issue 259](https://github.com/tevador/RandomX/pull/259) related to Apple silicon, but this doesn't seem to have helped.

Any ideas?

Edit: Forgot to add that my M1 Pro has 32GB of RAM and is on MacOS Sonoma 14.1

Edit 2: Whoops I see that RandomX 1.2.1 is not in the most recent tag. I'll rebuild off master and see if that helps...

# Discussion History
## thankfulfornever | 2023-11-07T17:37:42+00:00
Well what do you know. Solved my own problem. 

For future readers, this fix for Apple CPUs will be included in a future Monero release, so this issue is unlikely to rise up again.

## hyc | 2023-11-07T17:53:02+00:00
The actual change that fixed this was in https://github.com/tevador/RandomX/pull/281

## thankfulfornever | 2023-11-07T18:36:47+00:00
Ah good to know. Thanks Hyc. Either way, building from Master solved this issue, and it will be included in the next Monero release.

Have ALWAYS appreciated the hard work you've done for Monero. Thanks again.

# Action History
- Created by: thankfulfornever | 2023-11-07T14:51:11+00:00
- Closed at: 2023-11-07T17:37:42+00:00
