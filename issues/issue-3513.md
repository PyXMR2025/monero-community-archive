---
title: Mnemonic seed restores to wrong address with early blockchain
source_url: https://github.com/monero-project/monero/issues/3513
author: valentin-huebner
assignees: []
labels: []
created_at: '2018-03-28T12:36:23+00:00'
updated_at: '2022-03-16T15:37:34+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:37:34+00:00'
---

# Original Description
I restored a Monero wallet from its mnemonic seed with `monero-wallet-cli`, while my local daemon was running in the background. However, I hadn't downloaded the blockchain yet, so the daemon was downloading the first few blocks at that point. A wrong address was restored from the seed, which was of course empty, but checking `seed` returned what I had entered.

I then copied the whole blockchain from another drive, restarted the daemon, and tried restoring the wallet again. At this point, it restored correctly. I then checked the other wallet, which now gave me a seed that was different from what I had entered, but contained some of the right words.

As recommended [here](https://monero.stackexchange.com/questions/7887/mnemonic-seed-restored-to-wrong-address-with-early-blockchain?noredirect=1#comment6729_7887), I can provide the two public addresses if needed.

# Discussion History
## moneromooo-monero | 2018-03-28T14:23:09+00:00
Are you sure you entered the same words in both cases ? The blockchain isn't used to parse words into a secret key thankfully.

## valentin-huebner | 2018-03-28T14:54:29+00:00
Yes. When I checked the output of `seed` after parsing it was still correct, until I updated the blockchain. The distorted seed contains less than ten words from the real one, so it was quite obvious that it had changed. 

My theory was that maybe there was a change in behaviour of `monero-wallet-cli` at some point, and that the block height is used to determine whether the switch has happened yet.

## moneromooo-monero | 2018-03-28T16:30:32+00:00
If you move the monero to a new address, are you able to then send me the seed for testing (you can GPG encrypt the data with my public key in monero's tree, in utils/gpg_keys/moneromooo.asc) ? It would expose your prior transactions, but I would wipe it off my (encrypted) hard drive after I've debugged (or so I say).

## valentin-huebner | 2018-03-28T22:06:24+00:00
The wallet in question isn't mine, so I'd rather not, sorry. Anyway, here's the addresses if that helps!
[addresses.txt](https://github.com/monero-project/monero/files/1857944/addresses.txt)


## moneromooo-monero | 2018-03-28T22:38:31+00:00
OK. If you are able to, it would be nice if you could run this with valgrind. To do this, you (1) install valgrind, and (2) run your program with "valgrind " in front, eg: valgrind monero-wallet-cli --flag etc.
I'm interested in any output starting with ==. Alternatively, running with ASAN would also be OK, but that requires rebuilding after running cmake with -D SANITIZE=ON.
If you're able to build, and don't mind helping debug, and can still reproduce the issue, I might have some logging changes later on.


## valentin-huebner | 2018-03-29T10:14:50+00:00
Ok, did that. I didn't get any memory errors, so no lines starting with '==' other than the init message. I can build if needed; I'll try reproducing the issue first.

## moneromooo-monero | 2018-09-09T13:05:36+00:00
Could you reproduce the issue ?

## valentin-huebner | 2018-09-10T22:49:21+00:00
Ah sorry! No, it worked fine afterwards. I definitely did enter the right seed though, I tried many times very carefully over the course of several days (since this was about a significant amount of money). Only after updating the blockchain it worked, and I checked with my paper slip afterwards, it definitely was correct on paper, and of the one that I had entered previously nearly all of the words had changed.

# Action History
- Created by: valentin-huebner | 2018-03-28T12:36:23+00:00
- Closed at: 2022-03-16T15:37:34+00:00
