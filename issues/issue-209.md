---
title: RPC getblocktemplate not return POW Cummulate or other information
source_url: https://github.com/monero-project/monero/issues/209
author: perl5577
assignees: []
labels: []
created_at: '2015-01-05T21:29:02+00:00'
updated_at: '2015-01-05T22:17:04+00:00'
type: issue
status: closed
closed_at: '2015-01-05T22:17:04+00:00'
---

# Original Description
Present, getblocktemplate return only blob and height of blocktemplate .
No code can make difference between block 325454 and block 325454 result new branch after fork .

Present ,All pool continue mining for previous blocktemplate and not blocktemplate generate per new branch .

Exemple of attack.

1.) Pool mining regular .
When one miner find diff more 500% of diff research Ex: block 325454
Submit block 325454 and not broacast block  
Other pool continue mining of block 325454 and heavy pool mining block 325455

2a ) Other pool find block 325454 ( Jackpot )
Wait 5 secondes and broacast block with diff more 500% . Blockchain fork and new branch is create .
All other pool continue mining of badblock 325455 

You are all time for find block 325455 ( only solo mining for concurence )

Attack is easy is block diff is per exemple 500% not broadcast and mining next block .
If same block is find per network broadcast block with diff 500% and continue mining on solo .

All pool as block find reject per bitmonerod.


# Discussion History
## perl5577 | 2015-01-05T21:31:20+00:00
This is an example not violent. Attack can be optimized to take all the block with 15% of hashrate


## perl5577 | 2015-01-05T21:32:18+00:00
Of course my pool not using the attack 


## fluffypony | 2015-01-05T21:36:16+00:00
You're incorrect - getblocktemplate returns more than that, and it definitely returns the difficulty.

Per https://github.com/monero-project/bitmonero/blob/master/src/rpc/core_rpc_server_commands_defs.h#L383 -

```
    struct response
    {
      uint64_t difficulty;
      uint64_t height;
      uint64_t reserved_offset;
      blobdata blocktemplate_blob;
      std::string status;
```


## perl5577 | 2015-01-05T22:14:47+00:00
How make difference between 

block bad branch 
DIFF 145
height 14
reserved_offset 400
blocktemplate_blob XXXXXXXXXXXXXXXXXXXXX
status : OK

block good branch after reorganize blockchain with same height
DIFF 145
height 14
reserved_offset 400
blocktemplate_blob XXXXXXXXXXXXXXXXXXXXX
status : OK


## fluffypony | 2015-01-05T22:17:04+00:00
Though the longest chain rule. The longest chain may take many blocks to find, but that's the way it works. There's literally no change we can make to getblocktemplate to circumvent or change this basic nature of a consensus system. I would suggest you read up on the longest chain rule.


# Action History
- Created by: perl5577 | 2015-01-05T21:29:02+00:00
- Closed at: 2015-01-05T22:17:04+00:00
