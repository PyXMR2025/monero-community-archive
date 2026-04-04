---
title: Transaction relay not aligning with consensus rules
source_url: https://github.com/monero-project/monero/issues/1860
author: Gingeropolous
assignees: []
labels: []
created_at: '2017-03-10T02:10:36+00:00'
updated_at: '2023-08-26T17:07:32+00:00'
type: issue
status: closed
closed_at: '2023-08-26T17:07:32+00:00'
---

# Original Description
There is a transaction in the mempool as of 2017-03-09 ( 3d32acc7359c1fd8ac585f927582d0e4f5a0ce97733da3f2cfcabe11b28912e1 ) that has a mixin of 1 and is a non-RingCT transaction. This transaction was observed on multiple nodes, so it was relayed. 

Edited to add: The concern is that this makes it easy to spam the network with transactions that will never get mined but will get relayed to all nodes and fill up the mempool, and the transactions will never get mined so its effectively costless. 

```
2017-03-10 02:09:52.826	    7f4ef1ded740	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Found in pool
010001028080bb8b939b4402a42af713a2e1f563129bddc921ae9058d115db18e4af684a4c20ae836b6cdc0abc736a03068088aca3cf02026d5101198a9a7a04587d3ae0741baa09328ddf66fbf4ffb2b95311795c0e75e580d0dbc3f4020284d90734310ca002423397724970186d258474dc901a0324bb01e34329c2faef8080dd9da4170264c7b60af446ddfa5712d52b912722e19f3111d38b4afb3d369c174a1bd4a9b180a0b6cef7850202483549d6b184688c5fc2a96bf6298d956ee053e257d4a2f27ce58bbbaa37da1e80c09e90acbb1402fb21d786e2bea604245385d027286f6e19c228e43e1c9fde5771a3b427339cae8080d287e2bc2d027c79c51259a57a23bd2994f5f0fe6d32501f0b3f9cef478e7fa78926b5b27b112c01f5707bef4a294d1eaca8069ecfb34d2a6b152f85da48bc3868833bb9f1ba0d3902090134084e14962d19f9cfa64d926b17024c906cc5b007a2832a5cd47ad93cd000975ded0722f36be706329bf2364e1ff61f1aa444132a9f5cab028492441c8b5721af2330c6fa211704b9555b53b947023b5c9479c766989da475405d94e215971d9c1e613e119c7d02421b3616fafd370adc694975cc1e2cb548d220e7d271a52839f7a7b86945e10d
{
  "version": 1, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 300000000000000, 
        "key_offsets": [ 5412, 2551
        ], 
        "k_image": "a2e1f563129bddc921ae9058d115db18e4af684a4c20ae836b6cdc0abc736a03"
      }
    }
  ], 
  "vout": [ {
      "amount": 90000000000, 
      "target": {
        "key": "6d5101198a9a7a04587d3ae0741baa09328ddf66fbf4ffb2b95311795c0e75e5"
      }
    }, {
      "amount": 100000000000, 
      "target": {
        "key": "84d90734310ca002423397724970186d258474dc901a0324bb01e34329c2faef"
      }
    }, {
      "amount": 800000000000, 
      "target": {
        "key": "64c7b60af446ddfa5712d52b912722e19f3111d38b4afb3d369c174a1bd4a9b1"
      }
    }, {
      "amount": 9000000000000, 
      "target": {
        "key": "483549d6b184688c5fc2a96bf6298d956ee053e257d4a2f27ce58bbbaa37da1e"
      }
    }, {
      "amount": 90000000000000, 
      "target": {
        "key": "fb21d786e2bea604245385d027286f6e19c228e43e1c9fde5771a3b427339cae"
      }
    }, {
      "amount": 200000000000000, 
      "target": {
        "key": "7c79c51259a57a23bd2994f5f0fe6d32501f0b3f9cef478e7fa78926b5b27b11"
      }
    }
  ], 
  "extra": [ 1, 245, 112, 123, 239, 74, 41, 77, 30, 172, 168, 6, 158, 207, 179, 77, 42, 107, 21, 47, 133, 218, 72, 188, 56, 104, 131, 59, 185, 241, 186, 13, 57, 2, 9, 1, 52, 8, 78, 20, 150, 45, 25, 249
  ], 
  "signatures": [ "cfa64d926b17024c906cc5b007a2832a5cd47ad93cd000975ded0722f36be706329bf2364e1ff61f1aa444132a9f5cab028492441c8b5721af2330c6fa211704b9555b53b947023b5c9479c766989da475405d94e215971d9c1e613e119c7d02421b3616fafd370adc694975cc1e2cb548d220e7d271a52839f7a7b86945e10d"]
}
```

# Discussion History
## moneroexamples | 2017-03-17T03:10:39+00:00
Again same issue. But this time not only relyed, but they are being mined and included in a blockchian. Txs with mixin 0 are being mined and included in blockchain. How come?

https://xmrchain.net/tx/829c938ac8272879e86a7457ce85d9bb00b068f37102096a543488e21ff20770
https://xmrchain.net/tx/7d3a5d89a1e9ecf34aa4691121af67b914d72df86451dc9a5f944ceb6e003435

Should txs with mixin 0 be not allowed by now? 



## kenshi84 | 2017-03-17T05:22:53+00:00
/u/yuvzst pointed out that they are just dust being swept: https://www.reddit.com//r/Monero/comments/5zv9z8/have_txs_with_mixin_0_been_banned_or_not/

## moneroexamples | 2017-03-17T08:00:26+00:00
@kenshi84  

Thanks. I know now.

## Gingeropolous | 2017-03-22T15:41:03+00:00
@kenshi84 , @moneroexamples , my original case is distinct from the mixin 0 that are dust being swept.

Indeed, as of writing, the mixin 1 transaction is *still* in the mempool.

https://xmrchain.net/tx/3d32acc7359c1fd8ac585f927582d0e4f5a0ce97733da3f2cfcabe11b28912e1



## moneromooo-monero | 2017-04-14T22:05:57+00:00
Do you know if that tx had kept_by_block: T ? Since probably not, if you see this again, can you check (print_pool_sh will show it) ?

## Gingeropolous | 2023-08-26T17:07:32+00:00
I feel like this has been resolved. 

# Action History
- Created by: Gingeropolous | 2017-03-10T02:10:36+00:00
- Closed at: 2023-08-26T17:07:32+00:00
