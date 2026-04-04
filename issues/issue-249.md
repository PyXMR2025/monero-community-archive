---
title: ' bitmonerod make useless dust :( '
source_url: https://github.com/monero-project/monero/issues/249
author: perl5577
assignees: []
labels: []
created_at: '2015-03-31T08:00:51+00:00'
updated_at: '2015-11-24T14:50:05+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:50:04+00:00'
---

# Original Description
Bitmonerod make useless dust :( 

One exemple:
http://chainradar.com/xmr/transaction/e195f1f289259a777aaed4e62afafb4415a887bde682b4ad1b6f39788a69498e

Speend : 10 XMR
Payout : 0.7XMR
Change:  9.280000000000
Fee: 0.020000000000

Input :
10.000000000000
Output:
9.000000000000
0.200000000000
0.300000000000  -> Payout one user
0.400000000000 ->  Payout other user
0.080000000000 -> I have patched code for add dust in change  ( If not make , I increase fee per factor 5 )

TX in mempool before TX   X + 1  ( 30000 + 1 )
TX in mempool after   TX   X + 1  ( 30000 + 2 )   

Why not spend other TX  ( I have more 20.000 TX not spend , I can make TX with only 2 TXNO ) 
I have see one TXNO 0.7 and  0.01 and 0.02 


# Discussion History
## fluffypony | 2015-03-31T09:11:21+00:00
I'm not understanding which is the useless dust? the 0.08?


## perl5577 | 2015-03-31T11:09:28+00:00
Why wallet use tx with 10XMR when find one or two tx is Easy for make payout only 0.7 . On moment on tx is make , i have more 50 tx with exactly 0.7 or 0.8 and many tx fir payout fee.

When wallet get tx 10xmr to spend . I add in my wallet 2tx.

Tw with lower a mount never spend and cumulate lower amount


## perl5577 | 2015-03-31T11:12:18+00:00
I think wallet need continue search solution for little moment and log only get first solution .


## perl5577 | 2015-03-31T11:14:48+00:00
Not only use first solution .

If testsolution.nbtxout < previousolution.nbtxout:
 Previousolution = testsolution


## sammy007 | 2015-03-31T11:15:51+00:00
If I understood correctly he want wallet to choose and use best inputs in order to produce tx with minimal miner-fee. No need to use 10 XMR input to send 0.5 XMR if you can build tx from 0.1 XMR and 0.6 XMR.


## fluffypony | 2015-03-31T11:33:08+00:00
Searching for the "best" solution may be problematic if it tends towards favouring outputs of a certain age, as this could (in turn) reveal information about the true signer in a ring. The sections in MRL-0004 that deal with temporal association attacks apply. The output selection can definitely be evaluated over time, but it will always tend to create some smaller outputs in an effort to defeat analysis.

"It's not a bug, it's a feature!"


## fluffypony | 2015-11-24T14:50:04+00:00
Should be fixed with the MRL4 changes, but better input selection in general is something that we have to look at regularly.


# Action History
- Created by: perl5577 | 2015-03-31T08:00:51+00:00
- Closed at: 2015-11-24T14:50:04+00:00
