---
title: Pruned Node Language and Bootstrap Mode
source_url: https://github.com/monero-project/monero-site/issues/2031
author: PicoDeNero
assignees: []
labels:
- 💬 discussion
- 📖 moneropedia
created_at: '2022-08-25T16:54:48+00:00'
updated_at: '2022-08-29T09:29:32+00:00'
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
## PicoDeNero | 2022-08-25T17:09:12+00:00
This originally came to my attention through a conversation I had with @dEBRUYNE-1 on reddit back in April. https://www.reddit.com/r/monerosupport/comments/tp8yno/comment/i2ggy5z/

There are a lot of people posting regularly on r/MoneroSupport and r/Monero asking about pruning their local nodes or running a pruned node, [as recently as yesterday](https://www.reddit.com/r/Monero/comments/wwfnvn/can_i_download_a_pruned_version_of_the_blockchain/). **Monero users at large do not realize that the boostrap mode creates a local pruned node by default**, though many are interested in running pruned nodes. Also, in some cases, this has resulted in some confusion when users try to prune later on.

Generally, I think having pruned nodes by default is a really great feature, but there needs to be more publicly available and digestible information out there about it.

# Action History
- Created by: PicoDeNero | 2022-08-25T16:54:48+00:00
