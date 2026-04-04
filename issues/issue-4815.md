---
title: Can not recover from 25 word mnemonic
source_url: https://github.com/monero-project/monero/issues/4815
author: moneroproblem
assignees: []
labels: []
created_at: '2018-11-07T00:19:23+00:00'
updated_at: '2022-02-22T21:41:05+00:00'
type: issue
status: closed
closed_at: '2022-02-22T21:41:05+00:00'
---

# Original Description
I have problems restoring a wallet using the 25word mnemonic. If a github issue is not the right place to mention this, please let me know and I'll delete the issue.

In 2016 I have created a monero wallet - with a software version somewhere around 0.10. When I changed my laptop, I erased the hard disk assuming that I could restore the wallet with the 25 word mnemonic, which I wrote down on two different pieces of paper.

Some days ago, i.e., about two years later, I attempted to restore the wallet with the 25 word mnemonic and failed. The number of monero coins I have in this wallet is not negligible and I am pretty sure that I wrote the 25 mnemonic seed words down correctly. Until now, I have tried the following:

GUI version 0.13.0.3-13 (Mac)

With the GUI version 0.13.0.3-13 (monero version 0.13.0.4) I used "restore wallet from keys or mnemonic seed". When I entered the 25 words got a popup stating: "Electrum-style word list failed verification."

Next, I left out the last word and entered the remaining 24 words. This allowed me to restore a wallet, but it had a balance of 0 and its history was empty ("no history"). In settings, wallet, show seed & keys I could see 25 words. The first 24 words were identical to the words, which I pasted into the gui, but the 25th word was different to the one I left out.

monero-wallet-cli (version 0.13.0.4-release, Mac)

I have also used the command line interface from the subfolder monero-wallet-gui.app/Contents/MacOS:
$ ./monero-wallet-cli --restore-deterministic-wallet
When I enter the 25 words, I get the error "Error: Electrum-style word list failed verification"
When I enter 24 words and enter the 25th word as passphrase a wallet is created (scanning started from block 0), but the balance was 0. The command seed showed 25 completely different words.
When I enter 24 words and use an empty passphrase another wallet is created (scanning started from block 0), the balance was 0. The command "seed" showed the identical 24 words and a different 25th word (same as shown in the gui).

Is there something that I could / should try to restore access to my monero coins?

# Discussion History
## moneromooo-monero | 2018-11-07T09:36:16+00:00
In case there is a bug in restoration, you can always restore with a the version of monero you created the seed with.

There's also an old change where a couple words were replaced, but I think that was before 0.10. I don't remember the details, maybe someone in #monero does.

Last, it's possible your seed is using the old english list, but is also valid with the nw english list. In that case, try adding "--mnemonic-language englishold" or "--mnemonic-language english". This only applies if your mnemonic is in English obviously.


## moneroproblem | 2018-11-07T09:59:45+00:00
@moneromooo-monero Thanks for the fast answer. Yes, my words are in english. I will try "--mnemonic-language englishold" and also try a bunch of older releases. I must admit that I am not sure which release I have used - so trying a version prior to 0.10 sounds like a good idea. I'll update this thread once I have results. Thanks again!

## fluffypony | 2018-11-07T10:02:40+00:00
The dupe words replacement thing was really old, like early 2015 old, so possibly not that.

## moneroproblem | 2018-11-07T10:10:25+00:00
When I execute an older version while the blockchain in ~/.bitmonero has been downloaded with the current v0.13 monerod, I get this warning: 
Error: Daemon uses a different RPC major version (2) than the wallet (1): http://localhost:18081. Either update one of them, or use --allow-mismatched-daemon-version.

Would you recommend downloading the blockchain again with the daemon of the old monerod or is the option --allow-mismatched-daemon-version ok?

## moneromooo-monero | 2018-11-07T10:19:45+00:00
You do not need the blockchain.

## moneromooo-monero | 2018-12-13T12:57:06+00:00
Did you manage to restore it ? If so, once you moved the monero away, I'd like to get the seed and monero version you used so I can debug why current monero doesn't restore it. Assuming it was a correct seed in the first place.

## moneroproblem | 2018-12-14T07:04:28+00:00
Hi @moneromooo-monero,  thanks for you message. 
is there a way to send you a direct message?

## moneromooo-monero | 2018-12-14T10:47:45+00:00
Yes, "/query moneromooo" on Freenode.

## moneromooo-monero | 2019-04-01T18:54:30+00:00
Did you ever find out what happened ?

## moneromooo-monero | 2019-08-27T15:51:22+00:00
ping

## moneroproblem | 2019-08-27T16:32:52+00:00
Hi moneromooo,

sorry for the late reply. I was distracted by life, but I will investigating this further as we have discussed. Within 2 weeks, there will be an update on this issue with my findings. I understand that you don't want open issues sticking around.


## moneromooo-monero | 2019-08-28T10:59:24+00:00
Especially ones where there could be a rare bad bug hiding somewhere :)

Thanks


## moneromooo-monero | 2020-05-16T16:38:20+00:00
ping ? :)

## tsbgithub | 2020-07-17T13:53:50+00:00
Hi,

I had exactly the same issue with a wallet originally made with Monerujo some time in 2018. When trying to use the 25 word seed I got: "Error: Electrum-style word list failed verification". Both when trying to recreate with the latest monerujo app and monero-wallet-cli.

Not sure about the reason, but one thing to note is that the 23rd seed word is "returns". That is not in the current word lists.

I manages to recreate the wallet with the 13 word seed instead using the tool/guide from dEBRUYNE here: [https://monero.stackexchange.com/questions/6886/how-to-use-my-13-word-mymonero-mnemonic-seed-with-the-gui-cli-without-accessing](url)


## moneromooo-monero | 2020-07-27T12:53:26+00:00
Does Monerujo use the same word list as monero-wallet-cli/gui ?

## selsta | 2020-07-27T15:34:05+00:00
Yes

## moneromooo-monero | 2020-07-28T00:04:14+00:00
Did you copy/paste that list, or write it down manually ?

## tsbgithub | 2020-07-28T18:03:39+00:00
copy/paste to text editor, then printed to paper and saved. Also tried replacing "returns" with "return" as i found that word in english_old.h. Did not work with "return" either.

## selsta | 2022-02-22T21:41:05+00:00
No reply from issue creator, closing due to inactivity.

# Action History
- Created by: moneroproblem | 2018-11-07T00:19:23+00:00
- Closed at: 2022-02-22T21:41:05+00:00
