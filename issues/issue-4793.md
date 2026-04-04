---
title: Generalized M/N multisig not yet working reliably
source_url: https://github.com/monero-project/monero/issues/4793
author: rbrunner7
assignees: []
labels: []
created_at: '2018-11-04T13:50:18+00:00'
updated_at: '2018-12-04T15:17:20+00:00'
type: issue
status: closed
closed_at: '2018-12-04T15:17:20+00:00'
---

# Original Description
I tested generalized M/N multisig as implemented by @naughtyfox with #4036 and included in 0.13.0.4.

I made two different sets of 2/4 multisig testnet wallets (A, B, C, D), and both had the following identical and probably deterministic behaviour (I tried each case 3 times):

* Creating a transaction in wallet A, sending it to wallet **B** and submitting it there did not work. It gave the following error:
`This signature was made with stale data: export fresh multisig data, which other participants must then use`
(Of course the wallets *were* fully synced when creating and signing the transaction.)
* Creating a transaction in wallet A, sending it to wallet **C** and submitting it here not not work either, but with a different error:
`transaction <xxxxxxxx> was rejected by daemon with status: Failed Error: Reason: invalid input`
* Creating a transaction in wallet A, sending it to wallet **D** and submitting it here worked without any problem.

For comparison, I also built a wallet set for plain 4/4 multisig. I sent 2 transactions through those 4 wallets in two different ways, and both worked.

Furthermore, I built two wallet sets for 3/4 multisig that is supported for quite some time already, one using the "old" `finalize_multisig` command, and one using the new `exchange_multisig_keys` command. Again I sent 2 transactions through 3 wallets in two different ways, and everything worked.

Monero multisig is quite error-prone if done manually; however I used my MMS to establish the multisig wallets, to sync them, and move transactions between wallets, in an almost fully automated way. Because of this I regard it as quite unlikely that the error was on my side somehow, e.g. giving "MultisigV1" strings to the wrong wallet(s) when configuring. The fully working 4/4 and 3/4 cases also make a "handling error" unlikely in my opinion.

# Discussion History
## naughtyfox | 2018-11-05T17:54:12+00:00
> Creating a transaction in wallet A, sending it to wallet B and submitting it there did not work. It gave the following error

We encountered this kind of error in N/N schemes as well. Did wallet **B** participated in `export_multisig`? And if yes, did it call the same function after? This will definitely lead to the error.

> Creating a transaction in wallet A, sending it to wallet D and submitting it here worked without any problem

Did you call `export_multisig` and `import_multisig` among all of participants or only between **A** and **D** wallets? Could you please provide me with step-by-step instruction on how to reproduce this behavior?

Anyway thank you for the report. I will investigate it tomorrow.

## rbrunner7 | 2018-11-05T19:31:59+00:00
> We encountered this kind of error in N/N schemes as well. Did wallet B participated in export_multisig? And if yes, did it call the same function after? This will definitely lead to the error.

> Did you call export_multisig and import_multisig among all of participants or only between A and D wallets? Could you please provide me with step-by-step instruction on how to reproduce this behavior?

Well, that's what I meant by "syncing the wallets". I have that fully automated, no manual steps involved where I could forget `export_multisig`  or `import_multisig` or do it the "wrong way round" somehow. And all wallets are treated equally and symmetrically - right now I honestly have no idea how differences between the wallets B, C, D could develop this way.

> Could you please provide me with step-by-step instruction on how to reproduce this behavior?

Please bear with me, I don't write this as some kind of lame excuse because I am too lazy to write it down or because I am arrogant: My step-by-step instruction is simply "Configure and sync all 4 wallets correctly according to the rules that govern Monero multisig and then try to transact".

Note that interestingly the 3/4 case works, even using your new `exchange_multisig_keys` CLI wallet command, not the old `finalize_multisig` command.

I have three - hopefully - helpful proposals how we could proceed:

* If you think it could help I could easily test some more combinations, e.g. starting a transaction in wallet D and submitting it in C.
* I could mail you the two (A, B, C, D) 2/4 multisig wallet sets that don't work in identical ways.
* I could make available to you a beta version of my MMS. You would probably spend some hours to set everything up and learn to operate it, but once this is behind you would be much faster doing tests yourself.


## rbrunner7 | 2018-11-06T06:55:51+00:00
I have an idea where your tests (that I don't doubt were successful) and my tests could have a difference that maybe explain the errors I encountered:

Question: Are there any rules regarding order that must be followed when handing key sets to the CLI wallet `exchange_multisig_keys` command that I may have violated and that could lead to malformed wallets?

In detail: Let's assume I do the following for wallet A:

    exchange_multisig_keys <B> <C> <D>

Then *another* round, with new key sets from the other wallets is needed, but I change the order I hand over those new key sets as follows:

    exchange_multisig_keys <D> <C> <B>

I do that with my MMS: The order of the parameters of the `exchange_multisig_keys` may indeed be *different* between multiple rounds, because that order currently depends on the order of message reception by the wallets that is somewhat random. I can easily imagine however that when you did your manual tests you sticked to a fixed order, hence the possible difference between your test results and mine.

Is this **supposed** to work? If not, **should** it work? Or must the **same order** be used for multiple rounds of key exchanges?

## naughtyfox | 2018-11-06T09:56:46+00:00
In theory it shouldn't affect the wallet state. Currently I'm about to check it and try to reproduce this bug. My first guess the problem is in `export_multisig()` calls (we figured out you should be very careful using it in your automation)

## rbrunner7 | 2018-11-06T10:17:47+00:00
Yes, of course, if somehow the import and export of multisig info does not "balance out" and the wrong info goes into the wrong wallet, all kinds of things can probably go wrong.

You never know in IT, I don't say I don't have any bugs in my automation; it's just very hard for me to imagine that I still have one there if the same automation can deal with 4/4 and 3/4 cases without any problem - just not the 2/4 case ...

## naughtyfox | 2018-11-06T10:31:25+00:00
Don't worry, we have no options rather than solving this problem :)


## naughtyfox | 2018-11-06T13:19:23+00:00
I reproduced the problem, working on it now

## moneromooo-monero | 2018-12-04T15:15:48+00:00
+resolved

# Action History
- Created by: rbrunner7 | 2018-11-04T13:50:18+00:00
- Closed at: 2018-12-04T15:17:20+00:00
