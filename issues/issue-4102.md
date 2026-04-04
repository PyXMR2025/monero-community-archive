---
title: Daemon on Monero GUI wallet is unable to sync
source_url: https://github.com/monero-project/monero-gui/issues/4102
author: ch9PcB
assignees: []
labels: []
created_at: '2023-01-16T04:06:35+00:00'
updated_at: '2023-01-18T04:17:53+00:00'
type: issue
status: closed
closed_at: '2023-01-18T04:17:53+00:00'
---

# Original Description
I have been running Monero GUI wallet for almost a year already with no issues, including the current version, 0.18.1.2.

Using Monero GUI wallet, I have been able to sync, receive and spend my XMR without issues.

Last Christmas, one of my family members gifted me a brand new laptop computer.

I decided to transfer my Monero GUI wallet, including the updated lock.mdb and pruned data.mdb from my old computer to my new one.

The settings, password, path to blockchain on my new computer are identical to those on my old one.

The relevant details on both my old and new computers are:

Debian 11.6, 64-bit updated with latest security fixes
LXQt minimal install
Monero GUI wallet, monero-gui-linux-x64-v0.18.1.2.tar.bz2
Local node connecting to Mainnet

After launching Monero-GUI, the daemon on my new computer is unable to sync (see attached error log)

[error log - bitmonero.log of 15.01.2023.txt](https://github.com/monero-project/monero-gui/files/10422392/error.log.-.bitmonero.log.of.15.01.2023.txt)

The strange thing is that I am able to sync if I launch monerod in a terminal such as:

./monerod

I appreciate your help in resolving the issue.

# Discussion History
## selsta | 2023-01-16T04:43:30+00:00
When you manually launch monerod from the terminal did you add `--data-dir /path/to/blockchain` ? 

## ch9PcB | 2023-01-16T07:29:02+00:00
> When you manually launch monerod from the terminal did you add `--data-dir /path/to/blockchain` ?

Yes, I did.

In fact, the first time I launched `monerod` in a terminal, I added the following parameters:

`./monerod --data-dir /path/to/blockchain --prune-blockchain --ban-list block.txt`

Immediately there was an error message about unrecognized option `--ban-list` 

On the second attempt, I launched `monerod` in a terminal with two parameters:

`./monerod --data-dir /path/to/blockchain --prune-blockchain`

And `monerod` was able to sync and picked up where I last synced on my old computer, meaning I did not have to download the entire blockchain.



## selsta | 2023-01-16T07:31:29+00:00
The error log you shared doesn't have anything interesting. What happens exactly? Does the daemon fail to start? Does it start but stay stuck?

## ch9PcB | 2023-01-17T11:08:59+00:00
@selsta

> The error log you shared doesn't have anything interesting.

I'm sorry that you couldn't glean anything useful from bitmonero.log Perhaps you could ask the developer in charge to improve the software's error-handling code?

> What happens exactly? Does the daemon fail to start?

Yes, the daemon of Monero GUI wallet failed to start (see attached screenshot).
![Couldn't connect to daemon](https://user-images.githubusercontent.com/24192216/212883617-b7ca53f9-5e79-4808-a4f7-9ff56ec8e464.png)

> Does it start but stay stuck?

No, the daemon completely failed to start.



## selsta | 2023-01-17T14:20:10+00:00
Can you go to Settings -> Node and post a screenshot here?

## ch9PcB | 2023-01-17T17:58:32+00:00
@selsta 

> Can you go to Settings -> Node and post a screenshot here?

Here it is

![selsta01](https://user-images.githubusercontent.com/24192216/212975779-bbe306e1-c064-4769-b0e9-0b263fbd2f17.png)


## selsta | 2023-01-17T18:06:56+00:00
Try to remove your daemon startup flags. As you said in your previous comment you have issues with the ban-list flag so that's likely the issue.

You can also remove `--prune-blockchain` since your blockchain is already pruned.

## ch9PcB | 2023-01-18T01:13:39+00:00
@selsta 

> Try to remove your daemon startup flags. As you said in your previous comment you have issues with the ban-list flag so that's likely the issue.

OK, per your suggestion, I removed the daemon startup flags.

The daemon on my new computer was able to sync with Mainnet; moreover the daemon was able to sync from the last block before the transfer of data.mdb and lock.mdb from my old computer to the new one.

Question 1: On my old computer, the daemon is able to sync even with the daemon startup flags `--prune-blockchain` and `--ban-list`. Why is that so?

Question 2: On my new computer, the daemon startup flag `--ban-list block.txt` is removed. Is there a way to prevent my computer from connecting to malicious nodes?

## selsta | 2023-01-18T01:19:53+00:00
> Question 1: On my old computer, the daemon is able to sync even with the daemon startup flags --prune-blockchain and --ban-list. Why is that so?

It's likely that you didn't copy the block.txt file to the correct location, so it doesn't find block.txt and fails to start.

> Question 2: On my new computer, the daemon startup flag --ban-list block.txt is removed. Is there a way to prevent my computer from connecting to malicious nodes?

Adding any flags isn't necessary with any recent versions of monero but you can add `--enable-dns-blocklist` instead, then you don't have to manually specify a file.

## ch9PcB | 2023-01-18T04:17:40+00:00
@selsta

> but you can add `--enable-dns-blocklist` instead, then you don't have to manually specify a file.

Thanks.

I think that using the startup flag `--enable-dns-blocklist` is way neater and less time consuming than creating a text file called `block.txt` and inputting some IP addresses in it.

I will close this comment.


# Action History
- Created by: ch9PcB | 2023-01-16T04:06:35+00:00
- Closed at: 2023-01-18T04:17:53+00:00
