---
title: Can't restore correct wallet from seed.
source_url: https://github.com/monero-project/monero/issues/235
author: TheKoziTwo
assignees: []
labels: []
created_at: '2015-03-04T13:22:28+00:00'
updated_at: '2015-03-04T13:47:38+00:00'
type: issue
status: closed
closed_at: '2015-03-04T13:47:38+00:00'
---

# Original Description
**Problem:** Can't restore correct wallet from seed.

**Environment:**
Ubuntu 14.04
Bitmonero Wallet v.0.8.8.7-1016712

**Reproducible:**
1. Created new wallet (0 - English for seed language), was given this seed (Wallet id: 42GWgC):
`debut equip surfer tequila eldest heron eggs incur unnoticed nerves fawns ghost dawn revamp northern razor rafts wade calamity ocean zero evolved bygones cactus bygones`
2. Exit wallet
3. Run: ./simplewallet --restore-deterministic-wallet
4. Enter wallet name: test.bin
5. Enter (no password)
6. Enter seed
7. Gets wallet id 428RFv, the seed is repeated and identical except from one word, "incur" has been replaced with "incline".

Question:
So basically, I'm getting another wallet restored than the one I should. What am I doing wrong? Why is that word replaced?


# Discussion History
## fluffypony | 2015-03-04T13:47:38+00:00
Fixed in https://github.com/monero-project/bitmonero/commit/c01069f35253586ac2fbc3d507c7ed3ccdd900ce and https://github.com/monero-project/bitmonero/commit/10e4132e22ccc0f1a41763adee74699ebedb5ffc.

Restores for seeds containing the words "incline" or "launchpad" will have to use a newer version of Monero, and will have to replace "incline" with "inline", and replace "launchpad" with "ourselves".

Thanks for catching this:)


# Action History
- Created by: TheKoziTwo | 2015-03-04T13:22:28+00:00
- Closed at: 2015-03-04T13:47:38+00:00
