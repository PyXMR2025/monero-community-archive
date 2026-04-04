---
title: Pruned Node Language and Bootstrap Mode
source_url: https://github.com/monero-project/monero-gui/issues/4015
author: PicoDeNero
assignees: []
labels: []
created_at: '2022-08-25T16:55:01+00:00'
updated_at: '2022-08-28T18:50:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
To quote @rating89us, "Since https://github.com/monero-project/monero-gui/pull/3345, simple (bootstrap) mode now syncs a pruned blockchain from scratch." This was back in 2021.

Looking around, neither the GUI, the GUI Guide, nor the website mention anything about this. 

The GUI does have a pending issue about it: https://github.com/monero-project/monero-gui/pull/3408

I respectfully disagree, but understand selsta's concern that "[A simple mode user doesn't have to know what pruning is](https://github.com/monero-project/monero-gui/pull/3408#pullrequestreview-929716510)." in regards to the language that appears in the GUI itself. **However, IMHO, people who go looking for more detailed information about pruned nodes/bootstrap mode on Moneropedia or in the GUI guide should be able to find it.**

The Moneropedia page on the website has at least one article that should _probably_ be updated:
- (pruning) https://github.com/monero-project/monero-site/blob/master/_i18n/en/resources/moneropedia/pruning.md

The GUI Guide has at least two chapters that should _probably_ be updated too:
- Chapter 1 (choose-wallet-mode) https://github.com/monero-ecosystem/monero-GUI-guide/blob/master/en/ch01.md#choose-wallet-mode
- and Chapter 11 (Bootstrap nodes) https://github.com/monero-ecosystem/monero-GUI-guide/blob/master/en/ch11.md

Note: I almost never use Github, don't know what the hell I'm doing, just copy/pasting this in Monero-Site and GUI. Hoping someone who does know what they are doing can take this from here.

# Discussion History
## PicoDeNero | 2022-08-25T17:09:04+00:00
This originally came to my attention through a conversation I had with @dEBRUYNE-1 on reddit back in April. https://www.reddit.com/r/monerosupport/comments/tp8yno/comment/i2ggy5z/

There are a lot of people posting regularly on r/MoneroSupport and r/Monero asking about pruning their local nodes or running a pruned node, [as recently as yesterday](https://www.reddit.com/r/Monero/comments/wwfnvn/can_i_download_a_pruned_version_of_the_blockchain/). **Monero users at large do not realize that the boostrap mode creates a local pruned node by default**, though many are interested in running pruned nodes. Also, in some cases, this has resulted in some confusion when users try to prune later on.

Generally, I think having pruned nodes by default is a really great feature, but there needs to be more publicly available and digestible information out there about it.

## selsta | 2022-08-26T00:06:12+00:00
I don't know I feel like there will always be issues. If a users reads "pruned" node in simple mode and he doesn't know what that exactly means he gets unnecessary confused. We try to hide as much information as possible in simple mode.

The easiest way to get a pruned node currently is to use advanced mode and then select pruned node during daemon settings. Manually adding `--prune-blockchain` is not recommended.

<img width="841" alt="Screenshot 2022-08-26 at 01 59 06" src="https://user-images.githubusercontent.com/7697454/186789180-48114aa4-c15e-45bc-b12a-6d980e2c2805.png">

## PicoDeNero | 2022-08-28T18:46:44+00:00
Hi selsta. Thanks for taking the time to reply! I agree that these things can cause confusion with users, but shouldn't the language in the Monero GUI guide PDF and on the website at least be updated?

That way, if someone is just using the GUI, they won't get confused, but if they actively go looking for more information, they can find it.

For example, I really appreciate you sharing the new advanced mode checkbox feature to prune the blockchain. That is awesome!... and it is also a feature that I totally missed and is not mentioned anywhere that I can see (please correct me if I am wrong). The only language that even comes close to addressing this in the Monero Guide PDF packaged with v0.18.1.0 is the following:

> "If you run a local node as a full node with a bootstrap node (requires wallet in “simple mode (bootstrap)”),
> your wallet daemon will also download the blockchain file into your computer, but it will connect to a remote
> node (a bootstrap node) while the download is not finished, allowing you to immediately send/receive a
> transaction.
> If you want to run a local node as a pruned node, see [this guide](https://monero.stackexchange.com/questions/11454/how-do-i-utilize-blockchain-pruning-in-the-gui-monero-wallet-gui)."

The linked guide is a post on stackexchange made by @dEBRUYNE-1 in 2019. It is great, but as @selsta pointed out, it is now outdated.

I concede that including "pruned node" language in the GUI could be confusing to users, but IMHO Monero users shouldn't have to go to reddit or stackexchange to get information about pruned nodes and how to use them. Getmonero.org and the pdf guide should be updated.

# Action History
- Created by: PicoDeNero | 2022-08-25T16:55:01+00:00
