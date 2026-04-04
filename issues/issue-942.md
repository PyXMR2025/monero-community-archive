---
title: 'OSX issues - Abort trap: 6'
source_url: https://github.com/monero-project/monero/issues/942
author: ManfredKarrer
assignees: []
labels: []
created_at: '2016-07-31T20:04:02+00:00'
updated_at: '2016-08-01T14:15:06+00:00'
type: issue
status: closed
closed_at: '2016-08-01T14:15:06+00:00'
---

# Original Description
I get always an "Abort trap: 6" when running bitmonerod and simplewallet.
I installed a nightly build but its the same problem.

bitmonerod also logs:
2016-Jul-30 14:23:02.279945 [P2P8][93.81.51.138:59835 INC]Sync data returned unknown top block: 1102568 -> 1009962 [92606 blocks (-64 days) ahead] 

I tried a few times (with the older official download) to re-download the blockchain but without success.

Someone in the IRC recommended me a to set a flag, but forgot which one. 

I am on OSX  10.9.5.


# Discussion History
## moneromooo-monero | 2016-08-01T12:04:24+00:00
Add --max-concurrency 1


## ManfredKarrer | 2016-08-01T13:38:57+00:00
was first working (SYNCHRONIZED OK) but then i got again the 
Sync data returned unknown top block: 1104056 -> 1009962 [94094 blocks (-65 days) ahead] 


## radfish | 2016-08-01T14:09:07+00:00
That warning is harmless. Use 'status' command to check the block number your node is at.


## ManfredKarrer | 2016-08-01T14:15:01+00:00
ah ok. yeah seem the simplewallet works now again. thanks!
i think the log msg shoudl be changed, its confusing...


# Action History
- Created by: ManfredKarrer | 2016-07-31T20:04:02+00:00
- Closed at: 2016-08-01T14:15:06+00:00
