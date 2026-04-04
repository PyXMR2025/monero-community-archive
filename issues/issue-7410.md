---
title: Transactions do NOT add up to final balance! There's a mismatch.
source_url: https://github.com/monero-project/monero/issues/7410
author: xmrdog
assignees: []
labels: []
created_at: '2021-02-28T09:45:02+00:00'
updated_at: '2021-03-17T14:07:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have both hot and cold machines running Linux. Both have the same `v0.17.1.9` Monero version.

After performing these steps:

1. On hot machine, remove wallet file (leaving only the watch-only .keys file).
2. On hot machine, run `export_outputs all`.
3. On cold machine, run `import_outputs`.
4. On cold machine, run `export_key_images all`.
5. On hot machine, run `import_key_images`.
6. On hot machine, run `show_transfers all`

The final balance shown (after `refresh` completes) does **NOT** match up with the transactions! First of all:

* Can I assume the final balance shown after `refresh` is correct?

Assuming that's the case, **the transactions add up to a greater balance** than what I'm supposed to have.

Could this be related to https://github.com/monero-project/monero/issues/1406? I'm not sure because that was supposed to be fixed years ago.

[**] **UPDATE:** Removed irrelevant info.

# Discussion History
## xmrdog | 2021-02-28T11:26:15+00:00
I even tried adding an extra step between 2 and 3: On cold machine, delete wallet file (leaving only .keys file).

Same result.

## xmrdog | 2021-02-28T11:27:13+00:00
CCing @moneromooo-monero since he was involved with potentially related #1406.

## xmrdog | 2021-03-03T07:30:47+00:00
Updated above with clarification.

## xmrdog | 2021-03-03T07:32:40+00:00
@dEBRUYNE-1 CC

## dEBRUYNE-1 | 2021-03-03T12:22:22+00:00
Does the wallet state that any key images are missing? 

## xmrdog | 2021-03-03T12:26:15+00:00
@dEBRUYNE-1 No, it doesn't. (It did after step 1 + refresh, but after running all the steps above, the "missing key images" message is gone as expected.)

## xmrdog | 2021-03-03T21:50:42+00:00
@dEBRUYNE-1 @fluffypony @moneromooo-monero

I found a different way to reproduce exactly the same mismatch: By running `export_transfers all output=foo.csv`, I do indeed get a final "running balance" that is **greater** than shown by `balance`.

(So my earlier manual balance calculation was correct.)

Could this be an inflation bug or some other serious bug? The silence worries me.

## glv2 | 2021-03-04T08:25:36+00:00
Do you have transactions where your wallet sent money only to itself? I remember beeing suprised some time ago because the *show_transfers* command did not show the whole picture in this case.


## xmrdog | 2021-03-04T17:49:27+00:00
@glv2 No such thing in my case. Was your case a reported bug that was fixed? What was your solution?

I was able to investigate my case further. Since my wallet is simply transactions to/from an exchange, I know exactly what transactions to expect (since the exchange has a detailed ledger on their end).

Thankfully, the balance shown after `refresh` is exactly as expected. However, **two `out` transactions that should be there are not showing up** in `show_transfers`/`export_transfers`. This results in the mismatch between the final "running balance" and actual balance.

What could be the reasons for missing transactions?

FYI:

* I just noticed that my hot and cold machines were on different time zones, so I made the time zones equal and tried again. This did **not** help (nothing changed).
* One of the missing transactions is quite close in time to another one (1-2 hours). The other missing transaction is quite close (a few hours) to an end-of-year. (I have no idea if this date info is relevant.)

## dEBRUYNE-1 | 2021-03-04T20:16:42+00:00
Do you see any errors in the log (`monero-wallet-cli.log`) related to inability to 'decrypt' the missing transactions? 

## JustFranz | 2021-03-04T22:53:48+00:00
Can you send the whole incorrect balance or just the outputs that should not be there and will they go through?

## moneromooo-monero | 2021-03-04T23:58:42+00:00
Can you send me an compressed then encrypted log level 2 of simplewallet scanning this wallet, as well as the txids of the missing transactions please ?
My key's in utils/gpg_keys/moneromooo.asc, since the log will contain private info (though not the wallet keys).



## xmrdog | 2021-03-06T09:58:51+00:00
@moneromooo-monero

I was able to recover the missing transactions by copying the entire blockchain data over to the offline laptop, run `./monerod --offline`, run `./monero-wallet-cli` (without `--offline`), resync the wallet, and export the transactions.

The problem must be later in the pipeline, presumably somewhere in the hot/cold steps I outlined above.

I don't want to send over any private info like this.

Isn't this a great opportunity for someone to fully 100% reflect on and grasp the code of that entire pipeline again? To do some spring cleaning, check if there is some dust in there, so to speak. There's clearly a bug in there somewhere. Can someone here start a bug bounty on the Monero website?  I will contribute.

## selsta | 2021-03-06T18:58:02+00:00
@xmrdog https://hackerone.com/monero

## woodser | 2021-03-17T14:07:26+00:00
In case it's related to https://github.com/monero-project/monero/issues/5812, which I'm not able to reproduce now.

# Action History
- Created by: xmrdog | 2021-02-28T09:45:02+00:00
