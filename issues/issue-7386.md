---
title: seed generates a different wallet
source_url: https://github.com/monero-project/monero/issues/7386
author: bissiol
assignees: []
labels: []
created_at: '2021-02-19T14:21:33+00:00'
updated_at: '2022-07-20T20:43:18+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:43:18+00:00'
---

# Original Description
I was restoring my wallet from seed and my 25 word seed is generating a different primary address from the original wallet I created (and funded).
Seed's words are in Italian.
25th word is the same of 24th.
I tried with 24-word (without the last) and the result is the same primary address. 
I tried to restore from CLI and from GUI with same result.
I'm sure that I didn't use an offset passphrase when I generated the wallet.
I tried to change language of GUI app to Italian and to English with same output (always the same primary address that doesn't match my original one).
Please help.... maybe I lost funds?

# Discussion History
## bissiol | 2021-02-19T18:09:32+00:00
Ok I understand that is normal that last word repeats one of the 24 seed words...

## selsta | 2021-02-19T22:54:51+00:00
Which wallet did you use to generate the initial address? CLI?

## bissiol | 2021-02-19T23:31:08+00:00
> Which wallet did you use to generate the initial address? CLI?

The same I used to (try to) restore: monero-wallet-cli

Thanks for your reply

## selsta | 2021-02-19T23:51:27+00:00
Do you still have the original wallet file? I assume no?

## bissiol | 2021-02-20T06:40:45+00:00
> Do you still have the original wallet file? I assume no?

No. Only two paper backups (seed)

## selsta | 2021-02-24T12:35:00+00:00
Do you know which version was used to originally create the wallet?

Try to download the old version and restore the wallet from seed with it.

## bissiol | 2021-02-24T14:24:06+00:00
> Do you still have the original wallet file? I assume no?

No. Only two paper backups

> Do you know which version was used to originally create the wallet?
> 
> Try to download the old version and restore the wallet from seed with it.

I will try old versions. Do you know other issues about this version's difference in seed-to-address?

## selsta | 2021-02-24T14:25:27+00:00
> Do you know other issues about this version's difference in seed-to-address?

No, that's why I suspected accidental seed offset used, but you said that's not the case.

## elibroftw | 2021-11-13T17:14:10+00:00
@bissiol did you set the seed language in the CLI before you tried restoring from seed? 

## selsta | 2022-07-20T20:43:18+00:00
No reply from issue author and no steps to reproduce.

# Action History
- Created by: bissiol | 2021-02-19T14:21:33+00:00
- Closed at: 2022-07-20T20:43:18+00:00
