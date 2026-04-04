---
title: impossible with RPC call determine if chain fork or not fork
source_url: https://github.com/monero-project/monero/issues/1202
author: perl5577
assignees: []
labels: []
created_at: '2016-10-10T18:03:02+00:00'
updated_at: '2016-12-15T16:11:30+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:11:30+00:00'
---

# Original Description
/getheight 
Return only last height if new block is find with same height.

T0 network find block 85145 hash 000xxxx44
T0+1  /getheight  return 85145 
T0+2  Get blocktemplate  85145 hash 000xxxx44

T1 network find block 85144 
T1 network find block 85145  hash 000xxxx7e
T1+1  /getheight  return 85145   ( I mine allway bad block )

If get blocktemplate directly , I can estimate good fork with difficulty of block


# Discussion History
## moneromooo-monero | 2016-10-10T19:49:58+00:00
There is a getinfo which returns both height and top block hash.


## perl5577 | 2016-10-12T01:42:58+00:00
getinfo not return information for détermin best chain .
top_block_hash is empty from long time .

if information is present , I can not make response follow question :+1: 

Methode for detect fork without read log ?

Compare many daemon ? And find best chain ?

I think need information like SUM(Diff) is necessary .


## perl5577 | 2016-10-12T02:02:47+00:00
I open other issue for get_info write error data 


## moneromooo-monero | 2016-10-12T08:19:02+00:00
Add another bug for adding cumulative diff to get_info, please, and we'll do that.


## moneromooo-monero | 2016-10-15T15:39:51+00:00
You now have top hash and cumulative difficulty in PRs.
target_height is only used when batch syncing, not in "normal" keeping up with the network.


## luigi1111 | 2016-12-15T16:11:30+00:00
Desired functionality added in response to #1210 and #1211 

# Action History
- Created by: perl5577 | 2016-10-10T18:03:02+00:00
- Closed at: 2016-12-15T16:11:30+00:00
