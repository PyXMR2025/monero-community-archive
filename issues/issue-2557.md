---
title: Monerod crashed while sending transaction, now funds seem lost
source_url: https://github.com/monero-project/monero/issues/2557
author: thrrht
assignees: []
labels: []
created_at: '2017-10-01T10:38:24+00:00'
updated_at: '2017-10-16T14:04:35+00:00'
type: issue
status: closed
closed_at: '2017-10-16T13:36:24+00:00'
---

# Original Description
Yesterday i was making a transaction to donate Monero to a friend as a present. I started receiving strange errors after i did it and the daemon crashed while i was doing it. I only noticed the stacktrace in the logs later, but the client would say it cant connect to the daemon, even though the daemon was running on localhost and listening to connections. The exact complaint was this: "Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0". It started when i tried to verify if the receiving wallet has received the transaction.

Today I downloaded the GUI and used it to access the wallet from which i was sending and also the receiving wallet. I got errors trying to open them up, so i ended up opening just the .keys files and rescanning the blockchain for both wallets. Both wallets are empty and in the transaction history of the sending wallet i see just a transaction sending out all my funds (not just 1 monero as i wanted). Attached is the logfile. 

I wonder, did i just loose all my funds from the sending wallet ? It was more then 100 xmr. Another question is the reason why this happened. am i compromised ? is it some kind of glitch ? i seriously thought monero is stable enough that this kind of events would not happen. 

This is the transaction in question: https://moneroexplorer.com/search?value=ac93553c52d00a20c4dfe607767cadd836213f610cec69bef7dd0176a0bb7019

[30_git.log](https://github.com/monero-project/monero/files/1347066/30_git.log)


# Discussion History
## moneromooo-monero | 2017-10-01T11:25:56+00:00
Do you have a stack trace for the crash ?

Please report clearly what you did. Here is what I understood from the above:

You sent 1 monero from wallet A to wallet B. I assume monero-wallet-cli, but that is only implied.
monerod crashes
Something may or may not happen to wallet A afterwards, this is left unsaid
Wallet A is rescanned using monero-wallet-gui
Wallet B too
Wallet A shows all the monero being gone
Wallet B shows no incoming monero

Another important things you should mention is what command did you use to send from A to B.


## thrrht | 2017-10-01T11:39:59+00:00
Hi.

i use monero from github and recompiled somewhere around last week. So this is what happened: 

1. I start the daemon from command line
2. I start the monero-wallet-cli and create a new wallet called wedding
3. I note down the address and write down the seed for it (on a card as a present) and exit 
3.1 Im not sure but maybe already somewhere here im receiving the above error about no connection to daemon. I dont care as long as i have the seed and address, its a present
3.2 I try to debug this, coz last week i started using the daemon configured to connect over tor, so maybe its connected i think, so i kill the daemon and start the 'tor version' (just an alias how the daemon is started with torsocks) and try to open the wedding wallet again, still doesnt work so kill the tor connected monerod and start a normal one and go on. At this point i didnt do any transfer or anything, just created a new wallet and wrote down the seed.
4. I copy and decrypt a file containg my wallet and start the monero-wallet-cli again now opening my wallet called thr
5. I do the transaction like always: "transfer normal 10 address 1" to the wedding wallet address
6. show_transfers shows the transaction as pending 
7. im in a hurry so i wait a few more seconds, shutdown the machine and run to the church

.. 

later i try to re-check if it went through but whenever i try to open the new wallet called wedding (i didnt delete it coz i wanted to make sure it is credited) i get the "no connection to daemon" error - even now. when i open my old thr wallet i dont get that error.  i have to run again.

..

today i have finally time to check everything. i dont see a balance on the wedding wallet and i still get the no connection to daemon error. so i download the gui from getmonero and use it to access the wedding wallet. It doesnt work and i find a hint on the net that i have to delete the files associated with the wallet and just import the wedding.keys. That works (in gui) and i see no incoming transfer. Ok, so fortunately i still have the wallet - i can do it again. So i try to open my old wallet via the gui. I do the same (just thr.keys) and i see zero balance. uff. i try to verify via the gui-packaged cli. still the same. i try to verify via my own cli. still zero. so yeah. shit happens :(

edit: i dont have the stacktrace, just the attached log

## dEBRUYNE-1 | 2017-10-01T13:35:10+00:00
Could you try to verify whether the transaction went to the correct address using either of these guides:

https://monero.stackexchange.com/questions/6137/how-do-i-as-a-recipient-verify-that-my-transaction-actually-arrived

https://monero.stackexchange.com/questions/6134/how-do-i-as-a-sender-verify-that-my-transaction-actually-arrived

## moneromooo-monero | 2017-10-01T14:10:35+00:00
I think this is due to the wallet being unable to sync from the daemon right now, which I'm fixing at the moment. You probably sent all your monero and did not see the change yet, and only will once the wallet gets those blocks. It should still say you've got the monero in the locked balance though. Does it ? Same thing for the wedding wallet, it'll see the incoming monero once it can refresh. I'll ping you once the patch is up so you can try.

## thrrht | 2017-10-01T15:45:47+00:00
Hi @dEBRUYNE-1 

i already checked that before opening the ticket.

1. The receiving address didnt get anything (i use the wedding wallet address and private viewkey to check that). There is no matching inputs or output.

2. The sending wallet did spend all balance. There is no matching output, and one (out of two) matching input that is for the whole balance of the wallet. 

Now it might be, that i would accidentaly copy & paste the incomplete receiving address. But i would not copy a completely different address for sure. Another thing is how come that all balance was sent ? I just was sending 1 XMR. And also i know how hard it is to send the whole baance from the wallet (when i was doing that before and migrating to a more securely kept wallet i had to first get the fee and then distract it from the whole balance and then use the result as the amount to be sent). I was not doing anything like that, so i find this extremely strange. May i have been compromised ? 
 
@moneromooo-monero i surely hope you are correct, but with the decoded output im kinda loosing my hope. I wonder how come the new wallet (wedding wallet) still doesnt work and the old one does (via cli, not gui)

## dEBRUYNE-1 | 2017-10-01T19:06:39+00:00
Could you check the transaction with the private view key of the *sending* wallet. If any change was sent back to it, the private view key of the sending wallet should be able to "decode / decrypt" one of the outputs. Thus, enter the public address and the private view key of the *sending* wallet [here](https://xmrchain.net/search?value=ac93553c52d00a20c4dfe607767cadd836213f610cec69bef7dd0176a0bb7019). 

## thrrht | 2017-10-01T22:59:03+00:00
@dEBRUYNE-1 

hi, it is the 2. in the post above. Specificaly, there are 2 outputs but no match (or output match? : false)  for the private viewkey of the sending wallet and the address of the sending wallet. There are 2 inputs, one of them is "false", the other is "true" and has the whole former balance of the wallet.

Look, im seriously interested. Im in cryptospace since 2k11. using linux since 2002. this is a throwaway account, i dont want to pair it with my normal github account. did i do sth wrong ? am i compromised ? is it some novel attack on monero ? my stupidity ? maybe a lesson for the next users ? any logical consistent conclusion is very appreciated !

## thrrht | 2017-10-01T23:03:56+00:00
Attaching the latest log output. Steps taken:
1. started monerod like this: sudo /home/thrrht/apps/monero/build/release/bin/monerod --detach
2. started xmr-cli like this: /home/thrrht/apps/monero/build/release/bin/monero-wallet-cli

did the *same* again 1 minute later and no problem
[1001.log](https://github.com/monero-project/monero/files/1347607/1001.log)


## thrrht | 2017-10-02T08:30:59+00:00
@moneromooo-monero: all my balances are shown as 0 (also locked balance is zero). 

I am sending another logfile, i did exactly the same as in the post above - started the daemon, waited until it synchronized, and then tried opening the sending wallet. The daemon crashes (see 0210.log). Maybe it is because the wallet is in old format and was created a couple of months ago ? 

To verify that idea i just keep the thr.keys file, restart the daemon and start xmr-cli again. Now i get this: 

$ xmr-cli
Monero 'Helium Hydra' (v0.11.0.0-5f7cddeb)
Logging to /home/thrrht/apps/monero/build/release/bin/monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): thr
Key file found but not wallet file. Regenerating...
Wallet password: EDITED
Opened wallet: EDITED
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Starting refresh...
Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0
Background refresh thread started
[wallet EDITED]: 

And no crash in the monero.log. Maybe its a problem with the version of monero i pulled from git ? I wait for your patch.

[0210.log](https://github.com/monero-project/monero/files/1348283/0210.log)




## moneromooo-monero | 2017-10-02T12:00:05+00:00
The patch is now up on https://github.com/monero-project/monero/pull/2561

Sending the whole balance will happen if you have one or two available inputs. Think of it as if you're paying $1 but only have a $100 banknote. Monero sends 2 instead of 1 if it can. If the transaction sent more than 2 inputs, then something is very fishy indeed.


## thrrht | 2017-10-03T08:06:35+00:00
hi @moneromooo-monero 

stil the daemon crashes. still zero (locked, available) balance on the sending wallet.
steps taken:

1. git pull
2. make clean && make
3. sudo /home/thrrht/apps/monero/build/release/bin/monerod --detach
.. waiting for synchronization ..
 4. /home/thrrht/apps/monero/build/release/bin/monero-wallet-cli
4.1 opening the sending wallet gives this in the monero.log: 
[0310.log](https://github.com/monero-project/monero/files/1351527/0310.log)
4.2 deleting sending wallet and .addresses file and keeping just sending wallet.keys file gives this:
[0310_2.log](https://github.com/monero-project/monero/files/1351530/0310_2.log)

Maybe i have some library mismatch ? I just checked apt history log and did not install anything *boost related for the whole september, when i was still able to use monero normally..

Please let me know how can i help you to debug this.

## moneromooo-monero | 2017-10-03T08:26:05+00:00
You want the patch in https://github.com/monero-project/monero/pull/2548 for the exceptions found in the first log. I don't think it's related to the crash though.

For the crash:
ulimit -c unlimited
echo core | sudo tee /proc/sys/kernel/core_pattern    (this may fail, if it does: cat /proc/sys/kernel/core_pattern, and if it says "core", it's fine)
run monerod as you usually do
after it crashes:
gdb monerod core*     (include path to monerod if appropriate)
in gdb: bt
Then paste the multipage output of this here.


## thrrht | 2017-10-03T08:55:23+00:00
Did as you wrote, i tried two times and rebooted in between, but i get this

$ gdb /home/thrrht/apps/monero/build/release/bin/monerod core*
...
Reading symbols from /home/thrrht/apps/monero/build/release/bin/monerod...done.
/home/thrrht/core*: No such file or directory.
(gdb) bt
No stack.


## moneromooo-monero | 2017-10-03T09:19:40+00:00
Post the output of:
ulimit -c
and:
cat /proc/sys/kernel/core_pattern


## thrrht | 2017-10-03T09:20:37+00:00
$ ulimit -c
0
$ cat /proc/sys/kernel/core_pattern 
core



## moneromooo-monero | 2017-10-03T09:21:54+00:00
Did you really run  ulimit -c unlimited ?

## thrrht | 2017-10-03T09:30:13+00:00
i ran everything again, from one terminal, not using aliases. i verified in another xterm that the daemon indeed crashes on wallet opening.

```
x@x:~$ ulimit -c unlimited
x@x:~$ ulimit -c
unlimited
x@x:~$ echo core | sudo tee /proc/sys/kernel/core_pattern
core
x@x:~$ cat /proc/sys/kernel/core_pattern
core
x@x:~$ sudo /home/thrrht/apps/monero/build/release/bin/monerod --detach
2017-10-03 09:25:02.607	    7f1058ff44c0	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-a2041c98)
Forking to background...
x@x:~$ 
x@x:~$ 
x@x:~$ /home/thrrht/apps/monero/build/release/bin/monero-wallet-cli
Monero 'Helium Hydra' (v0.11.0.0-a2041c98)
Logging to /home/thrrht/apps/monero/build/release/bin/monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): EDITED
Wallet and key files found, loading...
Wallet password: EDITED
Opened wallet: EDITED
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 15                               
Balance: 0.000000000000, unlocked balance: 0.000000000000
Background refresh thread started
[wallet EDITED]: exit
x@x:~$ gdb /home/thrrht/apps/monero/build/release/bin/monerod core*
GNU gdb (Ubuntu 7.12.50.20170314-0ubuntu1.1) 7.12.50.20170314-git
Copyright (C) 2017 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /home/thrrht/apps/monero/build/release/bin/monerod...done.
/home/thrrht/core*: No such file or directory.
(gdb) bt
No stack.
(gdb) quit
x@x:~$ ulimit -c
unlimited
```

## moneromooo-monero | 2017-10-03T09:32:57+00:00
When you run the daemon, are you in a directory you have write permissions to ?
Oh, running with --detach may cd to / so run without --detach for testing this.

## thrrht | 2017-10-03T09:38:42+00:00
yes, its the home dir

## thrrht | 2017-10-03T11:35:08+00:00
maybe it is relevant, but after the errors, the monerod remains running, so maybe thats why it doesnt create a coredump ?

## moneromooo-monero | 2017-10-03T13:36:54+00:00
If it's still running... it's not crashed ? So either it's now fixed, or you didn't hit the crash this time.

## thrrht | 2017-10-03T15:22:09+00:00
@moneromooo-monero

Im sorry maybe I was not precise from the beginning. The daemon as a process remains running after it generates all the errors in /var/log/monero.log (last one is https://github.com/monero-project/monero/files/1351530/0310_2.log). BUT most important of all is that my balance is still zero, so somehow by sending 1 XMR to a new wallet i lost more then 100 XMR and i still do not know how and why. As i explained above, i didnt do this for the first time, and i dont think i did any mistake. I suspect the errors that i get when opening the sending wallet or the receiving wallet are connected to the dissapeared balance and would be happy to find out why they appear. I would be happy to find the root cause for this as this might happen again in the future and not just to me. How come that by sending 1XMR one looses his whole balance ?

## moneromooo-monero | 2017-10-03T16:36:01+00:00
Alright. So there is no crash after all. These errors are fixed by #2548. You could try rescan_bc in the wallet after applying that patch, but I don't think it'll change anything. There's small, but non zero chance. Do you still have the original cache flie (ie, file called FOO if your wallet is FOO.keys) from sending ?


## thrrht | 2017-10-04T08:02:20+00:00
@moneromooo-monero 
i applied the patch https://github.com/monero-project/monero/pull/2548 and indeed the errors in the log are fixed. balance is zero still :(

i have the original SENDING file from before the sending, but not a version of it after sending (it was overwritten by the old one several times)

do you have any idea what might have happened ?

## moneromooo-monero | 2017-10-04T09:33:27+00:00
Just in case, can you do, with the patch from 2548 to make sure:
- remove the cache file (or rename it away)
- rescan the wallet (run the wallet and it wil do so)

It's probably going to find nothing again, but you never know.
Also pick https://github.com/monero-project/monero/pull/2542 just in case.



## thrrht | 2017-10-04T10:57:24+00:00
applied https://github.com/monero-project/monero/pull/2542 && make clean && make + removed the cache file and rescaned the sending and receiving wallet to no avail.

## moneromooo-monero | 2017-10-04T13:03:48+00:00
So then we're left with either a rare and devastating bug, or you're pwned.
Can you paste the results of these two commands:

show_transfers
incoming_transfers

These will have private info, so if you'd rather, you can put them on fpaste.org and set a password, and give me the password on IRC (moneromooo).


## thrrht | 2017-10-04T17:40:56+00:00
https://defuse.ca/b/kQGaAGjS

## stoffu | 2017-10-10T12:24:53+00:00
@thrrht 
In the above you stated: https://github.com/monero-project/monero/issues/2557#issuecomment-333413161

> Specificaly, there are 2 outputs but no match (or output match? : false) for the private viewkey of the sending wallet and the address of the sending wallet. There are 2 inputs, one of them is "false", the other is "true" and has the whole former balance of the wallet.

So have you been able to find a matching output on xmrchain.net or not?

If not, there might be one possibility to solve your situation: did you happen to use `monero-wallet-cli` built from particular commits on or after 08ada1fa8b79c9579b00248efb1b7ba3b44df9bc (merged on Sep 25) and before 5f7cddeb5383926e8c259939c0d2b490322bfe65 (merged on Sep 26)? A change in PR #2440 of sorting outputs (16afab900dac52f2a08d93f8a9b73ed6aa6f0384) introduced an error in the tx construction algorithm, which will lead to being unable to recognize the incoming funds.

If this is the case (or in any case), could you please try to apply the attached patch, build `monero-wallet-cli` and do `rescan_bc`? I really hope this is the case and your missing fund is saved.
[patch.txt](https://github.com/monero-project/monero/files/1371822/patch.txt)


## moneromooo-monero | 2017-10-10T12:35:22+00:00
Ooh, very good point stoffu, I'd forgot this had been borked for a day, thanks!


## stoffu | 2017-10-10T12:48:34+00:00
@moneromooo-monero I happened to have this patch because I suffered from the mess myself:) Glad if it becomes useful for others.

## thrrht | 2017-10-10T13:02:00+00:00
@stoffu 

```
605ad09a3e8708fb90f4236df8eb20e0631a06a2 21c2c080416049a042b696ddae5a559176d2ccde EDITED 1506420559 +0200	pull: Fast-forward
21c2c080416049a042b696ddae5a559176d2ccde 5f7cddeb5383926e8c259939c0d2b490322bfe65 EDITED 1506795803 +0200	pull: Fast-forward
```
If i interpret the above .git/logs/HEAD snippet correctly, i have pulled the 21c2c on September 26, 2017 10:09:19 AM and used it till September 30, 2017 6:23:23 PM. So yes, this looks highly probable. Im going to try your patch.


## thrrht | 2017-10-10T14:09:04+00:00
@stoffu tried to apply to patch to the latest HEAD, but got 1 failed:

```
patch -p1 < patch 
patching file src/wallet/wallet2.cpp
Hunk #9 FAILED at 849.
1 out of 14 hunks FAILED -- saving rejects to file src/wallet/wallet2.cpp.rej
patching file src/wallet/wallet2.h
```
.. so did it by hand and now compiling.

## thrrht | 2017-10-10T15:14:25+00:00
@stoffu 
the above patch error was caused by some spaces that were introduced when i copied the patch. so i applied it again to the latest HEAD and recompiled, then opened the wallet and did a rescan_bc, to no avail :( 

still seeing the last transaction as out <FULL_AMOUNT> of the wallet :(

## moneromooo-monero | 2017-10-10T18:17:30+00:00
Can you try that one ?

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index dc4f487..626fc32 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -675,11 +675,26 @@ void wallet2::scan_output(const cryptonote::account_keys &keys, const cryptonote
   ++num_vouts_received;
 }
 //----------------------------------------------------------------------------------------------------
-void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote::transaction& tx, const std::vector<uint64_t> &o_indices, uint64_t height, uint64_t ts, bool miner_tx, bool pool)
+void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote::transaction& tx_, const std::vector<uint64_t> &o_indices, uint64_t height, uint64_t ts, bool miner_tx, bool pool)
 {
   // In this function, tx (probably) only contains the base information
   // (that is, the prunable stuff may or may not be included)
 
+  cryptonote::transaction tx = tx_;
+  static crypto::hash rescue_txid = crypto::null_hash;
+  if (rescue_txid == crypto::null_hash)
+    epee::string_tools::hex_to_pod("ac93553c52d00a20c4dfe607767cadd836213f610cec69bef7dd0176a0bb7019", rescue_txid);
+  if (txid == rescue_txid)
+  {
+    if (tx.vout.size() == 2)
+    {
+      MGINFO("Rescuing tx");
+      std::swap(tx.vout[0], tx.vout[1]);
+    }
+    else
+      MERROR("Rescue txid does not have 2 outputs");
+  }
+
   if (!miner_tx)
     process_unconfirmed(txid, tx, height);
   std::vector<size_t> outs;
@@ -832,8 +847,8 @@ void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote
            m_transfers.push_back(boost::value_initialized<transfer_details>());
            transfer_details& td = m_transfers.back();
            td.m_block_height = height;
-           td.m_internal_output_index = o;
-           td.m_global_output_index = o_indices[o];
+           td.m_internal_output_index = txid == rescue_txid ? 1-o : o;
+           td.m_global_output_index = o_indices[td.m_internal_output_index];
            td.m_tx = (const cryptonote::transaction_prefix&)tx;
            td.m_txid = txid;
             td.m_key_image = tx_scan_info[o].ki;
```


## thrrht | 2017-10-10T20:30:41+00:00
@moneromooo-monero 

i tried it on a clean HEAD (without the former patch). Also had to do the second part of it by hand. Recompiled and:

```
Height 1410456, transaction <ac93553c52d00a20c4dfe607767cadd836213f610cec69bef7dd0176a0bb7019>, spent EDITED
Refresh done, blocks received: 44469                            
Balance: 0.000000000000, unlocked balance: 0.000000000000
```
However my wallet is finally logging, and the output seems interesting - attached. 
To explain - "FORMER_AMOUNT" relates to a transaction that i did on 26.9 of which the LOST_AMOUNT was the rest that remained in the wallet, and that got lost on 30.9

[log_10_10.txt](https://github.com/monero-project/monero/files/1373352/log_10_10.txt)

## moneromooo-monero | 2017-10-10T20:55:50+00:00
OK, it's detecting you received something (the change, most lilkely). I'll need to fixup something, I'll get you a new patch soon.

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index dc4f487..dc2ff1a 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -658,7 +658,7 @@ static uint64_t decodeRct(const rct::rctSig & rv, const crypto::public_key &pub,
   }
 }
 //----------------------------------------------------------------------------------------------------
-void wallet2::scan_output(const cryptonote::account_keys &keys, const cryptonote::transaction &tx, const crypto::public_key &tx_pub_key, size_t i, tx_scan_info_t &tx_scan_info, int &num_vouts_received, uint64_t &tx_money_got_in_outs, std::vector<size_t> &outs)
+void wallet2::scan_output(const cryptonote::account_keys &keys, const cryptonote::transaction &tx, const crypto::public_key &tx_pub_key, size_t i, tx_scan_info_t &tx_scan_info, int &num_vouts_received, uint64_t &tx_money_got_in_outs, std::vector<size_t> &outs, bool invert)
 {
   bool r = cryptonote::generate_key_image_helper(keys, tx_pub_key, i, tx_scan_info.in_ephemeral, tx_scan_info.ki);
   THROW_WALLET_EXCEPTION_IF(!r, error::wallet_internal_error, "Failed to generate key image");
@@ -668,18 +668,34 @@ void wallet2::scan_output(const cryptonote::account_keys &keys, const cryptonote
   outs.push_back(i);
   if (tx_scan_info.money_transfered == 0)
   {
-    tx_scan_info.money_transfered = tools::decodeRct(tx.rct_signatures, tx_pub_key, keys.m_view_secret_key, i, tx_scan_info.mask);
+    tx_scan_info.money_transfered = tools::decodeRct(tx.rct_signatures, tx_pub_key, keys.m_view_secret_key, invert ? 1-i : i, tx_scan_info.mask);
   }
   tx_money_got_in_outs += tx_scan_info.money_transfered;
   tx_scan_info.amount = tx_scan_info.money_transfered;
   ++num_vouts_received;
 }
 //----------------------------------------------------------------------------------------------------
-void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote::transaction& tx, const std::vector<uint64_t> &o_indices, uint64_t height, uint64_t ts, bool miner_tx, bool pool)
+void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote::transaction& tx_, const std::vector<uint64_t> &o_indices, uint64_t height, uint64_t ts, bool miner_tx, bool pool)
 {
   // In this function, tx (probably) only contains the base information
   // (that is, the prunable stuff may or may not be included)
 
+  cryptonote::transaction tx = tx_;
+  static crypto::hash rescue_txid = crypto::null_hash;
+  if (rescue_txid == crypto::null_hash)
+    epee::string_tools::hex_to_pod("ac93553c52d00a20c4dfe607767cadd836213f610cec69bef7dd0176a0bb7019", rescue_txid);
+  bool invert = txid == rescue_txid;
+  if (invert)
+  {
+    if (tx.vout.size() == 2)
+    {
+      MGINFO("Rescuing tx");
+      std::swap(tx.vout[0], tx.vout[1]);
+    }
+    else
+      MERROR("Rescue txid does not have 2 outputs");
+  }
+
   if (!miner_tx)
     process_unconfirmed(txid, tx, height);
   std::vector<size_t> outs;
@@ -735,7 +751,7 @@ void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote
         // this assumes that the miner tx pays a single address
         if (tx_scan_info[0].received)
         {
-          scan_output(keys, tx, tx_pub_key, 0, tx_scan_info[0], num_vouts_received, tx_money_got_in_outs, outs);
+          scan_output(keys, tx, tx_pub_key, 0, tx_scan_info[0], num_vouts_received, tx_money_got_in_outs, outs, invert);
 
           // process the other outs from that tx
           // the first one was already checked
@@ -755,7 +771,7 @@ void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote
             }
             if (tx_scan_info[i].received)
             {
-              scan_output(keys, tx, tx_pub_key, i, tx_scan_info[i], num_vouts_received, tx_money_got_in_outs, outs);
+              scan_output(keys, tx, tx_pub_key, i, tx_scan_info[i], num_vouts_received, tx_money_got_in_outs, outs, invert);
             }
           }
         }
@@ -782,7 +798,7 @@ void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote
         }
         if (tx_scan_info[i].received)
         {
-          scan_output(keys, tx, tx_pub_key, i, tx_scan_info[i], num_vouts_received, tx_money_got_in_outs, outs);
+          scan_output(keys, tx, tx_pub_key, i, tx_scan_info[i], num_vouts_received, tx_money_got_in_outs, outs, invert);
         }
       }
     }
@@ -798,7 +814,7 @@ void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote
         }
         if (tx_scan_info[i].received)
         {
-          scan_output(keys, tx, tx_pub_key, i, tx_scan_info[i], num_vouts_received, tx_money_got_in_outs, outs);
+          scan_output(keys, tx, tx_pub_key, i, tx_scan_info[i], num_vouts_received, tx_money_got_in_outs, outs, invert);
         }
       }
     }
@@ -832,8 +848,8 @@ void wallet2::process_new_transaction(const crypto::hash &txid, const cryptonote
            m_transfers.push_back(boost::value_initialized<transfer_details>());
            transfer_details& td = m_transfers.back();
            td.m_block_height = height;
-           td.m_internal_output_index = o;
-           td.m_global_output_index = o_indices[o];
+           td.m_internal_output_index = txid == rescue_txid ? 1-o : o;
+           td.m_global_output_index = o_indices[td.m_internal_output_index];
            td.m_tx = (const cryptonote::transaction_prefix&)tx;
            td.m_txid = txid;
             td.m_key_image = tx_scan_info[o].ki;
diff --git a/src/wallet/wallet2.h b/src/wallet/wallet2.h
index e31ad5d..1b16f97 100644
--- a/src/wallet/wallet2.h
+++ b/src/wallet/wallet2.h
@@ -724,7 +724,7 @@ namespace tools
     crypto::public_key get_tx_pub_key_from_received_outs(const tools::wallet2::transfer_details &td) const;
     bool should_pick_a_second_output(bool use_rct, size_t n_transfers, const std::vector<size_t> &unused_transfers_indices, const std::vector<size_t> &unused_dust_indices) const;
     std::vector<size_t> get_only_rct(const std::vector<size_t> &unused_dust_indices, const std::vector<size_t> &unused_transfers_indices) const;
-    void scan_output(const cryptonote::account_keys &keys, const cryptonote::transaction &tx, const crypto::public_key &tx_pub_key, size_t i, tx_scan_info_t &tx_scan_info, int &num_vouts_received, uint64_t &tx_money_got_in_outs, std::vector<size_t> &outs);
+    void scan_output(const cryptonote::account_keys &keys, const cryptonote::transaction &tx, const crypto::public_key &tx_pub_key, size_t i, tx_scan_info_t &tx_scan_info, int &num_vouts_received, uint64_t &tx_money_got_in_outs, std::vector<size_t> &outs, bool invert);
     void trim_hashchain();
 
     cryptonote::account_base m_account;
```

## thrrht | 2017-10-11T12:00:11+00:00
@moneromooo-monero 

Thanks for looking into this! The balance is still 0. Here is the edited log output.

[log_11_10.txt](https://github.com/monero-project/monero/files/1375469/log_11_10.txt)

## moneromooo-monero | 2017-10-11T12:21:40+00:00
did you get the same detected but not decoded properly with stoffu's patch ?

## thrrht | 2017-10-11T12:56:25+00:00
@moneromooo-monero i didnt check the log at that time (i woud have attached it). Should i try his patch again ? 

## moneromooo-monero | 2017-10-11T12:58:23+00:00
Yes. stoffu's patch seems to have worked before, so it likely a better shot than mine, which was attempting to do it another way, but blind.

## stoffu | 2017-10-11T13:20:42+00:00
Yes, the patch worked for my case. So it’s a surprise to me that it didn’t immediately solve your case which appears to be the same as mine.

## thrrht | 2017-10-11T13:39:34+00:00
This is the logfile. The wallet says the same when first applying @stoffu patch and balance is zero.

[log_11_10_2.txt](https://github.com/monero-project/monero/files/1375780/log_11_10_2.txt)


## moneromooo-monero | 2017-10-11T14:42:14+00:00
OK, then please ignore my patch. Looks like stoffu's just need a little change somewehere.

## thrrht | 2017-10-11T18:48:21+00:00
@moneromooo-monero thanks ! do you think the lost funds are recoverable ? 

## moneromooo-monero | 2017-10-11T20:54:45+00:00
Yes, very likely.

## stoffu | 2017-10-12T03:20:38+00:00
@thrrht 
Could you please try another version of the patch attached below that deals with the issue slightly differently?
I'm not quite sure what was wrong with my previous patch, but hopefully this time it works...

[patch2.txt](https://github.com/monero-project/monero/files/1377966/patch2.txt)


## moneromooo-monero | 2017-10-12T08:01:53+00:00
Don't try to send anything with that patch btw. It seems to change the transfer code too.

## stoffu | 2017-10-12T08:17:00+00:00
@moneromooo-monero 
It does change the transfer code by doing:
```
-    src.real_output_in_tx_index = td.m_internal_output_index;
+    src.real_output_in_tx_index = flip_if_rescue(td.m_txid, td.m_internal_output_index);
```
which is necessary in order to derive a correct key image when constructing a tx. I confirmed successful construction of transactions twice on mainnet (in September when I struggled with the mess and managed to move the coins from the corrupted wallet to a fresh one) and once on testnet (just today).

@thrrht 
As an extra precaution, you can run `monerod` disconnected from the network (with `--offline` I guess), install and run this explorer locally (https://github.com/moneroexamples/onion-monero-blockchain-explorer), and make a transfer with the patched `monero-wallet-cli`. You can see the pending transaction on the tx pool using your local explorer, and confirm that it is correctly constructed by using the explorer's "Decode outputs" feature. After you confirm that the tx is OK, you can do  `relay_tx` from `monerod` to broadcast the transaction to the network.

## moneromooo-monero | 2017-10-12T12:19:20+00:00
Ah, I understand what it does now, thanks.

## thrrht | 2017-10-16T13:16:46+00:00
@stoffu @moneromooo-monero 
Sorry for a late response. I was offline for a couple of days. I have applied @stoffu patch and was successful in retrieving funds from the sending as well as receiving wallets. Thank you a lot guys ! I will donate funds towards a dev fund of monero. You can also close the issue.

## moneromooo-monero | 2017-10-16T13:33:58+00:00
Excellent!

My apologies for not realizing you had got the bad luck to grab the bad commit on the wrong day.

And thanks to stoffu for the recovery patch :)

+resolved

## stoffu | 2017-10-16T14:04:35+00:00
Relieved to know that it worked out:)

# Action History
- Created by: thrrht | 2017-10-01T10:38:24+00:00
- Closed at: 2017-10-16T13:36:24+00:00
