---
title: Change doesn't return after offline transaction signing
source_url: https://github.com/monero-project/monero/issues/1339
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2016-11-13T16:17:06+00:00'
updated_at: '2016-12-14T01:18:50+00:00'
type: issue
status: closed
closed_at: '2016-12-14T01:18:50+00:00'
---

# Original Description
I sent 0.10 XMR from a 0.74 XMR wallet via [offline transaction signing](https://monero.stackexchange.com/questions/2160/how-do-i-use-cold-transaction-signing) as a test.

At the `submit_transfer` step, the following was shown:

```
Loaded 1 transactions, for 0.700000000000, fee 0.002000000000, change 0.598000000000, sending 0.100000000000 to <address> with min mixin 4. Is this okay? (Y/Yes/N/No)y
Money successfully sent, transaction: <208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc>
```

Unfortunately, the change never returned to my original address. The online "watch-only" wallet said 0.04 XMR. Even after making the offline "spend" wallet hot, and doing `rescan_bc` there, no difference, still stuck at 0.04 XMR.

Block explorer [page](https://explorer.xmr.my/tx/208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc) for the transaction.

# Discussion History
## moneromooo-monero | 2016-11-13T22:42:44+00:00
The change is sent to that address, though there is a bug scanning. You can check that the change came back with check_tx_key (the tx key is saved only in the cold wallet, as it is secret). I'm working on fixing this right now.


## peanutsformonkeys | 2016-11-13T23:49:59+00:00
Indeed, I was able to check the change coming back with the `check_tx_key` command:

```
[wallet 4*****]: get_tx_key 208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc
Tx key: <txkey>
[wallet 4*****]: check_tx_key
Error: usage: check_tx_key <txid> <txkey> <address>
[wallet 4*****]: check_tx_key 208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc <txkey> <address>
<address> received 0.598000000000 in txid <208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc>
```

Thank you for clarifying so quickly. Looking forward to test the bugfix.


## moneromooo-monero | 2016-11-14T08:33:22+00:00
JFYI, might be a few days, I don't know what the bug is yet, and day job needs its time.


## rndbr | 2016-11-14T14:07:10+00:00
+1, I ran into this issue too. Thanks for the workaround in the meantime.


## moneromooo-monero | 2016-11-15T12:00:00+00:00
I found the bug, the cold signed txes mistakenly contain two pubkeys, and the wallet is using the wrong one.
The fix is easy, but recovering your change on a rescan will need a bit more changes to the wallet scanning code, and I'm not sure what's the cleanest way to do that just yet.


## peanutsformonkeys | 2016-11-15T18:53:31+00:00
Thanks. I'm glad you were able to find and fix the cause. I think it's an important feature. I don't particularly care about the change itself (only 0.598). If its recovery requires some ugly one-time code, then I'd just forget about it (should have been using testnet anyway). If though you find a way, without cluttering the code, I will donate the recovered change to the developer fund as a small token of appreciation.


## moneromooo-monero | 2016-11-15T19:19:18+00:00
https://github.com/monero-project/monero/pull/1344 should fix it all.


## moneromooo-monero | 2016-11-15T20:56:46+00:00
BTW, if you can try this, please report whether your change got found on a rescan.


## moneromooo-monero | 2016-11-15T21:07:59+00:00
Actually, trying to make clean commits after the fact got something that doesn't actually compile, some stuff I pushed needs some stuff I did not push. Will fix shortly...


## moneromooo-monero | 2016-11-15T21:21:18+00:00
fixed


## peanutsformonkeys | 2016-11-15T23:11:36+00:00
No success so far. I hope I am doing this right. Compiled from HEAD with brew (as I did before):

```
$ brew install monero --HEAD -v
…
HEAD is now at 9363b2a Merge pull request #1334
…
```

Launched the daemon, and then did a rescan:

```
Monero 'Wolfram Warptangent' (v0.10.0.0-9363b2a)
…
[wallet 4*****]: rescan_bc
Starting refresh...
Height <block>, transaction <txid>, received 0.040000000000
Height <block>, transaction <txid>, received 0.700000000000
Height 1178910, transaction <208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc>, spent 0.700000000000
Refresh done, blocks received: 1754                             
Balance: 0.040000000000, unlocked balance: 0.040000000000
[wallet 4*****]: 
```


## peanutsformonkeys | 2016-11-15T23:20:03+00:00
If it would be easier for you to troubleshoot, I can send you the mnemonic if you want.


## moneromooo-monero | 2016-11-16T09:02:58+00:00
That'd be because this patch is not merged yet, you'd need to compile the branch I linked to not, master.


## moneromooo-monero | 2016-11-16T09:24:13+00:00
I also upated the branch a bit, to make the scanning change a bit cleaner, should have no functional change.


## peanutsformonkeys | 2016-11-16T22:28:55+00:00
I am a total newbie wrt. git, so if you can provide me the commands needed to download and compile that specific branch / pull request, I will try that.


## moneromooo-monero | 2016-11-17T20:49:46+00:00
Actually, what you did first is good, as this patch just got merged :)


## peanutsformonkeys | 2016-11-17T22:44:42+00:00
Cool, the `rescan_bc` found the change!

```
Balance: 0.040000000000, unlocked balance: 0.040000000000
[wallet 4*****]: rescan_bc
Starting refresh...
…
Height 1178910, transaction <208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc>, received 0.008000000000
Height 1178910, transaction <208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc>, received 0.090000000000
Height 1178910, transaction <208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc>, received 0.500000000000
Height 1178910, transaction <208d82caac0642e2ee77c79e568c33d1d23ed785009f9c770227916fd8e504dc>, spent 0.700000000000
Balance: 0.638000000000, unlocked balance: 0.638000000000
[wallet 4*****]: 
```

I am sending it to the Monero donation address.


## peanutsformonkeys | 2016-11-17T23:05:37+00:00
Oops, I prematurely closed the issue. I have trouble sending moneroj from this wallet:

```
[wallet 4*****]: transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 0.598
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No)y
**Error: transaction was not constructed**
```


## moneromooo-monero | 2016-11-18T18:03:30+00:00
Any error in the log ?


## peanutsformonkeys | 2016-11-18T23:59:54+00:00
Yes, this is what appears in `monero-wallet-cli.log` when trying the above transaction:

```
2016-Nov-19 00:40:56.375743 Loaded wallet keys file, with public address: 44XdQ98oYwHaCLU5QK8YGUH7yDGiANQ5kStcniWtCqZN37caM8RotiNX5DkyBsTRs7AEiEs1xQ65DZQLvqBBJbVkHpVsr2t
2016-Nov-19 00:42:40.132854 amount=0.500000000000, real_output=3, real_output_in_tx_index=3, indexes: 250098 643941 961698 1076632 1078245 
2016-Nov-19 00:42:40.133551 amount=0.040000000000, real_output=3, real_output_in_tx_index=1, indexes: 200038 206895 233311 269940 271321 
2016-Nov-19 00:42:40.134185 amount=0.008000000000, real_output=3, real_output_in_tx_index=0, indexes: 112033 124183 128349 217662 218832 
2016-Nov-19 00:42:40.134816 amount=0.090000000000, real_output=3, real_output_in_tx_index=1, indexes: 136753 150663 152420 279162 279706 
2016-Nov-19 00:42:40.156416 ERROR /tmp/monero-20161117-27734-13vrcr6/src/cryptonote_core/cryptonote_format_utils.cpp:558 derived public key missmatch with output public key! 
derived_key:d9c9f015eb349b63dfa0213a2be6b19ecc5e41686afd954130318874dd474b3a
real output_public_key:ee478130597b474c3feb4e973fa39e268d49ba6281beafc60b294b076af6bccbe9aa7c81cdb5b3148fb7628063cd7a07d1add1643cedd3fa34479d859cc56265
2016-Nov-19 00:42:40.156532 ERROR /tmp/monero-20161117-27734-13vrcr6/src/wallet/wallet2.cpp:3625 !r. THROW EXCEPTION: error::tx_not_constructed
2016-Nov-19 00:42:40.158910 /tmp/monero-20161117-27734-13vrcr6/src/wallet/wallet2.cpp:3625:N5tools5error18tx_not_constructedE: transaction was not constructed
Sources:
  source 0:
    amount: 0.500000000000
  source 1:
    amount: 0.040000000000
  source 2:
    amount: 0.008000000000
  source 3:
    amount: 0.090000000000
Destinations:
  0: 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 0.008000000000
  1: 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 0.090000000000
  2: 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 0.500000000000
  3: 44XdQ98oYwHaCLU5QK8YGUH7yDGiANQ5kStcniWtCqZN37caM8RotiNX5DkyBsTRs7AEiEs1xQ65DZQLvqBBJbVkHpVsr2t 0.040000000000
unlock_time: 0
2016-Nov-19 00:42:40.209247 Error: transaction was not constructed
```


## moneromooo-monero | 2016-11-19T09:39:20+00:00
Does https://github.com/monero-project/monero/pull/1358 fix it ?


## peanutsformonkeys | 2016-11-20T19:36:55+00:00
I would like to try, but honestly have no idea what git commands will allow me to compile that.


## moneroexamples | 2016-11-21T00:55:17+00:00
@peanutsformonkeys 


```
git clone git@github.com:moneroexamples/monero.git
cd monero
curl https://patch-diff.githubusercontent.com/raw/monero-project/monero/pull/1358.patch | git apply -v -
make # to compile
```


## peanutsformonkeys | 2016-11-21T19:53:46+00:00
Thanks for the tip. I had to do a slightly different `git clone` command because the above gave an error. This worked:

`$ git clone https://github.com/moneroexamples/monero.git`


Patching the source mostly worked, except for 1 chunk it seems:

```
$ curl https://patch-diff.githubusercontent.com/raw/monero-project/monero/pull/1358.patch | git apply -v -
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  6161    0  6161    0     0   8255      0 --:--:-- --:--:-- --:--:--  9046
Checking patch src/wallet/wallet2.cpp...
Hunk #1 succeeded at 4624 (offset -64 lines).
Hunk #2 succeeded at 4696 (offset -64 lines).
error: while searching for:
    THROW_WALLET_EXCEPTION_IF(td.m_tx.vout.empty(), error::wallet_internal_error, "tx with no outputs at index " + boost::lexical_cast<std::string>(i));
    THROW_WALLET_EXCEPTION_IF(!parse_tx_extra(td.m_tx.extra, tx_extra_fields), error::wallet_internal_error,
        "Transaction extra has unsupported format at index " + boost::lexical_cast<std::string>(i));
    THROW_WALLET_EXCEPTION_IF(!find_tx_extra_field_by_type(tx_extra_fields, pub_key_field), error::wallet_internal_error,
        "Public key wasn't found in the transaction extra at index " + boost::lexical_cast<std::string>(i));

    cryptonote::generate_key_image_helper(m_account.get_keys(), pub_key_field.pub_key, td.m_internal_output_index, in_ephemeral, td.m_key_image);
    td.m_key_image_known = true;
    THROW_WALLET_EXCEPTION_IF(in_ephemeral.pub != boost::get<cryptonote::txout_to_key>(td.m_tx.vout[td.m_internal_output_index].target).key,
        error::wallet_internal_error, "key_image generated ephemeral public key not matched with output_key at index " + boost::lexical_cast<std::string>(i));

error: patch failed: src/wallet/wallet2.cpp:4845
error: src/wallet/wallet2.cpp: patch does not apply
Checking patch src/wallet/wallet2.h...
Hunk #1 succeeded at 569 (offset -22 lines).
```

Is this OK to compile with? It looks like it's not OK.

## moneroexamples | 2016-11-21T23:53:44+00:00
Patch didnt apply. Its possible you need to include some other patch first, then this one. Maybe first have to apply patch about fixing  decrypting key images:
https://patch-diff.githubusercontent.com/raw/monero-project/monero/pull/1351.patch





## peanutsformonkeys | 2016-11-22T19:41:59+00:00
Thank you. I tried that, patch 1351 applies cleanly. But then, patch 1358 fails again with a similar error:

```
$ curl https://patch-diff.githubusercontent.com/raw/monero-project/monero/pull/1358.patch | git apply -v -
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  6161    0  6161    0     0  12012      0 --:--:-- --:--:-- --:--:-- 12080
Checking patch src/wallet/wallet2.cpp...
Hunk #1 succeeded at 4624 (offset -64 lines).
Hunk #2 succeeded at 4696 (offset -64 lines).
error: while searching for:
    THROW_WALLET_EXCEPTION_IF(td.m_tx.vout.empty(), error::wallet_internal_error, "tx with no outputs at index " + boost::lexical_cast<std::string>(i));
    THROW_WALLET_EXCEPTION_IF(!parse_tx_extra(td.m_tx.extra, tx_extra_fields), error::wallet_internal_error,
        "Transaction extra has unsupported format at index " + boost::lexical_cast<std::string>(i));
    THROW_WALLET_EXCEPTION_IF(!find_tx_extra_field_by_type(tx_extra_fields, pub_key_field), error::wallet_internal_error,
        "Public key wasn't found in the transaction extra at index " + boost::lexical_cast<std::string>(i));

    cryptonote::generate_key_image_helper(m_account.get_keys(), pub_key_field.pub_key, td.m_internal_output_index, in_ephemeral, td.m_key_image);
    td.m_key_image_known = true;
    THROW_WALLET_EXCEPTION_IF(in_ephemeral.pub != boost::get<cryptonote::txout_to_key>(td.m_tx.vout[td.m_internal_output_index].target).key,
        error::wallet_internal_error, "key_image generated ephemeral public key not matched with output_key at index " + boost::lexical_cast<std::string>(i));

error: patch failed: src/wallet/wallet2.cpp:4845
error: src/wallet/wallet2.cpp: patch does not apply
Checking patch src/wallet/wallet2.h...
Hunk #1 succeeded at 569 (offset -22 lines).
```

If you guys think it's easier that I just hand-over the wallet's mnemonic, rather than educating me on how to patch and build that specific branch, that's fine by me. I don't want to be a burden.

## iDunk5400 | 2016-11-22T20:11:04+00:00
`git clone https://github.com/monero-project/monero.git`
`cd monero`
`git fetch origin pull/1358/head:1358`
`git checkout 1358`
`make`

## peanutsformonkeys | 2016-11-23T01:45:53+00:00
I was able to build 1358 with those instructions. But then I still got the same `transaction was not constructed` error when trying to send the change.

## moneromooo-monero | 2016-11-23T19:56:38+00:00
I've tried with a fresh hot/cold wallet pair so I could track outputs. I could send, then send change. Both txes were created by cold signing. Can you try again making sure both wallets are resynced ?

## peanutsformonkeys | 2016-11-23T20:30:00+00:00
I am not sure that the result I reported yesterday is representative. I am getting `Error: failed to load wallet: std::bad_alloc` when opening **any** existing wallet. Only by reimporting the mnemonic in a new wallet, I could try to transfer the change (but that thus failed). I suspect my build is not 100% OK. Unfortunately, I haven't got much time to pursue this further right now.

## moneromooo-monero | 2016-11-23T20:47:04+00:00
The std::bad_alloc thing is likely due to a change in boost version. Did you update boost recently ?

## moneromooo-monero | 2016-11-23T20:50:00+00:00
https://github.com/monero-project/monero/pull/1369 has a fix for bad change/fee being reported in show_transfers, and removes the double prompt. No further changes for now, low priority.

## moneromooo-monero | 2016-11-23T21:00:23+00:00
er, wrong bug for that last comment, ignore it :)

## moneromooo-monero | 2016-12-09T18:27:23+00:00
The "transaction was not constructed" thing should now be fixed by https://github.com/monero-project/monero/pull/1419. It requires rescanning the wallet though.

## peanutsformonkeys | 2016-12-14T01:18:50+00:00
The 0.10.1.0 point release finally allowed me to send the "cold signing" change to the Monero donation address after a `rescan_bc`:

```
[wallet 44XdQ9]: transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 0.598
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
Sending 0.598000000000.  The transaction fee is 0.004000000000.
Is this okay?  (Y/Yes/N/No): y
Money successfully sent, transaction <531dca45d78aa12e3aca11dd4d1dad5be7dd89fa9108ea663e069fdb1776d8bc>
```

On the target wallet (watch-only obviously for me), I could see the 0.598 XMR arrive:

```
Background refresh thread started
Height 1200833, transaction <531dca45d78aa12e3aca11dd4d1dad5be7dd89fa9108ea663e069fdb1776d8bc>, received 0.008000000000
Height 1200833, transaction <531dca45d78aa12e3aca11dd4d1dad5be7dd89fa9108ea663e069fdb1776d8bc>, received 0.090000000000
Height 1200833, transaction <531dca45d78aa12e3aca11dd4d1dad5be7dd89fa9108ea663e069fdb1776d8bc>, received 0.500000000000
[wallet 44AFFq]: 
```

Thanks a lot!

# Action History
- Created by: peanutsformonkeys | 2016-11-13T16:17:06+00:00
- Closed at: 2016-12-14T01:18:50+00:00
