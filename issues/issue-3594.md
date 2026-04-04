---
title: GUI doesn't properly shutdown, has to be killed from task manager (Windows)
source_url: https://github.com/monero-project/monero-gui/issues/3594
author: MoneroArbo
assignees: []
labels:
- bug
created_at: '2021-06-28T19:42:31+00:00'
updated_at: '2022-04-11T22:47:31+00:00'
type: issue
status: closed
closed_at: '2022-04-11T22:47:30+00:00'
---

# Original Description
Version 0.17.2.2

Starting (I think) in this release, I have had to force close Monero GUI from the task manager because it does not shut itself down, even after a long time. When I click the 'X' button to close the wallet, it says 'closing wallet' and gets stuck there. If I click 'X' again, the Window will close but the process continues to run in the background.

monero-wallet-gui.log appears to contain nothing useful.

# Discussion History
## selsta | 2021-06-28T19:43:43+00:00
Which wallet mode?

## selsta | 2021-06-28T19:44:34+00:00
> When I click the 'X' button to close the wallet, it says 'closing wallet' and gets stuck there.

How long did you wait?

## MoneroArbo | 2021-06-28T20:11:32+00:00
Advanced mode, connected to a node on my LAN. Also running in low graphics mode.

I've noticed the process running in the background after hitting X twice even after 12+ hours. As for when I only hit it once, leaving the window up, I'm not sure exactly. I know I've let it go for awhile before. Tested just now and it was still spinning after 5 minutes.

## selsta | 2021-06-28T20:13:45+00:00
Okay, but on Settings -> Node you have remote node selected?

## MoneroArbo | 2021-06-28T20:27:21+00:00
Yes.

Also, this could be a different issue, but I'm noticing that the wallet gets stuck on 'wallet blocks remaining: 0' for several minutes, even though the 2kish blocks it scanned before that went in about 2 seconds. This issue happens even if I wait for that to go away though, so maybe it needs a different bug report.

Additional info: Closing the wallet by clicking 'Close this wallet' in the settings displays the same issue.

Both of these issues also happen if I connect to the node at node.xmr.to instead of my local node.

**edit:** Also, it happens almost every time, but not *every* time. I was able to close the wallet with no issues just now, while connected to my local node. Don't think I did anything differently.

## selsta | 2021-06-28T20:33:00+00:00
Hmm, nothing was changed in v0.17.2.2 that would be remotely related to your issues.

> Also, it happens almost every time, but not every time. I was able to close the wallet with no issues just now, while connected to my local node. Don't think I did anything differently.

Does it trigger 100% if you have remote node selected?

## MoneroArbo | 2021-06-28T20:37:01+00:00
To clarify, I have not tried it with a truly local node. The node on my LAN is on a different host.

And I'm not 100% sure it just started in this version, but I've definitely been noticing it more recently. Fwiw other apps including Feather wallet don't do anything like this.

## selsta | 2021-07-13T22:18:17+00:00
Will check what Feather does differently on wallet exit.

## mac671 | 2021-07-22T17:01:29+00:00
What I noticed is that:
When I press close.
I have a selection if I want to keep the monerod alive or force kill.
The force kill works, but then the application is stuck forever in closing GUI state.

![image](https://user-images.githubusercontent.com/8583249/126678932-580ec9cf-abfd-4d86-844e-70f9dcca558e.png)

Mode: Advanced.
Node : Same machine as the wallet.

I am also experiencing a sync issue, but perhaps that one is not related to the gui not closing.
https://monero.stackexchange.com/questions/13199/monero-gui-wallet-stuck-after-blockchain-sync-succeeded



## selsta | 2021-07-22T17:05:12+00:00
@mac671 responded on SE

## mac671 | 2021-07-22T18:05:56+00:00
> @mac671 responded on SE

The GUI closes correctly now. After I exported the view key from my Ledger S, the wallet synchronized. And the GUI application is now properly closing and shutting down.

## ybop | 2021-11-05T09:49:27+00:00
I am having the same problem.  Connecting to remote node.  It will shutdown ok unless I leave it running for 10 minutes or so, after which it gets stuck forever in the closing GUI state.

Same issue occurs in GUI v0.17.2.0 and also with a new wallet file.

Shuts down fine if it only run for a few minutes.  But if I leave it running for 10 minutes or so it doesn't.

## selsta | 2021-11-05T19:18:40+00:00
I have been able to reproduce this issue now.

## nikbikthesly | 2021-11-30T23:32:11+00:00
I also have to force quit the gui on Mac

## selsta | 2021-11-30T23:33:32+00:00
@nikhildaniels every single time?

## nikbikthesly | 2021-12-01T02:50:28+00:00
Yes when I click "Close this wallet and return to main menu" in the top left it gets stuck.

## uFire | 2021-12-01T21:35:51+00:00
I have the same issue as all above but also in addition if I keep GUI running for some long time (30 mins or more) it become almost impossible to create a new transaction. I paste an address, type amount to send and the wheel next to "Transaction priority" keep spinning for a long time, sometimes infinite. When I anyways click the "Send" button, the window "Creating transaction" also keep without any buttons for a long time saying "Calculating fee...", sometimes infinite. So as a workaround I am forced to kill the monero process and start it over every time.

I thought that it is possible that my PC have some glitches so I tried running MoneroGUI on the brand new laptop - same result.

Windows 10 Pro
Monero GUI 0.17.2.3-113efbf (Qt 5.15.2), advanced mode - not installed but unpacked from monero-gui-win-x64-v0.17.2.3.zip

Running remote node on my home LAN CentOS7 server - unpacked and run original monero-linux-x64-v0.17.2.3.tar.bz2 with config file:

```
data-dir=/home/imuser/.bitmonero
log-file=/home/imuser/.bitmonero/monerod.log
max-log-file-size=0
p2p-bind-ip=0.0.0.0
p2p-bind-port=18080
rpc-bind-ip=0.0.0.0
rpc-bind-port=18081
confirm-external-bind=1
restricted-rpc=0
no-igd=1
rpc-login=myusername:mypassword
db-sync-mode=safe
enforce-dns-checkpointing=1
out-peers=64
in-peers=1024
limit-rate-down=1048576
```





## selsta | 2021-12-01T21:46:36+00:00
@uFire can you try a different node, for example mine:

88.198.199.23:18081

>if I keep GUI running for some long time (30 mins or more) it become almost impossible to create a new transaction

Do you still have this issue?

I want to figure out first if it's a daemon or if it's a wallet issue on your side.

## uFire | 2021-12-01T21:50:07+00:00
@selsta ok give me some time. Will change the node to 88.198.199.23:18081 right now and make some transactions during the next hour. 

## uFire | 2021-12-01T23:39:45+00:00
@selsta  Ok. I've done some tests. During the one hour since I switched to the node you suggested I made a dozen of transactions and everything went fast and smooth. Everything were working lightning fast.

Then I switched back to to my local node and all problems started again. With my node even changing transaction priority takes 20 to 100 seconds and even longer. 

Then I switched to my one more local node I set up and synchronized two days ago - all the issues stay in place. This  node is running on freshly installed Debian 11. The monero node compiled from source from master branch five days ago.

Both of my home servers, CentOS 7 and Debian 11, have firewall disabled so this can't be the reason. What makes those nodes similar is that both of them use similar config I posted above, both of them has RPC password enabled - so, maybe there some issues with password protected RPC connection to the remote nodes? 

Also, I captured some logs with action timemarks while reproducing those delays with TX priority changing but don't want to post them here. How can I send them to you?

## uFire | 2021-12-02T00:30:40+00:00
@selsta Also, when the wallet stuck at "Closing wallet..." screen, the log getting full of the following:

```
2021-12-02 00:27:00.412	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2222	refreshThreadFunc: refresh lock acquired...
2021-12-02 00:27:00.412	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2223	refreshThreadFunc: m_refreshEnabled: 0
2021-12-02 00:27:00.412	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2224	refreshThreadFunc: m_status: 0
2021-12-02 00:27:00.412	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2225	refreshThreadFunc: m_refreshShouldRescan: 0
2021-12-02 00:27:00.412	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2212	refreshThreadFunc: waiting for refresh...
2021-12-02 00:27:10.420	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2222	refreshThreadFunc: refresh lock acquired...
2021-12-02 00:27:10.420	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2223	refreshThreadFunc: m_refreshEnabled: 0
2021-12-02 00:27:10.420	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2224	refreshThreadFunc: m_status: 0
2021-12-02 00:27:10.420	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2225	refreshThreadFunc: m_refreshShouldRescan: 0
2021-12-02 00:27:10.420	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2212	refreshThreadFunc: waiting for refresh...
2021-12-02 00:27:20.428	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2222	refreshThreadFunc: refresh lock acquired...
2021-12-02 00:27:20.428	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2223	refreshThreadFunc: m_refreshEnabled: 0
2021-12-02 00:27:20.428	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2224	refreshThreadFunc: m_status: 0
2021-12-02 00:27:20.428	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2225	refreshThreadFunc: m_refreshShouldRescan: 0
2021-12-02 00:27:20.428	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2212	refreshThreadFunc: waiting for refresh...
2021-12-02 00:27:30.429	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2222	refreshThreadFunc: refresh lock acquired...
2021-12-02 00:27:30.429	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2223	refreshThreadFunc: m_refreshEnabled: 0
2021-12-02 00:27:30.429	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2224	refreshThreadFunc: m_status: 0
2021-12-02 00:27:30.429	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2225	refreshThreadFunc: m_refreshShouldRescan: 0
2021-12-02 00:27:30.429	16224	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2212	refreshThreadFunc: waiting for refresh...

```

## selsta | 2021-12-02T00:33:41+00:00
Do you have this issue with wallet getting stuck on "Closing wallet..." when using my node too? It seems it waits for the refresh to finish but the node doesn't reply correctly. How long did you wait?

## uFire | 2021-12-02T00:35:58+00:00
> Do you have this issue with wallet getting stuck on "Closing wallet..." when using my node too? It seems it waits for the refresh to finish but the node doesn't reply correctly. How long did you wait?

Testing this right now. Give me 15 mins.

## uFire | 2021-12-02T00:51:59+00:00
@selsta Looks like there is no exit issue when using your node. But to be sure I have to give it a long test, at least for an hour.

## MoneroArbo | 2021-12-02T01:11:53+00:00
@selsta I can confirm that I still have the "not closing" issue when using the node you specified. Seems like there may be different causes at play.

To others having this issue, I've been able to work around it by running monero-gui in portable mode. Not sure what the equivalent for OS X is, but on Windows if you've already initiated non-portable mode, you can get the GUI to re-initialize and give you the option for portable mode by deleting the registry entry at:

`Computer\HKEY_CURRENT_USER\SOFTWARE\monero-project`

Close the GUI, delete this key in regedit.exe, then start it again and select portable mode. Let us know if this does or doesn't work for you.

## selsta | 2021-12-02T01:13:16+00:00
> I can confirm that I still have the "not closing" issue when using the node you specified. Seems like there may be different causes at play.

Yes, two different issues

## uFire | 2021-12-02T03:10:18+00:00
@MoneroArbo I am a bit confused regarding "portable" mode. For example, I didn't installed my Monero GUI via Windows installer but obtained a zipped version from getmonero website, unpacked and use that way. And I don't remember any dialogue asking me which mode I prefer it to be, but I do have the registry entry you mentioned. I intended to use it without installation so got a zipped version and I am surprised it created its entry at the registry. I thought I already using portable version. Then why did he create registry entries?

Also, after two hours of running it with selsta's node, making transactions, turning it on and off I had no even a single "not closing" issue nor any delays. It just works. Will try running it with that node for the whole day tomorrow to get solid results.

Tried switching to both my local nodes with password protected RPC and all problems came back. Damn! I think I need to get some sleep, because it's already five in the morning here in Ukraine ))

UPD: My bad. I have removed the reg entry and there IS a portable mode checkbox. Will play with it tomorrow.


## uFire | 2021-12-02T21:45:45+00:00
Well, the "not closing" issue and fee calculation problems still persist. 

I have reset it to the portable mode, connected to my wallet, connected to selsta's node, disabled wallet locking on timeout, made a few transactions (everything went just fine) and left it for 15 hours in that state. I have tried creating a transaction just now and got an infinite spinning wheel in place of fee value (been waiting for 20 minutes). When I tried to close the wallet by clicking in the top left corner, it changed to the "Closing wallet..." screen and didn't exited for more than an hour, and then I killed the process. The daemon height displayed actual value so it were connected to the node.

## selsta | 2021-12-02T21:51:20+00:00
@uFire Portable mode is unrelated to your issue.

## selsta | 2022-04-11T22:47:30+00:00
Continuing in #3840

# Action History
- Created by: MoneroArbo | 2021-06-28T19:42:31+00:00
- Closed at: 2022-04-11T22:47:30+00:00
