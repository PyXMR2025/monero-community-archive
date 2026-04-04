---
title: 'Wallet GUI is stuck (or hangs or deadlocks) on creating transaction '
source_url: https://github.com/monero-project/monero-gui/issues/3349
author: possientis
assignees: []
labels: []
created_at: '2021-03-06T13:30:20+00:00'
updated_at: '2021-04-09T21:34:06+00:00'
type: issue
status: closed
closed_at: '2021-04-09T21:34:06+00:00'
---

# Original Description
I am very sorry I cannot provide a lot of info on this except that it happens repeatedly. There appears to be a transient issue of the Wallet GUI being in a state of deadlock when creating a transaction. When this happens, closing the wallet will rightly ask you whether you wish to keep the local `monerod` running but then it will also spin for ever and I can think of nothing else but to kill the process under linux. Upon restarting the wallet and retrying to send the transaction, it has always been fine so far. So this is not the end of the world, but it would be nice to get rid of problem. I am running:

```
john@front:~$ uname -a
Linux front 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64 GNU/Linux
```
wallet was build from source:
```
john@front:~/Libs/monero-gui$ git status
HEAD detached at v0.17.1.9
nothing to commit, working tree clean
```
The wallet is connected to fully synched local node, also built from source:
```
john@front:~/Libs/monero$ git status
HEAD detached at v0.17.1.9
nothing to commit, working tree clean
```

# Discussion History
## selsta | 2021-03-06T13:31:24+00:00
Do you use a HDD or SSD?

## possientis | 2021-03-06T13:33:08+00:00
HDD

## selsta | 2021-03-06T13:52:55+00:00
How long do you wait during transaction creation? It takes longer on a HDD but I'm not aware of any deadlocks.

## possientis | 2021-03-06T14:37:48+00:00
I probably wait around 2-3 minutes until I call it a day and kill the process. Interestingly, when I restart the wallet and transaction creation is successful (or when transaction creation is successful in the first attempt), it only takes a few seconds (5 seconds at most). Note also that all my transaction creation attempts are on a fully synched wallet and local node.

It seems that other people have experienced this, albeit in different context and different versions as reported by reddit and stackexchange:
[reddit](https://www.reddit.com/r/Monero/comments/8vcdhv/monero_gui_stuck_on_creating_transaction/)
[stackexchange](https://monero.stackexchange.com/questions/6673/stuck-at-creating-transaction)

## selsta | 2021-03-06T18:48:02+00:00
Can you check if you get same behaviour with monero-wallet-cli? If yes you have to open an issue on monero repo as it isn’t GUI related.

## possientis | 2021-03-06T23:13:34+00:00
I only recently switched to `monero-wallet-gui` and used `monero-wallet-cli` extensively before without witnessing the issue. However, if I am honest, I have always downloaded binaries for `monero-wallet-cli` rather than build it from source. So I will now run my own binaries (as I do for `monerod` and `monero-wallet-gui`) and see if the issue appears.

will revert asap

**EDIT**
Ok I am now running `monero-wallet-cli` with binaries build from source (same build as for `monerod`) and I have made 3 payments without noticing any issue. My last two payments on `monero-wallet-gui` I had to kill the process and restart the wallet. This is no proof but it feels to me like the issue is specific to the GUI wallet

## possientis | 2021-04-09T20:41:12+00:00
Actually, if I am honest, it is now clear that the issue may also arise with `monero-wallet-cli` albeit less often. So I am now thinking that you may wish to close this issue because I cannot provide a clear diagnostic or replicate the problem reliably. My wallet is usually running on very cheap hardware with 2 AMD cores on which are running a full `monerod` node as well as a full `bitcoind` node and `firefox`... So whenever I open my monero wallet (be it `cli` or `gui`) the hardware is being stretched and I can see my local `monerod` node struggles to keep up (and everything is HDD). Furthermore, I have set up my local `monerod` node so it only has one single peer (some raspberry Pi4 which is my main gate to the outside world). So my local `monerod` node may disconnect at times and I have seen this happen sometimes when  starting my monero wallet. So long story short, I am now starting to think this whole thing is happening because my local `monerod` node suddenly fails to keep up (hardware being suddenly stretched by opening firefox and wallet, and one single connection to peer). Apologies for hassle. 

## selsta | 2021-04-09T21:34:06+00:00
Thanks for the update. Closing as this does not seem GUI specific.

# Action History
- Created by: possientis | 2021-03-06T13:30:20+00:00
- Closed at: 2021-04-09T21:34:06+00:00
