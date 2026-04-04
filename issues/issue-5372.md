---
title: works  like a snail
source_url: https://github.com/monero-project/monero/issues/5372
author: nuriyevn
assignees: []
labels: []
created_at: '2019-03-30T15:23:36+00:00'
updated_at: '2019-04-04T07:00:07+00:00'
type: issue
status: closed
closed_at: '2019-03-30T16:42:50+00:00'
---

# Original Description
Does someone know how this works  ridiculously slow?  :D it stays for 3 minutes like that.
I am expecting that it will show the amount of blocks left to syncronize, but 15 minutes nothing happens.  Using fiat money I would make 50 transactions , who care about privacy if it works like a snail  :D  a bit criticising monero ))) 
0.13.0.4 version monero gui windows
http://joxi.net/5mdzbw8U31WkoA

# Discussion History
## dEBRUYNE-1 | 2019-03-30T16:38:40+00:00
You're using a wrong, outdated version. I'd advise to upgrade to GUI v0.14.0.0:

https://www.reddit.com/r/Monero/comments/ayshug/gui_v01400_boron_butterfly_released/

## nuriyevn | 2019-03-30T16:42:50+00:00
thanks, I have already made a transaction after updating to 0.14
But it's a bit frustrating that I wait some time and no visible reaction from a wallet gui.
However, it's great, that gui has caught up the blockchain paths correctly after update no need to know where is the local blockchain or password for a wallet and etc.
By the way, where is the local blockchain directory? 
Windows 10 

## setuidroot | 2019-03-30T17:35:06+00:00
Yes, I can answer why, but I need more information for your usage case; it looks like you are using a remote node to sync your wallet, no?

Remote nodes are servers run by generous people who let you download/sync the blockchain for free.  They are like seeders in torrenting.  They run a (public) remote node, which cost them server bandwidth and CPU cycles to help people who don't run their own nodes (for whatever reason.)  If you can run your own node (ie it's not illegal in your country (even if it was, you could run your own private node using a VPN and/or Tor, i2p, SOCKs proxies to synchronize it; but if you're not technically inclined and 100% confident you know how to do that and stay anonymous, don't risk it; use remote nodes that others provide for your safety.))

If you don't live in an insanely repressive country and you have a decent computer with at least 4GB of RAM, ~100GB storage (~75GB free preferred) and 2 CPU cores (CPU manufactured 2011 or newer would work well.)  I'd recommend you run your own private Monero node (they have a guide on how to do that here: https://www.monero.how/how-to-run-monero-node)

You should run your own node for increased privacy and it also helps out the network because when you run your node (you don't have to run it 24/7) then you'll be contributing to other nodes (seeding/uploading) while updating your copy of the blockchain from other peers (leaching/downloading.)  Setting up your own node will take 24 (or more) hours if you sync from scratch; but you can download a snapshot of the blockchain and import it so you'll only need to update the latest blocks.  (Guide for that here: https://www.monero.how/tutorial-how-to-speed-up-initial-blockchain-sync)

To answer your question, if you're using a remote node (which from the picture link you posted it appears that you are) then your speed of synchronizing the blockchain is limited by the remote node's CPU, bandwidth and other bottlenecks.  Also it looks like you already synchronized the blockchain witj a remote node and you're asking why does it take so long to work after you finish synchronizing with your remote node.  The answer is limitations of your own hardware as your computer has to verify and read through the blocks you received from your remote node.  If you use CLI (I've never used a GUI, so I'm not familiar sorry) with a remote node it shows you the blocks it's synchronized with the remote node and when finished it shows (in CLI) it scanning all of the blocks as it's looking through them for any transactions dealing with your wallet.  

TL;DR answer: 

I think this is the answer to your question, after you use a remote node to synchronize a copy of the blockchain, your computer scans all of those blocks looking for transactions pertaining to your wallet(s.)  I assume the GUI doesn't show this scan time graphically and thus you're confused, thinking it might be frozen, but I assure you it is not.

Also (I just assume) but make sure you're running the latest (post-fork) wallet from getmonero.org/downloads

:/ ah I typed all this up and didn't realize you were using old wallet version.  I'm posting this hoping it might help other people.

## dEBRUYNE-1 | 2019-03-30T19:58:56+00:00
>By the way, where is the local blockchain directory?

`C:\ProgramData\bitmonero\lmdb`

Note that, by default, this directory is hidden. You should, however, be able to easily navigate to it by pasting aforementioned path into the Windows Explorer bar. 

## nuriyevn | 2019-03-31T10:54:28+00:00
thanks for very 

>  I assume the GUI doesn't show this scan time graphically and thus you're confused, thinking it might be frozen, but I assure you it is not.

Yes, exactly, there was no progress at all. And that's a bit confusing. If it's an old version the software should propose a working version of an update.

But , yes, just need to update, simply that :)

## kayront | 2019-04-04T07:00:07+00:00
@setuidroot: The issue is that at least for me this slowness manifests even with a node running on the local network, and in a situation where there is no saturation of disk, network or memory on either client or server.

Every single time without fail, here is what happens:

1. start wallet, input password.

2. long (5-10+ sec) delay until anything comes up after "Starting refresh..."

3. A pattern were a few hundred blocks are refreshed, then the count stalls for 20+ seconds, rinse and repeat.

4. Eventually it gets refreshed. Now every time I type something in simplewallet, the prompt hangs and feels sluggish, I guess because there is no dedicated network thread on the client (haven't checked at all) - and keep in mind, this is on a LAN. With remote nodes, it's much, much worse.

5. Time to make a transfer, maybe! Server will stall for 10+ seconds looking for decoy outputs, even when it's not at all or hardly hitting the disks (data was already in OS buffer cache).

5.a: It's even worse if I concurrently run a second and/or a third wallet from other computers, then THEIR refreshes and TXs will stall for even longer, and ALL monero-wallet-cli get even more sluggish.

I've brought this issue up repeatedly, tbh find it hard to believe it's just me - we're talking 3 different operating systems involved, and a gigabit connection with a server that's idling 100% and yet struggling to return some data that was cached in RAM.


# Action History
- Created by: nuriyevn | 2019-03-30T15:23:36+00:00
- Closed at: 2019-03-30T16:42:50+00:00
