---
title: 'New install CLI, can''t transfer on testnet: Change Address it not Ours +
  Balance gone'
source_url: https://github.com/monero-project/monero/issues/5786
author: krtschmr
assignees: []
labels: []
created_at: '2019-08-01T09:28:13+00:00'
updated_at: '2019-10-28T17:17:49+00:00'
type: issue
status: closed
closed_at: '2019-10-28T17:03:54+00:00'
---

# Original Description
- brand new Ubuntu Desktop VM
- downloaded CLI from getmonero  `monero-x86_64-linux-gnu`
- run daemon `--testnet`
- created new wallet `
- i received 100 XMR via Reddit user. TX > 80 confirmations
- i try to send X to myself (subaddress or primary address). 
- everytime i receive error: _change address is not ours_
- i try to send 100 XMR to myself, not enough unlocked balance
- i use `sweep_all` to my own address. transaction was created and send out
- the money is literally gone - or at least won't show in my wallet anymore
![image](https://user-images.githubusercontent.com/13366714/62282189-544ebe80-b479-11e9-8010-93a330f9c5dc.png)

bonus for: why is my shell so weired displayed?


interesting: 

![image](https://user-images.githubusercontent.com/13366714/62281924-d5598600-b478-11e9-9232-2f535ca57ef9.png)

so something seems to be broken. maybe it was the wallet generation

`./monero-wallet-cli --testnet --subaddress-lookahead 0:20000 --generate-new-wallet hotwallet`

this is the seed , maybe someone can see where the funds went.

![image](https://user-images.githubusercontent.com/13366714/62282080-24072000-b479-11e9-99e8-51dd975ccdcf.png)



# Discussion History
## trasherdk | 2019-08-01T11:10:02+00:00
I believe there's a bug in the downloadable release `v0.14.1.2` that looks pretty much like your screen shots.  
Either compile `v0.14.1.2` from source, or download `v0.14.1.0`.

## trasherdk | 2019-08-01T11:13:22+00:00
Mining on `testnet`:
```
Height 1267889, txid <a6bca38d9665510aa212815949a62ff881f2e865552fffce69c9b8809adc64f1>, 10.805454574681, idx 0/0
Height 1267893, txid <92f9ce1f25b48e62fa3bc0a007f66bc383fa82dafbf7466d7da7132fe3b51055>, 5.402675763106, idx 0/0
Height 1267902, txid <315637954b2f30060ac09181606aa3c9ba06bc55637d8b9d9a523fb336707159>, 5.402603630015, idx 0/0
Height 1267906, txid <1bc5ecbf5469e9ea865c4959c567b970aed33c0e8c1ddaf69ba81ccf26d8391c>, 16.207687234635, idx 0/0
Height 1267912, txid <5b8846ec8ebc55d345993451bc0bad18e256b6bb8f5f2cac204bf2df49089a03>, 10.804990864370, idx 0/0
Height 1267921, txid <9a0d1b3eb08a14edf9fd2d97e7686fed0b0f0dac022f70a179c95daf4b7e2a5c>, 10.804805385868, idx 0/0
Height 1267925, txid <564ad33ee828b29c29b75b181e40abdfada83d677f66f9718fabdfb4d988b28e>, 10.804722951937, idx 0/0
Height 1267934, txid <74f10040a90504928385e592985ff0728cfe0f9dd1ce7cc193ba5db9c23c8aa1>, 21.609604354382, idx 0/0
Height 1267939, txid <3aa73047cfed75b62c10b0b21dd11261620c99389c83c32c9dc1bd78dc5c82e4>, 5.402201763280, idx 0/0
Height 1267945, txid <01e9a07fed90bc29630d0d50ecb4030871ee3031c958aca5da6a704f4cbc7052>, 5.402191459399, idx 0/0
Height 1267950, txid <139c0afc126e9f7b128fd7356589fb0e251e8a4b7b3374d85ca3531826769811>, 10.804228361863, idx 0/0
Height 1267960, txid <8d808f4d2c9d5be85077d8ed278e753f67759413d588ff37aa9390060c394c69>, 21.608044578856, idx 0/0
Height 1267964, txid <86f182ea954c944b4eb774896f84a22b2e8a03bfd39743cf32ed72d4f6b5c4c6>, 5.401964778963, idx 0/0
Height 1267975, txid <bf6f52a631ff37c238d9ccf88d44fdaa93d77e561953fb54b59fabee39f4c400>, 27.009694166519, idx 0/0
Height 1267977, txid <daf7833589e3f549de2dd4837ab8a303446508fada31a381e4b8fc598869d03a>, 5.401810229574, idx 0/0
Height 1267982, txid <c00576f9ad56bf6b8c5baeecb4c2dd21fe1409be47f31f0c2119e73acbc5b204>, 5.401779320227, idx 0/0
Height 1267989, txid <0cd4b9da6c50084a2d49627683d1b988ccc6c79d1dd818d82cc29a18539a7dcd>, 16.205647019689, idx 0/0
Height 1267994, txid <6e86a471686a28077999af3bbf1df647918a4383816a08d809fcdfd25f7db4b8>, 16.204987659622, idx 0/0
Height 1267997, txid <488457724352e5818954789e8e63230f47affc1cec23123561143717426c0d1e>, 10.803843744090, idx 0/0
[wallet 9zwQfv]: balance 
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 17689.607314966405, unlocked balance: 17678.803471222315 (3 block(s) to unlock)
```


## krtschmr | 2019-08-01T11:19:16+00:00
i can add: 
i created stagenet wallet  and didn't receive funds. same issue.

recreated same wallet with seed, funds received.



## moneromooo-monero | 2019-08-19T15:06:15+00:00
You're asking the wallet to create 0 accounts.

That particular value should be forbidden I suppose.

## krtschmr | 2019-08-19T15:07:43+00:00
@moneromooo-monero not sure tho. what happened is: i've recreated the wallet with the seed and then the funds been available. 


## moneromooo-monero | 2019-08-19T15:08:52+00:00
Following your steps works for me, without the lookahead. I get your results with the lookahead. I'll PR a change to forbid 0.

## moneromooo-monero | 2019-10-28T16:56:34+00:00
That got merged a while back.

+resolved

# Action History
- Created by: krtschmr | 2019-08-01T09:28:13+00:00
- Closed at: 2019-10-28T17:03:54+00:00
