---
title: Monero GUI Wallet Shows 0.00000  Balance After Deposit
source_url: https://github.com/monero-project/monero/issues/6711
author: bluestim
assignees: []
labels: []
created_at: '2020-07-17T16:05:40+00:00'
updated_at: '2020-07-17T17:50:43+00:00'
type: issue
status: closed
closed_at: '2020-07-17T17:50:14+00:00'
---

# Original Description
Hello Monero-project Community,

I also posted this on the Monero Reddit but thought I should post this here also.

I've spent a good amount of the past 2 weeks trying to figure out how to setup and use Tails with persistent storage with Monero GUI v0.16.0.2 running a local node on an external drive. I've tried to learn all I can about getting this setup on my own but when I sent some XMR to my Monero GUI Wallet it is still showing no balance. I'm sure it's going to the correct wallet and verified payment on: https://xmr.llcoins.net/checktx.html.

I followed dEBRUYNE's very thorough troubleshooting steps here: https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance and every thing for the most part checks out but it is still not working. :(

I also tried to use a few other guides out there and tried to run this command in the Terminal: 'sudo iptables -I OUTPUT 2 -p tcp -d 127.0.0.1 -m tcp --dport 18081 -j ACCEPT' which seems necessary for the local node to starting synchronizing.

The bottom left corner shows 'Connected' and'Wallet is synchronized','Daemon is synchronized' with the orange bars full like its completed.

When I run the 'Status' command under the Settings > Log tab it shows the two Height #'s match and 100.0% on mainnet,not mining, net hash 1.74 GH/s, v12.. but this part of the information doesn't look right to me, it's showing: 0(out)+0(in) connections. I also for some reason can't connect to any remote nodes. The last one I've tried is: node.moneroworld.com port:18089

With the risk of turning this post into a novel I've found my height on blockchain explorer XMRchain. I've renamed my Monero wallet file so it rebuilt itself, changed the Wallet restore height to: 1740000 so the Wallet rebuilt itself a 2nd time but still noooo luck.

I've tried to include all the important information but might've missed some stuff.

If I can some help from this community to solve this I would super greatly appreciate it. I've been beating myself upside my head trying to figure this out. halp.

# Discussion History
## bluestim | 2020-07-17T17:50:42+00:00
Issue may possibly be resolved through post.

# Action History
- Created by: bluestim | 2020-07-17T16:05:40+00:00
- Closed at: 2020-07-17T17:50:14+00:00
