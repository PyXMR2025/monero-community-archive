---
title: scan transaction by transaction id causes program to stop responding
source_url: https://github.com/monero-project/monero-gui/issues/4463
author: HoaxParagon
assignees: []
labels: []
created_at: '2025-06-26T13:44:27+00:00'
updated_at: '2025-06-29T10:03:43+00:00'
type: issue
status: closed
closed_at: '2025-06-29T10:03:43+00:00'
---

# Original Description
my wallet doesn't show my accounts value and the transaction isn't showing up in history. Manually scanning via 'scan transaction' makes the program stop responding. I used my third receive address to get a transaction. The history shows nothing and so does the balance, but the transaction has been verified thousands of times and when I rescan wallet, nothing shows up. My daemon is fully synced as well and the wallet says it's synced, but it is not showing the right balance. When I use prove/check, the transaction reports that it's gone through.

# Discussion History
## HoaxParagon | 2025-06-26T14:49:55+00:00
Okay, that's all well and good but how do I fix this?

## HoaxParagon | 2025-06-26T15:52:47+00:00
It was a phish wasn't it?

## selsta | 2025-06-26T15:56:09+00:00
Do you use a local node or a remote node?

## HoaxParagon | 2025-06-26T16:04:06+00:00
I use a local node.

## selsta | 2025-06-26T16:06:19+00:00
If you go to Settings -> Info, can you share your wallet restore height?

## HoaxParagon | 2025-06-26T16:14:38+00:00
it's sitting at 3420564

## HoaxParagon | 2025-06-28T15:26:58+00:00
Tried using a remote node to scan the transaction by id, still hangs the program.

## selsta | 2025-06-28T16:34:26+00:00
Do you use Ledger or another hardware wallet?

## HoaxParagon | 2025-06-28T16:37:05+00:00
I use a trezor safe 5

## selsta | 2025-06-28T16:38:58+00:00
I don't own such a device so I can't confirm if the "scan transaction" functionality works correctly with it. The incoming transaction, when was the date it should have been received?

## HoaxParagon | 2025-06-28T16:42:15+00:00
June the 23rd, from Kraken. I've used the prove/check function to verify it went through, the wallet should have money, but my balance is still zero and 'rescan balance' does nothing. I tried setting the height to zero and it's rebuilding the cache now, we'll see what that does.

## HoaxParagon | 2025-06-29T02:22:42+00:00
Well, I figured it out myself finally, at least, I had it, now it's back to zero balance. I set the height to zero, resynced the wallet, took a while, and my balance showed up until I scanned a transaction ID. Then it went back to zero but the program didn't stop responding.

## HoaxParagon | 2025-06-29T02:28:29+00:00
I restarted the app and it asked me, on the hardware wallet, to confirm a refresh, I pressed the button, it refreshed and now the balance is finally showing up.

## plowsof | 2025-06-29T09:49:03+00:00
i tried scan_tx with a ledger and it worked. granted, the tx was 1 block below the wallets sync height. do note: when attempting to use scan_tx you are prompted to export the devices private view key again. if you do not the symptoms include : staring at an unresponsive gui wondering whats going on. 

# Action History
- Created by: HoaxParagon | 2025-06-26T13:44:27+00:00
- Closed at: 2025-06-29T10:03:43+00:00
