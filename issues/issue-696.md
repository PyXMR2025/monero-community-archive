---
title: '[osx] Error when quitting: monero-wallet-gui quit unexpectedly.'
source_url: https://github.com/monero-project/monero-gui/issues/696
author: jonathancross
assignees: []
labels: []
created_at: '2017-04-26T19:41:02+00:00'
updated_at: '2018-01-20T18:30:18+00:00'
type: issue
status: closed
closed_at: '2018-01-20T18:30:18+00:00'
---

# Original Description
I am consistently getting this error when quitting the wallet (clicking **x** on window decoration or keyboard  `⌘Q`)

**monero-wallet-gui quit unexpectedly.**
Click Reopen to open the application again. Click Report
to see more detailed information and send a report to
Apple.

![monero-quit](https://cloud.githubusercontent.com/assets/5115470/25452884/6f642ca2-2ac7-11e7-93a4-23a03fa9e0c5.png)

At the moment I quit, I get these two messages in the log:
```
2017-04-26 21:38:05.475		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-04-26 21:38:05.482		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
```
Here is some info from the apple debug report:

```
Process:               monero-wallet-gui [9512]
Code Type:             X86-64 (Native)
OS Version:            Mac OS X 10.11.6 (15G1421)

Exception Type:        EXC_CRASH (SIGABRT)
Exception Codes:       0x0000000000000000, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Application Specific Information:
abort() called
*** error for object 0x7fd35b698610: pointer being freed was not allocated
```

FYI: I'm using a remote daemon.

# Discussion History
## Jaqueeee | 2017-04-26T22:18:31+00:00
Could you please change to loglevel 3 on settings page before exiting and paste the log output?

## jonathancross | 2017-05-01T01:38:19+00:00
I tried changing the log level to both 3 and 4.  Result was exactly the same as reported above, only these 2 lines in `~/.bitmonero/bitmonero.log`:
```
2017-05-01 03:32:03.311		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-01 03:32:03.313		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
```

## Jaqueeee | 2017-05-02T10:16:22+00:00
@jonathancross That's the daemon log. The wallet log is usually in monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui.log

I just noticed that the beta2 doesn't write to the log file on my OSX machine. If you don't have that file you can start gui by double clicking the (`monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui`) instead of the .app package. The  log output will be shown in a terminal window. 

You can also start it from a terminal window 
`./monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui`

Thanks for your help!


## jonathancross | 2017-05-04T16:14:01+00:00
Thanks @Jaqueeee I was not aware of that log.

I've had inconsistent results since working with that log:
1. The log file you mentioned (`monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui.log`)  did not exist.  I was seeing consistent crashes on exit every time (I'm using a version built from source).  I was running like so: `open` command from terminal and via doubleclick, no difference.
2. I decided to run the app directly from terminal as you suggested: `./monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui`
3. This caused the gui log file to be created as well as logging to terminal.
4. From this point on, I could not reproduce the crashes and have not determined what might have caused them.

Only ERROR messages in the log were these:
```
2017-05-04 18:02:46.179		ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature missmatch
2017-05-04 18:02:46.179		ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2081	!r. THROW EXCEPTION: error::invalid_password
2017-05-04 18:02:46.179		ERROR	WalletAPI	src/wallet/api/wallet.cpp:502	Error opening wallet: invalid password
2017-05-04 18:02:47.536		ERROR	WalletAPI	src/wallet/api/wallet.cpp:551	Status_Critical - not storing wallet
2017-05-04 18:03:48.095		DEBUG	WalletAPI	src/wallet/api/wallet.cpp:267	"\u001B[36m2017-05-04 18:03:48.065\t\tINFO \tglobal\tcontrib/epee/src/mlog.cpp:145\tNew log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO\n\u001B[0m\u001B[31m2017-05-04 18:03:48.066\t\tERROR\tmsgwriter\tsrc/common/scoped_message_writer.h:94\tError: Couldn't connect to daemon\n\u001B[0mError: Couldn't connect to daemon\n"
```

Deleting the `.app`, recompiling, etc had no effect (log still created, no crashing on exit).

So, I then made a fresh clone from https://github.com/jonathancross/monero-core  and recompiled.  The same crash came back on first try, but then disappeared for subsequent exits.

Sorry I haven't been able to determine anything concrete, but will keep trying...

## andersals | 2017-12-27T20:36:55+00:00
since i installed the monero gui wallet on my mbp i have serious serious system crash or better saying it shuts down my mac without even anouncing as if it gets too hot but no report or system anouncement happens  ... it happened after 3 days of syncing the blockchain and now i have this issues regularly... i try to update from el capitan to high sierra but to be honest i dont want such a gui wallet on my mac .. if this causes such a pain 

## stoffu | 2017-12-27T23:39:56+00:00
@andersals 
Wow, that crash sounds very strange and serious indeed. I also use Monero GUI on MacBookPro (2016) without any problems. To identify the cause of the problem, could you please try:

- Run `monerod` separately, and see if it already causes the heat problem
- Run GUI by connecting to a public node (see https://moneroworld.com/ for how)


## andersals | 2017-12-27T23:43:09+00:00
Monerod? I don’t know what u mean with separately / got the GUI wallet and since the blockchain sync I have serious hardware issues

Sent from ProtonMail Mobile

AN Mi., Dez. 27, 2017 bei 18:39, stoffu <notifications@github.com> Schrieb:

> [@andersals](https://github.com/andersals)
> Wow, that crash sounds very strange and serious indeed. I also use MacBookPro (2016) without any problems. To identify the cause of the problem, could you please try:
>
> - Run monerod separately, and see if it already causes the heat problem
> - Run GUI by connecting to a public node (see https://moneroworld.com/ for how)
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/696#issuecomment-354196408), or [mute the thread](https://github.com/notifications/unsubscribe-auth/AghT7wQY-x0H841je4scdGyTljYdrH8tks5tEtVOgaJpZM4NJVN6).
>
> {"api_version":"1.0","publisher":{"api_key":"05dde50f1d1a384dd78767c55493e4bb","name":"GitHub"},"entity":{"external_key":"github/monero-project/monero-gui","title":"monero-project/monero-gui","subtitle":"GitHub repository","main_image_url":"https://cloud.githubusercontent.com/assets/143418/17495839/a5054eac-5d88-11e6-95fc-7290892c7bb5.png","avatar_image_url":"https://cloud.githubusercontent.com/assets/143418/15842166/7c72db34-2c0b-11e6-9aed-b52498112777.png","action":{"name":"Open in GitHub","url":"https://github.com/monero-project/monero-gui"}},"updates":{"snippets":[{"icon":"PERSON","message":"@stoffu in #696: @andersals Wow, that crash sounds very strange and serious indeed. I also use MacBookPro (2016) without any problems. To identify the cause of the problem, could you please try: - Run `monerod` separately, and see if it already causes the heat problem - Run GUI by connecting to a public node (see https://moneroworld.com/ for how) "}],"action":{"name":"View Issue","url":"https://github.com/monero-project/monero-gui/issues/696#issuecomment-354196408"}}}

## andersals | 2017-12-27T23:47:15+00:00
But thanks for the try to help - I guess sth got real ficked up - I got my tinemaschine backup and to be honest I want to delete the GUI wallet completely with the blockchain but in the library the folder is only 50mb
I got my seed saved so maybe u can help me to get the xmr (not so much to be honest)  without starting the GUI wallet and the demon to an exchange/ I heard it would work to delete the monero wallet and u can get the coins
Best

Sent from ProtonMail Mobile

AN Mi., Dez. 27, 2017 bei 18:39, stoffu <notifications@github.com> Schrieb:

> [@andersals](https://github.com/andersals)
> Wow, that crash sounds very strange and serious indeed. I also use MacBookPro (2016) without any problems. To identify the cause of the problem, could you please try:
>
> - Run monerod separately, and see if it already causes the heat problem
> - Run GUI by connecting to a public node (see https://moneroworld.com/ for how)
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/696#issuecomment-354196408), or [mute the thread](https://github.com/notifications/unsubscribe-auth/AghT7wQY-x0H841je4scdGyTljYdrH8tks5tEtVOgaJpZM4NJVN6).
>
> {"api_version":"1.0","publisher":{"api_key":"05dde50f1d1a384dd78767c55493e4bb","name":"GitHub"},"entity":{"external_key":"github/monero-project/monero-gui","title":"monero-project/monero-gui","subtitle":"GitHub repository","main_image_url":"https://cloud.githubusercontent.com/assets/143418/17495839/a5054eac-5d88-11e6-95fc-7290892c7bb5.png","avatar_image_url":"https://cloud.githubusercontent.com/assets/143418/15842166/7c72db34-2c0b-11e6-9aed-b52498112777.png","action":{"name":"Open in GitHub","url":"https://github.com/monero-project/monero-gui"}},"updates":{"snippets":[{"icon":"PERSON","message":"@stoffu in #696: @andersals Wow, that crash sounds very strange and serious indeed. I also use MacBookPro (2016) without any problems. To identify the cause of the problem, could you please try: - Run `monerod` separately, and see if it already causes the heat problem - Run GUI by connecting to a public node (see https://moneroworld.com/ for how) "}],"action":{"name":"View Issue","url":"https://github.com/monero-project/monero-gui/issues/696#issuecomment-354196408"}}}

## stoffu | 2017-12-28T01:12:26+00:00
The app `monero-wallet-gui.app` is actually a folder (you can open it by choosing "Show Package Contents" in the right click menu) that contains a bunch of binaries (under `monero-wallet-gui.app/Contents/MacOS/`) including `monerod` which is the Monero full node daemon.

> I want to delete the GUI wallet completely with the blockchain but in the library the folder is only 50mb

The blockchain data is stored in a hidden folder `~/.bitmonero/`, so that might be what you want to get rid of.

> I got my seed saved so maybe u can help me to get the xmr (not so much to be honest)  without starting the GUI wallet and the demon to an exchange

To send your coins to anywhere, you do need to run the GUI, but you can omit running the daemon by using a remote public node. See the instruction here: https://moneroworld.com/

Or alternatively, you can use your wallet seed to log in to https://mymonero.com/. But in this case, you'd need to pay the fee of 0.1 XMR for importing all the history of transactions your wallet had previously (the fee is expensive because this process is a high load to the server).

BTW, keep in mind that sending your money to an exchange can potentially mean that you give up your money; since the secret key is held by not you but them, they can do whatever with your deposit (e.g. exit scam, get hacked, etc). If you're serious about your money, it's best to run the wallet software by yourself.


## jonathancross | 2018-01-20T18:30:18+00:00
I am no longer seeing this issue on the latest v0.11.1.0 version.
@andersals: I don't think your issue is related to my crash so I'll close this specific bug report.
Feel free to open a new issue with specifics of your crash if needed.

# Action History
- Created by: jonathancross | 2017-04-26T19:41:02+00:00
- Closed at: 2018-01-20T18:30:18+00:00
