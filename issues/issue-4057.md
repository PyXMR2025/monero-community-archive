---
title: After restarting the wallet is empty
source_url: https://github.com/monero-project/monero-gui/issues/4057
author: Querens
assignees: []
labels: []
created_at: '2022-10-30T19:10:54+00:00'
updated_at: '2022-11-13T00:26:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I restored the wallet from seed. Synced with daemon it has shown the correct status on my account. After relaunch account is empty like it's new. 

# Discussion History
## selsta | 2022-10-30T21:51:33+00:00
Same here, which operating system are you using? Which version do you use?

## Querens | 2022-10-30T22:07:22+00:00
Debian GNU/Linux bookworm/sid
i --\ monero-gui 0:0.18.1.2-1

## selsta | 2022-10-30T22:10:16+00:00
Did this happen once or does it happen every single time?

## Querens | 2022-10-30T22:31:10+00:00
This happens every time. It has worked only once on the first synchronization of the wallet with the blockchain

## NguBilal | 2022-11-12T22:29:32+00:00
Same here (GUI 0.18.1.2 on Windows 11). 
Only solution I found:
         Settings > Info > Wallet restore height: xxxxxx (Change)
Click "Change" and enter a block height from which on you want to restore, for example "250000". The wallet will reach back to that point in history and re-synchronize, and, at least here, restore the correct transaction history as well as the correct account balance. 

## selsta | 2022-11-13T00:25:27+00:00
@NguBilal it most likely means that the wallet can't save correctly. In which folder did you have your wallet saved?

Also can you try to start monero-gui as administrator?

# Action History
- Created by: Querens | 2022-10-30T19:10:54+00:00
