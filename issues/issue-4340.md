---
title: '[GUI][Restore wallet] Wallet can be restored with seed that has words truncated/suffixed
  with junk'
source_url: https://github.com/monero-project/monero-gui/issues/4340
author: b4n6-b4n6
assignees: []
labels: []
created_at: '2024-08-22T21:53:10+00:00'
updated_at: '2024-12-14T00:03:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Kindly observe video where I restored seed abandon x 25, but specific only aband x 25
[restore-bug-3.webm](https://github.com/user-attachments/assets/6ca1fe50-db35-4bb3-8a2f-10b79ba6a5f0)

Expected behavior: cannot restore seed with trunacted/suffixed with junk words

I think this is important, because it is possible to misspell words (especially when writing off paper / for non-english native speakers) and a word can get mixed up for another word in such case and restore to a different seed altogether

# Discussion History
## selsta | 2024-08-22T22:10:16+00:00
Only the first three letters get verified, that's how it is currently programmed. It has downsides and upsides, but this is currently intended behaviour, not only in the GUI but also CLI wallet.

## b4n6-b4n6 | 2024-08-23T07:51:46+00:00
okay... say we have scenario...


user misspells 'ailments' as 'aimlets', dosen't notice the misspelling and continues to restore this wallet, in this case 'aimlets' will successfully restore to 'aimless' instead of 'ailments' and user can be left confused
other words that can be misspelt yet successfully restore to another word include 'criminal' / 'circle' and 'bubble' / 'bulb'


edit: this does not happen in practice because the modern checksum check will catch this in practice, please ignore

> Only the first three letters get verified, that's how it is currently programmed. It has downsides and upsides, but this is currently intended behaviour, not only in the GUI but also CLI wallet.



## b4n6-b4n6 | 2024-08-23T09:38:30+00:00
> > Kindly observe video [restore-bug-3.webm](https://github.com/user-attachments/assets/6ca1fe50-db35-4bb3-8a2f-10b79ba6a5f0)
> > Expected behavior: cannot restore seed with trunacted/suffixed with junk words
> > I think this is important, because it is possible to misspell words (especially when writing off paper / for non-english native speakers) and a word can get mixed up for another word in such case and restore to a different seed altogether
> 
> I am baffled. All wallets should deny access. So he created addresses for you, right? The entropy level is zero.
> 
> I want to learn more from the experts.

Entropy level is not relevant to this issue. Seed like abandon x 25 can be used for testing. In video I want to bring attention to the possibility to specifiy seed words as truncated or suffix with any chars. In video I successfully restored wallet with seed a'bandon' x 25 while only specifing 'aband' x 25

## b4n6-b4n6 | 2024-08-31T04:09:44+00:00
problems that can occur in practice from this will be fixed with https://github.com/monero-project/monero-gui/issues/4342

## b4n6-b4n6 | 2024-08-31T04:20:42+00:00
> Only the first three letters get verified, that's how it is currently programmed. It has downsides and upsides, but this is currently intended behaviour, not only in the GUI but also CLI wallet.

[selsta](https://github.com/selsta)! I am working on a patch for this that does not change existing code, only adds an extra check post error to find strange words, please review PR [here](https://github.com/monero-project/monero/pull/9466)

Also I'd love to hear more about these 'upsides'

## selsta | 2024-12-14T00:03:53+00:00
I've approved the PR you linked, it will be merged with the next round of merges. The main upside is that people that make a typo somewhere after the first 3 letters in the word can still get their wallet restored. I'm not sure if that's the rational behind it, or not. Since the first 3 letters are all unique it's all that is required to verify a seed.

# Action History
- Created by: b4n6-b4n6 | 2024-08-22T21:53:10+00:00
