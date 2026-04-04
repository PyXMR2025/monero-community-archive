---
title: Not enough outputs to choose from, but wallet returns error that amount is
  not enough
source_url: https://github.com/monero-project/monero/issues/6320
author: rating89us
assignees: []
labels: []
created_at: '2020-02-06T21:09:47+00:00'
updated_at: '2020-02-06T21:39:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Transaction amount: 0.000001
Fee priority: Slow (0.2x fee)

Error screenshot (GUI):
![image](https://user-images.githubusercontent.com/45968869/73978523-c6262a00-492c-11ea-89a8-88b301e6a273.png)

Log (console):
```
2020-02-06 21:01:15.131	D transfer: adding 0.000001000000, for a total of 0.000001000000
2020-02-06 21:01:15.131	D estimated bulletproof rct tx size for 1 inputs with ring size 11 and 2 outputs: 1736 (800 saved)
2020-02-06 21:01:15.131	D Candidate subaddress index for spending: 0
2020-02-06 21:01:15.131	D Candidate subaddress index for spending: 1
2020-02-06 21:01:15.131	D Candidate subaddress index for spending: 2
2020-02-06 21:01:15.131	D Candidate subaddress index for spending: 3
2020-02-06 21:01:15.131	D Candidate subaddress index for spending: 4
2020-02-06 21:01:15.131	D Candidate subaddress index for spending: 5
2020-02-06 21:01:15.131	D estimated bulletproof rct tx size for 1 inputs with ring size 11 and 2 outputs: 1736 (800 saved)
2020-02-06 21:01:15.131	D estimated bulletproof rct tx size for 2 inputs with ring size 11 and 2 outputs: 2565 (1536 saved)
2020-02-06 21:01:15.131	D Ignoring output 25 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 206 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 231 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 238 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 244 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 256 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 259 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 265 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 269 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 272 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 275 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 277 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 279 of amount 0.000000100000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 280 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 282 of amount 0.000010370000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.131	D Ignoring output 283 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 284 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 289 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 291 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 292 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 295 of amount 0.000000100000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 296 of amount 0.000000100000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 298 of amount 0.000001000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 300 of amount 0.000000100000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Ignoring output 303 of amount 0.000010000000 which is below fractional threshold 0.000010689955
2020-02-06 21:01:15.132	D Starting with 1 non-dust outputs and 0 dust outputs
2020-02-06 21:01:15.132	D checking preferred
2020-02-06 21:01:15.132	D estimated bulletproof rct tx size for 2 inputs with ring size 11 and 2 outputs: 2565 (1536 saved)
2020-02-06 21:01:15.132	D pick_preferred_rct_inputs: needed_money 0.000034080000
2020-02-06 21:01:15.132	D Considering input 25, 0.000001000000
2020-02-06 21:01:15.132	D Considering input 206, 0.000010000000
2020-02-06 21:01:15.132	D Considering input 231, 0.000010000000
2020-02-06 21:01:15.132	D Considering input 238, 0.000010000000
2020-02-06 21:01:15.132	D Considering input 244, 0.000010000000
2020-02-06 21:01:15.132	D Considering input 256, 0.000010000000
2020-02-06 21:01:15.132	D Considering input 259, 0.000001000000
2020-02-06 21:01:15.132	D Considering input 265, 0.000010000000
2020-02-06 21:01:15.132	D Considering input 269, 0.000001000000
2020-02-06 21:01:15.132	D Considering input 272, 0.000010000000
2020-02-06 21:01:15.132	D Considering input 275, 0.000001000000
2020-02-06 21:01:15.133	D Considering input 277, 0.000001000000
2020-02-06 21:01:15.133	D Considering input 279, 0.000000100000
2020-02-06 21:01:15.133	D Considering input 280, 0.000001000000
2020-02-06 21:01:15.133	D Considering input 282, 0.000010370000
2020-02-06 21:01:15.133	D Considering input 283, 0.000001000000
2020-02-06 21:01:15.133	D Considering input 284, 0.000010000000
2020-02-06 21:01:15.133	D Considering input 289, 0.000001000000
2020-02-06 21:01:15.133	D Considering input 291, 0.000010000000
2020-02-06 21:01:15.133	D Considering input 292, 0.000010000000
2020-02-06 21:01:15.133	D Considering input 295, 0.000000100000
2020-02-06 21:01:15.133	D Considering input 296, 0.000000100000
2020-02-06 21:01:15.133	D Considering input 298, 0.000001000000
2020-02-06 21:01:15.133	D Considering input 300, 0.000000100000
2020-02-06 21:01:15.133	D Considering input 301, 0.000015800000
2020-02-06 21:01:15.133	D done checking preferred
2020-02-06 21:01:15.133	D Start of loop with 1 0, tx.dsts.size() 0
2020-02-06 21:01:15.133	D unused_transfers_indices: 301
2020-02-06 21:01:15.133	D unused_dust_indices: 
2020-02-06 21:01:15.133	D dsts size 1, first 0.000001000000
2020-02-06 21:01:15.133	D adding_fee 0, use_rct 1
2020-02-06 21:01:15.133	D Picking output 301, amount 0.000015800000, ki <3d66c09fb9354b541d6e7e119a53e2744f039777965a7440bfc4dc25e3f36aaa>
2020-02-06 21:01:15.133	D estimated bulletproof rct tx size for 1 inputs with ring size 11 and 1 outputs: 1594 (768 saved)
2020-02-06 21:01:15.133	D We can fully pay 8A62NhquGzAQEohZBDgyKgj55gfTSzBRK56HiWJdAn5gQNAQg2T1yEXG8K4RVn9NoHZSEFC5QD72BiD5uoXTudeT9PawUZ2 for 0.000001000000
2020-02-06 21:01:15.133	D Considering whether to create a tx now, 1 inputs, tx limit 149400
2020-02-06 21:01:15.133	D estimated bulletproof rct tx size for 1 inputs with ring size 11 and 2 outputs: 1736 (800 saved)
2020-02-06 21:01:15.133	D estimated bulletproof rct tx size for 1 inputs with ring size 11 and 2 outputs: 1736 (800 saved)
2020-02-06 21:01:15.133	D We don't have enough for the basic fee, switching to adding_fee
2020-02-06 21:01:15.134	D Start of loop with 0 0, tx.dsts.size() 1
2020-02-06 21:01:15.134	D unused_transfers_indices: 
2020-02-06 21:01:15.134	D unused_dust_indices: 
2020-02-06 21:01:15.134	D dsts size 0, first -
2020-02-06 21:01:15.134	D adding_fee 1, use_rct 1
2020-02-06 21:01:15.134	D No more outputs to choose from
2020-02-06 21:01:15.134	E 1. THROW EXCEPTION: error::tx_not_possible
2020-02-06 21:01:15.134	W /home/user/monero-gui/monero-gui/monero/src/wallet/wallet2.cpp:9625:N5tools5error15tx_not_possibleE: tx not possible, available = 0.000135570000, tx_amount = 0.000001000000, fee = 0.000022390000
```

# Discussion History
## moneromooo-monero | 2020-02-06T21:16:33+00:00
This is because you have loads of small outputs, try using sweep_below 0.001 and it should work.

## rating89us | 2020-02-06T21:26:00+00:00
Yes, I know. But the daemon shouldn't return this error message ("not enough money to transfer") to the GUI.

## selsta | 2020-02-06T21:28:14+00:00
It’s not the daemon, it is libwallet api: https://github.com/monero-project/monero/blob/40501cc13196adf05e86bf0b7d9e4cbdcd32cafb/src/wallet/api/wallet.cpp#L1537

## moneromooo-monero | 2020-02-06T21:39:49+00:00
Oh I see, it's the wording you're reporting. Sorry :)

# Action History
- Created by: rating89us | 2020-02-06T21:09:47+00:00
