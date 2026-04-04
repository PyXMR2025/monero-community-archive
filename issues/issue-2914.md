---
title: seed command not working
source_url: https://github.com/monero-project/monero/issues/2914
author: dam2k
assignees: []
labels: []
created_at: '2017-12-12T22:08:23+00:00'
updated_at: '2017-12-25T20:24:24+00:00'
type: issue
status: closed
closed_at: '2017-12-25T20:24:24+00:00'
---

# Original Description
The "seed" command is not working on my local cli wallet. I'm using the latest official monero binary version v0.11.1.0 64 bit on debian (amd64).

Everything is working as expected, but the seed command. The output below:

dino@blackbeast:~/MONEROCOIN$ ./monero-wallet-cli --wallet-file Wallet --trusted-daemon
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to ./monero-wallet-cli.log
Wallet password: ****************
Opened wallet: 49xxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxx
**********************************************************************
Use "help" command to see the list of available commands.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 0                                
Balance: 8.150135210000, unlocked balance: 8.150135210000
Background refresh thread started
[wallet 49xxXX]: seed
Wallet password: ****************

PLEASE NOTE: the following 25 words can be used to recover access to your wallet. Please write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.


[wallet 49xxXX]: WTF I can recover if I loose this stuff? Thanks.
unknown command: WTF I can recover if I loose this stuff? Thanks.
[wallet 49xxXX]: exit
dino@blackbeast:~/MONEROCOIN$

# Discussion History
## moneromooo-monero | 2017-12-13T09:41:43+00:00
If you look in monero-wallet-cli.log, is there more info (ie, a stack trace maybe) ?

## dam2k | 2017-12-13T21:42:13+00:00
Nope. Anything useful in monero-wallet-cli.log. This is the output just after running the "seed" command:

```
2017-12-13 21:38:21.654	    7ff0f1821ec0	INFO 	msgwriter	src/common/scoped_message_writer.h:102	
PLEASE NOTE: the following 25 words can be used to recover access to your wallet. Please write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.
```


## moneromooo-monero | 2017-12-13T23:13:17+00:00
Can you build with a patch if I post one ?

And just in case, backup the secret keys you get with the "spendkey" and "viewkey" commands. You can restore with them too.

## dam2k | 2017-12-14T00:10:41+00:00
Sure, I could build with a patch. OK that I can recover with those keys, thanks, but the seed command is supposed to work too :-)

## hyc | 2017-12-14T02:08:04+00:00
What seed language is your wallet set to?


## moneromooo-monero | 2017-12-14T10:06:10+00:00
Yes, it's supposed to work.

## moneromooo-monero | 2017-12-14T10:07:11+00:00
```
diff --git a/src/mnemonics/electrum-words.cpp b/src/mnemonics/electrum-words.cpp
index 2fe5d99..1a60211 100644
--- a/src/mnemonics/electrum-words.cpp
+++ b/src/mnemonics/electrum-words.cpp
@@ -362,6 +362,8 @@ namespace crypto
       }
       else
       {
+MGINFO("Unknown language");
+
         return false;
       }
       const std::vector<std::string> &word_list = language->get_word_list();
@@ -369,6 +371,8 @@ namespace crypto
       std::vector<std::string> words_store;
 
       uint32_t word_list_length = word_list.size();
+MGINFO("word list size:  " << word_list_length);
+
       // 8 bytes -> 3 words.  8 digits base 16 -> 3 digits base 1626
       for (unsigned int i=0; i < sizeof(src.data)/4; i++, words += ' ')
       {
@@ -393,6 +397,8 @@ namespace crypto
         words_store.push_back(word_list[w3]);
       }
 
+MGINFO("words store is now " << words_store.size());
+
       words.pop_back();
       words += (' ' + words_store[create_checksum_index(words_store, language->get_unique_prefix_length())]);
       return true;
diff --git a/src/simplewallet/simplewallet.cpp b/src/simplewallet/simplewallet.cpp
index 9504f38..291633e 100644
--- a/src/simplewallet/simplewallet.cpp
+++ b/src/simplewallet/simplewallet.cpp
@@ -312,6 +312,8 @@ bool simple_wallet::seed(const std::vector<std::string> &args/* = std::vector<st
     }
 
     success = m_wallet->get_seed(electrum_words);
+MGINFO("success: " << success);
+
   }
 
   if (success) 
@@ -975,6 +977,9 @@ void simple_wallet::print_seed(std::string seed)
   success_msg_writer(true) << "\n" << tr("PLEASE NOTE: the following 25 words can be used to recover access to your wallet. "
     "Please write them down and store them somewhere safe and secure. Please do not store them in "
     "your email or on file storage services outside of your immediate control.\n");
+size_t ns = 0; for (auto c: seed) if (' '==c) ++ns;
+MGINFO("Seed is " << seed.size() << " c and " << ns << " s");
+
   boost::replace_nth(seed, " ", 15, "\n");
   boost::replace_nth(seed, " ", 7, "\n");
   // don't log
```

## dam2k | 2017-12-15T05:04:33+00:00
The seed language is set to "Italian".
Cannot cleanly apply the patch to master codebase...

```
dino@blackbeast:/tmp/monero$ patch -p1 < ../electrum-words.cpp 
patching file src/mnemonics/electrum-words.cpp
Hunk #1 succeeded at 401 (offset 39 lines).
Hunk #2 succeeded at 410 with fuzz 2 (offset 39 lines).
Hunk #3 succeeded at 436 (offset 39 lines).
patching file src/simplewallet/simplewallet.cpp
Hunk #1 FAILED at 312.
Hunk #2 succeeded at 1347 (offset 372 lines).
1 out of 2 hunks FAILED -- saving rejects to file src/simplewallet/simplewallet.cpp.rej
```
but it was very easy to fix, and the code compiled correctly.
Seed still not working:
```
dino@blackbeast:~/MONEROCOIN$ ./monero-wallet-cli_test --wallet-file Wallet --trusted-daemon
Monero 'Helium Hydra' (v0.11.0.0-319163d2)
Logging to ./monero-wallet-cli_test.log
Wallet password: 
Opened wallet: 49xxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxxXXxx
**********************************************************************
Use "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 7                                
          Account               Balance      Unlocked balance                 Label
 *       0 49XxXx        8.557946570000        8.557946570000       Primary account
----------------------------------------------------------------------------------
          Total        8.557946570000        8.557946570000
Currently selected account: [0] Primary account
Balance: 8.557946570000, unlocked balance: 8.557946570000
Background refresh thread started
[wallet 49XxXx]: seed
Wallet password: 

PLEASE NOTE: the following 25 words can be used to recover access to your wallet. Please write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.


[wallet 49XxXx]: 
```
but now I have this stuff into the cli log (**Unknown language**):
```
2017-12-15 04:56:10.089	    7eff6566f6c0	INFO 	global	src/mnemonics/electrum-words.cpp:404	Unknown language
2017-12-15 04:56:10.089	    7eff6566f6c0	INFO 	global	src/simplewallet/simplewallet.cpp:445	success: 1
2017-12-15 04:56:10.089	    7eff6566f6c0	INFO 	msgwriter	src/common/scoped_message_writer.h:102	
PLEASE NOTE: the following 25 words can be used to recover access to your wallet. Please write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.

2017-12-15 04:56:10.089	    7eff6566f6c0	INFO 	global	src/simplewallet/simplewallet.cpp:1352	Seed is 0 c and 0 s
```
Thank you!

## dam2k | 2017-12-15T05:16:13+00:00
I switched the language from "Italian" to "Italiano" with `set seed language` and now the seed is working, but I will not put here the seed output eheheh.
Thank you for your support! Monero is great!

## moneromooo-monero | 2017-12-15T09:11:50+00:00
The patch was against the version you mentioned in the first post.
I'll add something to warn the user when the language is incorrect.

## moneromooo-monero | 2017-12-22T12:17:41+00:00
Was this wallet created long ago ? I'm wondering how it ended up with a slightly off language name.

## dam2k | 2017-12-22T15:45:08+00:00
YES!!! Good catch. It was created about 2 years ago and upgraded from minor version to minor version.

## moneromooo-monero | 2017-12-25T20:08:17+00:00
+resolved

# Action History
- Created by: dam2k | 2017-12-12T22:08:23+00:00
- Closed at: 2017-12-25T20:24:24+00:00
