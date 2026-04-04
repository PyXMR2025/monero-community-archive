---
title: 'Proposal: Sort the FAQ by more specific themes'
source_url: https://github.com/monero-project/monero-site/issues/2006
author: apertamono
assignees: []
labels:
- enhancement
- FAQ
created_at: '2022-07-26T15:19:20+00:00'
updated_at: '2023-06-06T18:50:57+00:00'
type: issue
status: closed
closed_at: '2023-06-06T18:50:57+00:00'
---

# Original Description
The FAQ has grown over the years, and with 38 questions, it needs more structure than the three current categories General, Advanced and Node and Wallet. The first two categories are meaningless anyway. After I saw a PR for a script that sorts the questions alphabetically, at least in English, in #1969, I thought there must be a better way. Let's use more specific categories, so we can group a handful of Q&A's in each, while users can quickly find the topic they're interested in.

What do you think of the following structure? I also cleaned up the grammar here and there.


## Basics

* How can I get Monero?
* Why is Monero called 'Monero'?
* How is Monero different from Bitcoin?
* What's the meaning of [technical word]?
* Are there videos I can watch to learn about Monero?
* Is it true that Monero has a hard fork every 6 months?
* Does Monero have a block size limit?
* How can I contribute?


## Privacy

* How is Monero’s privacy different from other coins?
* Is Monero magic and does it protect my privacy no matter what I do?
* Is Monero 100% anonymous?
* Is Monero a mixer or mixing service?
* (Proposed in #1766:) What is Dandelion++?
* (Proposed in #1887:) What if my transaction was mined in a block containing only two transactions?


## Security

* Why is my antivirus/firewall flagging the Monero software I just downloaded as malware?
* What is ASIC resistance? Why is it important?
* Are there known vulnerabilities in Monero?
* (Proposed in #1783:) I've been hit by a ransomware and they want me to pay a ransom in Monero. What can i do?


## Economics

* How does Monero have value?
* What is fungibility, and why is it important?
* What is Monero's maximum supply?
* (Proposed in #1965, maybe redundant:) Why doesn't Monero have a maximum supply?
* If Monero is so private, how do we know coins aren't being created out of thin air?
* (Proposed in #1792:) Does Monero support Atomic Swaps?


## Wallets

* Which wallet should I use?
* What is the difference between a light wallet and a normal wallet?
* I can't see my funds. Did I just lose all my Monero?
* I haven't touched my Monero in a long time, did I lose my coins due to a network upgrade?
* Why is my wallet taking so long to sync?
* Why does my wallet need to scan the blockchain everytime I open it?


## Node

* How do I decide if I should run a full node or a pruned node?
* How big is the Monero blockchain?
* Why does the blockchain need so much space?
* Can I avoid downloading the entire blockchain?
* Can I manually import the blockchain?
* How can I connect my node via Tor?
* Is it dangerous to run a personal node?
* Is it dangerous to use a remote node? What's the data a node operator can get from me?


# Discussion History
## erciccione | 2022-08-08T09:14:42+00:00
Thanks @ProkhorZ this sounds like a very good suggestions. I would change "Wallet" to "Wallets" and replace "Node" with something else, but it's definitely a very good start.

## apertamono | 2022-08-08T09:48:27+00:00
Thanks for the feedback, @erciccione. Would you prefer to split the 'Node' segment into 'Network' and 'Blockchain'? 

I'll wait for more comments before making a PR, and I still need to ask for that on the various channels.

## HardenedSteel | 2022-09-12T12:23:24+00:00
Replacing node with network sounds good for me.

# Action History
- Created by: apertamono | 2022-07-26T15:19:20+00:00
- Closed at: 2023-06-06T18:50:57+00:00
