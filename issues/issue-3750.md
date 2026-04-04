---
title: Problem with remote node (no connection to daemon)
source_url: https://github.com/monero-project/monero/issues/3750
author: AJIekceu4
assignees: []
labels: []
created_at: '2018-05-03T18:38:32+00:00'
updated_at: '2022-03-16T10:37:06+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:16:59+00:00'
---

# Original Description
Hello all. I am run remote node (node.xmr.ru:13666) Monero 'Lithium Luna' (v0.12.0.0-master-8361d60a). 
`Height: 1564863/1564863 (100.0%) on mainnet, not mining, net hash 489.36 MH/s, v7, up to date, 48(out)+11(in) connections, uptime 33d 1h 37m 59s`
According to netstat at this moment there are 50 simultaneous connections (RPC) from 45 different IP addresses. So, 45 people use this node. 
Now, when i try to make transaction (using this remote node), i got this error from my cli 'Lithium Luna' (v0.12.0.0-master-release):

> transfer 45ttEikQEZWN1m7VxaVN9rjQkpSdmpGZ82GwUps66neQ1PqbQMno4wMY8F5jiDt2GoHzCtMwa7PDPJUJYb1GYrMP4CwAwNp 0.1 8d3526aed9a09a943788496751c78c8f4757e7f6f3234a547efe77f3c9c6cc4b
Wallet password: 
Error: no connection to daemon. Please make sure daemon is running.
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a tranasction immediately. Alternatively, connect to another node so the original node cannot correlate information.

And i have information from few users who have same problem using this remote node. This problem revealed first time - today. So i can not make transaction, BUT i can refresh balance and no problem with this:

> [wallet 437bla]: transfer 45ttEikQEZWN1m7VxaVN9rjQkpSdmpGZ82GwUps66neQ1PqbQMno4wMY8F5jiDt2GoHzCtMwa7PDPJUJYb1GYrMP4CwAwNp 0.1 8d3526aed9a09a943788496751c78c8f4757e7f6f3234a547efe77f3c9c6cc4b
Wallet password: 
Error: no connection to daemon. Please make sure daemon is running.
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a tranasction immediately. Alternatively, connect to another node so the original node cannot correlate information.
[wallet 437bla]: transfer 45ttEikQEZWN1m7VxaVN9rjQkpSdmpGZ82GwUps66neQ1PqbQMno4wMY8F5jiDt2GoHzCtMwa7PDPJUJYb1GYrMP4CwAwNp 0.1 8d3526aed9a09a943788496751c78c8f4757e7f6f3234a547efe77f3c9c6cc4b
Wallet password: 
Error: no connection to daemon. Please make sure daemon is running.
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a tranasction immediately. Alternatively, connect to another node so the original node cannot correlate information.
[wallet 437bla]: transfer 45ttEikQEZWN1m7VxaVN9rjQkpSdmpGZ82GwUps66neQ1PqbQMno4wMY8F5jiDt2GoHzCtMwa7PDPJUJYb1GYrMP4CwAwNp 0.1 8d3526aed9a09a943788496751c78c8f4757e7f6f3234a547efe77f3c9c6cc4b
Wallet password: 
Error: no connection to daemon. Please make sure daemon is running.
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a tranasction immediately. Alternatively, connect to another node so the original node cannot correlate information.
[wallet 437bla]: refresh
Starting refresh...
Refresh done, blocks received: 3                                
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: xxx, unlocked balance: xxx

After node restart - same problem (but number of RPC clients is about 30). After 10 minutes - problem is gone and my cli wallet can make transaction with no error message. And after 5 minutes after this - i get same error again.



# Discussion History
## AJIekceu4 | 2018-05-03T20:01:31+00:00
Now i am testing last version of monerod (compiled from source today). 

## littleblackfish | 2018-05-04T04:50:24+00:00
I am having the same issue with a local daemon. 

## moneromooo-monero | 2018-05-04T10:53:41+00:00
Probably 1834127c820dcfeaa3d6f229c4e24b33d85eda7e

Try current code.

## littleblackfish | 2018-05-04T16:49:45+00:00
Can reproduce it with a fresh build from git. Issue was resolved after several reboots and daemon restarts, but came back again now. I can not get to the tx confirmation stage 49 times out of 50 tries.  
Log level 0 or 1 does not seem to have anything interesting. 

## AJIekceu4 | 2018-05-04T17:07:21+00:00
I don't see this problem in new version (compiled yesterday). Nobody complains about this problem (who used my node). I will test it few more days/week just to be sure.

## moneromooo-monero | 2018-05-04T18:50:31+00:00
What commit hash are you running littleblackfish ? I assume you're running the same for monerod and monero-wallet-cli, say if not.


## littleblackfish | 2018-05-04T19:14:31+00:00
6b9d9f56a1c7405a68ab5871d7db02e9d98836d5 as built from AUR with [monero-git pkgbuild](https://aur.archlinux.org/packages/monero-git). 

I have tried all combinations of the (12.0.0 release binary, git) x (daemon, wallet), to no persistent result. Whatever combination ended up working once, I could not reproduce next time I tried it. Furthermore, the release version have been working just fine until recently, although I don't attempt transfers that often. 

I know this is not much help but I spent a good chunk of yesterday trying to do a single transfer to no avail. I don't mind but I suspect this would be very disheartening to a less adventurous user. I'm surprised and somewhat relieved that nobody else is having the same issue. 

## moneromooo-monero | 2018-05-04T23:05:13+00:00
Run wallet with --log-level 2, and daemon with --log-level 1,perf:DEBUG

Then please post the last dozen lines of each log.


## littleblackfish | 2018-05-05T17:01:13+00:00
Actually, I can't reproduce this anymore. Believe me I tried. 10/10 transfer attempts went to the confirmation stage. Using both 12.0 release binary and git version. Poof! The issue went away. 
I'll make sure to capture logs next time I hit this.

## tailswim | 2018-05-15T20:18:15+00:00
Okay, I'm having this same problem repeatedly. I haven't been able to send a transaction for the last couple weeks and have tried all sorts of things. 

System: Debian Linux / Stretch / x64... all patched and updated. 

I've thrown out the .bitmonero folder and resynced. The problem remains. I've delete the .bitmonero folder, imported the blockchain.raw from getmonero.org, synced from its block and the problem remains. 

The wallet sync with the remote node just fine. Balance shows fine. All wallet features show fine. 

To debug the problem I started attempting to send payments to my own secondary wallet address. The conditions are: I'll specify the "transfer" command without a payment ID to myself. It'll ask for password. It'll pause for a moment and ask if it's okay to send without a payment ID. Once I confirm it'll sit for 2-3 minutes before coming back with: 

> Error: no connection to daemon. Please make sure daemon is running.

I get the same problem with the version compiled from github.

Client tag:
> Monero 'Lithium Luna' (v0.12.0.0-master-4b728d7d)

Daemon tag:
> Monero 'Lithium Luna' (v0.12.0.0-master-4b728d7d)

Do I need to move to a specific tag or branch to fix this? Or am I an anomaly?

I have debugging related questions. 

* If my node happens to connect to nodes on the minifork when it's syncing will that derail it? 
* If my node happens to be connected to nodes on the minifork when I send a transaction would that cause it to stall and quit? 
* Is there a timeout setting that's giving up on the connection between client and daemon?
* Does the data directory need to be set somewhere speicific for the client or can it be cleared? (e.g. running the client on a live boot and the client's data directory gets cleared between boots)
* Could a blockchain.raw file be pushed on the monero website so that people can deliberately import their way beyond the fork? (if there's a syncing error)

I have vendetta level angst with this problem and am going to poke at it until vanquished.

## littleblackfish | 2018-05-15T20:25:09+00:00
I second this guy, exact same story, but for me every time I attempt a casual transfer, this issue happens, every time I get around to cracking my knuckles in debug-mode, it goes away. Very frustrating. 
Please let me know if I can help zeroing in on it. 

## moneromooo-monero | 2018-05-15T21:02:21+00:00
That seems to be a recent commit, should be fine. Just use release-0.12 to keep up with new commits.
What's a minifork ?
If you're waiting 2-3 minutes, then it's very likely a timeout. Get an all thread stack trace while it's waiting to time out:  gdb /path/to/monerod \`pidof monerod\`. Then, in gdb: thread apply all bt.
The data directory can be removed, but it's unlikely to be the cause. There is a blockchain.raw on the site, updated reguarly AFAIK. In any case, recent code fixes the reorg problem.


## tailswim | 2018-05-15T21:11:18+00:00
+moneromoo - Will do. I'm waiting for a 24,000 block pop command that I issued to put me pre-fork. It's taking awhile. There was something like a 21-25 block fork that occurred on the network (says some reddits/stackexchanges) and part of the nodes on the network are supposedly off on that fork (says the reddits stackexchanges). I'm not sure if there are 0.11 nodes that are being connected to still, but I get a lot of these when the daemon syncs:

> ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1565697

Before I did the block pop it told me the top node was 1573522 so it's strange to me to see alternative blocks still coming up back so far. That's why I went ahead and popped it back but no matter how many times I resync I see a lot of these "ALTERNATIVE" messages. I hadn't even seen a message like it until this last month. 

## moneromooo-monero | 2018-05-15T21:19:28+00:00
If you have recent enough code (and you do), you can ignore this. Alternates happen daily, this one's just longer since some node never reorg'd and continued on its way.


## tailswim | 2018-05-15T21:27:45+00:00
+moneromoo - Question: Could latency between the daemon and peers cause the transactions to time out? e.g. Does the daemon need to talk to peers in real time to solve transaction fees or anything?

I normally have the daemon running transparently over Tor (the Tor proxy config is set at the firewall so that I don't have to wrestle with wrappers). I'm going to run some experimental transactions with and without the transparent proxying to see if the behaviour changes at all in addition to your gdb. 

## moneromooo-monero | 2018-05-15T21:41:57+00:00
P2P peers connections likely don't matter here, though Tor usage might slow down considerably.

## tailswim | 2018-05-15T23:16:05+00:00
+moneromoo - Before I forget to ask I'll ask now. When switching between clearnet to Tor... the official answer is that an identity used by the node in the clearnet should not be used in Tor. Is it enough to clear p2pstate.bin to wipe/reset the identity when switching or is there identifying information in the lmdb as well? e.g. would it be necessary to export the chain, wipe the .bitmonero folders, and then reimport the chain?

## moneromooo-monero | 2018-05-16T09:11:54+00:00
If you mean the peer id, it's reset on every start. There's nothing special in the chain, it's all public information.

## tailswim | 2018-05-17T06:31:26+00:00
+moneromooo - Thanks. Okay, so... chain reset was taking too long so I reverted back to the copy of the chain I was having the problem on. I rebooted the box clean with no other concurrent tasks running and suddenly the problem is gone. I had to follow a similar pattern when the problem first cropped up. When I rebooted the box and shut off everything else (all heavy startup services, etc...) I was able to get one transaction through. 

Right now my suspicion is it has something to do with resource starvation/competition causing the daemon or client to time out at higher probabilities (high enough that more than myself is experiencing it). I'm suspecting it's IO as my concurrent tasks are usually high IO and I've noticed the monero daemon can put itself into high IO states. 

I have the heavy background tasks restarted and will see if I can get the problem to start appearing again and do the gdb trace. Something like IO starvation/competition causing the daemon to timeout transfers could be enough of an edge case to duck release testing (supposing testing occurs on less "noisy" test rigs). 

## tailswim | 2018-05-17T06:49:31+00:00
+moneromooo - It's also worth noting that this is the first time I've seen "REORGANIZE SUCCESS" statements in awhile. I'm spitballing here but can reorgs timeout if IO is taking too long? 

## moneromooo-monero | 2018-05-17T07:31:18+00:00
A large reorg will hold the blockchain lock for a long time, and many RPCs also need that lock, so this is possible.

## tailswim | 2018-05-17T07:54:19+00:00
Okay, it's reproducable on my system. About 15 minutes into the high IO processes and I'm back to a 100% failure rate. I think I know what the problem is too. 

I captured the wallet-cli trace and two monerod traces. Something I note is when attaching gdb to monerod it would take several minutes to attach itself to the halted threads and the wallet gave up with a "Error: no connection to daemon." before gdb could even attach itself for a monerod attachment. 

I note the client stops on a "epoll_wait" under "epee::net_utils::blocked_mode_client::recv".

My guess is that a daemon on a high IO system takes longer to respond than usual and the client gives up and gives us this error. It's possible that littleblackfish's IO is fluctuating up and down causing the error to come and go. 

I've attached the stack traces for the daemon and client (didn't want to clutter this message). 

My question: Can the timeout on the wallet-cli be made a tweakable input parameter? And should the default timeout be set higher to compensate for the higher daemon IO as the chain grows? 

I'm willing to test a higher timeout setting in the wallet for confirmation.
[monero-wallet-cli.txt](https://github.com/monero-project/monero/files/2012140/monero-wallet-cli.txt)
[monerod-run1.txt](https://github.com/monero-project/monero/files/2012141/monerod-run1.txt)
[monerod-run2.txt](https://github.com/monero-project/monero/files/2012142/monerod-run2.txt)




## moneromooo-monero | 2018-05-17T08:18:36+00:00
It's timing out in get_output_histogram. Is your daemon trusted (ie, either local, or --trusted-deamon) ?

## tailswim | 2018-05-17T08:27:47+00:00
+moneromoo - It's a remote daemon but the client thinks it's local (local loopback port forwarded to server by ssh). I added the --trusted-daemon flag with the same error (no connection to daemon). When I shut down the other high IO tasks on the remote server then transfers start working again. So I'm still supposing the daemon takes longer to respond in high IO cases and the client gives up. 

## tailswim | 2018-05-17T16:47:40+00:00
+moneromoo - Update on this. I've noticed that "REORGANIZE SUCCESS" messages have stopped rolling again. I have a lot of "BLOCK ADDED AS ALTERNATIVE" messages but there are no reorgs coming up. I'm doing some testing to see if success messages stop rolling under high IO conditions daemon side. 

## tailswim | 2018-05-17T16:57:44+00:00
+moneromoo - Okay, with high IO tasks off on the server and no "REORGANIZE SUCCESS" messages coming up it took several minutes for the transaction to ask if the transaction fee was acceptable but it did eventually ask. With high IO tasks on the server it just gives up with the "Error: no connection to daemon". I'm not sure if the long window for confirming the transaction fee is normal or not but it does eventually respond if there's no IO competition. 

Edit: Subsequent attempts to send additional transactions prompt for the transaction fee immediately. Is there some kind of internal marker that advances when the first transfer attempt is put through causing subsequent ones to speed up?

## tailswim | 2018-05-17T17:12:57+00:00
The exact conditions for this error appear to be as follows:

* If the daemon has high IO competition: the client can fail with "Error: no connection to daemon. Please make sure daemon is running." - Potential wallet-cli timeout error waiting for daemon communication?

* If the IO drops low enough daemon side for one transaction in wallet-cli to prompt for the transaction fee then subsequent attempts in wallet-cli will also work... apparently even under high IO conditions. Daemon and/or wallet primed for transactions at the new block height?

The above conditions meet what littleblackfish was experiencing as well. e.g. clearing the plate to debug the issue (IO drops?), the daemon then responds timely enough to cause the wallet to prompt for the fee on the first transaction, and then all subsequent transactions work regardless of IO. This would remain true at least until the blockchain advances far enough again and the problem reappears (high IO competition with daemon causing first transfer to repeatedly fail).

Solution appears to be letting the wallet wait longer for daemon communication under high IO circumstances unless the daemon is doing something internally where it rudely hangs up if its own IO takes too long. 

My stopgap solution if anyone else is interested:

> Get the IO as low as possible wherever the daemon is. Prime the wallet/daemon for transactions by attempting to send a transfer to yourself (secondary address). Cancel the transaction when it prompts for accepting the fee. Perform your transactions as normal. 

## littleblackfish | 2018-05-17T18:13:41+00:00
This is very consistent with what I got, my daemon runs on a potato with a spinning drive that also runs litecoind. The times that I got it to work correlate well with fresh reboots (and no litecoind running). 
I also tried to mount the spinning drive to a faster machine over network and run monerod there to no avail. I think this suggests that IO is the bottleneck, not compute. 

## moneromooo-monero | 2018-06-25T21:59:23+00:00
Believed fixed by the new adaptive timeout system. Ropen if it still happens.

+resolved


## kvthweatt | 2022-03-16T10:00:22+00:00
Monero Oxygen Orion v0.17.3
When I don't change anything, it can send and receive from testnet faucet.

2022-03-16 09:41:38.193	    7fe0366e0a00	INFO	net.http	contrib/epee/include/storages/http_abstract_invoke.h:96	Failed to invoke http request to  /get_output_distribution.bin, wrong response code: 500
2022-03-16 09:41:38.193	    7fe0366e0a00	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:14067	!r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-03-16 09:41:38.193	    7fe0366e0a00	WARNING	net.http	src/wallet/wallet_errors.h:896	/home/kvthweatt/uttc/src/wallet/wallet2.cpp:14067:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = /get_output_distribution.bin

When I go to send coins, it disconnects from the daemon (running locally)
I wanted to run my own testnet chain so I cleared the checkpoints and changed the network connection info (ports and such) nothing else

# Action History
- Created by: AJIekceu4 | 2018-05-03T18:38:32+00:00
- Closed at: 2018-06-25T22:16:59+00:00
