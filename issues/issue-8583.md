---
title: wrong version
source_url: https://github.com/monero-project/monero/issues/8583
author: budmaster13
assignees: []
labels: []
created_at: '2022-09-21T19:03:07+00:00'
updated_at: '2022-11-03T14:34:18+00:00'
type: issue
status: closed
closed_at: '2022-09-26T23:28:12+00:00'
---

# Original Description
Daemon wont connect to GUI says using wrong version but i have latest version GUI version: 0.18.1.1-unknown (Qt 5.15.6)
Embedded Monero version: 0.18.1.1-unknown
Wallet path: /home//Monero/wallets
Wallet restore height: 2686804
Wallet log path: /home/.bitmonero/monero-wallet-gui.log
Wallet mode: Simple mode (bootstrap)
Graphics mode: OpenGL
I have used this wallet several times after fork with no issues. Now its saying im using wrong version.

# Discussion History
## selsta | 2022-09-21T19:04:57+00:00
Can you go to Settings -> Log and post the output of "status" ?

## selsta | 2022-09-21T19:07:16+00:00
Simple mode connects to a random remote node. If you connect to a remote node that is outdated (using v0.17) it will now say "wrong version". If you wait a bit it _should_ connect to a new node.

## budmaster13 | 2022-09-21T19:10:53+00:00
it wont let me drag and drop it here

## selsta | 2022-09-21T19:11:28+00:00
You should be able to copy paste it.

## budmaster13 | 2022-09-21T19:13:19+00:00
yea tried that as well. Said something went wrong and it wouldnt let me.

## selsta | 2022-09-21T19:13:59+00:00
Can you make a screenshot? Or is that what failed? Then copy paste the text.

## budmaster13 | 2022-09-21T19:17:58+00:00
Sent from Proton Mail mobile

https://www.reddit.com/r/Monero/comments/xk9ayu/monero_gui_problems/ipd4zr4?utm_medium=android_app&utm_source=share&context=3 I wrote down the status output in this reddit thread
-------- Original Message --------
On Sep 21, 2022, 3:14 PM, selsta wrote:

> Can you make a screenshot?
>
> —
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero/issues/8583#issuecomment-1254122098), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AMVPQWTV64MSOJ2H7KGEYKTV7NNAFANCNFSM6AAAAAAQSLOIIM).
> You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2022-09-21T19:19:42+00:00
It seems your daemon fails to start for some reason. Can you just set a custom remote node instead? I can give you instructions for it.

## budmaster13 | 2022-09-21T19:29:39+00:00
Its a bootstrap simple wallet. The blockchain is downloaded to my hard drive. Even when i just try to connect to remote node same problem i have with local node. Wrong version

## selsta | 2022-09-21T19:30:41+00:00
Which remote node did you connect to? And did you switch to advanced mode for that?

## budmaster13 | 2022-09-21T19:32:54+00:00
No i hit the icon in bottom left corner where it says switch to another public node when you hover your curser over it.

## budmaster13 | 2022-09-21T19:35:18+00:00
Here is a picture of wallet

Sent from Proton Mail mobile

-------- Original Message --------
On Sep 21, 2022, 3:30 PM, selsta wrote:

> Which remote node did you connect to? And did you switch to advanced mode for that?
>
> —
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero/issues/8583#issuecomment-1254138384), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AMVPQWTSNGRLUIMKJW2HCLTV7NO6XANCNFSM6AAAAAAQSLOIIM).
> You are receiving this because you authored the thread.Message ID: ***@***.***>

## budmaster13 | 2022-09-21T19:35:37+00:00
I sent you a picture with status on my cell phone to your email


## selsta | 2022-09-21T19:35:43+00:00
The easiest way to get things working is to follow the steps in this comment to connect to a remote node: https://github.com/monero-project/monero-gui/issues/3989#issuecomment-1214412781

## budmaster13 | 2022-09-21T19:37:08+00:00
How about my local node on my computer will i be able to use that?

## budmaster13 | 2022-09-21T19:38:27+00:00
I mean thats why i downloaded the blckchain on my hard drive

## selsta | 2022-09-21T19:39:08+00:00
You can try to select Local Node and then press "Start Daemon".

## ch9PcB | 2022-09-22T10:29:06+00:00
I, too, experienced the same problem of wrong version.

My Linux distro is Debian 11.5.0 (64-bit) and I downloaded the latest version using the following link: https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.1.1.tar.bz2

I verified the hash of it using a GPG-signed list of hashes using the below link:

https://www.getmonero.org/downloads/hashes.txt

Next, I extracted the contents of monero-gui-linux-x64-v0.18.1.1.tar.bz2 to the /home directory.

I launched it and typed in my password to the wallet.

After a few seconds I received an error message at the top of the Monero GUI screen. It stated:

`Connected daemon is not compatible with GUI. Please upgrade or connect to another daemon.`

A few seconds later, two words **Wrong version** appeared under **Network status** in the bottom left corner of Monero GUI.

In the Daemon Log these were the details:

```
[9/21/22 10:06 PM] 2022-09-21 22:06:51.663 I Monero 'Fluorine Fermi' (v0.18.1.1-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[9/21/22 10:07 PM] 2022-09-21 22:07:21.311 I Monero 'Fluorine Fermi' (v0.18.1.1-release)
Height: 2717051, target: 2717051 (100%)
Downloading at 0 kB/s
Next needed pruning seed: 8
1 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
188.40.127.121:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
```

I tried to disconnect it by going to **Settings** --> **Node** and clicking the orange button **Stop daemon**.  Monero GUI refused to disconnect despite me clicking on **Stop daemon** many times. In the end, I had to click the **X** at the top right-hand corner of the GUI and then the grey button **Force stop** at least two times. Only then the _stubborn_ Fluroine Fermi 0.18.1.1 exited/closed down.

I deleted the un-zipped monero-gui-linux-x64-v0.18.1.1.tar.bz2 and rebooted my machine.

I repeated the process of un-zipping monero-gui-linux-x64-v0.18.1.1.tar.bz2 to the /home directory and launching Monero GUI.

The same error occurred.

What happened next was I exited/closed down the _stubborn_ Monero GUI, deleted the un-zipped monero-gui-linux-x64-v0.18.1.1.tar.bz2 and rebooted my machine.

Fortunately I had not deleted the previous version. I un-zipped monero-gui-linux-x64-v0.18.1.0.tar.bz2 to the /home directory and launched it after typing the password.

This time, there were two error mesages (white text, black background) near the bottom of Monero GUI. They were:

```
Reverting to 0.18.1.0
Repairing incompatible wallet cache. Resyncing wallet.
```

I hope that @selsta will find a solution to the bug soon. Meanwhile I will stick to the not-stubborn v0.18.1.0 version.

Note: I have been using Monero GUI on Debian for more than two years now and never encountered such a serious bug before.

## selsta | 2022-09-22T10:36:05+00:00
We added a check that detects outdated nodes and wallets since a lot of people were connecting to outdated nodes, unfortunately due to a bug this breaks the daemon auto start / stop mechanic inside the GUI. We have a fix already and should have a new version out within the next days. In the meantime these are methods to work around it:

- Manually start the daemon from the Terminal or file explorer, it should quickly connect and the "wrong version" message disappears. If you have a custom blockchain location you can use the `--data-dir` flag.
- Connect to a remote node temporarily until we release v0.18.1.2 (Instructions here https://github.com/monero-project/monero-gui/issues/3989#issuecomment-1214412781)
- Downgrade to v0.18.1.0: https://github.com/monero-project/monero-gui/releases/tag/v0.18.1.0 (Only do this if the other two options are not possible, since this can cause a wallet rescan)


Edit: After doing more testing, the start / stop mechanic doesn't seem broken. Simple mode also seems to work for me. There's still the issue with "wrong version" showing up instead of "disconnected", but otherwise things seem to work here.

## ch9PcB | 2022-09-22T11:06:14+00:00
@selsta 

Thank you for suggesting 3 workarounds but it's too late for me because I have reverted to using v0.18.1.0.

Yes, there was a wallet rescan when I reverted to using v0.18.1.0 but the rescan didn't take much of my time. In any case, the rescan didn't corrupt data.mdb which is now 50.5GB (pruned).

## budmaster13 | 2022-09-22T13:38:27+00:00
Actually I fixed this problem by uninstalling the monero GUI on my computer. Then sending wallet file to trash. Then I reinstalled the wallet GUI and restoring wallet file from trash folder. It worked perfectly and I was able to use local node stored on my hard-drive.

Sent from Proton Mail mobile

-------- Original Message --------
On Sep 22, 2022, 7:06 AM, ch9PcB wrote:

> ***@***.***(https://github.com/selsta)
>
> Thank you for suggesting 3 workarounds but it's too late for me because I have reverted to using v0.18.1.0.
>
> Yes, there was a wallet rescan when I reverted to using v0.18.1.0 but the rescan didn't take much of my time. In any case, the rescan didn't corrupt data.mdb which is now 50.5GB (pruned).
>
> —
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero/issues/8583#issuecomment-1254870748), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AMVPQWQSIGSRKI643SB4FVLV7Q4TFANCNFSM6AAAAAAQSLOIIM).
> You are receiving this because you authored the thread.Message ID: ***@***.***>

## ch9PcB | 2022-09-22T17:48:01+00:00
@budmaster13 

> Then I reinstalled the wallet GUI

You used the installer, monero-gui-install-win-x64-v0.18.1.1.exe, is that correct?


## selsta | 2022-09-22T18:00:01+00:00
I doubt reinstalling helps here.

## ch9PcB | 2022-09-22T19:43:18+00:00
@selsta 

> I doubt reinstalling helps here.

Totally agree with you. You ARE one of the developers of this software. How can @budmaster13 be able to fix things better than you?

I noticed the post where you asked him to go to Settings --> Log and post the output of "status" and he gave many excuses.

Moreover, he didn't tell you the operating system he used.

He also referred to his post at Reddit/r/Monero titled [Monero GUI problems](https://www.reddit.com/r/Monero/comments/xk9ayu/monero_gui_problems/) in which he gave next to nothing feedback on the status.

## selsta | 2022-09-22T19:52:33+00:00
No status output makes sense when the daemon isn't started, which is happening with v0.18.1.1

## bf215181b5140522 | 2022-09-22T20:26:48+00:00
First off I'd like to thank the developers for the quick response on this, but I feel that it does beg the question as to what sort of testing is done before releases. I'm curious how a bug as conspicuous as this can make it into a final release version without being noticed a single time. Does this particular bug in gui v0.18.1.1 affect everyone trying to use a local daemon on all platforms?

## selsta | 2022-09-22T20:41:00+00:00
It does not affect using a local node directly, it affects the start / stop mechanic. If someone starts the daemon manually everything works fine.

The bug was an uninitialized variable in one part of the code (that unfortunately the compiler didn't warn about) that causes a bug somewhere completely else. I did do testing, but it was in remote node mode, so I didn't see the broken start / stop mechanic.

I personally don't have the resources to test every GUI feature before every release.

Edit: To add to this, I always start my daemon manually since I use master branch, which again caused that I didn't see the bug.

## ch9PcB | 2022-09-22T20:48:09+00:00
@selsta 

> No status output makes sense when the daemon isn't started, which is happening with v0.18.1.1

How was it that I was able to provide a Daemon Log?

>I personally don't have the resources to test every GUI feature before every release.

I understand that you are contributing your own time and resources to this project. Any bug -big and smal- don't faze me. I wish to take this opportunity to thank you for your hard work.

## selsta | 2022-09-22T20:58:19+00:00
@ch9PcB I'm don't know, could have been a timing thing where the daemon started before it got into the buggy wrong version mode.

## ki9us | 2022-09-22T22:38:27+00:00
I'm getting the same invalid version error, using my own node.  

Remote node version: 
```
$ monerod --version
Monero 'Fluorine Fermi' (v0.18.1.1-release)
```
That's running on debian and was installed from source 2 days ago.  

Local GUI verison: 
![image](https://user-images.githubusercontent.com/10123447/191862172-03e9977f-60f6-4003-9a1b-eb1618f9928f.png)

That's running on Arch and was installed with `pacman -S monero-gui` today.  

The "Type a command box" in the GUI's `Settings | Log` section is disabled, but I got this from `~/.bitmonero/monero-wallet-gui.log`:

```
2022-09-22 22:30:03.840	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
2022-09-22 22:30:03.840	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] monero-wallet-gui(+0x10fb0f) [0x555859611b0f] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] monero-wallet-gui(+0x20262a) [0x55585970462a] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] monero-wallet-gui(+0x203655) [0x555859705655] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] monero-wallet-gui(+0x22b9e0) [0x55585972d9e0] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] monero-wallet-gui(+0x5b6bb7) [0x555859ab8bb7] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] monero-wallet-gui(+0x2c5776) [0x5558597c7776] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] monero-wallet-gui(+0x2c9d5d) [0x5558597cbd5d] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] monero-wallet-gui(+0x2b47b6) [0x5558597b67b6] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] monero-wallet-gui(+0x2543c7) [0x5558597563c7] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] monero-wallet-gui(+0x254560) [0x555859756560] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] monero-wallet-gui(+0x266a06) [0x555859768a06] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /usr/lib/libQt5Core.so.5(+0xe8491) [0x7f3cff0e8491] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /usr/lib/libQt5Core.so.5(+0xe42ba) [0x7f3cff0e42ba] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] /usr/lib/libc.so.6(+0x8674d) [0x7f3cfe29f74d] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] /usr/lib/libc.so.6(+0x108700) [0x7f3cfe321700] 
2022-09-22 22:30:03.841	    7f3cf9e2f6c0	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

Uninstalling and re-installing the GUI with `sudo pacman -R monero-gui && sudo pacman -S monero-gui` didn't solve the problem for me.  Restarting the daemon and GUI didn't fix it either.  

`boost::system::system_error` is kinda vague so... good luck!  

## selsta | 2022-09-23T01:28:52+00:00
@ki9us So you are using Advanced mode (remote node)? Can you try to connect to one of these

- address: selsta1.featherwallet.net port: 18081
- address: selsta2.featherwallet.net port: 18081

to make sure it is not a network issue with the node you have?

## ki9us | 2022-09-23T12:39:44+00:00
That worked!  

It was my fault: port 18081 was closed.  Well it was unblocked but `monerod` was listening on `127.0.0.1` instead of `0.0.0.0`.  Fixed by adding ` --rpc-bind-ip=0.0.0.0  --confirm-external-bind` to my `monerod` command.  

So for me it just was a matter of a misleading error.  

BTW do you know how to set this for ipv6?  I tried `--rpc-bind-ipv6-address=::`, `--rpc-bind-ipv6-address ::`, `--rpc-bind-ipv6-address=[::]`, `--rpc-bind-ipv6-address=::`, and `--rpc-bind-ipv6-address ::0`  but none of those got it listening on IPv6.  

## j-berman | 2022-09-24T18:45:38+00:00
This "Wrong version" bug impacts people using v0.18.1.1 in the following ways:

1. On some systems, simple bootstrap mode doesn't auto-start a daemon and gets stuck with "Wrong version".
2. In other modes, like normal simple mode, the "Wrong version" status can sometimes appear confusingly. Leaving the GUI open *should* rectify it, but clicking "Stop daemon" while it's in that status can cause janky behavior.
3. In advanced mode or in the CLI wallet, setting the daemon to either a non-existent daemon or to an offline daemon (i.e. failing to connect to the daemon) can result in the "Wrong version" status.

All the above should be fixed in the next release. The code is [here](https://github.com/monero-project/monero/pull/8585) and [here](https://github.com/monero-project/monero-gui/pull/4036) available for testing. Personally I was extremely thorough in my GUI tests this time around and will be more thorough in testing the GUI in the future.

> what sort of testing is done before releases. I'm curious how a bug as conspicuous as this can make it into a final release version without being noticed a single time.

This was a valid question.

First of all I wrote the code. The mistake originated with me. I take responsibility for this.

I tested every code path I wrote and tested every possible daemon configuration pointing my CLI wallet to:
- my own local daemon running the latest version
- my own local daemon running a pre-fork version
- my own local daemon running modified code of a hypothetical future fork
- a non-existent node
- a node with an incorrect port set
- a remote node running the latest
- a remote node running pre-fork code
- all the above but with my wallet running a pre-fork version 
- all the above but my wallet running a modified code of a hypothetical future fork

There were additional combinations and permutations I tested making sure to hit all pieces of the code I impacted in the CLI wallet, but this should give you an idea of the testing I did. I also ran tests with the GUI and RPC wallet myself, but was not as extensive in those tests. Everything I did test worked as expected, and I spent a solid number of hours testing.

As @selsta said, the primary bug was an uninitialized variable. Here it was:

```
bool wallet_is_outdated, daemon_is_outdated = false;
```

Since `wallet_is_outdated` is not initialized there with false, it can either turn up true or false, the behavior is undefined. So if a wallet fails to connect to a daemon for whatever reason (which the GUI's auto-start does by default), and then the boolean turns up true, the "Wrong version" status would display. On my system, unfortunately the uninitialized variable always seems to read as `false` by default but that is not the case on other systems (e.g. I can only repro [this comment here](https://github.com/monero-project/monero/pull/8544#discussion_r974825557) by starting the wallet and then firing multiple `set_daemon` commands in a row). Usually the compiler warns about reading uninitialized variables, but the way the variable is used in the code unfortunately doesn't get the compiler to do so (also seems like a bug in the compiler, not sure; regardless, in the future I will be much more careful both when initializing variables myself, and will look out for this in code review. This was my original mistake.).

@selsta is always on top of and helpful in testing; various community members step up to help testing all the time as well. In an ideal world, all Monero wallets would have dedicated QA testers on each release who test all features and bug fixes on different systems before every release.



## ch9PcB | 2022-09-25T16:43:21+00:00
@j-berman 

> First of all I wrote the code. The mistake originated with me. I take responsibility for this.

Hello Justin

We don't blame you or ask that you admit your responsiblity for any errors that have happened or will ever happen to the code that you wrote and will write in the future.

We acknowledge that you are volunteering your spare time and limited resources to this project of your own free will.

We thank you that, in spite of your work and family commitments, you decide to advance this project along.

## selsta | 2022-09-26T23:28:12+00:00
Fix has been merged, will be included in v0.18.1.2

## selsta | 2022-09-30T18:24:57+00:00
v0.18.1.2 is out https://www.getmonero.org/downloads/

## budmaster13 | 2022-10-11T07:49:56+00:00
It's a simple mode with fullnode bootstrap

Sent from Proton Mail mobile

-------- Original Message --------
On Sep 21, 2022, 3:07 PM, selsta wrote:

> Simple mode connects to a random remote node. If you connect to a remote node that is outdated (using v0.17) it will now say "wrong version". If you wait a bit it should connect to a new node.
>
> —
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero/issues/8583#issuecomment-1254115196), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AMVPQWSZ4AG5TSG6NUQ6M73V7NMG7ANCNFSM6AAAAAAQSLOIIM).
> You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2022-10-11T14:37:15+00:00
@budmaster13 make sure to update to v9.18.1.2

## bitflorist | 2022-11-03T12:14:31+00:00
still doesn't work on Mac.
[03.11.22 13:14] 2022-11-03 12:14:20.765 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

## selsta | 2022-11-03T14:34:18+00:00
@bitflorist You have to explain what you are trying to do and what exactly doesn't work.

Also post which wallet mode you are using in Settings -> Info.

# Action History
- Created by: budmaster13 | 2022-09-21T19:03:07+00:00
- Closed at: 2022-09-26T23:28:12+00:00
