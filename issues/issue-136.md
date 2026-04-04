---
title: 'Error opening wallet: std::bad_alloc'
source_url: https://github.com/monero-project/monero-gui/issues/136
author: Jaqueeee
assignees: []
labels: []
created_at: '2016-11-08T23:32:59+00:00'
updated_at: '2018-12-01T16:43:55+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:58:25+00:00'
---

# Original Description
Get this on a wallet created with 0.10 cli-wallet. Other wallets created with GUI works fine. 

2016-Nov-09 00:08:33.732222 Loaded wallet keys file, with public address: XXXXXX
2016-Nov-09 00:08:33.910138 Trying to decrypt cache data
2016-Nov-09 00:08:34.667565 Failed to load encrypted cache, trying unencrypted
monero-core(17654,0x7000002a0000) malloc: *** mach_vm_map(size=10321121864773124096) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
Wallet *WalletManager::openWallet(const QString &, const QString &, bool): opened wallet: XXXXXX, status: 1
2016-Nov-09 00:08:34.875405 ERROR /...../monero-core/monero/src/wallet/api/wallet.cpp:276 Error opening wallet: std::bad_alloc

# Discussion History
## ghost | 2016-11-09T06:00:50+00:00
I get the same error with an old CLI-created wallet file. How can this be fixed?


## Jaqueeee | 2016-11-09T11:10:25+00:00
OK. I'm opening the issue again. My wallet cache was corrupted. Got same error in cli wallet. This worked for me:
1. Delete or move wallet cache (the file without .keys or address.txt suffix) 
2. Open wallet in monero-cli-wallet
3. The wallet cache restores. 
After this you should be able to open it in GUI again. Restoring wallet cache in GUI doesn't work yet, therefore you need to open it in cli wallet.  You could also restore from seed of course.


## ghost | 2016-11-12T07:34:46+00:00
Deleting the cache-file also worked for me, the error has gone.


## fluffypony | 2016-11-13T17:58:25+00:00
Closing as fixed


## MBuffenoir | 2017-01-17T14:42:35+00:00
I'm still having the same issue it looks like:

```
⚡  monero-wallet-cli --wallet-file=/Users/lalu/Monero/wallets/lalu/lalu
Monero 'Wolfram Warptangent' (v0.10.1.0-release)
Logging at log level 0 to /Users/lalu/monero-wallet-cli.log
Password: ***************
monero-wallet-cli(7694,0x7fffbd1f83c0) malloc: *** mach_vm_map(size=7809639168886382592) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
monero-wallet-cli(7694,0x7fffbd1f83c0) malloc: *** mach_vm_map(size=1630251929812803584) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
Error: failed to load wallet: std::bad_alloc
```

FYI, This wallet was generated using the gui beta

Hope those info help

## Jaqueeee | 2017-01-17T19:54:08+00:00
@MBuffenoir 
If your wallet was created with GUI beta you can only open it with the cli wallet bundled with the GUI. If you want to use older CLI wallet you need to delete the wallet cache file before opening.

## MBuffenoir | 2017-01-17T20:12:22+00:00
@Jaqueeee Thanks for the answer. I thought they would be compatible.

## Jaqueeee | 2017-01-17T20:28:22+00:00
The wallet cache got changed to a portable format that will make it easier to switch between platforms. Unfortunately it's not backwards compatible. More info here: https://github.com/monero-project/monero/pull/1462

## Baltsar | 2017-05-21T20:47:41+00:00
http://imgur.com/a/XXn8G

This happened to me, since I am not that tech savy where could I find the cache folder, I read it could work. Otherwise I can just reinstall the GUI on another computer and restore my seed words, right? 

## palexande | 2018-10-18T23:17:28+00:00
Getting this same error with latest CLI and GUI builds.  This was an account restored with seed via GUI.  Looks like the bug hasn't quite been nailed down yet?

## t-node | 2018-10-22T20:03:59+00:00
I am facing the same issue during restoration

## dEBRUYNE-1 | 2018-10-23T14:24:49+00:00
@palexande + @t-node  - The bug was "reintroduced" in GUI v0.13.0.3. It will be resolved in the upcoming GUI v0.13.0.4 though. 

## qertoip | 2018-12-01T14:54:43+00:00
Facing this bug on v0.13.0.4 both CLI and GUI.

**Edit:** the problem is only present if 0.13.0.4 is being ran over cache from 0.13.0.3. Rebuilding cache with 0.13.0.4 permanently resolves the problem.

# Action History
- Created by: Jaqueeee | 2016-11-08T23:32:59+00:00
- Closed at: 2016-11-13T17:58:25+00:00
