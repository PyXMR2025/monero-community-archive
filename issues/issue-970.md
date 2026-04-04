---
title: Monero GUI freezes after loading wallet
source_url: https://github.com/monero-project/monero-gui/issues/970
author: 1337tester
assignees: []
labels:
- resolved
created_at: '2017-11-23T13:05:27+00:00'
updated_at: '2018-04-19T16:41:10+00:00'
type: issue
status: closed
closed_at: '2018-04-19T16:41:10+00:00'
---

# Original Description
**Problem**
GUI Freezes (I suppose right after the daemon is about to start), 
![freeze_after_start](https://user-images.githubusercontent.com/6553766/33174167-1dfe19d2-d057-11e7-9853-761fc9deb6b2.jpg)

**Steps**
1. Build
2. Launch monero-wallet-gui
3. Load a wallet and enter password

**Additional info**
[freeze_after_start.log](https://github.com/monero-project/monero-gui/files/1499148/freeze_after_start.log)
Distro - Ubuntu 17.10
GUI_VERSION = "v0.11.1.0-81-g2147803"
GUI_MONERO_VERSION = "v0.10.3.1-1086-g49ce5946"


# Discussion History
## 1337tester | 2017-11-23T21:47:41+00:00
bug persists in the newest build
GUI_VERSION = "v0.11.1.0-94-gca71131"
GUI_MONERO_VERSION = "v0.10.3.1-1086-g49ce5946"


## 1337tester | 2017-11-30T23:22:22+00:00
bug persists in the newest build
GUI_VERSION = "v0.11.1.0-100-gd9d2050"
GUI_MONERO_VERSION = "v0.10.3.1-1136-g9fad4008"

any chance to get this fixed? This is basically blocking me to look at the new features:/


## dEBRUYNE-1 | 2017-12-01T11:46:09+00:00
What happens if you run `monerod` separately? If that doesn't work, please perform:

https://github.com/monero-project/monero#debugging

## 1337tester | 2017-12-01T13:52:28+00:00
Monerod seems to work on mainnet (wasn't doing the whole sync though)

On Testnet failing, log here:
[monerod_testnet.txt](https://github.com/monero-project/monero-gui/files/1521786/monerod_testnet.txt)

going to do the debugging

## medusadigital | 2017-12-01T14:53:44+00:00
please increase log level on startup

`./monerod --testnet --log-level 1`

maybe even log-level 2 required

## 1337tester | 2017-12-03T11:53:02+00:00
Valgrind - [valgrind.txt](https://github.com/monero-project/monero-gui/files/1524706/valgrind.txt)
monerod log lvl 2 - [monerod.log](https://github.com/monero-project/monero-gui/files/1524714/monerod.log)




## 1337tester | 2017-12-03T12:12:07+00:00
donwloading the whole testnet again, just checking if it solves the issue

## 1337tester | 2017-12-04T12:37:14+00:00
~~After redownloading the testnet blockchain, the issue is not present anymore~~

Issue persist still, only workaround I have is to use the remote node (but need to switch quickly at start)

## medusadigital | 2017-12-07T11:15:12+00:00
Hei, Im not sure, but i might have another workaround for you:

- clean all previous p2pstate.bin files for testnet
- download **release** 0.11.1.0
- start `./monerod--testnet `
- let it find some peers and sync a few blocks
- exit it
- start your own built binaries, also with `--testnet --log-level 1`
- should now be able to sync






## 1337tester | 2017-12-07T13:16:07+00:00
Hi @medusadigital,

thanks for the idea, but this is not about workaround (I can make it work with the 0.11.1.0 release, my monero usage is not affected:) ).

I was more concerned there is some bug in the newest build which might appear only on Ubuntu - but if nobody else is experiencing the same, the severity is probably low. 

## medusadigital | 2017-12-07T13:44:39+00:00
Nono, I can confrim there is a known bug, devs are aware. I just wasnt sure you ran into that one or something else. 


moneromoo said he is going to fix it.

there was a previous attempt allready here: https://github.com/moneromooo-monero/bitmonero/tree/peerlist

anyway, i opened a placeholder here: https://github.com/monero-project/monero/issues/2892

im quite sure thats the same issue you are experiencing 




## 1337tester | 2017-12-07T15:59:35+00:00
ok, cool, then I'm fine with closing this one

## ellisonch | 2017-12-08T18:09:46+00:00
My client is also totally locking up just after starting up.  I'm running monero-gui-v0.11.1.0 on windows 10.

## dEBRUYNE-1 | 2017-12-08T18:53:13+00:00
@ellisonch: Can you try:

https://monero.stackexchange.com/questions/6651/my-gui-feels-buggy-freezes-all-the-time

## 1337tester | 2018-04-19T16:36:31+00:00
outdated, please close

## sanderfoobar | 2018-04-19T16:39:21+00:00
Thanks @1337tester 

## sanderfoobar | 2018-04-19T16:39:24+00:00
+resolved

# Action History
- Created by: 1337tester | 2017-11-23T13:05:27+00:00
- Closed at: 2018-04-19T16:41:10+00:00
