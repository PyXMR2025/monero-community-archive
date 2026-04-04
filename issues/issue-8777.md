---
title: About the Use of Monero Coin Encryption Protocol, CryptoNote2 and RingCT3
source_url: https://github.com/monero-project/monero/issues/8777
author: 19231224lhr
assignees: []
labels: []
created_at: '2023-03-17T09:05:45+00:00'
updated_at: '2023-03-17T13:21:33+00:00'
type: issue
status: closed
closed_at: '2023-03-17T13:21:33+00:00'
---

# Original Description
I want to know that, is Monero still using the **CryptoNote2.0** to protect **sender's Identity information**? Or Monero has updated it's protocol, using **RingCT3.0 'bulletproof'** to protect **sender's Identity information**.
I know RingCT is to protect the Transaction amount, but as a new beginner, I find that RingCT3.0 uses 'bulletproof' to protect sender, so I don't know which protocol is used now in the Monero.
Thanks everyone.
![image](https://user-images.githubusercontent.com/70199004/225859245-7d7681d3-7b28-436c-8f97-22fa7aae765c.png)


# Discussion History
## moneromooo-monero | 2023-03-17T13:20:35+00:00
Monero can still use the original Cryptonote ring signatures to spend very old outputs. The vast majority of new transactions use ringct, which is similar to ring signatures in some way. I'm not sure where the 3.0 comes from. Bulletproofs are a type of range proof, which are used in new transactions which also use ringct. Bulletproofs do not provide identity information. They prove an amount is within a sane bound. RingCT signatures provide equiprobability between a set of outputs for the one that is actually spent within a ring. I suppose you can call this "sender's Identity information", even though cracking a ring to determine which output is spent will still not get you the sending address, since those are not on the chain in the first place.

I guess a short answer is "monero uses ringct and bulletproofs+ nowadays" (bulletproof+ is an incremental improvement over the original bulletproof).

## moneromooo-monero | 2023-03-17T13:21:29+00:00
But in any case, this is a bug tracker, you'd be better served asking this kind of question in #monero on irc.libera.chat, wihch can also be used via matrix.

Closing then.



# Action History
- Created by: 19231224lhr | 2023-03-17T09:05:45+00:00
- Closed at: 2023-03-17T13:21:33+00:00
