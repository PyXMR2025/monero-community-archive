---
title: mixin too low error when running sweep_unmixable
source_url: https://github.com/monero-project/monero/issues/2013
author: kiwiminer
assignees: []
labels: []
created_at: '2017-05-03T10:23:06+00:00'
updated_at: '2017-08-07T17:48:17+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:48:17+00:00'
---

# Original Description
Im having issues with making transactions with the remainder of my dusty wallet that was a result of a mining pool with small payouts.

Anyway, I got the majority to poloniex after sending many small transactions, i had to do this because sweep_unmixable is giving me an error.

Ive got about 2.02 XMR left in my wallet.
On bitcointalk I have been advised that this is a bug and should be reported here.

Below is my output:

[wallet 43xU1y]: sweep_unmixable
Wallet password:
Sweeping 1.659478336157 for a total fee of 0.024714400000.  Is this okay?  (Y/Ye
s/N/No): y
Error: transaction <e36b28297d8e7a19ec8bb656cf2b1069cce2009db84ea39f7dacc110a831
6e59> was rejected by daemon with status: Failed
Error: Reason: mixin too low

If you need my address for any diagnostics it is:
43xU1yfXiYvhGiyQwArZyRX8rgA7zW7c8Z6X7WHy7SbhPsQiEaCavLHHse3Gtds2gUYNrZApNAyNCazi
ozVoQNPJ3o6JkqD

I hope this is all the info you need

TIA


# Discussion History
## moneromooo-monero | 2017-05-06T11:48:02+00:00
Please try it again with log level 2 in the wallet (either start with --log-level 2, or run set_log 2 after starting). Paste the relevant log portions on fpaste.org (you can use a password if you want since the log will include some info about which outputs you own, which you might want to be private: give me the password on IRC, I'm "moneromooo" there).

## kiwiminer | 2017-05-07T00:58:17+00:00
OK, done that, there is nothing sensitive on my account, so no password needed :)
Here is the link below:
https://paste.fedoraproject.org/paste/0~5KXUlj~tBcsbd9rO~7eV5M1UNdIGYhyRLivL9gydE=

## moneromooo-monero | 2017-05-07T16:28:29+00:00
Thanks. The problem is that the wallet thinks that the min mixin is 4, though it is still 2 till v6 (it used to be till v5, but that was pushed back recently). Easy fix in the wallet only, I'll push soon.

## moneromooo-monero | 2017-05-07T17:29:01+00:00
https://github.com/monero-project/monero/pull/2017

## kiwiminer | 2017-05-07T22:05:13+00:00
Thanks, should be able to empty the dusty wallet once and for all!

## xxnirvana69xx | 2017-05-22T19:42:03+00:00
I'm having the same problem. Is the solution still waiting to be implimented? I'm unsure what to do from here.

## kiwiminer | 2017-05-22T22:34:22+00:00
I think its going to be added to the next release.
Not sure when this will be.
\

## binaryFate | 2017-06-26T11:25:39+00:00
@xxnirvana69xx @kiwiminer You can compile master if you need this before an official release.

## moneromooo-monero | 2017-08-07T17:40:49+00:00
+resolved

# Action History
- Created by: kiwiminer | 2017-05-03T10:23:06+00:00
- Closed at: 2017-08-07T17:48:17+00:00
