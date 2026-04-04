---
title: issue with ledger + monero osx wallet
source_url: https://github.com/monero-project/monero/issues/5228
author: heapxor
assignees: []
labels: []
created_at: '2019-03-04T14:39:51+00:00'
updated_at: '2021-08-13T04:30:19+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:30:19+00:00'
---

# Original Description
Hi,
not sure why/how u closed that issue. There is no solution and its still not working.



Since libpcsc-lite is now removed, this is moot. There are other bugs about new ledger comms failure with libhidapi :)

+resolved

_Originally posted by @moneromooo-monero in https://github.com/monero-project/monero/issues/4049#issuecomment-428152685_

# Discussion History
## moneromooo-monero | 2019-03-04T15:16:58+00:00
Because we do not use that library anymore, so it cannot error out anymore.
If you have another problem with Ledger on Mac, file another bug, which you did, but you did not give details of what's wrong. That's on master, since 0.14.0.0 might not be using this new library yet. So if you still can't get it to work on master, post details.

By the way, don't use Ledger with 0.14.0.0 on mainnet for now, there is a suspected money losing bug that's being tracked.


## lacksfish | 2019-03-17T05:58:39+00:00
I also do get this error. It was working before the version 0.14 release

`Error: unexpected error: Wrong Device Status : SW=6914 (EXPECT=9000, MASK=ffff)`

This only happens upon sending a transaction, up to that point it does work fine

EDIT: System is Ubuntu 18.04

## dEBRUYNE-1 | 2019-03-17T07:14:40+00:00
@lacksfish:

A few tips:

1. Make sure your Ledger Live firmware is v1.5.5

2. Make sure your Ledger Monero app is v1.2.2 

3. Make sure you are using GUI v0.14.0.0 

4. Make sure Ledger Live is closed. 

If you got all these steps covered, try:

- Using a different USB port
- Using a different USB cable 

## moneromooo-monero | 2019-03-17T10:26:28+00:00
Are you getting this problem with *master* or 0.1[34] ?

## lacksfish | 2019-03-17T18:05:51+00:00
@dEBRUYNE-1 

1. Ledger is on firmware 1.5.5
2. Monero app is version 1.2.2
3. GUI version is v0.14 (i used the official release first and then built it myself, same problem)
4. Ledger Live was closed

Also tried different USB ports and using the "official" Ledger USB cable.

I'm using an Ubuntu distro (18.04), so this might be an issue we see most on Ubuntu and maybe macOS.

## lacksfish | 2019-03-17T18:08:24+00:00
@moneromooo-monero 

Was using official GUI release first, so was using official 0.14 Monero version for sure.
When I built the GUI myself later, it automatically checked out a recent commit to compile monerod.

That's the one it built:
> commit 6cadbdcd2d952433db3c2422511ed4d13b2cc824 (HEAD -> release, tag: v0.14.0.2, origin/release-v0.13)


## lacksfish | 2019-03-17T18:29:42+00:00
So the device does get recognized initially

```
2019-03-17 18:13:38.743	    xxxxxxxxxxxx	DEBUG	device.ledger	src/device/device_ledger.cpp:353	Device 0 HIDUSB inited
2019-03-17 18:13:38.763	    xxxxxxxxxxxx	DEBUG	device.io	src/device/device_io_hid.cpp:88	HID Device found: 0001:000b:00
```

We then get to

```
2019-03-17 18:17:08.399	    xxxxxxxxxxxx	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:9043	Done creating 1 transactions, 0.000514550000 total fee, 0.000000000000 total change
```

After accepting the fee on the Ledger, it starts screaming:
(All RESP's before that did return 9000)
```
2019-03-17 18:21:34.080	    xxxxxxxxxxxxx	DEBUG	device.ledger	src/device/device_ledger.cpp:270	RESP : 6914 
2019-03-17 18:21:34.080	    xxxxxxxxxxxxx	ERROR	device.ledger	src/device/device_ledger.cpp:319	Wrong Device Status : SW=6914 (EXPECT=9000, MASK=ffff)
2019-03-17 18:21:34.081	    xxxxxxxxxxxxx	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 0
2019-03-17 18:21:34.081	    xxxxxxxxxxxxx	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.081	    xxxxxxxxxxxxx	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.081	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.081	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 3
2019-03-17 18:21:34.081	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:848	generate_key_derivation  : PARSE mode with known viewkey
2019-03-17 18:21:34.081	    xxxxxxxxxxxxx	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2037	startRefresh: refresh started/resumed...
2019-03-17 18:21:34.081	    xxxxxxxxxxxxx	WARN 	frontend	src/wallet/api/wallet.cpp:367	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x7f00d8024c90), parent's thread is QThread(0x556c7281b510), current thread is QThread(0x556c76b4b620)
2019-03-17 18:21:34.081	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 0
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 3
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:510	derive_subaddress_public_key  : PARSE mode with known viewkey
2019-03-17 18:21:34.082	    zzzzzzzzzzzzz	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.082	    zzzzzzzzzzzzz	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.082	    zzzzzzzzzzzzz	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 3
2019-03-17 18:21:34.082	    zzzzzzzzzzzzz	DEBUG	device.ledger	src/device/device_ledger.cpp:510	derive_subaddress_public_key  : PARSE mode with known viewkey
2019-03-17 18:21:34.082	    zzzzzzzzzzzzz	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.082	    zzzzzzzzzzzzz	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 0
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.082	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 3
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:848	generate_key_derivation  : PARSE mode with known viewkey
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 0
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 3
2019-03-17 18:21:34.084	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:510	derive_subaddress_public_key  : PARSE mode with known viewkey
2019-03-17 18:21:34.084	    wwwwwwwwwwwww	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.085	    wwwwwwwwwwwww	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.085	    wwwwwwwwwwwww	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 3
2019-03-17 18:21:34.085	    wwwwwwwwwwwww	DEBUG	device.ledger	src/device/device_ledger.cpp:510	derive_subaddress_public_key  : PARSE mode with known viewkey
2019-03-17 18:21:34.085	    wwwwwwwwwwwww	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.085	    wwwwwwwwwwwww	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:414	Switch to mode: 0
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2512	update_pool_state end
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2791	Refresh done, blocks received: 1, balance (all accounts): x.xxxxxxxxxxxx, unlocked: x.xxxxxxxxxxxx
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	DEBUG	frontend	src/wallet/api/wallet.cpp:359	refreshed
2019-03-17 18:21:34.085	    yyyyyyyyyyyyy	TRACE	WalletAPI	src/wallet/api/wallet.cpp:1982	refreshThreadFunc: waiting for refresh...
2019-03-17 18:21:34.096	    vvvvvvvvvvvvv	DEBUG	frontend	src/wallet/api/wallet.cpp:359	Transaction created
2019-03-17 18:21:34.096	    vvvvvvvvvvvvv	DEBUG	frontend	src/wallet/api/wallet.cpp:359	Hiding processing splash
2019-03-17 18:21:34.096	    vvvvvvvvvvvvv	ERROR	frontend	src/wallet/api/wallet.cpp:371	Can't create transaction:  unexpected error: Wrong Device Status : SW=6914 (EXPECT=9000, MASK=ffff)
```

## moneromooo-monero | 2019-03-17T19:41:57+00:00
And does it work on master ?

## lacksfish | 2019-03-17T20:53:40+00:00
Same issue when using monero built from latest master @ ea07a9bc61a87903cc338d6227f90fabb6c75c86

## moneromooo-monero | 2019-03-17T21:09:20+00:00
Thanks. So it is not a pcsc bug after all :/

## lacksfish | 2019-03-17T21:22:31+00:00
It is not! Happy days. Why didn't I check this before?!

I took the liberty to refresh my udev rules straight from the ledger repo at https://github.com/LedgerHQ/udev-rules which has seen some changes recently.

This doesn't solve the issue.

## lacksfish | 2019-03-17T21:25:20+00:00
@heapxor could you maybe investigate the content of your `/etc/udev/rules.d/20-hw1.rules` ?

Are there any differences between what you have and what is on the master branch in the ledger repo?

Compare against https://github.com/LedgerHQ/udev-rules/blob/master/20-hw1.rules

## moneromooo-monero | 2019-03-17T21:39:06+00:00
I'd read the shell script before running it.

## lacksfish | 2019-03-17T21:45:56+00:00
It also doesn't seem to consistently solve the issue. Now it is again reoccurring on both master and release...

## lacksfish | 2019-03-17T22:02:51+00:00
Ok, the issue somehow seems to be that it's not possible to send to the main addresses.

Sending to sub-addresses works..

## cslashm | 2019-03-18T08:52:08+00:00
6914 means the destination address shown during ephemeral destination key derivation and shown during the hash computation (mlsag-prehash) are not same or not presented in the same order. 

That's strange you get that. 

Note: definitively not related to hid,pcsc,udev...

## lacksfish | 2019-03-18T19:38:26+00:00
@cslashm, so it seems to throw here: https://github.com/LedgerHQ/ledger-app-monero/blob/2cb94bf774eccea89de9de34192205710e6a17f1/src/monero_prehash.c#L130

## lacksfish | 2019-03-18T19:41:12+00:00
Could it be related to the recent change for dummy payment ids, which get added if the field is not used?

## lacksfish | 2019-03-18T20:35:01+00:00
Tested again, sending to subaddresses works, it is only the main address starting with a `4` that is affected by this bug.

## pricead | 2019-03-20T21:48:00+00:00
Same issue when sending to a "4" address (Error: unexpected error: Wrong Device Status : SW=6914 (EXPECT=9000, MASK=ffff)) with OSX v0.14.0.2-release and Ledger XMR app 1.2.2

(also see the identical error with monerujo 1.11.5 + Ledger XMR app 1.2.2)

## moneromooo-monero | 2019-04-17T12:08:16+00:00
Is this fixed now ? The other bug linked above says the leger code update should fix it. Has anyone tried it ?

## lacksfish | 2019-04-17T12:10:01+00:00
Pretty sure it had to do with the recent change of how payment IDs are being used.
I will give it a spin this evening and will report back, promise.

## moneromooo-monero | 2019-04-17T13:05:03+00:00
That'd be surprising, but hey, it's software so you never know :)
Thanks

## cslashm | 2019-04-17T15:27:13+00:00
That's weird, It means that order of ouput change between the computation of ephemeral destination key address computation and the signature

## cslashm | 2019-04-18T08:14:18+00:00
I've just successfully transfer from a 45...to 4A... address.
I'm waiting for more report to try to be able to reproduce.
If I'm not,  I will provide in PM some directives to send me detailed log without disclosing privacy. 



## lacksfish | 2019-04-18T09:34:08+00:00
I've just built the GUI and Daemon from the respective master branches, but apparently I need the Monero app version 1.3.1, while I only have version 1.2.2 and I have no way to update.

Ledger Live tells me 1.2.2 is the latest version, so right now I can't access my Ledger wallet at all, lol.

## lacksfish | 2019-04-18T09:45:35+00:00
@moneromooo-monero I'd have tested it otherwise, but I'm all ears regarding recommended commit hashes to check out :)

## cslashm | 2019-04-18T13:06:20+00:00
@lacksfish  You can install it by activating "dev" mode in Live setting and relaunch the Live with `FORCE_PROVIDER=4 live-exec`

## lacksfish | 2019-04-18T14:29:36+00:00
Gotcha, will report back

## lacksfish | 2019-04-18T14:35:13+00:00
I get a
> Can't create transaction: internal error: Bad offset calculation

I'm using plain master build from monero-wallet-gui
when trying to send any amount to any address, sub-address or main-address

## moneromooo-monero | 2019-04-18T15:06:19+00:00
Do you have pre-rct outputs ?

## moneromooo-monero | 2019-04-18T15:06:44+00:00
"incoming_transfers available" will tell you.

## moneromooo-monero | 2019-04-18T15:16:51+00:00
Nevermind, this bug was only in the lineup patch, which is not merged yet (fixed now though).

## cslashm | 2019-04-18T15:31:47+00:00
I retested 1.3.1 few days ago with master CLI and it has worked. It required both client and daemon to be from up-to-date master.

## lacksfish | 2019-04-18T20:23:00+00:00
I will check again, I've built the GUI myself but let me double check which core build I used with the GUI.

## lacksfish | 2019-04-19T19:42:28+00:00
monero commit: 7973fb6a69ffa7c4f9d1671250d4a09ebf2965bb
monero gui commit: 10926644bfe049b3c7b1dcd9b274a3a79cfa1e94

> Can't create transaction: internal error: Bad offset calculation

Still get the same error when crafting the tx. Should I try a different commit/branch?

## lacksfish | 2019-04-23T16:55:48+00:00
@moneromooo-monero Any specific commits/branches I can check out? I'm eager to try.

## moneromooo-monero | 2019-04-23T17:11:01+00:00
Try current master. If it still does this, I'll get you a log patch..

## lacksfish | 2019-04-23T17:36:06+00:00
Yay, I ended up using the latest official release with v0.14.0.0 GUI and v0.14.0.2 Monero client and voila, I was able to send to a different primary address of an external wallet. With that version though I had the issue of not being able to send to my *own* primary address, so I'm glad that worked out.

On the Ledger I was using v1.2.2, which is the only other difference I can think of.

@heapxor still having issues or can this be closed? I kinda hijacked the issue anyways... :)

# Action History
- Created by: heapxor | 2019-03-04T14:39:51+00:00
- Closed at: 2021-08-13T04:30:19+00:00
