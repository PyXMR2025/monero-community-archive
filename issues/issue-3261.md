---
title: Monero x64-v0.17.1.5 GUI slow to catch up on hard disk vs Bitcoin Core, why?
source_url: https://github.com/monero-project/monero-gui/issues/3261
author: gab81
assignees: []
labels: []
created_at: '2020-12-09T11:25:56+00:00'
updated_at: '2020-12-13T09:43:45+00:00'
type: issue
status: closed
closed_at: '2020-12-10T09:58:49+00:00'
---

# Original Description
hi,

not sure this is an issue but GUI is slow in my opinion.. 

I have both Monero Core and Bitcoin Core on the same external hard disk. While we know that an external hard disk on usb3 is a bottleneck, the sync for BTC core (with few tweaks) is much faster compared with Monero Core. I have both clients disconnected for say 2 days.

BTC core takes about 30, 40 mins tops to sync all blocks, clearly using well my CPU whereas Monero Core can still use the CPU but relies so much on the disk, which in facts slows things down. But the difference is staggering.

i took a sample now and it did 270 blocks in 1 hour-ish. that's like 7 hours for 2000 blocks.

If i put it on my SSD on the other hand is faster, down to like 30 mins. I am not mining, just catching up blocks for the Core client.

So the question is, why is it so slow and needs so much disk work compared with BTC core? I can of course buy an external SSD hard disk, but that's no the point... 

thanks very much,
Gabrio


# Discussion History
## selsta | 2020-12-09T11:29:11+00:00
This is not a GUI issue, the daemon does the syncing.

Bitcoin does not have privacy so the verification process is way simpler. Monero benefits a lot with SSD drives because the verification process is disk read heavy.

## gab81 | 2020-12-09T14:02:40+00:00
ahhh got it, thanks for the clarification, so it has to do with the encryption of Monero's blockchain? just as a https page is heavier than a http? something like that i guess.

## dEBRUYNE-1 | 2020-12-09T21:44:33+00:00
In a sense. Verification per transaction effectively takes longer in Monero than in Bitcoin, hence the discrepancy in sync performance. 

## gab81 | 2020-12-13T09:43:45+00:00
one more question, is there a setting in the software that will speed up sync? i have quite a bit of ram available.... or it's just the SSD that makes a difference really? thanks

# Action History
- Created by: gab81 | 2020-12-09T11:25:56+00:00
- Closed at: 2020-12-10T09:58:49+00:00
